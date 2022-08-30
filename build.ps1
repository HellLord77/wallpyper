$Version = "0.1.0"

$Datas = @(
"modules\res"
"res"
"win32\syspin.exe")
$Imports = @(
"configparser"
"filecmp"
"gui"
"langs"
"webbrowser"
"xml.etree"
"libs.files"
"libs.log"
"libs.pyinstall"
"libs.request"
"libs.singleton"
"libs.timer"
"libs.utils"
"modules")
$Excludes = @()
$HooksDirs = @("hooks")
$Debug = $False
$EntryPoint = "src\init.py"
$Icon = "src\res\icon.ico"
$Manifest = "" # FIXME https://stackoverflow.com/questions/13964909/setting-uac-to-requireadministrator-using-pyinstaller-onefile-option-and-manifes
$NoConsole = $True
$Obfuscate = $False
$OneFile = $True
$OptimizationLevel = 2
$UPX = $False
$MainManifest = "manifest.xml"
$AddPython = $False
$CythonizeGlobs = @(
"src\libs\{colornames,iso}\__init__.py"
"src\libs\{cythonizer,files,pyinstall,singleton,timer}.py"
"src\{consts.init,main}.py")
$CythonizeCleanup = $True
$CodeRunBefore = @(
"from src.libs.ctyped.interface import _dump_pickle"
"_dump_pickle()")
$CodeRunAfter = @(
"from os import remove"
"remove('src\libs\ctyped\interface.pickle')")
$MinifyJsonRegExs = @(
"src\libs\colornames\colornames.min.json",
"src\libs\iso\iso_*.json")

$MegaURL = "https://mega.nz/MEGAcmdSetup64.exe"
$CodePythonBase = @(
"from sys import base_prefix"
"print(base_prefix)")
$CodeExtSuffix = @(
"from sysconfig import get_config_var"
"print(get_config_var('EXT_SUFFIX'))")
$CodeGlobTemplate = @(
"from Cython.Build.Dependencies import extended_iglob"
"print(';'.join(extended_iglob(r'{0}')))")

$IsGithub = Test-Path Env:GITHUB_REPOSITORY

function Get-ProjectName
{
    return Split-Path $( if ($IsGithub)
    {
        $Env:GITHUB_REPOSITORY
    }
    else
    {
        Split-Path -Path (Get-Location) -Leaf
    } ) -Leaf
}

function Start-Base64Process([String] $Base64, [String] $Args = "")
{
    $TempFile = New-TemporaryFile
    [IO.File]::WriteAllBytes($TempFile,[Convert]::FromBase64String($Base64))
    Start-Process $TempFile -ArgumentList $Args -Wait
    $TempFile.Delete()
}

function Get-ExeSize([System.IO.FileStream] $Stream)
{
    $Buffer = [byte[]]::New(4096)
    $Stream.Read($Buffer, 0, 4096) | Out-Null
    $HeaderOffset = [System.BitConverter]::ToInt32($Buffer, 60)
    $HeadersSize = 248
    if ([System.BitConverter]::ToUInt16($Buffer, $HeaderOffset + 4) -eq 0x8664)
    {
        $HeadersSize += 16
    }
    $SectionCount = [System.BitConverter]::ToUInt16($Buffer, $HeaderOffset + 6)
    $MaxPointer = 0
    $Size = 0
    for ($i = 0; $i -lt $SectionCount; $i++) {
        $SectionOffset = $HeaderOffset + $HeadersSize + $i * 40
        $RawDataPointer = [System.BitConverter]::ToInt32($Buffer, $SectionOffset + 20)
        if ($RawDataPointer -gt $MaxPointer)
        {
            $MaxPointer = $RawDataPointer
            $Size = $MaxPointer + [System.BitConverter]::ToInt32($Buffer, $SectionOffset + 16)
        }
    }
    return $Size
}

function MergeManifest([String]$ExePath, [String]$ManifestPath)
{
    $TempFile = New-TemporaryFile
    Copy-Item $ExePath -Destination $TempFile
    .\mt.exe -updateresource:"$ExePath;#1" -manifest "$ManifestPath" -nologo -verbose
    $TempStream = [System.IO.File]::OpenRead($TempFile)
    $ExeStream = [System.IO.File]::OpenWrite($ExePath)
    $TempStream.Seek($( Get-ExeSize $TempStream ), [System.IO.SeekOrigin]::Begin) | Out-Null
    $ExeStream.Seek(0, [System.IO.SeekOrigin]::End) | Out-Null
    $TempStream.CopyTo($ExeStream)
    $ExeStream.Close()
    $TempStream.Close()
    $TempFile.Delete()
}

function Get-MainArgs
{
    $Args = @("--noconfirm")
    if ($OneFile)
    {
        $Args += "--onefile"
    }
    if ($Debug)
    {
        $NoConsole = $False
        $Args += "--debug=all"
    }
    if ($NoConsole)
    {
        $Args += "--windowed"
    }
    if ($Manifest)
    {
        $Args += "--manifest=$Manifest"
    }
    if ($Icon)
    {
        $Args += "--icon=$Icon"
    }
    foreach ($Import in $Imports)
    {
        $Args += "--hidden-import=$Import"
    }
    foreach ($Exclude in $Excludes)
    {
        $Args += "--exclude-module=$Exclude"
    }
    foreach ($HooksDir in $HooksDirs)
    {
        $Args += "--additional-hooks-dir=$HooksDir"
    }
    if ($AddPython)
    {
        $Args += "--add-data=""$( Join-Path (Get-PythonResult $CodePythonBase) "python.exe" );."""
    }
    $BaseSrcDir = Split-Path (Split-Path $EntryPoint -Parent) -Leaf
    foreach ($Data in $Datas)
    {
        $SrcLeaf = Split-Path $Data -Leaf
        if ($SrcLeaf.EndsWith("%") -and $SrcLeaf.EndsWith("%"))
        {
            $DataSrc = (Get-Command $SrcLeaf.Substring(1, $SrcLeaf.Length - 2)).Path
            $DataDst = Split-Path $Data -Parent
        }
        else
        {
            $DataSrc = Join-Path $BaseSrcDir $Data
            if (Test-Path $DataSrc -PathType Leaf)
            {
                $DataDst = Split-Path $Data -Parent
            }
            else
            {
                $DataDst = $Data
            }
        }
        $Args += "--add-data=""$DataSrc;$DataDst""" -Replace "\\", "\\"
    }
    if ($UPX)
    {
        if (!(Get-Command upx -ErrorAction SilentlyContinue))
        {
            choco install upx --verbose --yes
        }
        Get-Command upx
    }
    else
    {
        $Args += "--noupx"
    }
    return $Args
}

function Get-PythonResult([string[]]$Lines)
{
    $Code = $Lines -Join "; "
    Write-Host "python <- $Code"
    return python -c $Code
}

function MinifyJsonFile([string]$Path, [string]$OutPath)
{
    if (-not$OutPath)
    {
        $OutPath = $Path
    }
    Write-Host "Minify $Path -> $OutPath"
    ConvertFrom-Json (Get-Content -Raw $Path) | ConvertTo-Json -Compress | Set-Content $Path
}

function Install-Dependencies
{
    python -m pip install pip --upgrade
    python -m pip install setuptools --upgrade

    if ($Obfuscate)
    {
        pip install pyinstaller --upgrade
        pip install pyarmor --upgrade
    }
    else
    {
        pip install wheel --upgrade
        # $Temp = Join-Path $Env:TEMP (Get-Random) FIXME https://github.com/pyinstaller/pyinstaller/issues/4824
        $Temp = Join-Path (Split-Path (Get-Location) -Qualifier) ([System.IO.Path]::GetRandomFileName())
        New-Item $Temp -ItemType Directory
        Push-Location $Temp
        pip download pyinstaller --no-deps --no-binary pyinstaller
        $Source = (Get-ChildItem -Attributes Archive).FullName
        tar -xvf $Source
        Set-Location $Source.Substring(0, $Source.Length - ".tar.gz".Length)
        Remove-Item (Join-Path "PyInstaller" "bootloader") -Force -Recurse
        python setup.py build install
        Pop-Location
        Remove-Item $Temp -Force -Recurse
    }
    if ($CythonizeGlobs)
    {
        pip install cython --pre # FIXME https://github.com/cython/cython/milestone/58
    }

    if (Test-Path requirements.txt -PathType Leaf)
    {
        pip install -r requirements.txt
    }
}

function Write-Build
{
    if ($CodeRunBefore)
    {
        Get-PythonResult $CodeRunBefore
    }

    if ($IsGithub)
    {
        foreach ($MinifyJsonRegEx in $MinifyJsonRegExs)
        {
            foreach ($Json in  Get-ChildItem -Path . -Filter $MinifyJsonRegEx)
            {
                MinifyJsonFile $Json.FullName
            }
        }
    }

    $MainArgs = Get-MainArgs
    if ($CythonizeGlobs)
    {
        cythonize -3 --inplace $CythonizeGlobs
    }

    $Name = Get-ProjectName
    $VersionLine = Get-Content $EntryPoint | Select-String -Pattern "__version__.\s*=\s*['`"].*['`"]"
    $FullName = "$Name-$( if ($VersionLine)
    {
        ($VersionLine -split { $_ -eq '''' -or $_ -eq '"' })[1]
    }
    else
    {
        "X.Y.Z"
    } )"
    "NAME=$FullName" >> $Env:GITHUB_ENV

    $AddArgs = "--clean", "--name=$FullName", $EntryPoint
    $env:PYTHONOPTIMIZE = $OptimizationLevel
    if ($Obfuscate)
    {
        pyarmor @("pack", "--output=dist", "--options=$MainArgs") $AddArgs
    }
    else
    {
        pyinstaller $MainArgs $AddArgs
    }

    $DistPath = Join-Path "dist" $FullName
    if ($OneFile)
    {
        $ExePath = "$DistPath.exe"
    }
    else
    {
        $ExePath = Join-Path $DistPath "$Name.exe"
        Move-Item (Join-Path $DistPath "$FullName.exe") $ExePath -Force
    }

    if ($CythonizeCleanup)
    {
        $ExtSuffix = Get-PythonResult $CodeExtSuffix
        foreach ($CythonizeGlob in $CythonizeGlobs)
        {
            $CodeGlob = @() + $CodeGlobTemplate
            $CodeGlob[1] = $CodeGlob[1] -f $CythonizeGlob
            $Files = Get-PythonResult $CodeGlob
            foreach ($File in $Files -Split ";")
            {
                $Root = $File.Substring(0,$File.LastIndexOf("."))
                Remove-Item "$Root.c" -Force
                Remove-Item "$Root$ExtSuffix" -Force
            }
        }
    }

    if ($MainManifest)
    {
        MergeManifest $ExePath $MainManifest
    }

    if ($CodeRunAfter)
    {
        Get-PythonResult $CodeRunAfter
    }
}

function UploadToMEGA
{
    if ($env:MEGA_USERNAME -and $env:MEGA_PASSWORD)
    {
        # choco install megacmd --verbose --yes FIXME Error retrieving packages from source
        $Temp = Join-Path $Env:TEMP (Split-Path $MegaURL -Leaf)
        Invoke-WebRequest $MegaURL -OutFile $Temp
        Start-Process $Temp "/S" -Wait
        Remove-Item $Temp -Force
        $env:PATH += ";$( Join-Path $env:LOCALAPPDATA "MEGAcmd" )"
        mega-login $env:MEGA_USERNAME $env:MEGA_PASSWORD
        mega-put dist (Join-Path "$( Get-ProjectName )-cp$( $env:PYTHON_VERSION -Replace "\.", """" )" ((Get-Date -Format o -AsUTC) -Replace ":", "."))
    }
    else
    {
        throw
    }
}

$ErrorActionPreference = "Stop"
if ($Args)
{
    switch ($Args[0])
    {
        "install" {
            Install-Dependencies; Break
        }
        "build" {
            Write-Build; Break
        }
        "upload" {
            UploadToMEGA; Break
        }
        Default {
            throw
        }
    }
    Invoke-Expression $Args[0]
}
else
{
    Write-Build
}
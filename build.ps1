$Version = "0.1.0"

$Datas = @(
"modules\res"
"res"
"win32\syspin.exe")
$Imports = @()
$Excludes = @()
$HooksDirs = @("hooks")
$OptimizationLevel = 2
$Debug = $False
$NoConsole = $True
$Obfuscate = $False
$OneFile = $True
$UPX = $False
$ModuleGraph = $True
$AddPython = $False
$EntryPoint = "src\init.py"
$Icon = "src\res\icon.ico"
# $Manifest = "manifest.xml" FIXME https://stackoverflow.com/questions/13964909/setting-uac-to-requireadministrator-using-pyinstaller-onefile-option-and-manifes
$Manifest = ""
$MainManifest = "manifest.xml"
$CythonizeGlobs = @(
"src\libs\{colornames,iso}\__init__.py"
"src\{langs,libs,modules,win32}\*.py"
"src\{consts.init,main}.py")
$CythonizeRemove = $True
$CodeRunBefore = @(
"from src.libs.ctyped.interface import _dump_pickle"
"_dump_pickle()")
$CodeRunAfter = @(
"from os import remove"
"remove('src\libs\ctyped\interface.pickle')")
$MinifyJsonRegExs = @(
"src\libs\colornames\colornames.min.json", "src\libs\iso\iso_*.json")

$CodePythonBase = @(
"from sys import base_prefix"
"print(base_prefix)")
$CodeExtSuffix = @(
"from sysconfig import get_config_var"
"print(get_config_var('EXT_SUFFIX'))")
$CodeGlobTemplate = @(
"from Cython.Build.Dependencies import extended_iglob"
"print(';'.join(extended_iglob(r'{0}')))")
$CodeModuleGraphTemplate = @(
"from itertools import islice"
"from sys import argv"
"from PyInstaller.lib.modulegraph.__main__ import create_graph, parse_arguments"
"from PyInstaller.lib.modulegraph.modulegraph import ExcludedModule"
"argv.append(r'{0}')"
"options = parse_arguments()"
"graph = create_graph(options.scripts, options.domods, options.debug, options.excludes, options.addpath)"
"print(';'.join(m.identifier for m in islice(graph.iter_graph(), 1, None) if not isinstance(m, ExcludedModule)))")
$CodeModuleGraphSmartTemplate = @(
"from sys import path"
"from PyInstaller.building.build_main import Analysis, initialize_modgraph"
"from PyInstaller.config import CONF"
"path.append(r'{0}')"
"CONF['workpath'] = r'{0}'"
"analysis = Analysis.__new__(Analysis)"
"graph = initialize_modgraph(r'{0}'.split(), r'{1}'.split(';') if r'{1}' else [])"
"graph.add_script(r'{0}')"
"graph.process_post_graph_hooks(analysis)"
"print(';'.join(module.identifier for module in graph.iter_graph()))")
$CopyTimeout = 5
$ModuleGraphSmart = $True
$CythonizeRemoveC = $False
$MegaURL = "https://mega.nz/MEGAcmdSetup64.exe"

$IsGithub = Test-Path Env:GITHUB_REPOSITORY

function Get-InsertedArray($Array, $Index, $Value)
{
    return $Array[0..($Index - 1)] + $Value + $Array[$Index..($Array.Length - 1)]
}

function Start-Base64Process([string] $Base64, [string] $Args = "")
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

function Copy-File([string]$Source, [string]$Destination, [int]$Timeout = 0)
{
    Write-Host "$Source -> $Destination"
    New-Item (Split-Path $Destination -Parent) -ItemType Directory -ErrorAction SilentlyContinue
    $EndTime = [int](Get-Date -UFormat %s) + $Timeout
    do
    {
        Copy-Item $Source -Destination $Destination -ErrorAction SilentlyContinue
        Start-Sleep 0.01
    } while (($EndTime -ge ([int](Get-Date -UFormat %s))) -and -not(Test-Path $Destination -PathType Leaf))
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

function Start-PythonCode([string[]]$Lines)
{
    $Code = $Lines -Join "; "
    Write-Host "python <- $Code"
    return python -c $Code
}

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

function Remove-Cythonized([bool] $Throw = $True)
{
    $ExtSuffix = Start-PythonCode $CodeExtSuffix
    foreach ($CythonizeGlob in $CythonizeGlobs)
    {
        $CodeGlob = @() + $CodeGlobTemplate
        $CodeGlob[1] = $CodeGlobTemplate[1] -f $CythonizeGlob
        $Files = Start-PythonCode $CodeGlob
        foreach ($File in $Files -Split ";")
        {
            $Root = $File.Substring(0,$File.LastIndexOf("."))
            if ($Throw -and $CythonizeRemoveC)
            {
                Remove-Item "$Root.c" -Force
            }
            try
            {
                Remove-Item "$Root$ExtSuffix" -Force
            }
            catch
            {
                if ($Throw)
                {
                    throw
                }
            }
        }
    }
}

function Get-ModuleGraph
{
    if ($ModuleGraphSmart)
    {
        Remove-Cythonized $False
        $TempDir = Join-Path $env:TEMP (New-Guid)
        New-Item $TempDir -ItemType Directory
        $CodeModuleGraphSmartProcess = @() + $CodeModuleGraphSmartTemplate
        $CodeModuleGraphSmartProcess[3] = $CodeModuleGraphSmartTemplate[3] -f (Split-Path $EntryPoint -Parent)
        $CodeModuleGraphSmartProcess[4] = $CodeModuleGraphSmartTemplate[4] -f $TempDir
        $CodeModuleGraphSmartProcess[6] = $CodeModuleGraphSmartTemplate[6] -f ($Excludes -Join " "), ($HooksDirs -Join ";")
        $CodeModuleGraphSmartProcess[7] = $CodeModuleGraphSmartTemplate[7] -f $EntryPoint
        $Modules = (Start-PythonCode $CodeModuleGraphSmartProcess) -Split ";"
        Remove-Item $TempDir -Force -Recurse
        return $Modules[1..($Modules.length - 1)]
    }
    else
    {
        $CodeModuleGraph = @() + $CodeModuleGraphTemplate
        $CodeModuleGraph[4] = $CodeModuleGraphTemplate[4] -f $EntryPoint
        foreach ($Exclude in $Excludes)
        {
            $CodeModuleGraph = Get-InsertedArray $CodeModuleGraph 5 ($CodeModuleGraphTemplate[4] -f "-x=$Exclude")
        }
        return (Start-PythonCode $CodeModuleGraph) -Split ";"
    }
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
        $Args += "--add-data=""$( Join-Path (Start-PythonCode $CodePythonBase) "python.exe" );."""
    }
    if ($ModuleGraph)
    {
        foreach ($Module in Get-ModuleGraph)
        {
            $Args += "--hidden-import=$Module"
        }
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
        # $TempDir = Join-Path $Env:TEMP (New-Guid) FIXME https://github.com/pyinstaller/pyinstaller/issues/4824
        $TempDir = Join-Path (Split-Path (Get-Location) -Qualifier) (Get-Random)
        New-Item $TempDir -ItemType Directory
        Push-Location $TempDir
        pip download pyinstaller --no-deps --no-binary pyinstaller
        $Source = (Get-ChildItem -Attributes Archive).FullName
        tar -xvf $Source
        Set-Location $Source.Substring(0, $Source.Length - ".tar.gz".Length)
        Remove-Item (Join-Path "PyInstaller" "bootloader") -Force -Recurse
        python setup.py build install
        Pop-Location
        Remove-Item $TempDir -Force -Recurse
    }
    if ($CythonizeGlobs)
    {
        # pip install cython FIXME https://github.com/cython/cython/milestone/58
        pip install cython --pre
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
        Start-PythonCode $CodeRunBefore
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
        Write-Host "cythonize <- $( $CythonizeGlobs -Join " " )"
        cythonize -3 --inplace $CythonizeGlobs
    }

    $Name = Get-ProjectName
    $VersionLine = Get-Content $EntryPoint | Select-String -Pattern "__version__.\s*=\s*['`"].*['`"]"
    $FullName = "$Name-$( if ($VersionLine)
    {
        ($VersionLine -Split { $_ -eq '''' -or $_ -eq '"' })[1]
    }
    else
    {
        "X.Y.Z"
    } )"
    "NAME=$FullName" >> $Env:GITHUB_ENV

    $AddArgs = "--name=$FullName", $EntryPoint
    $env:PYTHONOPTIMIZE = $OptimizationLevel
    if ($Obfuscate)
    {
        pyarmor @("pack", "--output=dist", "--options=$MainArgs") $AddArgs
    }
    else
    {
        Write-Host "pyinstaller $( $MainArgs -Join " " ) $( $AddArgs -Join " " )"
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

    if ($MainManifest)
    {
        $TempPath = Join-Path $env:TEMP (New-Guid)
        Copy-File $ExePath $TempPath $CopyTimeout
        MergeManifest $TempPath $MainManifest
        Move-Item $TempPath -Destination $ExePath -Force
    }

    if ($CythonizeRemove)
    {
        Remove-Cythonized
    }

    if ($CodeRunAfter)
    {
        Start-PythonCode $CodeRunAfter
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
}
else
{
    Write-Build
}

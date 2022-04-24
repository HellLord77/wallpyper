$Version = "0.0.4"

<#
.INPUTS
    $Datas = @()
    $Debug = $False
    $EntryPoint = "src\main.py"
    $Excludes = @()
    $Icon = ""
    $Manifest = "" FIXME https://stackoverflow.com/questions/13964909/setting-uac-to-requireadministrator-using-pyinstaller-onefile-option-and-manifes
    $NoConsole = $False
    $Obfuscate = $False
    $OneFile = $False
    $UPX = $False
    $MainManifest = ""
#>

$Datas = @("libs\colors\colornames.min.json", "libs\locales\iso_639-2.json", "libs\locales\iso_3166-1.json", "resources", "win32\syspin.exe")
$Icon = "src\resources\icon.ico"
$NoConsole = $True
$OneFile = $True
$MainManifest = "app.manifest"

$MegaURL = "https://mega.nz/MEGAcmdSetup64.exe"

function Get-Name
{
    return Split-Path $( if ($Env:GITHUB_REPOSITORY)
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

function CalculateExeSize([System.IO.FileStream] $Stream)
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
    for ($i = 0; $i -lt $SectionCount; $i++)
    {
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
    mt -updateresource:"$ExePath;#1" -manifest "$ManifestPath" -nologo -verbose
    $TempStream = [System.IO.File]::OpenRead($TempFile)
    $ExeStream = [System.IO.File]::OpenWrite($ExePath)
    $TempStream.Seek($( CalculateExeSize $TempStream ), [System.IO.SeekOrigin]::Begin) | Out-Null
    $ExeStream.Seek(0, [System.IO.SeekOrigin]::End) | Out-Null
    $TempStream.CopyTo($ExeStream)
    $ExeStream.Close()
    $TempStream.Close()
    $TempFile.Delete()
}

function Install-Dependencies
{
    python -m pip install pip --upgrade

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
    if (Test-Path requirements.txt -PathType Leaf)
    {
        pip install -r requirements.txt
    }
}

function BuildProject
{
    $MainArgs = @("--noconfirm")
    if ($OneFile)
    {
        $MainArgs += "--onefile"
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
        $MainArgs += "--noupx"
    }

    if (!$EntryPoint)
    {
        $EntryPoint = Join-Path "src" "main.py"
    }

    $SrcDir = Split-Path (Split-Path $EntryPoint -Parent) -Leaf
    if ($Datas)
    {
        foreach ($Data in $Datas)
        {
            $DataSrc = Join-Path $SrcDir $Data
            if (Test-Path $DataSrc -PathType Leaf)
            {
                $DataDst = Split-Path $Data -Parent
            }
            else
            {
                $DataDst = $Data
            }
            $MainArgs += "--add-data=""$DataSrc;$DataDst""" -Replace "\\", "\\"
        }
    }

    if ($Debug)
    {
        $NoConsole = $False
        $MainArgs += "--debug=all"
    }

    if ($Excludes)
    {
        foreach ($Exclude in $Excludes)
        {
            $MainArgs += "--exclude-module=$Exclude"
        }
    }

    if ($NoConsole)
    {
        $MainArgs += "--windowed"
    }

    if ($Icon)
    {
        $MainArgs += "--icon=$Icon"
    }

    if ($Manifest)
    {
        $MainArgs += "--manifest=$Manifest"
    }

    $FirstLine = Get-Content $EntryPoint -TotalCount 1
    $Name = Get-Name
    $FullName = "$Name-$( if ( $FirstLine.StartsWith("__version__"))
    {
        ($FirstLine -split { $_ -eq '''' -or $_ -eq '"' })[1]
    }
    else
    {
        "X.Y.Z"
    } )"
    "NAME=$FullName" >> $Env:GITHUB_ENV

    $AddArgs = "--clean", "--name=$FullName", $EntryPoint
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

    if ($MainManifest)
    {
        MergeManifest $ExePath $MainManifest
    }
}

function UploadBuild
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
        mega-put dist (Join-Path "$( Get-Name )-cp$( $env:PYTHON_VERSION -Replace "\.", """" )" ((Get-Date -Format o -AsUTC) -Replace ":", "."))
    }
    else
    {
        throw
    }
}

$ErrorActionPreference = "Stop"
if ($Args)
{
    Invoke-Expression $Args[0]
}
else
{
    BuildProject
}
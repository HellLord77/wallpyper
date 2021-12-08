$Version = "0.0.1"

<#  TODO: UPX
.INPUTS
    $Datas = @()
    $Debug = $False
    $EntryPoint = "src\main.py"
    $Excludes = @()
    $Icon = ""
    $NoConsole = $False
    $Obfuscate = $False
    $OneFile = $False
#>

$Datas = @("resources")  # fixme: remote build succeeds but artifact crashes
$Icon = "icon.ico"
$NoConsole = $True

function Install-Dependecies
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
        $Exists = $True
        while ($Exists)
        {
            # $Temp = Join-Path $Env:TEMP (Get-Random) fixme https://github.com/pyinstaller/pyinstaller/issues/4824
            $Temp = Join-Path (Split-Path (Get-Location) -Qualifier) ".temp-$( Get-Random )"
            $Exists = Test-Path $Temp
        }
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

function Build-Project
{
    $MainArgs = @("--noconfirm")
    if ($OneFile)
    {
        $MainArgs += "--onefile"
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
            $MainArgs += "--add-data=""$( Join-Path $SrcDir $Data );$Data"""
            $MainArgs[-1] = $MainArgs[-1].Replace("\", "\\")
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

    $FirstLine = Get-Content $EntryPoint -TotalCount 1
    $Name = Split-Path $( if ($Env:GITHUB_REPOSITORY)
    {
        $Env:GITHUB_REPOSITORY
    }
    else
    {
        Split-Path -Path (Get-Location) -Leaf
    } ) -Leaf
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

    if (!$OneFile)
    {
        $DistPath = Join-Path "dist" $FullName
        Rename-Item (Join-Path $DistPath "$FullName.exe") "$Name.exe" -Force
    }
}

$ErrorActionPreference = "Stop"
if ($Args)
{
    Invoke-Expression $Args[0]
}
else
{
    Build-Project
}
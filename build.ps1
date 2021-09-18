$Datas = @("resources")
$Icon = "icon.ico"
$NoConsole = $True
$OneFile = $True

function Install-Dependecies
{
    python -m pip install --upgrade pip

    if ($BuildBootloader)
    {
        $Exists = $True
        while ($Exists)
        {
            $Temp = Join-Path $Env:TEMP (Get-Random)
            $Exists = Test-Path $Temp
        }
        New-Item $Temp -ItemType Directory
        Push-Location $Temp
        pip download pyinstaller --no-deps --no-binary : all:
        tar -xf (Get-ChildItem -Attributes Archive).FullName
        Set-Location (Join-Path (Get-ChildItem -Attributes Directory).FullName "bootloader")
        python waf all
        Set-Location ..
        python setup.py install
        Pop-Location
        Remove-Item $Temp -Force -Recurse
    }
    else
    {
        pip install pyinstaller
    }

    if ($Obfuscate)
    {
        pip install pyarmor
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
    $FullName = "$( Split-Path $( if ($Env:GITHUB_REPOSITORY)
    {
        $Env:GITHUB_REPOSITORY
    }
    else
    {
        Split-Path -Path (Get-Location) -Leaf
    } ) -Leaf )-$( if ( $FirstLine.StartsWith("__version__"))
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

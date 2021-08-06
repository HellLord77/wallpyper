$Datas = @("resources")
$Icon = "icon.ico"
$NoConsole = $True
$Obfuscate = $True
$OneFile = $True

function Install-Dependecies
{
    python -m pip install --upgrade pip
    pip install pyinstaller
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
        python -c "$FirstLine; print(__version__)"
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
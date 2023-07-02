$Version = "0.3.2"
################################################################################
$Datas = @(
	"libs/request/cloudflare/browsers.json"  # FIXME https://pyinstaller.org/en/stable/hooks.html#PyInstaller.utils.hooks.is_package
	"res"
	"srcs/res"
	"win32/syspin.exe"
	"../build/pipe/pipe.exe;")
$Datas32 = @()
$Datas64 = @()
$Imports = @()
$Excludes = @()
$HooksDirs = @("hooks")
$RuntimeHooks = @()
$OptimizationLevel = 2  # FIXME https://github.com/pyinstaller/pyinstaller/issues/3379
$Debug = $False
$NoConsole = $True
$OneFile = $False
$ElevatedProc = $False
$RemoteProc = $False
$UPX = $True
$ModuleGraph = $True
$EntryPoint = "src/init.py"
$Icon = "src/res/icon.ico"
$Manifest = ""  # FIXME https://stackoverflow.com/questions/13964909/setting-uac-to-requireadministrator-using-pyinstaller-onefile-option-and-manifes
$MainManifest = "manifest.xml"

$CythonSourceGlobs = @(
	"src/libs/request/**/*.py"
	"src/libs/{colornames,isocodes,mimetype,spinners,urischemes,useragents}/__init__.py"
	# "src/libs/ctyped/interface/**/*.py"
	# "src/libs/ctyped/lib/*.py"  FIXME https://github.com/cython/cython/issues/3838
	"src/libs/ctyped/lib/__init__.py"
	# "src/libs/ctyped/type/*.py"
	"src/libs/ctyped/{const,enum,winrt}/*.py"
	# "src/libs/ctyped/{_utils,struct,union}.py"
	"src/libs/ctyped/{__init__,handle,macro}.py"
	"src/{plat,srcs,win32}/**/*.py"
	"src/{exts,langs,libs}/*.py"
	"src/*.py")
$CythonExcludeGlobs = @(
	"src/init.py"  # FIXME https://pyinstaller.org/en/stable/usage.html#cmdoption-arg-scriptname
	"src/libs/ctyped/enum/__init__.py")  # FIXME https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-1/fatal-error-c1002
$CythonNoDocstrings = $True
$CythonRemove = $True

$NuitkaSources = @()
$NuitkaRemove = $True

$mypycSources = @()  # TODO
$mypycRemove = $True

$CodeRunBefore = @(
	"from sys import argv"
	"from PyInstaller.utils.cliutils.makespec import run"
	"from PyInstaller import __main__"
	"argv.extend(('--noupx', '--icon=NONE', 'src/pipe.py'))"
	"run()"
	"lines = open('pipe.spec').readlines()"
	"open('pipe.spec', 'w').writelines(lines[:lines.index('coll = COLLECT(\n')])"
	"__main__.run(['pipe.spec'])")
$CodeRunBeforeRemote = @(
	"from src.libs.colornames import download"
	"download()"
	"from src.libs.isocodes import download"
	"download()"
	"from src.libs.mimetype import download"
	"download()"
	"from src.libs.request.cloudflare import download"
	"download()"
	"from src.libs.spinners import download"
	"download()"
	"from src.libs.urischemes import download"
	"download()"
	"from src.libs.useragents import download"
	"download()")
$CodeRunAfter = @()
$CodeRunAfterRemote = @()
$MinifyJsonRegExs = @(
	"src/libs/colornames/colornames.min.json"
	"src/libs/isocodes/iso_*.json"
	"src/libs/mimetype/db.json"
	"src/libs/request/cloudflare/browsers.json"
	"src/libs/spinners/spinners.json"
	"src/libs/useragents/user-agents.json")
$UPXDir = ""
################################################################################
$CodePythonIs64Bit = @(
	"from sys import maxsize"
	"print(maxsize > 2 ** 32)")
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
$MinifyJsonLocal = $False
$StripSymbols = $False
$ModuleGraphSmart = $True
$CythonRemoveC = $False
$NuitkaRemoveBuild = $True
$mypycCacheDir = ".mypy_cache"
################################################################################
$IsPython64Bit = $null
$ExtSuffix = $null
$CythonSources = $null

function ToArray($Object) {
	if ($Object -isnot [array]) { $Object = @($Object) }
	return @($Object)
}

function Get-InsertedArray([array]$Array, $Index, $Value) {
	if ($Index -lt 0 -or $Index -gt $Array.Length) { throw }
	elseif ($Index -eq 0) { $Array = $Value + $Array }
	elseif ($Index -eq $Array.Length) { $Array = $Array + $Value }
	else { $Array = $Array[0..($Index - 1)] + $Value + $Array[$Index..($Array.Length - 1)] }
	return ToArray $Array
}

function Get-RemovedArray([array]$Array, $Index) {
	if ($Index -lt 0 -or $Index -ge $Array.Length) { throw }
	elseif ($Index -eq 0) { $Array = $Array[1..($Array.Length - 1)] }
	elseif ($Index -eq ($Array.Length - 1)) { $Array = $Array[0..($Array.Length - 2)] }
	else { $Array = $Array[0..($Index - 1)] + $Array[($Index + 1)..($Array.Length - 1)] }
	return ToArray $Array
}

function Get-RemovedItemArray([array]$Array, $Item, $Count = [double]::PositiveInfinity) {
	for ($i = 0; $i -lt $Count; $i++) {
		if (-not $Array) { break }
		$Index = $Array.IndexOf($Item)
		if ($Index -eq -1) { break }
		else { $Array = Get-RemovedArray $Array $Index }
	}
	return ToArray $Array
}

function Start-Base64Process([string]$Base64, [string]$ArgList = "") {
	$TempFile = New-TemporaryFile
	[IO.File]::WriteAllBytes($TempFile, [Convert]::FromBase64String($Base64))
	Start-Process $TempFile -ArgumentList $ArgList -Wait
	$TempFile.Delete()
}

function Get-ExeSize([System.IO.FileStream]$Stream) {
	$Buffer = [byte[]]::New(4096)
	$Stream.Read($Buffer, 0, 4096) | Out-Null
	$HeaderOffset = [System.BitConverter]::ToInt32($Buffer, 60)
	$HeadersSize = 248
	if ([System.BitConverter]::ToUInt16($Buffer, $HeaderOffset + 4) -eq 0x8664) {
		$HeadersSize += 16
	}
	$SectionCount = [System.BitConverter]::ToUInt16($Buffer, $HeaderOffset + 6)
	$MaxPointer = 0
	$Size = 0
	for ($i = 0; $i -lt $SectionCount; $i++) {
		$SectionOffset = $HeaderOffset + $HeadersSize + $i * 40
		$RawDataPointer = [System.BitConverter]::ToInt32($Buffer, $SectionOffset + 20)
		if ($RawDataPointer -gt $MaxPointer) {
			$MaxPointer = $RawDataPointer
			$Size = $MaxPointer + [System.BitConverter]::ToInt32($Buffer, $SectionOffset + 16)
		}
	}
	return $Size
}

function Copy-File([string]$Source, [string]$Destination, [int]$Timeout = 0) {
	Write-Host "$Source -> $Destination"
	New-Item (Split-Path $Destination -Parent) -ItemType Directory -ErrorAction SilentlyContinue
	$EndTime = [int](Get-Date -UFormat %s) + $Timeout
	do {
		Copy-Item $Source -Destination $Destination -ErrorAction SilentlyContinue
		Start-Sleep 0.01
	} while (($EndTime -ge ([int](Get-Date -UFormat %s))) -and -not (Test-Path $Destination -PathType Leaf))
}

function MinifyJsonFile([string]$Path, [string]$OutPath) {
	if (-not $OutPath) { $OutPath = $Path }
	Write-Host "Minify $Path -> $OutPath"
	ConvertFrom-Json (Get-Content -Raw $Path) | ConvertTo-Json -Depth 100 -Compress | Set-Content $OutPath
}

function Get-DeveloperPath {
	$InstallPath = & (Install-PackageChoco "vswhere") -latest -property installationPath
	& "${Env:COMSPEC}" /s /c "`"$InstallPath\Common7\Tools\vsdevcmd.bat`" -no_logo && set" | ForEach-Object {
		$Name, $Value = $_ -Split '=', 2
		if ($Name -eq "PATH") { return $Value }
	}
}

function MergeManifest([string]$ExePath, [string]$ManifestPath) {
	$TempFile = New-TemporaryFile
	Copy-Item $ExePath -Destination $TempFile
	if (-not (Get-Command mt -ErrorAction SilentlyContinue)) { $Env:PATH += ";$(Get-DeveloperPath)" }
	mt -updateresource:"$ExePath;#1" -manifest "$ManifestPath" -nologo
	$TempStream = [System.IO.File]::OpenRead($TempFile)
	$ExeStream = [System.IO.File]::OpenWrite($ExePath)
	$TempStream.Seek($( Get-ExeSize $TempStream ), [System.IO.SeekOrigin]::Begin) | Out-Null
	$ExeStream.Seek(0, [System.IO.SeekOrigin]::End) | Out-Null
	$TempStream.CopyTo($ExeStream)
	$ExeStream.Close()
	$TempStream.Close()
	$TempFile.Delete()
}

function Install-PackageChoco($Package, $Command = "", $Force = $False) {
	if (-not $Command) { $Command = $Package }
	if ($Force -or -not (Get-Command $Command -ErrorAction SilentlyContinue)) {
		Write-Host "choco -> $Package"
		choco install $Package --yes
	}
	return (Get-Command $Command).Source
}

function Start-PythonCode([string[]]$Lines) {
	$Code = $Lines -Join "; "
	Write-Host "python <- $Code"
	return python -c $Code
}

function Get-ProjectName {
	return Split-Path $( if ($IsRemote) { $Env:GITHUB_REPOSITORY }
		else { Split-Path -Path (Get-Location) -Leaf } ) -Leaf
}

function Get-IsPython64Bit {
	if ($null -eq $Global:IsPython64Bit) {
		$Global:IsPython64Bit = [System.Convert]::ToBoolean((Start-PythonCode $CodePythonIs64Bit))
	}
	return $Global:IsPython64Bit
}

function Get-ExtSuffix {
	if ($null -eq $Global:ExtSuffix) {
		$Global:ExtSuffix = Start-PythonCode $CodeExtSuffix
	}
	return $Global:ExtSuffix
}

function Get-ModuleGraph {
	if ($ModuleGraphSmart) {
		Remove-Cython $False
		Remove-Nuitka $False
		Remove-mypyc $False
		$TempDir = Join-Path $Env:TEMP (New-Guid)
		New-Item $TempDir -ItemType Directory
		$CodeModuleGraphSmartProcess = @() + $CodeModuleGraphSmartTemplate
		$CodeModuleGraphSmartProcess[3] = $CodeModuleGraphSmartTemplate[3] -f (Split-Path $EntryPoint -Parent)
		$CodeModuleGraphSmartProcess[4] = $CodeModuleGraphSmartTemplate[4] -f $TempDir
		$CodeModuleGraphSmartProcess[6] = $CodeModuleGraphSmartTemplate[6] -f "$Excludes", ($HooksDirs -Join ";")
		$CodeModuleGraphSmartProcess[7] = $CodeModuleGraphSmartTemplate[7] -f $EntryPoint
		$Modules = (Start-PythonCode $CodeModuleGraphSmartProcess) -Split ";"
		Remove-Item $TempDir -Force -Recurse
		return $Modules[1..($Modules.length - 1)]
	}
	else {
		$CodeModuleGraph = @() + $CodeModuleGraphTemplate
		$CodeModuleGraph[4] = $CodeModuleGraphTemplate[4] -f $EntryPoint
		foreach ($Exclude in $Excludes) {
			$CodeModuleGraph = Get-InsertedArray $CodeModuleGraph 5 ($CodeModuleGraphTemplate[4] -f "-x=$Exclude")
		}
		return (Start-PythonCode $CodeModuleGraph) -Split ";"
	}
}

function Get-PyInstallerArgs {
	$ArgList = @("--noconfirm")
	if ($OneFile) { $ArgList += "--onefile" }
	if ($Debug) { $ArgList += "--debug=all" }
	if ($NoConsole) { $ArgList += "--windowed" }
	if ($Manifest) { $ArgList += "--manifest=$Manifest" }
	if ($ElevatedProc) { $ArgList += "--uac-admin" }
	if ($RemoteProc) { $ArgList += "--uac-uiaccess" }
	if ($Icon) { $ArgList += "--icon=$Icon" }
	foreach ($Import in $Imports) { $ArgList += "--hidden-import=$Import" }
	foreach ($Exclude in $Excludes) { $ArgList += "--exclude-module=$Exclude" }
	foreach ($HooksDir in $HooksDirs) { $ArgList += "--additional-hooks-dir=$HooksDir" }
	foreach ($RuntimeHook in $RuntimeHooks) { $ArgList += "--runtime-hook=$RuntimeHook" }
	if ($ModuleGraph) {
		$_, $Modules = Get-ModuleGraph
		foreach ($Module in $Modules) {
			$ArgList += "--hidden-import=$Module"
		}
	}
	$BaseSrcDir = Split-Path (Split-Path $EntryPoint -Parent) -Leaf
	foreach ($Data in $($Datas + $(If (Get-IsPython64Bit) { $Datas64 } else { $Datas32 }))) {
		$DataSrc = Join-Path $BaseSrcDir $Data
		if ($Data.Contains(";")) {
			$DataParts = $DataSrc -Split ";"
			$DataSrc = $DataParts[0]
			$DataDst = $DataParts[1]
		}
		else {
			if (Test-Path $DataSrc -PathType Leaf) { $DataDst = Split-Path $Data -Parent }
			else { $DataDst = $Data }
		}
		if (-not $DataDst) { $DataDst = "." }
		$ArgList += "--add-data=""$DataSrc;$DataDst"""
	}
	if ($UPX) {
		if (-not (Get-Command upx -ErrorAction SilentlyContinue)) {
			if (-not $UPXDir) {
				$UPXDir = Split-Path (Install-PackageChoco "upx") -Parent
			}
		}
		$ArgList += "--upx-dir=$UPXDir"
	}
	else { $ArgList += "--noupx" }
	if ($StripSymbols) { $ArgList += "--strip" }
	return $ArgList
}

function Remove-pyd([string[]]$Sources, [bool]$Throw) {
	foreach ($Source in $Sources) {
		$Root = $Source.Substring(0, $Source.LastIndexOf("."))
		try { Remove-Item "$Root$(Get-ExtSuffix)" -Force }
		catch { if ($Throw) { throw } }
	}
}

function Get-CythonSources {
	if ($null -eq $Global:CythonSources) {
		$Global:CythonSources = @()
		$CodeGlob = @() + $CodeGlobTemplate
		foreach ($CythonSourceGlob in $CythonSourceGlobs) {
			$CodeGlob[1] = $CodeGlobTemplate[1] -f $CythonSourceGlob
			foreach ($Source in (Start-PythonCode $CodeGlob) -Split ";") {
				$Global:CythonSources += $Source -Replace "\\", "/"
			}
		}
		foreach ($CythonExcludeGlob in $CythonExcludeGlobs) {
			$CodeGlob[1] = $CodeGlobTemplate[1] -f $CythonExcludeGlob
			foreach ($Exclude in (Start-PythonCode $CodeGlob) -Split ";") {
				$Global:CythonSources = Get-RemovedItemArray $Global:CythonSources ($Exclude -Replace "\\", "/")
			}
		}
	}
	return $Global:CythonSources
}

function Remove-Cython([bool]$Throw = $True) {
	Remove-pyd (Get-CythonSources) $Throw
	if ($CythonRemoveC) {
		foreach ($Source in Get-CythonSources) {
			Remove-Item "$(Source.Substring(0, $Source.LastIndexOf("."))).c" -Force -ErrorAction SilentlyContinue 
		}
	}
}

function Get-CythonArgs {
	$ArgsList = @("-3", "--inplace")
	if ($CythonNoDocstrings) {
		$ArgsList += "--no-docstrings"
	}
	foreach ($CythonExcludeGlob in $CythonExcludeGlobs) {
		$ArgsList += "--exclude=$CythonExcludeGlob"
	}
	return $ArgsList + $CythonSourceGlobs
}

function Remove-Nuitka([bool]$Throw = $True) {
	Remove-pyd $NuitkaSources $Throw
}

function Get-NuitkaArgs {
	$ArgList = @("--assume-yes-for-downloads", "--no-pyi-file", "--module")
	if ($NuitkaRemoveBuild) { $ArgList += "--remove-output" }
	return $ArgList
}

function Remove-mypyc([bool]$Throw = $True) {
	Remove-pyd $mypycSources $Throw
}

function Get-mypycArgs {
	$ArgList = @("--install-types", "--non-interactive")
	if ($mypycCacheDir) { $ArgList += "--cache-dir=$(Join-Path $PSScriptRoot $mypycCacheDir)" }
	return $ArgList
}

function Install-Requirements {
	python -m pip install pip --upgrade
	pip install setuptools --upgrade
	pip install wheel --upgrade

	# $TempDir = Join-Path $Env:TEMP (New-Guid) FIXME https://github.com/pyinstaller/pyinstaller/issues/4824
	$TempDir = Join-Path (Split-Path (Get-Location) -Qualifier) (Get-Random)
	New-Item $TempDir -ItemType Directory
	Push-Location $TempDir
	pip download pyinstaller --no-deps --no-binary pyinstaller
	$Source = (Get-ChildItem -Attributes Archive).FullName
	tar -xf $Source
	Set-Location $Source.Substring(0, $Source.Length - 7)
	Remove-Item (Join-Path "PyInstaller" "bootloader") -Force -Recurse
	python setup.py build
	pip install .
	Pop-Location
	Remove-Item $TempDir -Force -Recurse

	if ($CythonSourceGlobs) { pip install cython==3.0.0b2 }  # FIXME https://github.com/cython/cython/milestone/58
	if ($NuitkaSources) { pip install nuitka }
	if ($mypycSources) { pip install mypy }

	if (Test-Path requirements.txt -PathType Leaf) { pip install -r requirements.txt }
}

function Write-Build {
	if ($CodeRunBefore) {
		Start-PythonCode $CodeRunBefore
	}
	if ($IsRemote -and $CodeRunBeforeRemote) {
		Start-PythonCode $CodeRunBeforeRemote
	}

	if ($MinifyJsonLocal -or $IsRemote) {
		foreach ($MinifyJsonRegEx in $MinifyJsonRegExs) {
			foreach ($Json in  Get-ChildItem -Path . -Filter $MinifyJsonRegEx) {
				MinifyJsonFile $Json.FullName
			}
		}
	}

	$PyInstallerArgs = Get-PyInstallerArgs
	if ($CythonSourceGlobs) {
		$CythonArgs = Get-CythonArgs
		Write-Host "cythonize $CythonArgs"
		cythonize $CythonArgs
	}
	if ($NuitkaSources) {
		$NuitkaArgsBase = Get-NuitkaArgs
		foreach ($Source in $NuitkaSources) {
			$NuitkaArgs = $NuitkaArgsBase + @("--output-dir=$(Split-Path $Source -Parent)", $Source)
			Write-Host "nuitka $NuitkaArgs"
			nuitka $NuitkaArgs
		}
	}
	if ($mypycSources) {
		$mypycArgsBase = Get-mypycArgs
		foreach ($Source in $mypycSources) {
			Push-Location (Split-Path $Source -Parent)
			$mypycArgs = $mypycArgsBase + @(Split-Path $Source -Leaf)
			Write-Host "mypyc $mypycArgs"
			mypyc $mypycArgs
			Pop-Location
		}
	}

	$Name = Get-ProjectName
	$VersionLine = Get-Content $EntryPoint | Select-String -Pattern "__version__.\s*=\s*['`"].*['`"]"
	$FullName = "$Name-$( if ($VersionLine){
        ($VersionLine -Split { $_ -eq '''' -or $_ -eq '"' })[1]
    } else { "0.0.0" } )"
	"NAME=$FullName" >> $Env:GITHUB_ENV

	$CommonArgs = "--name=$FullName", $EntryPoint
	$Env:PYTHONOPTIMIZE = $OptimizationLevel
	$PyInstallerArgs += $CommonArgs
	Write-Host "pyinstaller $PyInstallerArgs"
	pyinstaller $PyInstallerArgs

	$DistPath = Join-Path "dist" $FullName
	if ($OneFile) { $ExePath = "$DistPath.exe" }
	else {
		$ExePath = Join-Path $DistPath "$Name.exe"
		Move-Item (Join-Path $DistPath "$FullName.exe") $ExePath -Force
	}

	if ($MainManifest) { MergeManifest $ExePath $MainManifest }

	if ($CythonRemove) { Remove-Cython }
	if ($NuitkaRemove) { Remove-Nuitka }
	if ($mypycRemove) { Remove-mypyc }

	if ($CodeRunAfter) { Start-PythonCode $CodeRunAfter }
	if ($IsRemote -and $CodeRunAfterRemote) { Start-PythonCode $CodeRunAfterRemote }
}

function Write-MEGA {
	if (-not $Env:MEGA_USERNAME -or -not $Env:MEGA_PASSWORD) {
		throw
	}
	if (-not (Get-Command mega-help -ErrorAction SilentlyContinue)) {
		$Env:PATH += ";$( Join-Path $Env:LOCALAPPDATA "MEGAcmd" )"
		Install-PackageChoco "megacmd" "mega-help"
	}
	mega-login $Env:MEGA_USERNAME $Env:MEGA_PASSWORD
	mega-put dist (Join-Path "$( Get-ProjectName )-cp$( $Env:PYTHON_VERSION -Replace "\.", """" )" ((Get-Date -Format o -AsUTC) -Replace ":", "."))
	mega-logout
}

$IsRemote = Test-Path Env:CI

$ErrorActionPreference = "Stop"
if ($Args) {
	switch ($Args[0]) {
		"install" { Install-Requirements; Break }
		"build" { Write-Build; Break }
		"upload" { Write-MEGA; Break }
		Default { throw }
	}
}
else { Write-Build }

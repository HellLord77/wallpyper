$Version = "0.2.1"

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
$Obfuscate = $False
$OneFile = $False
$ElevatedProc = $False
$RemoteProc = $False
$UPX = $False
$ModuleGraph = $True
$EntryPoint = "src/init.py"
$Icon = "src/res/icon.ico"
# $Manifest = "manifest.xml" FIXME https://stackoverflow.com/questions/13964909/setting-uac-to-requireadministrator-using-pyinstaller-onefile-option-and-manifes
$Manifest = ""
$MainManifest = "manifest.xml"
$CythonSources = @()
$CythonizeExcludeGlobs = @(
	"src/init.py"  # FIXME https://pyinstaller.org/en/stable/usage.html#cmdoption-arg-scriptname
	"src/libs/ctyped/enum/__init__.py")  # FIXME https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-1/fatal-error-c1002
$CythonizeSourceGlobs = @(
	"src/libs/request/**/*.py"
	"src/libs/{colornames,isocodes,mimetype,spinners,urischemes,useragents}/__init__.py"
	# "src/libs/ctyped/interface/**/*.py"
	# "src/libs/ctyped/lib/*.py"  FIXME https://github.com/cython/cython/issues/3838
	"src/libs/ctyped/lib/__init__.py"
	# "src/libs/ctyped/type/*.py"
	"src/libs/ctyped/{const,enum,winrt}/*.py"
	# "src/libs/ctyped/{_utils,struct,union}.py"
	"src/libs/ctyped/{__init__,handle,macro}.py"
	"src/win32/**/*.py"
	"src/{langs,libs,srcs}/*.py"
	"src/*.py")
# $CythonizeSourceGlobs = @()
$CythonizeAnnotate = $False
$CythonizeNoDocstrings = $True
$CythonizeRemove = $True
$CodeRunBefore = @(
	"from sys import argv"
	"from PyInstaller.utils.cliutils.makespec import run"
	"from PyInstaller import __main__"
	"argv.extend(('--noupx', '--icon=NONE', 'src/pipe.py'))"
	"run()"
	"lines = open('pipe.spec').readlines()"
	"open('pipe.spec', 'w').writelines(lines[:lines.index('coll = COLLECT(\n')])"
	"__main__.run(['pipe.spec'])"
)
$CodeRunBeforeRemote = @(
	"from src.libs.colornames import _download"
	"_download()"
	"from src.libs.isocodes import _download"
	"_download()"
	"from src.libs.mimetype import _download"
	"_download()"
	"from src.libs.request.cloudflare import _download"
	"_download()"
	"from src.libs.spinners import _download"
	"_download()"
	"from src.libs.urischemes import _download"
	"_download()"
	"from src.libs.useragents import _download"
	"_download()")
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

$CodePythonIs64Bit = @(
	"from sys import maxsize"
	"print(maxsize > 2 ** 32)")
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
$CodeCompileCTemplate = @(
	"from distutils.command.build_ext import build_ext"
	"from distutils.ccompiler import new_compiler"
	"from distutils.core import Distribution"
	"from os.path import splitext"
	"from sys import version_info"
	"build = build_ext(Distribution())"
	"build.finalize_options()"
	"compiler = new_compiler()"
	"source = r'{0}'"
	"objects = compiler.compile([source], include_dirs=build.include_dirs)"
	"libraries = [f'python{version_info.major}{version_info.minor}']"
	"compiler.link_executable(objects, splitext(source)[0], libraries=libraries, library_dirs=build.library_dirs)")
$ModuleGraphSmart = $True
$CythonizeRemoveC = $False
$MinifyJsonLocal = $False

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
	} while (($EndTime -ge ([int](Get-Date -UFormat %s))) -and -not(Test-Path $Destination -PathType Leaf))
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
	if (-not (Get-Command mt -ErrorAction SilentlyContinue)) { $Env:PATH += ";$(Get-DeveloperPath)"	}
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

function Get-CythonizedSources {
	$Sources = @()
	$CodeGlob = @() + $CodeGlobTemplate
	foreach ($CythonizeSourceGlob in $CythonizeSourceGlobs) {
		$CodeGlob[1] = $CodeGlobTemplate[1] -f $CythonizeSourceGlob
		foreach ($Source in (Start-PythonCode $CodeGlob) -Split ";") {
			$Sources += $Source -Replace "\\", "/"
		}
	}
	foreach ($CythonizeExcludeGlob in $CythonizeExcludeGlobs) {
		$CodeGlob[1] = $CodeGlobTemplate[1] -f $CythonizeExcludeGlob
		foreach ($Exclude in (Start-PythonCode $CodeGlob) -Split ";") {
			$Sources = Get-RemovedItemArray $Sources ($Exclude -Replace "\\", "/")
		}
	}
	return $Sources
}

function Remove-Cythonized([bool] $Throw = $True) {
	$ExtSuffix = Start-PythonCode $CodeExtSuffix
	foreach ($Source in Get-CythonizedSources) {
		$Root = $Source.Substring(0, $Source.LastIndexOf("."))
		if ($Throw -and $CythonizeRemoveC) { Remove-Item "$Root.c" -Force }
		try { Remove-Item "$Root$ExtSuffix" -Force }
		catch { if ($Throw) { throw } }
	}
}

function Get-ModuleGraph {
	if ($ModuleGraphSmart) {
		Remove-Cythonized $False
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
	if ($Icon) { $ArgList += "--icon=$Icon"	}
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
	foreach ($Data in $($Datas + $(If ($IsPython64Bit) { $Datas64 } else { $Datas32 }))) {
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
	return $ArgList
}

function Install-Requirements {
	python -m pip install pip --upgrade
	python -m pip install setuptools --upgrade

	if ($Obfuscate) {
		pip install pyinstaller --upgrade
		pip install pyarmor --upgrade
	}
	else {
		pip install wheel --upgrade
		# $TempDir = Join-Path $Env:TEMP (New-Guid) FIXME https://github.com/pyinstaller/pyinstaller/issues/4824
		$TempDir = Join-Path (Split-Path (Get-Location) -Qualifier) (Get-Random)
		New-Item $TempDir -ItemType Directory
		Push-Location $TempDir
		pip download pyinstaller --no-deps --no-binary pyinstaller
		$Source = (Get-ChildItem -Attributes Archive).FullName
		tar -xf $Source
		Set-Location $Source.Substring(0, $Source.Length - ".tar.gz".Length)
		Remove-Item (Join-Path "PyInstaller" "bootloader") -Force -Recurse
		python setup.py build
		pip install .
		Pop-Location
		Remove-Item $TempDir -Force -Recurse
	}
	if ($CythonSources -or $CythonizeSourceGlobs) {
		# FIXME https://github.com/cython/cython/milestone/58
		pip install --pre cython
	}

	if (Test-Path requirements.txt -PathType Leaf) {
		pip install -r requirements.txt
	}
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

	if ($CythonSources) {
		# FIXME pythonXX._pth [embeddable]
		$CythonArgsBase = @("--verbose", "-3", "--embed")
		if (-not $IsRemote -and $CythonizeAnnotate) {
			$CythonArgsBase += "--annotate"
		}
		if ($CythonizeNoDocstrings) {
			$CythonArgsBase += "--no-docstrings"
		}
		$CodeCompileC = @() + $CodeCompileCTemplate
		foreach ($CythonSource in $CythonSources) {
			$CythonArgs = $CythonArgsBase + $CythonSource
			Write-Host "cython $CythonArgs"
			cython $CythonArgs
			$SourceBase = $CythonSource.Substring(0, $CythonSource.LastIndexOf("."))
			$CodeCompileC[8] = $CodeCompileCTemplate[8] -f "$SourceBase.c"
			Start-PythonCode $CodeCompileC
			Remove-Item "$SourceBase.exp" -Force
			Remove-Item "$SourceBase.lib" -Force
			Remove-Item "$SourceBase.obj" -Force
		}
	}

	$PyInstallerArgs = Get-PyInstallerArgs
	if ($CythonizeSourceGlobs) {
		$CythonizeArgs = @("-3", "--inplace")
		if (-not $IsRemote -and $CythonizeAnnotate) {
			$CythonizeArgs += "--annotate"
		}
		if ($CythonizeNoDocstrings) {
			$CythonizeArgs += "--no-docstrings"
		}
		foreach ($CythonizeExcludeGlob in $CythonizeExcludeGlobs) {
			$CythonizeArgs += "--exclude=$CythonizeExcludeGlob"
		}
		$CythonizeArgs += $CythonizeSourceGlobs
		Write-Host "cythonize $CythonizeArgs"
		cythonize $CythonizeArgs
	}

	$Name = Get-ProjectName
	$VersionLine = Get-Content $EntryPoint | Select-String -Pattern "__version__.\s*=\s*['`"].*['`"]"
	$FullName = "$Name-$( if ($VersionLine)	{
		($VersionLine -Split { $_ -eq '''' -or $_ -eq '"' })[1]
	} else {
		"0.0.0"
	} )"
	"NAME=$FullName" >> $Env:GITHUB_ENV

	$CommonArgs = "--name=$FullName", $EntryPoint
	$Env:PYTHONOPTIMIZE = $OptimizationLevel
	if ($Obfuscate) {
		$PyArmorArgs = @("pack", "--output=dist", "--options=$PyInstallerArgs") + $CommonArgs
		Write-Host "pyarmor $PyArmorArgs"
		pyarmor $PyArmorArgs
	}
	else {
		$PyInstallerArgs += $CommonArgs
		Write-Host "pyinstaller $PyInstallerArgs"
		pyinstaller $PyInstallerArgs
	}

	$DistPath = Join-Path "dist" $FullName
	if ($OneFile) { $ExePath = "$DistPath.exe" }
	else {
		$ExePath = Join-Path $DistPath "$Name.exe"
		Move-Item (Join-Path $DistPath "$FullName.exe") $ExePath -Force
	}

	if ($MainManifest) { MergeManifest $ExePath $MainManifest }

	if ($CythonizeRemove) { Remove-Cythonized }

	if ($CodeRunAfter) { Start-PythonCode $CodeRunAfter	}
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
$IsPython64Bit = [System.Convert]::ToBoolean((Start-PythonCode $CodePythonIs64Bit))

$ErrorActionPreference = "Stop"
if ($Args) {
	switch ($Args[0]) {
		"install" { Install-Requirements; Break }
		"build" { Write-Build; Break }
		"upload" { Write-MEGA; Break }
		Default { throw }
	}
}
else {	Write-Build }

from __future__ import annotations as _

import ctypes as _ctypes
import typing as _typing
from typing import Any as _Any
from typing import Callable as _Callable
from typing import Union as _Union

import _ctypes as __ctypes

from .. import const as _const
from .. import enum as _enum
from .. import struct as _struct
from .._utils import _Globals
from .._utils import _Pointer
from .._utils import _PyCSimpleType
from .._utils import _SimpleCData
from .._utils import _resolve_type
from ..enum import iCUESDK as _enum_iCUESDK
from ..enum import libclang as _enum_libclang


def _callable() -> _Any:
    pass


c_byte: type[_ctypes.c_byte] = _Union[_ctypes.c_byte, int]
c_char: type[_ctypes.c_char] = _Union[_ctypes.c_char, bytes]
c_char_p: type[_ctypes.c_char_p] = _Union[_ctypes.c_char_p, _Pointer, bytes, None]
c_double: type[_ctypes.c_double] = _Union[_ctypes.c_double, float]
c_longdouble: type[_ctypes.c_longdouble] = _Union[_ctypes.c_longdouble, float]
c_float: type[_ctypes.c_float] = _Union[_ctypes.c_float, float]
c_int: type[_ctypes.c_int] = _Union[_ctypes.c_int, int]
c_int8: type[_ctypes.c_int8] = _Union[_ctypes.c_int8, int]
c_int16: type[_ctypes.c_int16] = _Union[_ctypes.c_int16, int]
c_int32: type[_ctypes.c_int32] = _Union[_ctypes.c_int32, int]
c_int64: type[_ctypes.c_int64] = _Union[_ctypes.c_int64, int]
c_long: type[_ctypes.c_long] = _Union[_ctypes.c_long, int]
c_longlong: type[_ctypes.c_longlong] = _Union[_ctypes.c_longlong, int]
c_short: type[_ctypes.c_short] = _Union[_ctypes.c_short, int]
c_size_t: type[_ctypes.c_size_t] = _Union[_ctypes.c_size_t, int]
c_ssize_t: type[_ctypes.c_ssize_t] = _Union[_ctypes.c_ssize_t, int]
c_ubyte: type[_ctypes.c_ubyte] = _Union[_ctypes.c_ubyte, int]
c_uint: type[_ctypes.c_uint] = _Union[_ctypes.c_uint, int]
c_uint8: type[_ctypes.c_uint8] = _Union[_ctypes.c_uint8, int]
c_uint16: type[_ctypes.c_uint16] = _Union[_ctypes.c_uint16, int]
c_uint32: type[_ctypes.c_uint32] = _Union[_ctypes.c_uint32, int]
c_uint64: type[_ctypes.c_uint64] = _Union[_ctypes.c_uint64, int]
c_ulong: type[_ctypes.c_ulong] = _Union[_ctypes.c_ulong, int]
c_ulonglong: type[_ctypes.c_ulonglong] = _Union[_ctypes.c_ulonglong, int]
c_ushort: type[_ctypes.c_ushort] = _Union[_ctypes.c_ushort, int]
c_void_p: type[_ctypes.c_void_p] = _Union[_ctypes.c_void_p, _ctypes.c_char_p, _ctypes.c_wchar_p, _Pointer, bytes, int, str, None]
c_wchar: type[_ctypes.c_wchar] = _Union[_ctypes.c_wchar, str]
c_wchar_p: type[_ctypes.c_wchar_p] = _Union[_ctypes.c_wchar_p, _Pointer, str, None]
c_bool: type[_ctypes.c_bool] = _Union[_ctypes.c_bool, bool]
HRESULT: type[_ctypes.HRESULT] = _Union[_ctypes.HRESULT, int]
py_object: type[_ctypes.py_object] = _Union[_ctypes.py_object, c_void_p, _Pointer, object]

c_void = c_void_p
c_uchar = c_ubyte
c_wchar_t = c_wchar

# basetsd
INT8 = c_char
INT16 = c_short
INT32 = c_int
INT64 = c_int64
UINT8 = c_uchar
UINT16 = c_ushort
UINT32 = c_uint
UINT64 = c_uint64
LONG32 = c_int
ULONG32 = c_uint
DWORD32 = c_uint
LONG64 = c_int64
ULONG64 = c_uint64
DWORD64 = c_uint64
# noinspection PyProtectedMember
INT_PTR = c_int64 if _const._WIN64 else c_int
# noinspection PyProtectedMember
UINT_PTR = c_uint64 if _const._WIN64 else c_uint
# noinspection PyProtectedMember
LONG_PTR = c_int64 if _const._WIN64 else c_long
# noinspection PyProtectedMember
ULONG_PTR = c_uint64 if _const._WIN64 else c_ulong
# noinspection PyProtectedMember
c_int3264 = c_int64 if _const._WIN64 else c_int
# noinspection PyProtectedMember
HALF_PTR = c_int if _const._WIN64 else c_short
# noinspection PyProtectedMember
UHALF_PTR = c_uint if _const._WIN64 else c_ushort
# noinspection PyProtectedMember
HANDLE_PTR = c_uint64 if _const._WIN64 else c_ulong
# noinspection PyProtectedMember
SHANDLE_PTR = c_int64 if _const._WIN64 else c_long

# minwindef
DWORD = c_ulong
BOOL = c_int
BYTE = c_uchar
WORD = c_ushort
FLOAT = c_float
INT = c_int
UINT = c_uint

# stdint
int8_t = c_char
int16_t = c_short
int32_t = c_int
int64_t = c_longlong
uint8_t = c_uchar
uint16_t = c_ushort
uint32_t = c_uint
uint64_t = c_ulonglong
int_least8_t = c_char
int_least16_t = c_short
int_least32_t = c_int
int_least64_t = c_longlong
uint_least8_t = c_uchar
uint_least16_t = c_ushort
uint_least32_t = c_uint
uint_least64_t = c_ulonglong
int_fast8_t = c_char
int_fast16_t = c_int
int_fast32_t = c_int
int_fast64_t = c_longlong
uint_fast8_t = c_uchar
uint_fast16_t = c_uint
uint_fast32_t = c_uint
uint_fast64_t = c_ulonglong
intmax_t = c_longlong
uintmax_t = c_ulonglong

# vadefs
uintptr_t = c_uint64

# vcruntime
ptrdiff_t = c_int64
intptr_t = c_int64

# python
# pyport
Py_uintptr_t = uintptr_t
Py_intptr_t = intptr_t
Py_ssize_t = Py_intptr_t
Py_hash_t = Py_ssize_t
Py_uhash_t = c_size_t

LPCCH = c_char_p
LPCH = c_char_p
LPCSTR = c_char_p
LPCVOID = c_void_p
LPCWCH = c_wchar_p
LPCWSTR = c_wchar_p
LPSTR = c_char_p
LPVOID = c_void_p
LPWCH = c_wchar_p
LPWSTR = c_wchar_p
NPSTR = c_char_p
NWPSTR = c_wchar_p
PBYTE = c_char_p
PCCH = c_char_p
PCH = c_char_p
PCHAR = c_char_p
PCNZCH = c_char_p
PCNZWCH = c_wchar_p
PCSTR = c_char_p
PCSZ = c_char_p
PCWCH = c_wchar_p
PCWSTR = c_wchar_p
PCZZSTR = c_char_p
PNZCH = c_char_p
PSTR = c_char_p
PVOID = c_void_p
PCVOID = c_void_p
PWCH = c_wchar_p
PWCHAR = c_wchar_p
PWSTR = c_wchar_p
PZZSTR = c_char_p
PZZWSTR = c_wchar_p
va_list = c_char_p
HDOMAINENUM = c_void_p
UIA_HWND = c_void_p

errno_t = c_int
wint_t = c_ushort
wctype_t = c_ushort
__time32_t = c_long
__time64_t = c_int64
rsize_t = c_size_t
VOID = c_void
REFTIME = c_double
NMCII_FLAGS = c_int
NMCSAEI_FLAGS = c_int
MP_POPUPFLAGS = c_int
PERSIST_SPROPSTORE_FLAGS = c_int
SIIGBF = c_int
PROPERTYID = c_int
PATTERNID = c_int
EVENTID = c_int
TEXTATTRIBUTEID = c_int
CONTROLTYPEID = c_int
LANDMARKTYPEID = c_int
METADATAID = c_int
HEADINGLEVELID = c_int
CCHAR = c_char
CHAR = c_char
DATE = c_double
DOUBLE = c_double
GPFIDL_FLAGS = c_int
LONG = c_long
LONGLONG = c_int64
REAL = c_float
RPC_STATUS = c_long
UHALF_PTR = c_uint
HALF_PTR = c_int
SHORT = c_short
UCHAR = c_uchar
ULONG = c_ulong
ULONGLONG = c_uint64
USHORT = c_ushort
VARIANT_BOOL = c_short
VARTYPE = c_ushort
WCHAR = c_wchar_t
boolean = c_uchar
byte = c_uchar
cs_byte = byte

__obj = c_void_p
# gdiplusgpstubs
GpGraphics = __obj
GpBrush = __obj
GpTexture = GpBrush
GpSolidFill = GpBrush
GpLineGradient = GpBrush
GpPathGradient = GpBrush
GpHatch = GpBrush
GpPen = __obj
GpCustomLineCap = __obj
GpAdjustableArrowCap = GpCustomLineCap
GpImage = __obj
GpBitmap = GpImage
GpMetafile = GpImage
GpImageAttributes = __obj
GpPath = __obj
GpRegion = __obj
GpPathIterator = __obj
GpFontFamily = __obj
GpFont = __obj
GpStringFormat = __obj
GpFontCollection = __obj
GpInstalledFontCollection = GpFontCollection
GpPrivateFontCollection = GpFontCollection
GpCachedBitmap = __obj
GpMatrix = __obj
# _
CGpEffect = __obj
# GLU
GLUnurbs = __obj
GLUquadric = __obj
GLUtesselator = __obj
GLUnurbsObj = GLUnurbs
GLUquadricObj = GLUquadric
GLUtesselatorObj = GLUtesselator
GLUtriangulatorObj = GLUtesselator
# wtypes
BSTR = __obj
# brotli
# decode
BrotliDecoderStateStruct = __obj
# encode
BrotliEncoderStateStruct = __obj
BrotliEncoderPreparedDictionaryStruct = __obj
# libclang
# BuildSystem
CXVirtualFileOverlay = __obj
CXModuleMapDescriptor = __obj
# CXCompilationDatabase
CXCompilationDatabase = __obj
CXCompileCommands = __obj
CXCompileCommand = __obj
# Index
CXIndex = __obj
CXTargetInfo = __obj
CXTranslationUnit = __obj
CXClientData = __obj
CXFile = __obj
CXDiagnostic = __obj
CXDiagnosticSet = __obj
CXCursorSet = __obj
CXPrintingPolicy = __obj
CXModule = __obj
CXCompletionString = __obj
CXEvalResult = __obj
CXRemapping = __obj
CXIdxClientFile = __obj
CXIdxClientEntity = __obj
CXIdxClientContainer = __obj
CXIdxClientASTFile = __obj
CXIndexAction = __obj
# Rewrite
CXRewriter = __obj
# zstd
# pool
POOL_ctx_s = __obj
# zstd
ZSTD_CCtx_s = __obj
ZSTD_DCtx_s = __obj
ZSTD_CDict_s = __obj
ZSTD_DDict_s = __obj
ZSTD_CCtx_params_s = __obj

__interface = c_void_p
IUnknown = __interface
IDispatch = __interface
IDWriteFontFace = __interface
ID2D1Geometry = __interface
ID2D1Brush = __interface
IActivationFactory = __interface

# circular import
TYPEDESC_U = DWORD

# noinspection PyProtectedMember
time_t = __time32_t if _const._USE_32BIT_TIME_T else __time64_t
DVD_REGISTER = DWORD
ACCESS_MASK = DWORD
ARGB = DWORD
VALID_UOP_SOMTHING_OR_OTHER = DWORD
REFERENCE_TIME = LONGLONG
SHCONTF = DWORD
SHGDNF = DWORD
FILEOPENDIALOGOPTIONS = DWORD
BROWSERFRAMEOPTIONS = DWORD
REFEXPLORERPANE = DWORD
SHCOLSTATEF = DWORD
KF_REDIRECT_FLAGS = DWORD
KF_REDIRECTION_CAPABILITIES = DWORD
PROPERTYUI_FLAGS = DWORD
TRANSFER_ADVISE_STATE = DWORD
EXPCMDSTATE = DWORD
EXPLORERPANESTATE = DWORD
NSTCSTYLE = DWORD
NSTCROOTSTYLE = DWORD
NSTCITEMSTATE = DWORD
SPINITF = DWORD
PROPERTYUI_NAME_FLAGS = DWORD
OPPROGDLGF = DWORD
PDMODE = DWORD
SPBEGINF = DWORD
TRANSFER_SOURCE_FLAGS = DWORD
PROPERTYUI_FORMAT_FLAGS = DWORD
CDBE_ACTIONS = DWORD
NSTCEHITTEST = DWORD
SV3CVW3_FLAGS = DWORD
NSTCECLICKTYPE = DWORD
EXPPS = UINT
SVSIF = UINT
DXGI_USAGE = UINT
OLE_HANDLE = UINT
OLE_XPOS_HIMETRIC = LONG
OLE_YPOS_HIMETRIC = LONG
OLE_XSIZE_HIMETRIC = LONG
OLE_YSIZE_HIMETRIC = LONG
ATOM = WORD
BOOLEAN = BYTE
BOOLAPI = BOOL
COLORREF = DWORD
D2D1_TAG = UINT64
DEVINST = DWORD
DEVNODE = DWORD
DEVPROPID = ULONG
DEVPROPTYPE = ULONG
DLL_DIRECTORY_COOKIE = PVOID
DWORDLONG = ULONGLONG
DWORD_PTR = ULONG_PTR
DISPID = LONG
HREFTYPE = DWORD
FARPROC = INT_PTR
HANDLE = PVOID
GraphicsState = UINT
GraphicsContainer = UINT
HDEVINFO = PVOID
HDSKSPC = PVOID
KPRIORITY = LONG
LANGID = WORD
LCID = DWORD
LP = LPWSTR
LPARAM = LONG_PTR
LRESULT = LONG_PTR
LSTATUS = LONG
MENUTEMPLATEA = VOID
MENUTEMPLATEW = VOID
NEARPROC = INT_PTR
NTSTATUS = LONG
OLECHAR = WCHAR
PROC = INT_PTR
PROPID = ULONG
PSSTDAPI = HRESULT
APP_DEPRECATED_HRESULT = HRESULT
D3D12_GPU_VIRTUAL_ADDRESS = UINT64
WICColor = UINT32
PixelFormat = INT
RETURN_TYPE = DWORD
SCODE = LONG
SFGAOF = ULONG
SICHINTF = DWORD
SIZE_T = ULONG_PTR
STDAPI = HRESULT
WINOLECTLAPI = HRESULT
WNF_CHANGE_STAMP = ULONG
WPARAM = UINT_PTR
HHANDLE = UINT_PTR
TASKID = UINT64
CONNID = DWORD

# noinspection PyProtectedMember
OLECHAR = WCHAR if _const._WIN32 and not _const.OLE2ANSI else c_char
# noinspection PyProtectedMember
LPOLESTR = LPWSTR if _const._WIN32 and not _const.OLE2ANSI else LPSTR
# noinspection PyProtectedMember
LPCOLESTR = LPCWSTR if _const._WIN32 and not _const.OLE2ANSI else LPCSTR
TCHAR = WCHAR if _const.UNICODE else c_char
TBYTE = WCHAR if _const.UNICODE else c_uchar

APARTMENT_SHUTDOWN_REGISTRATION_COOKIE = HANDLE
HOLEMENU = HANDLE
HIMC = HANDLE
HIMCC = HANDLE
HACCEL = HANDLE
HBITMAP = HANDLE
HBRUSH = HANDLE
HCOLORSPACE = HANDLE
HDC = HANDLE
HGLRC = HANDLE
HDESK = HANDLE
HENHMETAFILE = HANDLE
HFONT = HANDLE
HICON = HANDLE
HMENU = HANDLE
HDWP = HANDLE
HGDIOBJ = HANDLE
HGLOBAL = HANDLE
HHOOK = HANDLE
HINSTANCE = HANDLE
HKEY = HANDLE
HKL = HANDLE
HLOCAL = HANDLE
HMETAFILE = HANDLE
HMODULE = HANDLE
HMONITOR = HANDLE
HPAINTBUFFER = HANDLE
HPALETTE = HANDLE
HPEN = HANDLE
HRGN = HANDLE
HRSRC = HANDLE
HINTERNET = HANDLE
HSTR = HANDLE
HSTRING = HANDLE
HTASK = HANDLE
HTHEME = HANDLE
HUMPD = HANDLE
HWINEVENTHOOK = HANDLE
HWINSTA = HANDLE
HWND = HANDLE
SC_HANDLE = HANDLE
SERVICE_STATUS_HANDLE = HANDLE

PROPVAR_PAD1 = BYTE if _const.MIDL_PASS else WORD
PROPVAR_PAD2 = BYTE if _const.MIDL_PASS else WORD
PROPVAR_PAD3 = ULONG if _const.MIDL_PASS else WORD

ARGB64 = DWORDLONG
CONFIGRET = RETURN_TYPE
HCURSOR = HICON
REGSAM = DWORD
SHSTDAPI = STDAPI
MEMBERID = DISPID
HSEMAPHORE = DWORD_PTR
HEVENT = DWORD_PTR

LPCSTR_PROXY = ULONG_PTR
LPCWSTR_PROXY = ULONG_PTR
LPSTR_PROXY = ULONG_PTR
LPWSTR_PROXY = ULONG_PTR

# cfgmgr32
LOG_CONF = DWORD_PTR
RES_DES = DWORD_PTR
RESOURCEID = ULONG
PRIORITY = ULONG
RANGE_LIST = DWORD_PTR
RANGE_ELEMENT = DWORD_PTR
HMACHINE = HANDLE
CONFLICT_LIST = DWORD_PTR
DEVINSTID_A = PCHAR
DEVINSTID_W = PWCHAR
HCMNOTIFICATION = HANDLE
REGDISPOSITION = ULONG

# computedefs
HCS_SYSTEM = HANDLE
HCS_PROCESS = HANDLE
HCS_OPERATION = HANDLE
HCS_CALLBACK = HANDLE

# dwmapi
HTHUMBNAIL = HANDLE

# GL
GLenum = c_uint
GLboolean = c_uchar
GLbitfield = c_uint
GLbyte = c_char
GLshort = c_short
GLint = c_int
GLsizei = c_int
GLubyte = c_uchar
GLushort = c_ushort
GLuint = c_uint
GLfloat = c_float
GLclampf = c_float
GLdouble = c_double
GLclampd = c_double
GLvoid = c_void

# hstring
HSTRING_BUFFER = HANDLE

# RoMetadataApi
HCORENUM = c_int3264
COR_SIGNATURE = c_uchar
mdToken = ULONG32
mdModule = mdToken
mdTypeRef = mdToken
mdTypeDef = mdToken
mdFieldDef = mdToken
mdMethodDef = mdToken
mdParamDef = mdToken
mdInterfaceImpl = mdToken
mdMemberRef = mdToken
mdCustomAttribute = mdToken
mdPermission = mdToken
mdSignature = mdToken
mdEvent = mdToken
mdProperty = mdToken
mdModuleRef = mdToken
mdAssembly = mdToken
mdAssemblyRef = mdToken
mdFile = mdToken
mdExportedType = mdToken
mdManifestResource = mdToken
mdTypeSpec = mdToken
mdGenericParam = mdToken
mdMethodSpec = mdToken
mdGenericParamConstraint = mdToken
mdString = mdToken

# wincontypes
HPCON = HANDLE

# wincrypt
ALG_ID = c_uint
HCRYPTPROV = ULONG_PTR
HCRYPTKEY = ULONG_PTR
HCRYPTHASH = ULONG_PTR

ABORTPROC: _Callable[..., _Callable[
    [HDC, c_int], BOOL]] = _callable()
APPLICATION_RECOVERY_CALLBACK: _Callable[..., _Callable[
    [PVOID], DWORD]] = _callable()
BFFCALLBACK: _Callable[..., _Callable[
    [HWND, UINT, LPARAM, LPARAM], c_int]] = _callable()
DebugEventProc: _Callable[..., _Callable[
    [_enum.DebugEventLevel, PCHAR], VOID]] = _callable()
DLGPROC: _Callable[..., _Callable[
    [HWND, UINT, WPARAM, LPARAM], INT_PTR]] = _callable()
DLLGETVERSIONPROC: _Callable[..., _Callable[
    [_Pointer[_struct.DLLVERSIONINFO]], HRESULT]] = _callable()
DRAWSTATEPROC: _Callable[..., _Callable[
    [HDC, LPARAM, WPARAM, c_int, c_int], BOOL]] = _callable()
ENUMRESNAMEPROCA: _Callable[..., _Callable[
    [HMODULE, LPCSTR_PROXY, LPSTR_PROXY, LONG_PTR], BOOL]] = _callable()
ENUMRESNAMEPROCW: _Callable[..., _Callable[
    [HMODULE, LPCWSTR_PROXY, LPWSTR_PROXY, LONG_PTR], BOOL]] = _callable()
ENUMRESLANGPROCA: _Callable[..., _Callable[
    [HMODULE, LPCSTR_PROXY, LPCSTR_PROXY, WORD, LONG_PTR], BOOL]] = _callable()
ENUMRESLANGPROCW: _Callable[..., _Callable[
    [HMODULE, LPCWSTR_PROXY, LPCWSTR_PROXY, WORD, LONG_PTR], BOOL]] = _callable()
ENUMRESTYPEPROCA: _Callable[..., _Callable[
    [HMODULE, LPCSTR_PROXY, LONG_PTR], BOOL]] = _callable()
ENUMRESTYPEPROCW: _Callable[..., _Callable[
    [HMODULE, LPCWSTR_PROXY, LONG_PTR], BOOL]] = _callable()
GRAYSTRINGPROC: _Callable[..., _Callable[
    [HDC, LPARAM, c_int], BOOL]] = _callable()
HOOKPROC: _Callable[..., _Callable[
    [c_int, WPARAM, LPARAM], LRESULT]] = _callable()
ImageAbort: _Callable[..., _Callable[
    [PVOID], BOOL]] = _callable()
LPCCHOOKPROC: _Callable[..., _Callable[
    [HWND, UINT, WPARAM, LPARAM], UINT_PTR]] = _callable()
LPENCLAVE_ROUTINE: _Callable[..., _Callable[
    [LPVOID], LPVOID]] = _callable()
LPTHREAD_START_ROUTINE: _Callable[..., _Callable[
    [LPVOID], DWORD]] = _callable()
MONITORENUMPROC: _Callable[..., _Callable[
    [HMONITOR, HDC, _Pointer[_struct.RECT], LPARAM], BOOL]] = _callable()
PHANDLER_ROUTINE: _Callable[..., _Callable[
    [DWORD], BOOL]] = _callable()
PROPENUMPROCA: _Callable[..., _Callable[
    [HWND, LPCSTR, HANDLE], BOOL]] = _callable()
PROPENUMPROCW: _Callable[..., _Callable[
    [HWND, LPCWSTR, HANDLE], BOOL]] = _callable()
PROPENUMPROCEXA: _Callable[..., _Callable[
    [HWND, LPSTR, HANDLE, ULONG_PTR], BOOL]] = _callable()
PROPENUMPROCEXW: _Callable[..., _Callable[
    [HWND, LPWSTR, HANDLE, ULONG_PTR], BOOL]] = _callable()
PTIMERAPCROUTINE: _Callable[..., _Callable[
    [LPVOID, DWORD, DWORD], VOID]] = _callable()
SENDASYNCPROC: _Callable[..., _Callable[
    [HWND, UINT, ULONG_PTR, LRESULT], VOID]] = _callable()
TIMERPROC: _Callable[..., _Callable[
    [HWND, UINT, UINT_PTR, DWORD], VOID]] = _callable()
WINEVENTPROC: _Callable[..., _Callable[
    [HWINEVENTHOOK, DWORD, HWND, LONG, LONG, DWORD, DWORD], VOID]] = _callable()
WNDENUMPROC: _Callable[..., _Callable[
    [HWND, LPARAM], BOOL]] = _callable()
WNDPROC: _Callable[..., _Callable[
    [HWND, UINT, WPARAM, LPARAM], LRESULT]] = _callable()
EnumerateMetafileProc: _Callable[..., _Callable[
    [_enum.EmfPlusRecordType, UINT, UINT, _Pointer[BYTE], PVOID], BOOL]] = _callable()
GdiplusAbort: _Callable[..., _Callable[
    [], HRESULT]] = _callable()
PD2D1_EFFECT_FACTORY: _Callable[..., _Callable[
    [_Pointer[IUnknown]], HRESULT]] = _callable()
PFN_DESTRUCTION_CALLBACK: _Callable[..., _Callable[
    [c_void_p], c_void]] = _callable()
WAITORTIMERCALLBACKFUNC: _Callable[..., _Callable[
    [PVOID, BOOLEAN], VOID]] = _callable()
WORKERCALLBACKFUNC: _Callable[..., _Callable[
    [PVOID], VOID]] = _callable()
SUBCLASSPROC: _Callable[..., _Callable[
    [HWND, UINT, WPARAM, LPARAM, UINT_PTR, DWORD_PTR], LRESULT]] = _callable()
APC_CALLBACK_FUNCTION: _Callable[..., _Callable[
    [DWORD, PVOID, PVOID], VOID]] = _callable()
PFLS_CALLBACK_FUNCTION: _Callable[..., _Callable[
    [PVOID], VOID]] = _callable()
PSECURE_MEMORY_CACHE_CALLBACK: _Callable[..., _Callable[
    [PVOID, SIZE_T], BOOLEAN]] = _callable()
LPOVERLAPPED_COMPLETION_ROUTINE: _Callable[..., _Callable[
    [DWORD, DWORD, _Pointer[_struct.OVERLAPPED]], VOID]] = _callable()
FExecuteInAppDomainCallback: _Callable[..., _Callable[
    [c_void_p], HRESULT]] = _callable()
PFNProgressNotification: _Callable[..., _Callable[
    [LPVOID, ULONG, _enum.WICProgressOperation, c_double], HRESULT]] = _callable()
GOBJENUMPROC: _Callable[..., _Callable[
    [LPVOID, LPARAM], c_int]] = _callable()
LINEDDAPROC: _Callable[..., _Callable[
    [c_int, c_int, LPARAM], VOID]] = _callable()
ICMENUMPROCA: _Callable[..., _Callable[
    [LPSTR, LPARAM], c_int]] = _callable()
ICMENUMPROCW: _Callable[..., _Callable[
    [LPWSTR, LPARAM], c_int]] = _callable()
PFNGETACTIVATIONFACTORY: _Callable[..., _Callable[
    [HSTRING, _Pointer[IActivationFactory]], HRESULT]] = _callable()
CXCursorVisitor: _Callable[..., _Callable[
    [_Pointer[_struct.CXCursor], _Pointer[_struct.CXCursor], CXClientData], _enum_libclang.CXChildVisitResult]] = _callable()
CXInclusionVisitor: _Callable[..., _Callable[
    [CXFile, _Pointer[_struct.CXSourceLocation], c_uint, CXClientData], c_void]] = _callable()
CXFieldVisitor: _Callable[..., _Callable[
    [_Pointer[_struct.CXCursor], CXClientData], _enum_libclang.CXVisitorResult]] = _callable()
CXCursorAndRangeVisitor_visit: _Callable[..., _Callable[
    [c_void_p, _struct.CXCursor, _struct.CXSourceRange], _enum_libclang.CXVisitorResult]] = _callable()
IViewObject_Draw_pfnContinue: _Callable[..., _Callable[
    [ULONG_PTR], BOOL]] = _callable()

# TODO
DrawImageAbort: _Callable[..., _Callable[
    [PVOID], BOOL]] = ImageAbort
GetThumbnailImageAbort: _Callable[..., _Callable[
    [PVOID], BOOL]] = ImageAbort
WAITORTIMERCALLBACK: _Callable[..., _Callable[
    [PVOID, BOOLEAN], VOID]] = WAITORTIMERCALLBACKFUNC

# brotli
# decode
brotli_decoder_metadata_start_func: _Callable[..., _Callable[
    [c_void_p, c_size_t], c_void]] = _callable()
brotli_decoder_metadata_chunk_func: _Callable[..., _Callable[
    [c_void_p, c_size_t], c_void]] = _callable()
# types
brotli_alloc_func: _Callable[..., _Callable[
    [c_void_p, c_size_t], c_void_p]] = _callable()
brotli_free_func: _Callable[..., _Callable[
    [c_void_p, c_void_p], c_void]] = _callable()

# ChromaSDK
# RzChromaSDKTypes
RZRESULT = LONG
RZDURATION = c_uint
RZSIZE = c_size_t
PRZPARAM = c_void_p
RZID = DWORD
RZCOLOR = DWORD
# CChromaEditor
DebugLogPtr: _Callable[..., _Callable[
    [c_char_p], c_void]] = _callable()

# iCUESDK
# iCUESDK
CorsairLedLuid = c_uint
CorsairSessionStateChangedHandler: _Callable[..., _Callable[
    [c_void_p, _Pointer[_struct.CorsairSessionStateChanged]], c_void]] = _callable()
CorsairAsyncCallback: _Callable[..., _Callable[
    [c_void_p, _Pointer[_enum_iCUESDK.CorsairError]], c_void]] = _callable()
CorsairEventHandler: _Callable[..., _Callable[
    [c_void_p, _Pointer[_struct.CorsairEvent]], c_void]] = _callable()

# MysticLightSDK
# MysticLight_Test(C++)
CallbackDelegate: _Callable[..., _Callable[
    [], c_void]] = _callable()

# zstd
# zstd
ZSTD_allocFunction: _Callable[..., _Callable[
    [c_void_p, c_size_t], c_void_p]] = _callable()
ZSTD_freeFunction: _Callable[..., _Callable[
    [c_void_p, c_void_p], c_void]] = _callable()
ZSTD_sequenceProducer_F: _Callable[..., _Callable[
    [c_void_p, _Pointer[_struct.ZSTD_Sequence], c_size_t, c_void_p,
     c_size_t, c_void_p, c_size_t, c_int, c_size_t], c_size_t]] = _callable()


def _setattr(self: _PyCSimpleType, name: str, value):
    _ctypes.cast(id(self) + type(self).__dictoffset__, _ctypes.POINTER(_ctypes.py_object)).contents.value[name] = value


def _instancecheck(self: _PyCSimpleType, instance, *,
                   __instancecheck: _Callable[[_PyCSimpleType, _Any], bool] = _PyCSimpleType.__instancecheck__) -> bool:
    return __instancecheck(self, instance) or _subclasscheck(self, type(instance))


def _subclasscheck(self: _PyCSimpleType, subclass, *,
                   __subclasscheck: _Callable[[_PyCSimpleType, type], bool] = _PyCSimpleType.__subclasscheck__) -> bool:
    return __subclasscheck(self, subclass) or (((proxy_self := getattr(self, '_proxy', None)) is not None and __subclasscheck(
        proxy_self, subclass)) or ((proxy_subclass := getattr(subclass, '_proxy', None)) is not None and __subclasscheck(
        self, proxy_subclass)) or (proxy_self is not None and proxy_subclass is not None and __subclasscheck(proxy_self, proxy_subclass)))  # NOQA


# noinspection PyUnresolvedReferences,PyProtectedMember
del _ctypes.HRESULT._check_retval_
_setattr(_PyCSimpleType, '__instancecheck__', _instancecheck)
_setattr(_PyCSimpleType, '__subclasscheck__', _subclasscheck)
_setattr(__ctypes.Array, '__str__', lambda self: (f'<Array: {self._type_.__name__}<{self._length_}>'
                                                  f'<{", ".join(str(obj) for obj in self)}>>'))


class _TypeMixin:
    def __init__(self, value=None):
        self.value = value

    del __init__

    def __lt__(self, other) -> bool:
        return self.value.__lt__(getattr(other, 'value', other))

    def __le__(self, other) -> bool:
        return self.value.__le__(getattr(other, 'value', other))

    def __eq__(self, other) -> bool:
        return self.value.__eq__(getattr(other, 'value', other))

    def __ne__(self, other) -> bool:
        return self.value.__ne__(getattr(other, 'value', other))

    def __gt__(self, other) -> bool:
        return self.value.__gt__(getattr(other, 'value', other))

    def __ge__(self, other) -> bool:
        return self.value.__ge__(getattr(other, 'value', other))

    def __hash__(self):
        return self.value.__hash__()

    def __bool__(self) -> bool:
        return self.value.__bool__()

    def __len__(self) -> int:
        return self.value.__len__()

    def __add__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__add__(getattr(other, 'value', other)))

    def __sub__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__sub__(getattr(other, 'value', other)))

    def __mul__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__mul__(getattr(other, 'value', other)))

    def __matmul__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__matmul__(getattr(other, 'value', other)))

    def __truediv__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__truediv__(getattr(other, 'value', other)))

    def __floordiv__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__floordiv__(getattr(other, 'value', other)))

    def __mod__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__mod__(getattr(other, 'value', other)))

    def __divmod__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__divmod__(getattr(other, 'value', other)))

    def __pow__(self, other, modulo=None) -> _TypeMixin:
        return self.__class__(self.value.__pow__(getattr(other, 'value', other), modulo))

    def __lshift__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__lshift__(getattr(other, 'value', other)))

    def __rshift__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rshift__(getattr(other, 'value', other)))

    def __and__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__and__(getattr(other, 'value', other)))

    def __xor__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__xor__(getattr(other, 'value', other)))

    def __or__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__or__(getattr(other, 'value', other)))

    def __radd__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__radd__(getattr(other, 'value', other)))

    def __rsub__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rsub__(getattr(other, 'value', other)))

    def __rmul__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rmul__(getattr(other, 'value', other)))

    def __rmatmul__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rmatmul__(getattr(other, 'value', other)))

    def __rtruediv__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rtruediv__(getattr(other, 'value', other)))

    def __rfloordiv__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rfloordiv__(getattr(other, 'value', other)))

    def __rmod__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rmod__(getattr(other, 'value', other)))

    def __rdivmod__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rdivmod__(getattr(other, 'value', other)))

    def __rpow__(self, other, modulo=None) -> _TypeMixin:
        return self.__class__(self.value.__rpow__(getattr(other, 'value', other), modulo))

    def __rlshift__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rlshift__(getattr(other, 'value', other)))

    def __rrshift__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rrshift__(getattr(other, 'value', other)))

    def __rand__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rand__(getattr(other, 'value', other)))

    def __rxor__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__rxor__(getattr(other, 'value', other)))

    def __ror__(self, other) -> _TypeMixin:
        return self.__class__(self.value.__ror__(getattr(other, 'value', other)))

    def __iadd__(self, other):
        self.value = self.value.__add__(getattr(other, 'value', other))

    def __isub__(self, other):
        self.value = self.value.__sub__(getattr(other, 'value', other))

    def __imul__(self, other):
        self.value = self.value.__mul__(getattr(other, 'value', other))

    def __imatmul__(self, other):
        self.value = self.value.__matmul__(getattr(other, 'value', other))

    def __itruediv__(self, other):
        self.value = self.value.__itruediv__(getattr(other, 'value', other))

    def __ifloordiv__(self, other):
        self.value = self.value.__floordiv__(getattr(other, 'value', other))

    def __imod__(self, other):
        self.value = self.value.__mod__(getattr(other, 'value', other))

    def __ipow__(self, other):
        self.value = self.value.__pow__(getattr(other, 'value', other))

    def __ilshift__(self, other):
        self.value = self.value.__lshift__(getattr(other, 'value', other))

    def __irshift__(self, other):
        self.value = self.value.__rshift__(getattr(other, 'value', other))

    def __iand__(self, other):
        self.value = self.value.__and__(getattr(other, 'value', other))

    def __ixor__(self, other):
        self.value = self.value.__xor__(getattr(other, 'value', other))

    def __ior__(self, other):
        self.value = self.value.__ior__(getattr(other, 'value', other))

    def __neg__(self) -> _TypeMixin:
        return self.__class__(self.value.__neg__())

    def __pos__(self) -> _TypeMixin:
        return self.__class__(self.value.__pos__())

    def __abs__(self) -> _TypeMixin:
        return self.__class__(self.value.__abs__())

    def __invert__(self) -> _TypeMixin:
        return self.__class__(self.value.__invert__())

    def __complex__(self) -> complex:
        return complex(self.value)

    def __int__(self) -> int:
        return self.value.__int__()

    def __float__(self) -> float:
        return self.value.__float__()

    def __index__(self) -> int:
        return self.value.__index__()

    def __round__(self) -> _TypeMixin:
        return self.__class__(self.value.__round__())

    def __trunc__(self) -> _TypeMixin:
        return self.__class__(self.value.__trunc__())

    def __floor__(self) -> _TypeMixin:
        return self.__class__(self.value.__floor__())

    def __ceil__(self) -> _TypeMixin:
        return self.__class__(self.value.__ceil__())


# noinspection PyUnresolvedReferences,PyProtectedMember
def _init(item: str) -> type[_SimpleCData] | type[_ctypes._CFuncPtr]:
    var = _globals.vars[item]
    if var is None:
        c_type = _ctypes.CFUNCTYPE(*_resolve_type(_typing.get_args(
            eval(__annotations__[item], _globals))[1]))
    else:
        c_type = _resolve_type(var)
        if item != c_type.__name__:
            c_dict = _TypeMixin.__dict__.copy()
            c_dict.update(c_type.__dict__)
            c_dict['_proxy'] = c_type
            c_type = type(item, (_SimpleCData,), c_dict)
    return c_type


_globals = _Globals(globals(), True)

from ._ import CorsairDeviceId  # NOQA E402

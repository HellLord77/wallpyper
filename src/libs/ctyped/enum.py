from __future__ import annotations as _

import enum as _enum
import functools as _functools
import sys as _sys
from typing import Optional as _Optional, Union as _Union

from . import type as _type
from ._utils import _Globals

_AUTO = _sys.maxsize
_ASSIGNED = ('__str__', *(assigned for assigned in _functools.WRAPPER_ASSIGNMENTS))


class _IntEnumMeta(_enum.EnumMeta):
    # noinspection PyMethodOverriding
    @staticmethod
    def __call__(value: _Optional[int] = None):
        pass


class _IntEnum(_enum.IntEnum, metaclass=_IntEnumMeta):
    pass


class AsyncStatus(_IntEnum):
    Started = _AUTO
    Completed = _AUTO
    Canceled = _AUTO
    Error = _AUTO


class ColorAdjustType(_IntEnum):
    ColorAdjustTypeDefault = _AUTO
    ColorAdjustTypeBitmap = _AUTO
    ColorAdjustTypeBrush = _AUTO
    ColorAdjustTypePen = _AUTO
    ColorAdjustTypeText = _AUTO
    ColorAdjustTypeCount = _AUTO
    ColorAdjustTypeAny = _AUTO


class ColorMatrixFlags(_IntEnum):
    ColorMatrixFlagsDefault = _AUTO
    ColorMatrixFlagsSkipGrays = _AUTO
    ColorMatrixFlagsAltGray = _AUTO


class CreationCollisionOption(_IntEnum):
    GenerateUniqueName = _AUTO
    ReplaceExisting = _AUTO
    FailIfExists = _AUTO
    OpenIfExists = _AUTO


class ApplicationDataCreateDisposition(_IntEnum):
    Always = _AUTO
    Existing = _AUTO


class ApplicationDataLocality(_IntEnum):
    Local = _AUTO
    Roaming = _AUTO
    Temporary = _AUTO
    LocalCache = _AUTO
    SharedLocal = _AUTO


class FileAccessMode(_IntEnum):
    Read = _AUTO
    ReadWrite = _AUTO


class FileAttributes(_IntEnum):
    Normal = _AUTO
    ReadOnly = 0x1
    Directory = 0x10
    Archive = 0x20
    Temporary = 0x100
    LocallyIncomplete = 0x200


class KnownFolderId(_IntEnum):
    AppCaptures = _AUTO
    CameraRoll = _AUTO
    DocumentsLibrary = _AUTO
    HomeGroup = _AUTO
    MediaServerDevices = _AUTO
    MusicLibrary = _AUTO
    Objects3D = _AUTO
    PicturesLibrary = _AUTO
    Playlists = _AUTO
    RecordedCalls = _AUTO
    RemovableDevices = _AUTO
    SavedPictures = _AUTO
    Screenshots = _AUTO
    VideosLibrary = _AUTO
    AllAppMods = _AUTO
    CurrentAppMods = _AUTO
    DownloadsFolder = _AUTO


class KnownFoldersAccessStatus(_IntEnum):
    DeniedBySystem = _AUTO
    NotDeclaredByApp = _AUTO
    DeniedByUser = _AUTO
    UserPromptRequired = _AUTO
    Allowed = _AUTO
    AllowedPerAppFolder = _AUTO


class KnownLibraryId(_IntEnum):
    Music = _AUTO
    Pictures = _AUTO
    Videos = _AUTO
    Documents = _AUTO


class NameCollisionOption(_IntEnum):
    GenerateUniqueName = _AUTO
    ReplaceExisting = _AUTO
    FailIfExists = _AUTO


class StorageDeleteOption(_IntEnum):
    Default = _AUTO
    PermanentDelete = _AUTO


class StorageLibraryChangeType(_IntEnum):
    Created = _AUTO
    Deleted = _AUTO
    MovedOrRenamed = _AUTO
    ContentsChanged = _AUTO
    MovedOutOfLibrary = _AUTO
    MovedIntoLibrary = _AUTO
    ContentsReplaced = _AUTO
    IndexingStatusChanged = _AUTO
    EncryptionChanged = _AUTO
    ChangeTrackingLost = _AUTO


class StreamedFileFailureMode(_IntEnum):
    Failed = _AUTO
    CurrentlyUnavailable = _AUTO
    Incomplete = _AUTO


# noinspection PyPep8Naming
class DESKTOP_SLIDESHOW_DIRECTION(_IntEnum):
    DSD_FORWARD = _AUTO
    DSD_BACKWARD = _AUTO


# noinspection PyPep8Naming
class DESKTOP_SLIDESHOW_OPTIONS(_IntEnum):
    DSO_SHUFFLEIMAGES = 0x1


# noinspection PyPep8Naming
class DESKTOP_SLIDESHOW_STATE(_IntEnum):
    DSS_ENABLED = 0x1
    DSS_SLIDESHOW = 0x2
    DSS_DISABLED_BY_REMOTE_SESSION = 0x4


# noinspection PyPep8Naming
class DESKTOP_WALLPAPER_POSITION(_IntEnum):
    DWPOS_CENTER = _AUTO
    DWPOS_TILE = _AUTO
    DWPOS_STRETCH = _AUTO
    DWPOS_FIT = _AUTO
    DWPOS_FILL = _AUTO
    DWPOS_SPAN = _AUTO


class DebugEventLevel(_IntEnum):
    DebugEventLevelFatal = _AUTO
    DebugEventLevelWarning = _AUTO


class FILEOPENDIALOGOPTIONS(_IntEnum):
    FOS_OVERWRITEPROMPT = 0x2
    FOS_STRICTFILETYPES = 0x4
    FOS_NOCHANGEDIR = 0x8
    FOS_PICKFOLDERS = 0x20
    FOS_FORCEFILESYSTEM = 0x40
    FOS_ALLNONSTORAGEITEMS = 0x80
    FOS_NOVALIDATE = 0x100
    FOS_ALLOWMULTISELECT = 0x200
    FOS_PATHMUSTEXIST = 0x800
    FOS_FILEMUSTEXIST = 0x1000
    FOS_CREATEPROMPT = 0x2000
    FOS_SHAREAWARE = 0x4000
    FOS_NOREADONLYRETURN = 0x8000
    FOS_NOTESTFILECREATE = 0x10000
    FOS_HIDEMRUPLACES = 0x20000
    FOS_HIDEPINNEDPLACES = 0x40000
    FOS_NODEREFERENCELINKS = 0x100000
    FOS_OKBUTTONNEEDSINTERACTION = 0x200000
    FOS_DONTADDTORECENT = 0x2000000
    FOS_FORCESHOWHIDDEN = 0x10000000
    FOS_DEFAULTNOMINIMODE = 0x20000000
    FOS_FORCEPREVIEWPANEON = 0x40000000
    FOS_SUPPORTSTREAMABLEITEMS = 0x80000000


class GETPROPERTYSTOREFLAGS(_IntEnum):
    GPS_DEFAULT = _AUTO
    GPS_HANDLERPROPERTIESONLY = 0x1
    GPS_READWRITE = 0x2
    GPS_TEMPORARY = 0x4
    GPS_FASTPROPERTIESONLY = 0x8
    GPS_OPENSLOWITEM = 0x10
    GPS_DELAYCREATION = 0x20
    GPS_BESTEFFORT = 0x40
    GPS_NO_OPLOCK = 0x80
    GPS_PREFERQUERYPROPERTIES = 0x100
    GPS_EXTRINSICPROPERTIES = 0x200
    GPS_EXTRINSICPROPERTIESONLY = 0x400
    GPS_VOLATILEPROPERTIES = 0x800
    GPS_VOLATILEPROPERTIESONLY = 0x1000
    GPS_MASK_VALID = 0x1fff


class GenericFontFamily(_IntEnum):
    GenericFontFamilySerif = _AUTO
    GenericFontFamilySansSerif = _AUTO
    GenericFontFamilyMonospace = _AUTO


class MatrixOrder(_IntEnum):
    MatrixOrderPrepend = _AUTO
    MatrixOrderAppend = _AUTO


class WarpMode(_IntEnum):
    WarpModePerspective = _AUTO
    WarpModeBilinear = _AUTO


class LinearGradientMode(_IntEnum):
    LinearGradientModeHorizontal = _AUTO
    LinearGradientModeVertical = _AUTO
    LinearGradientModeForwardDiagonal = _AUTO
    LinearGradientModeBackwardDiagonal = _AUTO


class CombineMode(_IntEnum):
    CombineModeReplace = _AUTO
    CombineModeIntersect = _AUTO
    CombineModeUnion = _AUTO
    CombineModeXor = _AUTO
    CombineModeExclude = _AUTO
    CombineModeComplement = _AUTO


class QualityMode(_IntEnum):
    QualityModeInvalid = -1
    QualityModeDefault = _AUTO
    QualityModeLow = _AUTO
    QualityModeHigh = _AUTO


class FillMode(_IntEnum):
    FillModeAlternate = _AUTO
    FillModeWinding = _AUTO


class InputStreamOptions(_IntEnum):
    None_ = _AUTO
    Partial = 0x1
    ReadAhead = 0x2


# noinspection PyPep8Naming
class KNOWN_FOLDER_FLAG(_IntEnum):
    KF_FLAG_DEFAULT = 0x00000000
    KF_FLAG_FORCE_APP_DATA_REDIRECTION = 0x00080000
    KF_FLAG_RETURN_FILTER_REDIRECTION_TARGET = 0x00040000
    KF_FLAG_FORCE_PACKAGE_REDIRECTION = 0x00020000
    KF_FLAG_NO_PACKAGE_REDIRECTION = 0x00010000
    KF_FLAG_FORCE_APPCONTAINER_REDIRECTION = 0x00020000
    KF_FLAG_NO_APPCONTAINER_REDIRECTION = 0x00010000
    KF_FLAG_CREATE = 0x00008000
    KF_FLAG_DONT_VERIFY = 0x00004000
    KF_FLAG_DONT_UNEXPAND = 0x00002000
    KF_FLAG_NO_ALIAS = 0x00001000
    KF_FLAG_INIT = 0x00000800
    KF_FLAG_DEFAULT_PATH = 0x00000400
    KF_FLAG_NOT_PARENT_RELATIVE = 0x00000200
    KF_FLAG_SIMPLE_IDLIST = 0x00000100
    KF_FLAG_ALIAS_ONLY = 0x80000000


# noinspection PyPep8Naming
class RO_INIT_TYPE(_IntEnum):
    RO_INIT_SINGLETHREADED = _AUTO
    RO_INIT_MULTITHREADED = _AUTO


class SIGDN(_IntEnum):
    SIGDN_NORMALDISPLAY = _AUTO
    SIGDN_PARENTRELATIVEPARSING = 0x80018001
    SIGDN_DESKTOPABSOLUTEPARSING = 0x80028000
    SIGDN_PARENTRELATIVEEDITING = 0x80031001
    SIGDN_DESKTOPABSOLUTEEDITING = 0x8004c000
    SIGDN_FILESYSPATH = 0x80058000
    SIGDN_URL = 0x80068000
    SIGDN_PARENTRELATIVEFORADDRESSBAR = 0x8007c001
    SIGDN_PARENTRELATIVE = 0x80080001
    SIGDN_PARENTRELATIVEFORUI = 0x80094001


class TrustLevel(_IntEnum):
    BaseTrust = _AUTO
    PartialTrust = _AUTO
    FullTrust = _AUTO


class Unit(_IntEnum):
    UnitWorld = _AUTO
    UnitDisplay = _AUTO
    UnitPixel = _AUTO
    UnitPoint = _AUTO
    UnitInch = _AUTO
    UnitDocument = _AUTO
    UnitMillimeter = _AUTO


class Status(_IntEnum):
    Ok = _AUTO
    GenericError = _AUTO
    InvalidParameter = _AUTO
    OutOfMemory = _AUTO
    ObjectBusy = _AUTO
    InsufficientBuffer = _AUTO
    NotImplemented = _AUTO
    Win32Error = _AUTO
    WrongState = _AUTO
    Aborted = _AUTO
    FileNotFound = _AUTO
    ValueOverflow = _AUTO
    AccessDenied = _AUTO
    UnknownImageFormat = _AUTO
    FontFamilyNotFound = _AUTO
    FontStyleNotFound = _AUTO
    NotTrueTypeFont = _AUTO
    UnsupportedGdiplusVersion = _AUTO
    GdiplusNotInitialized = _AUTO
    PropertyNotFound = _AUTO
    PropertyNotSupported = _AUTO
    ProfileNotFound = _AUTO


# noinspection PyPep8Naming
class SHGFP_TYPE(_IntEnum):
    SHGFP_TYPE_CURRENT = _AUTO
    SHGFP_TYPE_DEFAULT = _AUTO


class VARENUM(_IntEnum):
    VT_EMPTY = _AUTO
    VT_NULL = _AUTO
    VT_I2 = _AUTO
    VT_I4 = _AUTO
    VT_R4 = _AUTO
    VT_R8 = _AUTO
    VT_CY = _AUTO
    VT_DATE = _AUTO
    VT_BSTR = _AUTO
    VT_DISPATCH = _AUTO
    VT_ERROR = _AUTO
    VT_BOOL = _AUTO
    VT_VARIANT = _AUTO
    VT_UNKNOWN = _AUTO
    VT_DECIMAL = _AUTO
    VT_I1 = 16
    VT_UI1 = _AUTO
    VT_UI2 = _AUTO
    VT_UI4 = _AUTO
    VT_I8 = _AUTO
    VT_UI8 = _AUTO
    VT_INT = _AUTO
    VT_UINT = _AUTO
    VT_VOID = _AUTO
    VT_HRESULT = _AUTO
    VT_PTR = _AUTO
    VT_SAFEARRAY = _AUTO
    VT_CARRAY = _AUTO
    VT_USERDEFINED = _AUTO
    VT_LPSTR = _AUTO
    VT_LPWSTR = _AUTO
    VT_RECORD = 36
    VT_INT_PTR = _AUTO
    VT_UINT_PTR = _AUTO
    VT_FILETIME = 64
    VT_BLOB = _AUTO
    VT_STREAM = _AUTO
    VT_STORAGE = _AUTO
    VT_STREAMED_OBJECT = _AUTO
    VT_STORED_OBJECT = _AUTO
    VT_BLOB_OBJECT = _AUTO
    VT_CF = _AUTO
    VT_CLSID = _AUTO
    VT_VERSIONED_STREAM = _AUTO
    VT_BSTR_BLOB = 0xfff
    VT_VECTOR = 0x1000
    VT_ARRAY = 0x2000
    VT_BYREF = 0x4000
    VT_RESERVED = 0x8000
    VT_ILLEGAL = 0xffff
    VT_ILLEGALMASKED = 0xfff
    VT_TYPEMASK = 0xfff


# noinspection PyPep8Naming
class SLGP_FLAGS(_IntEnum):
    SLGP_SHORTPATH = 0x1
    SLGP_UNCPRIORITY = 0x2
    SLGP_RAWPATH = 0x4
    SLGP_RELATIVEPRIORITY = 0x8


# noinspection PyPep8Naming
class SLR_FLAGS(_IntEnum):
    SLR_NONE = _AUTO
    SLR_NO_UI = 0x1
    SLR_ANY_MATCH = 0x2
    SLR_UPDATE = 0x4
    SLR_NOUPDATE = 0x8
    SLR_NOSEARCH = 0x10
    SLR_NOTRACK = 0x20
    SLR_NOLINKINFO = 0x40
    SLR_INVOKE_MSI = 0x80
    SLR_NO_UI_WITH_MSG_PUMP = 0x101
    SLR_OFFER_DELETE_WITHOUT_FILE = 0x200
    SLR_KNOWNFOLDER = 0x400
    SLR_MACHINE_IN_LOCAL_TARGET = 0x800
    SLR_UPDATE_MACHINE_AND_SID = 0x1000
    SLR_NO_OBJECT_ID = 0x2000


class RotateFlipType(_IntEnum):
    RotateNoneFlipNone = 0
    Rotate90FlipNone = 1
    Rotate180FlipNone = 2
    Rotate270FlipNone = 3
    RotateNoneFlipX = 4
    Rotate90FlipX = 5
    Rotate180FlipX = 6
    Rotate270FlipX = 7
    RotateNoneFlipY = Rotate180FlipX
    Rotate90FlipY = Rotate270FlipX
    Rotate180FlipY = RotateNoneFlipX
    Rotate270FlipY = Rotate90FlipX
    RotateNoneFlipXY = Rotate180FlipNone
    Rotate90FlipXY = Rotate270FlipNone
    Rotate180FlipXY = RotateNoneFlipNone
    Rotate270FlipXY = Rotate90FlipNone


class COINITBASE(_IntEnum):
    COINITBASE_MULTITHREADED = _AUTO


class COINIT(_IntEnum):
    COINIT_MULTITHREADED = COINITBASE.COINITBASE_MULTITHREADED
    COINIT_APARTMENTTHREADED = 0x2
    COINIT_DISABLE_OLE1DDE = 0x4
    COINIT_SPEED_OVER_MEMORY = 0x8


# noinspection PyPep8Naming
class PROCESS_DPI_AWARENESS(_IntEnum):
    PROCESS_DPI_UNAWARE = _AUTO
    PROCESS_SYSTEM_DPI_AWARE = _AUTO
    PROCESS_PER_MONITOR_DPI_AWARE = _AUTO


# noinspection PyPep8Naming
class MONITOR_DPI_TYPE(_IntEnum):
    MDT_EFFECTIVE_DPI = 0
    MDT_ANGULAR_DPI = _AUTO
    MDT_RAW_DPI = _AUTO
    MDT_DEFAULT = MDT_EFFECTIVE_DPI


# noinspection PyPep8Naming
class OPEN_AS_INFO_FLAGS(_IntEnum):
    OAIF_ALLOW_REGISTRATION = 0x00000001
    OAIF_REGISTER_EXT = 0x00000002
    OAIF_EXEC = 0x00000004
    OAIF_FORCE_REGISTRATION = 0x00000008
    OAIF_HIDE_REGISTRATION = 0x00000020
    OAIF_URL_PROTOCOL = 0x00000040
    OAIF_FILE_IS_URI = 0x00000080


class COINITICOR(_IntEnum):
    COINITCOR_DEFAULT = _AUTO


class COINITIEE(_IntEnum):
    COINITEE_DEFAULT = _AUTO
    COINITEE_DLL = _AUTO
    COINITEE_MAIN = _AUTO


class COUNINITIEE(_IntEnum):
    COUNINITEE_DEFAULT = _AUTO
    COUNINITEE_DLL = _AUTO


# noinspection PyPep8Naming
class HOST_TYPE(_IntEnum):
    HOST_TYPE_DEFAULT = _AUTO
    HOST_TYPE_APPLAUNCH = _AUTO
    HOST_TYPE_CORFLAG = _AUTO


# noinspection PyPep8Naming
class STARTUP_FLAGS(_IntEnum):
    STARTUP_CONCURRENT_GC = 0x1
    STARTUP_LOADER_OPTIMIZATION_MASK = 0x3 << 1
    STARTUP_LOADER_OPTIMIZATION_SINGLE_DOMAIN = 0x1 << 1
    STARTUP_LOADER_OPTIMIZATION_MULTI_DOMAIN = 0x2 << 1
    STARTUP_LOADER_OPTIMIZATION_MULTI_DOMAIN_HOST = 0x3 << 1
    STARTUP_LOADER_SAFEMODE = 0x10
    STARTUP_LOADER_SETPREFERENCE = 0x100
    STARTUP_SERVER_GC = 0x1000
    STARTUP_HOARD_GC_VM = 0x2000
    STARTUP_SINGLE_VERSION_HOSTING_INTERFACE = 0x4000
    STARTUP_LEGACY_IMPERSONATION = 0x10000
    STARTUP_DISABLE_COMMITTHREADSTACK = 0x20000
    STARTUP_ALWAYSFLOW_IMPERSONATION = 0x40000
    STARTUP_TRIM_GC_COMMIT = 0x80000
    STARTUP_ETW = 0x100000
    STARTUP_ARM = 0x400000


# noinspection PyPep8Naming
class CLSID_RESOLUTION_FLAGS(_IntEnum):
    CLSID_RESOLUTION_DEFAULT = _AUTO
    CLSID_RESOLUTION_REGISTERED = _AUTO


# noinspection PyPep8Naming
class RUNTIME_INFO_FLAGS(_IntEnum):
    RUNTIME_INFO_UPGRADE_VERSION = 0x1
    RUNTIME_INFO_REQUEST_IA64 = 0x2
    RUNTIME_INFO_REQUEST_AMD64 = 0x4
    RUNTIME_INFO_REQUEST_X86 = 0x8
    RUNTIME_INFO_DONT_RETURN_DIRECTORY = 0x10
    RUNTIME_INFO_DONT_RETURN_VERSION = 0x20
    RUNTIME_INFO_DONT_SHOW_ERROR_DIALOG = 0x40
    RUNTIME_INFO_IGNORE_ERROR_MODE = 0x1000


# noinspection PyPep8Naming
class APPDOMAIN_SECURITY_FLAGS(_IntEnum):
    APPDOMAIN_SECURITY_DEFAULT = _AUTO
    APPDOMAIN_SECURITY_SANDBOXED = 0x1
    APPDOMAIN_SECURITY_FORBID_CROSSAD_REVERSE_PINVOKE = 0x2
    APPDOMAIN_FORCE_TRIVIAL_WAIT_OPERATIONS = 0x8


class HandPreference(_IntEnum):
    HandPreference_LeftHanded = _AUTO
    HandPreference_RightHanded = _AUTO


class UIElementType(_IntEnum):
    UIElementType_ActiveCaption = _AUTO
    UIElementType_Background = _AUTO
    UIElementType_ButtonFace = _AUTO
    UIElementType_ButtonText = _AUTO
    UIElementType_CaptionText = _AUTO
    UIElementType_GrayText = _AUTO
    UIElementType_Highlight = _AUTO
    UIElementType_HighlightText = _AUTO
    UIElementType_Hotlight = _AUTO
    UIElementType_InactiveCaption = _AUTO
    UIElementType_InactiveCaptionText = _AUTO
    UIElementType_Window = _AUTO
    UIElementType_WindowText = _AUTO
    UIElementType_AccentColor = 1000
    UIElementType_TextHigh = _AUTO
    UIElementType_TextMedium = _AUTO
    UIElementType_TextLow = _AUTO
    UIElementType_TextContrastWithHigh = _AUTO
    UIElementType_NonTextHigh = _AUTO
    UIElementType_NonTextMediumHigh = _AUTO
    UIElementType_NonTextMedium = _AUTO
    UIElementType_NonTextMediumLow = _AUTO
    UIElementType_NonTextLow = _AUTO
    UIElementType_PageBackground = _AUTO
    UIElementType_PopupBackground = _AUTO
    UIElementType_OverlayOutsidePopup = _AUTO


# noinspection PyPep8Naming
class URL_SCHEME(_IntEnum):
    URL_SCHEME_INVALID = -1
    URL_SCHEME_UNKNOWN = _AUTO
    URL_SCHEME_FTP = _AUTO
    URL_SCHEME_HTTP = _AUTO
    URL_SCHEME_GOPHER = _AUTO
    URL_SCHEME_MAILTO = _AUTO
    URL_SCHEME_NEWS = _AUTO
    URL_SCHEME_NNTP = _AUTO
    URL_SCHEME_TELNET = _AUTO
    URL_SCHEME_WAIS = _AUTO
    URL_SCHEME_FILE = _AUTO
    URL_SCHEME_MK = _AUTO
    URL_SCHEME_HTTPS = _AUTO
    URL_SCHEME_SHELL = _AUTO
    URL_SCHEME_SNEWS = _AUTO
    URL_SCHEME_LOCAL = _AUTO
    URL_SCHEME_JAVASCRIPT = _AUTO
    URL_SCHEME_VBSCRIPT = _AUTO
    URL_SCHEME_ABOUT = _AUTO
    URL_SCHEME_RES = _AUTO
    URL_SCHEME_MSSHELLROOTED = _AUTO
    URL_SCHEME_MSSHELLIDLIST = _AUTO
    URL_SCHEME_MSHELP = _AUTO
    URL_SCHEME_MSSHELLDEVICE = _AUTO
    URL_SCHEME_WILDCARD = _AUTO
    URL_SCHEME_SEARCH_MS = _AUTO
    URL_SCHEME_SEARCH = _AUTO
    URL_SCHEME_KNOWNFOLDER = _AUTO
    URL_SCHEME_MAXVALUE = _AUTO


# noinspection PyPep8Naming
class URL_PART(_IntEnum):
    URL_PART_NONE = _AUTO
    URL_PART_SCHEME = _AUTO
    URL_PART_HOSTNAME = _AUTO
    URL_PART_USERNAME = _AUTO
    URL_PART_PASSWORD = _AUTO
    URL_PART_PORT = _AUTO
    URL_PART_QUERY = _AUTO


class URLIS(_IntEnum):
    URLIS_URL = _AUTO
    URLIS_OPAQUE = _AUTO
    URLIS_NOHISTORY = _AUTO
    URLIS_FILEURL = _AUTO
    URLIS_APPLIABLE = _AUTO
    URLIS_DIRECTORY = _AUTO
    URLIS_HASQUERY = _AUTO


# noinspection PyPep8Naming
class TA_PROPERTY(_IntEnum):
    TAP_FLAGS = _AUTO
    TAP_TRANSFORMCOUNT = _AUTO
    TAP_STAGGERDELAY = _AUTO
    TAP_STAGGERDELAYCAP = _AUTO
    TAP_STAGGERDELAYFACTOR = _AUTO
    TAP_ZORDER = _AUTO


# noinspection PyPep8Naming
class TA_PROPERTY_FLAG(_IntEnum):
    TAPF_NONE = 0x0
    TAPF_HASSTAGGER = 0x1
    TAPF_ISRTLAWARE = 0x2
    TAPF_ALLOWCOLLECTION = 0x4
    TAPF_HASBACKGROUND = 0x8
    TAPF_HASPERSPECTIVE = 0x10


# noinspection PyPep8Naming
class TA_TRANSFORM_TYPE(_IntEnum):
    TATT_TRANSLATE_2D = _AUTO
    TATT_SCALE_2D = _AUTO
    TATT_OPACITY = _AUTO
    TATT_CLIP = _AUTO


# noinspection PyPep8Naming
class TA_TRANSFORM_FLAG(_IntEnum):
    TATF_NONE = 0x0
    TATF_TARGETVALUES_USER = 0x1
    TATF_HASINITIALVALUES = 0x2
    TATF_HASORIGINVALUES = 0x4


class THEMESIZE(_IntEnum):
    TS_MIN = _AUTO
    TS_TRUE = _AUTO
    TS_DRAW = _AUTO


class PROPERTYORIGIN(_IntEnum):
    PO_STATE = _AUTO
    PO_PART = _AUTO
    PO_CLASS = _AUTO
    PO_GLOBAL = _AUTO
    PO_NOTFOUND = _AUTO


class WINDOWTHEMEATTRIBUTETYPE(_IntEnum):
    WTA_NONCLIENT = 1


# noinspection PyPep8Naming
class BP_ANIMATIONSTYLE(_IntEnum):
    BPAS_NONE = _AUTO
    BPAS_LINEAR = _AUTO
    BPAS_CUBIC = _AUTO
    BPAS_SINE = _AUTO


class MENUSTYLEPARTS(_IntEnum):
    MENU_MENUITEM_TMSCHEMA = 1
    MENU_MENUDROPDOWN_TMSCHEMA = _AUTO
    MENU_MENUBARITEM_TMSCHEMA = _AUTO
    MENU_MENUBARDROPDOWN_TMSCHEMA = _AUTO
    MENU_CHEVRON_TMSCHEMA = _AUTO
    MENU_SEPARATOR_TMSCHEMA = _AUTO
    MENU_BARBACKGROUND = _AUTO
    MENU_BARITEM = _AUTO
    MENU_POPUPBACKGROUND = _AUTO
    MENU_POPUPBORDERS = _AUTO
    MENU_POPUPCHECK = _AUTO
    MENU_POPUPCHECKBACKGROUND = _AUTO
    MENU_POPUPGUTTER = _AUTO
    MENU_POPUPITEM = _AUTO
    MENU_POPUPSEPARATOR = _AUTO
    MENU_POPUPSUBMENU = _AUTO
    MENU_SYSTEMCLOSE = _AUTO
    MENU_SYSTEMMAXIMIZE = _AUTO
    MENU_SYSTEMMINIMIZE = _AUTO
    MENU_SYSTEMRESTORE = _AUTO


class BARBACKGROUNDSTATES(_IntEnum):
    MB_ACTIVE = 1
    MB_INACTIVE = _AUTO


class POPUPCHECKSTATES(_IntEnum):
    MC_CHECKMARKNORMAL = 1
    MC_CHECKMARKDISABLED = _AUTO
    MC_BULLETNORMAL = _AUTO
    MC_BULLETDISABLED = _AUTO


class POPUPCHECKBACKGROUNDSTATES(_IntEnum):
    MCB_DISABLED = 1
    MCB_NORMAL = _AUTO
    MCB_BITMAP = _AUTO


class POPUPITEMSTATES(_IntEnum):
    MPI_NORMAL = 1
    MPI_HOT = _AUTO
    MPI_DISABLED = _AUTO
    MPI_DISABLEDHOT = _AUTO


class POPUPSUBMENUSTATES(_IntEnum):
    MSM_NORMAL = 1
    MSM_DISABLED = _AUTO


class SYSTEMCLOSESTATES(_IntEnum):
    MSYSC_NORMAL = 1
    MSYSC_DISABLED = _AUTO


class SYSTEMMAXIMIZESTATES(_IntEnum):
    MSYSMX_NORMAL = 1
    MSYSMX_DISABLED = _AUTO


class SYSTEMMINIMIZESTATES(_IntEnum):
    MSYSMN_NORMAL = 1
    MSYSMN_DISABLED = _AUTO


class SYSTEMRESTORESTATES(_IntEnum):
    MSYSR_NORMAL = 1
    MSYSR_DISABLED = _AUTO


# noinspection PyPep8Naming
class COMPUTER_NAME_FORMAT(_IntEnum):
    ComputerNameNetBIOS = _AUTO
    ComputerNameDnsHostname = _AUTO
    ComputerNameDnsDomain = _AUTO
    ComputerNameDnsFullyQualified = _AUTO
    ComputerNamePhysicalNetBIOS = _AUTO
    ComputerNamePhysicalDnsHostname = _AUTO
    ComputerNamePhysicalDnsDomain = _AUTO
    ComputerNamePhysicalDnsFullyQualified = _AUTO
    ComputerNameMax = _AUTO


# noinspection PyPep8Naming
class LOGICAL_PROCESSOR_RELATIONSHIP(_IntEnum):
    RelationProcessorCore = _AUTO
    RelationNumaNode = _AUTO
    RelationCache = _AUTO
    RelationProcessorPackage = _AUTO
    RelationGroup = _AUTO
    RelationProcessorDie = _AUTO
    RelationNumaNodeEx = _AUTO
    RelationProcessorModule = _AUTO
    RelationAll = 0xffff


# noinspection PyPep8Naming
class PROCESSOR_CACHE_TYPE(_IntEnum):
    CacheUnified = _AUTO
    CacheInstruction = _AUTO
    CacheData = _AUTO
    CacheTrace = _AUTO


# noinspection PyPep8Naming
class RTL_UMS_THREAD_INFO_CLASS(_IntEnum):
    UmsThreadInvalidInfoClass = _AUTO
    UmsThreadUserContext = _AUTO
    UmsThreadPriority = _AUTO
    UmsThreadAffinity = _AUTO
    UmsThreadTeb = _AUTO
    UmsThreadIsSuspended = _AUTO
    UmsThreadIsTerminated = _AUTO
    UmsThreadMaxInfoClass = _AUTO


# noinspection PyPep8Naming
class RTL_UMS_SCHEDULER_REASON(_IntEnum):
    UmsSchedulerStartup = _AUTO
    UmsSchedulerThreadBlocked = _AUTO
    UmsSchedulerThreadYield = _AUTO


class SHSTOCKICONID(_IntEnum):
    SIID_DOCNOASSOC = _AUTO
    SIID_DOCASSOC = _AUTO
    SIID_APPLICATION = _AUTO
    SIID_FOLDER = _AUTO
    SIID_FOLDEROPEN = _AUTO
    SIID_DRIVE525 = _AUTO
    SIID_DRIVE35 = _AUTO
    SIID_DRIVEREMOVE = _AUTO
    SIID_DRIVEFIXED = _AUTO
    SIID_DRIVENET = _AUTO
    SIID_DRIVENETDISABLED = _AUTO
    SIID_DRIVECD = _AUTO
    SIID_DRIVERAM = _AUTO
    SIID_WORLD = _AUTO
    SIID_SERVER = 15
    SIID_PRINTER = _AUTO
    SIID_MYNETWORK = _AUTO
    SIID_FIND = 22
    SIID_HELP = _AUTO
    SIID_SHARE = 28
    SIID_LINK = _AUTO
    SIID_SLOWFILE = _AUTO
    SIID_RECYCLER = _AUTO
    SIID_RECYCLERFULL = _AUTO
    SIID_MEDIACDAUDIO = 40
    SIID_LOCK = 47
    SIID_AUTOLIST = 49
    SIID_PRINTERNET = 50
    SIID_SERVERSHARE = _AUTO
    SIID_PRINTERFAX = _AUTO
    SIID_PRINTERFAXNET = _AUTO
    SIID_PRINTERFILE = _AUTO
    SIID_STACK = _AUTO
    SIID_MEDIASVCD = _AUTO
    SIID_STUFFEDFOLDER = _AUTO
    SIID_DRIVEUNKNOWN = _AUTO
    SIID_DRIVEDVD = _AUTO
    SIID_MEDIADVD = _AUTO
    SIID_MEDIADVDRAM = _AUTO
    SIID_MEDIADVDRW = _AUTO
    SIID_MEDIADVDR = _AUTO
    SIID_MEDIADVDROM = _AUTO
    SIID_MEDIACDAUDIOPLUS = _AUTO
    SIID_MEDIACDRW = _AUTO
    SIID_MEDIACDR = _AUTO
    SIID_MEDIACDBURN = _AUTO
    SIID_MEDIABLANKCD = _AUTO
    SIID_MEDIACDROM = _AUTO
    SIID_AUDIOFILES = _AUTO
    SIID_IMAGEFILES = _AUTO
    SIID_VIDEOFILES = _AUTO
    SIID_MIXEDFILES = _AUTO
    SIID_FOLDERBACK = _AUTO
    SIID_FOLDERFRONT = _AUTO
    SIID_SHIELD = _AUTO
    SIID_WARNING = _AUTO
    SIID_INFO = _AUTO
    SIID_ERROR = _AUTO
    SIID_KEY = _AUTO
    SIID_SOFTWARE = _AUTO
    SIID_RENAME = _AUTO
    SIID_DELETE = _AUTO
    SIID_MEDIAAUDIODVD = _AUTO
    SIID_MEDIAMOVIEDVD = _AUTO
    SIID_MEDIAENHANCEDCD = _AUTO
    SIID_MEDIAENHANCEDDVD = _AUTO
    SIID_MEDIAHDDVD = _AUTO
    SIID_MEDIABLURAY = _AUTO
    SIID_MEDIAVCD = _AUTO
    SIID_MEDIADVDPLUSR = _AUTO
    SIID_MEDIADVDPLUSRW = _AUTO
    SIID_DESKTOPPC = _AUTO
    SIID_MOBILEPC = _AUTO
    SIID_USERS = _AUTO
    SIID_MEDIASMARTMEDIA = _AUTO
    SIID_MEDIACOMPACTFLASH = _AUTO
    SIID_DEVICECELLPHONE = _AUTO
    SIID_DEVICECAMERA = _AUTO
    SIID_DEVICEVIDEOCAMERA = _AUTO
    SIID_DEVICEAUDIOPLAYER = _AUTO
    SIID_NETWORKCONNECT = _AUTO
    SIID_INTERNET = _AUTO
    SIID_ZIPFILE = _AUTO
    SIID_SETTINGS = _AUTO
    SIID_DRIVEHDDVD = 132
    SIID_DRIVEBD = _AUTO
    SIID_MEDIAHDDVDROM = _AUTO
    SIID_MEDIAHDDVDR = _AUTO
    SIID_MEDIAHDDVDRAM = _AUTO
    SIID_MEDIABDROM = _AUTO
    SIID_MEDIABDR = _AUTO
    SIID_MEDIABDRE = _AUTO
    SIID_CLUSTEREDDRIVE = _AUTO
    SIID_MAX_ICONS = 181


GpMatrixOrder = MatrixOrder
GpUnit = Unit
GpStatus = Status


class _EnumMeta(type(_type.c_uint)):
    __members__: dict[str, int]

    def __getattr__(self, name: str):
        if name in self.__members__:
            # noinspection PyCallingNonCallable
            val = self(self.__members__[name])
            val._name = name
            setattr(self, name, val)
        return super().__getattribute__(name)

    def __iter__(self):
        for name in self.__members__:
            yield getattr(self, name)


def _get_members(enum: _IntEnum) -> dict[int, str]:
    last = -1
    # noinspection PyUnresolvedReferences,PyProtectedMember
    return {name: (last := (last + 1) if val.value == _AUTO else val.value) for name, val in enum._member_map_.items()}


def _init(item: str) -> type:
    _globals.check_item(item)

    class Enum(_type.c_uint, metaclass=_EnumMeta):
        _name = None
        __members__ = _get_members(_globals.vars_[item])

        def __init__(self, value: _Optional[int] = None):
            if value is None:
                for val in self.__members__.values():
                    value = val
                    break
            super().__init__(value)

        @property
        def _name_(self) -> _Union[int, str]:
            if self._name is None:
                for name, val in self.__members__.items():
                    if self.value == val:
                        return name
                return self.value
            else:
                return self._name

        name = _name_

    return _functools.update_wrapper(Enum, _globals.vars_[item], _ASSIGNED, ())


_globals = _Globals()

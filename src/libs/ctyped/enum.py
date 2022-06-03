from __future__ import annotations as _

import enum as _enum
from typing import Optional as _Optional

from . import type as _type
from ._utils import _CT

_AUTO = object()

if None:
    class _EnumMeta(_enum.EnumMeta):
        # noinspection PyMethodOverriding
        def __call__(cls: type[_CT], value: _Optional[int] = None) -> _CT:
            pass


    class _Enum(_enum.IntEnum, metaclass=_EnumMeta):
        pass
else:
    class _EnumMeta(type(_type.c_int)):
        def __getattr__(self, name: str):
            if name in self._members:
                # noinspection PyCallingNonCallable
                setattr(self, name, self(self._members[name]))
            return super().__getattribute__(name)

        def __iter__(self):
            for name in self._members:
                yield getattr(self, name)

        def __str__(self):
            return f'{self.__name__}{str(self._members)}'.replace("'", '')


    class _Enum(_type.c_int, metaclass=_EnumMeta):
        _members: dict[str, int]

        def __init_subclass__(cls):
            last = -1
            cls._members = {}
            for name, val in tuple(vars(cls).items()):
                if not name.startswith('_'):
                    cls._members[name] = last = (last + 1) if val is _AUTO else val
                    delattr(cls, name)

        def __init__(self, value: _Optional[int] = None):
            if value is None:
                value = next(iter(self._members.values()))
            super().__init__(value)

        @property
        def name(self) -> str:
            for name, val in self._members.items():
                if self.value == val:
                    return name
            return str(self.value)

        def __str__(self):
            return f'{type(self).__name__}.{self.name}'


class ColorAdjustType(_Enum):
    Default = _AUTO
    Bitmap = _AUTO
    Brush = _AUTO
    Pen = _AUTO
    Text = _AUTO
    Count = _AUTO
    Any = _AUTO


class ColorMatrixFlags(_Enum):
    Default = _AUTO
    SkipGrays = _AUTO
    AltGray = _AUTO


# noinspection PyPep8Naming
class DESKTOP_SLIDESHOW_DIRECTION(_Enum):
    FORWARD = _AUTO
    BACKWARD = _AUTO


# noinspection PyPep8Naming
class DESKTOP_SLIDESHOW_OPTIONS(_Enum):
    SHUFFLEIMAGES = 0x1


# noinspection PyPep8Naming
class DESKTOP_SLIDESHOW_STATE(_Enum):
    ENABLED = 0x1
    SLIDESHOW = 0x2
    DISABLED_BY_REMOTE_SESSION = 0x4


# noinspection PyPep8Naming
class DESKTOP_WALLPAPER_POSITION(_Enum):
    CENTER = _AUTO
    TILE = _AUTO
    STRETCH = _AUTO
    FIT = _AUTO
    FILL = _AUTO
    SPAN = _AUTO


class DebugEventLevel(_Enum):
    Fatal = _AUTO
    Warning = _AUTO


class FILEOPENDIALOGOPTIONS(_Enum):
    OVERWRITEPROMPT = 0x2
    STRICTFILETYPES = 0x4
    NOCHANGEDIR = 0x8
    PICKFOLDERS = 0x20
    FORCEFILESYSTEM = 0x40
    ALLNONSTORAGEITEMS = 0x80
    NOVALIDATE = 0x100
    ALLOWMULTISELECT = 0x200
    PATHMUSTEXIST = 0x800
    FILEMUSTEXIST = 0x1000
    CREATEPROMPT = 0x2000
    SHAREAWARE = 0x4000
    NOREADONLYRETURN = 0x8000
    NOTESTFILECREATE = 0x10000
    HIDEMRUPLACES = 0x20000
    HIDEPINNEDPLACES = 0x40000
    NODEREFERENCELINKS = 0x100000
    OKBUTTONNEEDSINTERACTION = 0x200000
    DONTADDTORECENT = 0x2000000
    FORCESHOWHIDDEN = 0x10000000
    DEFAULTNOMINIMODE = 0x20000000
    FORCEPREVIEWPANEON = 0x40000000
    SUPPORTSTREAMABLEITEMS = 0x80000000


class GETPROPERTYSTOREFLAGS(_Enum):
    DEFAULT = _AUTO
    HANDLERPROPERTIESONLY = 0x1
    READWRITE = 0x2
    TEMPORARY = 0x4
    FASTPROPERTIESONLY = 0x8
    OPENSLOWITEM = 0x10
    DELAYCREATION = 0x20
    BESTEFFORT = 0x40
    NO_OPLOCK = 0x80
    PREFERQUERYPROPERTIES = 0x100
    EXTRINSICPROPERTIES = 0x200
    EXTRINSICPROPERTIESONLY = 0x400
    VOLATILEPROPERTIES = 0x800
    VOLATILEPROPERTIESONLY = 0x1000
    MASK_VALID = 0x1fff


class GenericFontFamily(_Enum):
    Serif = _AUTO
    SansSerif = _AUTO
    Monospace = _AUTO


class MatrixOrder(_Enum):
    Prepend = _AUTO
    Append = _AUTO


class WarpMode(_Enum):
    Perspective = _AUTO
    Bilinear = _AUTO


class LinearGradientMode(_Enum):
    Horizontal = _AUTO
    Vertical = _AUTO
    ForwardDiagonal = _AUTO
    BackwardDiagonal = _AUTO


class CombineMode(_Enum):
    Replace = _AUTO
    Intersect = _AUTO
    Union = _AUTO
    Xor = _AUTO
    Exclude = _AUTO
    Complement = _AUTO


class QualityMode(_Enum):
    Invalid = -1
    Default = _AUTO
    Low = _AUTO
    High = _AUTO


class CompositingMode(_Enum):
    SourceOver = _AUTO
    SourceCopy = _AUTO


class FillMode(_Enum):
    Alternate = _AUTO
    Winding = _AUTO


# noinspection PyPep8Naming
class KNOWN_FOLDER_FLAG(_Enum):
    DEFAULT = 0x00000000
    FORCE_APP_DATA_REDIRECTION = 0x00080000
    RETURN_FILTER_REDIRECTION_TARGET = 0x00040000
    FORCE_PACKAGE_REDIRECTION = 0x00020000
    NO_PACKAGE_REDIRECTION = 0x00010000
    FORCE_APPCONTAINER_REDIRECTION = 0x00020000
    NO_APPCONTAINER_REDIRECTION = 0x00010000
    CREATE = 0x00008000
    DONT_VERIFY = 0x00004000
    DONT_UNEXPAND = 0x00002000
    NO_ALIAS = 0x00001000
    INIT = 0x00000800
    DEFAULT_PATH = 0x00000400
    NOT_PARENT_RELATIVE = 0x00000200
    SIMPLE_IDLIST = 0x00000100
    ALIAS_ONLY = 0x80000000


# noinspection PyPep8Naming
class RO_INIT_TYPE(_Enum):
    SINGLETHREADED = _AUTO
    MULTITHREADED = _AUTO


class SIGDN(_Enum):
    NORMALDISPLAY = _AUTO
    PARENTRELATIVEPARSING = 0x80018001
    DESKTOPABSOLUTEPARSING = 0x80028000
    PARENTRELATIVEEDITING = 0x80031001
    DESKTOPABSOLUTEEDITING = 0x8004c000
    FILESYSPATH = 0x80058000
    URL = 0x80068000
    PARENTRELATIVEFORADDRESSBAR = 0x8007c001
    PARENTRELATIVE = 0x80080001
    PARENTRELATIVEFORUI = 0x80094001


class TrustLevel(_Enum):
    BaseTrust = _AUTO
    PartialTrust = _AUTO
    FullTrust = _AUTO


class Unit(_Enum):
    World = _AUTO
    Display = _AUTO
    Pixel = _AUTO
    Point = _AUTO
    Inch = _AUTO
    Document = _AUTO
    Millimeter = _AUTO


class Status(_Enum):
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
class SHGFP_TYPE(_Enum):
    CURRENT = _AUTO
    DEFAULT = _AUTO


class VARENUM(_Enum):
    EMPTY = _AUTO
    NULL = _AUTO
    I2 = _AUTO
    I4 = _AUTO
    R4 = _AUTO
    R8 = _AUTO
    CY = _AUTO
    DATE = _AUTO
    BSTR = _AUTO
    DISPATCH = _AUTO
    ERROR = _AUTO
    BOOL = _AUTO
    VARIANT = _AUTO
    UNKNOWN = _AUTO
    DECIMAL = _AUTO
    I1 = 16
    UI1 = _AUTO
    UI2 = _AUTO
    UI4 = _AUTO
    I8 = _AUTO
    UI8 = _AUTO
    INT = _AUTO
    UINT = _AUTO
    VOID = _AUTO
    HRESULT = _AUTO
    PTR = _AUTO
    SAFEARRAY = _AUTO
    CARRAY = _AUTO
    USERDEFINED = _AUTO
    LPSTR = _AUTO
    LPWSTR = _AUTO
    RECORD = 36
    INT_PTR = _AUTO
    UINT_PTR = _AUTO
    FILETIME = 64
    BLOB = _AUTO
    STREAM = _AUTO
    STORAGE = _AUTO
    STREAMED_OBJECT = _AUTO
    STORED_OBJECT = _AUTO
    BLOB_OBJECT = _AUTO
    CF = _AUTO
    CLSID = _AUTO
    VERSIONED_STREAM = _AUTO
    BSTR_BLOB = 0xfff
    VECTOR = 0x1000
    ARRAY = 0x2000
    BYREF = 0x4000
    RESERVED = 0x8000
    ILLEGAL = 0xffff
    ILLEGALMASKED = 0xfff
    TYPEMASK = 0xfff


# noinspection PyPep8Naming
class SLGP_FLAGS(_Enum):
    SHORTPATH = 0x1
    UNCPRIORITY = 0x2
    RAWPATH = 0x4
    RELATIVEPRIORITY = 0x8


# noinspection PyPep8Naming
class SLR_FLAGS(_Enum):
    NONE = _AUTO
    NO_UI = 0x1
    ANY_MATCH = 0x2
    UPDATE = 0x4
    NOUPDATE = 0x8
    NOSEARCH = 0x10
    NOTRACK = 0x20
    NOLINKINFO = 0x40
    INVOKE_MSI = 0x80
    NO_UI_WITH_MSG_PUMP = 0x101
    OFFER_DELETE_WITHOUT_FILE = 0x200
    KNOWNFOLDER = 0x400
    MACHINE_IN_LOCAL_TARGET = 0x800
    UPDATE_MACHINE_AND_SID = 0x1000
    NO_OBJECT_ID = 0x2000


class RotateFlipType(_Enum):
    RNoneFlipNone = 0
    R90FlipNone = 1
    R180FlipNone = 2
    R270FlipNone = 3
    RNoneFlipX = 4
    R90FlipX = 5
    R180FlipX = 6
    R270FlipX = 7
    RNoneFlipY = R180FlipX
    R90FlipY = R270FlipX
    R180FlipY = RNoneFlipX
    R270FlipY = R90FlipX
    RNoneFlipXY = R180FlipNone
    R90FlipXY = R270FlipNone
    R180FlipXY = RNoneFlipNone
    R270FlipXY = R90FlipNone


class COINITBASE(_Enum):
    MULTITHREADED = _AUTO


class COINIT(_Enum):
    MULTITHREADED = COINITBASE.MULTITHREADED
    APARTMENTTHREADED = 0x2
    DISABLE_OLE1DDE = 0x4
    SPEED_OVER_MEMORY = 0x8


# noinspection PyPep8Naming
class PROCESS_DPI_AWARENESS(_Enum):
    DPI_UNAWARE = _AUTO
    SYSTEM_DPI_AWARE = _AUTO
    PER_MONITOR_DPI_AWARE = _AUTO


# noinspection PyPep8Naming
class MONITOR_DPI_TYPE(_Enum):
    EFFECTIVE_DPI = 0
    ANGULAR_DPI = _AUTO
    RAW_DPI = _AUTO
    DEFAULT = EFFECTIVE_DPI


# noinspection PyPep8Naming
class OPEN_AS_INFO_FLAGS(_Enum):
    ALLOW_REGISTRATION = 0x00000001
    REGISTER_EXT = 0x00000002
    EXEC = 0x00000004
    FORCE_REGISTRATION = 0x00000008
    HIDE_REGISTRATION = 0x00000020
    URL_PROTOCOL = 0x00000040
    FILE_IS_URI = 0x00000080


class COINITICOR(_Enum):
    DEFAULT = _AUTO


class COINITIEE(_Enum):
    DEFAULT = _AUTO
    DLL = _AUTO
    MAIN = _AUTO


class COUNINITIEE(_Enum):
    DEFAULT = _AUTO
    DLL = _AUTO


# noinspection PyPep8Naming
class HOST_TYPE(_Enum):
    DEFAULT = _AUTO
    APPLAUNCH = _AUTO
    CORFLAG = _AUTO


# noinspection PyPep8Naming
class STARTUP_FLAGS(_Enum):
    CONCURRENT_GC = 0x1
    LOADER_OPTIMIZATION_MASK = 0x3 << 1
    LOADER_OPTIMIZATION_SINGLE_DOMAIN = 0x1 << 1
    LOADER_OPTIMIZATION_MULTI_DOMAIN = 0x2 << 1
    LOADER_OPTIMIZATION_MULTI_DOMAIN_HOST = 0x3 << 1
    LOADER_SAFEMODE = 0x10
    LOADER_SETPREFERENCE = 0x100
    SERVER_GC = 0x1000
    HOARD_GC_VM = 0x2000
    SINGLE_VERSION_HOSTING_INTERFACE = 0x4000
    LEGACY_IMPERSONATION = 0x10000
    DISABLE_COMMITTHREADSTACK = 0x20000
    ALWAYSFLOW_IMPERSONATION = 0x40000
    TRIM_GC_COMMIT = 0x80000
    ETW = 0x100000
    ARM = 0x400000


# noinspection PyPep8Naming
class CLSID_RESOLUTION_FLAGS(_Enum):
    RESOLUTION_DEFAULT = _AUTO
    RESOLUTION_REGISTERED = _AUTO


# noinspection PyPep8Naming
class RUNTIME_INFO_FLAGS(_Enum):
    UPGRADE_VERSION = 0x1
    REQUEST_IA64 = 0x2
    REQUEST_AMD64 = 0x4
    REQUEST_X86 = 0x8
    DONT_RETURN_DIRECTORY = 0x10
    DONT_RETURN_VERSION = 0x20
    DONT_SHOW_ERROR_DIALOG = 0x40
    IGNORE_ERROR_MODE = 0x1000


# noinspection PyPep8Naming
class APPDOMAIN_SECURITY_FLAGS(_Enum):
    SECURITY_DEFAULT = _AUTO
    SECURITY_SANDBOXED = 0x1
    SECURITY_FORBID_CROSSAD_REVERSE_PINVOKE = 0x2
    FORCE_TRIVIAL_WAIT_OPERATIONS = 0x8


# noinspection PyPep8Naming
class URL_SCHEME(_Enum):
    INVALID = -1
    UNKNOWN = _AUTO
    FTP = _AUTO
    HTTP = _AUTO
    GOPHER = _AUTO
    MAILTO = _AUTO
    NEWS = _AUTO
    NNTP = _AUTO
    TELNET = _AUTO
    WAIS = _AUTO
    FILE = _AUTO
    MK = _AUTO
    HTTPS = _AUTO
    SHELL = _AUTO
    SNEWS = _AUTO
    LOCAL = _AUTO
    JAVASCRIPT = _AUTO
    VBSCRIPT = _AUTO
    ABOUT = _AUTO
    RES = _AUTO
    MSSHELLROOTED = _AUTO
    MSSHELLIDLIST = _AUTO
    MSHELP = _AUTO
    MSSHELLDEVICE = _AUTO
    WILDCARD = _AUTO
    SEARCH_MS = _AUTO
    SEARCH = _AUTO
    KNOWNFOLDER = _AUTO
    MAXVALUE = _AUTO


# noinspection PyPep8Naming
class URL_PART(_Enum):
    NONE = _AUTO
    SCHEME = _AUTO
    HOSTNAME = _AUTO
    USERNAME = _AUTO
    PASSWORD = _AUTO
    PORT = _AUTO
    QUERY = _AUTO


class URLIS(_Enum):
    URL = _AUTO
    OPAQUE = _AUTO
    NOHISTORY = _AUTO
    FILEURL = _AUTO
    APPLIABLE = _AUTO
    DIRECTORY = _AUTO
    HASQUERY = _AUTO


# noinspection PyPep8Naming
class TA_PROPERTY(_Enum):
    FLAGS = _AUTO
    TRANSFORMCOUNT = _AUTO
    STAGGERDELAY = _AUTO
    STAGGERDELAYCAP = _AUTO
    STAGGERDELAYFACTOR = _AUTO
    ZORDER = _AUTO


# noinspection PyPep8Naming
class TA_PROPERTY_FLAG(_Enum):
    NONE = 0x0
    HASSTAGGER = 0x1
    ISRTLAWARE = 0x2
    ALLOWCOLLECTION = 0x4
    HASBACKGROUND = 0x8
    HASPERSPECTIVE = 0x10


# noinspection PyPep8Naming
class TA_TRANSFORM_TYPE(_Enum):
    TRANSLATE_2D = _AUTO
    SCALE_2D = _AUTO
    OPACITY = _AUTO
    CLIP = _AUTO


# noinspection PyPep8Naming
class TA_TRANSFORM_FLAG(_Enum):
    NONE = 0x0
    TARGETVALUES_USER = 0x1
    HASINITIALVALUES = 0x2
    HASORIGINVALUES = 0x4


class THEMESIZE(_Enum):
    MIN = _AUTO
    TRUE = _AUTO
    DRAW = _AUTO


class PROPERTYORIGIN(_Enum):
    STATE = _AUTO
    PART = _AUTO
    CLASS = _AUTO
    GLOBAL = _AUTO
    NOTFOUND = _AUTO


class WINDOWTHEMEATTRIBUTETYPE(_Enum):
    NONCLIENT = 1


# noinspection PyPep8Naming
class BP_ANIMATIONSTYLE(_Enum):
    NONE = _AUTO
    LINEAR = _AUTO
    CUBIC = _AUTO
    SINE = _AUTO


class MENUSTYLEPARTS(_Enum):
    MENUITEM_TMSCHEMA = 1
    MENUDROPDOWN_TMSCHEMA = _AUTO
    MENUBARITEM_TMSCHEMA = _AUTO
    MENUBARDROPDOWN_TMSCHEMA = _AUTO
    CHEVRON_TMSCHEMA = _AUTO
    SEPARATOR_TMSCHEMA = _AUTO
    BARBACKGROUND = _AUTO
    BARITEM = _AUTO
    POPUPBACKGROUND = _AUTO
    POPUPBORDERS = _AUTO
    POPUPCHECK = _AUTO
    POPUPCHECKBACKGROUND = _AUTO
    POPUPGUTTER = _AUTO
    POPUPITEM = _AUTO
    POPUPSEPARATOR = _AUTO
    POPUPSUBMENU = _AUTO
    SYSTEMCLOSE = _AUTO
    SYSTEMMAXIMIZE = _AUTO
    SYSTEMMINIMIZE = _AUTO
    SYSTEMRESTORE = _AUTO


class BARBACKGROUNDSTATES(_Enum):
    ACTIVE = 1
    INACTIVE = _AUTO


class POPUPCHECKSTATES(_Enum):
    CHECKMARKNORMAL = 1
    CHECKMARKDISABLED = _AUTO
    BULLETNORMAL = _AUTO
    BULLETDISABLED = _AUTO


class POPUPCHECKBACKGROUNDSTATES(_Enum):
    DISABLED = 1
    NORMAL = _AUTO
    BITMAP = _AUTO


class POPUPITEMSTATES(_Enum):
    NORMAL = 1
    HOT = _AUTO
    DISABLED = _AUTO
    DISABLEDHOT = _AUTO


class POPUPSUBMENUSTATES(_Enum):
    NORMAL = 1
    DISABLED = _AUTO


class SYSTEMCLOSESTATES(_Enum):
    NORMAL = 1
    DISABLED = _AUTO


class SYSTEMMAXIMIZESTATES(_Enum):
    NORMAL = 1
    DISABLED = _AUTO


class SYSTEMMINIMIZESTATES(_Enum):
    NORMAL = 1
    DISABLED = _AUTO


class SYSTEMRESTORESTATES(_Enum):
    NORMAL = 1
    DISABLED = _AUTO


# noinspection PyPep8Naming
class COMPUTER_NAME_FORMAT(_Enum):
    NetBIOS = _AUTO
    DnsHostname = _AUTO
    DnsDomain = _AUTO
    DnsFullyQualified = _AUTO
    PhysicalNetBIOS = _AUTO
    PhysicalDnsHostname = _AUTO
    PhysicalDnsDomain = _AUTO
    PhysicalDnsFullyQualified = _AUTO
    Max = _AUTO


# noinspection PyPep8Naming
class LOGICAL_PROCESSOR_RELATIONSHIP(_Enum):
    ProcessorCore = _AUTO
    NumaNode = _AUTO
    Cache = _AUTO
    ProcessorPackage = _AUTO
    Group = _AUTO
    ProcessorDie = _AUTO
    NumaNodeEx = _AUTO
    ProcessorModule = _AUTO
    All = 0xffff


# noinspection PyPep8Naming
class PROCESSOR_CACHE_TYPE(_Enum):
    Unified = _AUTO
    Instruction = _AUTO
    Data = _AUTO
    Trace = _AUTO


# noinspection PyPep8Naming
class RTL_UMS_THREAD_INFO_CLASS(_Enum):
    InvalidInfoClass = _AUTO
    UserContext = _AUTO
    Priority = _AUTO
    Affinity = _AUTO
    Teb = _AUTO
    IsSuspended = _AUTO
    IsTerminated = _AUTO
    MaxInfoClass = _AUTO


# noinspection PyPep8Naming
class RTL_UMS_SCHEDULER_REASON(_Enum):
    Startup = _AUTO
    ThreadBlocked = _AUTO
    ThreadYield = _AUTO


class SHSTOCKICONID(_Enum):
    DOCNOASSOC = _AUTO
    DOCASSOC = _AUTO
    APPLICATION = _AUTO
    FOLDER = _AUTO
    FOLDEROPEN = _AUTO
    DRIVE525 = _AUTO
    DRIVE35 = _AUTO
    DRIVEREMOVE = _AUTO
    DRIVEFIXED = _AUTO
    DRIVENET = _AUTO
    DRIVENETDISABLED = _AUTO
    DRIVECD = _AUTO
    DRIVERAM = _AUTO
    WORLD = _AUTO
    SERVER = 15
    PRINTER = _AUTO
    MYNETWORK = _AUTO
    FIND = 22
    HELP = _AUTO
    SHARE = 28
    LINK = _AUTO
    SLOWFILE = _AUTO
    RECYCLER = _AUTO
    RECYCLERFULL = _AUTO
    MEDIACDAUDIO = 40
    LOCK = 47
    AUTOLIST = 49
    PRINTERNET = 50
    SERVERSHARE = _AUTO
    PRINTERFAX = _AUTO
    PRINTERFAXNET = _AUTO
    PRINTERFILE = _AUTO
    STACK = _AUTO
    MEDIASVCD = _AUTO
    STUFFEDFOLDER = _AUTO
    DRIVEUNKNOWN = _AUTO
    DRIVEDVD = _AUTO
    MEDIADVD = _AUTO
    MEDIADVDRAM = _AUTO
    MEDIADVDRW = _AUTO
    MEDIADVDR = _AUTO
    MEDIADVDROM = _AUTO
    MEDIACDAUDIOPLUS = _AUTO
    MEDIACDRW = _AUTO
    MEDIACDR = _AUTO
    MEDIACDBURN = _AUTO
    MEDIABLANKCD = _AUTO
    MEDIACDROM = _AUTO
    AUDIOFILES = _AUTO
    IMAGEFILES = _AUTO
    VIDEOFILES = _AUTO
    MIXEDFILES = _AUTO
    FOLDERBACK = _AUTO
    FOLDERFRONT = _AUTO
    SHIELD = _AUTO
    WARNING = _AUTO
    INFO = _AUTO
    ERROR = _AUTO
    KEY = _AUTO
    SOFTWARE = _AUTO
    RENAME = _AUTO
    DELETE = _AUTO
    MEDIAAUDIODVD = _AUTO
    MEDIAMOVIEDVD = _AUTO
    MEDIAENHANCEDCD = _AUTO
    MEDIAENHANCEDDVD = _AUTO
    MEDIAHDDVD = _AUTO
    MEDIABLURAY = _AUTO
    MEDIAVCD = _AUTO
    MEDIADVDPLUSR = _AUTO
    MEDIADVDPLUSRW = _AUTO
    DESKTOPPC = _AUTO
    MOBILEPC = _AUTO
    USERS = _AUTO
    MEDIASMARTMEDIA = _AUTO
    MEDIACOMPACTFLASH = _AUTO
    DEVICECELLPHONE = _AUTO
    DEVICECAMERA = _AUTO
    DEVICEVIDEOCAMERA = _AUTO
    DEVICEAUDIOPLAYER = _AUTO
    NETWORKCONNECT = _AUTO
    INTERNET = _AUTO
    ZIPFILE = _AUTO
    SETTINGS = _AUTO
    DRIVEHDDVD = 132
    DRIVEBD = _AUTO
    MEDIAHDDVDROM = _AUTO
    MEDIAHDDVDR = _AUTO
    MEDIAHDDVDRAM = _AUTO
    MEDIABDROM = _AUTO
    MEDIABDR = _AUTO
    MEDIABDRE = _AUTO
    CLUSTEREDDRIVE = _AUTO
    MAX_ICONS = 181


# noinspection PyPep8Naming
class QUERY_USER_NOTIFICATION_STATE(_Enum):
    NOT_PRESENT = 1
    BUSY = _AUTO
    RUNNING_D3D_FULL_SCREEN = _AUTO
    PRESENTATION_MODE = _AUTO
    ACCEPTS_NOTIFICATIONS = _AUTO
    QUIET_TIME = _AUTO
    APP = _AUTO


# noinspection PyPep8Naming
class INPUT_MESSAGE_DEVICE_TYPE(_Enum):
    UNAVAILABLE = 0x00000000
    KEYBOARD = 0x00000001
    MOUSE = 0x00000002
    TOUCH = 0x00000004
    PEN = 0x00000008
    TOUCHPAD = 0x00000010


# noinspection PyPep8Naming
class INPUT_MESSAGE_ORIGIN_ID(_Enum):
    UNAVAILABLE = 0x00000000
    HARDWARE = 0x00000001
    INJECTED = 0x00000002
    SYSTEM = 0x00000004


# noinspection PyPep8Naming
class AR_STATE(_Enum):
    ENABLED = 0x0
    DISABLED = 0x1
    SUPPRESSED = 0x2
    REMOTESESSION = 0x4
    MULTIMON = 0x8
    NOSENSOR = 0x10
    NOT_SUPPORTED = 0x20
    DOCKED = 0x40
    LAPTOP = 0x80


# noinspection PyPep8Naming
class ORIENTATION_PREFERENCE(_Enum):
    NONE = 0x0
    LANDSCAPE = 0x1
    PORTRAIT = 0x2
    LANDSCAPE_FLIPPED = 0x4
    PORTRAIT_FLIPPED = 0x8


class InterpolationMode(_Enum):
    Invalid = QualityMode.Invalid
    Default = QualityMode.Default
    LowQuality = QualityMode.Low
    HighQuality = QualityMode.High
    Bilinear = _AUTO
    Bicubic = _AUTO
    NearestNeighbor = _AUTO
    HighQualityBilinear = _AUTO
    HighQualityBicubic = _AUTO


class SmoothingMode(_Enum):
    Invalid = QualityMode.Invalid
    Default = QualityMode.Default
    HighSpeed = QualityMode.Low
    HighQuality = QualityMode.High
    None_ = _AUTO
    AntiAlias = _AUTO


class CompositingQuality(_Enum):
    Invalid = QualityMode.Invalid
    Default = QualityMode.Default
    HighSpeed = QualityMode.Low
    HighQuality = QualityMode.High
    GammaCorrected = _AUTO
    AssumeLinear = _AUTO


class PixelOffsetMode(_Enum):
    Invalid = QualityMode.Invalid
    Default = QualityMode.Default
    HighSpeed = QualityMode.Low
    HighQuality = QualityMode.High
    None_ = _AUTO
    Half = _AUTO


class EncoderParameterValueType(_Enum):
    Byte = 1
    ASCII = _AUTO
    Short = _AUTO
    Long = _AUTO
    Rational = _AUTO
    LongRange = _AUTO
    Undefined = _AUTO
    RationalRange = _AUTO
    Pointer = _AUTO


class EncoderValue(_Enum):
    ColorTypeCMYK = _AUTO
    ColorTypeYCCK = _AUTO
    CompressionLZW = _AUTO
    CompressionCCITT3 = _AUTO
    CompressionCCITT4 = _AUTO
    CompressionRle = _AUTO
    CompressionNone = _AUTO
    ScanMethodInterlaced = _AUTO
    ScanMethodNonInterlaced = _AUTO
    VersionGif87 = _AUTO
    VersionGif89 = _AUTO
    RenderProgressive = _AUTO
    RenderNonProgressive = _AUTO
    TransformRotate90 = _AUTO
    TransformRotate180 = _AUTO
    TransformRotate270 = _AUTO
    TransformFlipHorizontal = _AUTO
    TransformFlipVertical = _AUTO
    MultiFrame = _AUTO
    LastFrame = _AUTO
    Flush = _AUTO
    FrameDimensionTime = _AUTO
    FrameDimensionResolution = _AUTO
    FrameDimensionPage = _AUTO
    ColorTypeGray = _AUTO
    ColorTypeRGB = _AUTO


# noinspection PyPep8Naming
class ACTIVATION_CONTEXT_INFO_CLASS(_Enum):
    ActivationContextBasicInformation = 1
    ActivationContextDetailedInformation = _AUTO
    AssemblyDetailedInformationInActivationContext = _AUTO
    FileInformationInAssemblyOfAssemblyInActivationContext = _AUTO
    RunlevelInformationInActivationContext = _AUTO
    CompatibilityInformationInActivationContext = _AUTO
    ActivationContextManifestResourceName = _AUTO
    MaxActivationContextInfoClass = _AUTO
    AssemblyDetailedInformationInActivationContxt = 3
    FileInformationInAssemblyOfAssemblyInActivationContxt = _AUTO


# noinspection PyPep8Naming
class HARDWARE_COUNTER_TYPE(_Enum):
    PMCCounter = _AUTO
    MaxHardwareCounterType = _AUTO


# noinspection PyPep8Naming
class ACTCTX_REQUESTED_RUN_LEVEL(_Enum):
    UNSPECIFIED = _AUTO
    AS_INVOKER = _AUTO
    HIGHEST_AVAILABLE = _AUTO
    REQUIRE_ADMIN = _AUTO
    NUMBERS = _AUTO


# noinspection PyPep8Naming
class HEAP_INFORMATION_CLASS(_Enum):
    CompatibilityInformation = _AUTO
    EnableTerminationOnCorruption = _AUTO
    OptimizeResources = 3
    Tag = 7


# noinspection PyPep8Naming
class ACTCTX_COMPATIBILITY_ELEMENT_TYPE(_Enum):
    UNKNOWN = _AUTO
    OS = _AUTO
    MITIGATION = _AUTO
    MAXVERSIONTESTED = _AUTO


class DWMWINDOWATTRIBUTE(_Enum):
    NCRENDERING_ENABLED = 1
    NCRENDERING_POLICY = _AUTO
    TRANSITIONS_FORCEDISABLED = _AUTO
    ALLOW_NCPAINT = _AUTO
    CAPTION_BUTTON_BOUNDS = _AUTO
    NONCLIENT_RTL_LAYOUT = _AUTO
    FORCE_ICONIC_REPRESENTATION = _AUTO
    FLIP3D_POLICY = _AUTO
    EXTENDED_FRAME_BOUNDS = _AUTO
    HAS_ICONIC_BITMAP = _AUTO
    DISALLOW_PEEK = _AUTO
    EXCLUDED_FROM_PEEK = _AUTO
    CLOAK = _AUTO
    CLOAKED = _AUTO
    FREEZE_REPRESENTATION = _AUTO
    PASSIVE_UPDATE_MODE = _AUTO
    USE_HOSTBACKDROPBRUSH = _AUTO
    USE_IMMERSIVE_DARK_MODE = 20
    WINDOW_CORNER_PREFERENCE = 33
    BORDER_COLOR = _AUTO
    CAPTION_COLOR = _AUTO
    TEXT_COLOR = _AUTO
    VISIBLE_FRAME_BORDER_THICKNESS = _AUTO
    LAST = _AUTO


# noinspection PyPep8Naming
class DWM_WINDOW_CORNER_PREFERENCE(_Enum):
    DEFAULT = _AUTO
    DONOTROUND = _AUTO
    ROUND = _AUTO
    ROUNDSMALL = _AUTO


class DWMNCRENDERINGPOLICY(_Enum):
    USEWINDOWSTYLE = _AUTO
    DISABLED = _AUTO
    ENABLED = _AUTO
    LAST = _AUTO


class DWMFLIP3DWINDOWPOLICY(_Enum):
    DEFAULT = _AUTO
    EXCLUDEBELOW = _AUTO
    EXCLUDEABOVE = _AUTO
    LAST = _AUTO


# noinspection PyPep8Naming
class XAML_REFERENCETRACKER_DISCONNECT(_Enum):
    DEFAULT = _AUTO
    SUSPEND = _AUTO


GpMatrixOrder = MatrixOrder
GpUnit = Unit
GpStatus = Status


class Windows:
    class ApplicationModel:
        class DataTransfer:
            class ClipboardHistoryItemsResultStatus(_Enum):
                Success = _AUTO
                AccessDenied = _AUTO
                ClipboardHistoryDisabled = _AUTO

            class DataPackageOperation(_Enum):
                None_ = _AUTO
                Copy = 0x1
                Move = 0x2
                Link = 0x4

            class SetHistoryItemAsContentStatus(_Enum):
                Success = _AUTO
                AccessDenied = _AUTO
                ItemDeleted = _AUTO

            class ShareUITheme(_Enum):
                Default = _AUTO
                Light = _AUTO
                Dark = _AUTO

    class Devices:
        class Input:
            class PointerDeviceType(_Enum):
                Touch = _AUTO
                Pen = _AUTO
                Mouse = _AUTO

    class Foundation:
        class AsyncStatus(_Enum):
            Started = _AUTO
            Completed = _AUTO
            Canceled = _AUTO
            Error = _AUTO

        class PropertyType(_Enum):
            Empty = _AUTO
            UInt8 = _AUTO
            Int16 = _AUTO
            UInt16 = _AUTO
            Int32 = _AUTO
            UInt32 = _AUTO
            Int64 = _AUTO
            UInt64 = _AUTO
            Single = _AUTO
            Double = _AUTO
            Char16 = _AUTO
            Boolean = _AUTO
            String = _AUTO
            Inspectable = _AUTO
            DateTime = _AUTO
            TimeSpan = _AUTO
            Guid = _AUTO
            Point = _AUTO
            Size = _AUTO
            Rect = _AUTO
            OtherType = _AUTO
            UInt8Array = 1025
            Int16Array = _AUTO
            UInt16Array = _AUTO
            Int32Array = _AUTO
            UInt32Array = _AUTO
            Int64Array = _AUTO
            UInt64Array = _AUTO
            SingleArray = _AUTO
            DoubleArray = _AUTO
            Char16Array = _AUTO
            BooleanArray = _AUTO
            StringArray = _AUTO
            InspectableArray = _AUTO
            DateTimeArray = _AUTO
            TimeSpanArray = _AUTO
            GuidArray = _AUTO
            PointArray = _AUTO
            SizeArray = _AUTO
            RectArray = _AUTO
            OtherTypeArray = _AUTO

        class Collections:
            class CollectionChange(_Enum):
                Reset = _AUTO
                ItemInserted = _AUTO
                ItemRemoved = _AUTO
                ItemChanged = _AUTO

    class Storage:
        class ApplicationDataCreateDisposition(_Enum):
            Always = _AUTO
            Existing = _AUTO

        class ApplicationDataLocality(_Enum):
            Local = _AUTO
            Roaming = _AUTO
            Temporary = _AUTO
            LocalCache = _AUTO
            SharedLocal = _AUTO

        class CreationCollisionOption(_Enum):
            GenerateUniqueName = _AUTO
            ReplaceExisting = _AUTO
            FailIfExists = _AUTO
            OpenIfExists = _AUTO

        class FileAccessMode(_Enum):
            Read = _AUTO
            ReadWrite = _AUTO

        class FileAttributes(_Enum):
            Normal = _AUTO
            ReadOnly = 0x1
            Directory = 0x10
            Archive = 0x20
            Temporary = 0x100
            LocallyIncomplete = 0x200

        class KnownFolderId(_Enum):
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

        class KnownFoldersAccessStatus(_Enum):
            DeniedBySystem = _AUTO
            NotDeclaredByApp = _AUTO
            DeniedByUser = _AUTO
            UserPromptRequired = _AUTO
            Allowed = _AUTO
            AllowedPerAppFolder = _AUTO

        class KnownLibraryId(_Enum):
            Music = _AUTO
            Pictures = _AUTO
            Videos = _AUTO
            Documents = _AUTO

        class NameCollisionOption(_Enum):
            GenerateUniqueName = _AUTO
            ReplaceExisting = _AUTO
            FailIfExists = _AUTO

        class StorageDeleteOption(_Enum):
            Default = _AUTO
            PermanentDelete = _AUTO

        class StorageItemTypes(_Enum):
            None_ = _AUTO
            File = _AUTO
            Folder = _AUTO

        class StorageLibraryChangeType(_Enum):
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

        class StorageOpenOptions(_Enum):
            None_ = _AUTO
            AllowOnlyReaders = _AUTO
            AllowReadersAndWriters = _AUTO

        class StreamedFileFailureMode(_Enum):
            Failed = _AUTO
            CurrentlyUnavailable = _AUTO
            Incomplete = _AUTO

        class Streams:
            class ByteOrder(_Enum):
                LittleEndian = _AUTO
                BigEndian = _AUTO

            class FileOpenDisposition(_Enum):
                OpenExisting = _AUTO
                OpenAlways = _AUTO
                CreateNew = _AUTO
                CreateAlways = _AUTO
                TruncateExisting = _AUTO

            class InputStreamOptions(_Enum):
                None_ = _AUTO
                Partial = 0x1
                ReadAhead = 0x2

            class UnicodeEncoding(_Enum):
                Utf8 = _AUTO
                Utf16LE = _AUTO
                Utf16BE = _AUTO

    class System:
        class AppDiagnosticInfoWatcherStatus(_Enum):
            Created = _AUTO
            Started = _AUTO
            EnumerationCompleted = _AUTO
            Stopping = _AUTO
            Stopped = _AUTO
            Aborted = _AUTO

        class AppMemoryUsageLevel(_Enum):
            Low = _AUTO
            Medium = _AUTO
            High = _AUTO
            OverLimit = _AUTO

        class AppResourceGroupEnergyQuotaState(_Enum):
            Unknown = _AUTO
            Over = _AUTO
            Under = _AUTO

        class AppResourceGroupExecutionState(_Enum):
            Unknown = _AUTO
            Running = _AUTO
            Suspending = _AUTO
            Suspended = _AUTO
            NotRunning = _AUTO

        class AppResourceGroupInfoWatcherStatus(_Enum):
            Created = _AUTO
            Started = _AUTO
            EnumerationCompleted = _AUTO
            Stopping = _AUTO
            Stopped = _AUTO
            Aborted = _AUTO

        class AutoUpdateTimeZoneStatus(_Enum):
            Attempted = _AUTO
            TimedOut = _AUTO
            Failed = _AUTO

        class DiagnosticAccessStatus(_Enum):
            Unspecified = _AUTO
            Denied = _AUTO
            Limited = _AUTO
            Allowed = _AUTO

        class DispatcherQueuePriority(_Enum):
            Low = -10
            Normal = 0
            High = 10

        class LaunchFileStatus(_Enum):
            Success = _AUTO
            AppUnavailable = _AUTO
            DeniedByPolicy = _AUTO
            FileTypeNotSupported = _AUTO
            Unknown = _AUTO

        class LaunchQuerySupportStatus(_Enum):
            Available = _AUTO
            AppNotInstalled = _AUTO
            AppUnavailable = _AUTO
            NotSupported = _AUTO
            Unknown = _AUTO

        class LaunchQuerySupportType(_Enum):
            Uri = _AUTO
            UriForResults = _AUTO

        class LaunchUriStatus(_Enum):
            Success = _AUTO
            AppUnavailable = _AUTO
            ProtocolUnavailable = _AUTO
            Unknown = _AUTO

        class PowerState(_Enum):
            ConnectedStandby = _AUTO
            SleepS3 = _AUTO

        class ProcessorArchitecture(_Enum):
            X86 = _AUTO
            Arm = 5
            X64 = 9
            Neutral = 11
            Arm64 = _AUTO
            X86OnArm64 = 14
            Unknown = 65535

        class RemoteLaunchUriStatus(_Enum):
            Unknown = _AUTO
            Success = _AUTO
            AppUnavailable = _AUTO
            ProtocolUnavailable = _AUTO
            RemoteSystemUnavailable = _AUTO
            ValueSetTooLarge = _AUTO
            DeniedByLocalSystem = _AUTO
            DeniedByRemoteSystem = _AUTO

        class ShutdownKind(_Enum):
            Shutdown = _AUTO
            Restart = _AUTO

        class UserAgeConsentGroup(_Enum):
            Child = _AUTO
            Minor = _AUTO
            Adult = _AUTO

        class UserAgeConsentResult(_Enum):
            NotEnforced = _AUTO
            Included = _AUTO
            NotIncluded = _AUTO
            Unknown = _AUTO
            Ambiguous = _AUTO

        class UserAuthenticationStatus(_Enum):
            Unauthenticated = _AUTO
            LocallyAuthenticated = _AUTO
            RemotelyAuthenticated = _AUTO

        class UserPictureSize(_Enum):
            Size64x64 = _AUTO
            Size208x208 = _AUTO
            Size424x424 = _AUTO
            Size1080x1080 = _AUTO

        class UserType(_Enum):
            LocalUser = _AUTO
            RemoteUser = _AUTO
            LocalGuest = _AUTO
            RemoteGuest = _AUTO
            SystemManaged = _AUTO

        class UserWatcherStatus(_Enum):
            Created = _AUTO
            Started = _AUTO
            EnumerationCompleted = _AUTO
            Stopping = _AUTO
            Stopped = _AUTO
            Aborted = _AUTO

        class UserWatcherUpdateKind(_Enum):
            Properties = _AUTO
            Picture = _AUTO

        class VirtualKey(_Enum):
            None_ = _AUTO
            LeftButton = _AUTO
            RightButton = _AUTO
            Cancel = _AUTO
            MiddleButton = _AUTO
            XButton1 = _AUTO
            XButton2 = _AUTO
            Back = 8
            Tab = _AUTO
            Clear = 12
            Enter = _AUTO
            Shift = 16
            Control = _AUTO
            Menu = _AUTO
            Pause = _AUTO
            CapitalLock = _AUTO
            Kana = _AUTO
            Hangul = 21
            ImeOn = _AUTO
            Junja = _AUTO
            Final = _AUTO
            Hanja = _AUTO
            Kanji = _AUTO
            ImeOff = _AUTO
            Escape = _AUTO
            Convert = _AUTO
            NonConvert = _AUTO
            Accept = _AUTO
            ModeChange = _AUTO
            Space = _AUTO
            PageUp = _AUTO
            PageDown = _AUTO
            End = _AUTO
            Home = _AUTO
            Left = _AUTO
            Up = _AUTO
            Right = _AUTO
            Down = _AUTO
            Select = _AUTO
            Print = _AUTO
            Execute = _AUTO
            Snapshot = _AUTO
            Insert = _AUTO
            Delete = _AUTO
            Help = _AUTO
            Number0 = _AUTO
            Number1 = _AUTO
            Number2 = _AUTO
            Number3 = _AUTO
            Number4 = _AUTO
            Number5 = _AUTO
            Number6 = _AUTO
            Number7 = _AUTO
            Number8 = _AUTO
            Number9 = _AUTO
            A = 65
            B = _AUTO
            C = _AUTO
            D = _AUTO
            E = _AUTO
            F = _AUTO
            G = _AUTO
            H = _AUTO
            I = _AUTO
            J = _AUTO
            K = _AUTO
            L = _AUTO
            M = _AUTO
            N = _AUTO
            O = _AUTO
            P = _AUTO
            Q = _AUTO
            R = _AUTO
            S = _AUTO
            T = _AUTO
            U = _AUTO
            V = _AUTO
            W = _AUTO
            X = _AUTO
            Y = _AUTO
            Z = _AUTO
            LeftWindows = _AUTO
            RightWindows = _AUTO
            Application = _AUTO
            Sleep = 95
            NumberPad0 = _AUTO
            NumberPad1 = _AUTO
            NumberPad2 = _AUTO
            NumberPad3 = _AUTO
            NumberPad4 = _AUTO
            NumberPad5 = _AUTO
            NumberPad6 = _AUTO
            NumberPad7 = _AUTO
            NumberPad8 = _AUTO
            NumberPad9 = _AUTO
            Multiply = _AUTO
            Add = _AUTO
            Separator = _AUTO
            Subtract = _AUTO
            Decimal = _AUTO
            Divide = _AUTO
            F1 = _AUTO
            F2 = _AUTO
            F3 = _AUTO
            F4 = _AUTO
            F5 = _AUTO
            F6 = _AUTO
            F7 = _AUTO
            F8 = _AUTO
            F9 = _AUTO
            F10 = _AUTO
            F11 = _AUTO
            F12 = _AUTO
            F13 = _AUTO
            F14 = _AUTO
            F15 = _AUTO
            F16 = _AUTO
            F17 = _AUTO
            F18 = _AUTO
            F19 = _AUTO
            F20 = _AUTO
            F21 = _AUTO
            F22 = _AUTO
            F23 = _AUTO
            F24 = _AUTO
            NavigationView = _AUTO
            NavigationMenu = _AUTO
            NavigationUp = _AUTO
            NavigationDown = _AUTO
            NavigationLeft = _AUTO
            NavigationRight = _AUTO
            NavigationAccept = _AUTO
            NavigationCancel = _AUTO
            NumberKeyLock = _AUTO
            Scroll = _AUTO
            LeftShift = 160
            RightShift = _AUTO
            LeftControl = _AUTO
            RightControl = _AUTO
            LeftMenu = _AUTO
            RightMenu = _AUTO
            GoBack = _AUTO
            GoForward = _AUTO
            Refresh = _AUTO
            Stop = _AUTO
            Search = _AUTO
            Favorites = _AUTO
            GoHome = _AUTO
            GamepadA = 195
            GamepadB = _AUTO
            GamepadX = _AUTO
            GamepadY = _AUTO
            GamepadRightShoulder = _AUTO
            GamepadLeftShoulder = _AUTO
            GamepadLeftTrigger = _AUTO
            GamepadRightTrigger = _AUTO
            GamepadDPadUp = _AUTO
            GamepadDPadDown = _AUTO
            GamepadDPadLeft = _AUTO
            GamepadDPadRight = _AUTO
            GamepadMenu = _AUTO
            GamepadView = _AUTO
            GamepadLeftThumbstickButton = _AUTO
            GamepadRightThumbstickButton = _AUTO
            GamepadLeftThumbstickUp = _AUTO
            GamepadLeftThumbstickDown = _AUTO
            GamepadLeftThumbstickRight = _AUTO
            GamepadLeftThumbstickLeft = _AUTO
            GamepadRightThumbstickUp = _AUTO
            GamepadRightThumbstickDown = _AUTO
            GamepadRightThumbstickRight = _AUTO
            GamepadRightThumbstickLeft = _AUTO

        class VirtualKeyModifiers(_Enum):
            None_ = _AUTO
            Control = 0x1
            Menu = 0x2
            Shift = 0x4
            Windows = 0x8

        class UserProfile:
            class AccountPictureKind(_Enum):
                SmallImage = _AUTO
                LargeImage = _AUTO
                Video = _AUTO

            class SetAccountPictureResult(_Enum):
                Success = _AUTO
                ChangeDisabled = _AUTO
                LargeOrDynamicError = _AUTO
                VideoFrameSizeError = _AUTO
                FileSizeError = _AUTO
                Failure = _AUTO

            class SetImageFeedResult(_Enum):
                Success = _AUTO
                ChangeDisabled = _AUTO
                UserCanceled = _AUTO

    class UI:
        class Composition:
            class AnimationControllerProgressBehavior(_Enum):
                Default = _AUTO
                IncludeDelayTime = _AUTO

            class AnimationDelayBehavior(_Enum):
                SetInitialValueAfterDelay = _AUTO
                SetInitialValueBeforeDelay = _AUTO

            class AnimationDirection(_Enum):
                Normal = _AUTO
                Reverse = _AUTO
                Alternate = _AUTO
                AlternateReverse = _AUTO

            class AnimationIterationBehavior(_Enum):
                Count = _AUTO
                Forever = _AUTO

            class AnimationPropertyAccessMode(_Enum):
                None_ = _AUTO
                ReadOnly = _AUTO
                WriteOnly = _AUTO
                ReadWrite = _AUTO

            class AnimationStopBehavior(_Enum):
                LeaveCurrentValue = _AUTO
                SetToInitialValue = _AUTO
                SetToFinalValue = _AUTO

            class CompositionBackfaceVisibility(_Enum):
                Inherit = _AUTO
                Visible = _AUTO
                Hidden = _AUTO

            class CompositionBatchTypes(_Enum):
                None_ = _AUTO
                Animation = 0x1
                Effect = 0x2
                InfiniteAnimation = 0x4
                AllAnimations = 0x5

            class CompositionBitmapInterpolationMode(_Enum):
                NearestNeighbor = _AUTO
                Linear = _AUTO
                MagLinearMinLinearMipLinear = _AUTO
                MagLinearMinLinearMipNearest = _AUTO
                MagLinearMinNearestMipLinear = _AUTO
                MagLinearMinNearestMipNearest = _AUTO
                MagNearestMinLinearMipLinear = _AUTO
                MagNearestMinLinearMipNearest = _AUTO
                MagNearestMinNearestMipLinear = _AUTO
                MagNearestMinNearestMipNearest = _AUTO

            class CompositionBorderMode(_Enum):
                None_ = _AUTO
                Soft = _AUTO
                Hard = _AUTO

            class CompositionColorSpace(_Enum):
                Auto = _AUTO
                Hsl = _AUTO
                Rgb = _AUTO
                HslLinear = _AUTO
                RgbLinear = _AUTO

            class CompositionCompositeMode(_Enum):
                Inherit = _AUTO
                SourceOver = _AUTO
                DestinationInvert = _AUTO
                MinBlend = _AUTO

            class CompositionDropShadowSourcePolicy(_Enum):
                Default = _AUTO
                InheritFromVisualContent = _AUTO

            class CompositionEasingFunctionMode(_Enum):
                In = _AUTO
                Out = _AUTO
                InOut = _AUTO

            class CompositionEffectFactoryLoadStatus(_Enum):
                Success = _AUTO
                EffectTooComplex = _AUTO
                Pending = _AUTO
                Other = -1

            class CompositionGetValueStatus(_Enum):
                Succeeded = _AUTO
                TypeMismatch = _AUTO
                NotFound = _AUTO

            class CompositionGradientExtendMode(_Enum):
                Clamp = _AUTO
                Wrap = _AUTO
                Mirror = _AUTO

            class CompositionMappingMode(_Enum):
                Absolute = _AUTO
                Relative = _AUTO

            class CompositionStretch(_Enum):
                None_ = _AUTO
                Fill = _AUTO
                Uniform = _AUTO
                UniformToFill = _AUTO

            class CompositionStrokeCap(_Enum):
                Flat = _AUTO
                Square = _AUTO
                Round = _AUTO
                Triangle = _AUTO

            class CompositionStrokeLineJoin(_Enum):
                Miter = _AUTO
                Bevel = _AUTO
                Round = _AUTO
                MiterOrBevel = _AUTO

        class Core:
            class AppViewBackButtonVisibility(_Enum):
                Visible = _AUTO
                Collapsed = _AUTO
                Disabled = _AUTO

            class CoreAcceleratorKeyEventType(_Enum):
                Character = 2
                DeadCharacter = _AUTO
                KeyDown = 0
                KeyUp = _AUTO
                SystemCharacter = 6
                SystemDeadCharacter = _AUTO
                SystemKeyDown = 4
                SystemKeyUp = _AUTO
                UnicodeCharacter = 8

            class CoreCursorType(_Enum):
                Arrow = _AUTO
                Cross = _AUTO
                Custom = _AUTO
                Hand = _AUTO
                Help = _AUTO
                IBeam = _AUTO
                SizeAll = _AUTO
                SizeNortheastSouthwest = _AUTO
                SizeNorthSouth = _AUTO
                SizeNorthwestSoutheast = _AUTO
                SizeWestEast = _AUTO
                UniversalNo = _AUTO
                UpArrow = _AUTO
                Wait = _AUTO
                Pin = _AUTO
                Person = _AUTO

            class CoreDispatcherPriority(_Enum):
                Idle = -2
                Low = _AUTO
                Normal = _AUTO
                High = _AUTO

            class CoreIndependentInputFilters(_Enum):
                None_ = _AUTO
                MouseButton = 0x1
                MouseWheel = 0x2
                MouseHover = 0x4
                PenWithBarrel = 0x8
                PenInverted = 0x10

            class CoreInputDeviceTypes(_Enum):
                None_ = _AUTO
                Touch = 0x1
                Pen = 0x2
                Mouse = 0x4

            class CoreProcessEventsOption(_Enum):
                ProcessOneAndAllPending = _AUTO
                ProcessOneIfPresent = _AUTO
                ProcessUntilQuit = _AUTO
                ProcessAllIfPresent = _AUTO

            class CoreProximityEvaluationScore(_Enum):
                Closest = _AUTO
                Farthest = 2147483647

            class CoreVirtualKeyStates(_Enum):
                None_ = _AUTO
                Down = 0x1
                Locked = 0x2

            class CoreWindowActivationMode(_Enum):
                None_ = _AUTO
                Deactivated = _AUTO
                ActivatedNotForeground = _AUTO
                ActivatedInForeground = _AUTO

            class CoreWindowActivationState(_Enum):
                CodeActivated = _AUTO
                Deactivated = _AUTO
                PointerActivated = _AUTO

            class CoreWindowFlowDirection(_Enum):
                LeftToRight = _AUTO
                RightToLeft = _AUTO

        class Notifications:
            class AdaptiveNotificationContentKind(_Enum):
                Text = _AUTO

            class BadgeTemplateType(_Enum):
                BadgeGlyph = _AUTO
                BadgeNumber = _AUTO

            class NotificationKinds(_Enum):
                Unknown = _AUTO
                Toast = 0x1

            class NotificationMirroring(_Enum):
                Allowed = _AUTO
                Disabled = _AUTO

            class NotificationSetting(_Enum):
                Enabled = _AUTO
                DisabledForApplication = _AUTO
                DisabledForUser = _AUTO
                DisabledByGroupPolicy = _AUTO
                DisabledByManifest = _AUTO

            class NotificationUpdateResult(_Enum):
                Succeeded = _AUTO
                Failed = _AUTO
                NotificationNotFound = _AUTO

            class PeriodicUpdateRecurrence(_Enum):
                HalfHour = _AUTO
                Hour = _AUTO
                SixHours = _AUTO
                TwelveHours = _AUTO
                Daily = _AUTO

            class TileFlyoutTemplateType(_Enum):
                TileFlyoutTemplate01 = _AUTO

            class TileTemplateType(_Enum):
                TileSquareImage = _AUTO
                TileSquareBlock = _AUTO
                TileSquareText01 = _AUTO
                TileSquareText02 = _AUTO
                TileSquareText03 = _AUTO
                TileSquareText04 = _AUTO
                TileSquarePeekImageAndText01 = _AUTO
                TileSquarePeekImageAndText02 = _AUTO
                TileSquarePeekImageAndText03 = _AUTO
                TileSquarePeekImageAndText04 = _AUTO
                TileWideImage = _AUTO
                TileWideImageCollection = _AUTO
                TileWideImageAndText01 = _AUTO
                TileWideImageAndText02 = _AUTO
                TileWideBlockAndText01 = _AUTO
                TileWideBlockAndText02 = _AUTO
                TileWidePeekImageCollection01 = _AUTO
                TileWidePeekImageCollection02 = _AUTO
                TileWidePeekImageCollection03 = _AUTO
                TileWidePeekImageCollection04 = _AUTO
                TileWidePeekImageCollection05 = _AUTO
                TileWidePeekImageCollection06 = _AUTO
                TileWidePeekImageAndText01 = _AUTO
                TileWidePeekImageAndText02 = _AUTO
                TileWidePeekImage01 = _AUTO
                TileWidePeekImage02 = _AUTO
                TileWidePeekImage03 = _AUTO
                TileWidePeekImage04 = _AUTO
                TileWidePeekImage05 = _AUTO
                TileWidePeekImage06 = _AUTO
                TileWideSmallImageAndText01 = _AUTO
                TileWideSmallImageAndText02 = _AUTO
                TileWideSmallImageAndText03 = _AUTO
                TileWideSmallImageAndText04 = _AUTO
                TileWideSmallImageAndText05 = _AUTO
                TileWideText01 = _AUTO
                TileWideText02 = _AUTO
                TileWideText03 = _AUTO
                TileWideText04 = _AUTO
                TileWideText05 = _AUTO
                TileWideText06 = _AUTO
                TileWideText07 = _AUTO
                TileWideText08 = _AUTO
                TileWideText09 = _AUTO
                TileWideText10 = _AUTO
                TileWideText11 = _AUTO
                TileSquare150x150Image = 0
                TileSquare150x150Block = _AUTO
                TileSquare150x150Text01 = _AUTO
                TileSquare150x150Text02 = _AUTO
                TileSquare150x150Text03 = _AUTO
                TileSquare150x150Text04 = _AUTO
                TileSquare150x150PeekImageAndText01 = _AUTO
                TileSquare150x150PeekImageAndText02 = _AUTO
                TileSquare150x150PeekImageAndText03 = _AUTO
                TileSquare150x150PeekImageAndText04 = _AUTO
                TileWide310x150Image = _AUTO
                TileWide310x150ImageCollection = _AUTO
                TileWide310x150ImageAndText01 = _AUTO
                TileWide310x150ImageAndText02 = _AUTO
                TileWide310x150BlockAndText01 = _AUTO
                TileWide310x150BlockAndText02 = _AUTO
                TileWide310x150PeekImageCollection01 = _AUTO
                TileWide310x150PeekImageCollection02 = _AUTO
                TileWide310x150PeekImageCollection03 = _AUTO
                TileWide310x150PeekImageCollection04 = _AUTO
                TileWide310x150PeekImageCollection05 = _AUTO
                TileWide310x150PeekImageCollection06 = _AUTO
                TileWide310x150PeekImageAndText01 = _AUTO
                TileWide310x150PeekImageAndText02 = _AUTO
                TileWide310x150PeekImage01 = _AUTO
                TileWide310x150PeekImage02 = _AUTO
                TileWide310x150PeekImage03 = _AUTO
                TileWide310x150PeekImage04 = _AUTO
                TileWide310x150PeekImage05 = _AUTO
                TileWide310x150PeekImage06 = _AUTO
                TileWide310x150SmallImageAndText01 = _AUTO
                TileWide310x150SmallImageAndText02 = _AUTO
                TileWide310x150SmallImageAndText03 = _AUTO
                TileWide310x150SmallImageAndText04 = _AUTO
                TileWide310x150SmallImageAndText05 = _AUTO
                TileWide310x150Text01 = _AUTO
                TileWide310x150Text02 = _AUTO
                TileWide310x150Text03 = _AUTO
                TileWide310x150Text04 = _AUTO
                TileWide310x150Text05 = _AUTO
                TileWide310x150Text06 = _AUTO
                TileWide310x150Text07 = _AUTO
                TileWide310x150Text08 = _AUTO
                TileWide310x150Text09 = _AUTO
                TileWide310x150Text10 = _AUTO
                TileWide310x150Text11 = _AUTO
                TileSquare310x310BlockAndText01 = _AUTO
                TileSquare310x310BlockAndText02 = _AUTO
                TileSquare310x310Image = _AUTO
                TileSquare310x310ImageAndText01 = _AUTO
                TileSquare310x310ImageAndText02 = _AUTO
                TileSquare310x310ImageAndTextOverlay01 = _AUTO
                TileSquare310x310ImageAndTextOverlay02 = _AUTO
                TileSquare310x310ImageAndTextOverlay03 = _AUTO
                TileSquare310x310ImageCollectionAndText01 = _AUTO
                TileSquare310x310ImageCollectionAndText02 = _AUTO
                TileSquare310x310ImageCollection = _AUTO
                TileSquare310x310SmallImagesAndTextList01 = _AUTO
                TileSquare310x310SmallImagesAndTextList02 = _AUTO
                TileSquare310x310SmallImagesAndTextList03 = _AUTO
                TileSquare310x310SmallImagesAndTextList04 = _AUTO
                TileSquare310x310Text01 = _AUTO
                TileSquare310x310Text02 = _AUTO
                TileSquare310x310Text03 = _AUTO
                TileSquare310x310Text04 = _AUTO
                TileSquare310x310Text05 = _AUTO
                TileSquare310x310Text06 = _AUTO
                TileSquare310x310Text07 = _AUTO
                TileSquare310x310Text08 = _AUTO
                TileSquare310x310TextList01 = _AUTO
                TileSquare310x310TextList02 = _AUTO
                TileSquare310x310TextList03 = _AUTO
                TileSquare310x310SmallImageAndText01 = _AUTO
                TileSquare310x310SmallImagesAndTextList05 = _AUTO
                TileSquare310x310Text09 = _AUTO
                TileSquare71x71IconWithBadge = _AUTO
                TileSquare150x150IconWithBadge = _AUTO
                TileWide310x150IconWithBadgeAndText = _AUTO
                TileSquare71x71Image = _AUTO
                TileTall150x310Image = _AUTO

            class ToastDismissalReason(_Enum):
                UserCanceled = _AUTO
                ApplicationHidden = _AUTO
                TimedOut = _AUTO

            class ToastHistoryChangedType(_Enum):
                Cleared = _AUTO
                Removed = _AUTO
                Expired = _AUTO
                Added = _AUTO

            class ToastNotificationPriority(_Enum):
                Default = _AUTO
                High = _AUTO

            class ToastTemplateType(_Enum):
                ToastImageAndText01 = _AUTO
                ToastImageAndText02 = _AUTO
                ToastImageAndText03 = _AUTO
                ToastImageAndText04 = _AUTO
                ToastText01 = _AUTO
                ToastText02 = _AUTO
                ToastText03 = _AUTO
                ToastText04 = _AUTO

            class UserNotificationChangedKind(_Enum):
                Added = _AUTO
                Removed = _AUTO

        class Popups:
            class MessageDialogOptions(_Enum):
                None_ = _AUTO
                AcceptUserInputAfterDelay = 0x1

            class Placement(_Enum):
                Default = _AUTO
                Above = _AUTO
                Below = _AUTO
                Left = _AUTO
                Right = _AUTO

        class Text:
            class CaretType(_Enum):
                Normal = _AUTO
                Null = _AUTO

            class FindOptions(_Enum):
                None_ = _AUTO
                Word = 0x2
                Case = 0x4

            class FontStretch(_Enum):
                Undefined = _AUTO
                UltraCondensed = _AUTO
                ExtraCondensed = _AUTO
                Condensed = _AUTO
                SemiCondensed = _AUTO
                Normal = _AUTO
                SemiExpanded = _AUTO
                Expanded = _AUTO
                ExtraExpanded = _AUTO
                UltraExpanded = _AUTO

            class FontStyle(_Enum):
                Normal = _AUTO
                Oblique = _AUTO
                Italic = _AUTO

            class FormatEffect(_Enum):
                Off = _AUTO
                On = _AUTO
                Toggle = _AUTO
                Undefined = _AUTO

            class HorizontalCHaracterAlignment(_Enum):
                Left = _AUTO
                Right = _AUTO
                Center = _AUTO

            class LetterCase(_Enum):
                Lower = _AUTO
                Upper = _AUTO

            class TextDecorations(_Enum):
                None_ = _AUTO
                Underline = 0x1
                Strikethrough = 0x2

        class ViewManagement:
            class ApplicationViewBoundsMode(_Enum):
                UseVisible = _AUTO
                UseCoreWindow = _AUTO

            class ApplicationViewMode(_Enum):
                Default = _AUTO
                CompactOverlay = _AUTO

            class ApplicationViewOrientation(_Enum):
                Landscape = _AUTO
                Portrait = _AUTO

            class ApplicationViewState(_Enum):
                FullScreenLandscape = _AUTO
                Filled = _AUTO
                Snapped = _AUTO
                FullScreenPortrait = _AUTO

            class ApplicationViewWindowingMode(_Enum):
                Auto = _AUTO
                PreferredLaunchViewSize = _AUTO
                FullScreen = _AUTO
                CompactOverlay = _AUTO
                Maximized = _AUTO

            class FullScreenSystemOverlayMode(_Enum):
                Standard = _AUTO
                Minimal = _AUTO

            class HandPreference(_Enum):
                LeftHanded = _AUTO
                RightHanded = _AUTO

            class UIColorType(_Enum):
                Background = _AUTO
                Foreground = _AUTO
                AccentDark3 = _AUTO
                AccentDark2 = _AUTO
                AccentDark1 = _AUTO
                Accent = _AUTO
                AccentLight1 = _AUTO
                AccentLight2 = _AUTO
                AccentLight3 = _AUTO
                Complement = _AUTO

            class UIElementType(_Enum):
                ActiveCaption = _AUTO
                Background = _AUTO
                ButtonFace = _AUTO
                ButtonText = _AUTO
                CaptionText = _AUTO
                GrayText = _AUTO
                Highlight = _AUTO
                HighlightText = _AUTO
                Hotlight = _AUTO
                InactiveCaption = _AUTO
                InactiveCaptionText = _AUTO
                Window = _AUTO
                WindowText = _AUTO
                AccentColor = 1000
                TextHigh = _AUTO
                TextMedium = _AUTO
                TextLow = _AUTO
                TextContrastWithHigh = _AUTO
                NonTextHigh = _AUTO
                NonTextMediumHigh = _AUTO
                NonTextMedium = _AUTO
                NonTextMediumLow = _AUTO
                NonTextLow = _AUTO
                PageBackground = _AUTO
                PopupBackground = _AUTO
                OverlayOutsidePopup = _AUTO

            class UserInteractionMode(_Enum):
                Mouse = _AUTO
                Touch = _AUTO

            class ViewSizePreference(_Enum):
                Default = _AUTO
                UseLess = _AUTO
                UseHalf = _AUTO
                UseMore = _AUTO
                UseMinimum = _AUTO
                UseNone = _AUTO
                Custom = _AUTO

        class Xaml:
            class ApplicationHighContrastAdjustment(_Enum):
                None_ = _AUTO
                Auto = 0xffffffff

            class ApplicationRequiresPointerMode(_Enum):
                Auto = _AUTO
                WhenRequested = _AUTO

            class ApplicationTheme(_Enum):
                Light = _AUTO
                Dark = _AUTO

            class AutomationTextAttributesEnum(_Enum):
                AnimationStyleAttribute = 40000
                BackgroundColorAttribute = _AUTO
                BulletStyleAttribute = _AUTO
                CapStyleAttribute = _AUTO
                CultureAttribute = _AUTO
                FontNameAttribute = _AUTO
                FontSizeAttribute = _AUTO
                FontWeightAttribute = _AUTO
                ForegroundColorAttribute = _AUTO
                HorizontalTextAlignmentAttribute = _AUTO
                IndentationFirstLineAttribute = _AUTO
                IndentationLeadingAttribute = _AUTO
                IndentationTrailingAttribute = _AUTO
                IsHiddenAttribute = _AUTO
                IsItalicAttribute = _AUTO
                IsReadOnlyAttribute = _AUTO
                IsSubscriptAttribute = _AUTO
                IsSuperscriptAttribute = _AUTO
                MarginBottomAttribute = _AUTO
                MarginLeadingAttribute = _AUTO
                MarginTopAttribute = _AUTO
                MarginTrailingAttribute = _AUTO
                OutlineStylesAttribute = _AUTO
                OverlineColorAttribute = _AUTO
                OverlineStyleAttribute = _AUTO
                StrikethroughColorAttribute = _AUTO
                StrikethroughStyleAttribute = _AUTO
                TabsAttribute = _AUTO
                TextFlowDirectionsAttribute = _AUTO
                UnderlineColorAttribute = _AUTO
                UnderlineStyleAttribute = _AUTO
                AnnotationTypesAttribute = _AUTO
                AnnotationObjectsAttribute = _AUTO
                StyleNameAttribute = _AUTO
                StyleIdAttribute = _AUTO
                LinkAttribute = _AUTO
                IsActiveAttribute = _AUTO
                SelectionActiveEndAttribute = _AUTO
                CaretPositionAttribute = _AUTO
                CaretBidiModeAttribute = _AUTO

            class DurationType(_Enum):
                Automatic = _AUTO
                TimeSpan = _AUTO
                Forever = _AUTO

            class ElementSoundKind(_Enum):
                Focus = _AUTO
                Invoke = _AUTO
                Show = _AUTO
                Hide = _AUTO
                MovePrevious = _AUTO
                MoveNext = _AUTO
                GoBack = _AUTO

            class ElementSoundMode(_Enum):
                Default = _AUTO
                FocusOnly = _AUTO
                Off = _AUTO

            class ElementSoundPlayerState(_Enum):
                Auto = _AUTO
                Off = _AUTO
                On = _AUTO

            class ElementSpatialAudioMode(_Enum):
                Auto = _AUTO
                Off = _AUTO
                On = _AUTO

            class ElementTheme(_Enum):
                Default = _AUTO
                Light = _AUTO
                Dark = _AUTO

            class FlowDirection(_Enum):
                LeftToRight = _AUTO
                RightToLeft = _AUTO

            class FocusState(_Enum):
                Unfocused = _AUTO
                Pointer = _AUTO
                Keyboard = _AUTO
                Programmatic = _AUTO

            class FocusVisualKind(_Enum):
                DottedLine = _AUTO
                HighVisibility = _AUTO
                Reveal = _AUTO

            class FontCapitals(_Enum):
                Normal = _AUTO
                AllSmallCaps = _AUTO
                SmallCaps = _AUTO
                AllPetiteCaps = _AUTO
                PetiteCaps = _AUTO
                Unicase = _AUTO
                Titling = _AUTO

            class FontEastAsianLanguage(_Enum):
                Normal = _AUTO
                HojoKanji = _AUTO
                Jis04 = _AUTO
                Jis78 = _AUTO
                Jis83 = _AUTO
                Jis90 = _AUTO
                NlcKanji = _AUTO
                Simplified = _AUTO
                Traditional = _AUTO
                TraditionalNames = _AUTO

            class FontEastAsianWidths(_Enum):
                Normal = _AUTO
                Full = _AUTO
                Half = _AUTO
                Proportional = _AUTO
                Quarter = _AUTO
                Third = _AUTO

            class FontFraction(_Enum):
                Normal = _AUTO
                Stacked = _AUTO
                Slashed = _AUTO

            class FontNumeralAlignment(_Enum):
                Normal = _AUTO
                Proportional = _AUTO
                Tabular = _AUTO

            class FontNumeralStyle(_Enum):
                Normal = _AUTO
                Lining = _AUTO
                OldStyle = _AUTO

            class FontVariants(_Enum):
                Normal = _AUTO
                Superscript = _AUTO
                Subscript = _AUTO
                Ordinal = _AUTO
                Inferior = _AUTO
                Ruby = _AUTO

            class GridUnitType(_Enum):
                Auto = _AUTO
                Pixel = _AUTO
                Star = _AUTO

            class HorizontalAlignment(_Enum):
                Left = _AUTO
                Center = _AUTO
                Right = _AUTO
                Stretch = _AUTO

            class LineStackingStrategy(_Enum):
                MaxHeight = _AUTO
                BlockLineHeight = _AUTO
                BaselineToBaseline = _AUTO

            class OpticalMarginAlignment(_Enum):
                None_ = _AUTO
                TrimSideBearings = _AUTO

            class TextAlignment(_Enum):
                Center = _AUTO
                Left = _AUTO
                Start = 1
                Right = _AUTO
                End = 2
                Justify = _AUTO
                DetectFromContent = _AUTO

            class TextLineBounds(_Enum):
                Full = _AUTO
                TrimToCapHeight = _AUTO
                TrimToBaseline = _AUTO
                Tight = _AUTO

            class TextReadingOrder(_Enum):
                Default = _AUTO
                UseFlowDirection = 0
                DetectFromContent = _AUTO

            class TextTrimming(_Enum):
                None_ = _AUTO
                CharacterEllipsis = _AUTO
                WordEllipsis = _AUTO
                Clip = _AUTO

            class TextWrapping(_Enum):
                NoWrap = 1
                Wrap = _AUTO
                WrapWithOverflow = _AUTO

            class Vector3TransitionComponents(_Enum):
                X = 0x1
                Y = 0x2
                Z = 0x4

            class VerticalAlignment(_Enum):
                Top = _AUTO
                Center = _AUTO
                Bottom = _AUTO
                Stretch = _AUTO

            class Visibility(_Enum):
                Visible = _AUTO
                Collapsed = _AUTO

            class Controls:
                class TextAlignment(_Enum):
                    Center = _AUTO
                    Left = 1
                    Start = 1
                    Right = 2
                    End = 2
                    Justify = _AUTO
                    DetectFromContent = _AUTO

                class TextTrimming(_Enum):
                    None_ = _AUTO
                    CharacterEllipsis = _AUTO
                    WordEllipsis = _AUTO
                    Clip = _AUTO

                class TextWrapping(_Enum):
                    NoWrap = 1
                    Wrap = _AUTO
                    WrapWholeWords = _AUTO

                class BackgroundSizing(_Enum):
                    InnerBorderEdge = _AUTO
                    OuterBorderEdge = _AUTO

                class CandidateWindowAlignment(_Enum):
                    Default = _AUTO
                    BottomEdge = _AUTO

                class CharacterCasing(_Enum):
                    Normal = _AUTO
                    Lower = _AUTO
                    Upper = _AUTO

                class ClickMode(_Enum):
                    Release = _AUTO
                    Press = _AUTO
                    Hover = _AUTO

                class ColorPickerHsvChannel(_Enum):
                    Hue = _AUTO
                    Saturation = _AUTO
                    Value = _AUTO
                    Alpha = _AUTO

                class ColorSpectrumComponents(_Enum):
                    HueValue = _AUTO
                    ValueHue = _AUTO
                    HueSaturation = _AUTO
                    SaturationHue = _AUTO
                    SaturationValue = _AUTO
                    ValueSaturation = _AUTO

                class ColorSpectrumShape(_Enum):
                    Box = _AUTO
                    Ring = _AUTO

                class ComboBoxSelectionChangedTrigger(_Enum):
                    Committed = _AUTO
                    Always = _AUTO

                class CommandBarDefaultLabelPosition(_Enum):
                    Bottom = _AUTO
                    Right = _AUTO
                    Collapsed = _AUTO

                class CommandBarDynamicOverflowAction(_Enum):
                    AddingToOverflow = _AUTO
                    RemovingFromOverflow = _AUTO

                class CommandBarLabelPosition(_Enum):
                    Default = _AUTO
                    Collapsed = _AUTO

                class CommandBarOverflowButtonVisibility(_Enum):
                    Auto = _AUTO
                    Visible = _AUTO
                    Collapsed = _AUTO

                class ContentDialogButton(_Enum):
                    None_ = _AUTO
                    Primary = _AUTO
                    Secondary = _AUTO
                    Close = _AUTO

                class ContentDialogPlacement(_Enum):
                    Popup = _AUTO
                    InPlace = _AUTO

                class ContentDialogResult(_Enum):
                    None_ = _AUTO
                    Primary = _AUTO
                    Secondary = _AUTO

                class ContentLinkChangeKind(_Enum):
                    Inserted = _AUTO
                    Removed = _AUTO
                    Edited = _AUTO

                class LightDismissOverlayMode(_Enum):
                    Auto = _AUTO
                    On = _AUTO
                    Off = _AUTO

                class Orientation(_Enum):
                    Vertical = _AUTO
                    Horizontal = _AUTO

                class PanelScrollingDirection(_Enum):
                    None_ = _AUTO
                    Forward = _AUTO
                    Backward = _AUTO

                class ParallaxSourceOffsetKind(_Enum):
                    Absolute = _AUTO
                    Relative = _AUTO

                class PasswordRevealMode(_Enum):
                    Peek = _AUTO
                    Hidden = _AUTO
                    Visible = _AUTO

                class PivotHeaderFocusVisualPlacement(_Enum):
                    ItemHeaders = _AUTO
                    SelectedItemHeader = _AUTO

                class PivotSlideInAnimationGroup(_Enum):
                    Default = _AUTO
                    GroupOne = _AUTO
                    GroupTwo = _AUTO
                    GroupThree = _AUTO

                class RefreshPullDirection(_Enum):
                    LeftToRight = _AUTO
                    TopToBottom = _AUTO
                    RightToLeft = _AUTO
                    BottomToTop = _AUTO

                class RefreshVisualizerOrientation(_Enum):
                    Auto = _AUTO
                    Normal = _AUTO
                    Rotate90DegreesCounterclockwise = _AUTO
                    Rotate270DegreesCounterclockwise = _AUTO

                class RefreshVisualizerState(_Enum):
                    Idle = _AUTO
                    Peeking = _AUTO
                    Interacting = _AUTO
                    Pending = _AUTO
                    Refreshing = _AUTO

                class RequiresPointer(_Enum):
                    Never = _AUTO
                    WhenEngaged = _AUTO
                    WhenFocused = _AUTO

                class RichEditClipboardFormat(_Enum):
                    AllFormats = _AUTO
                    PlainText = _AUTO

                class ScrollBarVisibility(_Enum):
                    Disabled = _AUTO
                    Auto = _AUTO
                    Hidden = _AUTO
                    Visible = _AUTO

                class ScrollIntoViewAlignment(_Enum):
                    Default = _AUTO
                    Leading = _AUTO

                class ScrollMode(_Enum):
                    Disabled = _AUTO
                    Enabled = _AUTO
                    Auto = _AUTO

                class SelectionMode(_Enum):
                    Single = _AUTO
                    Multiple = _AUTO
                    Extended = _AUTO

                class SnapPointsType(_Enum):
                    None_ = _AUTO
                    Optional = _AUTO
                    Mandatory = _AUTO
                    OptionalSingle = _AUTO
                    MandatorySingle = _AUTO

                class SplitViewDisplayMode(_Enum):
                    Overlay = _AUTO
                    Inline = _AUTO
                    CompactOverlay = _AUTO
                    CompactInline = _AUTO

                class SplitViewPanePlacement(_Enum):
                    Left = _AUTO
                    Right = _AUTO

                class StretchDirection(_Enum):
                    UpOnly = _AUTO
                    DownOnly = _AUTO
                    Both = _AUTO

                class SwipeBehaviorOnInvoked(_Enum):
                    Auto = _AUTO
                    Close = _AUTO
                    RemainOpen = _AUTO

                class SwipeMode(_Enum):
                    Reveal = _AUTO
                    Execute = _AUTO

                class Symbol(_Enum):
                    Previous = 57600
                    Next = _AUTO
                    Play = _AUTO
                    Pause = _AUTO
                    Edit = _AUTO
                    Save = _AUTO
                    Clear = _AUTO
                    Delete = _AUTO
                    Remove = _AUTO
                    Add = _AUTO
                    Cancel = _AUTO
                    Accept = _AUTO
                    More = _AUTO
                    Redo = _AUTO
                    Undo = _AUTO
                    Home = _AUTO
                    Up = _AUTO
                    Forward = _AUTO
                    Back = _AUTO
                    Favorite = _AUTO
                    Camera = _AUTO
                    Setting = _AUTO
                    Video = _AUTO
                    Sync = _AUTO
                    Download = _AUTO
                    Mail = _AUTO
                    Find = _AUTO
                    Help = _AUTO
                    Upload = _AUTO
                    Emoji = _AUTO
                    TwoPage = _AUTO
                    LeaveChat = _AUTO
                    MailForward = _AUTO
                    Clock = _AUTO
                    Send = _AUTO
                    Crop = _AUTO
                    RotateCamera = _AUTO
                    People = _AUTO
                    OpenPane = _AUTO
                    ClosePane = _AUTO
                    World = _AUTO
                    Flag = _AUTO
                    PreviewLink = _AUTO
                    Globe = _AUTO
                    Trim = _AUTO
                    AttachCamera = _AUTO
                    ZoomIn = _AUTO
                    Bookmarks = _AUTO
                    Document = _AUTO
                    ProtectedDocument = _AUTO
                    Page = _AUTO
                    Bullets = _AUTO
                    Comment = _AUTO
                    MailFilled = _AUTO
                    ContactInfo = _AUTO
                    HangUp = _AUTO
                    ViewAll = _AUTO
                    MapPin = _AUTO
                    Phone = _AUTO
                    VideoChat = _AUTO
                    Switch = _AUTO
                    Contact = _AUTO
                    Rename = _AUTO
                    Pin = 57665
                    MusicInfo = _AUTO
                    Go = _AUTO
                    Keyboard = _AUTO
                    DockLeft = _AUTO
                    DockRight = _AUTO
                    DockBottom = _AUTO
                    Remote = _AUTO
                    Refresh = _AUTO
                    Rotate = _AUTO
                    Shuffle = _AUTO
                    List = _AUTO
                    Shop = _AUTO
                    SelectAll = _AUTO
                    Orientation = _AUTO
                    Import = _AUTO
                    ImportAll = _AUTO
                    BrowsePhotos = 57685
                    WebCam = _AUTO
                    Pictures = 57688
                    SaveLocal = _AUTO
                    Caption = _AUTO
                    Stop = _AUTO
                    ShowResults = _AUTO
                    Volume = _AUTO
                    Repair = _AUTO
                    Message = _AUTO
                    Page2 = _AUTO
                    CalendarDay = _AUTO
                    CalendarWeek = _AUTO
                    Calendar = _AUTO
                    Character = _AUTO
                    MailReplyAll = _AUTO
                    Read = _AUTO
                    Link = _AUTO
                    Account = _AUTO
                    ShowBcc = _AUTO
                    HideBcc = _AUTO
                    Cut = _AUTO
                    Attach = _AUTO
                    Paste = _AUTO
                    Filter = _AUTO
                    Copy = _AUTO
                    Emoji2 = _AUTO
                    Important = _AUTO
                    MailReply = _AUTO
                    SlideShow = _AUTO
                    Sort = _AUTO
                    Manage = 57720
                    AllApps = _AUTO
                    DisconnectDrive = _AUTO
                    MapDrive = _AUTO
                    NewWindow = _AUTO
                    OpenWith = _AUTO
                    ContactPresence = 57729
                    Priority = _AUTO
                    GoToToday = 57732
                    Font = _AUTO
                    FontColor = _AUTO
                    Contact2 = _AUTO
                    Folder = _AUTO
                    Audio = _AUTO
                    Placeholder = _AUTO
                    View = _AUTO
                    SetLockScreen = _AUTO
                    SetTile = _AUTO
                    ClosedCaption = 57744
                    StopSlideShow = _AUTO
                    Permissions = _AUTO
                    Highlight = _AUTO
                    DisableUpdates = _AUTO
                    UnFavorite = _AUTO
                    UnPin = _AUTO
                    OpenLocal = _AUTO
                    Mute = _AUTO
                    Italic = _AUTO
                    Underline = _AUTO
                    Bold = _AUTO
                    MoveToFolder = _AUTO
                    LikeDislike = _AUTO
                    Dislike = _AUTO
                    Like = _AUTO
                    AlignRight = _AUTO
                    AlignCenter = _AUTO
                    AlignLeft = _AUTO
                    Zoom = _AUTO
                    ZoomOut = _AUTO
                    OpenFile = _AUTO
                    OtherUser = _AUTO
                    Admin = _AUTO
                    Street = 57795
                    Map = _AUTO
                    ClearSelection = _AUTO
                    FontDecrease = _AUTO
                    FontIncrease = _AUTO
                    FontSize = _AUTO
                    CellPhone = _AUTO
                    ReShare = _AUTO
                    Tag = _AUTO
                    RepeatOne = _AUTO
                    RepeatAll = _AUTO
                    OutlineStar = _AUTO
                    SolidStar = _AUTO
                    Calculator = _AUTO
                    Directions = _AUTO
                    Target = _AUTO
                    Library = _AUTO
                    PhoneBook = _AUTO
                    Memo = _AUTO
                    Microphone = _AUTO
                    PostUpdate = _AUTO
                    BackToWindow = _AUTO
                    FullScreen = _AUTO
                    NewFolder = _AUTO
                    CalendarReply = _AUTO
                    UnSyncFolder = 57821
                    ReportHacked = _AUTO
                    SyncFolder = _AUTO
                    BlockContact = _AUTO
                    SwitchApps = _AUTO
                    AddFriend = _AUTO
                    TouchPointer = _AUTO
                    GoToStart = _AUTO
                    ZeroBars = _AUTO
                    OneBar = _AUTO
                    TwoBars = _AUTO
                    ThreeBars = _AUTO
                    FourBars = _AUTO
                    Scan = 58004
                    Preview = _AUTO
                    GlobalNavigationButton = 59136
                    Share = 59181
                    Print = 59209
                    XboxOneConsole = 59792

                class TreeViewSelectionMode(_Enum):
                    None_ = _AUTO
                    Single = _AUTO
                    Multiple = _AUTO

                class TwoPaneViewMode(_Enum):
                    SinglePane = _AUTO
                    Wide = _AUTO
                    Tall = _AUTO

                class TwoPaneViewPriority(_Enum):
                    Pane1 = _AUTO
                    Pane2 = _AUTO

                class TwoPaneViewTallModeConfiguration(_Enum):
                    SinglePane = _AUTO
                    TopBottom = _AUTO
                    BottomTop = _AUTO

                class TwoPaneViewWideModeConfiguration(_Enum):
                    SinglePane = _AUTO
                    LeftRight = _AUTO
                    RightLeft = _AUTO

                class VirtualizationMode(_Enum):
                    Standard = _AUTO
                    Recycling = _AUTO

                class WebViewExecutionMode(_Enum):
                    SameThread = _AUTO
                    SeparateThread = _AUTO
                    SeparateProcess = _AUTO

                class WebViewPermissionState(_Enum):
                    Unknown = _AUTO
                    Defer = _AUTO
                    Allow = _AUTO
                    Deny = _AUTO

                class WebViewPermissionType(_Enum):
                    Geolocation = _AUTO
                    UnlimitedIndexedDBQuota = _AUTO
                    Media = _AUTO
                    PointerLock = _AUTO
                    WebNotifications = _AUTO
                    Screen = _AUTO
                    ImmersiveView = _AUTO

                class ZoomMode(_Enum):
                    Disabled = _AUTO
                    Enabled = _AUTO

                class Primitives:
                    class FlyoutPlacementMode(_Enum):
                        Top = _AUTO
                        Bottom = _AUTO
                        Left = _AUTO
                        Right = _AUTO
                        Full = _AUTO
                        TopEdgeAlignedLeft = _AUTO
                        TopEdgeAlignedRight = _AUTO
                        BottomEdgeAlignedLeft = _AUTO
                        BottomEdgeAlignedRight = _AUTO
                        LeftEdgeAlignedTop = _AUTO
                        LeftEdgeAlignedBottom = _AUTO
                        RightEdgeAlignedTop = _AUTO
                        RightEdgeAlignedBottom = _AUTO
                        Auto = _AUTO

                    class FlyoutShowMode(_Enum):
                        Auto = _AUTO
                        Standard = _AUTO
                        Transient = _AUTO
                        TransientWithDismissOnPointerMoveAway = _AUTO

                    class PlacementMode(_Enum):
                        Bottom = 2
                        Left = 9
                        Mouse = 7
                        Right = 4
                        Top = 10

                    class PopupPlacementMode(_Enum):
                        Auto = _AUTO
                        Top = _AUTO
                        Bottom = _AUTO
                        Left = _AUTO
                        Right = _AUTO
                        TopEdgeAlignedLeft = _AUTO
                        TopEdgeAlignedRight = _AUTO
                        BottomEdgeAlignedLeft = _AUTO
                        BottomEdgeAlignedRight = _AUTO
                        LeftEdgeAlignedTop = _AUTO
                        LeftEdgeAlignedBottom = _AUTO
                        RightEdgeAlignedTop = _AUTO
                        RightEdgeAlignedBottom = _AUTO

                    class ScrollEventType(_Enum):
                        SmallDecrement = _AUTO
                        SmallIncrement = _AUTO
                        LargeDecrement = _AUTO
                        LargeIncrement = _AUTO
                        ThumbPosition = _AUTO
                        ThumbTrack = _AUTO
                        First = _AUTO
                        Last = _AUTO
                        EndScroll = _AUTO

                    class ScrollingIndicatorMode(_Enum):
                        None_ = _AUTO
                        TouchIndicator = _AUTO
                        MouseIndicator = _AUTO

                    class SnapPointsAlignment(_Enum):
                        Near = _AUTO
                        Center = _AUTO
                        Far = _AUTO

                    class TickPlacement(_Enum):
                        None_ = _AUTO
                        TopLeft = _AUTO
                        BottomRight = _AUTO
                        Outside = _AUTO
                        Inline = _AUTO

            class Hosting:
                class XamlSourceFocusNavigationReason(_Enum):
                    Programmatic = _AUTO
                    Restore = _AUTO
                    First = 3
                    Last = _AUTO
                    Left = 7
                    Up = _AUTO
                    Right = 9
                    Down = _AUTO

            class Input:
                class FocusInputDeviceKind(_Enum):
                    None_ = _AUTO
                    Mouse = _AUTO
                    Touch = _AUTO
                    Pen = _AUTO
                    Keyboard = _AUTO
                    GameController = _AUTO

                class FocusNavigationDirection(_Enum):
                    Next = _AUTO
                    Previous = _AUTO
                    Up = _AUTO
                    Down = _AUTO
                    Left = _AUTO
                    Right = _AUTO
                    None_ = _AUTO

                class InputScopeNameValue(_Enum):
                    Default = _AUTO
                    Url = _AUTO
                    EmailSmtpAddress = 5
                    PersonalFullName = 7
                    CurrencyAmountAndSymbol = 20
                    CurrencyAmount = _AUTO
                    DateMonthNumber = 23
                    DateDayNumber = _AUTO
                    DateYear = _AUTO
                    Digits = 28
                    Number = _AUTO
                    Password = 31
                    TelephoneNumber = _AUTO
                    TelephoneCountryCode = _AUTO
                    TelephoneAreaCode = _AUTO
                    TelephoneLocalNumber = _AUTO
                    TimeHour = 37
                    TimeMinutesOrSeconds = _AUTO
                    NumberFullWidth = _AUTO
                    AlphanumericHalfWidth = _AUTO
                    AlphanumericFullWidth = _AUTO
                    Hiragana = 44
                    KatakanaHalfWidth = _AUTO
                    KatakanaFullWidth = _AUTO
                    Hanja = _AUTO
                    HangulHalfWidth = _AUTO
                    HangulFullWidth = _AUTO
                    Search = _AUTO
                    Formula = _AUTO
                    SearchIncremental = _AUTO
                    ChineseHalfWidth = _AUTO
                    ChineseFullWidth = _AUTO
                    NativeScript = _AUTO
                    Text = 57
                    Chat = _AUTO
                    NameOrPhoneNumber = _AUTO
                    Private = _AUTO
                    Maps = _AUTO
                    NumericPassword = _AUTO
                    NumericPin = _AUTO
                    AlphanumericPin = _AUTO
                    FormulaNumber = 67
                    ChatWithoutEmoji = _AUTO

                class KeyTipPlacementMode(_Enum):
                    Auto = _AUTO
                    Bottom = _AUTO
                    Top = _AUTO
                    Left = _AUTO
                    Right = _AUTO
                    Center = _AUTO
                    Hidden = _AUTO

                class KeyboardAcceleratorPlacementMode(_Enum):
                    Auto = _AUTO
                    Manual = _AUTO

                class KeyboardNavigationMode(_Enum):
                    Local = _AUTO
                    Cycle = _AUTO
                    Once = _AUTO

                class ManipulationModes(_Enum):
                    None_ = _AUTO
                    TranslateX = 0x1
                    TranslateY = 0x2
                    TranslateRailsX = 0x4
                    TranslateRailsY = 0x8
                    Rotate = 0x10
                    Scale = 0x20
                    TranslateInertia = 0x40
                    RotateInertia = 0x80
                    ScaleInertia = 0x100
                    All = 0xffff
                    System = 0x10000

                class StandardUICommandKind(_Enum):
                    None_ = _AUTO
                    Cut = _AUTO
                    Copy = _AUTO
                    Paste = _AUTO
                    SelectAll = _AUTO
                    Delete = _AUTO
                    Share = _AUTO
                    Save = _AUTO
                    Close = _AUTO
                    Pause = _AUTO
                    Play = _AUTO
                    Stop = _AUTO
                    Forward = _AUTO
                    Backward = _AUTO
                    Undo = _AUTO
                    Redo = _AUTO

                class XYFocusKeyboardNavigationMode(_Enum):
                    Auto = _AUTO
                    Enabled = _AUTO
                    Disabled = _AUTO

                class XYFocusNavigationStrategy(_Enum):
                    Auto = _AUTO
                    Projection = _AUTO
                    NavigationDirectionDistance = _AUTO
                    RectilinearDistance = _AUTO

                class XYFocusNavigationStrategyOverride(_Enum):
                    None_ = _AUTO
                    Auto = _AUTO
                    Projection = _AUTO
                    NavigationDirectionDistance = _AUTO
                    RectilinearDistance = _AUTO

            class Interop:
                class NotifyCollectionChangedAction(_Enum):
                    Add = _AUTO
                    Remove = _AUTO
                    Replace = _AUTO
                    Move = _AUTO
                    Reset = _AUTO

                class TypeKind(_Enum):
                    Primitive = _AUTO
                    Metadata = _AUTO
                    Custom = _AUTO

            class Media:
                class AcrylicBackgroundSource(_Enum):
                    HostBackdrop = _AUTO
                    Backdrop = _AUTO

                class AlignmentX(_Enum):
                    Left = _AUTO
                    Center = _AUTO
                    Right = _AUTO

                class AlignmentY(_Enum):
                    Top = _AUTO
                    Center = _AUTO
                    Bottom = _AUTO

                class AudioCategory(_Enum):
                    Other = _AUTO
                    ForegroundOnlyMedia = _AUTO
                    BackgroundCapableMedia = _AUTO
                    Communications = _AUTO
                    Alerts = _AUTO
                    SoundEffects = _AUTO
                    GameEffects = _AUTO
                    GameMedia = _AUTO
                    GameChat = _AUTO
                    Speech = _AUTO
                    Movie = _AUTO
                    Media = _AUTO

                class AudioDeviceType(_Enum):
                    Console = _AUTO
                    Multimedia = _AUTO
                    Communications = _AUTO

                class BrushMappingMode(_Enum):
                    Absolute = _AUTO
                    RelativeToBoundingBox = _AUTO

                class ColorInterpolationMode(_Enum):
                    ScRgbLinearInterpolation = _AUTO
                    SRgbLinearInterpolation = _AUTO

                class ElementCompositeMode(_Enum):
                    Inherit = _AUTO
                    SourceOver = _AUTO
                    MinBlend = _AUTO

                class FastPlayFallbackBehaviour(_Enum):
                    Skip = _AUTO
                    Hide = _AUTO
                    Disable = _AUTO

                class FillRule(_Enum):
                    EvenOdd = _AUTO
                    Nonzero = _AUTO

                class GradientSpreadMethod(_Enum):
                    Pad = _AUTO
                    Reflect = _AUTO
                    Repeat = _AUTO

                class LoadedImageSourceLoadStatus(_Enum):
                    Success = _AUTO
                    NetworkError = _AUTO
                    InvalidFormat = _AUTO
                    Other = _AUTO

                class MediaCanPlayResponse(_Enum):
                    NotSupported = _AUTO
                    Maybe = _AUTO
                    Probably = _AUTO

                class MediaElementState(_Enum):
                    Closed = _AUTO
                    Opening = _AUTO
                    Buffering = _AUTO
                    Playing = _AUTO
                    Paused = _AUTO
                    Stopped = _AUTO

                class PenLineCapStyle(_Enum):
                    Flat = _AUTO
                    Square = _AUTO
                    Round = _AUTO
                    Triangle = _AUTO

                class PenLineJoinStyle(_Enum):
                    Miter = _AUTO
                    Bevel = _AUTO
                    Round = _AUTO

                class RevealBrushState(_Enum):
                    Normal = _AUTO
                    PointerOver = _AUTO
                    Pressed = _AUTO

                class Stereo3DVideoPackingMode(_Enum):
                    None_ = _AUTO
                    SideBySide = _AUTO
                    TopBottom = _AUTO

                class Stereo3DVideoRenderMode(_Enum):
                    Mono = _AUTO
                    Stereo = _AUTO

                class Stretch(_Enum):
                    None_ = _AUTO
                    Fill = _AUTO
                    Uniform = _AUTO
                    UniformToFill = _AUTO

                class StyleSimulations(_Enum):
                    None_ = _AUTO
                    BoldSimulation = _AUTO
                    ItalicSimulation = _AUTO
                    BoldItalicSimulation = _AUTO

                class SweepDirection(_Enum):
                    Counterclockwise = _AUTO
                    Clockwise = _AUTO

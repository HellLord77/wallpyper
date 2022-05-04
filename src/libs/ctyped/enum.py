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
    class _EnumMeta(type(_type.c_uint)):
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


GpMatrixOrder = MatrixOrder
GpUnit = Unit
GpStatus = Status


class Windows:
    class Foundation:
        class AsyncStatus(_Enum):
            Started = _AUTO
            Completed = _AUTO
            Canceled = _AUTO
            Error = _AUTO

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
            class InputStreamOptions(_Enum):
                None_ = _AUTO
                Partial = 0x1
                ReadAhead = 0x2

    class UI:
        class Notifications:
            class NotificationMirroring(_Enum):
                Allowed = _AUTO
                Disabled = _AUTO

            class NotificationSetting(_Enum):
                Enabled = _AUTO
                DisabledForApplication = _AUTO
                DisabledForUser = _AUTO
                DisabledByGroupPolicy = _AUTO
                DisabledByManifest = _AUTO

            class ToastDismissalReason(_Enum):
                UserCanceled = _AUTO
                ApplicationHidden = _AUTO
                TimedOut = _AUTO

        class ViewManagement:
            class HandPreference(_Enum):
                LeftHanded = _AUTO
                RightHanded = _AUTO

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

        class Xaml:
            class FlowDirection(_Enum):
                LeftToRight = _AUTO
                RightToLeft = _AUTO

            class FocusState(_Enum):
                Unfocused = _AUTO
                Pointer = _AUTO
                Keyboard = _AUTO
                Programmatic = _AUTO

            class HorizontalAlignment(_Enum):
                Left = _AUTO
                Center = _AUTO
                Right = _AUTO
                Stretch = _AUTO

            class LineStackingStrategy(_Enum):
                MaxHeight = _AUTO
                BlockLineHeight = _AUTO
                BaselineToBaseline = _AUTO

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

                class Orientation(_Enum):
                    Vertical = _AUTO
                    Horizontal = _AUTO

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
                class ManipulationModes(_Enum):
                    None_ = 0
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

            class Interop:
                class TypeKind(_Enum):
                    Primitive = _AUTO
                    Metadata = _AUTO
                    Custom = _AUTO

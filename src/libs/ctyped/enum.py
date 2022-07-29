from __future__ import annotations as _

import enum as _enum
from typing import Optional as _Optional

from . import const as _const, type as _type
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


# noinspection PyPep8Naming
class DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY(_Enum):
    OTHER = -1
    HD15 = _AUTO
    SVIDEO = _AUTO
    COMPOSITE_VIDEO = _AUTO
    COMPONENT_VIDEO = _AUTO
    DVI = _AUTO
    HDMI = _AUTO
    LVDS = _AUTO
    D_JPN = _AUTO
    SDI = _AUTO
    DISPLAYPORT_EXTERNAL = _AUTO
    DISPLAYPORT_EMBEDDED = _AUTO
    UDI_EXTERNAL = _AUTO
    UDI_EMBEDDED = _AUTO
    SDTVDONGLE = _AUTO
    MIRACAST = _AUTO
    INDIRECT_WIRED = _AUTO
    INDIRECT_VIRTUAL = _AUTO
    DESPLAYPORT_USB_TUNNEL = _AUTO
    INTERNAL = 0x80000000
    FORCE_UINT32 = 0xFFFFFFFF


# noinspection PyPep8Naming
class DISPLAYCONFIG_SCANLINE_ORDERING(_Enum):
    UNSPECIFIED = _AUTO
    PROGRESSIVE = _AUTO
    INTERLACED = 2
    INTERLACED_UPPERFIELDFIRST = INTERLACED
    INTERLACED_LOWERFIELDFIRST = _AUTO
    FORCE_UINT32 = 0xFFFFFFFF


# noinspection PyPep8Naming
class DISPLAYCONFIG_SCALING(_Enum):
    IDENTITY = 1
    CENTERED = _AUTO
    STRETCHED = _AUTO
    ASPECTRATIOCENTEREDMAX = _AUTO
    CUSTOM = _AUTO
    PREFERRED = 128
    FORCE_UINT32 = 0xFFFFFFFF


# noinspection PyPep8Naming
class DISPLAYCONFIG_ROTATION(_Enum):
    IDENTITY = 1
    ROTATE90 = _AUTO
    ROTATE180 = _AUTO
    ROTATE270 = _AUTO
    FORCE_UINT32 = 0xFFFFFFFF


# noinspection PyPep8Naming
class DISPLAYCONFIG_MODE_INFO_TYPE(_Enum):
    SOURCE = 1
    TARGET = _AUTO
    DESKTOP_IMAGE = _AUTO
    FORCE_UINT32 = 0xFFFFFFFF


# noinspection PyPep8Naming
class DISPLAYCONFIG_PIXELFORMAT(_Enum):
    DP_8BPP = 1
    DP_16BPP = _AUTO
    DP_24BPP = _AUTO
    DP_32BPP = _AUTO
    DP_NONGDI = _AUTO
    DP_FORCE_UINT32 = 0xffffffff


# noinspection PyPep8Naming
class DISPLAYCONFIG_TOPOLOGY_ID(_Enum):
    INTERNAL = 0x00000001
    CLONE = 0x00000002
    EXTEND = 0x00000004
    EXTERNAL = 0x00000008
    FORCE_UINT32 = 0xFFFFFFFF


# noinspection PyPep8Naming
class DISPLAYCONFIG_DEVICE_INFO_TYPE(_Enum):
    GET_SOURCE_NAME = 1
    GET_TARGET_NAME = _AUTO
    GET_TARGET_PREFERRED_MODE = _AUTO
    GET_ADAPTER_NAME = _AUTO
    SET_TARGET_PERSISTENCE = _AUTO
    GET_TARGET_BASE_TYPE = _AUTO
    GET_SUPPORT_VIRTUAL_RESOLUTION = _AUTO
    SET_SUPPORT_VIRTUAL_RESOLUTION = _AUTO
    GET_ADVANCED_COLOR_INFO = _AUTO
    SET_ADVANCED_COLOR_STATE = _AUTO
    GET_SDR_WHITE_LEVEL = _AUTO
    GET_MONITOR_SPECIALIZATION = _AUTO
    SET_MONITOR_SPECIALIZATION = _AUTO
    FORCE_UINT32 = 0xFFFFFFFF


class BrushType(_Enum):
    SolidColor = 0
    HatchFill = 1
    TextureFill = 2
    PathGradient = 3
    LinearGradient = 4


class CombineMode(_Enum):
    Replace = 0
    Intersect = 1
    Union = 2
    Xor = 3
    Exclude = 4
    Complement = 5


class CompositingMode(_Enum):
    SourceOver = 0
    SourceCopy = 1


class CompositingQuality(_Enum):
    Default = 0
    HighSpeed = 1
    HighQuality = 2
    GammaCorrected = 3
    AssumeLinear = 4


class CoordinateSpace(_Enum):
    World = 0
    Page = 1
    Device = 2


class CustomLineCapType(_Enum):
    Default = 0
    AdjustableArrow = 1


class DashCap(_Enum):
    Flat = 0
    Round = 2
    Triangle = 3


class DashStyle(_Enum):
    Solid = 0
    Dash = 1
    Dot = 2
    DashDot = 3
    DashDotDot = 4
    Custom = 5


class DitherType(_Enum):
    None_ = 0
    Solid = 1
    Ordered4x4 = 2
    Ordered8x8 = 3
    Ordered16x16 = 4
    Ordered91x91 = 5
    Spiral4x4 = 6
    Spiral8x8 = 7
    DualSpiral4x4 = 8
    DualSpiral8x8 = 9
    ErrorDiffusion = 10


class DriverStringOptions(_Enum):
    CmapLookup = 1
    Vertical = 2
    RealizedAdvance = 4
    LimitSubpixel = 8


class EmfToWmfBitsFlags(_Enum):
    Default = 0
    EmbedEmf = 1
    IncludePlaceable = 2
    NoXORClip = 4


class EmfType(_Enum):
    EmfOnly = 3
    EmfPlusOnly = 4
    EmfPlusDual = 5


class EncoderParameterValueType(_Enum):
    Byte = 1
    ASCII = 2
    Short = 3
    Long = 4
    Rational = 5
    LongRange = 6
    Undefined = 7
    RationalRange = 8
    Pointer = 9


class EncoderValue(_Enum):
    ColorTypeCMYK = 0
    ColorTypeYCCK = 1
    CompressionLZW = 2
    CompressionCCITT3 = 3
    CompressionCCITT4 = 4
    CompressionRle = 5
    CompressionNone = 6
    ScanMethodInterlaced = 7
    ScanMethodNonInterlaced = 8
    VersionGif87 = 9
    VersionGif89 = 10
    RenderProgressive = 11
    RenderNonProgressive = 12
    TransformRotate90 = 13
    TransformRotate180 = 14
    TransformRotate270 = 15
    TransformFlipHorizontal = 16
    TransformFlipVertical = 17
    MultiFrame = 18
    LastFrame = 19
    Flush = 20
    FrameDimensionTime = 21
    FrameDimensionResolution = 22
    FrameDimensionPage = 23


class FillMode(_Enum):
    Alternate = 0
    Winding = 1


class FlushIntention(_Enum):
    Flush = 0
    Sync = 1


class FontStyle(_Enum):
    Regular = 0
    Bold = 1
    Italic = 2
    BoldItalic = 3
    Underline = 4
    Strikeout = 8


class HatchStyle(_Enum):
    HS_Horizontal = 0
    HS_Vertical = 1
    HS_ForwardDiagonal = 2
    HS_BackwardDiagonal = 3
    HS_Cross = 4
    HS_LargeGrid = 4
    HS_DiagonalCross = 5
    HS_05Percent = 6
    HS_10Percent = 7
    HS_20Percent = 8
    HS_25Percent = 9
    HS_30Percent = 10
    HS_40Percent = 11
    HS_50Percent = 12
    HS_60Percent = 13
    HS_70Percent = 14
    HS_75Percent = 15
    HS_80Percent = 16
    HS_90Percent = 17
    HS_LightDownwardDiagonal = 18
    HS_LightUpwardDiagonal = 19
    HS_DarkDownwardDiagonal = 20
    HS_DarkUpwardDiagonal = 21
    HS_WideDownwardDiagonal = 22
    HS_WideUpwardDiagonal = 23
    HS_LightVertical = 24
    HS_LightHorizontal = 25
    HS_NarrowVertical = 26
    HS_NarrowHorizontal = 27
    HS_DarkVertical = 28
    HS_DarkHorizontal = 29
    HS_DashedDownwardDiagonal = 30
    HS_DashedUpwardDiagonal = 31
    HS_DashedHorizontal = 32
    HS_DashedVertical = 33
    HS_SmallConfetti = 34
    HS_LargeConfetti = 35
    HS_ZigZag = 36
    HS_Wave = 37
    HS_DiagonalBrick = 38
    HS_HorizontalBrick = 39
    HS_Weave = 40
    HS_Plaid = 41
    HS_Divot = 42
    HS_DottedGrid = 43
    HS_DottedDiamond = 44
    HS_Shingle = 45
    HS_Trellis = 46
    HS_Sphere = 47
    HS_SmallGrid = 48
    HS_SmallCheckerBoard = 49
    HS_LargeCheckerBoard = 50
    HS_OutlinedDiamond = 51
    HS_SolidDiamond = 52
    HS_Total = 53
    HS_Min = 0
    HS_Max = 52


class HotkeyPrefix(_Enum):
    None_ = 0
    Show = 1
    Hide = 2


class ImageType(_Enum):
    Unknown = 0
    Bitmap = 1
    Metafile = 2


class InterpolationMode(_Enum):
    Invalid = -1
    Default = 0
    LowQuality = 1
    HighQuality = 2
    Bilinear = 3
    Bicubic = 4
    NearestNeighbor = 5
    HighQualityBilinear = 6
    HighQualityBicubic = 7


class LinearGradientMode(_Enum):
    Horizontal = 0
    Vertical = 1
    ForwardDiagonal = 2
    BackwardDiagonal = 3


class LineCap(_Enum):
    Flat = 0
    Square = 1
    Round = 2
    Triangle = 3
    NoAnchor = 16
    SquareAnchor = 17
    RoundAnchor = 18
    DiamondAnchor = 19
    ArrowAnchor = 20
    Custom = 255


class LineJoin(_Enum):
    Miter = 0
    Bevel = 1
    Round = 2
    MiterClipped = 3


class MatrixOrder(_Enum):
    Prepend = 0
    Append = 1


class MetafileFrameUnit(_Enum):
    Pixel = 2
    Point = 3
    Inch = 4
    Document = 5
    Millimeter = 6
    Gdi = 7


class MetafileType(_Enum):
    Invalid = 0
    Wmf = 1
    WmfPlaceable = 2
    Emf = 3
    EmfPlusOnly = 4
    EmfPlusDual = 5


class ObjectType(_Enum):
    Invalid = 0
    Brush = 1
    Pen = 2
    Path = 3
    Region = 4
    Font = 5
    StringFormat = 6
    ImageAttributes = 7
    CustomLineCap = 8
    Graphics = 9
    Min = 1
    Max = 9


class EmfPlusRecordType(_Enum):  # TODO
    WmfRecordTypeSetBkColor = _const.META_SETBKCOLOR | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetBkMode = _const.META_SETBKMODE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetMapMode = _const.META_SETMAPMODE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetROP2 = _const.META_SETROP2 | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetRelAbs = _const.META_SETRELABS | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetPolyFillMode = _const.META_SETPOLYFILLMODE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetStretchBltMode = _const.META_SETSTRETCHBLTMODE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetTextCharExtra = _const.META_SETTEXTCHAREXTRA | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetTextColor = _const.META_SETTEXTCOLOR | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetTextJustification = _const.META_SETTEXTJUSTIFICATION | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetWindowOrg = _const.META_SETWINDOWORG | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetWindowExt = _const.META_SETWINDOWEXT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetViewportOrg = _const.META_SETVIEWPORTORG | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetViewportExt = _const.META_SETVIEWPORTEXT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeOffsetWindowOrg = _const.META_OFFSETWINDOWORG | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeScaleWindowExt = _const.META_SCALEWINDOWEXT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeOffsetViewportOrg = _const.META_OFFSETVIEWPORTORG | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeScaleViewportExt = _const.META_SCALEVIEWPORTEXT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeLineTo = _const.META_LINETO | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeMoveTo = _const.META_MOVETO | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeExcludeClipRect = _const.META_EXCLUDECLIPRECT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeIntersectClipRect = _const.META_INTERSECTCLIPRECT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeArc = _const.META_ARC | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeEllipse = _const.META_ELLIPSE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeFloodFill = _const.META_FLOODFILL | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypePie = _const.META_PIE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeRectangle = _const.META_RECTANGLE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeRoundRect = _const.META_ROUNDRECT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypePatBlt = _const.META_PATBLT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSaveDC = _const.META_SAVEDC | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetPixel = _const.META_SETPIXEL | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeOffsetClipRgn = _const.META_OFFSETCLIPRGN | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeTextOut = _const.META_TEXTOUT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeBitBlt = _const.META_BITBLT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeStretchBlt = _const.META_STRETCHBLT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypePolygon = _const.META_POLYGON | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypePolyline = _const.META_POLYLINE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeEscape = _const.META_ESCAPE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeRestoreDC = _const.META_RESTOREDC | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeFillRegion = _const.META_FILLREGION | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeFrameRegion = _const.META_FRAMEREGION | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeInvertRegion = _const.META_INVERTREGION | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypePaintRegion = _const.META_PAINTREGION | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSelectClipRegion = _const.META_SELECTCLIPREGION | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSelectObject = _const.META_SELECTOBJECT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetTextAlign = _const.META_SETTEXTALIGN | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeDrawText = 0x062F | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeChord = _const.META_CHORD | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetMapperFlags = _const.META_SETMAPPERFLAGS | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeExtTextOut = _const.META_EXTTEXTOUT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetDIBToDev = _const.META_SETDIBTODEV | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSelectPalette = _const.META_SELECTPALETTE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeRealizePalette = _const.META_REALIZEPALETTE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeAnimatePalette = _const.META_ANIMATEPALETTE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetPalEntries = _const.META_SETPALENTRIES | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypePolyPolygon = _const.META_POLYPOLYGON | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeResizePalette = _const.META_RESIZEPALETTE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeDIBBitBlt = _const.META_DIBBITBLT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeDIBStretchBlt = _const.META_DIBSTRETCHBLT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeDIBCreatePatternBrush = _const.META_DIBCREATEPATTERNBRUSH | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeStretchDIB = _const.META_STRETCHDIB | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeExtFloodFill = _const.META_EXTFLOODFILL | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeSetLayout = 0x0149 | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeResetDC = 0x014C | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeStartDoc = 0x014D | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeStartPage = 0x004F | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeEndPage = 0x0050 | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeAbortDoc = 0x0052 | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeEndDoc = 0x005E | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeDeleteObject = _const.META_DELETEOBJECT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeCreatePalette = _const.META_CREATEPALETTE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeCreateBrush = 0x00F8 | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeCreatePatternBrush = _const.META_CREATEPATTERNBRUSH | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeCreatePenIndirect = _const.META_CREATEPENINDIRECT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeCreateFontIndirect = _const.META_CREATEFONTINDIRECT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeCreateBrushIndirect = _const.META_CREATEBRUSHINDIRECT | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeCreateBitmapIndirect = 0x02FD | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeCreateBitmap = 0x06FE | _const.GDIP_WMF_RECORD_BASE
    WmfRecordTypeCreateRegion = _const.META_CREATEREGION | _const.GDIP_WMF_RECORD_BASE
    EmfRecordTypeHeader = _const.EMR_HEADER
    EmfRecordTypePolyBezier = _const.EMR_POLYBEZIER
    EmfRecordTypePolygon = _const.EMR_POLYGON
    EmfRecordTypePolyline = _const.EMR_POLYLINE
    EmfRecordTypePolyBezierTo = _const.EMR_POLYBEZIERTO
    EmfRecordTypePolyLineTo = _const.EMR_POLYLINETO
    EmfRecordTypePolyPolyline = _const.EMR_POLYPOLYLINE
    EmfRecordTypePolyPolygon = _const.EMR_POLYPOLYGON
    EmfRecordTypeSetWindowExtEx = _const.EMR_SETWINDOWEXTEX
    EmfRecordTypeSetWindowOrgEx = _const.EMR_SETWINDOWORGEX
    EmfRecordTypeSetViewportExtEx = _const.EMR_SETVIEWPORTEXTEX
    EmfRecordTypeSetViewportOrgEx = _const.EMR_SETVIEWPORTORGEX
    EmfRecordTypeSetBrushOrgEx = _const.EMR_SETBRUSHORGEX
    EmfRecordTypeEOF = _const.EMR_EOF
    EmfRecordTypeSetPixelV = _const.EMR_SETPIXELV
    EmfRecordTypeSetMapperFlags = _const.EMR_SETMAPPERFLAGS
    EmfRecordTypeSetMapMode = _const.EMR_SETMAPMODE
    EmfRecordTypeSetBkMode = _const.EMR_SETBKMODE
    EmfRecordTypeSetPolyFillMode = _const.EMR_SETPOLYFILLMODE
    EmfRecordTypeSetROP2 = _const.EMR_SETROP2
    EmfRecordTypeSetStretchBltMode = _const.EMR_SETSTRETCHBLTMODE
    EmfRecordTypeSetTextAlign = _const.EMR_SETTEXTALIGN
    EmfRecordTypeSetColorAdjustment = _const.EMR_SETCOLORADJUSTMENT
    EmfRecordTypeSetTextColor = _const.EMR_SETTEXTCOLOR
    EmfRecordTypeSetBkColor = _const.EMR_SETBKCOLOR
    EmfRecordTypeOffsetClipRgn = _const.EMR_OFFSETCLIPRGN
    EmfRecordTypeMoveToEx = _const.EMR_MOVETOEX
    EmfRecordTypeSetMetaRgn = _const.EMR_SETMETARGN
    EmfRecordTypeExcludeClipRect = _const.EMR_EXCLUDECLIPRECT
    EmfRecordTypeIntersectClipRect = _const.EMR_INTERSECTCLIPRECT
    EmfRecordTypeScaleViewportExtEx = _const.EMR_SCALEVIEWPORTEXTEX
    EmfRecordTypeScaleWindowExtEx = _const.EMR_SCALEWINDOWEXTEX
    EmfRecordTypeSaveDC = _const.EMR_SAVEDC
    EmfRecordTypeRestoreDC = _const.EMR_RESTOREDC
    EmfRecordTypeSetWorldTransform = _const.EMR_SETWORLDTRANSFORM
    EmfRecordTypeModifyWorldTransform = _const.EMR_MODIFYWORLDTRANSFORM
    EmfRecordTypeSelectObject = _const.EMR_SELECTOBJECT
    EmfRecordTypeCreatePen = _const.EMR_CREATEPEN
    EmfRecordTypeCreateBrushIndirect = _const.EMR_CREATEBRUSHINDIRECT
    EmfRecordTypeDeleteObject = _const.EMR_DELETEOBJECT
    EmfRecordTypeAngleArc = _const.EMR_ANGLEARC
    EmfRecordTypeEllipse = _const.EMR_ELLIPSE
    EmfRecordTypeRectangle = _const.EMR_RECTANGLE
    EmfRecordTypeRoundRect = _const.EMR_ROUNDRECT
    EmfRecordTypeArc = _const.EMR_ARC
    EmfRecordTypeChord = _const.EMR_CHORD
    EmfRecordTypePie = _const.EMR_PIE
    EmfRecordTypeSelectPalette = _const.EMR_SELECTPALETTE
    EmfRecordTypeCreatePalette = _const.EMR_CREATEPALETTE
    EmfRecordTypeSetPaletteEntries = _const.EMR_SETPALETTEENTRIES
    EmfRecordTypeResizePalette = _const.EMR_RESIZEPALETTE
    EmfRecordTypeRealizePalette = _const.EMR_REALIZEPALETTE
    EmfRecordTypeExtFloodFill = _const.EMR_EXTFLOODFILL
    EmfRecordTypeLineTo = _const.EMR_LINETO
    EmfRecordTypeArcTo = _const.EMR_ARCTO
    EmfRecordTypePolyDraw = _const.EMR_POLYDRAW
    EmfRecordTypeSetArcDirection = _const.EMR_SETARCDIRECTION
    EmfRecordTypeSetMiterLimit = _const.EMR_SETMITERLIMIT
    EmfRecordTypeBeginPath = _const.EMR_BEGINPATH
    EmfRecordTypeEndPath = _const.EMR_ENDPATH
    EmfRecordTypeCloseFigure = _const.EMR_CLOSEFIGURE
    EmfRecordTypeFillPath = _const.EMR_FILLPATH
    EmfRecordTypeStrokeAndFillPath = _const.EMR_STROKEANDFILLPATH
    EmfRecordTypeStrokePath = _const.EMR_STROKEPATH
    EmfRecordTypeFlattenPath = _const.EMR_FLATTENPATH
    EmfRecordTypeWidenPath = _const.EMR_WIDENPATH
    EmfRecordTypeSelectClipPath = _const.EMR_SELECTCLIPPATH
    EmfRecordTypeAbortPath = _const.EMR_ABORTPATH
    EmfRecordTypeReserved_069 = 69
    EmfRecordTypeGdiComment = _const.EMR_GDICOMMENT
    EmfRecordTypeFillRgn = _const.EMR_FILLRGN
    EmfRecordTypeFrameRgn = _const.EMR_FRAMERGN
    EmfRecordTypeInvertRgn = _const.EMR_INVERTRGN
    EmfRecordTypePaintRgn = _const.EMR_PAINTRGN
    EmfRecordTypeExtSelectClipRgn = _const.EMR_EXTSELECTCLIPRGN
    EmfRecordTypeBitBlt = _const.EMR_BITBLT
    EmfRecordTypeStretchBlt = _const.EMR_STRETCHBLT
    EmfRecordTypeMaskBlt = _const.EMR_MASKBLT
    EmfRecordTypePlgBlt = _const.EMR_PLGBLT
    EmfRecordTypeSetDIBitsToDevice = _const.EMR_SETDIBITSTODEVICE
    EmfRecordTypeStretchDIBits = _const.EMR_STRETCHDIBITS
    EmfRecordTypeExtCreateFontIndirect = _const.EMR_EXTCREATEFONTINDIRECTW
    EmfRecordTypeExtTextOutA = _const.EMR_EXTTEXTOUTA
    EmfRecordTypeExtTextOutW = _const.EMR_EXTTEXTOUTW
    EmfRecordTypePolyBezier16 = _const.EMR_POLYBEZIER16
    EmfRecordTypePolygon16 = _const.EMR_POLYGON16
    EmfRecordTypePolyline16 = _const.EMR_POLYLINE16
    EmfRecordTypePolyBezierTo16 = _const.EMR_POLYBEZIERTO16
    EmfRecordTypePolylineTo16 = _const.EMR_POLYLINETO16
    EmfRecordTypePolyPolyline16 = _const.EMR_POLYPOLYLINE16
    EmfRecordTypePolyPolygon16 = _const.EMR_POLYPOLYGON16
    EmfRecordTypePolyDraw16 = _const.EMR_POLYDRAW16
    EmfRecordTypeCreateMonoBrush = _const.EMR_CREATEMONOBRUSH
    EmfRecordTypeCreateDIBPatternBrushPt = _const.EMR_CREATEDIBPATTERNBRUSHPT
    EmfRecordTypeExtCreatePen = _const.EMR_EXTCREATEPEN
    EmfRecordTypePolyTextOutA = _const.EMR_POLYTEXTOUTA
    EmfRecordTypePolyTextOutW = _const.EMR_POLYTEXTOUTW
    EmfRecordTypeSetICMMode = 98
    EmfRecordTypeCreateColorSpace = 99
    EmfRecordTypeSetColorSpace = 100
    EmfRecordTypeDeleteColorSpace = 101
    EmfRecordTypeGLSRecord = 102
    EmfRecordTypeGLSBoundedRecord = 103
    EmfRecordTypePixelFormat = 104
    EmfRecordTypeDrawEscape = 105
    EmfRecordTypeExtEscape = 106
    EmfRecordTypeStartDoc = 107
    EmfRecordTypeSmallTextOut = 108
    EmfRecordTypeForceUFIMapping = 109
    EmfRecordTypeNamedEscape = 110
    EmfRecordTypeColorCorrectPalette = 111
    EmfRecordTypeSetICMProfileA = 112
    EmfRecordTypeSetICMProfileW = 113
    EmfRecordTypeAlphaBlend = 114
    EmfRecordTypeSetLayout = 115
    EmfRecordTypeTransparentBlt = 116
    EmfRecordTypeReserved_117 = 117
    EmfRecordTypeGradientFill = 118
    EmfRecordTypeSetLinkedUFIs = 119
    EmfRecordTypeSetTextJustification = 120
    EmfRecordTypeColorMatchToTargetW = 121
    EmfRecordTypeCreateColorSpaceW = 122
    EmfRecordTypeMax = 122
    EmfRecordTypeMin = 1
    EmfPlusRecordTypeInvalid = _const.GDIP_EMFPLUS_RECORD_BASE
    EmfPlusRecordTypeHeader = _AUTO
    EmfPlusRecordTypeEndOfFile = _AUTO
    EmfPlusRecordTypeComment = _AUTO
    EmfPlusRecordTypeGetDC = _AUTO
    EmfPlusRecordTypeMultiFormatStart = _AUTO
    EmfPlusRecordTypeMultiFormatSection = _AUTO
    EmfPlusRecordTypeMultiFormatEnd = _AUTO
    EmfPlusRecordTypeObject = _AUTO
    EmfPlusRecordTypeClear = _AUTO
    EmfPlusRecordTypeFillRects = _AUTO
    EmfPlusRecordTypeDrawRects = _AUTO
    EmfPlusRecordTypeFillPolygon = _AUTO
    EmfPlusRecordTypeDrawLines = _AUTO
    EmfPlusRecordTypeFillEllipse = _AUTO
    EmfPlusRecordTypeDrawEllipse = _AUTO
    EmfPlusRecordTypeFillPie = _AUTO
    EmfPlusRecordTypeDrawPie = _AUTO
    EmfPlusRecordTypeDrawArc = _AUTO
    EmfPlusRecordTypeFillRegion = _AUTO
    EmfPlusRecordTypeFillPath = _AUTO
    EmfPlusRecordTypeDrawPath = _AUTO
    EmfPlusRecordTypeFillClosedCurve = _AUTO
    EmfPlusRecordTypeDrawClosedCurve = _AUTO
    EmfPlusRecordTypeDrawCurve = _AUTO
    EmfPlusRecordTypeDrawBeziers = _AUTO
    EmfPlusRecordTypeDrawImage = _AUTO
    EmfPlusRecordTypeDrawImagePoints = _AUTO
    EmfPlusRecordTypeDrawString = _AUTO
    EmfPlusRecordTypeSetRenderingOrigin = _AUTO
    EmfPlusRecordTypeSetAntiAliasMode = _AUTO
    EmfPlusRecordTypeSetTextRenderingHint = _AUTO
    EmfPlusRecordTypeSetTextContrast = _AUTO
    EmfPlusRecordTypeSetInterpolationMode = _AUTO
    EmfPlusRecordTypeSetPixelOffsetMode = _AUTO
    EmfPlusRecordTypeSetCompositingMode = _AUTO
    EmfPlusRecordTypeSetCompositingQuality = _AUTO
    EmfPlusRecordTypeSave = _AUTO
    EmfPlusRecordTypeRestore = _AUTO
    EmfPlusRecordTypeBeginContainer = _AUTO
    EmfPlusRecordTypeBeginContainerNoParams = _AUTO
    EmfPlusRecordTypeEndContainer = _AUTO
    EmfPlusRecordTypeSetWorldTransform = _AUTO
    EmfPlusRecordTypeResetWorldTransform = _AUTO
    EmfPlusRecordTypeMultiplyWorldTransform = _AUTO
    EmfPlusRecordTypeTranslateWorldTransform = _AUTO
    EmfPlusRecordTypeScaleWorldTransform = _AUTO
    EmfPlusRecordTypeRotateWorldTransform = _AUTO
    EmfPlusRecordTypeSetPageTransform = _AUTO
    EmfPlusRecordTypeResetClip = _AUTO
    EmfPlusRecordTypeSetClipRect = _AUTO
    EmfPlusRecordTypeSetClipPath = _AUTO
    EmfPlusRecordTypeSetClipRegion = _AUTO
    EmfPlusRecordTypeOffsetClip = _AUTO
    EmfPlusRecordTypeDrawDriverString = _AUTO
    if _const.GDIPVER >= 0x0110:
        EmfPlusRecordTypeStrokeFillPath = _AUTO
        EmfPlusRecordTypeSerializableObject = _AUTO
        EmfPlusRecordTypeSetTSGraphics = _AUTO
        EmfPlusRecordTypeSetTSClip = _AUTO
    EmfPlusRecordTotal = _AUTO
    # EmfPlusRecordTypeMax = EmfPlusRecordTotal - 1
    EmfPlusRecordTypeMin = EmfPlusRecordTypeHeader


class PathPointType(_Enum):
    Start = 0
    Line = 1
    Bezier = 3
    Bezier3 = 3
    PathTypeMask = 7
    PathDashMode = 16
    PathMarker = 32
    CloseSubpath = 128


class PenAlignment(_Enum):
    Center = 0
    Inset = 1


class PenType(_Enum):
    Unknown = -1
    SolidColor = 0
    HatchFill = 1
    TextureFill = 2
    PathGradient = 3
    LinearGradient = 4


class PixelOffsetMode(_Enum):
    Invalid = -1
    Default = 0
    HighSpeed = 1
    HighQuality = 2
    None_ = 3
    Half = 4


class QualityMode(_Enum):
    Invalid = -1
    Default = 0
    Low = 1
    High = 2


class SmoothingMode(_Enum):
    Invalid = -1
    Default = 0
    HighSpeed = 1
    HighQuality = 2
    None_ = 3
    AntiAlias8x4 = 4
    AntiAlias = 4
    AntiAlias8x8 = 5


class StringAlignment(_Enum):
    Near = 0
    Center = 1
    Far = 2


class StringDigitSubstitute(_Enum):
    User = 0
    None_ = 1
    National = 2
    Traditional = 3


class StringFormatFlags(_Enum):
    DirectionRightToLeft = 1
    DirectionVertical = 2
    NoFitBlackBox = 4
    DisplayFormatControl = 32
    NoFontFallback = 1024
    MeasureTrailingSpaces = 2048
    NoWrap = 4096
    LineLimit = 8192
    NoClip = 16384


class StringTrimming(_Enum):
    None_ = 0
    Character = 1
    Word = 2
    EllipsisCharacter = 3
    EllipsisWord = 4
    EllipsisPath = 5


class TextRenderingHint(_Enum):
    SystemDefault = 0
    SingleBitPerPixelGridFit = 1
    SingleBitPerPixel = 2
    AntiAliasGridFit = 3
    AntiAlias = 4
    ClearTypeGridFit = 5


class Unit(_Enum):
    World = 0
    Display = 1
    Pixel = 2
    Point = 3
    Inch = 4
    Document = 5
    Millimeter = 6


class WarpMode(_Enum):
    Perspective = 0
    Bilinear = 1


class WrapMode(_Enum):
    Tile = 0
    TileFlipX = 1
    TileFlipY = 2
    TileFlipXY = 3
    Clamp = 4


class GpTestControlEnum(_Enum):
    TestControlForceBilinear = 0
    TestControlForceNoICM = 1
    TestControlGetBuildNumber = 2


class Status(_Enum):
    Ok = 0
    GenericError = 1
    InvalidParameter = 2
    OutOfMemory = 3
    ObjectBusy = 4
    InsufficientBuffer = 5
    NotImplemented = 6
    Win32Error = 7
    WrongState = 8
    Aborted = 9
    FileNotFound = 10
    ValueOverflow = 11
    AccessDenied = 12
    UnknownImageFormat = 13
    FontFamilyNotFound = 14
    FontStyleNotFound = 15
    NotTrueTypeFont = 16
    UnsupportedGdiplusVersion = 17
    GdiplusNotInitialized = 18
    PropertyNotFound = 19
    PropertyNotSupported = 20
    ProfileNotFound = 21


class ImageCodecFlags(_Enum):
    Encoder = 1
    Decoder = 2
    SupportBitmap = 4
    SupportVector = 8
    SeekableEncode = 16
    BlockingDecode = 32
    Builtin = 65536
    System = 131072
    User = 262144


class ImageFlags(_Enum):
    None_ = 0
    Scalable = 1
    HasAlpha = 2
    HasTranslucent = 4
    PartiallyScalable = 8
    ColorSpaceRGB = 16
    ColorSpaceCMYK = 32
    ColorSpaceGRAY = 64
    ColorSpaceYCBCR = 128
    ColorSpaceYCCK = 256
    HasRealDPI = 4096
    HasRealPixelSize = 8192
    ReadOnly = 65536
    Caching = 131072


class ImageLockMode(_Enum):
    Read = 1
    Write = 2
    UserInputBuf = 4


class ItemDataPosition(_Enum):
    AfterHeader = 0
    AfterPalette = 1
    AfterBits = 2


class RotateFlipType(_Enum):
    RotateNoneFlipNone = 0
    Rotate90FlipNone = 1
    Rotate180FlipNone = 2
    Rotate270FlipNone = 3
    RotateNoneFlipX = 4
    Rotate90FlipX = 5
    Rotate180FlipX = 6
    Rotate270FlipX = 7
    Rotate180FlipXY = 0
    Rotate270FlipXY = 1
    RotateNoneFlipXY = 2
    Rotate90FlipXY = 3
    Rotate180FlipY = 4
    Rotate270FlipY = 5
    RotateNoneFlipY = 6
    Rotate90FlipY = 7


class PaletteFlags(_Enum):
    HasAlpha = 1
    GrayScale = 2
    Halftone = 4


class PaletteType(_Enum):
    Custom = 0
    Optimal = 1
    FixedBW = 2
    FixedHalftone8 = 3
    FixedHalftone27 = 4
    FixedHalftone64 = 5
    FixedHalftone125 = 6
    FixedHalftone216 = 7
    FixedHalftone252 = 8
    FixedHalftone256 = 9


class ColorChannelFlags(_Enum):
    C = 0
    M = 1
    Y = 2
    K = 3
    Last = 4


class ColorAdjustType(_Enum):
    Default = 0
    Bitmap = 1
    Brush = 2
    Pen = 3
    Text = 4
    Count = 5
    Any = 6


class ColorMatrixFlags(_Enum):
    Default = 0
    SkipGrays = 1
    AltGray = 2


class HistogramFormat(_Enum):
    ARGB = 0
    PARGB = 1
    RGB = 2
    Gray = 3
    B = 4
    G = 5
    R = 6
    A = 7


class CurveAdjustments(_Enum):
    Exposure = 0
    Density = 1
    Contrast = 2
    Highlight = 3
    Shadow = 4
    Midtone = 5
    WhiteSaturation = 6
    BlackSaturation = 7


class CurveChannel(_Enum):
    All = 0
    Red = 1
    Green = 2
    Blue = 3


# noinspection PyPep8Naming
class DXGI_FORMAT(_Enum):
    DF_UNKNOWN = _AUTO
    DF_R32G32B32A32_TYPELESS = _AUTO
    DF_R32G32B32A32_FLOAT = _AUTO
    DF_R32G32B32A32_UINT = _AUTO
    DF_R32G32B32A32_SINT = _AUTO
    DF_R32G32B32_TYPELESS = _AUTO
    DF_R32G32B32_FLOAT = _AUTO
    DF_R32G32B32_UINT = _AUTO
    DF_R32G32B32_SINT = _AUTO
    DF_R16G16B16A16_TYPELESS = _AUTO
    DF_R16G16B16A16_FLOAT = _AUTO
    DF_R16G16B16A16_UNORM = _AUTO
    DF_R16G16B16A16_UINT = _AUTO
    DF_R16G16B16A16_SNORM = _AUTO
    DF_R16G16B16A16_SINT = _AUTO
    DF_R32G32_TYPELESS = _AUTO
    DF_R32G32_FLOAT = _AUTO
    DF_R32G32_UINT = _AUTO
    DF_R32G32_SINT = _AUTO
    DF_R32G8X24_TYPELESS = _AUTO
    DF_D32_FLOAT_S8X24_UINT = _AUTO
    DF_R32_FLOAT_X8X24_TYPELESS = _AUTO
    DF_X32_TYPELESS_G8X24_UINT = _AUTO
    DF_R10G10B10A2_TYPELESS = _AUTO
    DF_R10G10B10A2_UNORM = _AUTO
    DF_R10G10B10A2_UINT = _AUTO
    DF_R11G11B10_FLOAT = _AUTO
    DF_R8G8B8A8_TYPELESS = _AUTO
    DF_R8G8B8A8_UNORM = _AUTO
    DF_R8G8B8A8_UNORM_SRGB = _AUTO
    DF_R8G8B8A8_UINT = _AUTO
    DF_R8G8B8A8_SNORM = _AUTO
    DF_R8G8B8A8_SINT = _AUTO
    DF_R16G16_TYPELESS = _AUTO
    DF_R16G16_FLOAT = _AUTO
    DF_R16G16_UNORM = _AUTO
    DF_R16G16_UINT = _AUTO
    DF_R16G16_SNORM = _AUTO
    DF_R16G16_SINT = _AUTO
    DF_R32_TYPELESS = _AUTO
    DF_D32_FLOAT = _AUTO
    DF_R32_FLOAT = _AUTO
    DF_R32_UINT = _AUTO
    DF_R32_SINT = _AUTO
    DF_R24G8_TYPELESS = _AUTO
    DF_D24_UNORM_S8_UINT = _AUTO
    DF_R24_UNORM_X8_TYPELESS = _AUTO
    DF_X24_TYPELESS_G8_UINT = _AUTO
    DF_R8G8_TYPELESS = _AUTO
    DF_R8G8_UNORM = _AUTO
    DF_R8G8_UINT = _AUTO
    DF_R8G8_SNORM = _AUTO
    DF_R8G8_SINT = _AUTO
    DF_R16_TYPELESS = _AUTO
    DF_R16_FLOAT = _AUTO
    DF_D16_UNORM = _AUTO
    DF_R16_UNORM = _AUTO
    DF_R16_UINT = _AUTO
    DF_R16_SNORM = _AUTO
    DF_R16_SINT = _AUTO
    DF_R8_TYPELESS = _AUTO
    DF_R8_UNORM = _AUTO
    DF_R8_UINT = _AUTO
    DF_R8_SNORM = _AUTO
    DF_R8_SINT = _AUTO
    DF_A8_UNORM = _AUTO
    DF_R1_UNORM = _AUTO
    DF_R9G9B9E5_SHAREDEXP = _AUTO
    DF_R8G8_B8G8_UNORM = _AUTO
    DF_G8R8_G8B8_UNORM = _AUTO
    DF_BC1_TYPELESS = _AUTO
    DF_BC1_UNORM = _AUTO
    DF_BC1_UNORM_SRGB = _AUTO
    DF_BC2_TYPELESS = _AUTO
    DF_BC2_UNORM = _AUTO
    DF_BC2_UNORM_SRGB = _AUTO
    DF_BC3_TYPELESS = _AUTO
    DF_BC3_UNORM = _AUTO
    DF_BC3_UNORM_SRGB = _AUTO
    DF_BC4_TYPELESS = _AUTO
    DF_BC4_UNORM = _AUTO
    DF_BC4_SNORM = _AUTO
    DF_BC5_TYPELESS = _AUTO
    DF_BC5_UNORM = _AUTO
    DF_BC5_SNORM = _AUTO
    DF_B5G6R5_UNORM = _AUTO
    DF_B5G5R5A1_UNORM = _AUTO
    DF_B8G8R8A8_UNORM = _AUTO
    DF_B8G8R8X8_UNORM = _AUTO
    DF_R10G10B10_XR_BIAS_A2_UNORM = _AUTO
    DF_B8G8R8A8_TYPELESS = _AUTO
    DF_B8G8R8A8_UNORM_SRGB = _AUTO
    DF_B8G8R8X8_TYPELESS = _AUTO
    DF_B8G8R8X8_UNORM_SRGB = _AUTO
    DF_BC6H_TYPELESS = _AUTO
    DF_BC6H_UF16 = _AUTO
    DF_BC6H_SF16 = _AUTO
    DF_BC7_TYPELESS = _AUTO
    DF_BC7_UNORM = _AUTO
    DF_BC7_UNORM_SRGB = _AUTO
    DF_AYUV = _AUTO
    DF_Y410 = _AUTO
    DF_Y416 = _AUTO
    DF_NV12 = _AUTO
    DF_P010 = _AUTO
    DF_P016 = _AUTO
    DF_420_OPAQUE = _AUTO
    DF_YUY2 = _AUTO
    DF_Y210 = _AUTO
    DF_Y216 = _AUTO
    DF_NV11 = _AUTO
    DF_AI44 = _AUTO
    DF_IA44 = _AUTO
    DF_P8 = _AUTO
    DF_A8P8 = _AUTO
    DF_B4G4R4A4_UNORM = _AUTO
    DF_P208 = 130
    DF_V208 = _AUTO
    DF_V408 = _AUTO
    DF_SAMPLER_FEEDBACK_MIN_MIP_OPAQUE = 189
    DF_SAMPLER_FEEDBACK_MIP_REGION_USED_OPAQUE = _AUTO
    DF_FORCE_UINT = 0xffffffff


# noinspection PyPep8Naming
class DXGI_MODE_SCANLINE_ORDER(_Enum):
    UNSPECIFIED = _AUTO
    PROGRESSIVE = _AUTO
    UPPER_FIELD_FIRST = _AUTO
    LOWER_FIELD_FIRST = _AUTO


# noinspection PyPep8Naming
class DXGI_MODE_SCALING(_Enum):
    UNSPECIFIED = _AUTO
    CENTERED = _AUTO
    STRETCHED = _AUTO


# noinspection PyPep8Naming
class DXGI_MODE_ROTATION(_Enum):
    UNSPECIFIED = _AUTO
    IDENTITY = _AUTO
    ROTATE90 = _AUTO
    ROTATE180 = _AUTO
    ROTATE270 = _AUTO


# noinspection PyPep8Naming
class DXGI_COLOR_SPACE_TYPE(_Enum):
    RGB_FULL_G22_NONE_P709 = _AUTO
    RGB_FULL_G10_NONE_P709 = _AUTO
    RGB_STUDIO_G22_NONE_P709 = _AUTO
    RGB_STUDIO_G22_NONE_P2020 = _AUTO
    RESERVED = _AUTO
    YCBCR_FULL_G22_NONE_P709_X601 = _AUTO
    YCBCR_STUDIO_G22_LEFT_P601 = _AUTO
    YCBCR_FULL_G22_LEFT_P601 = _AUTO
    YCBCR_STUDIO_G22_LEFT_P709 = _AUTO
    YCBCR_FULL_G22_LEFT_P709 = _AUTO
    YCBCR_STUDIO_G22_LEFT_P2020 = _AUTO
    YCBCR_FULL_G22_LEFT_P2020 = _AUTO
    RGB_FULL_G2084_NONE_P2020 = _AUTO
    YCBCR_STUDIO_G2084_LEFT_P2020 = _AUTO
    RGB_STUDIO_G2084_NONE_P2020 = _AUTO
    YCBCR_STUDIO_G22_TOPLEFT_P2020 = _AUTO
    YCBCR_STUDIO_G2084_TOPLEFT_P2020 = _AUTO
    RGB_FULL_G22_NONE_P2020 = _AUTO
    YCBCR_STUDIO_GHLG_TOPLEFT_P2020 = _AUTO
    YCBCR_FULL_GHLG_TOPLEFT_P2020 = _AUTO
    RGB_STUDIO_G24_NONE_P709 = _AUTO
    RGB_STUDIO_G24_NONE_P2020 = _AUTO
    YCBCR_STUDIO_G24_LEFT_P709 = _AUTO
    YCBCR_STUDIO_G24_LEFT_P2020 = _AUTO
    YCBCR_STUDIO_G24_TOPLEFT_P2020 = _AUTO
    CUSTOM = 0xFFFFFFFF


# noinspection PyPep8Naming
class DWRITE_MEASURING_MODE(_Enum):
    NATURAL = _AUTO
    GDI_CLASSIC = _AUTO
    GDI_NATURAL = _AUTO


# noinspection PyPep8Naming
class DWRITE_GLYPH_IMAGE_FORMATS(_Enum):
    NONE = 0x00000000
    TRUETYPE = 0x00000001
    CFF = 0x00000002
    COLR = 0x00000004
    SVG = 0x00000008
    PNG = 0x00000010
    JPEG = 0x00000020
    TIFF = 0x00000040
    PREMULTIPLIED_B8G8R8A8 = 0x00000080


# noinspection PyPep8Naming
class D2D1_ALPHA_MODE(_Enum):
    UNKNOWN = _AUTO
    PREMULTIPLIED = _AUTO
    STRAIGHT = _AUTO
    IGNORE = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_INTERPOLATION_MODE_DEFINITION(_Enum):
    NEAREST_NEIGHBOR = _AUTO
    LINEAR = _AUTO
    CUBIC = _AUTO
    MULTI_SAMPLE_LINEAR = _AUTO
    ANISOTROPIC = _AUTO
    HIGH_QUALITY_CUBIC = _AUTO
    FANT = _AUTO
    MIPMAP_LINEAR = _AUTO


# noinspection PyPep8Naming
class D2D1_GAMMA(_Enum):
    DG_2_2 = _AUTO
    DG_1_0 = _AUTO
    DG_FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_OPACITY_MASK_CONTENT(_Enum):
    GRAPHICS = _AUTO
    TEXT_NATURAL = _AUTO
    TEXT_GDI_COMPATIBLE = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_EXTEND_MODE(_Enum):
    CLAMP = _AUTO
    WRAP = _AUTO
    MIRROR = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_ANTIALIAS_MODE(_Enum):
    PER_PRIMITIVE = _AUTO
    ALIASED = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_TEXT_ANTIALIAS_MODE(_Enum):
    DEFAULT = _AUTO
    CLEARTYPE = _AUTO
    GRAYSCALE = _AUTO
    ALIASED = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_BITMAP_INTERPOLATION_MODE(_Enum):
    NEAREST_NEIGHBOR = D2D1_INTERPOLATION_MODE_DEFINITION.NEAREST_NEIGHBOR
    LINEAR = D2D1_INTERPOLATION_MODE_DEFINITION.LINEAR
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_DRAW_TEXT_OPTIONS(_Enum):
    NO_SNAP = 0x00000001
    CLIP = 0x00000002
    ENABLE_COLOR_FONT = 0x00000004
    DISABLE_COLOR_BITMAP_SNAPPIING = 0x00000008
    NONE = 0x00000000
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_DC_INITIALIZE_MODE(_Enum):
    COPY = _AUTO
    CLEAR = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_DEBUG_LEVEL(_Enum):
    NONE = _AUTO
    ERROR = _AUTO
    WARNING = _AUTO
    INFORMATION = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_FACTORY_TYPE(_Enum):
    SINGLE_THREADED = _AUTO
    MULTI_THREADED = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D3D_DRIVER_TYPE(_Enum):
    UNKNOWN = _AUTO
    HARDWARE = _AUTO
    REFERENCE = _AUTO
    NULL = _AUTO
    SOFTWARE = _AUTO
    WARP = _AUTO


# noinspection PyPep8Naming
class D3D_FEATURE_LEVEL(_Enum):
    DFL_1_0_CORE = 0x1000
    DFL_9_1 = 0x9100
    DFL_9_2 = 0x9200
    DFL_9_3 = 0x9300
    DEF_10_0 = 0xa000
    DEF_10_1 = 0xa100
    DEF_11_0 = 0xb000
    DEF_11_1 = 0xb100
    DEF_12_0 = 0xc000
    DEF_12_1 = 0xc100
    DEF_12_2 = 0xc200


# noinspection PyPep8Naming
class D2D1_WINDOW_STATE(_Enum):
    NONE = 0x0000000
    OCCLUDED = 0x0000001
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_RENDER_TARGET_TYPE(_Enum):
    DEFAULT = _AUTO
    SOFTWARE = _AUTO
    HARDWARE = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_FEATURE_LEVEL(_Enum):
    DEFL_DEFAULT = _AUTO
    DFL_9 = D3D_FEATURE_LEVEL.DFL_9_1
    DFL_10 = D3D_FEATURE_LEVEL.DEF_10_0
    DFL_FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_RENDER_TARGET_USAGE(_Enum):
    NONE = 0x00000000
    FORCE_BITMAP_REMOTING = 0x00000001
    GDI_COMPATIBLE = 0x00000002
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_PRESENT_OPTIONS(_Enum):
    NONE = 0x00000000
    RETAIN_CONTENTS = 0x00000001
    IMMEDIATELY = 0x00000002
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_PROPERTY_TYPE(_Enum):
    UNKNOWN = _AUTO
    STRING = _AUTO
    BOOL = _AUTO
    UINT32 = _AUTO
    INT32 = _AUTO
    FLOAT = _AUTO
    VECTOR2 = _AUTO
    VECTOR3 = _AUTO
    VECTOR4 = _AUTO
    BLOB = _AUTO
    IUNKNOWN = _AUTO
    ENUM = _AUTO
    ARRAY = _AUTO
    CLSID = _AUTO
    MATRIX_3X2 = _AUTO
    MATRIX_4X3 = _AUTO
    MATRIX_4X4 = _AUTO
    MATRIX_5X4 = _AUTO
    COLOR_CONTEXT = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_PROPERTY(_Enum):
    CLSID = 0x80000000
    DISPLAYNAME = 0x80000001
    AUTHOR = 0x80000002
    CATEGORY = 0x80000003
    DESCRIPTION = 0x80000004
    INPUTS = 0x80000005
    CACHED = 0x80000006
    PRECISION = 0x80000007
    MIN_INPUTS = 0x80000008
    MAX_INPUTS = 0x80000009
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SUBPROPERTY(_Enum):
    DISPLAYNAME = 0x80000000
    ISREADONLY = 0x80000001
    MIN = 0x80000002
    MAX = 0x80000003
    DEFAULT = 0x80000004
    FIELDS = 0x80000005
    INDEX = 0x80000006
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_BITMAP_OPTIONS(_Enum):
    NONE = 0x00000000
    TARGET = 0x00000001
    CANNOT_DRAW = 0x00000002
    CPU_READ = 0x00000004
    GDI_COMPATIBLE = 0x00000008
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_COMPOSITE_MODE(_Enum):
    SOURCE_OVER = _AUTO
    DESTINATION_OVER = _AUTO
    SOURCE_IN = _AUTO
    DESTINATION_IN = _AUTO
    SOURCE_OUT = _AUTO
    DESTINATION_OUT = _AUTO
    SOURCE_ATOP = _AUTO
    DESTINATION_ATOP = _AUTO
    XOR = _AUTO
    PLUS = _AUTO
    SOURCE_COPY = _AUTO
    BOUNDED_SOURCE_COPY = _AUTO
    MASK_INVERT = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_BUFFER_PRECISION(_Enum):
    DBP_UNKNOWN = _AUTO
    DBP_8BPC_UNORM = _AUTO
    DBP_8BPC_UNORM_SRGB = _AUTO
    DBP_16BPC_UNORM = _AUTO
    DBP_16BPC_FLOAT = _AUTO
    DBP_32BPC_FLOAT = _AUTO
    DBP_FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_MAP_OPTIONS(_Enum):
    NONE = _AUTO
    READ = _AUTO
    WRITE = _AUTO
    DISCARD = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_INTERPOLATION_MODE(_Enum):
    NEAREST_NEIGHBOR = D2D1_INTERPOLATION_MODE_DEFINITION.NEAREST_NEIGHBOR
    LINEAR = D2D1_INTERPOLATION_MODE_DEFINITION.LINEAR
    CUBIC = D2D1_INTERPOLATION_MODE_DEFINITION.CUBIC
    MULTI_SAMPLE_LINEAR = D2D1_INTERPOLATION_MODE_DEFINITION.MULTI_SAMPLE_LINEAR
    ANISOTROPIC = D2D1_INTERPOLATION_MODE_DEFINITION.ANISOTROPIC
    HIGH_QUALITY_CUBIC = D2D1_INTERPOLATION_MODE_DEFINITION.HIGH_QUALITY_CUBIC
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_UNIT_MODE(_Enum):
    DIPS = _AUTO
    PIXELS = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_COLOR_SPACE(_Enum):
    CUSTOM = _AUTO
    SRGB = _AUTO
    SCRGB = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_DEVICE_CONTEXT_OPTIONS(_Enum):
    NONE = _AUTO
    ENNABLE_MULTITHREADED_OPTIMIZATIONS = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_STROKE_TRANSFORM_TYPE(_Enum):
    NORMAL = _AUTO
    TYPE_FIXED = _AUTO
    HAIRLINE = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_PRIMITIVE_BLEND(_Enum):
    SOURCE_OVER = _AUTO
    COPY = _AUTO
    MIN = _AUTO
    ADD = _AUTO
    MAX = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_THREADING_MODE(_Enum):
    SINGLE_THREADED = D2D1_FACTORY_TYPE.SINGLE_THREADED
    MULTI_THREADED = D2D1_FACTORY_TYPE.MULTI_THREADED
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_COLOR_INTERPOLATION_MODE(_Enum):
    STRAIGHT = _AUTO
    PREMULTIPLIED = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_ARC_SIZE(_Enum):
    SMALL = _AUTO
    LARGE = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_CAP_STYLE(_Enum):
    FLAT = _AUTO
    SQUARE = _AUTO
    ROUND = _AUTO
    TRIANGLE = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_DASH_STYLE(_Enum):
    SOLID = _AUTO
    DASH = _AUTO
    DOT = _AUTO
    DASH_DOT = _AUTO
    DASH_DOT_DOT = _AUTO
    CUSTOM = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_LINE_JOIN(_Enum):
    MITER = _AUTO
    BEVEL = _AUTO
    ROUND = _AUTO
    MITER_OR_BEVEL = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_COMBINE_MODE(_Enum):
    UNION = _AUTO
    INTERSECT = _AUTO
    XOR = _AUTO
    EXCLUDE = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_GEOMETRY_RELATION(_Enum):
    UNKNOWN = _AUTO
    DISJOINT = _AUTO
    IS_CONTAINED = _AUTO
    CONTAINS = _AUTO
    OVERLAP = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_GEOMETRY_SIMPLIFICATION_OPTION(_Enum):
    CUBICS_AND_LINES = _AUTO
    LINES = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_FIGURE_BEGIN(_Enum):
    FILLED = _AUTO
    HOLLOW = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_FIGURE_END(_Enum):
    OPEN = _AUTO
    CLOSED = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D3D11_CREATE_DEVICE_FLAG(_Enum):
    SINGLETHREADED = 0x1
    DEBUG = 0x2
    SWITCH_TO_REF = 0x4
    PREVENT_INTERNAL_THREADING_OPTIMIZATIONS = 0x8
    BGRA_SUPPORT = 0x20
    DEBUGGABLE = 0x40
    PREVENT_ALTERING_LAYER_SETTINGS_FROM_REGISTRY = 0x80
    DISABLE_GPU_TIMEOUT = 0x100
    VIDEO_SUPPORT = 0x800


# noinspection PyPep8Naming
class D2D1_SVG_PAINT_TYPE(_Enum):
    NONE = _AUTO
    COLOR = _AUTO
    CURRENT_COLOR = _AUTO
    URI = _AUTO
    URI_NONE = _AUTO
    URI_COLOR = _AUTO
    URI_CURRENT_COLOR = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_LENGTH_UNITS(_Enum):
    NUMBER = _AUTO
    PERCENTAGE = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_DISPLAY(_Enum):
    INLINE = _AUTO
    NONE = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_VISIBILITY(_Enum):
    VISIBLE = _AUTO
    HIDDEN = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_OVERFLOW(_Enum):
    VISIBLE = _AUTO
    HIDDEN = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_LINE_CAP(_Enum):
    BUTT = D2D1_CAP_STYLE.FLAT
    SQUARE = D2D1_CAP_STYLE.SQUARE
    ROUND = D2D1_CAP_STYLE.ROUND
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_LINE_JOIN(_Enum):
    BEVEL = D2D1_LINE_JOIN.BEVEL
    MITER = D2D1_LINE_JOIN.MITER_OR_BEVEL
    ROUND = D2D1_LINE_JOIN.ROUND
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_ASPECT_ALIGN(_Enum):
    NONE = _AUTO
    X_MIN_Y_MIN = _AUTO
    X_MID_Y_MIN = _AUTO
    X_MAX_Y_MIN = _AUTO
    X_MIN_Y_MID = _AUTO
    X_MID_Y_MID = _AUTO
    X_MAX_Y_MID = _AUTO
    X_MIN_Y_MAX = _AUTO
    X_MID_Y_MAX = _AUTO
    X_MAX_Y_MAX = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_ASPECT_SCALING(_Enum):
    MEET = _AUTO
    SLICE = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_PATH_COMMAND(_Enum):
    COLSE_PATH = _AUTO
    MOVE_ABSOLUTE = _AUTO
    MOVE_RELATIVE = _AUTO
    LINE_ABSOLUTE = _AUTO
    LINE_RELATIVE = _AUTO
    CUBIC_ABSOLUTE = _AUTO
    CUBIC_RELATIVE = _AUTO
    QUADRATIC_ABSOLUTE = _AUTO
    QUADRATIC_RELATIVE = _AUTO
    ARC_ABSOLUTE = _AUTO
    ARC_RELATIVE = _AUTO
    HORIZONTAL_ABSOLUTE = _AUTO
    HORIZONTAL_RELATIVE = _AUTO
    VERTICAL_ABSOLUTE = _AUTO
    VERTICAL_RELATIVE = _AUTO
    CUBIC_SMOOTH_ABSOLUTE = _AUTO
    CUBIC_SMOOTH_RELATIVE = _AUTO
    QUADRATIC_SMOOTH_ABSOLUTE = _AUTO
    QUADRATIC_SMOOTH_RELATIVE = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_UNIT_TYPE(_Enum):
    USER_SPACE_ON_USE = _AUTO
    BOUNDING_BOX = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_ATTRIBUTE_STRING_TYPE(_Enum):
    SVG = _AUTO
    ID = _AUTO
    FORCE_DWORD = 0xffffffff


# noinspection PyPep8Naming
class D2D1_SVG_ATTRIBUTE_POD_TYPE(_Enum):
    FLOAT = _AUTO
    COLOR = _AUTO
    FILL_MODE = _AUTO
    DISPLAY = _AUTO
    OVERFLOW = _AUTO
    LINE_CAP = _AUTO
    LINE_JOIN = _AUTO
    VISIBILITY = _AUTO
    MATRIX = _AUTO
    UNIT_TYPE = _AUTO
    EXTEND_MODE = _AUTO
    PRESERVE_ASPECT_RATIO = _AUTO
    VIEWBOX = _AUTO
    LENGTH = _AUTO
    FORCE_DWORD = 0xffffffff


GpStatus = Status
GpFillMode = FillMode
GpWrapMode = WrapMode
GpUnit = Unit
GpCoordinateSpace = CoordinateSpace
GpHatchStyle = HatchStyle
GpDashStyle = DashStyle
GpLineCap = LineCap
GpDashCap = DashCap
GpPenAlignment = PenAlignment
GpLineJoin = LineJoin
GpPenType = PenType
GpBrushType = BrushType
GpMatrixOrder = MatrixOrder
GpFlushIntention = FlushIntention


class Windows:
    class AI:
        class MachineLearning:
            class LearningModelDeviceKind(_Enum):
                Default = 0
                Cpu = 1
                DirectX = 2
                DirectXHighPerformance = 3
                DirectXMinPower = 4

            class LearningModelFeatureKind(_Enum):
                Tensor = 0
                Sequence = 1
                Map = 2
                Image = 3

            class LearningModelPixelRange(_Enum):
                ZeroTo255 = 0
                ZeroToOne = 1
                MinusOneToOne = 2

            class TensorKind(_Enum):
                Undefined = 0
                Float = 1
                UInt8 = 2
                Int8 = 3
                UInt16 = 4
                Int16 = 5
                Int32 = 6
                Int64 = 7
                String = 8
                Boolean = 9
                Float16 = 10
                Double = 11
                UInt32 = 12
                UInt64 = 13
                Complex64 = 14
                Complex128 = 15

            class Preview:
                class FeatureElementKindPreview(_Enum):
                    Undefined = 0
                    Float = 1
                    UInt8 = 2
                    Int8 = 3
                    UInt16 = 4
                    Int16 = 5
                    Int32 = 6
                    Int64 = 7
                    String = 8
                    Boolean = 9
                    Float16 = 10
                    Double = 11
                    UInt32 = 12
                    UInt64 = 13
                    Complex64 = 14
                    Complex128 = 15

                class LearningModelDeviceKindPreview(_Enum):
                    LearningDeviceAny = 0
                    LearningDeviceCpu = 1
                    LearningDeviceGpu = 2
                    LearningDeviceNpu = 3
                    LearningDeviceDsp = 4
                    LearningDeviceFpga = 5

                class LearningModelFeatureKindPreview(_Enum):
                    Undefined = 0
                    Tensor = 1
                    Sequence = 2
                    Map = 3
                    Image = 4

    class ApplicationModel:
        class AddResourcePackageOptions(_Enum):
            None_ = 0x0
            ForceTargetAppShutdown = 0x1
            ApplyUpdateIfAvailable = 0x2

        class AppExecutionContext(_Enum):
            Unknown = 0
            Host = 1
            Guest = 2

        class AppInstallerPolicySource(_Enum):
            Default = 0
            System = 1

        class FullTrustLaunchResult(_Enum):
            Success = 0
            AccessDenied = 1
            FileNotFound = 2
            Unknown = 3

        class LimitedAccessFeatureStatus(_Enum):
            Unavailable = 0
            Available = 1
            AvailableWithoutToken = 2
            Unknown = 3

        class PackageContentGroupState(_Enum):
            NotStaged = 0
            Queued = 1
            Staging = 2
            Staged = 3

        class PackageRelationship(_Enum):
            Dependencies = 0
            Dependents = 1
            All = 2

        class PackageSignatureKind(_Enum):
            None_ = 0
            Developer = 1
            Enterprise = 2
            Store = 3
            System = 4

        class PackageUpdateAvailability(_Enum):
            Unknown = 0
            NoUpdates = 1
            Available = 2
            Required = 3
            Error = 4

        class StartupTaskState(_Enum):
            Disabled = 0
            DisabledByUser = 1
            Enabled = 2
            DisabledByPolicy = 3
            EnabledByPolicy = 4

        class Activation:
            class ActivationKind(_Enum):
                Launch = 0
                Search = 1
                ShareTarget = 2
                File = 3
                Protocol = 4
                FileOpenPicker = 5
                FileSavePicker = 6
                CachedFileUpdater = 7
                ContactPicker = 8
                Device = 9
                PrintTaskSettings = 10
                CameraSettings = 11
                RestrictedLaunch = 12
                AppointmentsProvider = 13
                Contact = 14
                LockScreenCall = 15
                VoiceCommand = 16
                LockScreen = 17
                PickerReturned = 1000
                WalletAction = 1001
                PickFileContinuation = 1002
                PickSaveFileContinuation = 1003
                PickFolderContinuation = 1004
                WebAuthenticationBrokerContinuation = 1005
                WebAccountProvider = 1006
                ComponentUI = 1007
                ProtocolForResults = 1009
                ToastNotification = 1010
                Print3DWorkflow = 1011
                DialReceiver = 1012
                DevicePairing = 1013
                UserDataAccountsProvider = 1014
                FilePickerExperience = 1015
                LockScreenComponent = 1016
                ContactPanel = 1017
                PrintWorkflowForegroundTask = 1018
                GameUIProvider = 1019
                StartupTask = 1020
                CommandLineLaunch = 1021
                BarcodeScannerProvider = 1022
                PrintSupportJobUI = 1023
                PrintSupportSettingsUI = 1024
                PhoneCallActivation = 1025
                VpnForeground = 1026

            class ApplicationExecutionState(_Enum):
                NotRunning = 0
                Running = 1
                Suspended = 2
                Terminated = 3
                ClosedByUser = 4

        class Appointments:
            class AppointmentBusyStatus(_Enum):
                Busy = 0
                Tentative = 1
                Free = 2
                OutOfOffice = 3
                WorkingElsewhere = 4

            class AppointmentCalendarOtherAppReadAccess(_Enum):
                SystemOnly = 0
                Limited = 1
                Full = 2
                None_ = 3

            class AppointmentCalendarOtherAppWriteAccess(_Enum):
                None_ = 0
                SystemOnly = 1
                Limited = 2

            class AppointmentCalendarSyncStatus(_Enum):
                Idle = 0
                Syncing = 1
                UpToDate = 2
                AuthenticationError = 3
                PolicyError = 4
                UnknownError = 5
                ManualAccountRemovalRequired = 6

            class AppointmentConflictType(_Enum):
                None_ = 0
                Adjacent = 1
                Overlap = 2

            class AppointmentDaysOfWeek(_Enum):
                None_ = 0x0
                Sunday = 0x1
                Monday = 0x2
                Tuesday = 0x4
                Wednesday = 0x8
                Thursday = 0x10
                Friday = 0x20
                Saturday = 0x40

            class AppointmentDetailsKind(_Enum):
                PlainText = 0
                Html = 1

            class AppointmentParticipantResponse(_Enum):
                None_ = 0
                Tentative = 1
                Accepted = 2
                Declined = 3
                Unknown = 4

            class AppointmentParticipantRole(_Enum):
                RequiredAttendee = 0
                OptionalAttendee = 1
                Resource = 2

            class AppointmentRecurrenceUnit(_Enum):
                Daily = 0
                Weekly = 1
                Monthly = 2
                MonthlyOnDay = 3
                Yearly = 4
                YearlyOnDay = 5

            class AppointmentSensitivity(_Enum):
                Public = 0
                Private = 1

            class AppointmentStoreAccessType(_Enum):
                AppCalendarsReadWrite = 0
                AllCalendarsReadOnly = 1
                AllCalendarsReadWrite = 2

            class AppointmentStoreChangeType(_Enum):
                AppointmentCreated = 0
                AppointmentModified = 1
                AppointmentDeleted = 2
                ChangeTrackingLost = 3
                CalendarCreated = 4
                CalendarModified = 5
                CalendarDeleted = 6

            class AppointmentSummaryCardView(_Enum):
                System = 0
                App = 1

            class AppointmentWeekOfMonth(_Enum):
                First = 0
                Second = 1
                Third = 2
                Fourth = 3
                Last = 4

            class FindAppointmentCalendarsOptions(_Enum):
                None_ = 0x0
                IncludeHidden = 0x1

            class RecurrenceType(_Enum):
                Master = 0
                Instance = 1
                ExceptionInstance = 2

        class AppService:
            class AppServiceClosedStatus(_Enum):
                Completed = 0
                Canceled = 1
                ResourceLimitsExceeded = 2
                Unknown = 3

            class AppServiceConnectionStatus(_Enum):
                Success = 0
                AppNotInstalled = 1
                AppUnavailable = 2
                AppServiceUnavailable = 3
                Unknown = 4
                RemoteSystemUnavailable = 5
                RemoteSystemNotSupportedByApp = 6
                NotAuthorized = 7
                AuthenticationError = 8
                NetworkNotAvailable = 9
                DisabledByPolicy = 10
                WebServiceUnavailable = 11

            class AppServiceResponseStatus(_Enum):
                Success = 0
                Failure = 1
                ResourceLimitsExceeded = 2
                Unknown = 3
                RemoteSystemUnavailable = 4
                MessageSizeTooLarge = 5
                AppUnavailable = 6
                AuthenticationError = 7
                NetworkNotAvailable = 8
                DisabledByPolicy = 9
                WebServiceUnavailable = 10

            class StatelessAppServiceResponseStatus(_Enum):
                Success = 0
                AppNotInstalled = 1
                AppUnavailable = 2
                AppServiceUnavailable = 3
                RemoteSystemUnavailable = 4
                RemoteSystemNotSupportedByApp = 5
                NotAuthorized = 6
                ResourceLimitsExceeded = 7
                MessageSizeTooLarge = 8
                Failure = 9
                Unknown = 10
                AuthenticationError = 11
                NetworkNotAvailable = 12
                DisabledByPolicy = 13
                WebServiceUnavailable = 14

        class Background:
            class AlarmAccessStatus(_Enum):
                Unspecified = 0
                AllowedWithWakeupCapability = 1
                AllowedWithoutWakeupCapability = 2
                Denied = 3

            class ApplicationTriggerResult(_Enum):
                Allowed = 0
                CurrentlyRunning = 1
                DisabledByPolicy = 2
                UnknownError = 3

            class BackgroundAccessRequestKind(_Enum):
                AlwaysAllowed = 0
                AllowedSubjectToSystemPolicy = 1

            class BackgroundAccessStatus(_Enum):
                Unspecified = 0
                AllowedWithAlwaysOnRealTimeConnectivity = 1
                AllowedMayUseActiveRealTimeConnectivity = 2
                Denied = 3
                AlwaysAllowed = 4
                AllowedSubjectToSystemPolicy = 5
                DeniedBySystemPolicy = 6
                DeniedByUser = 7

            class BackgroundTaskCancellationReason(_Enum):
                Abort = 0
                Terminating = 1
                LoggingOff = 2
                ServicingUpdate = 3
                IdleTask = 4
                Uninstall = 5
                ConditionLoss = 6
                SystemPolicy = 7
                QuietHoursEntered = 8
                ExecutionTimeExceeded = 9
                ResourceRevocation = 10
                EnergySaver = 11

            class BackgroundTaskThrottleCounter(_Enum):
                All = 0
                Cpu = 1
                Network = 2

            class BackgroundWorkCostValue(_Enum):
                Low = 0
                Medium = 1
                High = 2

            class CustomSystemEventTriggerRecurrence(_Enum):
                Once = 0
                Always = 1

            class DeviceTriggerResult(_Enum):
                Allowed = 0
                DeniedByUser = 1
                DeniedBySystem = 2
                LowBattery = 3

            class LocationTriggerType(_Enum):
                Geofence = 0

            class MediaProcessingTriggerResult(_Enum):
                Allowed = 0
                CurrentlyRunning = 1
                DisabledByPolicy = 2
                UnknownError = 3

            class SystemConditionType(_Enum):
                Invalid = 0
                UserPresent = 1
                UserNotPresent = 2
                InternetAvailable = 3
                InternetNotAvailable = 4
                SessionConnected = 5
                SessionDisconnected = 6
                FreeNetworkAvailable = 7
                BackgroundWorkCostNotHigh = 8

            class SystemTriggerType(_Enum):
                Invalid = 0
                SmsReceived = 1
                UserPresent = 2
                UserAway = 3
                NetworkStateChange = 4
                ControlChannelReset = 5
                InternetAvailable = 6
                SessionConnected = 7
                ServicingComplete = 8
                LockScreenApplicationAdded = 9
                LockScreenApplicationRemoved = 10
                TimeZoneChange = 11
                OnlineIdConnectedStateChange = 12
                BackgroundWorkCostChange = 13
                PowerStateChange = 14
                DefaultSignInAccountChange = 15

        class Calls:
            class CellularDtmfMode(_Enum):
                Continuous = 0
                Burst = 1

            class DtmfKey(_Enum):
                D0 = 0
                D1 = 1
                D2 = 2
                D3 = 3
                D4 = 4
                D5 = 5
                D6 = 6
                D7 = 7
                D8 = 8
                D9 = 9
                Star = 10
                Pound = 11

            class DtmfToneAudioPlayback(_Enum):
                Play = 0
                DoNotPlay = 1

            class PhoneAudioRoutingEndpoint(_Enum):
                Default = 0
                Bluetooth = 1
                Speakerphone = 2

            class PhoneCallAudioDevice(_Enum):
                Unknown = 0
                LocalDevice = 1
                RemoteDevice = 2

            class PhoneCallDirection(_Enum):
                Unknown = 0
                Incoming = 1
                Outgoing = 2

            class PhoneCallHistoryEntryMedia(_Enum):
                Audio = 0
                Video = 1

            class PhoneCallHistoryEntryOtherAppReadAccess(_Enum):
                Full = 0
                SystemOnly = 1

            class PhoneCallHistoryEntryQueryDesiredMedia(_Enum):
                None_ = 0x0
                Audio = 0x1
                Video = 0x2

            class PhoneCallHistoryEntryRawAddressKind(_Enum):
                PhoneNumber = 0
                Custom = 1

            class PhoneCallHistorySourceIdKind(_Enum):
                CellularPhoneLineId = 0
                PackageFamilyName = 1

            class PhoneCallHistoryStoreAccessType(_Enum):
                AppEntriesReadWrite = 0
                AllEntriesLimitedReadWrite = 1
                AllEntriesReadWrite = 2

            class PhoneCallMedia(_Enum):
                Audio = 0
                AudioAndVideo = 1
                AudioAndRealTimeText = 2

            class PhoneCallOperationStatus(_Enum):
                Succeeded = 0
                OtherFailure = 1
                TimedOut = 2
                ConnectionLost = 3
                InvalidCallState = 4

            class PhoneCallStatus(_Enum):
                Lost = 0
                Incoming = 1
                Dialing = 2
                Talking = 3
                Held = 4
                Ended = 5

            class PhoneLineNetworkOperatorDisplayTextLocation(_Enum):
                Default = 0
                Tile = 1
                Dialer = 2
                InCallUI = 3

            class PhoneLineOperationStatus(_Enum):
                Succeeded = 0
                OtherFailure = 1
                TimedOut = 2
                ConnectionLost = 3
                InvalidCallState = 4

            class PhoneLineTransport(_Enum):
                Cellular = 0
                VoipApp = 1
                Bluetooth = 2

            class PhoneLineWatcherStatus(_Enum):
                Created = 0
                Started = 1
                EnumerationCompleted = 2
                Stopped = 3

            class PhoneNetworkState(_Enum):
                Unknown = 0
                NoSignal = 1
                Deregistered = 2
                Denied = 3
                Searching = 4
                Home = 5
                RoamingInternational = 6
                RoamingDomestic = 7

            class PhoneSimState(_Enum):
                Unknown = 0
                PinNotRequired = 1
                PinUnlocked = 2
                PinLocked = 3
                PukLocked = 4
                NotInserted = 5
                Invalid = 6
                Disabled = 7

            class PhoneVoicemailType(_Enum):
                None_ = 0
                Traditional = 1
                Visual = 2

            class TransportDeviceAudioRoutingStatus(_Enum):
                Unknown = 0
                CanRouteToLocalDevice = 1
                CannotRouteToLocalDevice = 2

            class VoipPhoneCallMedia(_Enum):
                None_ = 0x0
                Audio = 0x1
                Video = 0x2

            class VoipPhoneCallRejectReason(_Enum):
                UserIgnored = 0
                TimedOut = 1
                OtherIncomingCall = 2
                EmergencyCallExists = 3
                InvalidCallState = 4

            class VoipPhoneCallResourceReservationStatus(_Enum):
                Success = 0
                ResourcesNotAvailable = 1

            class VoipPhoneCallState(_Enum):
                Ended = 0
                Held = 1
                Active = 2
                Incoming = 3
                Outgoing = 4

            class Background:
                class PhoneCallBlockedReason(_Enum):
                    InCallBlockingList = 0
                    PrivateNumber = 1
                    UnknownNumber = 2

                class PhoneIncomingCallDismissedReason(_Enum):
                    Unknown = 0
                    CallRejected = 1
                    TextReply = 2
                    ConnectionLost = 3

                class PhoneLineChangeKind(_Enum):
                    Added = 0
                    Removed = 1
                    PropertiesChanged = 2

                class PhoneLineProperties(_Enum):
                    None_ = 0x0
                    BrandingOptions = 0x1
                    CanDial = 0x2
                    CellularDetails = 0x4
                    DisplayColor = 0x8
                    DisplayName = 0x10
                    NetworkName = 0x20
                    NetworkState = 0x40
                    Transport = 0x80
                    Voicemail = 0x100

                class PhoneTriggerType(_Enum):
                    NewVoicemailMessage = 0
                    CallHistoryChanged = 1
                    LineChanged = 2
                    AirplaneModeDisabledForEmergencyCall = 3
                    CallOriginDataRequest = 4
                    CallBlocked = 5
                    IncomingCallDismissed = 6
                    IncomingCallNotification = 7

        class Chat:
            class ChatConversationThreadingKind(_Enum):
                Participants = 0
                ContactId = 1
                ConversationId = 2
                Custom = 3

            class ChatItemKind(_Enum):
                Message = 0
                Conversation = 1

            class ChatMessageChangeType(_Enum):
                MessageCreated = 0
                MessageModified = 1
                MessageDeleted = 2
                ChangeTrackingLost = 3

            class ChatMessageKind(_Enum):
                Standard = 0
                FileTransferRequest = 1
                TransportCustom = 2
                JoinedConversation = 3
                LeftConversation = 4
                OtherParticipantJoinedConversation = 5
                OtherParticipantLeftConversation = 6

            class ChatMessageOperatorKind(_Enum):
                Unspecified = 0
                Sms = 1
                Mms = 2
                Rcs = 3

            class ChatMessageStatus(_Enum):
                Draft = 0
                Sending = 1
                Sent = 2
                SendRetryNeeded = 3
                SendFailed = 4
                Received = 5
                ReceiveDownloadNeeded = 6
                ReceiveDownloadFailed = 7
                ReceiveDownloading = 8
                Deleted = 9
                Declined = 10
                Cancelled = 11
                Recalled = 12
                ReceiveRetryNeeded = 13

            class ChatMessageTransportKind(_Enum):
                Text = 0
                Untriaged = 1
                Blocked = 2
                Custom = 3

            class ChatMessageValidationStatus(_Enum):
                Valid = 0
                NoRecipients = 1
                InvalidData = 2
                MessageTooLarge = 3
                TooManyRecipients = 4
                TransportInactive = 5
                TransportNotFound = 6
                TooManyAttachments = 7
                InvalidRecipients = 8
                InvalidBody = 9
                InvalidOther = 10
                ValidWithLargeMessage = 11
                VoiceRoamingRestriction = 12
                DataRoamingRestriction = 13

            class ChatRestoreHistorySpan(_Enum):
                LastMonth = 0
                LastYear = 1
                AnyTime = 2

            class ChatStoreChangedEventKind(_Enum):
                NotificationsMissed = 0
                StoreModified = 1
                MessageCreated = 2
                MessageModified = 3
                MessageDeleted = 4
                ConversationModified = 5
                ConversationDeleted = 6
                ConversationTransportDeleted = 7

            class ChatTransportErrorCodeCategory(_Enum):
                None_ = 0
                Http = 1
                Network = 2
                MmsServer = 3

            class ChatTransportInterpretedErrorCode(_Enum):
                None_ = 0
                Unknown = 1
                InvalidRecipientAddress = 2
                NetworkConnectivity = 3
                ServiceDenied = 4
                Timeout = 5

            class RcsServiceKind(_Enum):
                Chat = 0
                GroupChat = 1
                FileTransfer = 2
                Capability = 3

        class Contacts:
            class ContactAddressKind(_Enum):
                Home = 0
                Work = 1
                Other = 2

            class ContactAnnotationOperations(_Enum):
                None_ = 0x0
                ContactProfile = 0x1
                Message = 0x2
                AudioCall = 0x4
                VideoCall = 0x8
                SocialFeeds = 0x10
                Share = 0x20

            class ContactAnnotationStoreAccessType(_Enum):
                AppAnnotationsReadWrite = 0
                AllAnnotationsReadWrite = 1

            class ContactBatchStatus(_Enum):
                Success = 0
                ServerSearchSyncManagerError = 1
                ServerSearchUnknownError = 2

            class ContactCardHeaderKind(_Enum):
                Default = 0
                Basic = 1
                Enterprise = 2

            class ContactCardTabKind(_Enum):
                Default = 0
                Email = 1
                Messaging = 2
                Phone = 3
                Video = 4
                OrganizationalHierarchy = 5

            class ContactChangeType(_Enum):
                Created = 0
                Modified = 1
                Deleted = 2
                ChangeTrackingLost = 3

            class ContactDateKind(_Enum):
                Birthday = 0
                Anniversary = 1
                Other = 2

            class ContactEmailKind(_Enum):
                Personal = 0
                Work = 1
                Other = 2

            class ContactFieldCategory(_Enum):
                None_ = 0
                Home = 1
                Work = 2
                Mobile = 3
                Other = 4

            class ContactFieldType(_Enum):
                Email = 0
                PhoneNumber = 1
                Location = 2
                InstantMessage = 3
                Custom = 4
                ConnectedServiceAccount = 5
                ImportantDate = 6
                Address = 7
                SignificantOther = 8
                Notes = 9
                Website = 10
                JobInfo = 11

            class ContactListOtherAppReadAccess(_Enum):
                SystemOnly = 0
                Limited = 1
                Full = 2
                None_ = 3

            class ContactListOtherAppWriteAccess(_Enum):
                None_ = 0
                SystemOnly = 1
                Limited = 2

            class ContactListSyncStatus(_Enum):
                Idle = 0
                Syncing = 1
                UpToDate = 2
                AuthenticationError = 3
                PolicyError = 4
                UnknownError = 5
                ManualAccountRemovalRequired = 6

            class ContactMatchReasonKind(_Enum):
                Name = 0
                EmailAddress = 1
                PhoneNumber = 2
                JobInfo = 3
                YomiName = 4
                Other = 5

            class ContactNameOrder(_Enum):
                FirstNameLastName = 0
                LastNameFirstName = 1

            class ContactPhoneKind(_Enum):
                Home = 0
                Mobile = 1
                Work = 2
                Other = 3
                Pager = 4
                BusinessFax = 5
                HomeFax = 6
                Company = 7
                Assistant = 8
                Radio = 9

            class ContactQueryDesiredFields(_Enum):
                None_ = 0x0
                PhoneNumber = 0x1
                EmailAddress = 0x2
                PostalAddress = 0x4

            class ContactQuerySearchFields(_Enum):
                None_ = 0x0
                Name = 0x1
                Email = 0x2
                Phone = 0x4

            class ContactQuerySearchScope(_Enum):
                Local = 0
                Server = 1

            class ContactRelationship(_Enum):
                Other = 0
                Spouse = 1
                Partner = 2
                Sibling = 3
                Parent = 4
                Child = 5

            class ContactSelectionMode(_Enum):
                Contacts = 0
                Fields = 1

            class ContactStoreAccessType(_Enum):
                AppContactsReadWrite = 0
                AllContactsReadOnly = 1
                AllContactsReadWrite = 2

            class PinnedContactSurface(_Enum):
                StartMenu = 0
                Taskbar = 1

            class Provider:
                class AddContactResult(_Enum):
                    Added = 0
                    AlreadyAdded = 1
                    Unavailable = 2

        class ConversationalAgent:
            class ActivationSignalDetectionConfigurationCreationStatus(_Enum):
                Success = 0
                SignalIdNotAvailable = 1
                ModelIdNotSupported = 2
                InvalidSignalId = 3
                InvalidModelId = 4
                InvalidDisplayName = 5
                ConfigurationAlreadyExists = 6
                CreationNotSupported = 7

            class ActivationSignalDetectionConfigurationRemovalResult(_Enum):
                Success = 0
                NotFound = 1
                CurrentlyEnabled = 2
                RemovalNotSupported = 3

            class ActivationSignalDetectionConfigurationSetModelDataResult(_Enum):
                Success = 0
                EmptyModelData = 1
                UnsupportedFormat = 2
                ConfigurationCurrentlyEnabled = 3
                InvalidData = 4
                SetModelDataNotSupported = 5
                ConfigurationNotFound = 6
                UnknownError = 7

            class ActivationSignalDetectionConfigurationStateChangeResult(_Enum):
                Success = 0
                NoModelData = 1
                ConfigurationNotFound = 2

            class ActivationSignalDetectionTrainingDataFormat(_Enum):
                Voice8kHz8BitMono = 0
                Voice8kHz16BitMono = 1
                Voice16kHz8BitMono = 2
                Voice16kHz16BitMono = 3
                VoiceOEMDefined = 4
                Audio44kHz8BitMono = 5
                Audio44kHz16BitMono = 6
                Audio48kHz8BitMono = 7
                Audio48kHz16BitMono = 8
                AudioOEMDefined = 9
                OtherOEMDefined = 10

            class ActivationSignalDetectorKind(_Enum):
                AudioPattern = 0
                AudioImpulse = 1
                HardwareEvent = 2

            class ActivationSignalDetectorPowerState(_Enum):
                HighPower = 0
                ConnectedLowPower = 1
                DisconnectedLowPower = 2

            class ConversationalAgentActivationKind(_Enum):
                VoiceActivationPreview = 0
                Foreground = 1

            class ConversationalAgentActivationResult(_Enum):
                Success = 0
                AgentInactive = 1
                ScreenNotAvailable = 2
                AgentInterrupted = 3

            class ConversationalAgentSessionUpdateResponse(_Enum):
                Success = 0
                Failed = 1

            class ConversationalAgentState(_Enum):
                Inactive = 0
                Detecting = 1
                Listening = 2
                Working = 3
                Speaking = 4
                ListeningAndSpeaking = 5

            class ConversationalAgentSystemStateChangeType(_Enum):
                UserAuthentication = 0
                ScreenAvailability = 1
                IndicatorLightAvailability = 2
                VoiceActivationAvailability = 3

            class ConversationalAgentVoiceActivationPrerequisiteKind(_Enum):
                MicrophonePermission = 0
                KnownAgents = 1
                AgentAllowed = 2
                AppCapability = 3
                BackgroundTaskRegistration = 4
                PolicyPermission = 5

            class DetectionConfigurationAvailabilityChangeKind(_Enum):
                SystemResourceAccess = 0
                Permission = 1
                LockScreenPermission = 2

            class DetectionConfigurationTrainingStatus(_Enum):
                Success = 0
                FormatNotSupported = 1
                VoiceTooQuiet = 2
                VoiceTooLoud = 3
                VoiceTooFast = 4
                VoiceTooSlow = 5
                VoiceQualityProblem = 6
                TrainingSystemInternalError = 7
                TrainingTimedOut = 8
                ConfigurationNotFound = 9

            class SignalDetectorResourceKind(_Enum):
                ParallelModelSupport = 0
                ParallelModelSupportForAgent = 1
                ParallelSignalSupport = 2
                ParallelSignalSupportForAgent = 3
                DisplayOffSupport = 4
                PluggedInPower = 5
                Detector = 6
                SupportedSleepState = 7
                SupportedBatterySaverState = 8
                ScreenAvailability = 9
                InputHardware = 10
                AcousticEchoCancellation = 11
                ModelIdSupport = 12
                DataChannel = 13

        class Core:
            class AppRestartFailureReason(_Enum):
                RestartPending = 0
                NotInForeground = 1
                InvalidUser = 2
                Other = 3

        class DataTransfer:
            class ClipboardHistoryItemsResultStatus(_Enum):
                Success = 0
                AccessDenied = 1
                ClipboardHistoryDisabled = 2

            class DataPackageOperation(_Enum):
                None_ = 0x0
                Copy = 0x1
                Move = 0x2
                Link = 0x4

            class SetHistoryItemAsContentStatus(_Enum):
                Success = 0
                AccessDenied = 1
                ItemDeleted = 2

            class ShareUITheme(_Enum):
                Default = 0
                Light = 1
                Dark = 2

            class DragDrop:
                class DragDropModifiers(_Enum):
                    None_ = 0x0
                    Shift = 0x1
                    Control = 0x2
                    Alt = 0x4
                    LeftButton = 0x8
                    MiddleButton = 0x10
                    RightButton = 0x20

                class Core:
                    class CoreDragUIContentMode(_Enum):
                        Auto = 0x0
                        Deferred = 0x1

        class Email:
            class EmailAttachmentDownloadState(_Enum):
                NotDownloaded = 0
                Downloading = 1
                Downloaded = 2
                Failed = 3

            class EmailBatchStatus(_Enum):
                Success = 0
                ServerSearchSyncManagerError = 1
                ServerSearchUnknownError = 2

            class EmailCertificateValidationStatus(_Enum):
                Success = 0
                NoMatch = 1
                InvalidUsage = 2
                InvalidCertificate = 3
                Revoked = 4
                ChainRevoked = 5
                RevocationServerFailure = 6
                Expired = 7
                Untrusted = 8
                ServerError = 9
                UnknownFailure = 10

            class EmailFlagState(_Enum):
                Unflagged = 0
                Flagged = 1
                Completed = 2
                Cleared = 3

            class EmailImportance(_Enum):
                Normal = 0
                High = 1
                Low = 2

            class EmailMailboxActionKind(_Enum):
                MarkMessageAsSeen = 0
                MarkMessageRead = 1
                ChangeMessageFlagState = 2
                MoveMessage = 3
                SaveDraft = 4
                SendMessage = 5
                CreateResponseReplyMessage = 6
                CreateResponseReplyAllMessage = 7
                CreateResponseForwardMessage = 8
                MoveFolder = 9
                MarkFolderForSyncEnabled = 10

            class EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation(_Enum):
                None_ = 0
                StrongAlgorithm = 1
                AnyAlgorithm = 2

            class EmailMailboxAutoReplyMessageResponseKind(_Enum):
                Html = 0
                PlainText = 1

            class EmailMailboxChangeType(_Enum):
                MessageCreated = 0
                MessageModified = 1
                MessageDeleted = 2
                FolderCreated = 3
                FolderModified = 4
                FolderDeleted = 5
                ChangeTrackingLost = 6

            class EmailMailboxCreateFolderStatus(_Enum):
                Success = 0
                NetworkError = 1
                PermissionsError = 2
                ServerError = 3
                UnknownFailure = 4
                NameCollision = 5
                ServerRejected = 6

            class EmailMailboxDeleteFolderStatus(_Enum):
                Success = 0
                NetworkError = 1
                PermissionsError = 2
                ServerError = 3
                UnknownFailure = 4
                CouldNotDeleteEverything = 5

            class EmailMailboxEmptyFolderStatus(_Enum):
                Success = 0
                NetworkError = 1
                PermissionsError = 2
                ServerError = 3
                UnknownFailure = 4
                CouldNotDeleteEverything = 5

            class EmailMailboxOtherAppReadAccess(_Enum):
                SystemOnly = 0
                Full = 1
                None_ = 2

            class EmailMailboxOtherAppWriteAccess(_Enum):
                None_ = 0
                Limited = 1

            class EmailMailboxSmimeEncryptionAlgorithm(_Enum):
                Any = 0
                TripleDes = 1
                Des = 2
                RC2128Bit = 3
                RC264Bit = 4
                RC240Bit = 5

            class EmailMailboxSmimeSigningAlgorithm(_Enum):
                Any = 0
                Sha1 = 1
                MD5 = 2

            class EmailMailboxSyncStatus(_Enum):
                Idle = 0
                Syncing = 1
                UpToDate = 2
                AuthenticationError = 3
                PolicyError = 4
                UnknownError = 5
                ManualAccountRemovalRequired = 6

            class EmailMeetingResponseType(_Enum):
                Accept = 0
                Decline = 1
                Tentative = 2

            class EmailMessageBodyKind(_Enum):
                Html = 0
                PlainText = 1

            class EmailMessageDownloadState(_Enum):
                PartiallyDownloaded = 0
                Downloading = 1
                Downloaded = 2
                Failed = 3

            class EmailMessageResponseKind(_Enum):
                None_ = 0
                Reply = 1
                ReplyAll = 2
                Forward = 3

            class EmailMessageSmimeKind(_Enum):
                None_ = 0
                ClearSigned = 1
                OpaqueSigned = 2
                Encrypted = 3

            class EmailQueryKind(_Enum):
                All = 0
                Important = 1
                Flagged = 2
                Unread = 3
                Read = 4
                Unseen = 5

            class EmailQuerySearchFields(_Enum):
                None_ = 0x0
                Subject = 0x1
                Sender = 0x2
                Preview = 0x4
                Recipients = 0x8

            class EmailQuerySearchScope(_Enum):
                Local = 0
                Server = 1

            class EmailQuerySortDirection(_Enum):
                Descending = 0
                Ascending = 1

            class EmailQuerySortProperty(_Enum):
                Date = 0

            class EmailRecipientResolutionStatus(_Enum):
                Success = 0
                RecipientNotFound = 1
                AmbiguousRecipient = 2
                NoCertificate = 3
                CertificateRequestLimitReached = 4
                CannotResolveDistributionList = 5
                ServerError = 6
                UnknownFailure = 7

            class EmailSpecialFolderKind(_Enum):
                None_ = 0
                Root = 1
                Inbox = 2
                Outbox = 3
                Drafts = 4
                DeletedItems = 5
                Sent = 6

            class EmailStoreAccessType(_Enum):
                AppMailboxesReadWrite = 0
                AllMailboxesLimitedReadWrite = 1

        class ExtendedExecution:
            class ExtendedExecutionReason(_Enum):
                Unspecified = 0
                LocationTracking = 1
                SavingData = 2

            class ExtendedExecutionResult(_Enum):
                Allowed = 0
                Denied = 1

            class ExtendedExecutionRevokedReason(_Enum):
                Resumed = 0
                SystemPolicy = 1

            class Foreground:
                class ExtendedExecutionForegroundReason(_Enum):
                    Unspecified = 0
                    SavingData = 1
                    BackgroundAudio = 2
                    Unconstrained = 3

                class ExtendedExecutionForegroundResult(_Enum):
                    Allowed = 0
                    Denied = 1

                class ExtendedExecutionForegroundRevokedReason(_Enum):
                    Resumed = 0
                    SystemPolicy = 1

        class Payments:
            class PaymentCanMakePaymentResultStatus(_Enum):
                Unknown = 0
                Yes = 1
                No = 2
                NotAllowed = 3
                UserNotSignedIn = 4
                SpecifiedPaymentMethodIdsNotSupported = 5
                NoQualifyingCardOnFile = 6

            class PaymentOptionPresence(_Enum):
                None_ = 0
                Optional = 1
                Required = 2

            class PaymentRequestChangeKind(_Enum):
                ShippingOption = 0
                ShippingAddress = 1

            class PaymentRequestCompletionStatus(_Enum):
                Succeeded = 0
                Failed = 1
                Unknown = 2

            class PaymentRequestStatus(_Enum):
                Succeeded = 0
                Failed = 1
                Canceled = 2

            class PaymentShippingType(_Enum):
                Shipping = 0
                Delivery = 1
                Pickup = 2

        class Resources:
            class Core:
                class ResourceCandidateKind(_Enum):
                    String = 0
                    File = 1
                    EmbeddedData = 2

                class ResourceQualifierPersistence(_Enum):
                    None_ = 0
                    LocalMachine = 1

            class Management:
                class IndexedResourceType(_Enum):
                    String = 0
                    Path = 1
                    EmbeddedData = 2

        class Search:
            class Core:
                class SearchSuggestionKind(_Enum):
                    Query = 0
                    Result = 1
                    Separator = 2

        class SocialInfo:
            class SocialFeedItemStyle(_Enum):
                Default = 0
                Photo = 1

            class SocialFeedKind(_Enum):
                HomeFeed = 0
                ContactFeed = 1
                Dashboard = 2

            class SocialFeedUpdateMode(_Enum):
                Append = 0
                Replace = 1

            class SocialItemBadgeStyle(_Enum):
                Hidden = 0
                Visible = 1
                VisibleWithCount = 2

        class Store:
            class FulfillmentResult(_Enum):
                Succeeded = 0
                NothingToFulfill = 1
                PurchasePending = 2
                PurchaseReverted = 3
                ServerError = 4

            class ProductPurchaseStatus(_Enum):
                Succeeded = 0
                AlreadyPurchased = 1
                NotFulfilled = 2
                NotPurchased = 3

            class ProductType(_Enum):
                Unknown = 0
                Durable = 1
                Consumable = 2

            class LicenseManagement:
                class LicenseRefreshOption(_Enum):
                    RunningLicenses = 0
                    AllLicenses = 1

            class Preview:
                class DeliveryOptimizationDownloadMode(_Enum):
                    Simple = 0
                    HttpOnly = 1
                    Lan = 2
                    Group = 3
                    Internet = 4
                    Bypass = 5

                class DeliveryOptimizationDownloadModeSource(_Enum):
                    Default = 0
                    Policy = 1

                class StoreLogOptions(_Enum):
                    None_ = 0x0
                    TryElevate = 0x1

                class StorePreviewProductPurchaseStatus(_Enum):
                    Succeeded = 0
                    AlreadyPurchased = 1
                    NotFulfilled = 2
                    NotPurchased = 3

                class StoreSystemFeature(_Enum):
                    ArchitectureX86 = 0
                    ArchitectureX64 = 1
                    ArchitectureArm = 2
                    DirectX9 = 3
                    DirectX10 = 4
                    DirectX11 = 5
                    D3D12HardwareFL11 = 6
                    D3D12HardwareFL12 = 7
                    Memory300MB = 8
                    Memory750MB = 9
                    Memory1GB = 10
                    Memory2GB = 11
                    CameraFront = 12
                    CameraRear = 13
                    Gyroscope = 14
                    Hover = 15
                    Magnetometer = 16
                    Nfc = 17
                    Resolution720P = 18
                    ResolutionWvga = 19
                    ResolutionWvgaOr720P = 20
                    ResolutionWxga = 21
                    ResolutionWvgaOrWxga = 22
                    ResolutionWxgaOr720P = 23
                    Memory4GB = 24
                    Memory6GB = 25
                    Memory8GB = 26
                    Memory12GB = 27
                    Memory16GB = 28
                    Memory20GB = 29
                    VideoMemory2GB = 30
                    VideoMemory4GB = 31
                    VideoMemory6GB = 32
                    VideoMemory1GB = 33
                    ArchitectureArm64 = 34

                class InstallControl:
                    class AppInstallState(_Enum):
                        Pending = 0
                        Starting = 1
                        AcquiringLicense = 2
                        Downloading = 3
                        RestoringData = 4
                        Installing = 5
                        Completed = 6
                        Canceled = 7
                        Paused = 8
                        Error = 9
                        PausedLowBattery = 10
                        PausedWiFiRecommended = 11
                        PausedWiFiRequired = 12
                        ReadyToDownload = 13

                    class AppInstallType(_Enum):
                        Install = 0
                        Update = 1
                        Repair = 2

                    class AppInstallationToastNotificationMode(_Enum):
                        Default = 0
                        Toast = 1
                        ToastWithoutPopup = 2
                        NoToast = 3

                    class AutoUpdateSetting(_Enum):
                        Disabled = 0
                        Enabled = 1
                        DisabledByPolicy = 2
                        EnabledByPolicy = 3

                    class GetEntitlementStatus(_Enum):
                        Succeeded = 0
                        NoStoreAccount = 1
                        NetworkError = 2
                        ServerError = 3

        class UserActivities:
            class UserActivityState(_Enum):
                New = 0
                Published = 1

        class UserDataAccounts:
            class UserDataAccountContentKinds(_Enum):
                Email = 0x1
                Contact = 0x2
                Appointment = 0x4

            class UserDataAccountOtherAppReadAccess(_Enum):
                SystemOnly = 0
                Full = 1
                None_ = 2

            class UserDataAccountStoreAccessType(_Enum):
                AllAccountsReadOnly = 0
                AppAccountsReadWrite = 1

            class Provider:
                class UserDataAccountProviderOperationKind(_Enum):
                    AddAccount = 0
                    Settings = 1
                    ResolveErrors = 2

                class UserDataAccountProviderPartnerAccountKind(_Enum):
                    Exchange = 0
                    PopOrImap = 1

            class SystemAccess:
                class DeviceAccountAuthenticationType(_Enum):
                    Basic = 0
                    OAuth = 1
                    SingleSignOn = 2

                class DeviceAccountIconId(_Enum):
                    Exchange = 0
                    Msa = 1
                    Outlook = 2
                    Generic = 3

                class DeviceAccountMailAgeFilter(_Enum):
                    All = 0
                    Last1Day = 1
                    Last3Days = 2
                    Last7Days = 3
                    Last14Days = 4
                    Last30Days = 5
                    Last90Days = 6

                class DeviceAccountServerType(_Enum):
                    Exchange = 0
                    Pop = 1
                    Imap = 2

                class DeviceAccountSyncScheduleKind(_Enum):
                    Manual = 0
                    Every15Minutes = 1
                    Every30Minutes = 2
                    Every60Minutes = 3
                    Every2Hours = 4
                    Daily = 5
                    AsItemsArrive = 6

        class UserDataTasks:
            class UserDataTaskDaysOfWeek(_Enum):
                None_ = 0x0
                Sunday = 0x1
                Monday = 0x2
                Tuesday = 0x4
                Wednesday = 0x8
                Thursday = 0x10
                Friday = 0x20
                Saturday = 0x40

            class UserDataTaskDetailsKind(_Enum):
                PlainText = 0
                Html = 1

            class UserDataTaskKind(_Enum):
                Single = 0
                Recurring = 1
                Regenerating = 2

            class UserDataTaskListOtherAppReadAccess(_Enum):
                Full = 0
                SystemOnly = 1
                None_ = 2

            class UserDataTaskListOtherAppWriteAccess(_Enum):
                Limited = 0
                None_ = 1

            class UserDataTaskListSyncStatus(_Enum):
                Idle = 0
                Syncing = 1
                UpToDate = 2
                AuthenticationError = 3
                PolicyError = 4
                UnknownError = 5

            class UserDataTaskPriority(_Enum):
                Normal = 0
                High = 1

            class UserDataTaskQueryKind(_Enum):
                All = 0
                Incomplete = 1
                Complete = 2

            class UserDataTaskQuerySortProperty(_Enum):
                DueDate = 0

            class UserDataTaskRecurrenceUnit(_Enum):
                Daily = 0
                Weekly = 1
                Monthly = 2
                MonthlyOnDay = 3
                Yearly = 4
                YearlyOnDay = 5

            class UserDataTaskRegenerationUnit(_Enum):
                Daily = 0
                Weekly = 1
                Monthly = 2
                Yearly = 4

            class UserDataTaskSensitivity(_Enum):
                Public = 0
                Private = 1

            class UserDataTaskStoreAccessType(_Enum):
                AppTasksReadWrite = 0
                AllTasksLimitedReadWrite = 1

            class UserDataTaskWeekOfMonth(_Enum):
                First = 0
                Second = 1
                Third = 2
                Fourth = 3
                Last = 4

        class VoiceCommands:
            class VoiceCommandCompletionReason(_Enum):
                Unknown = 0
                CommunicationFailed = 1
                ResourceLimitsExceeded = 2
                Canceled = 3
                TimeoutExceeded = 4
                AppLaunched = 5
                Completed = 6

            class VoiceCommandContentTileType(_Enum):
                TitleOnly = 0
                TitleWithText = 1
                TitleWith68x68Icon = 2
                TitleWith68x68IconAndText = 3
                TitleWith68x92Icon = 4
                TitleWith68x92IconAndText = 5
                TitleWith280x140Icon = 6
                TitleWith280x140IconAndText = 7

        class Wallet:
            class WalletActionKind(_Enum):
                OpenItem = 0
                Transaction = 1
                MoreTransactions = 2
                Message = 3
                Verb = 4

            class WalletBarcodeSymbology(_Enum):
                Invalid = 0
                Upca = 1
                Upce = 2
                Ean13 = 3
                Ean8 = 4
                Itf = 5
                Code39 = 6
                Code128 = 7
                Qr = 8
                Pdf417 = 9
                Aztec = 10
                Custom = 100000

            class WalletDetailViewPosition(_Enum):
                Hidden = 0
                HeaderField1 = 1
                HeaderField2 = 2
                PrimaryField1 = 3
                PrimaryField2 = 4
                SecondaryField1 = 5
                SecondaryField2 = 6
                SecondaryField3 = 7
                SecondaryField4 = 8
                SecondaryField5 = 9
                CenterField1 = 10
                FooterField1 = 11
                FooterField2 = 12
                FooterField3 = 13
                FooterField4 = 14

            class WalletItemKind(_Enum):
                Invalid = 0
                Deal = 1
                General = 2
                PaymentInstrument = 3
                Ticket = 4
                BoardingPass = 5
                MembershipCard = 6

            class WalletSummaryViewPosition(_Enum):
                Hidden = 0
                Field1 = 1
                Field2 = 2

            class System:
                class WalletItemAppAssociation(_Enum):
                    None_ = 0
                    AppInstalled = 1
                    AppNotInstalled = 2

    class Data:
        class Json:
            class JsonErrorStatus(_Enum):
                Unknown = 0
                InvalidJsonString = 1
                InvalidJsonNumber = 2
                JsonValueNotFound = 3
                ImplementationLimit = 4

            class JsonValueType(_Enum):
                Null = 0
                Boolean = 1
                Number = 2
                String = 3
                Array = 4
                Object = 5

        class Pdf:
            class PdfPageRotation(_Enum):
                Normal = 0
                Rotate90 = 1
                Rotate180 = 2
                Rotate270 = 3

        class Text:
            class AlternateNormalizationFormat(_Enum):
                NotNormalized = 0
                Number = 1
                Currency = 3
                Date = 4
                Time = 5

            class TextPredictionOptions(_Enum):
                None_ = 0x0
                Predictions = 0x1
                Corrections = 0x2

            class UnicodeGeneralCategory(_Enum):
                UppercaseLetter = 0
                LowercaseLetter = 1
                TitlecaseLetter = 2
                ModifierLetter = 3
                OtherLetter = 4
                NonspacingMark = 5
                SpacingCombiningMark = 6
                EnclosingMark = 7
                DecimalDigitNumber = 8
                LetterNumber = 9
                OtherNumber = 10
                SpaceSeparator = 11
                LineSeparator = 12
                ParagraphSeparator = 13
                Control = 14
                Format = 15
                Surrogate = 16
                PrivateUse = 17
                ConnectorPunctuation = 18
                DashPunctuation = 19
                OpenPunctuation = 20
                ClosePunctuation = 21
                InitialQuotePunctuation = 22
                FinalQuotePunctuation = 23
                OtherPunctuation = 24
                MathSymbol = 25
                CurrencySymbol = 26
                ModifierSymbol = 27
                OtherSymbol = 28
                NotAssigned = 29

            class UnicodeNumericType(_Enum):
                None_ = 0
                Decimal = 1
                Digit = 2
                Numeric = 3

        class Xml:
            class Dom:
                class NodeType(_Enum):
                    Invalid = 0
                    ElementNode = 1
                    AttributeNode = 2
                    TextNode = 3
                    DataSectionNode = 4
                    EntityReferenceNode = 5
                    EntityNode = 6
                    ProcessingInstructionNode = 7
                    CommentNode = 8
                    DocumentNode = 9
                    DocumentTypeNode = 10
                    DocumentFragmentNode = 11
                    NotationNode = 12

    class Devices:
        class Adc:
            class AdcChannelMode(_Enum):
                SingleEnded = 0
                Differential = 1

            class Provider:
                class ProviderAdcChannelMode(_Enum):
                    SingleEnded = 0
                    Differential = 1

        class AllJoyn:
            class AllJoynAuthenticationMechanism(_Enum):
                None_ = 0
                SrpAnonymous = 1
                SrpLogon = 2
                EcdheNull = 3
                EcdhePsk = 4
                EcdheEcdsa = 5
                EcdheSpeke = 6

            class AllJoynBusAttachmentState(_Enum):
                Disconnected = 0
                Connecting = 1
                Connected = 2
                Disconnecting = 3

            class AllJoynSessionLostReason(_Enum):
                None_ = 0
                ProducerLeftSession = 1
                ProducerClosedAbruptly = 2
                RemovedByProducer = 3
                LinkTimeout = 4
                Other = 5

            class AllJoynTrafficType(_Enum):
                Unknown = 0
                Messages = 1
                RawUnreliable = 2
                RawReliable = 4

        class Bluetooth:
            class BluetoothAddressType(_Enum):
                Public = 0
                Random = 1
                Unspecified = 2

            class BluetoothCacheMode(_Enum):
                Cached = 0
                Uncached = 1

            class BluetoothConnectionStatus(_Enum):
                Disconnected = 0
                Connected = 1

            class BluetoothError(_Enum):
                Success = 0
                RadioNotAvailable = 1
                ResourceInUse = 2
                DeviceNotConnected = 3
                OtherError = 4
                DisabledByPolicy = 5
                NotSupported = 6
                DisabledByUser = 7
                ConsentRequired = 8
                TransportNotSupported = 9

            class BluetoothLEPreferredConnectionParametersRequestStatus(_Enum):
                Unspecified = 0
                Success = 1
                DeviceNotAvailable = 2
                AccessDenied = 3

            class BluetoothMajorClass(_Enum):
                Miscellaneous = 0
                Computer = 1
                Phone = 2
                NetworkAccessPoint = 3
                AudioVideo = 4
                Peripheral = 5
                Imaging = 6
                Wearable = 7
                Toy = 8
                Health = 9

            class BluetoothMinorClass(_Enum):
                Uncategorized = 0
                ComputerDesktop = 1
                ComputerServer = 2
                ComputerLaptop = 3
                ComputerHandheld = 4
                ComputerPalmSize = 5
                ComputerWearable = 6
                ComputerTablet = 7
                PhoneCellular = 1
                PhoneCordless = 2
                PhoneSmartPhone = 3
                PhoneWired = 4
                PhoneIsdn = 5
                NetworkFullyAvailable = 0
                NetworkUsed01To17Percent = 8
                NetworkUsed17To33Percent = 16
                NetworkUsed33To50Percent = 24
                NetworkUsed50To67Percent = 32
                NetworkUsed67To83Percent = 40
                NetworkUsed83To99Percent = 48
                NetworkNoServiceAvailable = 56
                AudioVideoWearableHeadset = 1
                AudioVideoHandsFree = 2
                AudioVideoMicrophone = 4
                AudioVideoLoudspeaker = 5
                AudioVideoHeadphones = 6
                AudioVideoPortableAudio = 7
                AudioVideoCarAudio = 8
                AudioVideoSetTopBox = 9
                AudioVideoHifiAudioDevice = 10
                AudioVideoVcr = 11
                AudioVideoVideoCamera = 12
                AudioVideoCamcorder = 13
                AudioVideoVideoMonitor = 14
                AudioVideoVideoDisplayAndLoudspeaker = 15
                AudioVideoVideoConferencing = 16
                AudioVideoGamingOrToy = 18
                PeripheralJoystick = 1
                PeripheralGamepad = 2
                PeripheralRemoteControl = 3
                PeripheralSensing = 4
                PeripheralDigitizerTablet = 5
                PeripheralCardReader = 6
                PeripheralDigitalPen = 7
                PeripheralHandheldScanner = 8
                PeripheralHandheldGesture = 9
                WearableWristwatch = 1
                WearablePager = 2
                WearableJacket = 3
                WearableHelmet = 4
                WearableGlasses = 5
                ToyRobot = 1
                ToyVehicle = 2
                ToyDoll = 3
                ToyController = 4
                ToyGame = 5
                HealthBloodPressureMonitor = 1
                HealthThermometer = 2
                HealthWeighingScale = 3
                HealthGlucoseMeter = 4
                HealthPulseOximeter = 5
                HealthHeartRateMonitor = 6
                HealthHealthDataDisplay = 7
                HealthStepCounter = 8
                HealthBodyCompositionAnalyzer = 9
                HealthPeakFlowMonitor = 10
                HealthMedicationMonitor = 11
                HealthKneeProsthesis = 12
                HealthAnkleProsthesis = 13
                HealthGenericHealthManager = 14
                HealthPersonalMobilityDevice = 15

            class BluetoothServiceCapabilities(_Enum):
                None_ = 0x0
                LimitedDiscoverableMode = 0x1
                PositioningService = 0x8
                NetworkingService = 0x10
                RenderingService = 0x20
                CapturingService = 0x40
                ObjectTransferService = 0x80
                AudioService = 0x100
                TelephoneService = 0x200
                InformationService = 0x400

            class Advertisement:
                class BluetoothLEAdvertisementFlags(_Enum):
                    None_ = 0x0
                    LimitedDiscoverableMode = 0x1
                    GeneralDiscoverableMode = 0x2
                    ClassicNotSupported = 0x4
                    DualModeControllerCapable = 0x8
                    DualModeHostCapable = 0x10

                class BluetoothLEAdvertisementPublisherStatus(_Enum):
                    Created = 0
                    Waiting = 1
                    Started = 2
                    Stopping = 3
                    Stopped = 4
                    Aborted = 5

                class BluetoothLEAdvertisementType(_Enum):
                    ConnectableUndirected = 0
                    ConnectableDirected = 1
                    ScannableUndirected = 2
                    NonConnectableUndirected = 3
                    ScanResponse = 4
                    Extended = 5

                class BluetoothLEAdvertisementWatcherStatus(_Enum):
                    Created = 0
                    Started = 1
                    Stopping = 2
                    Stopped = 3
                    Aborted = 4

                class BluetoothLEScanningMode(_Enum):
                    Passive = 0
                    Active = 1
                    None_ = 2

            class Background:
                class BluetoothEventTriggeringMode(_Enum):
                    Serial = 0
                    Batch = 1
                    KeepLatest = 2

            class GenericAttributeProfile:
                class GattCharacteristicProperties(_Enum):
                    None_ = 0x0
                    Broadcast = 0x1
                    Read = 0x2
                    WriteWithoutResponse = 0x4
                    Write = 0x8
                    Notify = 0x10
                    Indicate = 0x20
                    AuthenticatedSignedWrites = 0x40
                    ExtendedProperties = 0x80
                    ReliableWrites = 0x100
                    WritableAuxiliaries = 0x200

                class GattClientCharacteristicConfigurationDescriptorValue(_Enum):
                    None_ = 0
                    Notify = 1
                    Indicate = 2

                class GattCommunicationStatus(_Enum):
                    Success = 0
                    Unreachable = 1
                    ProtocolError = 2
                    AccessDenied = 3

                class GattOpenStatus(_Enum):
                    Unspecified = 0
                    Success = 1
                    AlreadyOpened = 2
                    NotFound = 3
                    SharingViolation = 4
                    AccessDenied = 5

                class GattProtectionLevel(_Enum):
                    Plain = 0
                    AuthenticationRequired = 1
                    EncryptionRequired = 2
                    EncryptionAndAuthenticationRequired = 3

                class GattRequestState(_Enum):
                    Pending = 0
                    Completed = 1
                    Canceled = 2

                class GattServiceProviderAdvertisementStatus(_Enum):
                    Created = 0
                    Stopped = 1
                    Started = 2
                    Aborted = 3
                    StartedWithoutAllAdvertisementData = 4

                class GattSessionStatus(_Enum):
                    Closed = 0
                    Active = 1

                class GattSharingMode(_Enum):
                    Unspecified = 0
                    Exclusive = 1
                    SharedReadOnly = 2
                    SharedReadAndWrite = 3

                class GattWriteOption(_Enum):
                    WriteWithResponse = 0
                    WriteWithoutResponse = 1

        class Custom:
            class DeviceAccessMode(_Enum):
                Read = 0
                Write = 1
                ReadWrite = 2

            class DeviceSharingMode(_Enum):
                Shared = 0
                Exclusive = 1

            class IOControlAccessMode(_Enum):
                Any = 0
                Read = 1
                Write = 2
                ReadWrite = 3

            class IOControlBufferingMethod(_Enum):
                Buffered = 0
                DirectInput = 1
                DirectOutput = 2
                Neither = 3

        class Display:
            class DisplayMonitorConnectionKind(_Enum):
                Internal = 0
                Wired = 1
                Wireless = 2
                Virtual = 3

            class DisplayMonitorDescriptorKind(_Enum):
                Edid = 0
                DisplayId = 1

            class DisplayMonitorPhysicalConnectorKind(_Enum):
                Unknown = 0
                HD15 = 1
                AnalogTV = 2
                Dvi = 3
                Hdmi = 4
                Lvds = 5
                Sdi = 6
                DisplayPort = 7

            class DisplayMonitorUsageKind(_Enum):
                Standard = 0
                HeadMounted = 1
                SpecialPurpose = 2

            class Core:
                class DisplayBitsPerChannel(_Enum):
                    None_ = 0x0
                    Bpc6 = 0x1
                    Bpc8 = 0x2
                    Bpc10 = 0x4
                    Bpc12 = 0x8
                    Bpc14 = 0x10
                    Bpc16 = 0x20

                class DisplayDeviceCapability(_Enum):
                    FlipOverride = 0

                class DisplayManagerOptions(_Enum):
                    None_ = 0x0
                    EnforceSourceOwnership = 0x1
                    VirtualRefreshRateAware = 0x2

                class DisplayManagerResult(_Enum):
                    Success = 0
                    UnknownFailure = 1
                    TargetAccessDenied = 2
                    TargetStale = 3
                    RemoteSessionNotSupported = 4

                class DisplayModeQueryOptions(_Enum):
                    None_ = 0x0
                    OnlyPreferredResolution = 0x1

                class DisplayPathScaling(_Enum):
                    Identity = 0
                    Centered = 1
                    Stretched = 2
                    AspectRatioStretched = 3
                    Custom = 4
                    DriverPreferred = 5

                class DisplayPathStatus(_Enum):
                    Unknown = 0
                    Succeeded = 1
                    Pending = 2
                    Failed = 3
                    FailedAsync = 4
                    InvalidatedAsync = 5

                class DisplayPresentStatus(_Enum):
                    Success = 0
                    SourceStatusPreventedPresent = 1
                    ScanoutInvalid = 2
                    SourceInvalid = 3
                    DeviceInvalid = 4
                    UnknownFailure = 5

                class DisplayRotation(_Enum):
                    None_ = 0
                    Clockwise90Degrees = 1
                    Clockwise180Degrees = 2
                    Clockwise270Degrees = 3

                class DisplayScanoutOptions(_Enum):
                    None_ = 0x0
                    AllowTearing = 0x2

                class DisplaySourceStatus(_Enum):
                    Active = 0
                    PoweredOff = 1
                    Invalid = 2
                    OwnedByAnotherDevice = 3
                    Unowned = 4

                class DisplayStateApplyOptions(_Enum):
                    None_ = 0x0
                    FailIfStateChanged = 0x1
                    ForceReapply = 0x2
                    ForceModeEnumeration = 0x4

                class DisplayStateFunctionalizeOptions(_Enum):
                    None_ = 0x0
                    FailIfStateChanged = 0x1
                    ValidateTopologyOnly = 0x2

                class DisplayStateOperationStatus(_Enum):
                    Success = 0
                    PartialFailure = 1
                    UnknownFailure = 2
                    TargetOwnershipLost = 3
                    SystemStateChanged = 4
                    TooManyPathsForAdapter = 5
                    ModesNotSupported = 6
                    RemoteSessionNotSupported = 7

                class DisplayTargetPersistence(_Enum):
                    None_ = 0
                    BootPersisted = 1
                    TemporaryPersisted = 2
                    PathPersisted = 3

                class DisplayTaskSignalKind(_Enum):
                    OnPresentFlipAway = 0
                    OnPresentFlipTo = 1

                class DisplayWireFormatColorSpace(_Enum):
                    BT709 = 0
                    BT2020 = 1
                    ProfileDefinedWideColorGamut = 2

                class DisplayWireFormatEotf(_Enum):
                    Sdr = 0
                    HdrSmpte2084 = 1

                class DisplayWireFormatHdrMetadata(_Enum):
                    None_ = 0
                    Hdr10 = 1
                    Hdr10Plus = 2
                    DolbyVisionLowLatency = 3

                class DisplayWireFormatPixelEncoding(_Enum):
                    Rgb444 = 0
                    Ycc444 = 1
                    Ycc422 = 2
                    Ycc420 = 3
                    Intensity = 4

        class Enumeration:
            class DeviceAccessStatus(_Enum):
                Unspecified = 0
                Allowed = 1
                DeniedByUser = 2
                DeniedBySystem = 3

            class DeviceClass(_Enum):
                All = 0
                AudioCapture = 1
                AudioRender = 2
                PortableStorageDevice = 3
                VideoCapture = 4
                ImageScanner = 5
                Location = 6

            class DeviceInformationKind(_Enum):
                Unknown = 0
                DeviceInterface = 1
                DeviceContainer = 2
                Device = 3
                DeviceInterfaceClass = 4
                AssociationEndpoint = 5
                AssociationEndpointContainer = 6
                AssociationEndpointService = 7
                DevicePanel = 8

            class DevicePairingKinds(_Enum):
                None_ = 0x0
                ConfirmOnly = 0x1
                DisplayPin = 0x2
                ProvidePin = 0x4
                ConfirmPinMatch = 0x8
                ProvidePasswordCredential = 0x10

            class DevicePairingProtectionLevel(_Enum):
                Default = 0
                None_ = 1
                Encryption = 2
                EncryptionAndAuthentication = 3

            class DevicePairingResultStatus(_Enum):
                Paired = 0
                NotReadyToPair = 1
                NotPaired = 2
                AlreadyPaired = 3
                ConnectionRejected = 4
                TooManyConnections = 5
                HardwareFailure = 6
                AuthenticationTimeout = 7
                AuthenticationNotAllowed = 8
                AuthenticationFailure = 9
                NoSupportedProfiles = 10
                ProtectionLevelCouldNotBeMet = 11
                AccessDenied = 12
                InvalidCeremonyData = 13
                PairingCanceled = 14
                OperationAlreadyInProgress = 15
                RequiredHandlerNotRegistered = 16
                RejectedByHandler = 17
                RemoteDeviceHasAssociation = 18
                Failed = 19

            class DevicePickerDisplayStatusOptions(_Enum):
                None_ = 0x0
                ShowProgress = 0x1
                ShowDisconnectButton = 0x2
                ShowRetryButton = 0x4

            class DeviceUnpairingResultStatus(_Enum):
                Unpaired = 0
                AlreadyUnpaired = 1
                OperationAlreadyInProgress = 2
                AccessDenied = 3
                Failed = 4

            class DeviceWatcherEventKind(_Enum):
                Add = 0
                Update = 1
                Remove = 2

            class DeviceWatcherStatus(_Enum):
                Created = 0
                Started = 1
                EnumerationCompleted = 2
                Stopping = 3
                Stopped = 4
                Aborted = 5

            class Panel(_Enum):
                Unknown = 0
                Front = 1
                Back = 2
                Top = 3
                Bottom = 4
                Left = 5
                Right = 6

            class Pnp:
                class PnpObjectType(_Enum):
                    Unknown = 0
                    DeviceInterface = 1
                    DeviceContainer = 2
                    Device = 3
                    DeviceInterfaceClass = 4
                    AssociationEndpoint = 5
                    AssociationEndpointContainer = 6
                    AssociationEndpointService = 7
                    DevicePanel = 8

        class Geolocation:
            class AltitudeReferenceSystem(_Enum):
                Unspecified = 0
                Terrain = 1
                Ellipsoid = 2
                Geoid = 3
                Surface = 4

            class GeolocationAccessStatus(_Enum):
                Unspecified = 0
                Allowed = 1
                Denied = 2

            class GeoshapeType(_Enum):
                Geopoint = 0
                Geocircle = 1
                Geopath = 2
                GeoboundingBox = 3

            class PositionAccuracy(_Enum):
                Default = 0
                High = 1

            class PositionSource(_Enum):
                Cellular = 0
                Satellite = 1
                WiFi = 2
                IPAddress = 3
                Unknown = 4
                Default = 5
                Obfuscated = 6

            class PositionStatus(_Enum):
                Ready = 0
                Initializing = 1
                NoData = 2
                Disabled = 3
                NotInitialized = 4
                NotAvailable = 5

            class VisitMonitoringScope(_Enum):
                Venue = 0
                City = 1

            class VisitStateChange(_Enum):
                TrackingLost = 0
                Arrived = 1
                Departed = 2
                OtherMovement = 3

            class Geofencing:
                class GeofenceMonitorStatus(_Enum):
                    Ready = 0
                    Initializing = 1
                    NoData = 2
                    Disabled = 3
                    NotInitialized = 4
                    NotAvailable = 5

                class GeofenceRemovalReason(_Enum):
                    Used = 0
                    Expired = 1

                class GeofenceState(_Enum):
                    None_ = 0x0
                    Entered = 0x1
                    Exited = 0x2
                    Removed = 0x4

                class MonitoredGeofenceStates(_Enum):
                    None_ = 0x0
                    Entered = 0x1
                    Exited = 0x2
                    Removed = 0x4

            class Provider:
                class LocationOverrideStatus(_Enum):
                    Success = 0
                    AccessDenied = 1
                    AlreadyStarted = 2
                    Other = 3

        class Gpio:
            class GpioChangePolarity(_Enum):
                Falling = 0
                Rising = 1
                Both = 2

            class GpioOpenStatus(_Enum):
                PinOpened = 0
                PinUnavailable = 1
                SharingViolation = 2
                MuxingConflict = 3
                UnknownError = 4

            class GpioPinDriveMode(_Enum):
                Input = 0
                Output = 1
                InputPullUp = 2
                InputPullDown = 3
                OutputOpenDrain = 4
                OutputOpenDrainPullUp = 5
                OutputOpenSource = 6
                OutputOpenSourcePullDown = 7

            class GpioPinEdge(_Enum):
                FallingEdge = 0
                RisingEdge = 1

            class GpioPinValue(_Enum):
                Low = 0
                High = 1

            class GpioSharingMode(_Enum):
                Exclusive = 0
                SharedReadOnly = 1

            class Provider:
                class ProviderGpioPinDriveMode(_Enum):
                    Input = 0
                    Output = 1
                    InputPullUp = 2
                    InputPullDown = 3
                    OutputOpenDrain = 4
                    OutputOpenDrainPullUp = 5
                    OutputOpenSource = 6
                    OutputOpenSourcePullDown = 7

                class ProviderGpioPinEdge(_Enum):
                    FallingEdge = 0
                    RisingEdge = 1

                class ProviderGpioPinValue(_Enum):
                    Low = 0
                    High = 1

                class ProviderGpioSharingMode(_Enum):
                    Exclusive = 0
                    SharedReadOnly = 1

        class Haptics:
            class VibrationAccessStatus(_Enum):
                Allowed = 0
                DeniedByUser = 1
                DeniedBySystem = 2
                DeniedByEnergySaver = 3

        class HumanInterfaceDevice:
            class HidCollectionType(_Enum):
                Physical = 0
                Application = 1
                Logical = 2
                Report = 3
                NamedArray = 4
                UsageSwitch = 5
                UsageModifier = 6
                Other = 7

            class HidReportType(_Enum):
                Input = 0
                Output = 1
                Feature = 2

        class I2c:
            class I2cBusSpeed(_Enum):
                StandardMode = 0
                FastMode = 1

            class I2cSharingMode(_Enum):
                Exclusive = 0
                Shared = 1

            class I2cTransferStatus(_Enum):
                FullTransfer = 0
                PartialTransfer = 1
                SlaveAddressNotAcknowledged = 2
                ClockStretchTimeout = 3
                UnknownError = 4

            class Provider:
                class ProviderI2cBusSpeed(_Enum):
                    StandardMode = 0
                    FastMode = 1

                class ProviderI2cSharingMode(_Enum):
                    Exclusive = 0
                    Shared = 1

                class ProviderI2cTransferStatus(_Enum):
                    FullTransfer = 0
                    PartialTransfer = 1
                    SlaveAddressNotAcknowledged = 2

        class Input:
            class PointerDeviceType(_Enum):
                Touch = 0
                Pen = 1
                Mouse = 2

            class Preview:
                class GazeDeviceConfigurationStatePreview(_Enum):
                    Unknown = 0
                    Ready = 1
                    Configuring = 2
                    ScreenSetupNeeded = 3
                    UserCalibrationNeeded = 4

        class Lights:
            class LampArrayKind(_Enum):
                Undefined = 0
                Keyboard = 1
                Mouse = 2
                GameController = 3
                Peripheral = 4
                Scene = 5
                Notification = 6
                Chassis = 7
                Wearable = 8
                Furniture = 9
                Art = 10

            class LampPurposes(_Enum):
                Undefined = 0x0
                Control = 0x1
                Accent = 0x2
                Branding = 0x4
                Status = 0x8
                Illumination = 0x10
                Presentation = 0x20

            class Effects:
                class LampArrayEffectCompletionBehavior(_Enum):
                    ClearState = 0
                    KeepState = 1

                class LampArrayEffectStartMode(_Enum):
                    Sequential = 0
                    Simultaneous = 1

                class LampArrayRepetitionMode(_Enum):
                    Occurrences = 0
                    Forever = 1

        class Midi:
            class MidiMessageType(_Enum):
                None_ = 0
                NoteOff = 128
                NoteOn = 144
                PolyphonicKeyPressure = 160
                ControlChange = 176
                ProgramChange = 192
                ChannelPressure = 208
                PitchBendChange = 224
                SystemExclusive = 240
                MidiTimeCode = 241
                SongPositionPointer = 242
                SongSelect = 243
                TuneRequest = 246
                EndSystemExclusive = 247
                TimingClock = 248
                Start = 250
                Continue = 251
                Stop = 252
                ActiveSensing = 254
                SystemReset = 255

        class Perception:
            class PerceptionFrameSourceAccessStatus(_Enum):
                Unspecified = 0
                Allowed = 1
                DeniedByUser = 2
                DeniedBySystem = 3

            class PerceptionFrameSourcePropertyChangeStatus(_Enum):
                Unknown = 0
                Accepted = 1
                LostControl = 2
                PropertyNotSupported = 3
                PropertyReadOnly = 4
                ValueOutOfRange = 5

        class PointOfService:
            class BarcodeScannerStatus(_Enum):
                Online = 0
                Off = 1
                Offline = 2
                OffOrOffline = 3
                Extended = 4

            class BarcodeSymbologyDecodeLengthKind(_Enum):
                AnyLength = 0
                Discrete = 1
                Range = 2

            class CashDrawerStatusKind(_Enum):
                Online = 0
                Off = 1
                Offline = 2
                OffOrOffline = 3
                Extended = 4

            class LineDisplayCursorType(_Enum):
                None_ = 0
                Block = 1
                HalfBlock = 2
                Underline = 3
                Reverse = 4
                Other = 5

            class LineDisplayDescriptorState(_Enum):
                Off = 0
                On = 1
                Blink = 2

            class LineDisplayHorizontalAlignment(_Enum):
                Left = 0
                Center = 1
                Right = 2

            class LineDisplayMarqueeFormat(_Enum):
                None_ = 0
                Walk = 1
                Place = 2

            class LineDisplayPowerStatus(_Enum):
                Unknown = 0
                Online = 1
                Off = 2
                Offline = 3
                OffOrOffline = 4

            class LineDisplayScrollDirection(_Enum):
                Up = 0
                Down = 1
                Left = 2
                Right = 3

            class LineDisplayTextAttribute(_Enum):
                Normal = 0
                Blink = 1
                Reverse = 2
                ReverseBlink = 3

            class LineDisplayTextAttributeGranularity(_Enum):
                NotSupported = 0
                EntireDisplay = 1
                PerCharacter = 2

            class LineDisplayVerticalAlignment(_Enum):
                Top = 0
                Center = 1
                Bottom = 2

            class MagneticStripeReaderAuthenticationLevel(_Enum):
                NotSupported = 0
                Optional = 1
                Required = 2

            class MagneticStripeReaderAuthenticationProtocol(_Enum):
                None_ = 0
                ChallengeResponse = 1

            class MagneticStripeReaderErrorReportingType(_Enum):
                CardLevel = 0
                TrackLevel = 1

            class MagneticStripeReaderStatus(_Enum):
                Unauthenticated = 0
                Authenticated = 1
                Extended = 2

            class MagneticStripeReaderTrackErrorType(_Enum):
                None_ = 0
                StartSentinelError = 1
                EndSentinelError = 2
                ParityError = 3
                LrcError = 4

            class MagneticStripeReaderTrackIds(_Enum):
                None_ = 0
                Track1 = 1
                Track2 = 2
                Track3 = 4
                Track4 = 8

            class PosConnectionTypes(_Enum):
                Local = 0x1
                IP = 0x2
                Bluetooth = 0x4

            class PosPrinterAlignment(_Enum):
                Left = 0
                Center = 1
                Right = 2

            class PosPrinterBarcodeTextPosition(_Enum):
                None_ = 0
                Above = 1
                Below = 2

            class PosPrinterCartridgeSensors(_Enum):
                None_ = 0x0
                Removed = 0x1
                Empty = 0x2
                HeadCleaning = 0x4
                NearEnd = 0x8

            class PosPrinterColorCapabilities(_Enum):
                None_ = 0x0
                Primary = 0x1
                Custom1 = 0x2
                Custom2 = 0x4
                Custom3 = 0x8
                Custom4 = 0x10
                Custom5 = 0x20
                Custom6 = 0x40
                Cyan = 0x80
                Magenta = 0x100
                Yellow = 0x200
                Full = 0x400

            class PosPrinterColorCartridge(_Enum):
                Unknown = 0
                Primary = 1
                Custom1 = 2
                Custom2 = 3
                Custom3 = 4
                Custom4 = 5
                Custom5 = 6
                Custom6 = 7
                Cyan = 8
                Magenta = 9
                Yellow = 10

            class PosPrinterLineDirection(_Enum):
                Horizontal = 0
                Vertical = 1

            class PosPrinterLineStyle(_Enum):
                SingleSolid = 0
                DoubleSolid = 1
                Broken = 2
                Chain = 3

            class PosPrinterMapMode(_Enum):
                Dots = 0
                Twips = 1
                English = 2
                Metric = 3

            class PosPrinterMarkFeedCapabilities(_Enum):
                None_ = 0x0
                ToTakeUp = 0x1
                ToCutter = 0x2
                ToCurrentTopOfForm = 0x4
                ToNextTopOfForm = 0x8

            class PosPrinterMarkFeedKind(_Enum):
                ToTakeUp = 0
                ToCutter = 1
                ToCurrentTopOfForm = 2
                ToNextTopOfForm = 3

            class PosPrinterPrintSide(_Enum):
                Unknown = 0
                Side1 = 1
                Side2 = 2

            class PosPrinterRotation(_Enum):
                Normal = 0
                Right90 = 1
                Left90 = 2
                Rotate180 = 3

            class PosPrinterRuledLineCapabilities(_Enum):
                None_ = 0x0
                Horizontal = 0x1
                Vertical = 0x2

            class PosPrinterStatusKind(_Enum):
                Online = 0
                Off = 1
                Offline = 2
                OffOrOffline = 3
                Extended = 4

            class UnifiedPosErrorReason(_Enum):
                UnknownErrorReason = 0
                NoService = 1
                Disabled = 2
                Illegal = 3
                NoHardware = 4
                Closed = 5
                Offline = 6
                Failure = 7
                Timeout = 8
                Busy = 9
                Extended = 10

            class UnifiedPosErrorSeverity(_Enum):
                UnknownErrorSeverity = 0
                Warning = 1
                Recoverable = 2
                Unrecoverable = 3
                AssistanceRequired = 4
                Fatal = 5

            class UnifiedPosHealthCheckLevel(_Enum):
                UnknownHealthCheckLevel = 0
                POSInternal = 1
                External = 2
                Interactive = 3

            class UnifiedPosPowerReportingType(_Enum):
                UnknownPowerReportingType = 0
                Standard = 1
                Advanced = 2

            class Provider:
                class BarcodeScannerTriggerState(_Enum):
                    Released = 0
                    Pressed = 1

        class Portable:
            class ServiceDeviceType(_Enum):
                CalendarService = 0
                ContactsService = 1
                DeviceStatusService = 2
                NotesService = 3
                RingtonesService = 4
                SmsService = 5
                TasksService = 6

        class Printers:
            class IppAttributeErrorReason(_Enum):
                RequestEntityTooLarge = 0
                AttributeNotSupported = 1
                AttributeValuesNotSupported = 2
                AttributeNotSettable = 3
                ConflictingAttributes = 4

            class IppAttributeValueKind(_Enum):
                Unsupported = 0
                Unknown = 1
                NoValue = 2
                Integer = 3
                Boolean = 4
                Enum = 5
                OctetString = 6
                DateTime = 7
                Resolution = 8
                RangeOfInteger = 9
                Collection = 10
                TextWithLanguage = 11
                NameWithLanguage = 12
                TextWithoutLanguage = 13
                NameWithoutLanguage = 14
                Keyword = 15
                Uri = 16
                UriSchema = 17
                Charset = 18
                NaturalLanguage = 19
                MimeMediaType = 20

            class IppResolutionUnit(_Enum):
                DotsPerInch = 0
                DotsPerCentimeter = 1

            class PageConfigurationSource(_Enum):
                PrintJobConfiguration = 0
                PdlContent = 1

            class Extensions:
                class Print3DWorkflowDetail(_Enum):
                    Unknown = 0
                    ModelExceedsPrintBed = 1
                    UploadFailed = 2
                    InvalidMaterialSelection = 3
                    InvalidModel = 4
                    ModelNotManifold = 5
                    InvalidPrintTicket = 6

                class Print3DWorkflowStatus(_Enum):
                    Abandoned = 0
                    Canceled = 1
                    Failed = 2
                    Slicing = 3
                    Submitted = 4

        class Pwm:
            class PwmPulsePolarity(_Enum):
                ActiveHigh = 0
                ActiveLow = 1

        class Radios:
            class RadioAccessStatus(_Enum):
                Unspecified = 0
                Allowed = 1
                DeniedByUser = 2
                DeniedBySystem = 3

            class RadioKind(_Enum):
                Other = 0
                WiFi = 1
                MobileBroadband = 2
                Bluetooth = 3
                FM = 4

            class RadioState(_Enum):
                Unknown = 0
                On = 1
                Off = 2
                Disabled = 3

        class Scanners:
            class ImageScannerAutoCroppingMode(_Enum):
                Disabled = 0
                SingleRegion = 1
                MultipleRegion = 2

            class ImageScannerColorMode(_Enum):
                Color = 0
                Grayscale = 1
                Monochrome = 2
                AutoColor = 3

            class ImageScannerFormat(_Enum):
                Jpeg = 0
                Png = 1
                DeviceIndependentBitmap = 2
                Tiff = 3
                Xps = 4
                OpenXps = 5
                Pdf = 6

            class ImageScannerScanSource(_Enum):
                Default = 0
                Flatbed = 1
                Feeder = 2
                AutoConfigured = 3

        class Sensors:
            class AccelerometerReadingType(_Enum):
                Standard = 0
                Linear = 1
                Gravity = 2

            class ActivitySensorReadingConfidence(_Enum):
                High = 0
                Low = 1

            class ActivityType(_Enum):
                Unknown = 0
                Idle = 1
                Stationary = 2
                Fidgeting = 3
                Walking = 4
                Running = 5
                InVehicle = 6
                Biking = 7

            class HumanEngagement(_Enum):
                Unknown = 0
                Engaged = 1
                Unengaged = 2

            class HumanPresence(_Enum):
                Unknown = 0
                Present = 1
                NotPresent = 2

            class MagnetometerAccuracy(_Enum):
                Unknown = 0
                Unreliable = 1
                Approximate = 2
                High = 3

            class PedometerStepKind(_Enum):
                Unknown = 0
                Walking = 1
                Running = 2

            class SensorOptimizationGoal(_Enum):
                Precision = 0
                PowerEfficiency = 1

            class SensorReadingType(_Enum):
                Absolute = 0
                Relative = 1

            class SensorType(_Enum):
                Accelerometer = 0
                ActivitySensor = 1
                Barometer = 2
                Compass = 3
                CustomSensor = 4
                Gyroscope = 5
                ProximitySensor = 6
                Inclinometer = 7
                LightSensor = 8
                OrientationSensor = 9
                Pedometer = 10
                RelativeInclinometer = 11
                RelativeOrientationSensor = 12
                SimpleOrientationSensor = 13

            class SimpleOrientation(_Enum):
                NotRotated = 0
                Rotated90DegreesCounterclockwise = 1
                Rotated180DegreesCounterclockwise = 2
                Rotated270DegreesCounterclockwise = 3
                Faceup = 4
                Facedown = 5

        class SerialCommunication:
            class SerialError(_Enum):
                Frame = 0
                BufferOverrun = 1
                ReceiveFull = 2
                ReceiveParity = 3
                TransmitFull = 4

            class SerialHandshake(_Enum):
                None_ = 0
                RequestToSend = 1
                XOnXOff = 2
                RequestToSendXOnXOff = 3

            class SerialParity(_Enum):
                None_ = 0
                Odd = 1
                Even = 2
                Mark = 3
                Space = 4

            class SerialPinChange(_Enum):
                BreakSignal = 0
                CarrierDetect = 1
                ClearToSend = 2
                DataSetReady = 3
                RingIndicator = 4

            class SerialStopBitCount(_Enum):
                One = 0
                OnePointFive = 1
                Two = 2

        class SmartCards:
            class SmartCardActivationPolicyChangeResult(_Enum):
                Denied = 0
                Allowed = 1

            class SmartCardAppletIdGroupActivationPolicy(_Enum):
                Disabled = 0
                ForegroundOverride = 1
                Enabled = 2

            class SmartCardAutomaticResponseStatus(_Enum):
                None_ = 0
                Success = 1
                UnknownError = 2

            class SmartCardCryptogramAlgorithm(_Enum):
                None_ = 0
                CbcMac = 1
                Cvc3Umd = 2
                DecimalizedMsd = 3
                Cvc3MD = 4
                Sha1 = 5
                SignedDynamicApplicationData = 6
                RsaPkcs1 = 7
                Sha256Hmac = 8

            class SmartCardCryptogramGeneratorOperationStatus(_Enum):
                Success = 0
                AuthorizationFailed = 1
                AuthorizationCanceled = 2
                AuthorizationRequired = 3
                CryptogramMaterialPackageStorageKeyExists = 4
                NoCryptogramMaterialPackageStorageKey = 5
                NoCryptogramMaterialPackage = 6
                UnsupportedCryptogramMaterialPackage = 7
                UnknownCryptogramMaterialName = 8
                InvalidCryptogramMaterialUsage = 9
                ApduResponseNotSent = 10
                OtherError = 11
                ValidationFailed = 12
                NotSupported = 13

            class SmartCardCryptogramMaterialPackageConfirmationResponseFormat(_Enum):
                None_ = 0
                VisaHmac = 1

            class SmartCardCryptogramMaterialPackageFormat(_Enum):
                None_ = 0
                JweRsaPki = 1

            class SmartCardCryptogramMaterialProtectionMethod(_Enum):
                None_ = 0
                WhiteBoxing = 1

            class SmartCardCryptogramMaterialType(_Enum):
                None_ = 0
                StaticDataAuthentication = 1
                TripleDes112 = 2
                Aes = 3
                RsaPkcs1 = 4

            class SmartCardCryptogramPlacementOptions(_Enum):
                None_ = 0x0
                UnitsAreInNibbles = 0x1
                ChainOutput = 0x2

            class SmartCardCryptogramStorageKeyAlgorithm(_Enum):
                None_ = 0
                Rsa2048 = 1

            class SmartCardCryptogramStorageKeyCapabilities(_Enum):
                None_ = 0x0
                HardwareProtection = 0x1
                UnlockPrompt = 0x2

            class SmartCardCryptographicKeyAttestationStatus(_Enum):
                NoAttestation = 0
                SoftwareKeyWithoutTpm = 1
                SoftwareKeyWithTpm = 2
                TpmKeyUnknownAttestationStatus = 3
                TpmKeyWithoutAttestationCapability = 4
                TpmKeyWithTemporaryAttestationFailure = 5
                TpmKeyWithLongTermAttestationFailure = 6
                TpmKeyWithAttestation = 7

            class SmartCardEmulationCategory(_Enum):
                Other = 0
                Payment = 1

            class SmartCardEmulationType(_Enum):
                Host = 0
                Uicc = 1
                EmbeddedSE = 2

            class SmartCardEmulatorConnectionDeactivatedReason(_Enum):
                ConnectionLost = 0
                ConnectionRedirected = 1

            class SmartCardEmulatorConnectionSource(_Enum):
                Unknown = 0
                NfcReader = 1

            class SmartCardEmulatorEnablementPolicy(_Enum):
                Never = 0
                Always = 1
                ScreenOn = 2
                ScreenUnlocked = 3

            class SmartCardLaunchBehavior(_Enum):
                Default = 0
                AboveLock = 1

            class SmartCardPinCharacterPolicyOption(_Enum):
                Allow = 0
                RequireAtLeastOne = 1
                Disallow = 2

            class SmartCardReaderKind(_Enum):
                Any = 0
                Generic = 1
                Tpm = 2
                Nfc = 3
                Uicc = 4
                EmbeddedSE = 5

            class SmartCardReaderStatus(_Enum):
                Disconnected = 0
                Ready = 1
                Exclusive = 2

            class SmartCardStatus(_Enum):
                Disconnected = 0
                Ready = 1
                Shared = 2
                Exclusive = 3
                Unresponsive = 4

            class SmartCardTriggerType(_Enum):
                EmulatorTransaction = 0
                EmulatorNearFieldEntry = 1
                EmulatorNearFieldExit = 2
                EmulatorHostApplicationActivated = 3
                EmulatorAppletIdGroupRegistrationChanged = 4
                ReaderCardAdded = 5

            class SmartCardUnlockPromptingBehavior(_Enum):
                AllowUnlockPrompt = 0
                RequireUnlockPrompt = 1
                PreventUnlockPrompt = 2

        class Sms:
            class CellularClass(_Enum):
                None_ = 0
                Gsm = 1
                Cdma = 2

            class SmsBroadcastType(_Enum):
                Other = 0
                CmasPresidential = 1
                CmasExtreme = 2
                CmasSevere = 3
                CmasAmber = 4
                CmasTest = 5
                EUAlert1 = 6
                EUAlert2 = 7
                EUAlert3 = 8
                EUAlertAmber = 9
                EUAlertInfo = 10
                EtwsEarthquake = 11
                EtwsTsunami = 12
                EtwsTsunamiAndEarthquake = 13
                LatAlertLocal = 14

            class SmsDataFormat(_Enum):
                Unknown = 0
                CdmaSubmit = 1
                GsmSubmit = 2
                CdmaDeliver = 3
                GsmDeliver = 4

            class SmsDeviceStatus(_Enum):
                Off = 0
                Ready = 1
                SimNotInserted = 2
                BadSim = 3
                DeviceFailure = 4
                SubscriptionNotActivated = 5
                DeviceLocked = 6
                DeviceBlocked = 7

            class SmsEncoding(_Enum):
                Unknown = 0
                Optimal = 1
                SevenBitAscii = 2
                Unicode = 3
                GsmSevenBit = 4
                EightBit = 5
                Latin = 6
                Korean = 7
                IA5 = 8
                ShiftJis = 9
                LatinHebrew = 10

            class SmsFilterActionType(_Enum):
                AcceptImmediately = 0
                Drop = 1
                Peek = 2
                Accept = 3

            class SmsGeographicalScope(_Enum):
                None_ = 0
                CellWithImmediateDisplay = 1
                LocationArea = 2
                Plmn = 3
                Cell = 4

            class SmsMessageClass(_Enum):
                None_ = 0
                Class0 = 1
                Class1 = 2
                Class2 = 3
                Class3 = 4

            class SmsMessageFilter(_Enum):
                All = 0
                Unread = 1
                Read = 2
                Sent = 3
                Draft = 4

            class SmsMessageType(_Enum):
                Binary = 0
                Text = 1
                Wap = 2
                App = 3
                Broadcast = 4
                Voicemail = 5
                Status = 6

            class SmsModemErrorCode(_Enum):
                Other = 0
                MessagingNetworkError = 1
                SmsOperationNotSupportedByDevice = 2
                SmsServiceNotSupportedByNetwork = 3
                DeviceFailure = 4
                MessageNotEncodedProperly = 5
                MessageTooLarge = 6
                DeviceNotReady = 7
                NetworkNotReady = 8
                InvalidSmscAddress = 9
                NetworkFailure = 10
                FixedDialingNumberRestricted = 11

        class Spi:
            class SpiMode(_Enum):
                Mode0 = 0
                Mode1 = 1
                Mode2 = 2
                Mode3 = 3

            class SpiSharingMode(_Enum):
                Exclusive = 0
                Shared = 1

            class Provider:
                class ProviderSpiMode(_Enum):
                    Mode0 = 0
                    Mode1 = 1
                    Mode2 = 2
                    Mode3 = 3

                class ProviderSpiSharingMode(_Enum):
                    Exclusive = 0
                    Shared = 1

        class Usb:
            class UsbControlRecipient(_Enum):
                Device = 0
                SpecifiedInterface = 1
                Endpoint = 2
                Other = 3
                DefaultInterface = 4

            class UsbControlTransferType(_Enum):
                Standard = 0
                Class = 1
                Vendor = 2

            class UsbEndpointType(_Enum):
                Control = 0
                Isochronous = 1
                Bulk = 2
                Interrupt = 3

            class UsbReadOptions(_Enum):
                None_ = 0x0
                AutoClearStall = 0x1
                OverrideAutomaticBufferManagement = 0x2
                IgnoreShortPacket = 0x4
                AllowPartialReads = 0x8

            class UsbTransferDirection(_Enum):
                Out = 0
                In = 1

            class UsbWriteOptions(_Enum):
                None_ = 0x0
                AutoClearStall = 0x1
                ShortPacketTerminate = 0x2

        class WiFi:
            class WiFiAccessStatus(_Enum):
                Unspecified = 0
                Allowed = 1
                DeniedByUser = 2
                DeniedBySystem = 3

            class WiFiConnectionMethod(_Enum):
                Default = 0
                WpsPin = 1
                WpsPushButton = 2

            class WiFiConnectionStatus(_Enum):
                UnspecifiedFailure = 0
                Success = 1
                AccessRevoked = 2
                InvalidCredential = 3
                NetworkNotAvailable = 4
                Timeout = 5
                UnsupportedAuthenticationProtocol = 6

            class WiFiNetworkKind(_Enum):
                Any = 0
                Infrastructure = 1
                Adhoc = 2

            class WiFiOnDemandHotspotAvailability(_Enum):
                Available = 0
                Unavailable = 1

            class WiFiOnDemandHotspotCellularBars(_Enum):
                ZeroBars = 0
                OneBar = 1
                TwoBars = 2
                ThreeBars = 3
                FourBars = 4
                FiveBars = 5

            class WiFiOnDemandHotspotConnectStatus(_Enum):
                UnspecifiedFailure = 0
                Success = 1
                AppTimedOut = 2
                InvalidCredential = 3
                NetworkNotAvailable = 4
                UnsupportedAuthenticationProtocol = 5
                BluetoothConnectFailed = 6
                BluetoothTransmissionError = 7
                OperationCanceledByUser = 8
                EntitlementCheckFailed = 9
                NoCellularSignal = 10
                CellularDataTurnedOff = 11
                WlanConnectFailed = 12
                WlanNotVisible = 13
                AccessPointCannotConnect = 14
                CellularConnectTimedOut = 15
                RoamingNotAllowed = 16
                PairingRequired = 17
                DataLimitReached = 18

            class WiFiPhyKind(_Enum):
                Unknown = 0
                Fhss = 1
                Dsss = 2
                IRBaseband = 3
                Ofdm = 4
                Hrdsss = 5
                Erp = 6
                HT = 7
                Vht = 8
                Dmg = 9
                HE = 10
                Eht = 11

            class WiFiReconnectionKind(_Enum):
                Automatic = 0
                Manual = 1

            class WiFiWpsConfigurationStatus(_Enum):
                UnspecifiedFailure = 0
                Success = 1
                Timeout = 2

            class WiFiWpsKind(_Enum):
                Unknown = 0
                Pin = 1
                PushButton = 2
                Nfc = 3
                Ethernet = 4
                Usb = 5

        class WiFiDirect:
            class WiFiDirectAdvertisementListenStateDiscoverability(_Enum):
                None_ = 0
                Normal = 1
                Intensive = 2

            class WiFiDirectAdvertisementPublisherStatus(_Enum):
                Created = 0
                Started = 1
                Stopped = 2
                Aborted = 3

            class WiFiDirectConfigurationMethod(_Enum):
                ProvidePin = 0
                DisplayPin = 1
                PushButton = 2

            class WiFiDirectConnectionStatus(_Enum):
                Disconnected = 0
                Connected = 1

            class WiFiDirectDeviceSelectorType(_Enum):
                DeviceInterface = 0
                AssociationEndpoint = 1

            class WiFiDirectError(_Enum):
                Success = 0
                RadioNotAvailable = 1
                ResourceInUse = 2

            class WiFiDirectPairingProcedure(_Enum):
                GroupOwnerNegotiation = 0
                Invitation = 1

            class Services:
                class WiFiDirectServiceAdvertisementStatus(_Enum):
                    Created = 0
                    Started = 1
                    Stopped = 2
                    Aborted = 3

                class WiFiDirectServiceConfigurationMethod(_Enum):
                    Default = 0
                    PinDisplay = 1
                    PinEntry = 2

                class WiFiDirectServiceError(_Enum):
                    Success = 0
                    RadioNotAvailable = 1
                    ResourceInUse = 2
                    UnsupportedHardware = 3
                    NoHardware = 4

                class WiFiDirectServiceIPProtocol(_Enum):
                    Tcp = 6
                    Udp = 17

                class WiFiDirectServiceSessionErrorStatus(_Enum):
                    Ok = 0
                    Disassociated = 1
                    LocalClose = 2
                    RemoteClose = 3
                    SystemFailure = 4
                    NoResponseFromRemote = 5

                class WiFiDirectServiceSessionStatus(_Enum):
                    Closed = 0
                    Initiated = 1
                    Requested = 2
                    Open = 3

                class WiFiDirectServiceStatus(_Enum):
                    Available = 0
                    Busy = 1
                    Custom = 2

    class Foundation:
        class AsyncStatus(_Enum):
            Started = _AUTO
            Completed = _AUTO
            Canceled = _AUTO
            Error = _AUTO

        class PropertyType(_Enum):
            Empty = 0
            UInt8 = 1
            Int16 = 2
            UInt16 = 3
            Int32 = 4
            UInt32 = 5
            Int64 = 6
            UInt64 = 7
            Single = 8
            Double = 9
            Char16 = 10
            Boolean = 11
            String = 12
            Inspectable = 13
            DateTime = 14
            TimeSpan = 15
            Guid = 16
            Point = 17
            Size = 18
            Rect = 19
            OtherType = 20
            UInt8Array = 1025
            Int16Array = 1026
            UInt16Array = 1027
            Int32Array = 1028
            UInt32Array = 1029
            Int64Array = 1030
            UInt64Array = 1031
            SingleArray = 1032
            DoubleArray = 1033
            Char16Array = 1034
            BooleanArray = 1035
            StringArray = 1036
            InspectableArray = 1037
            DateTimeArray = 1038
            TimeSpanArray = 1039
            GuidArray = 1040
            PointArray = 1041
            SizeArray = 1042
            RectArray = 1043
            OtherTypeArray = 1044

        class Collections:
            class CollectionChange(_Enum):
                Reset = _AUTO
                ItemInserted = _AUTO
                ItemRemoved = _AUTO
                ItemChanged = _AUTO

        class Diagnostics:
            class CausalityRelation(_Enum):
                AssignDelegate = 0
                Join = 1
                Choice = 2
                Cancel = 3
                Error = 4

            class CausalitySource(_Enum):
                Application = 0
                Library = 1
                System = 2

            class CausalitySynchronousWork(_Enum):
                CompletionNotification = 0
                ProgressNotification = 1
                Execution = 2

            class CausalityTraceLevel(_Enum):
                Required = 0
                Important = 1
                Verbose = 2

            class ErrorOptions(_Enum):
                None_ = 0x0
                SuppressExceptions = 0x1
                ForceExceptions = 0x2
                UseSetErrorInfo = 0x4
                SuppressSetErrorInfo = 0x8

            class LoggingFieldFormat(_Enum):
                Default = 0
                Hidden = 1
                String = 2
                Boolean = 3
                Hexadecimal = 4
                ProcessId = 5
                ThreadId = 6
                Port = 7
                Ipv4Address = 8
                Ipv6Address = 9
                SocketAddress = 10
                Xml = 11
                Json = 12
                Win32Error = 13
                NTStatus = 14
                HResult = 15
                FileTime = 16
                Signed = 17
                Unsigned = 18

            class LoggingLevel(_Enum):
                Verbose = 0
                Information = 1
                Warning = 2
                Error = 3
                Critical = 4

            class LoggingOpcode(_Enum):
                Info = 0
                Start = 1
                Stop = 2
                Reply = 6
                Resume = 7
                Suspend = 8
                Send = 9

        class Metadata:
            class GCPressureAmount(_Enum):
                Low = 0
                Medium = 1
                High = 2

    class Gaming:
        class Input:
            class ArcadeStickButtons(_Enum):
                None_ = 0x0
                StickUp = 0x1
                StickDown = 0x2
                StickLeft = 0x4
                StickRight = 0x8
                Action1 = 0x10
                Action2 = 0x20
                Action3 = 0x40
                Action4 = 0x80
                Action5 = 0x100
                Action6 = 0x200
                Special1 = 0x400
                Special2 = 0x800

            class FlightStickButtons(_Enum):
                None_ = 0x0
                FirePrimary = 0x1
                FireSecondary = 0x2

            class GameControllerButtonLabel(_Enum):
                None_ = 0
                XboxBack = 1
                XboxStart = 2
                XboxMenu = 3
                XboxView = 4
                XboxUp = 5
                XboxDown = 6
                XboxLeft = 7
                XboxRight = 8
                XboxA = 9
                XboxB = 10
                XboxX = 11
                XboxY = 12
                XboxLeftBumper = 13
                XboxLeftTrigger = 14
                XboxLeftStickButton = 15
                XboxRightBumper = 16
                XboxRightTrigger = 17
                XboxRightStickButton = 18
                XboxPaddle1 = 19
                XboxPaddle2 = 20
                XboxPaddle3 = 21
                XboxPaddle4 = 22
                Mode = 23
                Select = 24
                Menu = 25
                View = 26
                Back = 27
                Start = 28
                Options = 29
                Share = 30
                Up = 31
                Down = 32
                Left = 33
                Right = 34
                LetterA = 35
                LetterB = 36
                LetterC = 37
                LetterL = 38
                LetterR = 39
                LetterX = 40
                LetterY = 41
                LetterZ = 42
                Cross = 43
                Circle = 44
                Square = 45
                Triangle = 46
                LeftBumper = 47
                LeftTrigger = 48
                LeftStickButton = 49
                Left1 = 50
                Left2 = 51
                Left3 = 52
                RightBumper = 53
                RightTrigger = 54
                RightStickButton = 55
                Right1 = 56
                Right2 = 57
                Right3 = 58
                Paddle1 = 59
                Paddle2 = 60
                Paddle3 = 61
                Paddle4 = 62
                Plus = 63
                Minus = 64
                DownLeftArrow = 65
                DialLeft = 66
                DialRight = 67
                Suspension = 68

            class GameControllerSwitchKind(_Enum):
                TwoWay = 0
                FourWay = 1
                EightWay = 2

            class GameControllerSwitchPosition(_Enum):
                Center = 0
                Up = 1
                UpRight = 2
                Right = 3
                DownRight = 4
                Down = 5
                DownLeft = 6
                Left = 7
                UpLeft = 8

            class GamepadButtons(_Enum):
                None_ = 0x0
                Menu = 0x1
                View = 0x2
                A = 0x4
                B = 0x8
                X = 0x10
                Y = 0x20
                DPadUp = 0x40
                DPadDown = 0x80
                DPadLeft = 0x100
                DPadRight = 0x200
                LeftShoulder = 0x400
                RightShoulder = 0x800
                LeftThumbstick = 0x1000
                RightThumbstick = 0x2000
                Paddle1 = 0x4000
                Paddle2 = 0x8000
                Paddle3 = 0x10000
                Paddle4 = 0x20000

            class OptionalUINavigationButtons(_Enum):
                None_ = 0x0
                Context1 = 0x1
                Context2 = 0x2
                Context3 = 0x4
                Context4 = 0x8
                PageUp = 0x10
                PageDown = 0x20
                PageLeft = 0x40
                PageRight = 0x80
                ScrollUp = 0x100
                ScrollDown = 0x200
                ScrollLeft = 0x400
                ScrollRight = 0x800

            class RacingWheelButtons(_Enum):
                None_ = 0x0
                PreviousGear = 0x1
                NextGear = 0x2
                DPadUp = 0x4
                DPadDown = 0x8
                DPadLeft = 0x10
                DPadRight = 0x20
                Button1 = 0x40
                Button2 = 0x80
                Button3 = 0x100
                Button4 = 0x200
                Button5 = 0x400
                Button6 = 0x800
                Button7 = 0x1000
                Button8 = 0x2000
                Button9 = 0x4000
                Button10 = 0x8000
                Button11 = 0x10000
                Button12 = 0x20000
                Button13 = 0x40000
                Button14 = 0x80000
                Button15 = 0x100000
                Button16 = 0x200000

            class RequiredUINavigationButtons(_Enum):
                None_ = 0x0
                Menu = 0x1
                View = 0x2
                Accept = 0x4
                Cancel = 0x8
                Up = 0x10
                Down = 0x20
                Left = 0x40
                Right = 0x80

            class Custom:
                class GipFirmwareUpdateStatus(_Enum):
                    Completed = 0
                    UpToDate = 1
                    Failed = 2

                class GipMessageClass(_Enum):
                    Command = 0
                    LowLatency = 1
                    StandardLatency = 2

                class XusbDeviceSubtype(_Enum):
                    Unknown = 0
                    Gamepad = 1
                    ArcadePad = 2
                    ArcadeStick = 3
                    FlightStick = 4
                    Wheel = 5
                    Guitar = 6
                    GuitarAlternate = 7
                    GuitarBass = 8
                    DrumKit = 9
                    DancePad = 10

                class XusbDeviceType(_Enum):
                    Unknown = 0
                    Gamepad = 1

            class ForceFeedback:
                class ConditionForceEffectKind(_Enum):
                    Spring = 0
                    Damper = 1
                    Inertia = 2
                    Friction = 3

                class ForceFeedbackEffectAxes(_Enum):
                    None_ = 0x0
                    X = 0x1
                    Y = 0x2
                    Z = 0x4

                class ForceFeedbackEffectState(_Enum):
                    Stopped = 0
                    Running = 1
                    Paused = 2
                    Faulted = 3

                class ForceFeedbackLoadEffectResult(_Enum):
                    Succeeded = 0
                    EffectStorageFull = 1
                    EffectNotSupported = 2

                class PeriodicForceEffectKind(_Enum):
                    SquareWave = 0
                    SineWave = 1
                    TriangleWave = 2
                    SawtoothWaveUp = 3
                    SawtoothWaveDown = 4

        class Preview:
            class GamesEnumeration:
                class GameListCategory(_Enum):
                    Candidate = 0
                    ConfirmedBySystem = 1
                    ConfirmedByUser = 2

                class GameListEntryLaunchableState(_Enum):
                    NotLaunchable = 0
                    ByLastRunningFullPath = 1
                    ByUserProvidedPath = 2
                    ByTile = 3

        class UI:
            class GameChatMessageOrigin(_Enum):
                Voice = 0
                Text = 1

            class GameChatOverlayPosition(_Enum):
                BottomCenter = 0
                BottomLeft = 1
                BottomRight = 2
                MiddleRight = 3
                MiddleLeft = 4
                TopCenter = 5
                TopLeft = 6
                TopRight = 7

        class XboxLive:
            class Storage:
                class GameSaveErrorStatus(_Enum):
                    Ok = 0

    class Globalization:
        class DayOfWeek(_Enum):
            Sunday = 0
            Monday = 1
            Tuesday = 2
            Wednesday = 3
            Thursday = 4
            Friday = 5
            Saturday = 6

        class LanguageLayoutDirection(_Enum):
            Ltr = 0
            Rtl = 1
            TtbLtr = 2
            TtbRtl = 3

        class DateTimeFormatting:
            class DayFormat(_Enum):
                None_ = 0
                Default = 1

            class DayOfWeekFormat(_Enum):
                None_ = 0
                Default = 1
                Abbreviated = 2
                Full = 3

            class HourFormat(_Enum):
                None_ = 0
                Default = 1

            class MinuteFormat(_Enum):
                None_ = 0
                Default = 1

            class MonthFormat(_Enum):
                None_ = 0
                Default = 1
                Abbreviated = 2
                Full = 3
                Numeric = 4

            class SecondFormat(_Enum):
                None_ = 0
                Default = 1

            class YearFormat(_Enum):
                None_ = 0
                Default = 1
                Abbreviated = 2
                Full = 3

        class NumberFormatting:
            class CurrencyFormatterMode(_Enum):
                UseSymbol = 0
                UseCurrencyCode = 1

            class RoundingAlgorithm(_Enum):
                None_ = 0
                RoundDown = 1
                RoundUp = 2
                RoundTowardsZero = 3
                RoundAwayFromZero = 4
                RoundHalfDown = 5
                RoundHalfUp = 6
                RoundHalfTowardsZero = 7
                RoundHalfAwayFromZero = 8
                RoundHalfToEven = 9
                RoundHalfToOdd = 10

        class PhoneNumberFormatting:
            class PhoneNumberFormat(_Enum):
                E164 = 0
                International = 1
                National = 2
                Rfc3966 = 3

            class PhoneNumberMatchResult(_Enum):
                NoMatch = 0
                ShortNationalSignificantNumberMatch = 1
                NationalSignificantNumberMatch = 2
                ExactMatch = 3

            class PhoneNumberParseResult(_Enum):
                Valid = 0
                NotANumber = 1
                InvalidCountryCode = 2
                TooShort = 3
                TooLong = 4

            class PredictedPhoneNumberKind(_Enum):
                FixedLine = 0
                Mobile = 1
                FixedLineOrMobile = 2
                TollFree = 3
                PremiumRate = 4
                SharedCost = 5
                Voip = 6
                PersonalNumber = 7
                Pager = 8
                UniversalAccountNumber = 9
                Voicemail = 10
                Unknown = 11

    class Graphics:
        class Capture:
            class GraphicsCaptureAccessKind(_Enum):
                Borderless = 0
                Programmatic = 1

        class DirectX:
            class DirectXAlphaMode(_Enum):
                Unspecified = 0
                Premultiplied = 1
                Straight = 2
                Ignore = 3

            class DirectXColorSpace(_Enum):
                RgbFullG22NoneP709 = 0
                RgbFullG10NoneP709 = 1
                RgbStudioG22NoneP709 = 2
                RgbStudioG22NoneP2020 = 3
                Reserved = 4
                YccFullG22NoneP709X601 = 5
                YccStudioG22LeftP601 = 6
                YccFullG22LeftP601 = 7
                YccStudioG22LeftP709 = 8
                YccFullG22LeftP709 = 9
                YccStudioG22LeftP2020 = 10
                YccFullG22LeftP2020 = 11
                RgbFullG2084NoneP2020 = 12
                YccStudioG2084LeftP2020 = 13
                RgbStudioG2084NoneP2020 = 14
                YccStudioG22TopLeftP2020 = 15
                YccStudioG2084TopLeftP2020 = 16
                RgbFullG22NoneP2020 = 17
                YccStudioGHlgTopLeftP2020 = 18
                YccFullGHlgTopLeftP2020 = 19
                RgbStudioG24NoneP709 = 20
                RgbStudioG24NoneP2020 = 21
                YccStudioG24LeftP709 = 22
                YccStudioG24LeftP2020 = 23
                YccStudioG24TopLeftP2020 = 24

            class DirectXPixelFormat(_Enum):
                Unknown = 0
                R32G32B32A32Typeless = 1
                R32G32B32A32Float = 2
                R32G32B32A32UInt = 3
                R32G32B32A32Int = 4
                R32G32B32Typeless = 5
                R32G32B32Float = 6
                R32G32B32UInt = 7
                R32G32B32Int = 8
                R16G16B16A16Typeless = 9
                R16G16B16A16Float = 10
                R16G16B16A16UIntNormalized = 11
                R16G16B16A16UInt = 12
                R16G16B16A16IntNormalized = 13
                R16G16B16A16Int = 14
                R32G32Typeless = 15
                R32G32Float = 16
                R32G32UInt = 17
                R32G32Int = 18
                R32G8X24Typeless = 19
                D32FloatS8X24UInt = 20
                R32FloatX8X24Typeless = 21
                X32TypelessG8X24UInt = 22
                R10G10B10A2Typeless = 23
                R10G10B10A2UIntNormalized = 24
                R10G10B10A2UInt = 25
                R11G11B10Float = 26
                R8G8B8A8Typeless = 27
                R8G8B8A8UIntNormalized = 28
                R8G8B8A8UIntNormalizedSrgb = 29
                R8G8B8A8UInt = 30
                R8G8B8A8IntNormalized = 31
                R8G8B8A8Int = 32
                R16G16Typeless = 33
                R16G16Float = 34
                R16G16UIntNormalized = 35
                R16G16UInt = 36
                R16G16IntNormalized = 37
                R16G16Int = 38
                R32Typeless = 39
                D32Float = 40
                R32Float = 41
                R32UInt = 42
                R32Int = 43
                R24G8Typeless = 44
                D24UIntNormalizedS8UInt = 45
                R24UIntNormalizedX8Typeless = 46
                X24TypelessG8UInt = 47
                R8G8Typeless = 48
                R8G8UIntNormalized = 49
                R8G8UInt = 50
                R8G8IntNormalized = 51
                R8G8Int = 52
                R16Typeless = 53
                R16Float = 54
                D16UIntNormalized = 55
                R16UIntNormalized = 56
                R16UInt = 57
                R16IntNormalized = 58
                R16Int = 59
                R8Typeless = 60
                R8UIntNormalized = 61
                R8UInt = 62
                R8IntNormalized = 63
                R8Int = 64
                A8UIntNormalized = 65
                R1UIntNormalized = 66
                R9G9B9E5SharedExponent = 67
                R8G8B8G8UIntNormalized = 68
                G8R8G8B8UIntNormalized = 69
                BC1Typeless = 70
                BC1UIntNormalized = 71
                BC1UIntNormalizedSrgb = 72
                BC2Typeless = 73
                BC2UIntNormalized = 74
                BC2UIntNormalizedSrgb = 75
                BC3Typeless = 76
                BC3UIntNormalized = 77
                BC3UIntNormalizedSrgb = 78
                BC4Typeless = 79
                BC4UIntNormalized = 80
                BC4IntNormalized = 81
                BC5Typeless = 82
                BC5UIntNormalized = 83
                BC5IntNormalized = 84
                B5G6R5UIntNormalized = 85
                B5G5R5A1UIntNormalized = 86
                B8G8R8A8UIntNormalized = 87
                B8G8R8X8UIntNormalized = 88
                R10G10B10XRBiasA2UIntNormalized = 89
                B8G8R8A8Typeless = 90
                B8G8R8A8UIntNormalizedSrgb = 91
                B8G8R8X8Typeless = 92
                B8G8R8X8UIntNormalizedSrgb = 93
                BC6HTypeless = 94
                BC6H16UnsignedFloat = 95
                BC6H16Float = 96
                BC7Typeless = 97
                BC7UIntNormalized = 98
                BC7UIntNormalizedSrgb = 99
                Ayuv = 100
                Y410 = 101
                Y416 = 102
                NV12 = 103
                P010 = 104
                P016 = 105
                Opaque420 = 106
                Yuy2 = 107
                Y210 = 108
                Y216 = 109
                NV11 = 110
                AI44 = 111
                IA44 = 112
                P8 = 113
                A8P8 = 114
                B4G4R4A4UIntNormalized = 115
                P208 = 130
                V208 = 131
                V408 = 132
                SamplerFeedbackMinMipOpaque = 189
                SamplerFeedbackMipRegionUsedOpaque = 190

            class DirectXPrimitiveTopology(_Enum):
                Undefined = 0
                PointList = 1
                LineList = 2
                LineStrip = 3
                TriangleList = 4
                TriangleStrip = 5

            class Direct3D11:
                class Direct3DBindings(_Enum):
                    VertexBuffer = 0x1
                    IndexBuffer = 0x2
                    ConstantBuffer = 0x4
                    ShaderResource = 0x8
                    StreamOutput = 0x10
                    RenderTarget = 0x20
                    DepthStencil = 0x40
                    UnorderedAccess = 0x80
                    Decoder = 0x200
                    VideoEncoder = 0x400

                class Direct3DUsage(_Enum):
                    Default = 0
                    Immutable = 1
                    Dynamic = 2
                    Staging = 3

        class Display:
            class AdvancedColorKind(_Enum):
                StandardDynamicRange = 0
                WideColorGamut = 1
                HighDynamicRange = 2

            class DisplayBrightnessOverrideOptions(_Enum):
                None_ = 0x0
                UseDimmedPolicyWhenBatteryIsLow = 0x1

            class DisplayBrightnessOverrideScenario(_Enum):
                IdleBrightness = 0
                BarcodeReadingBrightness = 1
                FullBrightness = 2

            class DisplayBrightnessScenario(_Enum):
                DefaultBrightness = 0
                IdleBrightness = 1
                BarcodeReadingBrightness = 2
                FullBrightness = 3

            class DisplayColorOverrideScenario(_Enum):
                Accurate = 0

            class DisplayOrientations(_Enum):
                None_ = 0x0
                Landscape = 0x1
                Portrait = 0x2
                LandscapeFlipped = 0x4
                PortraitFlipped = 0x8

            class HdrMetadataFormat(_Enum):
                Hdr10 = 0
                Hdr10Plus = 1

            class ResolutionScale(_Enum):
                Invalid = 0
                Scale100Percent = 100
                Scale120Percent = 120
                Scale125Percent = 125
                Scale140Percent = 140
                Scale150Percent = 150
                Scale160Percent = 160
                Scale175Percent = 175
                Scale180Percent = 180
                Scale200Percent = 200
                Scale225Percent = 225
                Scale250Percent = 250
                Scale300Percent = 300
                Scale350Percent = 350
                Scale400Percent = 400
                Scale450Percent = 450
                Scale500Percent = 500

            class Core:
                class HdmiDisplayColorSpace(_Enum):
                    RgbLimited = 0
                    RgbFull = 1
                    BT2020 = 2
                    BT709 = 3

                class HdmiDisplayHdrOption(_Enum):
                    None_ = 0
                    EotfSdr = 1
                    Eotf2084 = 2
                    DolbyVisionLowLatency = 3

                class HdmiDisplayPixelEncoding(_Enum):
                    Rgb444 = 0
                    Ycc444 = 1
                    Ycc422 = 2
                    Ycc420 = 3

        class Holographic:
            class HolographicDepthReprojectionMethod(_Enum):
                DepthReprojection = 0
                AutoPlanar = 1

            class HolographicFramePresentResult(_Enum):
                Success = 0
                DeviceRemoved = 1

            class HolographicFramePresentWaitBehavior(_Enum):
                WaitForFrameToFinish = 0
                DoNotWaitForFrameToFinish = 1

            class HolographicReprojectionMode(_Enum):
                PositionAndOrientation = 0
                OrientationOnly = 1
                Disabled = 2

            class HolographicSpaceUserPresence(_Enum):
                Absent = 0
                PresentPassive = 1
                PresentActive = 2

            class HolographicViewConfigurationKind(_Enum):
                Display = 0
                PhotoVideoCamera = 1

        class Imaging:
            class BitmapAlphaMode(_Enum):
                Premultiplied = 0
                Straight = 1
                Ignore = 2

            class BitmapBufferAccessMode(_Enum):
                Read = 0
                ReadWrite = 1
                Write = 2

            class BitmapFlip(_Enum):
                None_ = 0
                Horizontal = 1
                Vertical = 2

            class BitmapInterpolationMode(_Enum):
                NearestNeighbor = 0
                Linear = 1
                Cubic = 2
                Fant = 3

            class BitmapPixelFormat(_Enum):
                Unknown = 0
                Rgba16 = 12
                Rgba8 = 30
                Gray16 = 57
                Gray8 = 62
                Bgra8 = 87
                Nv12 = 103
                P010 = 104
                Yuy2 = 107

            class BitmapRotation(_Enum):
                None_ = 0
                Clockwise90Degrees = 1
                Clockwise180Degrees = 2
                Clockwise270Degrees = 3

            class ColorManagementMode(_Enum):
                DoNotColorManage = 0
                ColorManageToSRgb = 1

            class ExifOrientationMode(_Enum):
                IgnoreExifOrientation = 0
                RespectExifOrientation = 1

            class JpegSubsamplingMode(_Enum):
                Default = 0
                Y4Cb2Cr0 = 1
                Y4Cb2Cr2 = 2
                Y4Cb4Cr4 = 3

            class PngFilterMode(_Enum):
                Automatic = 0
                None_ = 1
                Sub = 2
                Up = 3
                Average = 4
                Paeth = 5
                Adaptive = 6

            class TiffCompressionMode(_Enum):
                Automatic = 0
                None_ = 1
                Ccitt3 = 2
                Ccitt4 = 3
                Lzw = 4
                Rle = 5
                Zip = 6
                LzwhDifferencing = 7

        class Printing:
            class PrintBinding(_Enum):
                Default = 0
                NotAvailable = 1
                PrinterCustom = 2
                None_ = 3
                Bale = 4
                BindBottom = 5
                BindLeft = 6
                BindRight = 7
                BindTop = 8
                Booklet = 9
                EdgeStitchBottom = 10
                EdgeStitchLeft = 11
                EdgeStitchRight = 12
                EdgeStitchTop = 13
                Fold = 14
                JogOffset = 15
                Trim = 16

            class PrintBordering(_Enum):
                Default = 0
                NotAvailable = 1
                PrinterCustom = 2
                Bordered = 3
                Borderless = 4

            class PrintCollation(_Enum):
                Default = 0
                NotAvailable = 1
                PrinterCustom = 2
                Collated = 3
                Uncollated = 4

            class PrintColorMode(_Enum):
                Default = 0
                NotAvailable = 1
                PrinterCustom = 2
                Color = 3
                Grayscale = 4
                Monochrome = 5

            class PrintDuplex(_Enum):
                Default = 0
                NotAvailable = 1
                PrinterCustom = 2
                OneSided = 3
                TwoSidedShortEdge = 4
                TwoSidedLongEdge = 5

            class PrintHolePunch(_Enum):
                Default = 0
                NotAvailable = 1
                PrinterCustom = 2
                None_ = 3
                LeftEdge = 4
                RightEdge = 5
                TopEdge = 6
                BottomEdge = 7

            class PrintMediaSize(_Enum):
                Default = 0
                NotAvailable = 1
                PrinterCustom = 2
                BusinessCard = 3
                CreditCard = 4
                IsoA0 = 5
                IsoA1 = 6
                IsoA10 = 7
                IsoA2 = 8
                IsoA3 = 9
                IsoA3Extra = 10
                IsoA3Rotated = 11
                IsoA4 = 12
                IsoA4Extra = 13
                IsoA4Rotated = 14
                IsoA5 = 15
                IsoA5Extra = 16
                IsoA5Rotated = 17
                IsoA6 = 18
                IsoA6Rotated = 19
                IsoA7 = 20
                IsoA8 = 21
                IsoA9 = 22
                IsoB0 = 23
                IsoB1 = 24
                IsoB10 = 25
                IsoB2 = 26
                IsoB3 = 27
                IsoB4 = 28
                IsoB4Envelope = 29
                IsoB5Envelope = 30
                IsoB5Extra = 31
                IsoB7 = 32
                IsoB8 = 33
                IsoB9 = 34
                IsoC0 = 35
                IsoC1 = 36
                IsoC10 = 37
                IsoC2 = 38
                IsoC3 = 39
                IsoC3Envelope = 40
                IsoC4 = 41
                IsoC4Envelope = 42
                IsoC5 = 43
                IsoC5Envelope = 44
                IsoC6 = 45
                IsoC6C5Envelope = 46
                IsoC6Envelope = 47
                IsoC7 = 48
                IsoC8 = 49
                IsoC9 = 50
                IsoDLEnvelope = 51
                IsoDLEnvelopeRotated = 52
                IsoSRA3 = 53
                Japan2LPhoto = 54
                JapanChou3Envelope = 55
                JapanChou3EnvelopeRotated = 56
                JapanChou4Envelope = 57
                JapanChou4EnvelopeRotated = 58
                JapanDoubleHagakiPostcard = 59
                JapanDoubleHagakiPostcardRotated = 60
                JapanHagakiPostcard = 61
                JapanHagakiPostcardRotated = 62
                JapanKaku2Envelope = 63
                JapanKaku2EnvelopeRotated = 64
                JapanKaku3Envelope = 65
                JapanKaku3EnvelopeRotated = 66
                JapanLPhoto = 67
                JapanQuadrupleHagakiPostcard = 68
                JapanYou1Envelope = 69
                JapanYou2Envelope = 70
                JapanYou3Envelope = 71
                JapanYou4Envelope = 72
                JapanYou4EnvelopeRotated = 73
                JapanYou6Envelope = 74
                JapanYou6EnvelopeRotated = 75
                JisB0 = 76
                JisB1 = 77
                JisB10 = 78
                JisB2 = 79
                JisB3 = 80
                JisB4 = 81
                JisB4Rotated = 82
                JisB5 = 83
                JisB5Rotated = 84
                JisB6 = 85
                JisB6Rotated = 86
                JisB7 = 87
                JisB8 = 88
                JisB9 = 89
                NorthAmerica10x11 = 90
                NorthAmerica10x12 = 91
                NorthAmerica10x14 = 92
                NorthAmerica11x17 = 93
                NorthAmerica14x17 = 94
                NorthAmerica4x6 = 95
                NorthAmerica4x8 = 96
                NorthAmerica5x7 = 97
                NorthAmerica8x10 = 98
                NorthAmerica9x11 = 99
                NorthAmericaArchitectureASheet = 100
                NorthAmericaArchitectureBSheet = 101
                NorthAmericaArchitectureCSheet = 102
                NorthAmericaArchitectureDSheet = 103
                NorthAmericaArchitectureESheet = 104
                NorthAmericaCSheet = 105
                NorthAmericaDSheet = 106
                NorthAmericaESheet = 107
                NorthAmericaExecutive = 108
                NorthAmericaGermanLegalFanfold = 109
                NorthAmericaGermanStandardFanfold = 110
                NorthAmericaLegal = 111
                NorthAmericaLegalExtra = 112
                NorthAmericaLetter = 113
                NorthAmericaLetterExtra = 114
                NorthAmericaLetterPlus = 115
                NorthAmericaLetterRotated = 116
                NorthAmericaMonarchEnvelope = 117
                NorthAmericaNote = 118
                NorthAmericaNumber10Envelope = 119
                NorthAmericaNumber10EnvelopeRotated = 120
                NorthAmericaNumber11Envelope = 121
                NorthAmericaNumber12Envelope = 122
                NorthAmericaNumber14Envelope = 123
                NorthAmericaNumber9Envelope = 124
                NorthAmericaPersonalEnvelope = 125
                NorthAmericaQuarto = 126
                NorthAmericaStatement = 127
                NorthAmericaSuperA = 128
                NorthAmericaSuperB = 129
                NorthAmericaTabloid = 130
                NorthAmericaTabloidExtra = 131
                OtherMetricA3Plus = 132
                OtherMetricA4Plus = 133
                OtherMetricFolio = 134
                OtherMetricInviteEnvelope = 135
                OtherMetricItalianEnvelope = 136
                Prc10Envelope = 137
                Prc10EnvelopeRotated = 138
                Prc16K = 139
                Prc16KRotated = 140
                Prc1Envelope = 141
                Prc1EnvelopeRotated = 142
                Prc2Envelope = 143
                Prc2EnvelopeRotated = 144
                Prc32K = 145
                Prc32KBig = 146
                Prc32KRotated = 147
                Prc3Envelope = 148
                Prc3EnvelopeRotated = 149
                Prc4Envelope = 150
                Prc4EnvelopeRotated = 151
                Prc5Envelope = 152
                Prc5EnvelopeRotated = 153
                Prc6Envelope = 154
                Prc6EnvelopeRotated = 155
                Prc7Envelope = 156
                Prc7EnvelopeRotated = 157
                Prc8Envelope = 158
                Prc8EnvelopeRotated = 159
                Prc9Envelope = 160
                Prc9EnvelopeRotated = 161
                Roll04Inch = 162
                Roll06Inch = 163
                Roll08Inch = 164
                Roll12Inch = 165
                Roll15Inch = 166
                Roll18Inch = 167
                Roll22Inch = 168
                Roll24Inch = 169
                Roll30Inch = 170
                Roll36Inch = 171
                Roll54Inch = 172

            class PrintMediaType(_Enum):
                Default = 0
                NotAvailable = 1
                PrinterCustom = 2
                AutoSelect = 3
                Archival = 4
                BackPrintFilm = 5
                Bond = 6
                CardStock = 7
                Continuous = 8
                EnvelopePlain = 9
                EnvelopeWindow = 10
                Fabric = 11
                HighResolution = 12
                Label = 13
                MultiLayerForm = 14
                MultiPartForm = 15
                Photographic = 16
                PhotographicFilm = 17
                PhotographicGlossy = 18
                PhotographicHighGloss = 19
                PhotographicMatte = 20
                PhotographicSatin = 21
                PhotographicSemiGloss = 22
                Plain = 23
                Screen = 24
                ScreenPaged = 25
                Stationery = 26
                TabStockFull = 27
                TabStockPreCut = 28
                Transparency = 29
                TShirtTransfer = 30
                None_ = 31

            class PrintOrientation(_Enum):
                Default = 0
                NotAvailable = 1
                PrinterCustom = 2
                Portrait = 3
                PortraitFlipped = 4
                Landscape = 5
                LandscapeFlipped = 6

            class PrintQuality(_Enum):
                Default = 0
                NotAvailable = 1
                PrinterCustom = 2
                Automatic = 3
                Draft = 4
                Fax = 5
                High = 6
                Normal = 7
                Photographic = 8
                Text = 9

            class PrintStaple(_Enum):
                Default = 0
                NotAvailable = 1
                PrinterCustom = 2
                None_ = 3
                StapleTopLeft = 4
                StapleTopRight = 5
                StapleBottomLeft = 6
                StapleBottomRight = 7
                StapleDualLeft = 8
                StapleDualRight = 9
                StapleDualTop = 10
                StapleDualBottom = 11
                SaddleStitch = 12

            class PrintTaskCompletion(_Enum):
                Abandoned = 0
                Canceled = 1
                Failed = 2
                Submitted = 3

            class OptionDetails:
                class PrintOptionStates(_Enum):
                    None_ = 0x0
                    Enabled = 0x1
                    Constrained = 0x2

                class PrintOptionType(_Enum):
                    Unknown = 0
                    Number = 1
                    Text = 2
                    ItemList = 3
                    Toggle = 4

            class PrintSupport:
                class SettingsLaunchKind(_Enum):
                    JobPrintTicket = 0
                    UserDefaultPrintTicket = 1

                class WorkflowPrintTicketValidationStatus(_Enum):
                    Resolved = 0
                    Conflicting = 1
                    Invalid = 2

            class PrintTicket:
                class PrintTicketFeatureSelectionType(_Enum):
                    PickOne = 0
                    PickMany = 1

                class PrintTicketParameterDataType(_Enum):
                    Integer = 0
                    NumericString = 1
                    String = 2

                class PrintTicketValueType(_Enum):
                    Integer = 0
                    String = 1
                    Unknown = 2

            class Workflow:
                class PdlConversionHostBasedProcessingOperations(_Enum):
                    None_ = 0x0
                    PageRotation = 0x1
                    PageOrdering = 0x2
                    Copies = 0x4
                    BlankPageInsertion = 0x8

                class PrintWorkflowAttributesMergePolicy(_Enum):
                    MergePreferPrintTicketOnConflict = 0
                    MergePreferPsaOnConflict = 1
                    DoNotMergeWithPrintTicket = 2

                class PrintWorkflowJobAbortReason(_Enum):
                    JobFailed = 0
                    UserCanceled = 1

                class PrintWorkflowPdlConversionType(_Enum):
                    XpsToPdf = 0
                    XpsToPwgr = 1
                    XpsToPclm = 2

                class PrintWorkflowPrinterJobStatus(_Enum):
                    Error = 0
                    Aborted = 1
                    InProgress = 2
                    Completed = 3

                class PrintWorkflowSessionStatus(_Enum):
                    Started = 0
                    Completed = 1
                    Aborted = 2
                    Closed = 3
                    PdlDataAvailableForModification = 4

                class PrintWorkflowSubmittedStatus(_Enum):
                    Succeeded = 0
                    Canceled = 1
                    Failed = 2

                class PrintWorkflowUICompletionStatus(_Enum):
                    Completed = 0
                    LaunchFailed = 1
                    JobFailed = 2
                    UserCanceled = 3

        class Printing3D:
            class Print3DTaskCompletion(_Enum):
                Abandoned = 0
                Canceled = 1
                Failed = 2
                Slicing = 3
                Submitted = 4

            class Print3DTaskDetail(_Enum):
                Unknown = 0
                ModelExceedsPrintBed = 1
                UploadFailed = 2
                InvalidMaterialSelection = 3
                InvalidModel = 4
                ModelNotManifold = 5
                InvalidPrintTicket = 6

            class Printing3DBufferFormat(_Enum):
                Unknown = 0
                R32G32B32A32Float = 2
                R32G32B32A32UInt = 3
                R32G32B32Float = 6
                R32G32B32UInt = 7
                Printing3DDouble = 500
                Printing3DUInt = 501

            class Printing3DMeshVerificationMode(_Enum):
                FindFirstError = 0
                FindAllErrors = 1

            class Printing3DModelUnit(_Enum):
                Meter = 0
                Micron = 1
                Millimeter = 2
                Centimeter = 3
                Inch = 4
                Foot = 5

            class Printing3DObjectType(_Enum):
                Model = 0
                Support = 1
                Others = 2

            class Printing3DPackageCompression(_Enum):
                Low = 0
                Medium = 1
                High = 2

            class Printing3DTextureEdgeBehavior(_Enum):
                None_ = 0
                Wrap = 1
                Mirror = 2
                Clamp = 3

    class Management:
        class MdmAlertDataType(_Enum):
            String = 0
            Base64 = 1
            Boolean = 2
            Integer = 3

        class MdmAlertMark(_Enum):
            None_ = 0
            Fatal = 1
            Critical = 2
            Warning = 3
            Informational = 4

        class MdmSessionState(_Enum):
            NotStarted = 0
            Starting = 1
            Connecting = 2
            Communicating = 3
            AlertStatusAvailable = 4
            Retrying = 5
            Completed = 6

        class Deployment:
            class AddPackageByAppInstallerOptions(_Enum):
                None_ = 0x0
                InstallAllResources = 0x20
                ForceTargetAppShutdown = 0x40
                RequiredContentGroupOnly = 0x100
                LimitToExistingPackages = 0x200

            class DeploymentOptions(_Enum):
                None_ = 0x0
                ForceApplicationShutdown = 0x1
                DevelopmentMode = 0x2
                InstallAllResources = 0x20
                ForceTargetApplicationShutdown = 0x40
                RequiredContentGroupOnly = 0x100
                ForceUpdateFromAnyVersion = 0x40000
                RetainFilesOnFailure = 0x200000
                StageInPlace = 0x400000

            class DeploymentProgressState(_Enum):
                Queued = 0
                Processing = 1

            class PackageInstallState(_Enum):
                NotInstalled = 0
                Staged = 1
                Installed = 2
                Paused = 6

            class PackageState(_Enum):
                Normal = 0
                LicenseInvalid = 1
                Modified = 2
                Tampered = 3

            class PackageStatus(_Enum):
                OK = 0x0
                LicenseIssue = 0x1
                Modified = 0x2
                Tampered = 0x4
                Disabled = 0x8

            class PackageStubPreference(_Enum):
                Full = 0
                Stub = 1

            class PackageTypes(_Enum):
                None_ = 0x0
                Main = 0x1
                Framework = 0x2
                Resource = 0x4
                Bundle = 0x8
                Xap = 0x10
                Optional = 0x20

            class RemovalOptions(_Enum):
                None_ = 0x0
                PreserveApplicationData = 0x1000
                PreserveRoamableApplicationData = 0x80
                RemoveForAllUsers = 0x80000

            class SharedPackageContainerCreationCollisionOptions(_Enum):
                FailIfExists = 0
                MergeWithExisting = 1
                ReplaceExisting = 2

            class SharedPackageContainerOperationStatus(_Enum):
                Success = 0
                BlockedByPolicy = 1
                AlreadyExists = 2
                PackageFamilyExistsInAnotherContainer = 3
                NotFound = 4
                UnknownFailure = 5

            class StubPackageOption(_Enum):
                Default = 0
                InstallFull = 1
                InstallStub = 2
                UsePreference = 3

        class Policies:
            class NamedPolicyKind(_Enum):
                Invalid = 0
                Binary = 1
                Boolean = 2
                Int32 = 3
                Int64 = 4
                String = 5

        class Update:
            class WindowsUpdateAdministratorOptions(_Enum):
                None_ = 0x0
                RequireAdministratorApprovalForScans = 0x1
                RequireAdministratorApprovalForUpdates = 0x2
                RequireAdministratorApprovalForActions = 0x4

            class WindowsUpdateAdministratorStatus(_Enum):
                Succeeded = 0
                NoAdministratorRegistered = 1
                OtherAdministratorIsRegistered = 2

            class WindowsUpdateAttentionRequiredReason(_Enum):
                None_ = 0
                SeekerUpdate = 1
                ReadyToReboot = 2
                NeedNonMeteredNetwork = 3
                NeedUserAgreementForMeteredNetwork = 4
                NeedNetwork = 5
                NeedMoreSpace = 6
                BatterySaverEnabled = 7
                NeedUserInteraction = 8
                NeedUserAgreementForPolicy = 9
                CompatibilityError = 10
                NeedUserInteractionForEula = 11
                NeedUserInteractionForCta = 12
                Regulated = 13
                ExternalReboot = 14
                OtherUpdate = 15
                BlockedByProvider = 16
                BlockedByPostRebootFailure = 17
                UserEngaged = 18
                BlockedByBattery = 19
                Exclusivity = 20
                BlockedBySerialization = 21
                ConflictClass = 22
                BlockedByAdminApproval = 23
                BlockedByTooManyAttempts = 24
                BlockedByFailure = 25
                Demotion = 26
                BlockedByActiveHours = 27
                ScheduledForMaintenance = 28
                PolicyScheduledInstallTime = 29
                BlockedByOobe = 30
                DeferredDuringOobe = 31
                DeferredForSustainableTime = 32

        class Workplace:
            class MessagingSyncPolicy(_Enum):
                Disallowed = 0
                Allowed = 1
                Required = 2

    class Media:
        class AudioBufferAccessMode(_Enum):
            Read = 0
            ReadWrite = 1
            Write = 2

        class AudioProcessing(_Enum):
            Default = 0
            Raw = 1

        class MediaPlaybackAutoRepeatMode(_Enum):
            None_ = 0
            Track = 1
            List = 2

        class MediaPlaybackStatus(_Enum):
            Closed = 0
            Changing = 1
            Stopped = 2
            Playing = 3
            Paused = 4

        class MediaPlaybackType(_Enum):
            Unknown = 0
            Music = 1
            Video = 2
            Image = 3

        class MediaTimelineControllerState(_Enum):
            Paused = 0
            Running = 1
            Stalled = 2
            Error = 3

        class SoundLevel(_Enum):
            Muted = 0
            Low = 1
            Full = 2

        class SystemMediaTransportControlsButton(_Enum):
            Play = 0
            Pause = 1
            Stop = 2
            Record = 3
            FastForward = 4
            Rewind = 5
            Next = 6
            Previous = 7
            ChannelUp = 8
            ChannelDown = 9

        class SystemMediaTransportControlsProperty(_Enum):
            SoundLevel = 0

        class AppRecording:
            class AppRecordingSaveScreenshotOption(_Enum):
                None_ = 0
                HdrContentVisible = 1

        class Audio:
            class AudioDeviceNodeCreationStatus(_Enum):
                Success = 0
                DeviceNotAvailable = 1
                FormatNotSupported = 2
                UnknownFailure = 3
                AccessDenied = 4

            class AudioFileNodeCreationStatus(_Enum):
                Success = 0
                FileNotFound = 1
                InvalidFileType = 2
                FormatNotSupported = 3
                UnknownFailure = 4

            class AudioGraphCreationStatus(_Enum):
                Success = 0
                DeviceNotAvailable = 1
                FormatNotSupported = 2
                UnknownFailure = 3

            class AudioGraphUnrecoverableError(_Enum):
                None_ = 0
                AudioDeviceLost = 1
                AudioSessionDisconnected = 2
                UnknownFailure = 3

            class AudioNodeEmitterDecayKind(_Enum):
                Natural = 0
                Custom = 1

            class AudioNodeEmitterSettings(_Enum):
                None_ = 0x0
                DisableDoppler = 0x1

            class AudioNodeEmitterShapeKind(_Enum):
                Omnidirectional = 0
                Cone = 1

            class AudioPlaybackConnectionOpenResultStatus(_Enum):
                Success = 0
                RequestTimedOut = 1
                DeniedBySystem = 2
                UnknownFailure = 3

            class AudioPlaybackConnectionState(_Enum):
                Closed = 0
                Opened = 1

            class MediaSourceAudioInputNodeCreationStatus(_Enum):
                Success = 0
                FormatNotSupported = 1
                NetworkError = 2
                UnknownFailure = 3

            class MixedRealitySpatialAudioFormatPolicy(_Enum):
                UseMixedRealityDefaultSpatialAudioFormat = 0
                UseDeviceConfigurationDefaultSpatialAudioFormat = 1

            class QuantumSizeSelectionMode(_Enum):
                SystemDefault = 0
                LowestLatency = 1
                ClosestToDesired = 2

            class SetDefaultSpatialAudioFormatStatus(_Enum):
                Succeeded = 0
                AccessDenied = 1
                LicenseExpired = 2
                LicenseNotValidForAudioEndpoint = 3
                NotSupportedOnAudioEndpoint = 4
                UnknownError = 5

            class SpatialAudioModel(_Enum):
                ObjectBased = 0
                FoldDown = 1

        class Capture:
            class AppBroadcastCameraCaptureState(_Enum):
                Stopped = 0
                Started = 1
                Failed = 2

            class AppBroadcastCameraOverlayLocation(_Enum):
                TopLeft = 0
                TopCenter = 1
                TopRight = 2
                MiddleLeft = 3
                MiddleCenter = 4
                MiddleRight = 5
                BottomLeft = 6
                BottomCenter = 7
                BottomRight = 8

            class AppBroadcastCameraOverlaySize(_Enum):
                Small = 0
                Medium = 1
                Large = 2

            class AppBroadcastCaptureTargetType(_Enum):
                AppView = 0
                EntireDisplay = 1

            class AppBroadcastExitBroadcastModeReason(_Enum):
                NormalExit = 0
                UserCanceled = 1
                AuthorizationFail = 2
                ForegroundAppActivated = 3

            class AppBroadcastMicrophoneCaptureState(_Enum):
                Stopped = 0
                Started = 1
                Failed = 2

            class AppBroadcastPlugInState(_Enum):
                Unknown = 0
                Initialized = 1
                MicrosoftSignInRequired = 2
                OAuthSignInRequired = 3
                ProviderSignInRequired = 4
                InBandwidthTest = 5
                ReadyToBroadcast = 6

            class AppBroadcastPreviewState(_Enum):
                Started = 0
                Stopped = 1
                Failed = 2

            class AppBroadcastSignInResult(_Enum):
                Success = 0
                AuthenticationFailed = 1
                Unauthorized = 2
                ServiceUnavailable = 3
                Unknown = 4

            class AppBroadcastSignInState(_Enum):
                NotSignedIn = 0
                MicrosoftSignInInProgress = 1
                MicrosoftSignInComplete = 2
                OAuthSignInInProgress = 3
                OAuthSignInComplete = 4

            class AppBroadcastStreamState(_Enum):
                Initializing = 0
                StreamReady = 1
                Started = 2
                Paused = 3
                Terminated = 4

            class AppBroadcastTerminationReason(_Enum):
                NormalTermination = 0
                LostConnectionToService = 1
                NoNetworkConnectivity = 2
                ServiceAbort = 3
                ServiceError = 4
                ServiceUnavailable = 5
                InternalError = 6
                UnsupportedFormat = 7
                BackgroundTaskTerminated = 8
                BackgroundTaskUnresponsive = 9

            class AppBroadcastVideoEncodingBitrateMode(_Enum):
                Custom = 0
                Auto = 1

            class AppBroadcastVideoEncodingResolutionMode(_Enum):
                Custom = 0
                Auto = 1

            class AppCaptureHistoricalBufferLengthUnit(_Enum):
                Megabytes = 0
                Seconds = 1

            class AppCaptureMetadataPriority(_Enum):
                Informational = 0
                Important = 1

            class AppCaptureMicrophoneCaptureState(_Enum):
                Stopped = 0
                Started = 1
                Failed = 2

            class AppCaptureRecordingState(_Enum):
                InProgress = 0
                Completed = 1
                Failed = 2

            class AppCaptureVideoEncodingBitrateMode(_Enum):
                Custom = 0
                High = 1
                Standard = 2

            class AppCaptureVideoEncodingFrameRateMode(_Enum):
                Standard = 0
                High = 1

            class AppCaptureVideoEncodingResolutionMode(_Enum):
                Custom = 0
                High = 1
                Standard = 2

            class CameraCaptureUIMaxPhotoResolution(_Enum):
                HighestAvailable = 0
                VerySmallQvga = 1
                SmallVga = 2
                MediumXga = 3
                Large3M = 4
                VeryLarge5M = 5

            class CameraCaptureUIMaxVideoResolution(_Enum):
                HighestAvailable = 0
                LowDefinition = 1
                StandardDefinition = 2
                HighDefinition = 3

            class CameraCaptureUIMode(_Enum):
                PhotoOrVideo = 0
                Photo = 1
                Video = 2

            class CameraCaptureUIPhotoFormat(_Enum):
                Jpeg = 0
                Png = 1
                JpegXR = 2

            class CameraCaptureUIVideoFormat(_Enum):
                Mp4 = 0
                Wmv = 1

            class ForegroundActivationArgument(_Enum):
                SignInRequired = 0
                MoreSettings = 1

            class GameBarCommand(_Enum):
                OpenGameBar = 0
                RecordHistoricalBuffer = 1
                ToggleStartStopRecord = 2
                StartRecord = 3
                StopRecord = 4
                TakeScreenshot = 5
                StartBroadcast = 6
                StopBroadcast = 7
                PauseBroadcast = 8
                ResumeBroadcast = 9
                ToggleStartStopBroadcast = 10
                ToggleMicrophoneCapture = 11
                ToggleCameraCapture = 12
                ToggleRecordingIndicator = 13

            class GameBarCommandOrigin(_Enum):
                ShortcutKey = 0
                Cortana = 1
                AppCommand = 2

            class GameBarServicesDisplayMode(_Enum):
                Windowed = 0
                FullScreenExclusive = 1

            class GameBarTargetCapturePolicy(_Enum):
                EnabledBySystem = 0
                EnabledByUser = 1
                NotEnabled = 2
                ProhibitedBySystem = 3
                ProhibitedByPublisher = 4

            class KnownVideoProfile(_Enum):
                VideoRecording = 0
                HighQualityPhoto = 1
                BalancedVideoAndPhoto = 2
                VideoConferencing = 3
                PhotoSequence = 4
                HighFrameRate = 5
                VariablePhotoSequence = 6
                HdrWithWcgVideo = 7
                HdrWithWcgPhoto = 8
                VideoHdr8 = 9
                CompressedCamera = 10

            class MediaCaptureDeviceExclusiveControlReleaseMode(_Enum):
                OnDispose = 0
                OnAllStreamsStopped = 1

            class MediaCaptureDeviceExclusiveControlStatus(_Enum):
                ExclusiveControlAvailable = 0
                SharedReadOnlyAvailable = 1

            class MediaCaptureMemoryPreference(_Enum):
                Auto = 0
                Cpu = 1

            class MediaCaptureSharingMode(_Enum):
                ExclusiveControl = 0
                SharedReadOnly = 1

            class MediaCaptureThermalStatus(_Enum):
                Normal = 0
                Overheated = 1

            class MediaCategory(_Enum):
                Other = 0
                Communications = 1
                Media = 2
                GameChat = 3
                Speech = 4
                FarFieldSpeech = 5
                UniformSpeech = 6
                VoiceTyping = 7

            class MediaStreamType(_Enum):
                VideoPreview = 0
                VideoRecord = 1
                Audio = 2
                Photo = 3
                Metadata = 4

            class PhotoCaptureSource(_Enum):
                Auto = 0
                VideoPreview = 1
                Photo = 2

            class PowerlineFrequency(_Enum):
                Disabled = 0
                FiftyHertz = 1
                SixtyHertz = 2
                Auto = 3

            class StreamingCaptureMode(_Enum):
                AudioAndVideo = 0
                Audio = 1
                Video = 2

            class VideoDeviceCharacteristic(_Enum):
                AllStreamsIndependent = 0
                PreviewRecordStreamsIdentical = 1
                PreviewPhotoStreamsIdentical = 2
                RecordPhotoStreamsIdentical = 3
                AllStreamsIdentical = 4

            class VideoRotation(_Enum):
                None_ = 0
                Clockwise90Degrees = 1
                Clockwise180Degrees = 2
                Clockwise270Degrees = 3

            class Frames:
                class MediaFrameReaderAcquisitionMode(_Enum):
                    Realtime = 0
                    Buffered = 1

                class MediaFrameReaderStartStatus(_Enum):
                    Success = 0
                    UnknownFailure = 1
                    DeviceNotAvailable = 2
                    OutputFormatNotSupported = 3
                    ExclusiveControlNotAvailable = 4

                class MediaFrameSourceGetPropertyStatus(_Enum):
                    Success = 0
                    UnknownFailure = 1
                    NotSupported = 2
                    DeviceNotAvailable = 3
                    MaxPropertyValueSizeTooSmall = 4
                    MaxPropertyValueSizeRequired = 5

                class MediaFrameSourceKind(_Enum):
                    Custom = 0
                    Color = 1
                    Infrared = 2
                    Depth = 3
                    Audio = 4
                    Image = 5
                    Metadata = 6

                class MediaFrameSourceSetPropertyStatus(_Enum):
                    Success = 0
                    UnknownFailure = 1
                    NotSupported = 2
                    InvalidValue = 3
                    DeviceNotAvailable = 4
                    NotInControl = 5

                class MultiSourceMediaFrameReaderStartStatus(_Enum):
                    Success = 0
                    NotSupported = 1
                    InsufficientResources = 2
                    DeviceNotAvailable = 3
                    UnknownFailure = 4

        class Casting:
            class CastingConnectionErrorStatus(_Enum):
                Succeeded = 0
                DeviceDidNotRespond = 1
                DeviceError = 2
                DeviceLocked = 3
                ProtectedPlaybackFailed = 4
                InvalidCastingSource = 5
                Unknown = 6

            class CastingConnectionState(_Enum):
                Disconnected = 0
                Connected = 1
                Rendering = 2
                Disconnecting = 3
                Connecting = 4

            class CastingPlaybackTypes(_Enum):
                None_ = 0x0
                Audio = 0x1
                Video = 0x2
                Picture = 0x4

        class ClosedCaptioning:
            class ClosedCaptionColor(_Enum):
                Default = 0
                White = 1
                Black = 2
                Red = 3
                Green = 4
                Blue = 5
                Yellow = 6
                Magenta = 7
                Cyan = 8

            class ClosedCaptionEdgeEffect(_Enum):
                Default = 0
                None_ = 1
                Raised = 2
                Depressed = 3
                Uniform = 4
                DropShadow = 5

            class ClosedCaptionOpacity(_Enum):
                Default = 0
                OneHundredPercent = 1
                SeventyFivePercent = 2
                TwentyFivePercent = 3
                ZeroPercent = 4

            class ClosedCaptionSize(_Enum):
                Default = 0
                FiftyPercent = 1
                OneHundredPercent = 2
                OneHundredFiftyPercent = 3
                TwoHundredPercent = 4

            class ClosedCaptionStyle(_Enum):
                Default = 0
                MonospacedWithSerifs = 1
                ProportionalWithSerifs = 2
                MonospacedWithoutSerifs = 3
                ProportionalWithoutSerifs = 4
                Casual = 5
                Cursive = 6
                SmallCapitals = 7

        class ContentRestrictions:
            class ContentAccessRestrictionLevel(_Enum):
                Allow = 0
                Warn = 1
                Block = 2
                Hide = 3

            class RatedContentCategory(_Enum):
                General = 0
                Application = 1
                Game = 2
                Movie = 3
                Television = 4
                Music = 5

        class Control:
            class GlobalSystemMediaTransportControlsSessionPlaybackStatus(_Enum):
                Closed = 0
                Opened = 1
                Changing = 2
                Stopped = 3
                Playing = 4
                Paused = 5

        class Core:
            class AudioDecoderDegradation(_Enum):
                None_ = 0
                DownmixTo2Channels = 1
                DownmixTo6Channels = 2
                DownmixTo8Channels = 3

            class AudioDecoderDegradationReason(_Enum):
                None_ = 0
                LicensingRequirement = 1
                SpatialAudioNotSupported = 2

            class CodecCategory(_Enum):
                Encoder = 0
                Decoder = 1

            class CodecKind(_Enum):
                Audio = 0
                Video = 1

            class FaceDetectionMode(_Enum):
                HighPerformance = 0
                Balanced = 1
                HighQuality = 2

            class MediaDecoderStatus(_Enum):
                FullySupported = 0
                UnsupportedSubtype = 1
                UnsupportedEncoderProperties = 2
                Degraded = 3

            class MediaSourceState(_Enum):
                Initial = 0
                Opening = 1
                Opened = 2
                Failed = 3
                Closed = 4

            class MediaSourceStatus(_Enum):
                FullySupported = 0
                Unknown = 1

            class MediaStreamSourceClosedReason(_Enum):
                Done = 0
                UnknownError = 1
                AppReportedError = 2
                UnsupportedProtectionSystem = 3
                ProtectionSystemFailure = 4
                UnsupportedEncodingFormat = 5
                MissingSampleRequestedEventHandler = 6

            class MediaStreamSourceErrorStatus(_Enum):
                Other = 0
                OutOfMemory = 1
                FailedToOpenFile = 2
                FailedToConnectToServer = 3
                ConnectionToServerLost = 4
                UnspecifiedNetworkError = 5
                DecodeError = 6
                UnsupportedMediaFormat = 7

            class MediaTrackKind(_Enum):
                Audio = 0
                Video = 1
                TimedMetadata = 2

            class MseAppendMode(_Enum):
                Segments = 0
                Sequence = 1

            class MseEndOfStreamStatus(_Enum):
                Success = 0
                NetworkError = 1
                DecodeError = 2
                UnknownError = 3

            class MseReadyState(_Enum):
                Closed = 0
                Open = 1
                Ended = 2

            class SceneAnalysisRecommendation(_Enum):
                Standard = 0
                Hdr = 1
                LowLight = 2

            class TimedMetadataKind(_Enum):
                Caption = 0
                Chapter = 1
                Custom = 2
                Data = 3
                Description = 4
                Subtitle = 5
                ImageSubtitle = 6
                Speech = 7

            class TimedMetadataTrackErrorCode(_Enum):
                None_ = 0
                DataFormatError = 1
                NetworkError = 2
                InternalError = 3

            class TimedTextBoutenPosition(_Enum):
                Before = 0
                After = 1
                Outside = 2

            class TimedTextBoutenType(_Enum):
                None_ = 0
                Auto = 1
                FilledCircle = 2
                OpenCircle = 3
                FilledDot = 4
                OpenDot = 5
                FilledSesame = 6
                OpenSesame = 7

            class TimedTextDisplayAlignment(_Enum):
                Before = 0
                After = 1
                Center = 2

            class TimedTextFlowDirection(_Enum):
                LeftToRight = 0
                RightToLeft = 1

            class TimedTextFontStyle(_Enum):
                Normal = 0
                Oblique = 1
                Italic = 2

            class TimedTextLineAlignment(_Enum):
                Start = 0
                End = 1
                Center = 2

            class TimedTextRubyAlign(_Enum):
                Center = 0
                Start = 1
                End = 2
                SpaceAround = 3
                SpaceBetween = 4
                WithBase = 5

            class TimedTextRubyPosition(_Enum):
                Before = 0
                After = 1
                Outside = 2

            class TimedTextRubyReserve(_Enum):
                None_ = 0
                Before = 1
                After = 2
                Both = 3
                Outside = 4

            class TimedTextScrollMode(_Enum):
                Popon = 0
                Rollup = 1

            class TimedTextUnit(_Enum):
                Pixels = 0
                Percentage = 1

            class TimedTextWeight(_Enum):
                Normal = 400
                Bold = 700

            class TimedTextWrapping(_Enum):
                NoWrap = 0
                Wrap = 1

            class TimedTextWritingMode(_Enum):
                LeftRightTopBottom = 0
                RightLeftTopBottom = 1
                TopBottomRightLeft = 2
                TopBottomLeftRight = 3
                LeftRight = 4
                RightLeft = 5
                TopBottom = 6

            class VideoStabilizationEffectEnabledChangedReason(_Enum):
                Programmatic = 0
                PixelRateTooHigh = 1
                RunningSlowly = 2

        class Devices:
            class AdvancedPhotoMode(_Enum):
                Auto = 0
                Standard = 1
                Hdr = 2
                LowLight = 3

            class AudioDeviceRole(_Enum):
                Default = 0
                Communications = 1

            class AutoFocusRange(_Enum):
                FullRange = 0
                Macro = 1
                Normal = 2

            class CameraOcclusionKind(_Enum):
                Lid = 0
                CameraHardware = 1

            class CameraStreamState(_Enum):
                NotStreaming = 0
                Streaming = 1
                BlockedForPrivacy = 2
                Shutdown = 3

            class CaptureSceneMode(_Enum):
                Auto = 0
                Manual = 1
                Macro = 2
                Portrait = 3
                Sport = 4
                Snow = 5
                Night = 6
                Beach = 7
                Sunset = 8
                Candlelight = 9
                Landscape = 10
                NightPortrait = 11
                Backlit = 12

            class CaptureUse(_Enum):
                None_ = 0
                Photo = 1
                Video = 2

            class ColorTemperaturePreset(_Enum):
                Auto = 0
                Manual = 1
                Cloudy = 2
                Daylight = 3
                Flash = 4
                Fluorescent = 5
                Tungsten = 6
                Candlelight = 7

            class DigitalWindowMode(_Enum):
                Off = 0
                On = 1
                Auto = 2

            class FocusMode(_Enum):
                Auto = 0
                Single = 1
                Continuous = 2
                Manual = 3

            class FocusPreset(_Enum):
                Auto = 0
                Manual = 1
                AutoMacro = 2
                AutoNormal = 3
                AutoInfinity = 4
                AutoHyperfocal = 5

            class HdrVideoMode(_Enum):
                Off = 0
                On = 1
                Auto = 2

            class InfraredTorchMode(_Enum):
                Off = 0
                On = 1
                AlternatingFrameIllumination = 2

            class IsoSpeedPreset(_Enum):
                Auto = 0
                Iso50 = 1
                Iso80 = 2
                Iso100 = 3
                Iso200 = 4
                Iso400 = 5
                Iso800 = 6
                Iso1600 = 7
                Iso3200 = 8
                Iso6400 = 9
                Iso12800 = 10
                Iso25600 = 11

            class ManualFocusDistance(_Enum):
                Infinity = 0
                Hyperfocal = 1
                Nearest = 2

            class MediaCaptureFocusState(_Enum):
                Uninitialized = 0
                Lost = 1
                Searching = 2
                Focused = 3
                Failed = 4

            class MediaCaptureOptimization(_Enum):
                Default = 0
                Quality = 1
                Latency = 2
                Power = 3
                LatencyThenQuality = 4
                LatencyThenPower = 5
                PowerAndQuality = 6

            class MediaCapturePauseBehavior(_Enum):
                RetainHardwareResources = 0
                ReleaseHardwareResources = 1

            class OpticalImageStabilizationMode(_Enum):
                Off = 0
                On = 1
                Auto = 2

            class RegionOfInterestType(_Enum):
                Unknown = 0
                Face = 1

            class SendCommandStatus(_Enum):
                Success = 0
                DeviceNotAvailable = 1

            class TelephonyKey(_Enum):
                D0 = 0
                D1 = 1
                D2 = 2
                D3 = 3
                D4 = 4
                D5 = 5
                D6 = 6
                D7 = 7
                D8 = 8
                D9 = 9
                Star = 10
                Pound = 11
                A = 12
                B = 13
                C = 14
                D = 15

            class VideoDeviceControllerGetDevicePropertyStatus(_Enum):
                Success = 0
                UnknownFailure = 1
                BufferTooSmall = 2
                NotSupported = 3
                DeviceNotAvailable = 4
                MaxPropertyValueSizeTooSmall = 5
                MaxPropertyValueSizeRequired = 6

            class VideoDeviceControllerSetDevicePropertyStatus(_Enum):
                Success = 0
                UnknownFailure = 1
                NotSupported = 2
                InvalidValue = 3
                DeviceNotAvailable = 4
                NotInControl = 5

            class VideoTemporalDenoisingMode(_Enum):
                Off = 0
                On = 1
                Auto = 2

            class ZoomTransitionMode(_Enum):
                Auto = 0
                Direct = 1
                Smooth = 2

            class Core:
                class FrameFlashMode(_Enum):
                    Disable = 0
                    Enable = 1
                    Global = 2

        class DialProtocol:
            class DialAppLaunchResult(_Enum):
                Launched = 0
                FailedToLaunch = 1
                NotFound = 2
                NetworkFailure = 3

            class DialAppState(_Enum):
                Unknown = 0
                Stopped = 1
                Running = 2
                NetworkFailure = 3

            class DialAppStopResult(_Enum):
                Stopped = 0
                StopFailed = 1
                OperationNotSupported = 2
                NetworkFailure = 3

            class DialDeviceDisplayStatus(_Enum):
                None_ = 0
                Connecting = 1
                Connected = 2
                Disconnecting = 3
                Disconnected = 4
                Error = 5

        class Editing:
            class MediaTrimmingPreference(_Enum):
                Fast = 0
                Precise = 1

            class VideoFramePrecision(_Enum):
                NearestFrame = 0
                NearestKeyFrame = 1

        class Effects:
            class AudioEffectType(_Enum):
                Other = 0
                AcousticEchoCancellation = 1
                NoiseSuppression = 2
                AutomaticGainControl = 3
                BeamForming = 4
                ConstantToneRemoval = 5
                Equalizer = 6
                LoudnessEqualizer = 7
                BassBoost = 8
                VirtualSurround = 9
                VirtualHeadphones = 10
                SpeakerFill = 11
                RoomCorrection = 12
                BassManagement = 13
                EnvironmentalEffects = 14
                SpeakerProtection = 15
                SpeakerCompensation = 16
                DynamicRangeCompression = 17
                FarFieldBeamForming = 18
                DeepNoiseSuppression = 19

            class MediaEffectClosedReason(_Enum):
                Done = 0
                UnknownError = 1
                UnsupportedEncodingFormat = 2
                EffectCurrentlyUnloaded = 3

            class MediaMemoryTypes(_Enum):
                Gpu = 0
                Cpu = 1
                GpuAndCpu = 2

        class Import:
            class PhotoImportAccessMode(_Enum):
                ReadWrite = 0
                ReadOnly = 1
                ReadAndDelete = 2

            class PhotoImportConnectionTransport(_Enum):
                Unknown = 0
                Usb = 1
                IP = 2
                Bluetooth = 3

            class PhotoImportContentType(_Enum):
                Unknown = 0
                Image = 1
                Video = 2

            class PhotoImportContentTypeFilter(_Enum):
                OnlyImages = 0
                OnlyVideos = 1
                ImagesAndVideos = 2
                ImagesAndVideosFromCameraRoll = 3

            class PhotoImportImportMode(_Enum):
                ImportEverything = 0
                IgnoreSidecars = 1
                IgnoreSiblings = 2
                IgnoreSidecarsAndSiblings = 3

            class PhotoImportItemSelectionMode(_Enum):
                SelectAll = 0
                SelectNone = 1
                SelectNew = 2

            class PhotoImportPowerSource(_Enum):
                Unknown = 0
                Battery = 1
                External = 2

            class PhotoImportSourceType(_Enum):
                Generic = 0
                Camera = 1
                MediaPlayer = 2
                Phone = 3
                Video = 4
                PersonalInfoManager = 5
                AudioRecorder = 6

            class PhotoImportStage(_Enum):
                NotStarted = 0
                FindingItems = 1
                ImportingItems = 2
                DeletingImportedItemsFromSource = 3

            class PhotoImportStorageMediumType(_Enum):
                Undefined = 0
                Fixed = 1
                Removable = 2

            class PhotoImportSubfolderCreationMode(_Enum):
                DoNotCreateSubfolders = 0
                CreateSubfoldersFromFileDate = 1
                CreateSubfoldersFromExifDate = 2
                KeepOriginalFolderStructure = 3

            class PhotoImportSubfolderDateFormat(_Enum):
                Year = 0
                YearMonth = 1
                YearMonthDay = 2

        class MediaProperties:
            class AudioEncodingQuality(_Enum):
                Auto = 0
                High = 1
                Medium = 2
                Low = 3

            class MediaMirroringOptions(_Enum):
                None_ = 0x0
                Horizontal = 0x1
                Vertical = 0x2

            class MediaPixelFormat(_Enum):
                Nv12 = 0
                Bgra8 = 1
                P010 = 2

            class MediaRotation(_Enum):
                None_ = 0
                Clockwise90Degrees = 1
                Clockwise180Degrees = 2
                Clockwise270Degrees = 3

            class MediaThumbnailFormat(_Enum):
                Bmp = 0
                Bgra8 = 1

            class SphericalVideoFrameFormat(_Enum):
                None_ = 0
                Unsupported = 1
                Equirectangular = 2

            class StereoscopicVideoPackingMode(_Enum):
                None_ = 0
                SideBySide = 1
                TopBottom = 2

            class VideoEncodingQuality(_Enum):
                Auto = 0
                HD1080p = 1
                HD720p = 2
                Wvga = 3
                Ntsc = 4
                Pal = 5
                Vga = 6
                Qvga = 7
                Uhd2160p = 8
                Uhd4320p = 9

        class Miracast:
            class MiracastReceiverApplySettingsStatus(_Enum):
                Success = 0
                UnknownFailure = 1
                MiracastNotSupported = 2
                AccessDenied = 3
                FriendlyNameTooLong = 4
                ModelNameTooLong = 5
                ModelNumberTooLong = 6
                InvalidSettings = 7

            class MiracastReceiverAuthorizationMethod(_Enum):
                None_ = 0
                ConfirmConnection = 1
                PinDisplayIfRequested = 2
                PinDisplayRequired = 3

            class MiracastReceiverDisconnectReason(_Enum):
                Finished = 0
                AppSpecificError = 1
                ConnectionNotAccepted = 2
                DisconnectedByUser = 3
                FailedToStartStreaming = 4
                MediaDecodingError = 5
                MediaStreamingError = 6
                MediaDecryptionError = 7

            class MiracastReceiverGameControllerDeviceUsageMode(_Enum):
                AsGameController = 0
                AsMouseAndKeyboard = 1

            class MiracastReceiverListeningStatus(_Enum):
                NotListening = 0
                Listening = 1
                ConnectionPending = 2
                Connected = 3
                DisabledByPolicy = 4
                TemporarilyDisabled = 5

            class MiracastReceiverSessionStartStatus(_Enum):
                Success = 0
                UnknownFailure = 1
                MiracastNotSupported = 2
                AccessDenied = 3

            class MiracastReceiverWiFiStatus(_Enum):
                MiracastSupportUndetermined = 0
                MiracastNotSupported = 1
                MiracastSupportNotOptimized = 2
                MiracastSupported = 3

            class MiracastTransmitterAuthorizationStatus(_Enum):
                Undecided = 0
                Allowed = 1
                AlwaysPrompt = 2
                Blocked = 3

        class Playback:
            class AutoLoadedDisplayPropertyKind(_Enum):
                None_ = 0
                MusicOrVideo = 1
                Music = 2
                Video = 3

            class FailedMediaStreamKind(_Enum):
                Unknown = 0
                Audio = 1
                Video = 2

            class MediaBreakInsertionMethod(_Enum):
                Interrupt = 0
                Replace = 1

            class MediaCommandEnablingRule(_Enum):
                Auto = 0
                Always = 1
                Never = 2

            class MediaPlaybackItemChangedReason(_Enum):
                InitialItem = 0
                EndOfStream = 1
                Error = 2
                AppRequested = 3

            class MediaPlaybackItemErrorCode(_Enum):
                None_ = 0
                Aborted = 1
                NetworkError = 2
                DecodeError = 3
                SourceNotSupportedError = 4
                EncryptionError = 5

            class MediaPlaybackSessionVideoConstrictionReason(_Enum):
                None_ = 0
                VirtualMachine = 1
                UnsupportedDisplayAdapter = 2
                UnsignedDriver = 3
                FrameServerEnabled = 4
                OutputProtectionFailed = 5
                Unknown = 6

            class MediaPlaybackState(_Enum):
                None_ = 0
                Opening = 1
                Buffering = 2
                Playing = 3
                Paused = 4

            class MediaPlayerAudioCategory(_Enum):
                Other = 0
                Communications = 3
                Alerts = 4
                SoundEffects = 5
                GameEffects = 6
                GameMedia = 7
                GameChat = 8
                Speech = 9
                Movie = 10
                Media = 11

            class MediaPlayerAudioDeviceType(_Enum):
                Console = 0
                Multimedia = 1
                Communications = 2

            class MediaPlayerError(_Enum):
                Unknown = 0
                Aborted = 1
                NetworkError = 2
                DecodingError = 3
                SourceNotSupported = 4

            class MediaPlayerState(_Enum):
                Closed = 0
                Opening = 1
                Buffering = 2
                Playing = 3
                Paused = 4
                Stopped = 5

            class SphericalVideoProjectionMode(_Enum):
                Spherical = 0
                Flat = 1

            class StereoscopicVideoRenderMode(_Enum):
                Mono = 0
                Stereo = 1

            class TimedMetadataTrackPresentationMode(_Enum):
                Disabled = 0
                Hidden = 1
                ApplicationPresented = 2
                PlatformPresented = 3

        class Playlists:
            class PlaylistFormat(_Enum):
                WindowsMedia = 0
                Zune = 1
                M3u = 2

        class PlayTo:
            class PlayToConnectionError(_Enum):
                None_ = 0
                DeviceNotResponding = 1
                DeviceError = 2
                DeviceLocked = 3
                ProtectedPlaybackFailed = 4

            class PlayToConnectionState(_Enum):
                Disconnected = 0
                Connected = 1
                Rendering = 2

        class Protection:
            class GraphicsTrustStatus(_Enum):
                TrustNotRequired = 0
                TrustEstablished = 1
                EnvironmentNotSupported = 2
                DriverNotSupported = 3
                DriverSigningFailure = 4
                UnknownFailure = 5

            class HdcpProtection(_Enum):
                Off = 0
                On = 1
                OnWithTypeEnforcement = 2

            class HdcpSetProtectionResult(_Enum):
                Success = 0
                TimedOut = 1
                NotSupported = 2
                UnknownFailure = 3

            class ProtectionCapabilityResult(_Enum):
                NotSupported = 0
                Maybe = 1
                Probably = 2

            class RenewalStatus(_Enum):
                NotStarted = 0
                UpdatesInProgress = 1
                UserCancelled = 2
                AppComponentsMayNeedUpdating = 3
                NoComponentsFound = 4

            class RevocationAndRenewalReasons(_Enum):
                UserModeComponentLoad = 0x1
                KernelModeComponentLoad = 0x2
                AppComponent = 0x4
                GlobalRevocationListLoadFailed = 0x10
                InvalidGlobalRevocationListSignature = 0x20
                GlobalRevocationListAbsent = 0x1000
                ComponentRevoked = 0x2000
                InvalidComponentCertificateExtendedKeyUse = 0x4000
                ComponentCertificateRevoked = 0x8000
                InvalidComponentCertificateRoot = 0x10000
                ComponentHighSecurityCertificateRevoked = 0x20000
                ComponentLowSecurityCertificateRevoked = 0x40000
                BootDriverVerificationFailed = 0x100000
                ComponentSignedWithTestCertificate = 0x1000000
                EncryptionFailure = 0x10000000

            class PlayReady:
                class NDCertificateFeature(_Enum):
                    Transmitter = 1
                    Receiver = 2
                    SharedCertificate = 3
                    SecureClock = 4
                    AntiRollBackClock = 5
                    CRLS = 9
                    PlayReady3Features = 13

                class NDCertificatePlatformID(_Enum):
                    Windows = 0
                    OSX = 1
                    WindowsOnARM = 2
                    WindowsMobile7 = 5
                    iOSOnARM = 6
                    XBoxOnPPC = 7
                    WindowsPhone8OnARM = 8
                    WindowsPhone8OnX86 = 9
                    XboxOne = 10
                    AndroidOnARM = 11
                    WindowsPhone81OnARM = 12
                    WindowsPhone81OnX86 = 13

                class NDCertificateType(_Enum):
                    Unknown = 0
                    PC = 1
                    Device = 2
                    Domain = 3
                    Issuer = 4
                    CrlSigner = 5
                    Service = 6
                    Silverlight = 7
                    Application = 8
                    Metering = 9
                    KeyFileSigner = 10
                    Server = 11
                    LicenseSigner = 12

                class NDClosedCaptionFormat(_Enum):
                    ATSC = 0
                    SCTE20 = 1
                    Unknown = 2

                class NDContentIDType(_Enum):
                    KeyID = 1
                    PlayReadyObject = 2
                    Custom = 3

                class NDMediaStreamType(_Enum):
                    Audio = 1
                    Video = 2

                class NDProximityDetectionType(_Enum):
                    UDP = 1
                    TCP = 2
                    TransportAgnostic = 4

                class NDStartAsyncOptions(_Enum):
                    MutualAuthentication = 1
                    WaitForLicenseDescriptor = 2

                class PlayReadyDecryptorSetup(_Enum):
                    Uninitialized = 0
                    OnDemand = 1

                class PlayReadyEncryptionAlgorithm(_Enum):
                    Unprotected = 0
                    Aes128Ctr = 1
                    Cocktail = 4
                    Aes128Cbc = 5
                    Unspecified = 65535
                    Uninitialized = 2147483647

                class PlayReadyHardwareDRMFeatures(_Enum):
                    HardwareDRM = 1
                    HEVC = 2
                    Aes128Cbc = 3

                class PlayReadyITADataFormat(_Enum):
                    SerializedProperties = 0
                    SerializedProperties_WithContentProtectionWrapper = 1

        class Render:
            class AudioRenderCategory(_Enum):
                Other = 0
                ForegroundOnlyMedia = 1
                BackgroundCapableMedia = 2
                Communications = 3
                Alerts = 4
                SoundEffects = 5
                GameEffects = 6
                GameMedia = 7
                GameChat = 8
                Speech = 9
                Movie = 10
                Media = 11

        class SpeechRecognition:
            class SpeechContinuousRecognitionMode(_Enum):
                Default = 0
                PauseOnRecognition = 1

            class SpeechRecognitionAudioProblem(_Enum):
                None_ = 0
                TooNoisy = 1
                NoSignal = 2
                TooLoud = 3
                TooQuiet = 4
                TooFast = 5
                TooSlow = 6

            class SpeechRecognitionConfidence(_Enum):
                High = 0
                Medium = 1
                Low = 2
                Rejected = 3

            class SpeechRecognitionConstraintProbability(_Enum):
                Default = 0
                Min = 1
                Max = 2

            class SpeechRecognitionConstraintType(_Enum):
                Topic = 0
                List = 1
                Grammar = 2
                VoiceCommandDefinition = 3

            class SpeechRecognitionResultStatus(_Enum):
                Success = 0
                TopicLanguageNotSupported = 1
                GrammarLanguageMismatch = 2
                GrammarCompilationFailure = 3
                AudioQualityFailure = 4
                UserCanceled = 5
                Unknown = 6
                TimeoutExceeded = 7
                PauseLimitExceeded = 8
                NetworkFailure = 9
                MicrophoneUnavailable = 10

            class SpeechRecognitionScenario(_Enum):
                WebSearch = 0
                Dictation = 1
                FormFilling = 2

            class SpeechRecognizerState(_Enum):
                Idle = 0
                Capturing = 1
                Processing = 2
                SoundStarted = 3
                SoundEnded = 4
                SpeechDetected = 5
                Paused = 6

        class SpeechSynthesis:
            class SpeechAppendedSilence(_Enum):
                Default = 0
                Min = 1

            class SpeechPunctuationSilence(_Enum):
                Default = 0
                Min = 1

            class VoiceGender(_Enum):
                Male = 0
                Female = 1

        class Streaming:
            class ConnectionStatus(_Enum):
                Online = 0
                Offline = 1
                Sleeping = 2

            class DeviceTypes(_Enum):
                Unknown = 0x0
                DigitalMediaRenderer = 0x1
                DigitalMediaServer = 0x2
                DigitalMediaPlayer = 0x4

            class TransportState(_Enum):
                Unknown = 0
                Stopped = 1
                Playing = 2
                Transitioning = 3
                Paused = 4
                Recording = 5
                NoMediaPresent = 6
                Last = 7

            class TransportStatus(_Enum):
                Unknown = 0
                Ok = 1
                ErrorOccurred = 2
                Last = 3

            class Adaptive:
                class AdaptiveMediaSourceCreationStatus(_Enum):
                    Success = 0
                    ManifestDownloadFailure = 1
                    ManifestParseFailure = 2
                    UnsupportedManifestContentType = 3
                    UnsupportedManifestVersion = 4
                    UnsupportedManifestProfile = 5
                    UnknownFailure = 6

                class AdaptiveMediaSourceDiagnosticType(_Enum):
                    ManifestUnchangedUponReload = 0
                    ManifestMismatchUponReload = 1
                    ManifestSignaledEndOfLiveEventUponReload = 2
                    MediaSegmentSkipped = 3
                    ResourceNotFound = 4
                    ResourceTimedOut = 5
                    ResourceParsingError = 6
                    BitrateDisabled = 7
                    FatalMediaSourceError = 8

                class AdaptiveMediaSourceDownloadBitrateChangedReason(_Enum):
                    SufficientInboundBitsPerSecond = 0
                    InsufficientInboundBitsPerSecond = 1
                    LowBufferLevel = 2
                    PositionChanged = 3
                    TrackSelectionChanged = 4
                    DesiredBitratesChanged = 5
                    ErrorInPreviousBitrate = 6

                class AdaptiveMediaSourceResourceType(_Enum):
                    Manifest = 0
                    InitializationSegment = 1
                    MediaSegment = 2
                    Key = 3
                    InitializationVector = 4
                    MediaSegmentIndex = 5

        class Transcoding:
            class MediaVideoProcessingAlgorithm(_Enum):
                Default = 0
                MrfCrf444 = 1

            class TranscodeFailureReason(_Enum):
                None_ = 0
                Unknown = 1
                InvalidProfile = 2
                CodecNotFound = 3

    class Networking:
        class DomainNameType(_Enum):
            Suffix = 0
            FullyQualified = 1

        class HostNameSortOptions(_Enum):
            None_ = 0x0
            OptimizeForLongConnections = 0x2

        class HostNameType(_Enum):
            DomainName = 0
            Ipv4 = 1
            Ipv6 = 2
            Bluetooth = 3

        class BackgroundTransfer:
            class BackgroundTransferBehavior(_Enum):
                Parallel = 0
                Serialized = 1

            class BackgroundTransferCostPolicy(_Enum):
                Default = 0
                UnrestrictedOnly = 1
                Always = 2

            class BackgroundTransferPriority(_Enum):
                Default = 0
                High = 1
                Low = 2

            class BackgroundTransferStatus(_Enum):
                Idle = 0
                Running = 1
                PausedByApplication = 2
                PausedCostedNetwork = 3
                PausedNoNetwork = 4
                Completed = 5
                Canceled = 6
                Error = 7
                PausedRecoverableWebErrorStatus = 8
                PausedSystemPolicy = 32

        class Connectivity:
            class CellularApnAuthenticationType(_Enum):
                None_ = 0
                Pap = 1
                Chap = 2
                Mschapv2 = 3

            class ConnectionProfileDeleteStatus(_Enum):
                Success = 0
                DeniedByUser = 1
                DeniedBySystem = 2
                UnknownError = 3

            class DataUsageGranularity(_Enum):
                PerMinute = 0
                PerHour = 1
                PerDay = 2
                Total = 3

            class DomainAuthenticationKind(_Enum):
                None_ = 0
                Ldap = 1
                Tls = 2

            class DomainConnectivityLevel(_Enum):
                None_ = 0
                Unauthenticated = 1
                Authenticated = 2

            class NetworkAuthenticationType(_Enum):
                None_ = 0
                Unknown = 1
                Open80211 = 2
                SharedKey80211 = 3
                Wpa = 4
                WpaPsk = 5
                WpaNone = 6
                Rsna = 7
                RsnaPsk = 8
                Ihv = 9
                Wpa3 = 10
                Wpa3Enterprise192Bits = 10
                Wpa3Sae = 11
                Owe = 12
                Wpa3Enterprise = 13

            class NetworkConnectivityLevel(_Enum):
                None_ = 0
                LocalAccess = 1
                ConstrainedInternetAccess = 2
                InternetAccess = 3

            class NetworkCostType(_Enum):
                Unknown = 0
                Unrestricted = 1
                Fixed = 2
                Variable = 3

            class NetworkEncryptionType(_Enum):
                None_ = 0
                Unknown = 1
                Wep = 2
                Wep40 = 3
                Wep104 = 4
                Tkip = 5
                Ccmp = 6
                WpaUseGroup = 7
                RsnUseGroup = 8
                Ihv = 9
                Gcmp = 10
                Gcmp256 = 11

            class NetworkTypes(_Enum):
                None_ = 0x0
                Internet = 0x1
                PrivateNetwork = 0x2

            class RoamingStates(_Enum):
                None_ = 0x0
                NotRoaming = 0x1
                Roaming = 0x2

            class TriStates(_Enum):
                DoNotCare = 0
                No = 1
                Yes = 2

            class WwanDataClass(_Enum):
                None_ = 0x0
                Gprs = 0x1
                Edge = 0x2
                Umts = 0x4
                Hsdpa = 0x8
                Hsupa = 0x10
                LteAdvanced = 0x20
                Cdma1xRtt = 0x10000
                Cdma1xEvdo = 0x20000
                Cdma1xEvdoRevA = 0x40000
                Cdma1xEvdv = 0x80000
                Cdma3xRtt = 0x100000
                Cdma1xEvdoRevB = 0x200000
                CdmaUmb = 0x400000
                Custom = 0x80000000

            class WwanNetworkIPKind(_Enum):
                None_ = 0
                Ipv4 = 1
                Ipv6 = 2
                Ipv4v6 = 3
                Ipv4v6v4Xlat = 4

            class WwanNetworkRegistrationState(_Enum):
                None_ = 0
                Deregistered = 1
                Searching = 2
                Home = 3
                Roaming = 4
                Partner = 5
                Denied = 6

        class NetworkOperators:
            class DataClasses(_Enum):
                None_ = 0x0
                Gprs = 0x1
                Edge = 0x2
                Umts = 0x4
                Hsdpa = 0x8
                Hsupa = 0x10
                LteAdvanced = 0x20
                NewRadioNonStandalone = 0x40
                NewRadioStandalone = 0x80
                Cdma1xRtt = 0x10000
                Cdma1xEvdo = 0x20000
                Cdma1xEvdoRevA = 0x40000
                Cdma1xEvdv = 0x80000
                Cdma3xRtt = 0x100000
                Cdma1xEvdoRevB = 0x200000
                CdmaUmb = 0x400000
                Custom = 0x80000000

            class ESimAuthenticationPreference(_Enum):
                OnEntry = 0
                OnAction = 1
                Never = 2

            class ESimDiscoverResultKind(_Enum):
                None_ = 0
                Events = 1
                ProfileMetadata = 2

            class ESimOperationStatus(_Enum):
                Success = 0
                NotAuthorized = 1
                NotFound = 2
                PolicyViolation = 3
                InsufficientSpaceOnCard = 4
                ServerFailure = 5
                ServerNotReachable = 6
                TimeoutWaitingForUserConsent = 7
                IncorrectConfirmationCode = 8
                ConfirmationCodeMaxRetriesExceeded = 9
                CardRemoved = 10
                CardBusy = 11
                Other = 12
                CardGeneralFailure = 13
                ConfirmationCodeMissing = 14
                InvalidMatchingId = 15
                NoEligibleProfileForThisDevice = 16
                OperationAborted = 17
                EidMismatch = 18
                ProfileNotAvailableForNewBinding = 19
                ProfileNotReleasedByOperator = 20
                OperationProhibitedByProfileClass = 21
                ProfileNotPresent = 22
                NoCorrespondingRequest = 23
                TimeoutWaitingForResponse = 24
                IccidAlreadyExists = 25
                ProfileProcessingError = 26
                ServerNotTrusted = 27
                ProfileDownloadMaxRetriesExceeded = 28

            class ESimProfileClass(_Enum):
                Operational = 0
                Test = 1
                Provisioning = 2

            class ESimProfileMetadataState(_Enum):
                Unknown = 0
                WaitingForInstall = 1
                Downloading = 2
                Installing = 3
                Expired = 4
                RejectingDownload = 5
                NoLongerAvailable = 6
                DeniedByPolicy = 7

            class ESimProfileState(_Enum):
                Unknown = 0
                Disabled = 1
                Enabled = 2
                Deleted = 3

            class ESimState(_Enum):
                Unknown = 0
                Idle = 1
                Removed = 2
                Busy = 3

            class ESimWatcherStatus(_Enum):
                Created = 0
                Started = 1
                EnumerationCompleted = 2
                Stopping = 3
                Stopped = 4

            class HotspotAuthenticationResponseCode(_Enum):
                NoError = 0
                LoginSucceeded = 50
                LoginFailed = 100
                RadiusServerError = 102
                NetworkAdministratorError = 105
                LoginAborted = 151
                AccessGatewayInternalError = 255

            class MobileBroadbandAccountWatcherStatus(_Enum):
                Created = 0
                Started = 1
                EnumerationCompleted = 2
                Stopped = 3
                Aborted = 4

            class MobileBroadbandDeviceType(_Enum):
                Unknown = 0
                Embedded = 1
                Removable = 2
                Remote = 3

            class MobileBroadbandModemStatus(_Enum):
                Success = 0
                OtherFailure = 1
                Busy = 2
                NoDeviceSupport = 3

            class MobileBroadbandPinFormat(_Enum):
                Unknown = 0
                Numeric = 1
                Alphanumeric = 2

            class MobileBroadbandPinLockState(_Enum):
                Unknown = 0
                Unlocked = 1
                PinRequired = 2
                PinUnblockKeyRequired = 3

            class MobileBroadbandPinType(_Enum):
                None_ = 0
                Custom = 1
                Pin1 = 2
                Pin2 = 3
                SimPin = 4
                FirstSimPin = 5
                NetworkPin = 6
                NetworkSubsetPin = 7
                ServiceProviderPin = 8
                CorporatePin = 9
                SubsidyLock = 10

            class MobileBroadbandRadioState(_Enum):
                Off = 0
                On = 1

            class MobileBroadbandSlotState(_Enum):
                Unmanaged = 0
                Unknown = 1
                OffEmpty = 2
                Off = 3
                Empty = 4
                NotReady = 5
                Active = 6
                Error = 7
                ActiveEsim = 8
                ActiveEsimNoProfile = 9

            class MobileBroadbandUiccAppOperationStatus(_Enum):
                Success = 0
                InvalidUiccFilePath = 1
                AccessConditionNotHeld = 2
                UiccBusy = 3

            class NetworkDeviceStatus(_Enum):
                DeviceNotReady = 0
                DeviceReady = 1
                SimNotInserted = 2
                BadSim = 3
                DeviceHardwareFailure = 4
                AccountNotActivated = 5
                DeviceLocked = 6
                DeviceBlocked = 7

            class NetworkOperatorDataUsageNotificationKind(_Enum):
                DataUsageProgress = 0

            class NetworkOperatorEventMessageType(_Enum):
                Gsm = 0
                Cdma = 1
                Ussd = 2
                DataPlanThresholdReached = 3
                DataPlanReset = 4
                DataPlanDeleted = 5
                ProfileConnected = 6
                ProfileDisconnected = 7
                RegisteredRoaming = 8
                RegisteredHome = 9
                TetheringEntitlementCheck = 10
                TetheringOperationalStateChanged = 11
                TetheringNumberOfClientsChanged = 12

            class NetworkRegistrationState(_Enum):
                None_ = 0
                Deregistered = 1
                Searching = 2
                Home = 3
                Roaming = 4
                Partner = 5
                Denied = 6

            class ProfileMediaType(_Enum):
                Wlan = 0
                Wwan = 1

            class TetheringCapability(_Enum):
                Enabled = 0
                DisabledByGroupPolicy = 1
                DisabledByHardwareLimitation = 2
                DisabledByOperator = 3
                DisabledBySku = 4
                DisabledByRequiredAppNotInstalled = 5
                DisabledDueToUnknownCause = 6
                DisabledBySystemCapability = 7

            class TetheringOperationStatus(_Enum):
                Success = 0
                Unknown = 1
                MobileBroadbandDeviceOff = 2
                WiFiDeviceOff = 3
                EntitlementCheckTimeout = 4
                EntitlementCheckFailure = 5
                OperationInProgress = 6
                BluetoothDeviceOff = 7
                NetworkLimitedConnectivity = 8

            class TetheringOperationalState(_Enum):
                Unknown = 0
                On = 1
                Off = 2
                InTransition = 3

            class TetheringWiFiBand(_Enum):
                Auto = 0
                TwoPointFourGigahertz = 1
                FiveGigahertz = 2

            class UiccAccessCondition(_Enum):
                AlwaysAllowed = 0
                Pin1 = 1
                Pin2 = 2
                Pin3 = 3
                Pin4 = 4
                Administrative5 = 5
                Administrative6 = 6
                NeverAllowed = 7

            class UiccAppKind(_Enum):
                Unknown = 0
                MF = 1
                MFSim = 2
                MFRuim = 3
                USim = 4
                CSim = 5
                ISim = 6

            class UiccAppRecordKind(_Enum):
                Unknown = 0
                Transparent = 1
                RecordOriented = 2

            class UssdResultCode(_Enum):
                NoActionRequired = 0
                ActionRequired = 1
                Terminated = 2
                OtherLocalClient = 3
                OperationNotSupported = 4
                NetworkTimeout = 5

        class Proximity:
            class PeerDiscoveryTypes(_Enum):
                None_ = 0x0
                Browse = 0x1
                Triggered = 0x2

            class PeerRole(_Enum):
                Peer = 0
                Host = 1
                Client = 2

            class PeerWatcherStatus(_Enum):
                Created = 0
                Started = 1
                EnumerationCompleted = 2
                Stopping = 3
                Stopped = 4
                Aborted = 5

            class TriggeredConnectState(_Enum):
                PeerFound = 0
                Listening = 1
                Connecting = 2
                Completed = 3
                Canceled = 4
                Failed = 5

        class PushNotifications:
            class PushNotificationType(_Enum):
                Toast = 0
                Tile = 1
                Badge = 2
                Raw = 3
                TileFlyout = 4

        class ServiceDiscovery:
            class Dnssd:
                class DnssdRegistrationStatus(_Enum):
                    Success = 0
                    InvalidServiceName = 1
                    ServerError = 2
                    SecurityError = 3

                class DnssdServiceWatcherStatus(_Enum):
                    Created = 0
                    Started = 1
                    EnumerationCompleted = 2
                    Stopping = 3
                    Stopped = 4
                    Aborted = 5

        class Sockets:
            class ControlChannelTriggerResetReason(_Enum):
                FastUserSwitched = 0
                LowPowerExit = 1
                QuietHoursExit = 2
                ApplicationRestart = 3

            class ControlChannelTriggerResourceType(_Enum):
                RequestSoftwareSlot = 0
                RequestHardwareSlot = 1

            class ControlChannelTriggerStatus(_Enum):
                HardwareSlotRequested = 0
                SoftwareSlotAllocated = 1
                HardwareSlotAllocated = 2
                PolicyError = 3
                SystemError = 4
                TransportDisconnected = 5
                ServiceUnavailable = 6

            class MessageWebSocketReceiveMode(_Enum):
                FullMessage = 0
                PartialMessage = 1

            class SocketActivityConnectedStandbyAction(_Enum):
                DoNotWake = 0
                Wake = 1

            class SocketActivityKind(_Enum):
                None_ = 0
                StreamSocketListener = 1
                DatagramSocket = 2
                StreamSocket = 3

            class SocketActivityTriggerReason(_Enum):
                None_ = 0
                SocketActivity = 1
                ConnectionAccepted = 2
                KeepAliveTimerExpired = 3
                SocketClosed = 4

            class SocketErrorStatus(_Enum):
                Unknown = 0
                OperationAborted = 1
                HttpInvalidServerResponse = 2
                ConnectionTimedOut = 3
                AddressFamilyNotSupported = 4
                SocketTypeNotSupported = 5
                HostNotFound = 6
                NoDataRecordOfRequestedType = 7
                NonAuthoritativeHostNotFound = 8
                ClassTypeNotFound = 9
                AddressAlreadyInUse = 10
                CannotAssignRequestedAddress = 11
                ConnectionRefused = 12
                NetworkIsUnreachable = 13
                UnreachableHost = 14
                NetworkIsDown = 15
                NetworkDroppedConnectionOnReset = 16
                SoftwareCausedConnectionAbort = 17
                ConnectionResetByPeer = 18
                HostIsDown = 19
                NoAddressesFound = 20
                TooManyOpenFiles = 21
                MessageTooLong = 22
                CertificateExpired = 23
                CertificateUntrustedRoot = 24
                CertificateCommonNameIsIncorrect = 25
                CertificateWrongUsage = 26
                CertificateRevoked = 27
                CertificateNoRevocationCheck = 28
                CertificateRevocationServerOffline = 29
                CertificateIsInvalid = 30

            class SocketMessageType(_Enum):
                Binary = 0
                Utf8 = 1

            class SocketProtectionLevel(_Enum):
                PlainSocket = 0
                Ssl = 1
                SslAllowNullEncryption = 2
                BluetoothEncryptionAllowNullAuthentication = 3
                BluetoothEncryptionWithAuthentication = 4
                Ssl3AllowWeakEncryption = 5
                Tls10 = 6
                Tls11 = 7
                Tls12 = 8
                Unspecified = 9

            class SocketQualityOfService(_Enum):
                Normal = 0
                LowLatency = 1

            class SocketSslErrorSeverity(_Enum):
                None_ = 0
                Ignorable = 1
                Fatal = 2

        class Vpn:
            class VpnAppIdType(_Enum):
                PackageFamilyName = 0
                FullyQualifiedBinaryName = 1
                FilePath = 2

            class VpnAuthenticationMethod(_Enum):
                Mschapv2 = 0
                Eap = 1
                Certificate = 2
                PresharedKey = 3

            class VpnChannelActivityEventType(_Enum):
                Idle = 0
                Active = 1

            class VpnChannelRequestCredentialsOptions(_Enum):
                None_ = 0x0
                Retrying = 0x1
                UseForSingleSignIn = 0x2

            class VpnCredentialType(_Enum):
                UsernamePassword = 0
                UsernameOtpPin = 1
                UsernamePasswordAndPin = 2
                UsernamePasswordChange = 3
                SmartCard = 4
                ProtectedCertificate = 5
                UnProtectedCertificate = 6

            class VpnDataPathType(_Enum):
                Send = 0
                Receive = 1

            class VpnDomainNameType(_Enum):
                Suffix = 0
                FullyQualified = 1
                Reserved = 65535

            class VpnIPProtocol(_Enum):
                None_ = 0
                Tcp = 6
                Udp = 17
                Icmp = 1
                Ipv6Icmp = 58
                Igmp = 2
                Pgm = 113

            class VpnManagementConnectionStatus(_Enum):
                Disconnected = 0
                Disconnecting = 1
                Connected = 2
                Connecting = 3

            class VpnManagementErrorStatus(_Enum):
                Ok = 0
                Other = 1
                InvalidXmlSyntax = 2
                ProfileNameTooLong = 3
                ProfileInvalidAppId = 4
                AccessDenied = 5
                CannotFindProfile = 6
                AlreadyDisconnecting = 7
                AlreadyConnected = 8
                GeneralAuthenticationFailure = 9
                EapFailure = 10
                SmartCardFailure = 11
                CertificateFailure = 12
                ServerConfiguration = 13
                NoConnection = 14
                ServerConnection = 15
                UserNamePassword = 16
                DnsNotResolvable = 17
                InvalidIP = 18

            class VpnNativeProtocolType(_Enum):
                Pptp = 0
                L2tp = 1
                IpsecIkev2 = 2

            class VpnPacketBufferStatus(_Enum):
                Ok = 0
                InvalidBufferSize = 1

            class VpnRoutingPolicyType(_Enum):
                SplitRouting = 0
                ForceAllTrafficOverVpn = 1

        class XboxLive:
            class XboxLiveEndpointPairCreationBehaviors(_Enum):
                None_ = 0x0
                ReevaluatePath = 0x1

            class XboxLiveEndpointPairCreationStatus(_Enum):
                Succeeded = 0
                NoLocalNetworks = 1
                NoCompatibleNetworkPaths = 2
                LocalSystemNotAuthorized = 3
                Canceled = 4
                TimedOut = 5
                RemoteSystemNotAuthorized = 6
                RefusedDueToConfiguration = 7
                UnexpectedInternalError = 8

            class XboxLiveEndpointPairState(_Enum):
                Invalid = 0
                CreatingOutbound = 1
                CreatingInbound = 2
                Ready = 3
                DeletingLocally = 4
                RemoteEndpointTerminating = 5
                Deleted = 6

            class XboxLiveNetworkAccessKind(_Enum):
                Open = 0
                Moderate = 1
                Strict = 2

            class XboxLiveQualityOfServiceMeasurementStatus(_Enum):
                NotStarted = 0
                InProgress = 1
                InProgressWithProvisionalResults = 2
                Succeeded = 3
                NoLocalNetworks = 4
                NoCompatibleNetworkPaths = 5
                LocalSystemNotAuthorized = 6
                Canceled = 7
                TimedOut = 8
                RemoteSystemNotAuthorized = 9
                RefusedDueToConfiguration = 10
                UnexpectedInternalError = 11

            class XboxLiveQualityOfServiceMetric(_Enum):
                AverageLatencyInMilliseconds = 0
                MinLatencyInMilliseconds = 1
                MaxLatencyInMilliseconds = 2
                AverageOutboundBitsPerSecond = 3
                MinOutboundBitsPerSecond = 4
                MaxOutboundBitsPerSecond = 5
                AverageInboundBitsPerSecond = 6
                MinInboundBitsPerSecond = 7
                MaxInboundBitsPerSecond = 8

            class XboxLiveSocketKind(_Enum):
                None_ = 0
                Datagram = 1
                Stream = 2

    class Perception:
        class People:
            class HandJointKind(_Enum):
                Palm = 0
                Wrist = 1
                ThumbMetacarpal = 2
                ThumbProximal = 3
                ThumbDistal = 4
                ThumbTip = 5
                IndexMetacarpal = 6
                IndexProximal = 7
                IndexIntermediate = 8
                IndexDistal = 9
                IndexTip = 10
                MiddleMetacarpal = 11
                MiddleProximal = 12
                MiddleIntermediate = 13
                MiddleDistal = 14
                MiddleTip = 15
                RingMetacarpal = 16
                RingProximal = 17
                RingIntermediate = 18
                RingDistal = 19
                RingTip = 20
                LittleMetacarpal = 21
                LittleProximal = 22
                LittleIntermediate = 23
                LittleDistal = 24
                LittleTip = 25

            class JointPoseAccuracy(_Enum):
                High = 0
                Approximate = 1

        class Spatial:
            class SpatialAnchorExportPurpose(_Enum):
                Relocalization = 0
                Sharing = 1

            class SpatialEntityWatcherStatus(_Enum):
                Created = 0
                Started = 1
                EnumerationCompleted = 2
                Stopping = 3
                Stopped = 4
                Aborted = 5

            class SpatialLocatability(_Enum):
                Unavailable = 0
                OrientationOnly = 1
                PositionalTrackingActivating = 2
                PositionalTrackingActive = 3
                PositionalTrackingInhibited = 4

            class SpatialLookDirectionRange(_Enum):
                ForwardOnly = 0
                Omnidirectional = 1

            class SpatialMovementRange(_Enum):
                NoMovement = 0
                Bounded = 1

            class SpatialPerceptionAccessStatus(_Enum):
                Unspecified = 0
                Allowed = 1
                DeniedByUser = 2
                DeniedBySystem = 3

    class Phone:
        class Networking:
            class Voip:
                class SeamlessCallUpgradeSupport(_Enum):
                    Unknown = 0
                    NotSupported = 1
                    Supported = 2

                class VoipCallMedia(_Enum):
                    None_ = 0x0
                    Audio = 0x1
                    Video = 0x2

                class VoipCallRejectReason(_Enum):
                    UserIgnored = 0
                    TimedOut = 1
                    OtherIncomingCall = 2
                    EmergencyCallExists = 3
                    InvalidCallState = 4

                class VoipCallState(_Enum):
                    Ended = 0
                    Held = 1
                    Active = 2
                    Incoming = 3
                    Outgoing = 4

                class VoipOperationType(_Enum):
                    QueryRemotePartySeamless = 0

        class UI:
            class Core:
                class CoreInputScope(_Enum):
                    Default = 0
                    Url = 1
                    EmailSmtpAddress = 5
                    Number = 29
                    TelephoneNumber = 32
                    Text = 49
                    Search = 51

    class Security:
        class Authentication:
            class Identity:
                class Core:
                    class MicrosoftAccountMultiFactorAuthenticationType(_Enum):
                        User = 0
                        Device = 1

                    class MicrosoftAccountMultiFactorServiceResponse(_Enum):
                        Success = 0
                        Error = 1
                        NoNetworkConnection = 2
                        ServiceUnavailable = 3
                        TotpSetupDenied = 4
                        NgcNotSetup = 5
                        SessionAlreadyDenied = 6
                        SessionAlreadyApproved = 7
                        SessionExpired = 8
                        NgcNonceExpired = 9
                        InvalidSessionId = 10
                        InvalidSessionType = 11
                        InvalidOperation = 12
                        InvalidStateTransition = 13
                        DeviceNotFound = 14
                        FlowDisabled = 15
                        SessionNotApproved = 16
                        OperationCanceledByUser = 17
                        NgcDisabledByServer = 18
                        NgcKeyNotFoundOnServer = 19
                        UIRequired = 20
                        DeviceIdChanged = 21

                    class MicrosoftAccountMultiFactorSessionApprovalStatus(_Enum):
                        Pending = 0
                        Approved = 1
                        Denied = 2

                    class MicrosoftAccountMultiFactorSessionAuthenticationStatus(_Enum):
                        Authenticated = 0
                        Unauthenticated = 1

                class Provider:
                    class SecondaryAuthenticationFactorAuthenticationMessage(_Enum):
                        Invalid = 0
                        SwipeUpWelcome = 1
                        TapWelcome = 2
                        DeviceNeedsAttention = 3
                        LookingForDevice = 4
                        LookingForDevicePluggedin = 5
                        BluetoothIsDisabled = 6
                        NfcIsDisabled = 7
                        WiFiIsDisabled = 8
                        ExtraTapIsRequired = 9
                        DisabledByPolicy = 10
                        TapOnDeviceRequired = 11
                        HoldFinger = 12
                        ScanFinger = 13
                        UnauthorizedUser = 14
                        ReregisterRequired = 15
                        TryAgain = 16
                        SayPassphrase = 17
                        ReadyToSignIn = 18
                        UseAnotherSignInOption = 19
                        ConnectionRequired = 20
                        TimeLimitExceeded = 21
                        CanceledByUser = 22
                        CenterHand = 23
                        MoveHandCloser = 24
                        MoveHandFarther = 25
                        PlaceHandAbove = 26
                        RecognitionFailed = 27
                        DeviceUnavailable = 28

                    class SecondaryAuthenticationFactorAuthenticationScenario(_Enum):
                        SignIn = 0
                        CredentialPrompt = 1

                    class SecondaryAuthenticationFactorAuthenticationStage(_Enum):
                        NotStarted = 0
                        WaitingForUserConfirmation = 1
                        CollectingCredential = 2
                        SuspendingAuthentication = 3
                        CredentialCollected = 4
                        CredentialAuthenticated = 5
                        StoppingAuthentication = 6
                        ReadyForLock = 7
                        CheckingDevicePresence = 8

                    class SecondaryAuthenticationFactorAuthenticationStatus(_Enum):
                        Failed = 0
                        Started = 1
                        UnknownDevice = 2
                        DisabledByPolicy = 3
                        InvalidAuthenticationStage = 4

                    class SecondaryAuthenticationFactorDeviceCapabilities(_Enum):
                        None_ = 0x0
                        SecureStorage = 0x1
                        StoreKeys = 0x2
                        ConfirmUserIntentToAuthenticate = 0x4
                        SupportSecureUserPresenceCheck = 0x8
                        TransmittedDataIsEncrypted = 0x10
                        HMacSha256 = 0x20
                        CloseRangeDataTransmission = 0x40

                    class SecondaryAuthenticationFactorDeviceFindScope(_Enum):
                        User = 0
                        AllUsers = 1

                    class SecondaryAuthenticationFactorDevicePresence(_Enum):
                        Absent = 0
                        Present = 1

                    class SecondaryAuthenticationFactorDevicePresenceMonitoringMode(_Enum):
                        Unsupported = 0
                        AppManaged = 1
                        SystemManaged = 2

                    class SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus(_Enum):
                        Unsupported = 0
                        Succeeded = 1
                        DisabledByPolicy = 2

                    class SecondaryAuthenticationFactorFinishAuthenticationStatus(_Enum):
                        Failed = 0
                        Completed = 1
                        NonceExpired = 2

                    class SecondaryAuthenticationFactorRegistrationStatus(_Enum):
                        Failed = 0
                        Started = 1
                        CanceledByUser = 2
                        PinSetupRequired = 3
                        DisabledByPolicy = 4

            class OnlineId:
                class CredentialPromptType(_Enum):
                    PromptIfNeeded = 0
                    RetypeCredentials = 1
                    DoNotPrompt = 2

                class OnlineIdSystemTicketStatus(_Enum):
                    Success = 0
                    Error = 1
                    ServiceConnectionError = 2

            class Web:
                class TokenBindingKeyType(_Enum):
                    Rsa2048 = 0
                    EcdsaP256 = 1
                    AnyExisting = 2

                class WebAuthenticationOptions(_Enum):
                    None_ = 0x0
                    SilentMode = 0x1
                    UseTitle = 0x2
                    UseHttpPost = 0x4
                    UseCorporateNetwork = 0x8

                class WebAuthenticationStatus(_Enum):
                    Success = 0
                    UserCancel = 1
                    ErrorHttp = 2

                class Core:
                    class FindAllWebAccountsStatus(_Enum):
                        Success = 0
                        NotAllowedByProvider = 1
                        NotSupportedByProvider = 2
                        ProviderError = 3

                    class WebTokenRequestPromptType(_Enum):
                        Default = 0
                        ForceAuthentication = 1

                    class WebTokenRequestStatus(_Enum):
                        Success = 0
                        UserCancel = 1
                        AccountSwitch = 2
                        UserInteractionRequired = 3
                        AccountProviderNotAvailable = 4
                        ProviderError = 5

                class Provider:
                    class WebAccountClientViewType(_Enum):
                        IdOnly = 0
                        IdAndProperties = 1

                    class WebAccountProviderOperationKind(_Enum):
                        RequestToken = 0
                        GetTokenSilently = 1
                        AddAccount = 2
                        ManageAccount = 3
                        DeleteAccount = 4
                        RetrieveCookies = 5
                        SignOutAccount = 6

                    class WebAccountScope(_Enum):
                        PerUser = 0
                        PerApplication = 1

                    class WebAccountSelectionOptions(_Enum):
                        Default = 0x0
                        New = 0x1

        class Authorization:
            class AppCapabilityAccess:
                class AppCapabilityAccessStatus(_Enum):
                    DeniedBySystem = 0
                    NotDeclaredByApp = 1
                    DeniedByUser = 2
                    UserPromptRequired = 3
                    Allowed = 4

        class Credentials:
            class KeyCredentialAttestationStatus(_Enum):
                Success = 0
                UnknownError = 1
                NotSupported = 2
                TemporaryFailure = 3

            class KeyCredentialCreationOption(_Enum):
                ReplaceExisting = 0
                FailIfExists = 1

            class KeyCredentialStatus(_Enum):
                Success = 0
                UnknownError = 1
                NotFound = 2
                UserCanceled = 3
                UserPrefersPassword = 4
                CredentialAlreadyExists = 5
                SecurityDeviceLocked = 6

            class WebAccountPictureSize(_Enum):
                Size64x64 = 64
                Size208x208 = 208
                Size424x424 = 424
                Size1080x1080 = 1080

            class WebAccountState(_Enum):
                None_ = 0
                Connected = 1
                Error = 2

            class UI:
                class AuthenticationProtocol(_Enum):
                    Basic = 0
                    Digest = 1
                    Ntlm = 2
                    Kerberos = 3
                    Negotiate = 4
                    CredSsp = 5
                    Custom = 6

                class CredentialSaveOption(_Enum):
                    Unselected = 0
                    Selected = 1
                    Hidden = 2

                class UserConsentVerificationResult(_Enum):
                    Verified = 0
                    DeviceNotPresent = 1
                    NotConfiguredForUser = 2
                    DisabledByPolicy = 3
                    DeviceBusy = 4
                    RetriesExhausted = 5
                    Canceled = 6

                class UserConsentVerifierAvailability(_Enum):
                    Available = 0
                    DeviceNotPresent = 1
                    NotConfiguredForUser = 2
                    DisabledByPolicy = 3
                    DeviceBusy = 4

        class Cryptography:
            class BinaryStringEncoding(_Enum):
                Utf8 = 0
                Utf16LE = 1
                Utf16BE = 2

            class Certificates:
                class CertificateChainPolicy(_Enum):
                    Base = 0
                    Ssl = 1
                    NTAuthentication = 2
                    MicrosoftRoot = 3

                class ChainValidationResult(_Enum):
                    Success = 0
                    Untrusted = 1
                    Revoked = 2
                    Expired = 3
                    IncompleteChain = 4
                    InvalidSignature = 5
                    WrongUsage = 6
                    InvalidName = 7
                    InvalidCertificateAuthorityPolicy = 8
                    BasicConstraintsError = 9
                    UnknownCriticalExtension = 10
                    RevocationInformationMissing = 11
                    RevocationFailure = 12
                    OtherErrors = 13

                class EnrollKeyUsages(_Enum):
                    None_ = 0x0
                    Decryption = 0x1
                    Signing = 0x2
                    KeyAgreement = 0x4

                class ExportOption(_Enum):
                    NotExportable = 0
                    Exportable = 1

                class InstallOptions(_Enum):
                    None_ = 0x0
                    DeleteExpired = 0x1

                class KeyProtectionLevel(_Enum):
                    NoConsent = 0
                    ConsentOnly = 1
                    ConsentWithPassword = 2
                    ConsentWithFingerprint = 3

                class KeySize(_Enum):
                    Invalid = 0
                    Rsa2048 = 2048
                    Rsa4096 = 4096

                class SignatureValidationResult(_Enum):
                    Success = 0
                    InvalidParameter = 1
                    BadMessage = 2
                    InvalidSignature = 3
                    OtherErrors = 4

            class Core:
                class Capi1KdfTargetAlgorithm(_Enum):
                    NotAes = 0
                    Aes = 1

                class CryptographicPadding(_Enum):
                    None_ = 0
                    RsaOaep = 1
                    RsaPkcs1V15 = 2
                    RsaPss = 3

                class CryptographicPrivateKeyBlobType(_Enum):
                    Pkcs8RawPrivateKeyInfo = 0
                    Pkcs1RsaPrivateKey = 1
                    BCryptPrivateKey = 2
                    Capi1PrivateKey = 3
                    BCryptEccFullPrivateKey = 4

                class CryptographicPublicKeyBlobType(_Enum):
                    X509SubjectPublicKeyInfo = 0
                    Pkcs1RsaPublicKey = 1
                    BCryptPublicKey = 2
                    Capi1PublicKey = 3
                    BCryptEccFullPublicKey = 4

        class DataProtection:
            class UserDataAvailability(_Enum):
                Always = 0
                AfterFirstUnlock = 1
                WhileUnlocked = 2

            class UserDataBufferUnprotectStatus(_Enum):
                Succeeded = 0
                Unavailable = 1

            class UserDataStorageItemProtectionStatus(_Enum):
                Succeeded = 0
                NotProtectable = 1
                DataUnavailable = 2

        class EnterpriseData:
            class DataProtectionStatus(_Enum):
                ProtectedToOtherIdentity = 0
                Protected = 1
                Revoked = 2
                Unprotected = 3
                LicenseExpired = 4
                AccessSuspended = 5

            class EnforcementLevel(_Enum):
                NoProtection = 0
                Silent = 1
                Override = 2
                Block = 3

            class FileProtectionStatus(_Enum):
                Undetermined = 0
                Unknown = 0
                Unprotected = 1
                Revoked = 2
                Protected = 3
                ProtectedByOtherUser = 4
                ProtectedToOtherEnterprise = 5
                NotProtectable = 6
                ProtectedToOtherIdentity = 7
                LicenseExpired = 8
                AccessSuspended = 9
                FileInUse = 10

            class ProtectedImportExportStatus(_Enum):
                Ok = 0
                Undetermined = 1
                Unprotected = 2
                Revoked = 3
                NotRoamable = 4
                ProtectedToOtherIdentity = 5
                LicenseExpired = 6
                AccessSuspended = 7

            class ProtectionPolicyAuditAction(_Enum):
                Decrypt = 0
                CopyToLocation = 1
                SendToRecipient = 2
                Other = 3

            class ProtectionPolicyEvaluationResult(_Enum):
                Allowed = 0
                Blocked = 1
                ConsentRequired = 2

            class ProtectionPolicyRequestAccessBehavior(_Enum):
                Decrypt = 0
                TreatOverridePolicyAsBlock = 1

        class ExchangeActiveSyncProvisioning:
            class EasDisallowConvenienceLogonResult(_Enum):
                NotEvaluated = 0
                Compliant = 1
                CanBeCompliant = 2
                RequestedPolicyIsStricter = 3

            class EasEncryptionProviderType(_Enum):
                NotEvaluated = 0
                WindowsEncryption = 1
                OtherEncryption = 2

            class EasMaxInactivityTimeLockResult(_Enum):
                NotEvaluated = 0
                Compliant = 1
                CanBeCompliant = 2
                RequestedPolicyIsStricter = 3
                InvalidParameter = 4

            class EasMaxPasswordFailedAttemptsResult(_Enum):
                NotEvaluated = 0
                Compliant = 1
                CanBeCompliant = 2
                RequestedPolicyIsStricter = 3
                InvalidParameter = 4

            class EasMinPasswordComplexCharactersResult(_Enum):
                NotEvaluated = 0
                Compliant = 1
                CanBeCompliant = 2
                RequestedPolicyIsStricter = 3
                RequestedPolicyNotEnforceable = 4
                InvalidParameter = 5
                CurrentUserHasBlankPassword = 6
                AdminsHaveBlankPassword = 7
                UserCannotChangePassword = 8
                AdminsCannotChangePassword = 9
                LocalControlledUsersCannotChangePassword = 10
                ConnectedAdminsProviderPolicyIsWeak = 11
                ConnectedUserProviderPolicyIsWeak = 12
                ChangeConnectedAdminsPassword = 13
                ChangeConnectedUserPassword = 14

            class EasMinPasswordLengthResult(_Enum):
                NotEvaluated = 0
                Compliant = 1
                CanBeCompliant = 2
                RequestedPolicyIsStricter = 3
                RequestedPolicyNotEnforceable = 4
                InvalidParameter = 5
                CurrentUserHasBlankPassword = 6
                AdminsHaveBlankPassword = 7
                UserCannotChangePassword = 8
                AdminsCannotChangePassword = 9
                LocalControlledUsersCannotChangePassword = 10
                ConnectedAdminsProviderPolicyIsWeak = 11
                ConnectedUserProviderPolicyIsWeak = 12
                ChangeConnectedAdminsPassword = 13
                ChangeConnectedUserPassword = 14

            class EasPasswordExpirationResult(_Enum):
                NotEvaluated = 0
                Compliant = 1
                CanBeCompliant = 2
                RequestedPolicyIsStricter = 3
                RequestedExpirationIncompatible = 4
                InvalidParameter = 5
                UserCannotChangePassword = 6
                AdminsCannotChangePassword = 7
                LocalControlledUsersCannotChangePassword = 8

            class EasPasswordHistoryResult(_Enum):
                NotEvaluated = 0
                Compliant = 1
                CanBeCompliant = 2
                RequestedPolicyIsStricter = 3
                InvalidParameter = 4

            class EasRequireEncryptionResult(_Enum):
                NotEvaluated = 0
                Compliant = 1
                CanBeCompliant = 2
                NotProvisionedOnAllVolumes = 3
                DeFixedDataNotSupported = 4
                FixedDataNotSupported = 4
                DeHardwareNotCompliant = 5
                HardwareNotCompliant = 5
                DeWinReNotConfigured = 6
                LockNotConfigured = 6
                DeProtectionSuspended = 7
                ProtectionSuspended = 7
                DeOsVolumeNotProtected = 8
                OsVolumeNotProtected = 8
                DeProtectionNotYetEnabled = 9
                ProtectionNotYetEnabled = 9
                NoFeatureLicense = 10
                OsNotProtected = 11
                UnexpectedFailure = 12

        class Isolation:
            class IsolatedWindowsEnvironmentActivator(_Enum):
                System = 0
                User = 1

            class IsolatedWindowsEnvironmentAllowedClipboardFormats(_Enum):
                None_ = 0x0
                Text = 0x1
                Image = 0x2
                Rtf = 0x4

            class IsolatedWindowsEnvironmentAvailablePrinters(_Enum):
                None_ = 0x0
                Local = 0x1
                Network = 0x2
                SystemPrintToPdf = 0x4
                SystemPrintToXps = 0x8

            class IsolatedWindowsEnvironmentClipboardCopyPasteDirections(_Enum):
                None_ = 0x0
                HostToIsolatedWindowsEnvironment = 0x1
                IsolatedWindowsEnvironmentToHost = 0x2

            class IsolatedWindowsEnvironmentCreateStatus(_Enum):
                Success = 0
                FailureByPolicy = 1
                UnknownFailure = 2

            class IsolatedWindowsEnvironmentCreationPriority(_Enum):
                Low = 0
                Normal = 1

            class IsolatedWindowsEnvironmentHostError(_Enum):
                AdminPolicyIsDisabledOrNotPresent = 0
                FeatureNotInstalled = 1
                HardwareRequirementsNotMet = 2
                RebootRequired = 3
                UnknownError = 4

            class IsolatedWindowsEnvironmentLaunchFileStatus(_Enum):
                Success = 0
                UnknownFailure = 1
                EnvironmentUnavailable = 2
                FileNotFound = 3
                TimedOut = 4
                AlreadySharedWithConflictingOptions = 5

            class IsolatedWindowsEnvironmentOwnerRegistrationStatus(_Enum):
                Success = 0
                InvalidArgument = 1
                AccessDenied = 2
                InsufficientMemory = 3
                UnknownFailure = 4

            class IsolatedWindowsEnvironmentPostMessageStatus(_Enum):
                Success = 0
                UnknownFailure = 1
                EnvironmentUnavailable = 2

            class IsolatedWindowsEnvironmentProcessState(_Enum):
                Running = 1
                Aborted = 2
                Completed = 3

            class IsolatedWindowsEnvironmentProgressState(_Enum):
                Queued = 0
                Processing = 1
                Completed = 2
                Creating = 3
                Retrying = 4
                Starting = 5
                Finalizing = 6

            class IsolatedWindowsEnvironmentShareFileStatus(_Enum):
                Success = 0
                UnknownFailure = 1
                EnvironmentUnavailable = 2
                AlreadySharedWithConflictingOptions = 3
                FileNotFound = 4
                AccessDenied = 5

            class IsolatedWindowsEnvironmentShareFolderStatus(_Enum):
                Success = 0
                UnknownFailure = 1
                EnvironmentUnavailable = 2
                FolderNotFound = 3
                AccessDenied = 4

            class IsolatedWindowsEnvironmentSignInProgress(_Enum):
                Connecting = 0
                Connected = 1
                Authenticating = 2
                SettingUpAccount = 3
                Finalizing = 4
                Completed = 5

            class IsolatedWindowsEnvironmentStartProcessStatus(_Enum):
                Success = 0
                UnknownFailure = 1
                EnvironmentUnavailable = 2
                FileNotFound = 3
                AppNotRegistered = 4

    class Services:
        class Cortana:
            class CortanaPermission(_Enum):
                BrowsingHistory = 0
                Calendar = 1
                CallHistory = 2
                Contacts = 3
                Email = 4
                InputPersonalization = 5
                Location = 6
                Messaging = 7
                Microphone = 8
                Personalization = 9
                PhoneCall = 10

            class CortanaPermissionsChangeResult(_Enum):
                Success = 0
                Unavailable = 1
                DisabledByPolicy = 2

        class Maps:
            class ManeuverWarningKind(_Enum):
                None_ = 0
                Accident = 1
                AdministrativeDivisionChange = 2
                Alert = 3
                BlockedRoad = 4
                CheckTimetable = 5
                Congestion = 6
                Construction = 7
                CountryChange = 8
                DisabledVehicle = 9
                GateAccess = 10
                GetOffTransit = 11
                GetOnTransit = 12
                IllegalUTurn = 13
                MassTransit = 14
                Miscellaneous = 15
                NoIncident = 16
                Other = 17
                OtherNews = 18
                OtherTrafficIncidents = 19
                PlannedEvent = 20
                PrivateRoad = 21
                RestrictedTurn = 22
                RoadClosures = 23
                RoadHazard = 24
                ScheduledConstruction = 25
                SeasonalClosures = 26
                Tollbooth = 27
                TollRoad = 28
                TollZoneEnter = 29
                TollZoneExit = 30
                TrafficFlow = 31
                TransitLineChange = 32
                UnpavedRoad = 33
                UnscheduledConstruction = 34
                Weather = 35

            class ManeuverWarningSeverity(_Enum):
                None_ = 0
                LowImpact = 1
                Minor = 2
                Moderate = 3
                Serious = 4

            class MapLocationDesiredAccuracy(_Enum):
                High = 0
                Low = 1

            class MapLocationFinderStatus(_Enum):
                Success = 0
                UnknownError = 1
                InvalidCredentials = 2
                BadLocation = 3
                IndexFailure = 4
                NetworkFailure = 5
                NotSupported = 6

            class MapManeuverNotices(_Enum):
                None_ = 0x0
                Toll = 0x1
                Unpaved = 0x2

            class MapRouteFinderStatus(_Enum):
                Success = 0
                UnknownError = 1
                InvalidCredentials = 2
                NoRouteFound = 3
                NoRouteFoundWithGivenOptions = 4
                StartPointNotFound = 5
                EndPointNotFound = 6
                NoPedestrianRouteFound = 7
                NetworkFailure = 8
                NotSupported = 9

            class MapRouteManeuverKind(_Enum):
                None_ = 0
                Start = 1
                Stopover = 2
                StopoverResume = 3
                End = 4
                GoStraight = 5
                UTurnLeft = 6
                UTurnRight = 7
                TurnKeepLeft = 8
                TurnKeepRight = 9
                TurnLightLeft = 10
                TurnLightRight = 11
                TurnLeft = 12
                TurnRight = 13
                TurnHardLeft = 14
                TurnHardRight = 15
                FreewayEnterLeft = 16
                FreewayEnterRight = 17
                FreewayLeaveLeft = 18
                FreewayLeaveRight = 19
                FreewayContinueLeft = 20
                FreewayContinueRight = 21
                TrafficCircleLeft = 22
                TrafficCircleRight = 23
                TakeFerry = 24

            class MapRouteOptimization(_Enum):
                Time = 0
                Distance = 1
                TimeWithTraffic = 2
                Scenic = 3

            class MapRouteRestrictions(_Enum):
                None_ = 0x0
                Highways = 0x1
                TollRoads = 0x2
                Ferries = 0x4
                Tunnels = 0x8
                DirtRoads = 0x10
                Motorail = 0x20

            class MapServiceDataUsagePreference(_Enum):
                Default = 0
                OfflineMapDataOnly = 1

            class TrafficCongestion(_Enum):
                Unknown = 0
                Light = 1
                Mild = 2
                Medium = 3
                Heavy = 4

            class WaypointKind(_Enum):
                Stop = 0
                Via = 1

            class Guidance:
                class GuidanceAudioMeasurementSystem(_Enum):
                    Meters = 0
                    MilesAndYards = 1
                    MilesAndFeet = 2

                class GuidanceAudioNotificationKind(_Enum):
                    Maneuver = 0
                    Route = 1
                    Gps = 2
                    SpeedLimit = 3
                    Traffic = 4
                    TrafficCamera = 5

                class GuidanceAudioNotifications(_Enum):
                    None_ = 0x0
                    Maneuver = 0x1
                    Route = 0x2
                    Gps = 0x4
                    SpeedLimit = 0x8
                    Traffic = 0x10
                    TrafficCamera = 0x20

                class GuidanceLaneMarkers(_Enum):
                    None_ = 0x0
                    LightRight = 0x1
                    Right = 0x2
                    HardRight = 0x4
                    Straight = 0x8
                    UTurnLeft = 0x10
                    HardLeft = 0x20
                    Left = 0x40
                    LightLeft = 0x80
                    UTurnRight = 0x100

                class GuidanceManeuverKind(_Enum):
                    None_ = 0
                    GoStraight = 1
                    UTurnRight = 2
                    UTurnLeft = 3
                    TurnKeepRight = 4
                    TurnLightRight = 5
                    TurnRight = 6
                    TurnHardRight = 7
                    KeepMiddle = 8
                    TurnKeepLeft = 9
                    TurnLightLeft = 10
                    TurnLeft = 11
                    TurnHardLeft = 12
                    FreewayEnterRight = 13
                    FreewayEnterLeft = 14
                    FreewayLeaveRight = 15
                    FreewayLeaveLeft = 16
                    FreewayKeepRight = 17
                    FreewayKeepLeft = 18
                    TrafficCircleRight1 = 19
                    TrafficCircleRight2 = 20
                    TrafficCircleRight3 = 21
                    TrafficCircleRight4 = 22
                    TrafficCircleRight5 = 23
                    TrafficCircleRight6 = 24
                    TrafficCircleRight7 = 25
                    TrafficCircleRight8 = 26
                    TrafficCircleRight9 = 27
                    TrafficCircleRight10 = 28
                    TrafficCircleRight11 = 29
                    TrafficCircleRight12 = 30
                    TrafficCircleLeft1 = 31
                    TrafficCircleLeft2 = 32
                    TrafficCircleLeft3 = 33
                    TrafficCircleLeft4 = 34
                    TrafficCircleLeft5 = 35
                    TrafficCircleLeft6 = 36
                    TrafficCircleLeft7 = 37
                    TrafficCircleLeft8 = 38
                    TrafficCircleLeft9 = 39
                    TrafficCircleLeft10 = 40
                    TrafficCircleLeft11 = 41
                    TrafficCircleLeft12 = 42
                    Start = 43
                    End = 44
                    TakeFerry = 45
                    PassTransitStation = 46
                    LeaveTransitStation = 47

                class GuidanceMode(_Enum):
                    None_ = 0
                    Simulation = 1
                    Navigation = 2
                    Tracking = 3

            class LocalSearch:
                class LocalLocationFinderStatus(_Enum):
                    Success = 0
                    UnknownError = 1
                    InvalidCredentials = 2
                    InvalidCategory = 3
                    InvalidSearchTerm = 4
                    InvalidSearchArea = 5
                    NetworkFailure = 6
                    NotSupported = 7

            class OfflineMaps:
                class OfflineMapPackageQueryStatus(_Enum):
                    Success = 0
                    UnknownError = 1
                    InvalidCredentials = 2
                    NetworkFailure = 3

                class OfflineMapPackageStartDownloadStatus(_Enum):
                    Success = 0
                    UnknownError = 1
                    InvalidCredentials = 2
                    DeniedWithoutCapability = 3

                class OfflineMapPackageStatus(_Enum):
                    NotDownloaded = 0
                    Downloading = 1
                    Downloaded = 2
                    Deleting = 3

        class Store:
            class StoreCanLicenseStatus(_Enum):
                NotLicensableToUser = 0
                Licensable = 1
                LicenseActionNotApplicableToProduct = 2
                NetworkError = 3
                ServerError = 4

            class StoreConsumableStatus(_Enum):
                Succeeded = 0
                InsufficentQuantity = 1
                NetworkError = 2
                ServerError = 3

            class StoreDurationUnit(_Enum):
                Minute = 0
                Hour = 1
                Day = 2
                Week = 3
                Month = 4
                Year = 5

            class StorePackageUpdateState(_Enum):
                Pending = 0
                Downloading = 1
                Deploying = 2
                Completed = 3
                Canceled = 4
                OtherError = 5
                ErrorLowBattery = 6
                ErrorWiFiRecommended = 7
                ErrorWiFiRequired = 8

            class StorePurchaseStatus(_Enum):
                Succeeded = 0
                AlreadyPurchased = 1
                NotPurchased = 2
                NetworkError = 3
                ServerError = 4

            class StoreQueueItemExtendedState(_Enum):
                ActivePending = 0
                ActiveStarting = 1
                ActiveAcquiringLicense = 2
                ActiveDownloading = 3
                ActiveRestoringData = 4
                ActiveInstalling = 5
                Completed = 6
                Canceled = 7
                Paused = 8
                Error = 9
                PausedPackagesInUse = 10
                PausedLowBattery = 11
                PausedWiFiRecommended = 12
                PausedWiFiRequired = 13
                PausedReadyToInstall = 14

            class StoreQueueItemKind(_Enum):
                Install = 0
                Update = 1
                Repair = 2

            class StoreQueueItemState(_Enum):
                Active = 0
                Completed = 1
                Canceled = 2
                Error = 3
                Paused = 4

            class StoreRateAndReviewStatus(_Enum):
                Succeeded = 0
                CanceledByUser = 1
                NetworkError = 2
                Error = 3

            class StoreUninstallStorePackageStatus(_Enum):
                Succeeded = 0
                CanceledByUser = 1
                NetworkError = 2
                UninstallNotApplicable = 3
                Error = 4

        class TargetedContent:
            class TargetedContentAppInstallationState(_Enum):
                NotApplicable = 0
                NotInstalled = 1
                Installed = 2

            class TargetedContentAvailability(_Enum):
                None_ = 0
                Partial = 1
                All = 2

            class TargetedContentInteraction(_Enum):
                Impression = 0
                ClickThrough = 1
                Hover = 2
                Like = 3
                Dislike = 4
                Dismiss = 5
                Ineligible = 6
                Accept = 7
                Decline = 8
                Defer = 9
                Canceled = 10
                Conversion = 11
                Opportunity = 12

            class TargetedContentObjectKind(_Enum):
                Collection = 0
                Item = 1
                Value = 2

            class TargetedContentValueKind(_Enum):
                String = 0
                Uri = 1
                Number = 2
                Boolean = 3
                File = 4
                ImageFile = 5
                Action = 6
                Strings = 7
                Uris = 8
                Numbers = 9
                Booleans = 10
                Files = 11
                ImageFiles = 12
                Actions = 13

    class Storage:
        class ApplicationDataCreateDisposition(_Enum):
            Always = 0
            Existing = 1

        class ApplicationDataLocality(_Enum):
            Local = 0
            Roaming = 1
            Temporary = 2
            LocalCache = 3
            SharedLocal = 4

        class CreationCollisionOption(_Enum):
            GenerateUniqueName = 0
            ReplaceExisting = 1
            FailIfExists = 2
            OpenIfExists = 3

        class FileAccessMode(_Enum):
            Read = 0
            ReadWrite = 1

        class FileAttributes(_Enum):
            Normal = 0x0
            ReadOnly = 0x1
            Directory = 0x10
            Archive = 0x20
            Temporary = 0x100
            LocallyIncomplete = 0x200

        class KnownFolderId(_Enum):
            AppCaptures = 0
            CameraRoll = 1
            DocumentsLibrary = 2
            HomeGroup = 3
            MediaServerDevices = 4
            MusicLibrary = 5
            Objects3D = 6
            PicturesLibrary = 7
            Playlists = 8
            RecordedCalls = 9
            RemovableDevices = 10
            SavedPictures = 11
            Screenshots = 12
            VideosLibrary = 13
            AllAppMods = 14
            CurrentAppMods = 15
            DownloadsFolder = 16

        class KnownFoldersAccessStatus(_Enum):
            DeniedBySystem = 0
            NotDeclaredByApp = 1
            DeniedByUser = 2
            UserPromptRequired = 3
            Allowed = 4
            AllowedPerAppFolder = 5

        class KnownLibraryId(_Enum):
            Music = 0
            Pictures = 1
            Videos = 2
            Documents = 3

        class NameCollisionOption(_Enum):
            GenerateUniqueName = 0
            ReplaceExisting = 1
            FailIfExists = 2

        class StorageDeleteOption(_Enum):
            Default = 0
            PermanentDelete = 1

        class StorageItemTypes(_Enum):
            None_ = 0x0
            File = 0x1
            Folder = 0x2

        class StorageLibraryChangeType(_Enum):
            Created = 0
            Deleted = 1
            MovedOrRenamed = 2
            ContentsChanged = 3
            MovedOutOfLibrary = 4
            MovedIntoLibrary = 5
            ContentsReplaced = 6
            IndexingStatusChanged = 7
            EncryptionChanged = 8
            ChangeTrackingLost = 9

        class StorageOpenOptions(_Enum):
            None_ = 0x0
            AllowOnlyReaders = 0x1
            AllowReadersAndWriters = 0x2

        class StreamedFileFailureMode(_Enum):
            Failed = 0
            CurrentlyUnavailable = 1
            Incomplete = 2

        class AccessCache:
            class AccessCacheOptions(_Enum):
                None_ = 0x0
                DisallowUserInput = 0x1
                FastLocationsOnly = 0x2
                UseReadOnlyCachedCopy = 0x4
                SuppressAccessTimeUpdate = 0x8

            class RecentStorageItemVisibility(_Enum):
                AppOnly = 0
                AppAndSystem = 1

        class Compression:
            class CompressAlgorithm(_Enum):
                InvalidAlgorithm = 0
                NullAlgorithm = 1
                Mszip = 2
                Xpress = 3
                XpressHuff = 4
                Lzms = 5

        class FileProperties:
            class PhotoOrientation(_Enum):
                Unspecified = 0
                Normal = 1
                FlipHorizontal = 2
                Rotate180 = 3
                FlipVertical = 4
                Transpose = 5
                Rotate270 = 6
                Transverse = 7
                Rotate90 = 8

            class PropertyPrefetchOptions(_Enum):
                None_ = 0x0
                MusicProperties = 0x1
                VideoProperties = 0x2
                ImageProperties = 0x4
                DocumentProperties = 0x8
                BasicProperties = 0x10

            class ThumbnailMode(_Enum):
                PicturesView = 0
                VideosView = 1
                MusicView = 2
                DocumentsView = 3
                ListView = 4
                SingleItem = 5

            class ThumbnailOptions(_Enum):
                None_ = 0x0
                ReturnOnlyIfCached = 0x1
                ResizeThumbnail = 0x2
                UseCurrentScale = 0x4

            class ThumbnailType(_Enum):
                Image = 0
                Icon = 1

            class VideoOrientation(_Enum):
                Normal = 0
                Rotate90 = 90
                Rotate180 = 180
                Rotate270 = 270

        class Pickers:
            class PickerLocationId(_Enum):
                DocumentsLibrary = 0
                ComputerFolder = 1
                Desktop = 2
                Downloads = 3
                HomeGroup = 4
                MusicLibrary = 5
                PicturesLibrary = 6
                VideosLibrary = 7
                Objects3D = 8
                Unspecified = 9

            class PickerViewMode(_Enum):
                List = 0
                Thumbnail = 1

            class Provider:
                class AddFileResult(_Enum):
                    Added = 0
                    AlreadyAdded = 1
                    NotAllowed = 2
                    Unavailable = 3

                class FileSelectionMode(_Enum):
                    Single = 0
                    Multiple = 1

                class SetFileNameResult(_Enum):
                    Succeeded = 0
                    NotAllowed = 1
                    Unavailable = 2

        class Provider:
            class CachedFileOptions(_Enum):
                None_ = 0x0
                RequireUpdateOnAccess = 0x1
                UseCachedFileWhenOffline = 0x2
                DenyAccessWhenOffline = 0x4

            class CachedFileTarget(_Enum):
                Local = 0
                Remote = 1

            class FileUpdateStatus(_Enum):
                Incomplete = 0
                Complete = 1
                UserInputNeeded = 2
                CurrentlyUnavailable = 3
                Failed = 4
                CompleteAndRenamed = 5

            class ReadActivationMode(_Enum):
                NotNeeded = 0
                BeforeAccess = 1

            class StorageProviderHardlinkPolicy(_Enum):
                None_ = 0x0
                Allowed = 0x1

            class StorageProviderHydrationPolicy(_Enum):
                Partial = 0
                Progressive = 1
                Full = 2
                AlwaysFull = 3

            class StorageProviderHydrationPolicyModifier(_Enum):
                None_ = 0x0
                ValidationRequired = 0x1
                StreamingAllowed = 0x2
                AutoDehydrationAllowed = 0x4
                AllowFullRestartHydration = 0x8

            class StorageProviderInSyncPolicy(_Enum):
                Default = 0x0
                FileCreationTime = 0x1
                FileReadOnlyAttribute = 0x2
                FileHiddenAttribute = 0x4
                FileSystemAttribute = 0x8
                DirectoryCreationTime = 0x10
                DirectoryReadOnlyAttribute = 0x20
                DirectoryHiddenAttribute = 0x40
                DirectorySystemAttribute = 0x80
                FileLastWriteTime = 0x100
                DirectoryLastWriteTime = 0x200
                PreserveInsyncForSyncEngine = 0x80000000

            class StorageProviderPopulationPolicy(_Enum):
                Full = 1
                AlwaysFull = 2

            class StorageProviderProtectionMode(_Enum):
                Unknown = 0
                Personal = 1

            class StorageProviderState(_Enum):
                InSync = 0
                Syncing = 1
                Paused = 2
                Error = 3
                Warning = 4
                Offline = 5

            class StorageProviderUICommandState(_Enum):
                Enabled = 0
                Disabled = 1
                Hidden = 2

            class StorageProviderUriSourceStatus(_Enum):
                Success = 0
                NoSyncRoot = 1
                FileNotFound = 2

            class UIStatus(_Enum):
                Unavailable = 0
                Hidden = 1
                Visible = 2
                Complete = 3

            class WriteActivationMode(_Enum):
                ReadOnly = 0
                NotNeeded = 1
                AfterWrite = 2

        class Search:
            class CommonFileQuery(_Enum):
                DefaultQuery = 0
                OrderByName = 1
                OrderByTitle = 2
                OrderByMusicProperties = 3
                OrderBySearchRank = 4
                OrderByDate = 5

            class CommonFolderQuery(_Enum):
                DefaultQuery = 0
                GroupByYear = 100
                GroupByMonth = 101
                GroupByArtist = 102
                GroupByAlbum = 103
                GroupByAlbumArtist = 104
                GroupByComposer = 105
                GroupByGenre = 106
                GroupByPublishedYear = 107
                GroupByRating = 108
                GroupByTag = 109
                GroupByAuthor = 110
                GroupByType = 111

            class DateStackOption(_Enum):
                None_ = 0
                Year = 1
                Month = 2

            class FolderDepth(_Enum):
                Shallow = 0
                Deep = 1

            class IndexedState(_Enum):
                Unknown = 0
                NotIndexed = 1
                PartiallyIndexed = 2
                FullyIndexed = 3

            class IndexerOption(_Enum):
                UseIndexerWhenAvailable = 0
                OnlyUseIndexer = 1
                DoNotUseIndexer = 2
                OnlyUseIndexerAndOptimizeForIndexedProperties = 3

        class Streams:
            class ByteOrder(_Enum):
                LittleEndian = 0
                BigEndian = 1

            class FileOpenDisposition(_Enum):
                OpenExisting = 0
                OpenAlways = 1
                CreateNew = 2
                CreateAlways = 3
                TruncateExisting = 4

            class InputStreamOptions(_Enum):
                None_ = 0x0
                Partial = 0x1
                ReadAhead = 0x2

            class UnicodeEncoding(_Enum):
                Utf8 = 0
                Utf16LE = 1
                Utf16BE = 2

    class System:
        class AppDiagnosticInfoWatcherStatus(_Enum):
            Created = 0
            Started = 1
            EnumerationCompleted = 2
            Stopping = 3
            Stopped = 4
            Aborted = 5

        class AppMemoryUsageLevel(_Enum):
            Low = 0
            Medium = 1
            High = 2
            OverLimit = 3

        class AppResourceGroupEnergyQuotaState(_Enum):
            Unknown = 0
            Over = 1
            Under = 2

        class AppResourceGroupExecutionState(_Enum):
            Unknown = 0
            Running = 1
            Suspending = 2
            Suspended = 3
            NotRunning = 4

        class AppResourceGroupInfoWatcherStatus(_Enum):
            Created = 0
            Started = 1
            EnumerationCompleted = 2
            Stopping = 3
            Stopped = 4
            Aborted = 5

        class AutoUpdateTimeZoneStatus(_Enum):
            Attempted = 0
            TimedOut = 1
            Failed = 2

        class DiagnosticAccessStatus(_Enum):
            Unspecified = 0
            Denied = 1
            Limited = 2
            Allowed = 3

        class DispatcherQueuePriority(_Enum):
            Normal = 0
            High = 10

        class LaunchFileStatus(_Enum):
            Success = 0
            AppUnavailable = 1
            DeniedByPolicy = 2
            FileTypeNotSupported = 3
            Unknown = 4

        class LaunchQuerySupportStatus(_Enum):
            Available = 0
            AppNotInstalled = 1
            AppUnavailable = 2
            NotSupported = 3
            Unknown = 4

        class LaunchQuerySupportType(_Enum):
            Uri = 0
            UriForResults = 1

        class LaunchUriStatus(_Enum):
            Success = 0
            AppUnavailable = 1
            ProtocolUnavailable = 2
            Unknown = 3

        class PowerState(_Enum):
            ConnectedStandby = 0
            SleepS3 = 1

        class ProcessorArchitecture(_Enum):
            X86 = 0
            Arm = 5
            X64 = 9
            Neutral = 11
            Arm64 = 12
            X86OnArm64 = 14
            Unknown = 65535

        class RemoteLaunchUriStatus(_Enum):
            Unknown = 0
            Success = 1
            AppUnavailable = 2
            ProtocolUnavailable = 3
            RemoteSystemUnavailable = 4
            ValueSetTooLarge = 5
            DeniedByLocalSystem = 6
            DeniedByRemoteSystem = 7

        class ShutdownKind(_Enum):
            Shutdown = 0
            Restart = 1

        class UserAgeConsentGroup(_Enum):
            Child = 0
            Minor = 1
            Adult = 2

        class UserAgeConsentResult(_Enum):
            NotEnforced = 0
            Included = 1
            NotIncluded = 2
            Unknown = 3
            Ambiguous = 4

        class UserAuthenticationStatus(_Enum):
            Unauthenticated = 0
            LocallyAuthenticated = 1
            RemotelyAuthenticated = 2

        class UserPictureSize(_Enum):
            Size64x64 = 0
            Size208x208 = 1
            Size424x424 = 2
            Size1080x1080 = 3

        class UserType(_Enum):
            LocalUser = 0
            RemoteUser = 1
            LocalGuest = 2
            RemoteGuest = 3
            SystemManaged = 4

        class UserWatcherStatus(_Enum):
            Created = 0
            Started = 1
            EnumerationCompleted = 2
            Stopping = 3
            Stopped = 4
            Aborted = 5

        class UserWatcherUpdateKind(_Enum):
            Properties = 0
            Picture = 1

        class VirtualKey(_Enum):
            None_ = 0
            LeftButton = 1
            RightButton = 2
            Cancel = 3
            MiddleButton = 4
            XButton1 = 5
            XButton2 = 6
            Back = 8
            Tab = 9
            Clear = 12
            Enter = 13
            Shift = 16
            Control = 17
            Menu = 18
            Pause = 19
            CapitalLock = 20
            Kana = 21
            Hangul = 21
            ImeOn = 22
            Junja = 23
            Final = 24
            Hanja = 25
            Kanji = 25
            ImeOff = 26
            Escape = 27
            Convert = 28
            NonConvert = 29
            Accept = 30
            ModeChange = 31
            Space = 32
            PageUp = 33
            PageDown = 34
            End = 35
            Home = 36
            Left = 37
            Up = 38
            Right = 39
            Down = 40
            Select = 41
            Print = 42
            Execute = 43
            Snapshot = 44
            Insert = 45
            Delete = 46
            Help = 47
            Number0 = 48
            Number1 = 49
            Number2 = 50
            Number3 = 51
            Number4 = 52
            Number5 = 53
            Number6 = 54
            Number7 = 55
            Number8 = 56
            Number9 = 57
            A = 65
            B = 66
            C = 67
            D = 68
            E = 69
            F = 70
            G = 71
            H = 72
            I = 73  # noqa
            J = 74
            K = 75
            L = 76
            M = 77
            N = 78
            O = 79  # noqa
            P = 80
            Q = 81
            R = 82
            S = 83
            T = 84
            U = 85
            V = 86
            W = 87
            X = 88
            Y = 89
            Z = 90
            LeftWindows = 91
            RightWindows = 92
            Application = 93
            Sleep = 95
            NumberPad0 = 96
            NumberPad1 = 97
            NumberPad2 = 98
            NumberPad3 = 99
            NumberPad4 = 100
            NumberPad5 = 101
            NumberPad6 = 102
            NumberPad7 = 103
            NumberPad8 = 104
            NumberPad9 = 105
            Multiply = 106
            Add = 107
            Separator = 108
            Subtract = 109
            Decimal = 110
            Divide = 111
            F1 = 112
            F2 = 113
            F3 = 114
            F4 = 115
            F5 = 116
            F6 = 117
            F7 = 118
            F8 = 119
            F9 = 120
            F10 = 121
            F11 = 122
            F12 = 123
            F13 = 124
            F14 = 125
            F15 = 126
            F16 = 127
            F17 = 128
            F18 = 129
            F19 = 130
            F20 = 131
            F21 = 132
            F22 = 133
            F23 = 134
            F24 = 135
            NavigationView = 136
            NavigationMenu = 137
            NavigationUp = 138
            NavigationDown = 139
            NavigationLeft = 140
            NavigationRight = 141
            NavigationAccept = 142
            NavigationCancel = 143
            NumberKeyLock = 144
            Scroll = 145
            LeftShift = 160
            RightShift = 161
            LeftControl = 162
            RightControl = 163
            LeftMenu = 164
            RightMenu = 165
            GoBack = 166
            GoForward = 167
            Refresh = 168
            Stop = 169
            Search = 170
            Favorites = 171
            GoHome = 172
            GamepadA = 195
            GamepadB = 196
            GamepadX = 197
            GamepadY = 198
            GamepadRightShoulder = 199
            GamepadLeftShoulder = 200
            GamepadLeftTrigger = 201
            GamepadRightTrigger = 202
            GamepadDPadUp = 203
            GamepadDPadDown = 204
            GamepadDPadLeft = 205
            GamepadDPadRight = 206
            GamepadMenu = 207
            GamepadView = 208
            GamepadLeftThumbstickButton = 209
            GamepadRightThumbstickButton = 210
            GamepadLeftThumbstickUp = 211
            GamepadLeftThumbstickDown = 212
            GamepadLeftThumbstickRight = 213
            GamepadLeftThumbstickLeft = 214
            GamepadRightThumbstickUp = 215
            GamepadRightThumbstickDown = 216
            GamepadRightThumbstickRight = 217
            GamepadRightThumbstickLeft = 218

        class VirtualKeyModifiers(_Enum):
            None_ = 0x0
            Control = 0x1
            Menu = 0x2
            Shift = 0x4
            Windows = 0x8

        class Diagnostics:
            class DiagnosticActionState(_Enum):
                Initializing = 0
                Downloading = 1
                VerifyingTrust = 2
                Detecting = 3
                Resolving = 4
                VerifyingResolution = 5
                Executing = 6

            class DevicePortal:
                class DevicePortalConnectionClosedReason(_Enum):
                    Unknown = 0
                    ResourceLimitsExceeded = 1
                    ProtocolError = 2
                    NotAuthorized = 3
                    UserNotPresent = 4
                    ServiceTerminated = 5

            class Telemetry:
                class PlatformTelemetryRegistrationStatus(_Enum):
                    Success = 0
                    SettingsOutOfRange = 1
                    UnknownFailure = 2

            class TraceReporting:
                class PlatformDiagnosticActionState(_Enum):
                    Success = 0
                    FreeNetworkNotAvailable = 1
                    ACPowerNotAvailable = 2

                class PlatformDiagnosticEscalationType(_Enum):
                    OnCompletion = 0
                    OnFailure = 1

                class PlatformDiagnosticEventBufferLatencies(_Enum):
                    Normal = 0x1
                    CostDeferred = 0x2
                    Realtime = 0x4

                class PlatformDiagnosticTracePriority(_Enum):
                    Normal = 0
                    UserElevated = 1

                class PlatformDiagnosticTraceSlotState(_Enum):
                    NotRunning = 0
                    Running = 1
                    Throttled = 2

                class PlatformDiagnosticTraceSlotType(_Enum):
                    Alternative = 0
                    AlwaysOn = 1
                    Mini = 2

        class Power:
            class BatteryStatus(_Enum):
                NotPresent = 0
                Discharging = 1
                Idle = 2
                Charging = 3

            class EnergySaverStatus(_Enum):
                Disabled = 0
                Off = 1
                On = 2

            class PowerSupplyStatus(_Enum):
                NotPresent = 0
                Inadequate = 1
                Adequate = 2

        class Preview:
            class HingeState(_Enum):
                Unknown = 0
                Closed = 1
                Concave = 2
                Flat = 3
                Convex = 4
                Full = 5

        class Profile:
            class PlatformDataCollectionLevel(_Enum):
                Security = 0
                Basic = 1
                Enhanced = 2
                Full = 3

            class SystemIdentificationSource(_Enum):
                None_ = 0
                Tpm = 1
                Uefi = 2
                Registry = 3

            class SystemOutOfBoxExperienceState(_Enum):
                NotStarted = 0
                InProgress = 1
                Completed = 2

            class UnsupportedAppRequirementReasons(_Enum):
                Unknown = 0x0
                DeniedBySystem = 0x1

        class RemoteSystems:
            class RemoteSystemAccessStatus(_Enum):
                Unspecified = 0
                Allowed = 1
                DeniedByUser = 2
                DeniedBySystem = 3

            class RemoteSystemAuthorizationKind(_Enum):
                SameUser = 0
                Anonymous = 1

            class RemoteSystemDiscoveryType(_Enum):
                Any = 0
                Proximal = 1
                Cloud = 2
                SpatiallyProximal = 3

            class RemoteSystemPlatform(_Enum):
                Unknown = 0
                Windows = 1
                Android = 2
                Ios = 3
                Linux = 4

            class RemoteSystemSessionCreationStatus(_Enum):
                Success = 0
                SessionLimitsExceeded = 1
                OperationAborted = 2

            class RemoteSystemSessionDisconnectedReason(_Enum):
                SessionUnavailable = 0
                RemovedByController = 1
                SessionClosed = 2

            class RemoteSystemSessionJoinStatus(_Enum):
                Success = 0
                SessionLimitsExceeded = 1
                OperationAborted = 2
                SessionUnavailable = 3
                RejectedByController = 4

            class RemoteSystemSessionMessageChannelReliability(_Enum):
                Reliable = 0
                Unreliable = 1

            class RemoteSystemSessionParticipantWatcherStatus(_Enum):
                Created = 0
                Started = 1
                EnumerationCompleted = 2
                Stopping = 3
                Stopped = 4
                Aborted = 5

            class RemoteSystemSessionWatcherStatus(_Enum):
                Created = 0
                Started = 1
                EnumerationCompleted = 2
                Stopping = 3
                Stopped = 4
                Aborted = 5

            class RemoteSystemStatus(_Enum):
                Unavailable = 0
                DiscoveringAvailability = 1
                Available = 2
                Unknown = 3

            class RemoteSystemStatusType(_Enum):
                Any = 0
                Available = 1

            class RemoteSystemWatcherError(_Enum):
                Unknown = 0
                InternetNotAvailable = 1
                AuthenticationError = 2

        class Threading:
            class WorkItemOptions(_Enum):
                None_ = 0x0
                TimeSliced = 0x1

            class WorkItemPriority(_Enum):
                Normal = 0
                High = 1

        class Update:
            class SystemUpdateAttentionRequiredReason(_Enum):
                None_ = 0
                NetworkRequired = 1
                InsufficientDiskSpace = 2
                InsufficientBattery = 3
                UpdateBlocked = 4

            class SystemUpdateItemState(_Enum):
                NotStarted = 0
                Initializing = 1
                Preparing = 2
                Calculating = 3
                Downloading = 4
                Installing = 5
                Completed = 6
                RebootRequired = 7
                Error = 8

            class SystemUpdateManagerState(_Enum):
                Idle = 0
                Detecting = 1
                ReadyToDownload = 2
                Downloading = 3
                ReadyToInstall = 4
                Installing = 5
                RebootRequired = 6
                ReadyToFinalize = 7
                Finalizing = 8
                Completed = 9
                AttentionRequired = 10
                Error = 11

            class SystemUpdateStartInstallAction(_Enum):
                UpToReboot = 0
                AllowReboot = 1

        class UserProfile:
            class AccountPictureKind(_Enum):
                SmallImage = 0
                LargeImage = 1
                Video = 2

            class SetAccountPictureResult(_Enum):
                Success = 0
                ChangeDisabled = 1
                LargeOrDynamicError = 2
                VideoFrameSizeError = 3
                FileSizeError = 4
                Failure = 5

            class SetImageFeedResult(_Enum):
                Success = 0
                ChangeDisabled = 1
                UserCanceled = 2

    class UI:
        class ApplicationSettings:
            class SettingsEdgeLocation(_Enum):
                Right = 0
                Left = 1

            class SupportedWebAccountActions(_Enum):
                None_ = 0x0
                Reconnect = 0x1
                Remove = 0x2
                ViewDetails = 0x4
                Manage = 0x8
                More = 0x10

            class WebAccountAction(_Enum):
                Reconnect = 0
                Remove = 1
                ViewDetails = 2
                Manage = 3
                More = 4

        class Composition:
            class AnimationControllerProgressBehavior(_Enum):
                Default = 0
                IncludesDelayTime = 1

            class AnimationDelayBehavior(_Enum):
                SetInitialValueAfterDelay = 0
                SetInitialValueBeforeDelay = 1

            class AnimationDirection(_Enum):
                Normal = 0
                Reverse = 1
                Alternate = 2
                AlternateReverse = 3

            class AnimationIterationBehavior(_Enum):
                Count = 0
                Forever = 1

            class AnimationPropertyAccessMode(_Enum):
                None_ = 0
                ReadOnly = 1
                WriteOnly = 2
                ReadWrite = 3

            class AnimationStopBehavior(_Enum):
                LeaveCurrentValue = 0
                SetToInitialValue = 1
                SetToFinalValue = 2

            class CompositionBackfaceVisibility(_Enum):
                Inherit = 0
                Visible = 1
                Hidden = 2

            class CompositionBatchTypes(_Enum):
                None_ = 0x0
                Animation = 0x1
                Effect = 0x2
                InfiniteAnimation = 0x4
                AllAnimations = 0x5

            class CompositionBitmapInterpolationMode(_Enum):
                NearestNeighbor = 0
                Linear = 1
                MagLinearMinLinearMipLinear = 2
                MagLinearMinLinearMipNearest = 3
                MagLinearMinNearestMipLinear = 4
                MagLinearMinNearestMipNearest = 5
                MagNearestMinLinearMipLinear = 6
                MagNearestMinLinearMipNearest = 7
                MagNearestMinNearestMipLinear = 8
                MagNearestMinNearestMipNearest = 9

            class CompositionBorderMode(_Enum):
                Inherit = 0
                Soft = 1
                Hard = 2

            class CompositionColorSpace(_Enum):
                Auto = 0
                Hsl = 1
                Rgb = 2
                HslLinear = 3
                RgbLinear = 4

            class CompositionCompositeMode(_Enum):
                Inherit = 0
                SourceOver = 1
                DestinationInvert = 2
                MinBlend = 3

            class CompositionDropShadowSourcePolicy(_Enum):
                Default = 0
                InheritFromVisualContent = 1

            class CompositionEasingFunctionMode(_Enum):
                In = 0
                Out = 1
                InOut = 2

            class CompositionEffectFactoryLoadStatus(_Enum):
                Success = 0
                EffectTooComplex = 1
                Pending = 2

            class CompositionGetValueStatus(_Enum):
                Succeeded = 0
                TypeMismatch = 1
                NotFound = 2

            class CompositionGradientExtendMode(_Enum):
                Clamp = 0
                Wrap = 1
                Mirror = 2

            class CompositionMappingMode(_Enum):
                Absolute = 0
                Relative = 1

            class CompositionStretch(_Enum):
                None_ = 0
                Fill = 1
                Uniform = 2
                UniformToFill = 3

            class CompositionStrokeCap(_Enum):
                Flat = 0
                Square = 1
                Round = 2
                Triangle = 3

            class CompositionStrokeLineJoin(_Enum):
                Miter = 0
                Bevel = 1
                Round = 2
                MiterOrBevel = 3

            class Diagnostics:
                class CompositionDebugOverdrawContentKinds(_Enum):
                    None_ = 0x0
                    OffscreenRendered = 0x1
                    Colors = 0x2
                    Effects = 0x4
                    Shadows = 0x8
                    Lights = 0x10
                    Surfaces = 0x20
                    SwapChains = 0x40

            class Effects:
                class SceneLightingEffectReflectanceModel(_Enum):
                    BlinnPhong = 0
                    PhysicallyBasedBlinnPhong = 1

            class Interactions:
                class InteractionBindingAxisModes(_Enum):
                    None_ = 0x0
                    PositionX = 0x1
                    PositionY = 0x2
                    Scale = 0x4

                class InteractionChainingMode(_Enum):
                    Auto = 0
                    Always = 1
                    Never = 2

                class InteractionSourceMode(_Enum):
                    Disabled = 0
                    EnabledWithInertia = 1
                    EnabledWithoutInertia = 2

                class InteractionSourceRedirectionMode(_Enum):
                    Disabled = 0
                    Enabled = 1

                class InteractionTrackerClampingOption(_Enum):
                    Auto = 0
                    Disabled = 1

                class InteractionTrackerPositionUpdateOption(_Enum):
                    Default = 0
                    AllowActiveCustomScaleAnimation = 1

                class VisualInteractionSourceRedirectionMode(_Enum):
                    Off = 0
                    CapableTouchpadOnly = 1
                    PointerWheelOnly = 2
                    CapableTouchpadAndPointerWheel = 3

            class Scenes:
                class SceneAlphaMode(_Enum):
                    Opaque = 0
                    AlphaTest = 1
                    Blend = 2

                class SceneAttributeSemantic(_Enum):
                    Index = 0
                    Vertex = 1
                    Normal = 2
                    TexCoord0 = 3
                    TexCoord1 = 4
                    Color = 5
                    Tangent = 6

                class SceneComponentType(_Enum):
                    MeshRendererComponent = 0

                class SceneWrappingMode(_Enum):
                    ClampToEdge = 0
                    MirroredRepeat = 1
                    Repeat = 2

        class Core:
            class AppViewBackButtonVisibility(_Enum):
                Visible = 0
                Collapsed = 1
                Disabled = 2

            class CoreAcceleratorKeyEventType(_Enum):
                Character = 2
                DeadCharacter = 3
                KeyDown = 0
                KeyUp = 1
                SystemCharacter = 6
                SystemDeadCharacter = 7
                SystemKeyDown = 4
                SystemKeyUp = 5
                UnicodeCharacter = 8

            class CoreCursorType(_Enum):
                Arrow = 0
                Cross = 1
                Custom = 2
                Hand = 3
                Help = 4
                IBeam = 5
                SizeAll = 6
                SizeNortheastSouthwest = 7
                SizeNorthSouth = 8
                SizeNorthwestSoutheast = 9
                SizeWestEast = 10
                UniversalNo = 11
                UpArrow = 12
                Wait = 13
                Pin = 14
                Person = 15

            class CoreDispatcherPriority(_Enum):
                Normal = 0
                High = 1

            class CoreIndependentInputFilters(_Enum):
                None_ = 0x0
                MouseButton = 0x1
                MouseWheel = 0x2
                MouseHover = 0x4
                PenWithBarrel = 0x8
                PenInverted = 0x10

            class CoreInputDeviceTypes(_Enum):
                None_ = 0x0
                Touch = 0x1
                Pen = 0x2
                Mouse = 0x4

            class CoreProcessEventsOption(_Enum):
                ProcessOneAndAllPending = 0
                ProcessOneIfPresent = 1
                ProcessUntilQuit = 2
                ProcessAllIfPresent = 3

            class CoreProximityEvaluationScore(_Enum):
                Closest = 0
                Farthest = 2147483647

            class CoreVirtualKeyStates(_Enum):
                None_ = 0x0
                Down = 0x1
                Locked = 0x2

            class CoreWindowActivationMode(_Enum):
                None_ = 0
                Deactivated = 1
                ActivatedNotForeground = 2
                ActivatedInForeground = 3

            class CoreWindowActivationState(_Enum):
                CodeActivated = 0
                Deactivated = 1
                PointerActivated = 2

            class CoreWindowFlowDirection(_Enum):
                LeftToRight = 0
                RightToLeft = 1

            class AnimationMetrics:
                class AnimationEffect(_Enum):
                    Expand = 0
                    Collapse = 1
                    Reposition = 2
                    FadeIn = 3
                    FadeOut = 4
                    AddToList = 5
                    DeleteFromList = 6
                    AddToGrid = 7
                    DeleteFromGrid = 8
                    AddToSearchGrid = 9
                    DeleteFromSearchGrid = 10
                    AddToSearchList = 11
                    DeleteFromSearchList = 12
                    ShowEdgeUI = 13
                    ShowPanel = 14
                    HideEdgeUI = 15
                    HidePanel = 16
                    ShowPopup = 17
                    HidePopup = 18
                    PointerDown = 19
                    PointerUp = 20
                    DragSourceStart = 21
                    DragSourceEnd = 22
                    TransitionContent = 23
                    Reveal = 24
                    Hide = 25
                    DragBetweenEnter = 26
                    DragBetweenLeave = 27
                    SwipeSelect = 28
                    SwipeDeselect = 29
                    SwipeReveal = 30
                    EnterPage = 31
                    TransitionPage = 32
                    CrossFade = 33
                    Peek = 34
                    UpdateBadge = 35

                class AnimationEffectTarget(_Enum):
                    Primary = 0
                    Added = 1
                    Affected = 2
                    Background = 3
                    Content = 4
                    Deleted = 5
                    Deselected = 6
                    DragSource = 7
                    Hidden = 8
                    Incoming = 9
                    Outgoing = 10
                    Outline = 11
                    Remaining = 12
                    Revealed = 13
                    RowIn = 14
                    RowOut = 15
                    Selected = 16
                    Selection = 17
                    Shown = 18
                    Tapped = 19

                class PropertyAnimationType(_Enum):
                    Scale = 0
                    Translation = 1
                    Opacity = 2

        class Input:
            class CrossSlidingState(_Enum):
                Started = 0
                Dragging = 1
                Selecting = 2
                SelectSpeedBumping = 3
                SpeedBumping = 4
                Rearranging = 5
                Completed = 6

            class DraggingState(_Enum):
                Started = 0
                Continuing = 1
                Completed = 2

            class EdgeGestureKind(_Enum):
                Touch = 0
                Keyboard = 1
                Mouse = 2

            class GazeInputAccessStatus(_Enum):
                Unspecified = 0
                Allowed = 1
                DeniedByUser = 2
                DeniedBySystem = 3

            class GestureSettings(_Enum):
                None_ = 0x0
                Tap = 0x1
                DoubleTap = 0x2
                Hold = 0x4
                HoldWithMouse = 0x8
                RightTap = 0x10
                Drag = 0x20
                ManipulationTranslateX = 0x40
                ManipulationTranslateY = 0x80
                ManipulationTranslateRailsX = 0x100
                ManipulationTranslateRailsY = 0x200
                ManipulationRotate = 0x400
                ManipulationScale = 0x800
                ManipulationTranslateInertia = 0x1000
                ManipulationRotateInertia = 0x2000
                ManipulationScaleInertia = 0x4000
                CrossSlide = 0x8000
                ManipulationMultipleFingerPanning = 0x10000

            class HoldingState(_Enum):
                Started = 0
                Completed = 1
                Canceled = 2

            class InputActivationState(_Enum):
                None_ = 0
                Deactivated = 1
                ActivatedNotForeground = 2
                ActivatedInForeground = 3

            class PointerUpdateKind(_Enum):
                Other = 0
                LeftButtonPressed = 1
                LeftButtonReleased = 2
                RightButtonPressed = 3
                RightButtonReleased = 4
                MiddleButtonPressed = 5
                MiddleButtonReleased = 6
                XButton1Pressed = 7
                XButton1Released = 8
                XButton2Pressed = 9
                XButton2Released = 10

            class RadialControllerMenuKnownIcon(_Enum):
                Scroll = 0
                Zoom = 1
                UndoRedo = 2
                Volume = 3
                NextPreviousTrack = 4
                Ruler = 5
                InkColor = 6
                InkThickness = 7
                PenType = 8

            class RadialControllerSystemMenuItemKind(_Enum):
                Scroll = 0
                Zoom = 1
                UndoRedo = 2
                Volume = 3
                NextPreviousTrack = 4

            class Inking:
                class HandwritingLineHeight(_Enum):
                    Small = 0
                    Medium = 1
                    Large = 2

                class InkDrawingAttributesKind(_Enum):
                    Default = 0
                    Pencil = 1

                class InkHighContrastAdjustment(_Enum):
                    UseSystemColorsWhenNecessary = 0
                    UseSystemColors = 1
                    UseOriginalColors = 2

                class InkInputProcessingMode(_Enum):
                    None_ = 0
                    Inking = 1
                    Erasing = 2

                class InkInputRightDragAction(_Enum):
                    LeaveUnprocessed = 0
                    AllowProcessing = 1

                class InkManipulationMode(_Enum):
                    Inking = 0
                    Erasing = 1
                    Selecting = 2

                class InkPersistenceFormat(_Enum):
                    GifWithEmbeddedIsf = 0
                    Isf = 1

                class InkPresenterPredefinedConfiguration(_Enum):
                    SimpleSinglePointer = 0
                    SimpleMultiplePointer = 1

                class InkPresenterStencilKind(_Enum):
                    Other = 0
                    Ruler = 1
                    Protractor = 2

                class InkRecognitionTarget(_Enum):
                    All = 0
                    Selected = 1
                    Recent = 2

                class PenHandedness(_Enum):
                    Right = 0
                    Left = 1

                class PenTipShape(_Enum):
                    Circle = 0
                    Rectangle = 1

                class Analysis:
                    class InkAnalysisDrawingKind(_Enum):
                        Drawing = 0
                        Circle = 1
                        Ellipse = 2
                        Triangle = 3
                        IsoscelesTriangle = 4
                        EquilateralTriangle = 5
                        RightTriangle = 6
                        Quadrilateral = 7
                        Rectangle = 8
                        Square = 9
                        Diamond = 10
                        Trapezoid = 11
                        Parallelogram = 12
                        Pentagon = 13
                        Hexagon = 14

                    class InkAnalysisNodeKind(_Enum):
                        UnclassifiedInk = 0
                        Root = 1
                        WritingRegion = 2
                        Paragraph = 3
                        Line = 4
                        InkWord = 5
                        InkBullet = 6
                        InkDrawing = 7
                        ListItem = 8

                    class InkAnalysisStatus(_Enum):
                        Updated = 0
                        Unchanged = 1

                    class InkAnalysisStrokeKind(_Enum):
                        Auto = 0
                        Writing = 1
                        Drawing = 2

                class Core:
                    class CoreWetStrokeDisposition(_Enum):
                        Inking = 0
                        Completed = 1
                        Canceled = 2

            class Preview:
                class Injection:
                    class InjectedInputButtonChangeKind(_Enum):
                        None_ = 0
                        FirstButtonDown = 1
                        FirstButtonUp = 2
                        SecondButtonDown = 3
                        SecondButtonUp = 4
                        ThirdButtonDown = 5
                        ThirdButtonUp = 6
                        FourthButtonDown = 7
                        FourthButtonUp = 8
                        FifthButtonDown = 9
                        FifthButtonUp = 10

                    class InjectedInputKeyOptions(_Enum):
                        None_ = 0x0
                        ExtendedKey = 0x1
                        KeyUp = 0x2
                        ScanCode = 0x8
                        Unicode = 0x4

                    class InjectedInputMouseOptions(_Enum):
                        None_ = 0x0
                        Move = 0x1
                        LeftDown = 0x2
                        LeftUp = 0x4
                        RightDown = 0x8
                        RightUp = 0x10
                        MiddleDown = 0x20
                        MiddleUp = 0x40
                        XDown = 0x80
                        XUp = 0x100
                        Wheel = 0x800
                        HWheel = 0x1000
                        MoveNoCoalesce = 0x2000
                        VirtualDesk = 0x4000
                        Absolute = 0x8000

                    class InjectedInputPenButtons(_Enum):
                        None_ = 0x0
                        Barrel = 0x1
                        Inverted = 0x2
                        Eraser = 0x4

                    class InjectedInputPenParameters(_Enum):
                        None_ = 0x0
                        Pressure = 0x1
                        Rotation = 0x2
                        TiltX = 0x4
                        TiltY = 0x8

                    class InjectedInputPointerOptions(_Enum):
                        None_ = 0x0
                        New = 0x1
                        InRange = 0x2
                        InContact = 0x4
                        FirstButton = 0x10
                        SecondButton = 0x20
                        Primary = 0x2000
                        Confidence = 0x4000
                        Canceled = 0x8000
                        PointerDown = 0x10000
                        Update = 0x20000
                        PointerUp = 0x40000
                        CaptureChanged = 0x200000

                    class InjectedInputShortcut(_Enum):
                        Back = 0
                        Start = 1
                        Search = 2

                    class InjectedInputTouchParameters(_Enum):
                        None_ = 0x0
                        Contact = 0x1
                        Orientation = 0x2
                        Pressure = 0x4

                    class InjectedInputVisualizationMode(_Enum):
                        None_ = 0
                        Default = 1
                        Indirect = 2

            class Spatial:
                class SpatialGestureSettings(_Enum):
                    None_ = 0x0
                    Tap = 0x1
                    DoubleTap = 0x2
                    Hold = 0x4
                    ManipulationTranslate = 0x8
                    NavigationX = 0x10
                    NavigationY = 0x20
                    NavigationZ = 0x40
                    NavigationRailsX = 0x80
                    NavigationRailsY = 0x100
                    NavigationRailsZ = 0x200

                class SpatialInteractionPressKind(_Enum):
                    None_ = 0
                    Select = 1
                    Menu = 2
                    Grasp = 3
                    Touchpad = 4
                    Thumbstick = 5

                class SpatialInteractionSourceHandedness(_Enum):
                    Unspecified = 0
                    Left = 1
                    Right = 2

                class SpatialInteractionSourceKind(_Enum):
                    Other = 0
                    Hand = 1
                    Voice = 2
                    Controller = 3

                class SpatialInteractionSourcePositionAccuracy(_Enum):
                    High = 0
                    Approximate = 1

        class Notifications:
            class AdaptiveNotificationContentKind(_Enum):
                Text = 0

            class BadgeTemplateType(_Enum):
                BadgeGlyph = 0
                BadgeNumber = 1

            class NotificationKinds(_Enum):
                Unknown = 0x0
                Toast = 0x1

            class NotificationMirroring(_Enum):
                Allowed = 0
                Disabled = 1

            class NotificationSetting(_Enum):
                Enabled = 0
                DisabledForApplication = 1
                DisabledForUser = 2
                DisabledByGroupPolicy = 3
                DisabledByManifest = 4

            class NotificationUpdateResult(_Enum):
                Succeeded = 0
                Failed = 1
                NotificationNotFound = 2

            class PeriodicUpdateRecurrence(_Enum):
                HalfHour = 0
                Hour = 1
                SixHours = 2
                TwelveHours = 3
                Daily = 4

            class TileFlyoutTemplateType(_Enum):
                TileFlyoutTemplate01 = 0

            class TileTemplateType(_Enum):
                TileSquareImage = 0
                TileSquareBlock = 1
                TileSquareText01 = 2
                TileSquareText02 = 3
                TileSquareText03 = 4
                TileSquareText04 = 5
                TileSquarePeekImageAndText01 = 6
                TileSquarePeekImageAndText02 = 7
                TileSquarePeekImageAndText03 = 8
                TileSquarePeekImageAndText04 = 9
                TileWideImage = 10
                TileWideImageCollection = 11
                TileWideImageAndText01 = 12
                TileWideImageAndText02 = 13
                TileWideBlockAndText01 = 14
                TileWideBlockAndText02 = 15
                TileWidePeekImageCollection01 = 16
                TileWidePeekImageCollection02 = 17
                TileWidePeekImageCollection03 = 18
                TileWidePeekImageCollection04 = 19
                TileWidePeekImageCollection05 = 20
                TileWidePeekImageCollection06 = 21
                TileWidePeekImageAndText01 = 22
                TileWidePeekImageAndText02 = 23
                TileWidePeekImage01 = 24
                TileWidePeekImage02 = 25
                TileWidePeekImage03 = 26
                TileWidePeekImage04 = 27
                TileWidePeekImage05 = 28
                TileWidePeekImage06 = 29
                TileWideSmallImageAndText01 = 30
                TileWideSmallImageAndText02 = 31
                TileWideSmallImageAndText03 = 32
                TileWideSmallImageAndText04 = 33
                TileWideSmallImageAndText05 = 34
                TileWideText01 = 35
                TileWideText02 = 36
                TileWideText03 = 37
                TileWideText04 = 38
                TileWideText05 = 39
                TileWideText06 = 40
                TileWideText07 = 41
                TileWideText08 = 42
                TileWideText09 = 43
                TileWideText10 = 44
                TileWideText11 = 45
                TileSquare150x150Image = 0
                TileSquare150x150Block = 1
                TileSquare150x150Text01 = 2
                TileSquare150x150Text02 = 3
                TileSquare150x150Text03 = 4
                TileSquare150x150Text04 = 5
                TileSquare150x150PeekImageAndText01 = 6
                TileSquare150x150PeekImageAndText02 = 7
                TileSquare150x150PeekImageAndText03 = 8
                TileSquare150x150PeekImageAndText04 = 9
                TileWide310x150Image = 10
                TileWide310x150ImageCollection = 11
                TileWide310x150ImageAndText01 = 12
                TileWide310x150ImageAndText02 = 13
                TileWide310x150BlockAndText01 = 14
                TileWide310x150BlockAndText02 = 15
                TileWide310x150PeekImageCollection01 = 16
                TileWide310x150PeekImageCollection02 = 17
                TileWide310x150PeekImageCollection03 = 18
                TileWide310x150PeekImageCollection04 = 19
                TileWide310x150PeekImageCollection05 = 20
                TileWide310x150PeekImageCollection06 = 21
                TileWide310x150PeekImageAndText01 = 22
                TileWide310x150PeekImageAndText02 = 23
                TileWide310x150PeekImage01 = 24
                TileWide310x150PeekImage02 = 25
                TileWide310x150PeekImage03 = 26
                TileWide310x150PeekImage04 = 27
                TileWide310x150PeekImage05 = 28
                TileWide310x150PeekImage06 = 29
                TileWide310x150SmallImageAndText01 = 30
                TileWide310x150SmallImageAndText02 = 31
                TileWide310x150SmallImageAndText03 = 32
                TileWide310x150SmallImageAndText04 = 33
                TileWide310x150SmallImageAndText05 = 34
                TileWide310x150Text01 = 35
                TileWide310x150Text02 = 36
                TileWide310x150Text03 = 37
                TileWide310x150Text04 = 38
                TileWide310x150Text05 = 39
                TileWide310x150Text06 = 40
                TileWide310x150Text07 = 41
                TileWide310x150Text08 = 42
                TileWide310x150Text09 = 43
                TileWide310x150Text10 = 44
                TileWide310x150Text11 = 45
                TileSquare310x310BlockAndText01 = 46
                TileSquare310x310BlockAndText02 = 47
                TileSquare310x310Image = 48
                TileSquare310x310ImageAndText01 = 49
                TileSquare310x310ImageAndText02 = 50
                TileSquare310x310ImageAndTextOverlay01 = 51
                TileSquare310x310ImageAndTextOverlay02 = 52
                TileSquare310x310ImageAndTextOverlay03 = 53
                TileSquare310x310ImageCollectionAndText01 = 54
                TileSquare310x310ImageCollectionAndText02 = 55
                TileSquare310x310ImageCollection = 56
                TileSquare310x310SmallImagesAndTextList01 = 57
                TileSquare310x310SmallImagesAndTextList02 = 58
                TileSquare310x310SmallImagesAndTextList03 = 59
                TileSquare310x310SmallImagesAndTextList04 = 60
                TileSquare310x310Text01 = 61
                TileSquare310x310Text02 = 62
                TileSquare310x310Text03 = 63
                TileSquare310x310Text04 = 64
                TileSquare310x310Text05 = 65
                TileSquare310x310Text06 = 66
                TileSquare310x310Text07 = 67
                TileSquare310x310Text08 = 68
                TileSquare310x310TextList01 = 69
                TileSquare310x310TextList02 = 70
                TileSquare310x310TextList03 = 71
                TileSquare310x310SmallImageAndText01 = 72
                TileSquare310x310SmallImagesAndTextList05 = 73
                TileSquare310x310Text09 = 74
                TileSquare71x71IconWithBadge = 75
                TileSquare150x150IconWithBadge = 76
                TileWide310x150IconWithBadgeAndText = 77
                TileSquare71x71Image = 78
                TileTall150x310Image = 79

            class ToastDismissalReason(_Enum):
                UserCanceled = 0
                ApplicationHidden = 1
                TimedOut = 2

            class ToastHistoryChangedType(_Enum):
                Cleared = 0
                Removed = 1
                Expired = 2
                Added = 3

            class ToastNotificationMode(_Enum):
                Unrestricted = 0
                PriorityOnly = 1
                AlarmsOnly = 2

            class ToastNotificationPriority(_Enum):
                Default = 0
                High = 1

            class ToastTemplateType(_Enum):
                ToastImageAndText01 = 0
                ToastImageAndText02 = 1
                ToastImageAndText03 = 2
                ToastImageAndText04 = 3
                ToastText01 = 4
                ToastText02 = 5
                ToastText03 = 6
                ToastText04 = 7

            class UserNotificationChangedKind(_Enum):
                Added = 0
                Removed = 1

            class Management:
                class UserNotificationListenerAccessStatus(_Enum):
                    Unspecified = 0
                    Allowed = 1
                    Denied = 2

        class Popups:
            class MessageDialogOptions(_Enum):
                None_ = 0x0
                AcceptUserInputAfterDelay = 0x1

            class Placement(_Enum):
                Default = 0
                Above = 1
                Below = 2
                Left = 3
                Right = 4

        class Shell:
            class SecurityAppKind(_Enum):
                WebProtection = 0

            class SecurityAppState(_Enum):
                Disabled = 0
                Enabled = 1

            class SecurityAppSubstatus(_Enum):
                Undetermined = 0
                NoActionNeeded = 1
                ActionRecommended = 2
                ActionNeeded = 3

            class ShareWindowCommand(_Enum):
                None_ = 0
                StartSharing = 1
                StopSharing = 2

        class StartScreen:
            class ForegroundText(_Enum):
                Dark = 0
                Light = 1

            class JumpListItemKind(_Enum):
                Arguments = 0
                Separator = 1

            class JumpListSystemGroupKind(_Enum):
                None_ = 0
                Frequent = 1
                Recent = 2

            class TileMixedRealityModelActivationBehavior(_Enum):
                Default = 0
                None_ = 1

            class TileOptions(_Enum):
                None_ = 0x0
                ShowNameOnLogo = 0x1
                ShowNameOnWideLogo = 0x2
                CopyOnDeployment = 0x4

            class TileSize(_Enum):
                Default = 0
                Square30x30 = 1
                Square70x70 = 2
                Square150x150 = 3
                Wide310x150 = 4
                Square310x310 = 5
                Square71x71 = 6
                Square44x44 = 7

        class Text:
            class CaretType(_Enum):
                Normal = 0
                Null = 1

            class FindOptions(_Enum):
                None_ = 0x0
                Word = 0x2
                Case = 0x4

            class FontStretch(_Enum):
                Undefined = 0
                UltraCondensed = 1
                ExtraCondensed = 2
                Condensed = 3
                SemiCondensed = 4
                Normal = 5
                SemiExpanded = 6
                Expanded = 7
                ExtraExpanded = 8
                UltraExpanded = 9

            class FontStyle(_Enum):
                Normal = 0
                Oblique = 1
                Italic = 2

            class FormatEffect(_Enum):
                Off = 0
                On = 1
                Toggle = 2
                Undefined = 3

            class HorizontalCharacterAlignment(_Enum):
                Left = 0
                Right = 1
                Center = 2

            class LetterCase(_Enum):
                Lower = 0
                Upper = 1

            class LineSpacingRule(_Enum):
                Undefined = 0
                Single = 1
                OneAndHalf = 2
                Double = 3
                AtLeast = 4
                Exactly = 5
                Multiple = 6
                Percent = 7

            class LinkType(_Enum):
                Undefined = 0
                NotALink = 1
                ClientLink = 2
                FriendlyLinkName = 3
                FriendlyLinkAddress = 4
                AutoLink = 5
                AutoLinkEmail = 6
                AutoLinkPhone = 7
                AutoLinkPath = 8

            class MarkerAlignment(_Enum):
                Undefined = 0
                Left = 1
                Center = 2
                Right = 3

            class MarkerStyle(_Enum):
                Undefined = 0
                Parenthesis = 1
                Parentheses = 2
                Period = 3
                Plain = 4
                Minus = 5
                NoNumber = 6

            class MarkerType(_Enum):
                Undefined = 0
                None_ = 1
                Bullet = 2
                Arabic = 3
                LowercaseEnglishLetter = 4
                UppercaseEnglishLetter = 5
                LowercaseRoman = 6
                UppercaseRoman = 7
                UnicodeSequence = 8
                CircledNumber = 9
                BlackCircleWingding = 10
                WhiteCircleWingding = 11
                ArabicWide = 12
                SimplifiedChinese = 13
                TraditionalChinese = 14
                JapanSimplifiedChinese = 15
                JapanKorea = 16
                ArabicDictionary = 17
                ArabicAbjad = 18
                Hebrew = 19
                ThaiAlphabetic = 20
                ThaiNumeric = 21
                DevanagariVowel = 22
                DevanagariConsonant = 23
                DevanagariNumeric = 24

            class ParagraphAlignment(_Enum):
                Undefined = 0
                Left = 1
                Center = 2
                Right = 3
                Justify = 4

            class ParagraphStyle(_Enum):
                Undefined = 0
                None_ = 1
                Normal = 2
                Heading1 = 3
                Heading2 = 4
                Heading3 = 5
                Heading4 = 6
                Heading5 = 7
                Heading6 = 8
                Heading7 = 9
                Heading8 = 10
                Heading9 = 11

            class PointOptions(_Enum):
                None_ = 0x0
                IncludeInset = 0x1
                Start = 0x20
                ClientCoordinates = 0x100
                AllowOffClient = 0x200
                Transform = 0x400
                NoHorizontalScroll = 0x10000
                NoVerticalScroll = 0x40000

            class RangeGravity(_Enum):
                UIBehavior = 0
                Backward = 1
                Forward = 2
                Inward = 3
                Outward = 4

            class RichEditMathMode(_Enum):
                NoMath = 0
                MathOnly = 1

            class SelectionOptions(_Enum):
                StartActive = 0x1
                AtEndOfLine = 0x2
                Overtype = 0x4
                Active = 0x8
                Replace = 0x10

            class SelectionType(_Enum):
                None_ = 0
                InsertionPoint = 1
                Normal = 2
                InlineShape = 7
                Shape = 8

            class TabAlignment(_Enum):
                Left = 0
                Center = 1
                Right = 2
                Decimal = 3
                Bar = 4

            class TabLeader(_Enum):
                Spaces = 0
                Dots = 1
                Dashes = 2
                Lines = 3
                ThickLines = 4
                Equals = 5

            class TextDecorations(_Enum):
                None_ = 0x0
                Underline = 0x1
                Strikethrough = 0x2

            class TextGetOptions(_Enum):
                None_ = 0x0
                AdjustCrlf = 0x1
                UseCrlf = 0x2
                UseObjectText = 0x4
                AllowFinalEop = 0x8
                NoHidden = 0x20
                IncludeNumbering = 0x40
                FormatRtf = 0x2000
                UseLf = 0x1000000

            class TextRangeUnit(_Enum):
                Character = 0
                Word = 1
                Sentence = 2
                Paragraph = 3
                Line = 4
                Story = 5
                Screen = 6
                Section = 7
                Window = 8
                CharacterFormat = 9
                ParagraphFormat = 10
                Object = 11
                HardParagraph = 12
                Cluster = 13
                Bold = 14
                Italic = 15
                Underline = 16
                Strikethrough = 17
                ProtectedText = 18
                Link = 19
                SmallCaps = 20
                AllCaps = 21
                Hidden = 22
                Outline = 23
                Shadow = 24
                Imprint = 25
                Disabled = 26
                Revised = 27
                Subscript = 28
                Superscript = 29
                FontBound = 30
                LinkProtected = 31
                ContentLink = 32

            class TextScript(_Enum):
                Undefined = 0
                Ansi = 1
                EastEurope = 2
                Cyrillic = 3
                Greek = 4
                Turkish = 5
                Hebrew = 6
                Arabic = 7
                Baltic = 8
                Vietnamese = 9
                Default = 10
                Symbol = 11
                Thai = 12
                ShiftJis = 13
                GB2312 = 14
                Hangul = 15
                Big5 = 16
                PC437 = 17
                Oem = 18
                Mac = 19
                Armenian = 20
                Syriac = 21
                Thaana = 22
                Devanagari = 23
                Bengali = 24
                Gurmukhi = 25
                Gujarati = 26
                Oriya = 27
                Tamil = 28
                Telugu = 29
                Kannada = 30
                Malayalam = 31
                Sinhala = 32
                Lao = 33
                Tibetan = 34
                Myanmar = 35
                Georgian = 36
                Jamo = 37
                Ethiopic = 38
                Cherokee = 39
                Aboriginal = 40
                Ogham = 41
                Runic = 42
                Khmer = 43
                Mongolian = 44
                Braille = 45
                Yi = 46
                Limbu = 47
                TaiLe = 48
                NewTaiLue = 49
                SylotiNagri = 50
                Kharoshthi = 51
                Kayahli = 52
                UnicodeSymbol = 53
                Emoji = 54
                Glagolitic = 55
                Lisu = 56
                Vai = 57
                NKo = 58
                Osmanya = 59
                PhagsPa = 60
                Gothic = 61
                Deseret = 62
                Tifinagh = 63

            class TextSetOptions(_Enum):
                None_ = 0x0
                UnicodeBidi = 0x1
                Unlink = 0x8
                Unhide = 0x10
                CheckTextLimit = 0x20
                FormatRtf = 0x2000
                ApplyRtfDocumentDefaults = 0x4000

            class UnderlineType(_Enum):
                Undefined = 0
                None_ = 1
                Single = 2
                Words = 3
                Double = 4
                Dotted = 5
                Dash = 6
                DashDot = 7
                DashDotDot = 8
                Wave = 9
                Thick = 10
                Thin = 11
                DoubleWave = 12
                HeavyWave = 13
                LongDash = 14
                ThickDash = 15
                ThickDashDot = 16
                ThickDashDotDot = 17
                ThickDotted = 18
                ThickLongDash = 19

            class VerticalCharacterAlignment(_Enum):
                Top = 0
                Baseline = 1
                Bottom = 2

            class Core:
                class CoreTextFormatUpdatingReason(_Enum):
                    None_ = 0
                    CompositionUnconverted = 1
                    CompositionConverted = 2
                    CompositionTargetUnconverted = 3
                    CompositionTargetConverted = 4

                class CoreTextFormatUpdatingResult(_Enum):
                    Succeeded = 0
                    Failed = 1

                class CoreTextInputPaneDisplayPolicy(_Enum):
                    Automatic = 0
                    Manual = 1

                class CoreTextInputScope(_Enum):
                    Default = 0
                    Url = 1
                    FilePath = 2
                    FileName = 3
                    EmailUserName = 4
                    EmailAddress = 5
                    UserName = 6
                    PersonalFullName = 7
                    PersonalNamePrefix = 8
                    PersonalGivenName = 9
                    PersonalMiddleName = 10
                    PersonalSurname = 11
                    PersonalNameSuffix = 12
                    Address = 13
                    AddressPostalCode = 14
                    AddressStreet = 15
                    AddressStateOrProvince = 16
                    AddressCity = 17
                    AddressCountryName = 18
                    AddressCountryShortName = 19
                    CurrencyAmountAndSymbol = 20
                    CurrencyAmount = 21
                    Date = 22
                    DateMonth = 23
                    DateDay = 24
                    DateYear = 25
                    DateMonthName = 26
                    DateDayName = 27
                    Number = 29
                    SingleCharacter = 30
                    Password = 31
                    TelephoneNumber = 32
                    TelephoneCountryCode = 33
                    TelephoneAreaCode = 34
                    TelephoneLocalNumber = 35
                    Time = 36
                    TimeHour = 37
                    TimeMinuteOrSecond = 38
                    NumberFullWidth = 39
                    AlphanumericHalfWidth = 40
                    AlphanumericFullWidth = 41
                    CurrencyChinese = 42
                    Bopomofo = 43
                    Hiragana = 44
                    KatakanaHalfWidth = 45
                    KatakanaFullWidth = 46
                    Hanja = 47
                    HangulHalfWidth = 48
                    HangulFullWidth = 49
                    Search = 50
                    Formula = 51
                    SearchIncremental = 52
                    ChineseHalfWidth = 53
                    ChineseFullWidth = 54
                    NativeScript = 55
                    Text = 57
                    Chat = 58
                    NameOrPhoneNumber = 59
                    EmailUserNameOrAddress = 60
                    Private = 61
                    Maps = 62
                    PasswordNumeric = 63
                    FormulaNumber = 67
                    ChatWithoutEmoji = 68
                    Digits = 28
                    PinNumeric = 64
                    PinAlphanumeric = 65

                class CoreTextSelectionUpdatingResult(_Enum):
                    Succeeded = 0
                    Failed = 1

                class CoreTextTextUpdatingResult(_Enum):
                    Succeeded = 0
                    Failed = 1

        class UIAutomation:
            class Core:
                class AutomationRemoteOperationStatus(_Enum):
                    Success = 0
                    MalformedBytecode = 1
                    InstructionLimitExceeded = 2
                    UnhandledException = 3
                    ExecutionFailure = 4

        class ViewManagement:
            class ApplicationViewBoundsMode(_Enum):
                UseVisible = 0
                UseCoreWindow = 1

            class ApplicationViewMode(_Enum):
                Default = 0
                CompactOverlay = 1

            class ApplicationViewOrientation(_Enum):
                Landscape = 0
                Portrait = 1

            class ApplicationViewState(_Enum):
                FullScreenLandscape = 0
                Filled = 1
                Snapped = 2
                FullScreenPortrait = 3

            class ApplicationViewSwitchingOptions(_Enum):
                Default = 0x0
                SkipAnimation = 0x1
                ConsolidateViews = 0x2

            class ApplicationViewWindowingMode(_Enum):
                Auto = 0
                PreferredLaunchViewSize = 1
                FullScreen = 2
                CompactOverlay = 3
                Maximized = 4

            class FullScreenSystemOverlayMode(_Enum):
                Standard = 0
                Minimal = 1

            class HandPreference(_Enum):
                LeftHanded = 0
                RightHanded = 1

            class ScreenCaptureDisabledBehavior(_Enum):
                DrawAsBlack = 0
                ExcludeFromCapture = 1

            class UIColorType(_Enum):
                Background = 0
                Foreground = 1
                AccentDark3 = 2
                AccentDark2 = 3
                AccentDark1 = 4
                Accent = 5
                AccentLight1 = 6
                AccentLight2 = 7
                AccentLight3 = 8
                Complement = 9

            class UIElementType(_Enum):
                ActiveCaption = 0
                Background = 1
                ButtonFace = 2
                ButtonText = 3
                CaptionText = 4
                GrayText = 5
                Highlight = 6
                HighlightText = 7
                Hotlight = 8
                InactiveCaption = 9
                InactiveCaptionText = 10
                Window = 11
                WindowText = 12
                AccentColor = 1000
                TextHigh = 1001
                TextMedium = 1002
                TextLow = 1003
                TextContrastWithHigh = 1004
                NonTextHigh = 1005
                NonTextMediumHigh = 1006
                NonTextMedium = 1007
                NonTextMediumLow = 1008
                NonTextLow = 1009
                PageBackground = 1010
                PopupBackground = 1011
                OverlayOutsidePopup = 1012

            class UserInteractionMode(_Enum):
                Mouse = 0
                Touch = 1

            class ViewSizePreference(_Enum):
                Default = 0
                UseLess = 1
                UseHalf = 2
                UseMore = 3
                UseMinimum = 4
                UseNone = 5
                Custom = 6

            class Core:
                class CoreInputViewKind(_Enum):
                    Default = 0
                    Keyboard = 1
                    Handwriting = 2
                    Emoji = 3
                    Symbols = 4
                    Clipboard = 5
                    Dictation = 6

                class CoreInputViewOcclusionKind(_Enum):
                    Docked = 0
                    Floating = 1
                    Overlay = 2

                class CoreInputViewXYFocusTransferDirection(_Enum):
                    Up = 0
                    Right = 1
                    Down = 2
                    Left = 3

        class WebUI:
            class PrintContent(_Enum):
                AllPages = 0
                CurrentPage = 1
                CustomPageRange = 2
                CurrentSelection = 3

        class WindowManagement:
            class AppWindowClosedReason(_Enum):
                Other = 0
                AppInitiated = 1
                UserInitiated = 2

            class AppWindowFrameStyle(_Enum):
                Default = 0
                NoFrame = 1

            class AppWindowPresentationKind(_Enum):
                Default = 0
                CompactOverlay = 1
                FullScreen = 2

            class AppWindowTitleBarVisibility(_Enum):
                Default = 0
                AlwaysHidden = 1

            class WindowingEnvironmentKind(_Enum):
                Unknown = 0
                Overlapped = 1
                Tiled = 2

        class Xaml:
            class ApplicationHighContrastAdjustment(_Enum):
                None_ = 0x0

            class ApplicationRequiresPointerMode(_Enum):
                Auto = 0
                WhenRequested = 1

            class ApplicationTheme(_Enum):
                Light = 0
                Dark = 1

            class AutomationTextAttributesEnum(_Enum):
                AnimationStyleAttribute = 40000
                BackgroundColorAttribute = 40001
                BulletStyleAttribute = 40002
                CapStyleAttribute = 40003
                CultureAttribute = 40004
                FontNameAttribute = 40005
                FontSizeAttribute = 40006
                FontWeightAttribute = 40007
                ForegroundColorAttribute = 40008
                HorizontalTextAlignmentAttribute = 40009
                IndentationFirstLineAttribute = 40010
                IndentationLeadingAttribute = 40011
                IndentationTrailingAttribute = 40012
                IsHiddenAttribute = 40013
                IsItalicAttribute = 40014
                IsReadOnlyAttribute = 40015
                IsSubscriptAttribute = 40016
                IsSuperscriptAttribute = 40017
                MarginBottomAttribute = 40018
                MarginLeadingAttribute = 40019
                MarginTopAttribute = 40020
                MarginTrailingAttribute = 40021
                OutlineStylesAttribute = 40022
                OverlineColorAttribute = 40023
                OverlineStyleAttribute = 40024
                StrikethroughColorAttribute = 40025
                StrikethroughStyleAttribute = 40026
                TabsAttribute = 40027
                TextFlowDirectionsAttribute = 40028
                UnderlineColorAttribute = 40029
                UnderlineStyleAttribute = 40030
                AnnotationTypesAttribute = 40031
                AnnotationObjectsAttribute = 40032
                StyleNameAttribute = 40033
                StyleIdAttribute = 40034
                LinkAttribute = 40035
                IsActiveAttribute = 40036
                SelectionActiveEndAttribute = 40037
                CaretPositionAttribute = 40038
                CaretBidiModeAttribute = 40039

            class DurationType(_Enum):
                Automatic = 0
                TimeSpan = 1
                Forever = 2

            class ElementHighContrastAdjustment(_Enum):
                None_ = 0x0
                Application = 0x80000000

            class ElementSoundKind(_Enum):
                Focus = 0
                Invoke = 1
                Show = 2
                Hide = 3
                MovePrevious = 4
                MoveNext = 5
                GoBack = 6

            class ElementSoundMode(_Enum):
                Default = 0
                FocusOnly = 1
                Off = 2

            class ElementSoundPlayerState(_Enum):
                Auto = 0
                Off = 1
                On = 2

            class ElementSpatialAudioMode(_Enum):
                Auto = 0
                Off = 1
                On = 2

            class ElementTheme(_Enum):
                Default = 0
                Light = 1
                Dark = 2

            class FlowDirection(_Enum):
                LeftToRight = 0
                RightToLeft = 1

            class FocusState(_Enum):
                Unfocused = 0
                Pointer = 1
                Keyboard = 2
                Programmatic = 3

            class FocusVisualKind(_Enum):
                DottedLine = 0
                HighVisibility = 1
                Reveal = 2

            class FontCapitals(_Enum):
                Normal = 0
                AllSmallCaps = 1
                SmallCaps = 2
                AllPetiteCaps = 3
                PetiteCaps = 4
                Unicase = 5
                Titling = 6

            class FontEastAsianLanguage(_Enum):
                Normal = 0
                HojoKanji = 1
                Jis04 = 2
                Jis78 = 3
                Jis83 = 4
                Jis90 = 5
                NlcKanji = 6
                Simplified = 7
                Traditional = 8
                TraditionalNames = 9

            class FontEastAsianWidths(_Enum):
                Normal = 0
                Full = 1
                Half = 2
                Proportional = 3
                Quarter = 4
                Third = 5

            class FontFraction(_Enum):
                Normal = 0
                Stacked = 1
                Slashed = 2

            class FontNumeralAlignment(_Enum):
                Normal = 0
                Proportional = 1
                Tabular = 2

            class FontNumeralStyle(_Enum):
                Normal = 0
                Lining = 1
                OldStyle = 2

            class FontVariants(_Enum):
                Normal = 0
                Superscript = 1
                Subscript = 2
                Ordinal = 3
                Inferior = 4
                Ruby = 5

            class GridUnitType(_Enum):
                Auto = 0
                Pixel = 1
                Star = 2

            class HorizontalAlignment(_Enum):
                Left = 0
                Center = 1
                Right = 2
                Stretch = 3

            class LineStackingStrategy(_Enum):
                MaxHeight = 0
                BlockLineHeight = 1
                BaselineToBaseline = 2

            class OpticalMarginAlignment(_Enum):
                None_ = 0
                TrimSideBearings = 1

            class TextAlignment(_Enum):
                Center = 0
                Left = 1
                Start = 1
                Right = 2
                End = 2
                Justify = 3
                DetectFromContent = 4

            class TextLineBounds(_Enum):
                Full = 0
                TrimToCapHeight = 1
                TrimToBaseline = 2
                Tight = 3

            class TextReadingOrder(_Enum):
                Default = 0
                UseFlowDirection = 0
                DetectFromContent = 1

            class TextTrimming(_Enum):
                None_ = 0
                CharacterEllipsis = 1
                WordEllipsis = 2
                Clip = 3

            class TextWrapping(_Enum):
                NoWrap = 1
                Wrap = 2
                WrapWholeWords = 3

            class Vector3TransitionComponents(_Enum):
                X = 0x1
                Y = 0x2
                Z = 0x4

            class VerticalAlignment(_Enum):
                Top = 0
                Center = 1
                Bottom = 2
                Stretch = 3

            class Visibility(_Enum):
                Visible = 0
                Collapsed = 1

            class Automation:
                class AnnotationType(_Enum):
                    Unknown = 60000
                    SpellingError = 60001
                    GrammarError = 60002
                    Comment = 60003
                    FormulaError = 60004
                    TrackChanges = 60005
                    Header = 60006
                    Footer = 60007
                    Highlighted = 60008
                    Endnote = 60009
                    Footnote = 60010
                    InsertionChange = 60011
                    DeletionChange = 60012
                    MoveChange = 60013
                    FormatChange = 60014
                    UnsyncedChange = 60015
                    EditingLockedChange = 60016
                    ExternalChange = 60017
                    ConflictingChange = 60018
                    Author = 60019
                    AdvancedProofingIssue = 60020
                    DataValidationError = 60021
                    CircularReferenceError = 60022

                class AutomationActiveEnd(_Enum):
                    None_ = 0
                    Start = 1
                    End = 2

                class AutomationAnimationStyle(_Enum):
                    None_ = 0
                    LasVegasLights = 1
                    BlinkingBackground = 2
                    SparkleText = 3
                    MarchingBlackAnts = 4
                    MarchingRedAnts = 5
                    Shimmer = 6
                    Other = 7

                class AutomationBulletStyle(_Enum):
                    None_ = 0
                    HollowRoundBullet = 1
                    FilledRoundBullet = 2
                    HollowSquareBullet = 3
                    FilledSquareBullet = 4
                    DashBullet = 5
                    Other = 6

                class AutomationCaretBidiMode(_Enum):
                    LTR = 0
                    RTL = 1

                class AutomationCaretPosition(_Enum):
                    Unknown = 0
                    EndOfLine = 1
                    BeginningOfLine = 2

                class AutomationFlowDirections(_Enum):
                    Default = 0
                    RightToLeft = 1
                    BottomToTop = 2
                    Vertical = 3

                class AutomationOutlineStyles(_Enum):
                    None_ = 0
                    Outline = 1
                    Shadow = 2
                    Engraved = 3
                    Embossed = 4

                class AutomationStyleId(_Enum):
                    Heading1 = 70001
                    Heading2 = 70002
                    Heading3 = 70003
                    Heading4 = 70004
                    Heading5 = 70005
                    Heading6 = 70006
                    Heading7 = 70007
                    Heading8 = 70008
                    Heading9 = 70009
                    Title = 70010
                    Subtitle = 70011
                    Normal = 70012
                    Emphasis = 70013
                    Quote = 70014
                    BulletedList = 70015

                class AutomationTextDecorationLineStyle(_Enum):
                    None_ = 0
                    Single = 1
                    WordsOnly = 2
                    Double = 3
                    Dot = 4
                    Dash = 5
                    DashDot = 6
                    DashDotDot = 7
                    Wavy = 8
                    ThickSingle = 9
                    DoubleWavy = 10
                    ThickWavy = 11
                    LongDash = 12
                    ThickDash = 13
                    ThickDashDot = 14
                    ThickDashDotDot = 15
                    ThickDot = 16
                    ThickLongDash = 17
                    Other = 18

                class AutomationTextEditChangeType(_Enum):
                    None_ = 0
                    AutoCorrect = 1
                    Composition = 2
                    CompositionFinalized = 3

                class DockPosition(_Enum):
                    Top = 0
                    Left = 1
                    Bottom = 2
                    Right = 3
                    Fill = 4
                    None_ = 5

                class ExpandCollapseState(_Enum):
                    Collapsed = 0
                    Expanded = 1
                    PartiallyExpanded = 2
                    LeafNode = 3

                class RowOrColumnMajor(_Enum):
                    RowMajor = 0
                    ColumnMajor = 1
                    Indeterminate = 2

                class ScrollAmount(_Enum):
                    LargeDecrement = 0
                    SmallDecrement = 1
                    NoAmount = 2
                    LargeIncrement = 3
                    SmallIncrement = 4

                class SupportedTextSelection(_Enum):
                    None_ = 0
                    Single = 1
                    Multiple = 2

                class SynchronizedInputType(_Enum):
                    KeyUp = 1
                    KeyDown = 2
                    LeftMouseUp = 4
                    LeftMouseDown = 8
                    RightMouseUp = 16
                    RightMouseDown = 32

                class ToggleState(_Enum):
                    Off = 0
                    On = 1
                    Indeterminate = 2

                class WindowInteractionState(_Enum):
                    Running = 0
                    Closing = 1
                    ReadyForUserInteraction = 2
                    BlockedByModalWindow = 3
                    NotResponding = 4

                class WindowVisualState(_Enum):
                    Normal = 0
                    Maximized = 1
                    Minimized = 2

                class ZoomUnit(_Enum):
                    NoAmount = 0
                    LargeDecrement = 1
                    SmallDecrement = 2
                    LargeIncrement = 3
                    SmallIncrement = 4

                class Peers:
                    class AccessibilityView(_Enum):
                        Raw = 0
                        Control = 1
                        Content = 2

                    class AutomationControlType(_Enum):
                        Button = 0
                        Calendar = 1
                        CheckBox = 2
                        ComboBox = 3
                        Edit = 4
                        Hyperlink = 5
                        Image = 6
                        ListItem = 7
                        List = 8
                        Menu = 9
                        MenuBar = 10
                        MenuItem = 11
                        ProgressBar = 12
                        RadioButton = 13
                        ScrollBar = 14
                        Slider = 15
                        Spinner = 16
                        StatusBar = 17
                        Tab = 18
                        TabItem = 19
                        Text = 20
                        ToolBar = 21
                        ToolTip = 22
                        Tree = 23
                        TreeItem = 24
                        Custom = 25
                        Group = 26
                        Thumb = 27
                        DataGrid = 28
                        DataItem = 29
                        Document = 30
                        SplitButton = 31
                        Window = 32
                        Pane = 33
                        Header = 34
                        HeaderItem = 35
                        Table = 36
                        TitleBar = 37
                        Separator = 38
                        SemanticZoom = 39
                        AppBar = 40

                    class AutomationEvents(_Enum):
                        ToolTipOpened = 0
                        ToolTipClosed = 1
                        MenuOpened = 2
                        MenuClosed = 3
                        AutomationFocusChanged = 4
                        InvokePatternOnInvoked = 5
                        SelectionItemPatternOnElementAddedToSelection = 6
                        SelectionItemPatternOnElementRemovedFromSelection = 7
                        SelectionItemPatternOnElementSelected = 8
                        SelectionPatternOnInvalidated = 9
                        TextPatternOnTextSelectionChanged = 10
                        TextPatternOnTextChanged = 11
                        AsyncContentLoaded = 12
                        PropertyChanged = 13
                        StructureChanged = 14
                        DragStart = 15
                        DragCancel = 16
                        DragComplete = 17
                        DragEnter = 18
                        DragLeave = 19
                        Dropped = 20
                        LiveRegionChanged = 21
                        InputReachedTarget = 22
                        InputReachedOtherElement = 23
                        InputDiscarded = 24
                        WindowClosed = 25
                        WindowOpened = 26
                        ConversionTargetChanged = 27
                        TextEditTextChanged = 28
                        LayoutInvalidated = 29

                    class AutomationHeadingLevel(_Enum):
                        None_ = 0
                        Level1 = 1
                        Level2 = 2
                        Level3 = 3
                        Level4 = 4
                        Level5 = 5
                        Level6 = 6
                        Level7 = 7
                        Level8 = 8
                        Level9 = 9

                    class AutomationLandmarkType(_Enum):
                        None_ = 0
                        Custom = 1
                        Form = 2
                        Main = 3
                        Navigation = 4
                        Search = 5

                    class AutomationLiveSetting(_Enum):
                        Off = 0
                        Polite = 1
                        Assertive = 2

                    class AutomationNavigationDirection(_Enum):
                        Parent = 0
                        NextSibling = 1
                        PreviousSibling = 2
                        FirstChild = 3
                        LastChild = 4

                    class AutomationNotificationKind(_Enum):
                        ItemAdded = 0
                        ItemRemoved = 1
                        ActionCompleted = 2
                        ActionAborted = 3
                        Other = 4

                    class AutomationNotificationProcessing(_Enum):
                        ImportantAll = 0
                        ImportantMostRecent = 1
                        All = 2
                        MostRecent = 3
                        CurrentThenMostRecent = 4

                    class AutomationOrientation(_Enum):
                        None_ = 0
                        Horizontal = 1
                        Vertical = 2

                    class AutomationStructureChangeType(_Enum):
                        ChildAdded = 0
                        ChildRemoved = 1
                        ChildrenInvalidated = 2
                        ChildrenBulkAdded = 3
                        ChildrenBulkRemoved = 4
                        ChildrenReordered = 5

                    class PatternInterface(_Enum):
                        Invoke = 0
                        Selection = 1
                        Value = 2
                        RangeValue = 3
                        Scroll = 4
                        ScrollItem = 5
                        ExpandCollapse = 6
                        Grid = 7
                        GridItem = 8
                        MultipleView = 9
                        Window = 10
                        SelectionItem = 11
                        Dock = 12
                        Table = 13
                        TableItem = 14
                        Toggle = 15
                        Transform = 16
                        Text = 17
                        ItemContainer = 18
                        VirtualizedItem = 19
                        Text2 = 20
                        TextChild = 21
                        TextRange = 22
                        Annotation = 23
                        Drag = 24
                        DropTarget = 25
                        ObjectModel = 26
                        Spreadsheet = 27
                        SpreadsheetItem = 28
                        Styles = 29
                        Transform2 = 30
                        SynchronizedInput = 31
                        TextEdit = 32
                        CustomNavigation = 33

                class Text:
                    class TextPatternRangeEndpoint(_Enum):
                        Start = 0
                        End = 1

                    class TextUnit(_Enum):
                        Character = 0
                        Format = 1
                        Word = 2
                        Line = 3
                        Paragraph = 4
                        Page = 5
                        Document = 6

            class Controls:
                class AppBarClosedDisplayMode(_Enum):
                    Compact = 0
                    Minimal = 1
                    Hidden = 2

                class AutoSuggestionBoxTextChangeReason(_Enum):
                    UserInput = 0
                    ProgrammaticChange = 1
                    SuggestionChosen = 2

                class BackgroundSizing(_Enum):
                    InnerBorderEdge = 0
                    OuterBorderEdge = 1

                class CalendarViewDisplayMode(_Enum):
                    Month = 0
                    Year = 1
                    Decade = 2

                class CalendarViewSelectionMode(_Enum):
                    None_ = 0
                    Single = 1
                    Multiple = 2

                class CandidateWindowAlignment(_Enum):
                    Default = 0
                    BottomEdge = 1

                class CharacterCasing(_Enum):
                    Normal = 0
                    Lower = 1
                    Upper = 2

                class ClickMode(_Enum):
                    Release = 0
                    Press = 1
                    Hover = 2

                class ColorPickerHsvChannel(_Enum):
                    Hue = 0
                    Saturation = 1
                    Value = 2
                    Alpha = 3

                class ColorSpectrumComponents(_Enum):
                    HueValue = 0
                    ValueHue = 1
                    HueSaturation = 2
                    SaturationHue = 3
                    SaturationValue = 4
                    ValueSaturation = 5

                class ColorSpectrumShape(_Enum):
                    Box = 0
                    Ring = 1

                class ComboBoxSelectionChangedTrigger(_Enum):
                    Committed = 0
                    Always = 1

                class CommandBarDefaultLabelPosition(_Enum):
                    Bottom = 0
                    Right = 1
                    Collapsed = 2

                class CommandBarDynamicOverflowAction(_Enum):
                    AddingToOverflow = 0
                    RemovingFromOverflow = 1

                class CommandBarLabelPosition(_Enum):
                    Default = 0
                    Collapsed = 1

                class CommandBarOverflowButtonVisibility(_Enum):
                    Auto = 0
                    Visible = 1
                    Collapsed = 2

                class ContentDialogButton(_Enum):
                    None_ = 0
                    Primary = 1
                    Secondary = 2
                    Close = 3

                class ContentDialogPlacement(_Enum):
                    Popup = 0
                    InPlace = 1

                class ContentDialogResult(_Enum):
                    None_ = 0
                    Primary = 1
                    Secondary = 2

                class ContentLinkChangeKind(_Enum):
                    Inserted = 0
                    Removed = 1
                    Edited = 2

                class DisabledFormattingAccelerators(_Enum):
                    None_ = 0x0
                    Bold = 0x1
                    Italic = 0x2
                    Underline = 0x4

                class HandwritingPanelPlacementAlignment(_Enum):
                    Auto = 0
                    TopLeft = 1
                    TopRight = 2
                    BottomLeft = 3
                    BottomRight = 4

                class IncrementalLoadingTrigger(_Enum):
                    None_ = 0
                    Edge = 1

                class InkToolbarButtonFlyoutPlacement(_Enum):
                    Auto = 0
                    Top = 1
                    Bottom = 2
                    Left = 3
                    Right = 4

                class InkToolbarFlyoutItemKind(_Enum):
                    Simple = 0
                    Radio = 1
                    Check = 2
                    RadioCheck = 3

                class InkToolbarInitialControls(_Enum):
                    All = 0
                    None_ = 1
                    PensOnly = 2
                    AllExceptPens = 3

                class InkToolbarMenuKind(_Enum):
                    Stencil = 0

                class InkToolbarStencilKind(_Enum):
                    Ruler = 0
                    Protractor = 1

                class InkToolbarToggle(_Enum):
                    Ruler = 0
                    Custom = 1

                class InkToolbarTool(_Enum):
                    BallpointPen = 0
                    Pencil = 1
                    Highlighter = 2
                    Eraser = 3
                    CustomPen = 4
                    CustomTool = 5

                class ItemsUpdatingScrollMode(_Enum):
                    KeepItemsInView = 0
                    KeepScrollOffset = 1
                    KeepLastItemInView = 2

                class LightDismissOverlayMode(_Enum):
                    Auto = 0
                    On = 1
                    Off = 2

                class ListPickerFlyoutSelectionMode(_Enum):
                    Single = 0
                    Multiple = 1

                class ListViewReorderMode(_Enum):
                    Disabled = 0
                    Enabled = 1

                class ListViewSelectionMode(_Enum):
                    None_ = 0
                    Single = 1
                    Multiple = 2
                    Extended = 3

                class NavigationViewBackButtonVisible(_Enum):
                    Collapsed = 0
                    Visible = 1
                    Auto = 2

                class NavigationViewDisplayMode(_Enum):
                    Minimal = 0
                    Compact = 1
                    Expanded = 2

                class NavigationViewOverflowLabelMode(_Enum):
                    MoreLabel = 0
                    NoLabel = 1

                class NavigationViewPaneDisplayMode(_Enum):
                    Auto = 0
                    Left = 1
                    Top = 2
                    LeftCompact = 3
                    LeftMinimal = 4

                class NavigationViewSelectionFollowsFocus(_Enum):
                    Disabled = 0
                    Enabled = 1

                class NavigationViewShoulderNavigationEnabled(_Enum):
                    WhenSelectionFollowsFocus = 0
                    Always = 1
                    Never = 2

                class Orientation(_Enum):
                    Vertical = 0
                    Horizontal = 1

                class PanelScrollingDirection(_Enum):
                    None_ = 0
                    Forward = 1
                    Backward = 2

                class ParallaxSourceOffsetKind(_Enum):
                    Absolute = 0
                    Relative = 1

                class PasswordRevealMode(_Enum):
                    Peek = 0
                    Hidden = 1
                    Visible = 2

                class PivotHeaderFocusVisualPlacement(_Enum):
                    ItemHeaders = 0
                    SelectedItemHeader = 1

                class PivotSlideInAnimationGroup(_Enum):
                    Default = 0
                    GroupOne = 1
                    GroupTwo = 2
                    GroupThree = 3

                class RefreshPullDirection(_Enum):
                    LeftToRight = 0
                    TopToBottom = 1
                    RightToLeft = 2
                    BottomToTop = 3

                class RefreshVisualizerOrientation(_Enum):
                    Auto = 0
                    Normal = 1
                    Rotate90DegreesCounterclockwise = 2
                    Rotate270DegreesCounterclockwise = 3

                class RefreshVisualizerState(_Enum):
                    Idle = 0
                    Peeking = 1
                    Interacting = 2
                    Pending = 3
                    Refreshing = 4

                class RequiresPointer(_Enum):
                    Never = 0
                    WhenEngaged = 1
                    WhenFocused = 2

                class RichEditClipboardFormat(_Enum):
                    AllFormats = 0
                    PlainText = 1

                class ScrollBarVisibility(_Enum):
                    Disabled = 0
                    Auto = 1
                    Hidden = 2
                    Visible = 3

                class ScrollIntoViewAlignment(_Enum):
                    Default = 0
                    Leading = 1

                class ScrollMode(_Enum):
                    Disabled = 0
                    Enabled = 1
                    Auto = 2

                class SelectionMode(_Enum):
                    Single = 0
                    Multiple = 1
                    Extended = 2

                class SnapPointsType(_Enum):
                    None_ = 0
                    Optional = 1
                    Mandatory = 2
                    OptionalSingle = 3
                    MandatorySingle = 4

                class SplitViewDisplayMode(_Enum):
                    Overlay = 0
                    Inline = 1
                    CompactOverlay = 2
                    CompactInline = 3

                class SplitViewPanePlacement(_Enum):
                    Left = 0
                    Right = 1

                class StretchDirection(_Enum):
                    UpOnly = 0
                    DownOnly = 1
                    Both = 2

                class SwipeBehaviorOnInvoked(_Enum):
                    Auto = 0
                    Close = 1
                    RemainOpen = 2

                class SwipeMode(_Enum):
                    Reveal = 0
                    Execute = 1

                class Symbol(_Enum):
                    Previous = 57600
                    Next = 57601
                    Play = 57602
                    Pause = 57603
                    Edit = 57604
                    Save = 57605
                    Clear = 57606
                    Delete = 57607
                    Remove = 57608
                    Add = 57609
                    Cancel = 57610
                    Accept = 57611
                    More = 57612
                    Redo = 57613
                    Undo = 57614
                    Home = 57615
                    Up = 57616
                    Forward = 57617
                    Back = 57618
                    Favorite = 57619
                    Camera = 57620
                    Setting = 57621
                    Video = 57622
                    Sync = 57623
                    Download = 57624
                    Mail = 57625
                    Find = 57626
                    Help = 57627
                    Upload = 57628
                    Emoji = 57629
                    TwoPage = 57630
                    LeaveChat = 57631
                    MailForward = 57632
                    Clock = 57633
                    Send = 57634
                    Crop = 57635
                    RotateCamera = 57636
                    People = 57637
                    OpenPane = 57638
                    ClosePane = 57639
                    World = 57640
                    Flag = 57641
                    PreviewLink = 57642
                    Globe = 57643
                    Trim = 57644
                    AttachCamera = 57645
                    ZoomIn = 57646
                    Bookmarks = 57647
                    Document = 57648
                    ProtectedDocument = 57649
                    Page = 57650
                    Bullets = 57651
                    Comment = 57652
                    MailFilled = 57653
                    ContactInfo = 57654
                    HangUp = 57655
                    ViewAll = 57656
                    MapPin = 57657
                    Phone = 57658
                    VideoChat = 57659
                    Switch = 57660
                    Contact = 57661
                    Rename = 57662
                    Pin = 57665
                    MusicInfo = 57666
                    Go = 57667
                    Keyboard = 57668
                    DockLeft = 57669
                    DockRight = 57670
                    DockBottom = 57671
                    Remote = 57672
                    Refresh = 57673
                    Rotate = 57674
                    Shuffle = 57675
                    List = 57676
                    Shop = 57677
                    SelectAll = 57678
                    Orientation = 57679
                    Import = 57680
                    ImportAll = 57681
                    BrowsePhotos = 57685
                    WebCam = 57686
                    Pictures = 57688
                    SaveLocal = 57689
                    Caption = 57690
                    Stop = 57691
                    ShowResults = 57692
                    Volume = 57693
                    Repair = 57694
                    Message = 57695
                    Page2 = 57696
                    CalendarDay = 57697
                    CalendarWeek = 57698
                    Calendar = 57699
                    Character = 57700
                    MailReplyAll = 57701
                    Read = 57702
                    Link = 57703
                    Account = 57704
                    ShowBcc = 57705
                    HideBcc = 57706
                    Cut = 57707
                    Attach = 57708
                    Paste = 57709
                    Filter = 57710
                    Copy = 57711
                    Emoji2 = 57712
                    Important = 57713
                    MailReply = 57714
                    SlideShow = 57715
                    Sort = 57716
                    Manage = 57720
                    AllApps = 57721
                    DisconnectDrive = 57722
                    MapDrive = 57723
                    NewWindow = 57724
                    OpenWith = 57725
                    ContactPresence = 57729
                    Priority = 57730
                    GoToToday = 57732
                    Font = 57733
                    FontColor = 57734
                    Contact2 = 57735
                    Folder = 57736
                    Audio = 57737
                    Placeholder = 57738
                    View = 57739
                    SetLockScreen = 57740
                    SetTile = 57741
                    ClosedCaption = 57744
                    StopSlideShow = 57745
                    Permissions = 57746
                    Highlight = 57747
                    DisableUpdates = 57748
                    UnFavorite = 57749
                    UnPin = 57750
                    OpenLocal = 57751
                    Mute = 57752
                    Italic = 57753
                    Underline = 57754
                    Bold = 57755
                    MoveToFolder = 57756
                    LikeDislike = 57757
                    Dislike = 57758
                    Like = 57759
                    AlignRight = 57760
                    AlignCenter = 57761
                    AlignLeft = 57762
                    Zoom = 57763
                    ZoomOut = 57764
                    OpenFile = 57765
                    OtherUser = 57766
                    Admin = 57767
                    Street = 57795
                    Map = 57796
                    ClearSelection = 57797
                    FontDecrease = 57798
                    FontIncrease = 57799
                    FontSize = 57800
                    CellPhone = 57801
                    ReShare = 57802
                    Tag = 57803
                    RepeatOne = 57804
                    RepeatAll = 57805
                    OutlineStar = 57806
                    SolidStar = 57807
                    Calculator = 57808
                    Directions = 57809
                    Target = 57810
                    Library = 57811
                    PhoneBook = 57812
                    Memo = 57813
                    Microphone = 57814
                    PostUpdate = 57815
                    BackToWindow = 57816
                    FullScreen = 57817
                    NewFolder = 57818
                    CalendarReply = 57819
                    UnSyncFolder = 57821
                    ReportHacked = 57822
                    SyncFolder = 57823
                    BlockContact = 57824
                    SwitchApps = 57825
                    AddFriend = 57826
                    TouchPointer = 57827
                    GoToStart = 57828
                    ZeroBars = 57829
                    OneBar = 57830
                    TwoBars = 57831
                    ThreeBars = 57832
                    FourBars = 57833
                    Scan = 58004
                    Preview = 58005
                    GlobalNavigationButton = 59136
                    Share = 59181
                    Print = 59209
                    XboxOneConsole = 59792

                class TreeViewSelectionMode(_Enum):
                    None_ = 0
                    Single = 1
                    Multiple = 2

                class TwoPaneViewMode(_Enum):
                    SinglePane = 0
                    Wide = 1
                    Tall = 2

                class TwoPaneViewPriority(_Enum):
                    Pane1 = 0
                    Pane2 = 1

                class TwoPaneViewTallModeConfiguration(_Enum):
                    SinglePane = 0
                    TopBottom = 1
                    BottomTop = 2

                class TwoPaneViewWideModeConfiguration(_Enum):
                    SinglePane = 0
                    LeftRight = 1
                    RightLeft = 2

                class VirtualizationMode(_Enum):
                    Standard = 0
                    Recycling = 1

                class WebViewExecutionMode(_Enum):
                    SameThread = 0
                    SeparateThread = 1
                    SeparateProcess = 2

                class WebViewPermissionState(_Enum):
                    Unknown = 0
                    Defer = 1
                    Allow = 2
                    Deny = 3

                class WebViewPermissionType(_Enum):
                    Geolocation = 0
                    UnlimitedIndexedDBQuota = 1
                    Media = 2
                    PointerLock = 3
                    WebNotifications = 4
                    Screen = 5
                    ImmersiveView = 6

                class ZoomMode(_Enum):
                    Disabled = 0
                    Enabled = 1

                class Maps:
                    class MapAnimationKind(_Enum):
                        Default = 0
                        None_ = 1
                        Linear = 2
                        Bow = 3

                    class MapCameraChangeReason(_Enum):
                        System = 0
                        UserInteraction = 1
                        Programmatic = 2

                    class MapColorScheme(_Enum):
                        Light = 0
                        Dark = 1

                    class MapElementCollisionBehavior(_Enum):
                        Hide = 0
                        RemainVisible = 1

                    class MapInteractionMode(_Enum):
                        Auto = 0
                        Disabled = 1
                        GestureOnly = 2
                        PointerAndKeyboard = 2
                        ControlOnly = 3
                        GestureAndControl = 4
                        PointerKeyboardAndControl = 4
                        PointerOnly = 5

                    class MapLoadingStatus(_Enum):
                        Loading = 0
                        Loaded = 1
                        DataUnavailable = 2
                        DownloadedMapsManagerUnavailable = 3

                    class MapModel3DShadingOption(_Enum):
                        Default = 0
                        Flat = 1
                        Smooth = 2

                    class MapPanInteractionMode(_Enum):
                        Auto = 0
                        Disabled = 1

                    class MapProjection(_Enum):
                        WebMercator = 0
                        Globe = 1

                    class MapStyle(_Enum):
                        None_ = 0
                        Road = 1
                        Aerial = 2
                        AerialWithRoads = 3
                        Terrain = 4
                        Aerial3D = 5
                        Aerial3DWithRoads = 6
                        Custom = 7

                    class MapTileAnimationState(_Enum):
                        Stopped = 0
                        Paused = 1
                        Playing = 2

                    class MapTileLayer(_Enum):
                        LabelOverlay = 0
                        RoadOverlay = 1
                        AreaOverlay = 2
                        BackgroundOverlay = 3
                        BackgroundReplacement = 4

                    class MapVisibleRegionKind(_Enum):
                        Near = 0
                        Full = 1

                    class MapWatermarkMode(_Enum):
                        Automatic = 0
                        On = 1

                class Primitives:
                    class AnimationDirection(_Enum):
                        Left = 0
                        Top = 1
                        Right = 2
                        Bottom = 3

                    class ComponentResourceLocation(_Enum):
                        Application = 0
                        Nested = 1

                    class EdgeTransitionLocation(_Enum):
                        Left = 0
                        Top = 1
                        Right = 2
                        Bottom = 3

                    class FlyoutPlacementMode(_Enum):
                        Top = 0
                        Bottom = 1
                        Left = 2
                        Right = 3
                        Full = 4
                        TopEdgeAlignedLeft = 5
                        TopEdgeAlignedRight = 6
                        BottomEdgeAlignedLeft = 7
                        BottomEdgeAlignedRight = 8
                        LeftEdgeAlignedTop = 9
                        LeftEdgeAlignedBottom = 10
                        RightEdgeAlignedTop = 11
                        RightEdgeAlignedBottom = 12
                        Auto = 13

                    class FlyoutShowMode(_Enum):
                        Auto = 0
                        Standard = 1
                        Transient = 2
                        TransientWithDismissOnPointerMoveAway = 3

                    class GeneratorDirection(_Enum):
                        Forward = 0
                        Backward = 1

                    class GroupHeaderPlacement(_Enum):
                        Top = 0
                        Left = 1

                    class ListViewItemPresenterCheckMode(_Enum):
                        Inline = 0
                        Overlay = 1

                    class ListViewItemPresenterSelectionIndicatorMode(_Enum):
                        Inline = 0
                        Overlay = 1

                    class PlacementMode(_Enum):
                        Bottom = 2
                        Left = 9
                        Mouse = 7
                        Right = 4
                        Top = 10

                    class PopupPlacementMode(_Enum):
                        Auto = 0
                        Top = 1
                        Bottom = 2
                        Left = 3
                        Right = 4
                        TopEdgeAlignedLeft = 5
                        TopEdgeAlignedRight = 6
                        BottomEdgeAlignedLeft = 7
                        BottomEdgeAlignedRight = 8
                        LeftEdgeAlignedTop = 9
                        LeftEdgeAlignedBottom = 10
                        RightEdgeAlignedTop = 11
                        RightEdgeAlignedBottom = 12

                    class ScrollEventType(_Enum):
                        SmallDecrement = 0
                        SmallIncrement = 1
                        LargeDecrement = 2
                        LargeIncrement = 3
                        ThumbPosition = 4
                        ThumbTrack = 5
                        First = 6
                        Last = 7
                        EndScroll = 8

                    class ScrollingIndicatorMode(_Enum):
                        None_ = 0
                        TouchIndicator = 1
                        MouseIndicator = 2

                    class SliderSnapsTo(_Enum):
                        StepValues = 0
                        Ticks = 1

                    class SnapPointsAlignment(_Enum):
                        Near = 0
                        Center = 1
                        Far = 2

                    class TickPlacement(_Enum):
                        None_ = 0
                        TopLeft = 1
                        BottomRight = 2
                        Outside = 3
                        Inline = 4

            class Core:
                class Direct:
                    class XamlEventIndex(_Enum):
                        FrameworkElement_DataContextChanged = 16
                        FrameworkElement_SizeChanged = 17
                        FrameworkElement_LayoutUpdated = 18
                        UIElement_KeyUp = 22
                        UIElement_KeyDown = 23
                        UIElement_GotFocus = 24
                        UIElement_LostFocus = 25
                        UIElement_DragStarting = 26
                        UIElement_DropCompleted = 27
                        UIElement_CharacterReceived = 28
                        UIElement_DragEnter = 29
                        UIElement_DragLeave = 30
                        UIElement_DragOver = 31
                        UIElement_Drop = 32
                        UIElement_PointerPressed = 38
                        UIElement_PointerMoved = 39
                        UIElement_PointerReleased = 40
                        UIElement_PointerEntered = 41
                        UIElement_PointerExited = 42
                        UIElement_PointerCaptureLost = 43
                        UIElement_PointerCanceled = 44
                        UIElement_PointerWheelChanged = 45
                        UIElement_Tapped = 46
                        UIElement_DoubleTapped = 47
                        UIElement_Holding = 48
                        UIElement_ContextRequested = 49
                        UIElement_ContextCanceled = 50
                        UIElement_RightTapped = 51
                        UIElement_ManipulationStarting = 52
                        UIElement_ManipulationInertiaStarting = 53
                        UIElement_ManipulationStarted = 54
                        UIElement_ManipulationDelta = 55
                        UIElement_ManipulationCompleted = 56
                        UIElement_ProcessKeyboardAccelerators = 60
                        UIElement_GettingFocus = 61
                        UIElement_LosingFocus = 62
                        UIElement_NoFocusCandidateFound = 63
                        UIElement_PreviewKeyDown = 64
                        UIElement_PreviewKeyUp = 65
                        UIElement_BringIntoViewRequested = 66
                        AppBar_Opening = 109
                        AppBar_Opened = 110
                        AppBar_Closing = 111
                        AppBar_Closed = 112
                        AutoSuggestBox_SuggestionChosen = 113
                        AutoSuggestBox_TextChanged = 114
                        AutoSuggestBox_QuerySubmitted = 115
                        CalendarDatePicker_CalendarViewDayItemChanging = 116
                        CalendarDatePicker_DateChanged = 117
                        CalendarDatePicker_Opened = 118
                        CalendarDatePicker_Closed = 119
                        CalendarView_CalendarViewDayItemChanging = 120
                        CalendarView_SelectedDatesChanged = 121
                        ComboBox_DropDownClosed = 122
                        ComboBox_DropDownOpened = 123
                        CommandBar_DynamicOverflowItemsChanging = 124
                        ContentDialog_Closing = 126
                        ContentDialog_Closed = 127
                        ContentDialog_Opened = 128
                        ContentDialog_PrimaryButtonClick = 129
                        ContentDialog_SecondaryButtonClick = 130
                        ContentDialog_CloseButtonClick = 131
                        Control_FocusEngaged = 132
                        Control_FocusDisengaged = 133
                        DatePicker_DateChanged = 135
                        Frame_Navigated = 136
                        Frame_Navigating = 137
                        Frame_NavigationFailed = 138
                        Frame_NavigationStopped = 139
                        Hub_SectionHeaderClick = 143
                        Hub_SectionsInViewChanged = 144
                        ItemsPresenter_HorizontalSnapPointsChanged = 148
                        ItemsPresenter_VerticalSnapPointsChanged = 149
                        ListViewBase_ItemClick = 150
                        ListViewBase_DragItemsStarting = 151
                        ListViewBase_DragItemsCompleted = 152
                        ListViewBase_ContainerContentChanging = 153
                        ListViewBase_ChoosingItemContainer = 154
                        ListViewBase_ChoosingGroupHeaderContainer = 155
                        MediaTransportControls_ThumbnailRequested = 167
                        MenuFlyoutItem_Click = 168
                        RichEditBox_TextChanging = 177
                        ScrollViewer_ViewChanging = 192
                        ScrollViewer_ViewChanged = 193
                        ScrollViewer_DirectManipulationStarted = 194
                        ScrollViewer_DirectManipulationCompleted = 195
                        SearchBox_QueryChanged = 196
                        SearchBox_SuggestionsRequested = 197
                        SearchBox_QuerySubmitted = 198
                        SearchBox_ResultSuggestionChosen = 199
                        SearchBox_PrepareForFocusOnKeyboardInput = 200
                        SemanticZoom_ViewChangeStarted = 201
                        SemanticZoom_ViewChangeCompleted = 202
                        SettingsFlyout_BackClick = 203
                        StackPanel_HorizontalSnapPointsChanged = 208
                        StackPanel_VerticalSnapPointsChanged = 209
                        TimePicker_TimeChanged = 227
                        ToggleSwitch_Toggled = 228
                        ToolTip_Closed = 229
                        ToolTip_Opened = 230
                        VirtualizingStackPanel_CleanUpVirtualizedItemEvent = 231
                        WebView_SeparateProcessLost = 232
                        WebView_LoadCompleted = 233
                        WebView_ScriptNotify = 234
                        WebView_NavigationFailed = 235
                        WebView_NavigationStarting = 236
                        WebView_ContentLoading = 237
                        WebView_DOMContentLoaded = 238
                        WebView_NavigationCompleted = 239
                        WebView_FrameNavigationStarting = 240
                        WebView_FrameContentLoading = 241
                        WebView_FrameDOMContentLoaded = 242
                        WebView_FrameNavigationCompleted = 243
                        WebView_LongRunningScriptDetected = 244
                        WebView_UnsafeContentWarningDisplaying = 245
                        WebView_UnviewableContentIdentified = 246
                        WebView_ContainsFullScreenElementChanged = 247
                        WebView_UnsupportedUriSchemeIdentified = 248
                        WebView_NewWindowRequested = 249
                        WebView_PermissionRequested = 250
                        ButtonBase_Click = 256
                        CarouselPanel_HorizontalSnapPointsChanged = 257
                        CarouselPanel_VerticalSnapPointsChanged = 258
                        OrientedVirtualizingPanel_HorizontalSnapPointsChanged = 263
                        OrientedVirtualizingPanel_VerticalSnapPointsChanged = 264
                        RangeBase_ValueChanged = 267
                        ScrollBar_Scroll = 268
                        Selector_SelectionChanged = 269
                        Thumb_DragStarted = 270
                        Thumb_DragDelta = 271
                        Thumb_DragCompleted = 272
                        ToggleButton_Checked = 273
                        ToggleButton_Unchecked = 274
                        ToggleButton_Indeterminate = 275
                        WebView_WebResourceRequested = 283
                        ScrollViewer_AnchorRequested = 291
                        DatePicker_SelectedDateChanged = 322
                        TimePicker_SelectedTimeChanged = 323

                    class XamlPropertyIndex(_Enum):
                        AutomationProperties_AcceleratorKey = 5
                        AutomationProperties_AccessibilityView = 6
                        AutomationProperties_AccessKey = 7
                        AutomationProperties_AutomationId = 8
                        AutomationProperties_ControlledPeers = 9
                        AutomationProperties_HelpText = 10
                        AutomationProperties_IsRequiredForForm = 11
                        AutomationProperties_ItemStatus = 12
                        AutomationProperties_ItemType = 13
                        AutomationProperties_LabeledBy = 14
                        AutomationProperties_LiveSetting = 15
                        AutomationProperties_Name = 16
                        ToolTipService_Placement = 24
                        ToolTipService_PlacementTarget = 25
                        ToolTipService_ToolTip = 26
                        Typography_AnnotationAlternates = 28
                        Typography_Capitals = 29
                        Typography_CapitalSpacing = 30
                        Typography_CaseSensitiveForms = 31
                        Typography_ContextualAlternates = 32
                        Typography_ContextualLigatures = 33
                        Typography_ContextualSwashes = 34
                        Typography_DiscretionaryLigatures = 35
                        Typography_EastAsianExpertForms = 36
                        Typography_EastAsianLanguage = 37
                        Typography_EastAsianWidths = 38
                        Typography_Fraction = 39
                        Typography_HistoricalForms = 40
                        Typography_HistoricalLigatures = 41
                        Typography_Kerning = 42
                        Typography_MathematicalGreek = 43
                        Typography_NumeralAlignment = 44
                        Typography_NumeralStyle = 45
                        Typography_SlashedZero = 46
                        Typography_StandardLigatures = 47
                        Typography_StandardSwashes = 48
                        Typography_StylisticAlternates = 49
                        Typography_StylisticSet1 = 50
                        Typography_StylisticSet10 = 51
                        Typography_StylisticSet11 = 52
                        Typography_StylisticSet12 = 53
                        Typography_StylisticSet13 = 54
                        Typography_StylisticSet14 = 55
                        Typography_StylisticSet15 = 56
                        Typography_StylisticSet16 = 57
                        Typography_StylisticSet17 = 58
                        Typography_StylisticSet18 = 59
                        Typography_StylisticSet19 = 60
                        Typography_StylisticSet2 = 61
                        Typography_StylisticSet20 = 62
                        Typography_StylisticSet3 = 63
                        Typography_StylisticSet4 = 64
                        Typography_StylisticSet5 = 65
                        Typography_StylisticSet6 = 66
                        Typography_StylisticSet7 = 67
                        Typography_StylisticSet8 = 68
                        Typography_StylisticSet9 = 69
                        Typography_Variants = 70
                        AutomationPeer_EventsSource = 75
                        AutoSuggestBoxSuggestionChosenEventArgs_SelectedItem = 76
                        AutoSuggestBoxTextChangedEventArgs_Reason = 77
                        Brush_Opacity = 78
                        Brush_RelativeTransform = 79
                        Brush_Transform = 80
                        CollectionViewSource_IsSourceGrouped = 81
                        CollectionViewSource_ItemsPath = 82
                        CollectionViewSource_Source = 83
                        CollectionViewSource_View = 84
                        ColorKeyFrame_KeyTime = 90
                        ColorKeyFrame_Value = 91
                        ColumnDefinition_ActualWidth = 92
                        ColumnDefinition_MaxWidth = 93
                        ColumnDefinition_MinWidth = 94
                        ColumnDefinition_Width = 95
                        ComboBoxTemplateSettings_DropDownClosedHeight = 96
                        ComboBoxTemplateSettings_DropDownOffset = 97
                        ComboBoxTemplateSettings_DropDownOpenedHeight = 98
                        ComboBoxTemplateSettings_SelectedItemDirection = 99
                        DoubleKeyFrame_KeyTime = 107
                        DoubleKeyFrame_Value = 108
                        EasingFunctionBase_EasingMode = 111
                        FlyoutBase_AttachedFlyout = 114
                        FlyoutBase_Placement = 115
                        Geometry_Bounds = 118
                        Geometry_Transform = 119
                        GradientStop_Color = 120
                        GradientStop_Offset = 121
                        GroupStyle_ContainerStyle = 124
                        GroupStyle_ContainerStyleSelector = 125
                        GroupStyle_HeaderContainerStyle = 126
                        GroupStyle_HeaderTemplate = 127
                        GroupStyle_HeaderTemplateSelector = 128
                        GroupStyle_HidesIfEmpty = 129
                        GroupStyle_Panel = 130
                        InertiaExpansionBehavior_DesiredDeceleration = 144
                        InertiaExpansionBehavior_DesiredExpansion = 145
                        InertiaRotationBehavior_DesiredDeceleration = 146
                        InertiaRotationBehavior_DesiredRotation = 147
                        InertiaTranslationBehavior_DesiredDeceleration = 148
                        InertiaTranslationBehavior_DesiredDisplacement = 149
                        InputScope_Names = 150
                        InputScopeName_NameValue = 151
                        KeySpline_ControlPoint1 = 153
                        KeySpline_ControlPoint2 = 154
                        ManipulationPivot_Center = 159
                        ManipulationPivot_Radius = 160
                        ObjectKeyFrame_KeyTime = 183
                        ObjectKeyFrame_Value = 184
                        PageStackEntry_SourcePageType = 185
                        PathFigure_IsClosed = 192
                        PathFigure_IsFilled = 193
                        PathFigure_Segments = 194
                        PathFigure_StartPoint = 195
                        Pointer_IsInContact = 199
                        Pointer_IsInRange = 200
                        Pointer_PointerDeviceType = 201
                        Pointer_PointerId = 202
                        PointKeyFrame_KeyTime = 205
                        PointKeyFrame_Value = 206
                        PrintDocument_DocumentSource = 209
                        ProgressBarTemplateSettings_ContainerAnimationEndPosition = 211
                        ProgressBarTemplateSettings_ContainerAnimationStartPosition = 212
                        ProgressBarTemplateSettings_EllipseAnimationEndPosition = 213
                        ProgressBarTemplateSettings_EllipseAnimationWellPosition = 214
                        ProgressBarTemplateSettings_EllipseDiameter = 215
                        ProgressBarTemplateSettings_EllipseOffset = 216
                        ProgressBarTemplateSettings_IndicatorLengthDelta = 217
                        ProgressRingTemplateSettings_EllipseDiameter = 218
                        ProgressRingTemplateSettings_EllipseOffset = 219
                        ProgressRingTemplateSettings_MaxSideLength = 220
                        PropertyPath_Path = 221
                        RowDefinition_ActualHeight = 226
                        RowDefinition_Height = 227
                        RowDefinition_MaxHeight = 228
                        RowDefinition_MinHeight = 229
                        SetterBase_IsSealed = 233
                        SettingsFlyoutTemplateSettings_BorderBrush = 234
                        SettingsFlyoutTemplateSettings_BorderThickness = 235
                        SettingsFlyoutTemplateSettings_ContentTransitions = 236
                        SettingsFlyoutTemplateSettings_HeaderBackground = 237
                        SettingsFlyoutTemplateSettings_HeaderForeground = 238
                        SettingsFlyoutTemplateSettings_IconSource = 239
                        Style_BasedOn = 244
                        Style_IsSealed = 245
                        Style_Setters = 246
                        Style_TargetType = 247
                        TextElement_CharacterSpacing = 249
                        TextElement_FontFamily = 250
                        TextElement_FontSize = 251
                        TextElement_FontStretch = 252
                        TextElement_FontStyle = 253
                        TextElement_FontWeight = 254
                        TextElement_Foreground = 255
                        TextElement_IsTextScaleFactorEnabled = 256
                        TextElement_Language = 257
                        Timeline_AutoReverse = 263
                        Timeline_BeginTime = 264
                        Timeline_Duration = 265
                        Timeline_FillBehavior = 266
                        Timeline_RepeatBehavior = 267
                        Timeline_SpeedRatio = 268
                        TimelineMarker_Text = 269
                        TimelineMarker_Time = 270
                        TimelineMarker_Type = 271
                        ToggleSwitchTemplateSettings_CurtainCurrentToOffOffset = 273
                        ToggleSwitchTemplateSettings_CurtainCurrentToOnOffset = 274
                        ToggleSwitchTemplateSettings_CurtainOffToOnOffset = 275
                        ToggleSwitchTemplateSettings_CurtainOnToOffOffset = 276
                        ToggleSwitchTemplateSettings_KnobCurrentToOffOffset = 277
                        ToggleSwitchTemplateSettings_KnobCurrentToOnOffset = 278
                        ToggleSwitchTemplateSettings_KnobOffToOnOffset = 279
                        ToggleSwitchTemplateSettings_KnobOnToOffOffset = 280
                        ToolTipTemplateSettings_FromHorizontalOffset = 281
                        ToolTipTemplateSettings_FromVerticalOffset = 282
                        UIElement_AllowDrop = 292
                        UIElement_CacheMode = 293
                        UIElement_Clip = 295
                        UIElement_CompositeMode = 296
                        UIElement_IsDoubleTapEnabled = 297
                        UIElement_IsHitTestVisible = 298
                        UIElement_IsHoldingEnabled = 299
                        UIElement_IsRightTapEnabled = 300
                        UIElement_IsTapEnabled = 301
                        UIElement_ManipulationMode = 302
                        UIElement_Opacity = 303
                        UIElement_PointerCaptures = 304
                        UIElement_Projection = 305
                        UIElement_RenderSize = 306
                        UIElement_RenderTransform = 307
                        UIElement_RenderTransformOrigin = 308
                        UIElement_Transitions = 309
                        UIElement_UseLayoutRounding = 311
                        UIElement_Visibility = 312
                        VisualState_Storyboard = 322
                        VisualStateGroup_States = 323
                        VisualStateGroup_Transitions = 324
                        VisualStateManager_CustomVisualStateManager = 325
                        VisualStateManager_VisualStateGroups = 326
                        VisualTransition_From = 327
                        VisualTransition_GeneratedDuration = 328
                        VisualTransition_GeneratedEasingFunction = 329
                        VisualTransition_Storyboard = 330
                        VisualTransition_To = 331
                        ArcSegment_IsLargeArc = 332
                        ArcSegment_Point = 333
                        ArcSegment_RotationAngle = 334
                        ArcSegment_Size = 335
                        ArcSegment_SweepDirection = 336
                        BackEase_Amplitude = 337
                        BeginStoryboard_Storyboard = 338
                        BezierSegment_Point1 = 339
                        BezierSegment_Point2 = 340
                        BezierSegment_Point3 = 341
                        BitmapSource_PixelHeight = 342
                        BitmapSource_PixelWidth = 343
                        Block_LineHeight = 344
                        Block_LineStackingStrategy = 345
                        Block_Margin = 346
                        Block_TextAlignment = 347
                        BounceEase_Bounces = 348
                        BounceEase_Bounciness = 349
                        ColorAnimation_By = 350
                        ColorAnimation_EasingFunction = 351
                        ColorAnimation_EnableDependentAnimation = 352
                        ColorAnimation_From = 353
                        ColorAnimation_To = 354
                        ColorAnimationUsingKeyFrames_EnableDependentAnimation = 355
                        ColorAnimationUsingKeyFrames_KeyFrames = 356
                        ContentThemeTransition_HorizontalOffset = 357
                        ContentThemeTransition_VerticalOffset = 358
                        ControlTemplate_TargetType = 359
                        DispatcherTimer_Interval = 362
                        DoubleAnimation_By = 363
                        DoubleAnimation_EasingFunction = 364
                        DoubleAnimation_EnableDependentAnimation = 365
                        DoubleAnimation_From = 366
                        DoubleAnimation_To = 367
                        DoubleAnimationUsingKeyFrames_EnableDependentAnimation = 368
                        DoubleAnimationUsingKeyFrames_KeyFrames = 369
                        EasingColorKeyFrame_EasingFunction = 372
                        EasingDoubleKeyFrame_EasingFunction = 373
                        EasingPointKeyFrame_EasingFunction = 374
                        EdgeUIThemeTransition_Edge = 375
                        ElasticEase_Oscillations = 376
                        ElasticEase_Springiness = 377
                        EllipseGeometry_Center = 378
                        EllipseGeometry_RadiusX = 379
                        EllipseGeometry_RadiusY = 380
                        EntranceThemeTransition_FromHorizontalOffset = 381
                        EntranceThemeTransition_FromVerticalOffset = 382
                        EntranceThemeTransition_IsStaggeringEnabled = 383
                        EventTrigger_Actions = 384
                        EventTrigger_RoutedEvent = 385
                        ExponentialEase_Exponent = 386
                        Flyout_Content = 387
                        Flyout_FlyoutPresenterStyle = 388
                        FrameworkElement_ActualHeight = 389
                        FrameworkElement_ActualWidth = 390
                        FrameworkElement_DataContext = 391
                        FrameworkElement_FlowDirection = 392
                        FrameworkElement_Height = 393
                        FrameworkElement_HorizontalAlignment = 394
                        FrameworkElement_Language = 396
                        FrameworkElement_Margin = 397
                        FrameworkElement_MaxHeight = 398
                        FrameworkElement_MaxWidth = 399
                        FrameworkElement_MinHeight = 400
                        FrameworkElement_MinWidth = 401
                        FrameworkElement_Parent = 402
                        FrameworkElement_RequestedTheme = 403
                        FrameworkElement_Resources = 404
                        FrameworkElement_Style = 405
                        FrameworkElement_Tag = 406
                        FrameworkElement_Triggers = 407
                        FrameworkElement_VerticalAlignment = 408
                        FrameworkElement_Width = 409
                        FrameworkElementAutomationPeer_Owner = 410
                        GeometryGroup_Children = 411
                        GeometryGroup_FillRule = 412
                        GradientBrush_ColorInterpolationMode = 413
                        GradientBrush_GradientStops = 414
                        GradientBrush_MappingMode = 415
                        GradientBrush_SpreadMethod = 416
                        GridViewItemTemplateSettings_DragItemsCount = 417
                        ItemAutomationPeer_Item = 419
                        ItemAutomationPeer_ItemsControlAutomationPeer = 420
                        LineGeometry_EndPoint = 422
                        LineGeometry_StartPoint = 423
                        LineSegment_Point = 424
                        ListViewItemTemplateSettings_DragItemsCount = 425
                        Matrix3DProjection_ProjectionMatrix = 426
                        MenuFlyout_Items = 427
                        MenuFlyout_MenuFlyoutPresenterStyle = 428
                        ObjectAnimationUsingKeyFrames_EnableDependentAnimation = 429
                        ObjectAnimationUsingKeyFrames_KeyFrames = 430
                        PaneThemeTransition_Edge = 431
                        PathGeometry_Figures = 432
                        PathGeometry_FillRule = 433
                        PlaneProjection_CenterOfRotationX = 434
                        PlaneProjection_CenterOfRotationY = 435
                        PlaneProjection_CenterOfRotationZ = 436
                        PlaneProjection_GlobalOffsetX = 437
                        PlaneProjection_GlobalOffsetY = 438
                        PlaneProjection_GlobalOffsetZ = 439
                        PlaneProjection_LocalOffsetX = 440
                        PlaneProjection_LocalOffsetY = 441
                        PlaneProjection_LocalOffsetZ = 442
                        PlaneProjection_ProjectionMatrix = 443
                        PlaneProjection_RotationX = 444
                        PlaneProjection_RotationY = 445
                        PlaneProjection_RotationZ = 446
                        PointAnimation_By = 447
                        PointAnimation_EasingFunction = 448
                        PointAnimation_EnableDependentAnimation = 449
                        PointAnimation_From = 450
                        PointAnimation_To = 451
                        PointAnimationUsingKeyFrames_EnableDependentAnimation = 452
                        PointAnimationUsingKeyFrames_KeyFrames = 453
                        PolyBezierSegment_Points = 456
                        PolyLineSegment_Points = 457
                        PolyQuadraticBezierSegment_Points = 458
                        PopupThemeTransition_FromHorizontalOffset = 459
                        PopupThemeTransition_FromVerticalOffset = 460
                        PowerEase_Power = 461
                        QuadraticBezierSegment_Point1 = 466
                        QuadraticBezierSegment_Point2 = 467
                        RectangleGeometry_Rect = 470
                        RelativeSource_Mode = 471
                        RenderTargetBitmap_PixelHeight = 472
                        RenderTargetBitmap_PixelWidth = 473
                        Setter_Property = 474
                        Setter_Value = 475
                        SolidColorBrush_Color = 476
                        SplineColorKeyFrame_KeySpline = 477
                        SplineDoubleKeyFrame_KeySpline = 478
                        SplinePointKeyFrame_KeySpline = 479
                        TileBrush_AlignmentX = 483
                        TileBrush_AlignmentY = 484
                        TileBrush_Stretch = 485
                        Binding_Converter = 487
                        Binding_ConverterLanguage = 488
                        Binding_ConverterParameter = 489
                        Binding_ElementName = 490
                        Binding_FallbackValue = 491
                        Binding_Mode = 492
                        Binding_Path = 493
                        Binding_RelativeSource = 494
                        Binding_Source = 495
                        Binding_TargetNullValue = 496
                        Binding_UpdateSourceTrigger = 497
                        BitmapImage_CreateOptions = 498
                        BitmapImage_DecodePixelHeight = 499
                        BitmapImage_DecodePixelType = 500
                        BitmapImage_DecodePixelWidth = 501
                        BitmapImage_UriSource = 502
                        Border_Background = 503
                        Border_BorderBrush = 504
                        Border_BorderThickness = 505
                        Border_Child = 506
                        Border_ChildTransitions = 507
                        Border_CornerRadius = 508
                        Border_Padding = 509
                        CaptureElement_Source = 510
                        CaptureElement_Stretch = 511
                        CompositeTransform_CenterX = 514
                        CompositeTransform_CenterY = 515
                        CompositeTransform_Rotation = 516
                        CompositeTransform_ScaleX = 517
                        CompositeTransform_ScaleY = 518
                        CompositeTransform_SkewX = 519
                        CompositeTransform_SkewY = 520
                        CompositeTransform_TranslateX = 521
                        CompositeTransform_TranslateY = 522
                        ContentPresenter_CharacterSpacing = 523
                        ContentPresenter_Content = 524
                        ContentPresenter_ContentTemplate = 525
                        ContentPresenter_ContentTemplateSelector = 526
                        ContentPresenter_ContentTransitions = 527
                        ContentPresenter_FontFamily = 528
                        ContentPresenter_FontSize = 529
                        ContentPresenter_FontStretch = 530
                        ContentPresenter_FontStyle = 531
                        ContentPresenter_FontWeight = 532
                        ContentPresenter_Foreground = 533
                        ContentPresenter_IsTextScaleFactorEnabled = 534
                        ContentPresenter_LineStackingStrategy = 535
                        ContentPresenter_MaxLines = 536
                        ContentPresenter_OpticalMarginAlignment = 537
                        ContentPresenter_TextLineBounds = 539
                        ContentPresenter_TextWrapping = 540
                        Control_Background = 541
                        Control_BorderBrush = 542
                        Control_BorderThickness = 543
                        Control_CharacterSpacing = 544
                        Control_FocusState = 546
                        Control_FontFamily = 547
                        Control_FontSize = 548
                        Control_FontStretch = 549
                        Control_FontStyle = 550
                        Control_FontWeight = 551
                        Control_Foreground = 552
                        Control_HorizontalContentAlignment = 553
                        Control_IsEnabled = 554
                        Control_IsTabStop = 555
                        Control_IsTextScaleFactorEnabled = 556
                        Control_Padding = 557
                        Control_TabIndex = 558
                        Control_TabNavigation = 559
                        Control_Template = 560
                        Control_VerticalContentAlignment = 561
                        DragItemThemeAnimation_TargetName = 565
                        DragOverThemeAnimation_Direction = 566
                        DragOverThemeAnimation_TargetName = 567
                        DragOverThemeAnimation_ToOffset = 568
                        DropTargetItemThemeAnimation_TargetName = 569
                        FadeInThemeAnimation_TargetName = 570
                        FadeOutThemeAnimation_TargetName = 571
                        Glyphs_Fill = 574
                        Glyphs_FontRenderingEmSize = 575
                        Glyphs_FontUri = 576
                        Glyphs_Indices = 577
                        Glyphs_OriginX = 578
                        Glyphs_OriginY = 579
                        Glyphs_StyleSimulations = 580
                        Glyphs_UnicodeString = 581
                        IconElement_Foreground = 584
                        Image_NineGrid = 586
                        Image_PlayToSource = 587
                        Image_Source = 588
                        Image_Stretch = 589
                        ImageBrush_ImageSource = 591
                        InlineUIContainer_Child = 592
                        ItemsPresenter_Footer = 594
                        ItemsPresenter_FooterTemplate = 595
                        ItemsPresenter_FooterTransitions = 596
                        ItemsPresenter_Header = 597
                        ItemsPresenter_HeaderTemplate = 598
                        ItemsPresenter_HeaderTransitions = 599
                        ItemsPresenter_Padding = 601
                        LinearGradientBrush_EndPoint = 602
                        LinearGradientBrush_StartPoint = 603
                        MatrixTransform_Matrix = 604
                        MediaElement_ActualStereo3DVideoPackingMode = 605
                        MediaElement_AreTransportControlsEnabled = 606
                        MediaElement_AspectRatioHeight = 607
                        MediaElement_AspectRatioWidth = 608
                        MediaElement_AudioCategory = 609
                        MediaElement_AudioDeviceType = 610
                        MediaElement_AudioStreamCount = 611
                        MediaElement_AudioStreamIndex = 612
                        MediaElement_AutoPlay = 613
                        MediaElement_Balance = 614
                        MediaElement_BufferingProgress = 615
                        MediaElement_CanPause = 616
                        MediaElement_CanSeek = 617
                        MediaElement_CurrentState = 618
                        MediaElement_DefaultPlaybackRate = 619
                        MediaElement_DownloadProgress = 620
                        MediaElement_DownloadProgressOffset = 621
                        MediaElement_IsAudioOnly = 623
                        MediaElement_IsFullWindow = 624
                        MediaElement_IsLooping = 625
                        MediaElement_IsMuted = 626
                        MediaElement_IsStereo3DVideo = 627
                        MediaElement_Markers = 628
                        MediaElement_NaturalDuration = 629
                        MediaElement_NaturalVideoHeight = 630
                        MediaElement_NaturalVideoWidth = 631
                        MediaElement_PlaybackRate = 632
                        MediaElement_PlayToPreferredSourceUri = 633
                        MediaElement_PlayToSource = 634
                        MediaElement_Position = 635
                        MediaElement_PosterSource = 636
                        MediaElement_ProtectionManager = 637
                        MediaElement_RealTimePlayback = 638
                        MediaElement_Source = 639
                        MediaElement_Stereo3DVideoPackingMode = 640
                        MediaElement_Stereo3DVideoRenderMode = 641
                        MediaElement_Stretch = 642
                        MediaElement_TransportControls = 643
                        MediaElement_Volume = 644
                        Panel_Background = 647
                        Panel_Children = 648
                        Panel_ChildrenTransitions = 649
                        Panel_IsItemsHost = 651
                        Paragraph_Inlines = 652
                        Paragraph_TextIndent = 653
                        PointerDownThemeAnimation_TargetName = 660
                        PointerUpThemeAnimation_TargetName = 662
                        PopInThemeAnimation_FromHorizontalOffset = 664
                        PopInThemeAnimation_FromVerticalOffset = 665
                        PopInThemeAnimation_TargetName = 666
                        PopOutThemeAnimation_TargetName = 667
                        Popup_Child = 668
                        Popup_ChildTransitions = 669
                        Popup_HorizontalOffset = 670
                        Popup_IsLightDismissEnabled = 673
                        Popup_IsOpen = 674
                        Popup_VerticalOffset = 676
                        RepositionThemeAnimation_FromHorizontalOffset = 683
                        RepositionThemeAnimation_FromVerticalOffset = 684
                        RepositionThemeAnimation_TargetName = 685
                        ResourceDictionary_MergedDictionaries = 687
                        ResourceDictionary_Source = 688
                        ResourceDictionary_ThemeDictionaries = 689
                        RichTextBlock_Blocks = 691
                        RichTextBlock_CharacterSpacing = 692
                        RichTextBlock_FontFamily = 693
                        RichTextBlock_FontSize = 694
                        RichTextBlock_FontStretch = 695
                        RichTextBlock_FontStyle = 696
                        RichTextBlock_FontWeight = 697
                        RichTextBlock_Foreground = 698
                        RichTextBlock_HasOverflowContent = 699
                        RichTextBlock_IsColorFontEnabled = 700
                        RichTextBlock_IsTextScaleFactorEnabled = 701
                        RichTextBlock_IsTextSelectionEnabled = 702
                        RichTextBlock_LineHeight = 703
                        RichTextBlock_LineStackingStrategy = 704
                        RichTextBlock_MaxLines = 705
                        RichTextBlock_OpticalMarginAlignment = 706
                        RichTextBlock_OverflowContentTarget = 707
                        RichTextBlock_Padding = 708
                        RichTextBlock_SelectedText = 709
                        RichTextBlock_SelectionHighlightColor = 710
                        RichTextBlock_TextAlignment = 711
                        RichTextBlock_TextIndent = 712
                        RichTextBlock_TextLineBounds = 713
                        RichTextBlock_TextReadingOrder = 714
                        RichTextBlock_TextTrimming = 715
                        RichTextBlock_TextWrapping = 716
                        RichTextBlockOverflow_HasOverflowContent = 717
                        RichTextBlockOverflow_MaxLines = 718
                        RichTextBlockOverflow_OverflowContentTarget = 719
                        RichTextBlockOverflow_Padding = 720
                        RotateTransform_Angle = 721
                        RotateTransform_CenterX = 722
                        RotateTransform_CenterY = 723
                        Run_FlowDirection = 725
                        Run_Text = 726
                        ScaleTransform_CenterX = 727
                        ScaleTransform_CenterY = 728
                        ScaleTransform_ScaleX = 729
                        ScaleTransform_ScaleY = 730
                        SetterBaseCollection_IsSealed = 732
                        Shape_Fill = 733
                        Shape_GeometryTransform = 734
                        Shape_Stretch = 735
                        Shape_Stroke = 736
                        Shape_StrokeDashArray = 737
                        Shape_StrokeDashCap = 738
                        Shape_StrokeDashOffset = 739
                        Shape_StrokeEndLineCap = 740
                        Shape_StrokeLineJoin = 741
                        Shape_StrokeMiterLimit = 742
                        Shape_StrokeStartLineCap = 743
                        Shape_StrokeThickness = 744
                        SkewTransform_AngleX = 745
                        SkewTransform_AngleY = 746
                        SkewTransform_CenterX = 747
                        SkewTransform_CenterY = 748
                        Span_Inlines = 749
                        SplitCloseThemeAnimation_ClosedLength = 750
                        SplitCloseThemeAnimation_ClosedTarget = 751
                        SplitCloseThemeAnimation_ClosedTargetName = 752
                        SplitCloseThemeAnimation_ContentTarget = 753
                        SplitCloseThemeAnimation_ContentTargetName = 754
                        SplitCloseThemeAnimation_ContentTranslationDirection = 755
                        SplitCloseThemeAnimation_ContentTranslationOffset = 756
                        SplitCloseThemeAnimation_OffsetFromCenter = 757
                        SplitCloseThemeAnimation_OpenedLength = 758
                        SplitCloseThemeAnimation_OpenedTarget = 759
                        SplitCloseThemeAnimation_OpenedTargetName = 760
                        SplitOpenThemeAnimation_ClosedLength = 761
                        SplitOpenThemeAnimation_ClosedTarget = 762
                        SplitOpenThemeAnimation_ClosedTargetName = 763
                        SplitOpenThemeAnimation_ContentTarget = 764
                        SplitOpenThemeAnimation_ContentTargetName = 765
                        SplitOpenThemeAnimation_ContentTranslationDirection = 766
                        SplitOpenThemeAnimation_ContentTranslationOffset = 767
                        SplitOpenThemeAnimation_OffsetFromCenter = 768
                        SplitOpenThemeAnimation_OpenedLength = 769
                        SplitOpenThemeAnimation_OpenedTarget = 770
                        SplitOpenThemeAnimation_OpenedTargetName = 771
                        Storyboard_Children = 772
                        Storyboard_TargetName = 774
                        Storyboard_TargetProperty = 775
                        SwipeBackThemeAnimation_FromHorizontalOffset = 776
                        SwipeBackThemeAnimation_FromVerticalOffset = 777
                        SwipeBackThemeAnimation_TargetName = 778
                        SwipeHintThemeAnimation_TargetName = 779
                        SwipeHintThemeAnimation_ToHorizontalOffset = 780
                        SwipeHintThemeAnimation_ToVerticalOffset = 781
                        TextBlock_CharacterSpacing = 782
                        TextBlock_FontFamily = 783
                        TextBlock_FontSize = 784
                        TextBlock_FontStretch = 785
                        TextBlock_FontStyle = 786
                        TextBlock_FontWeight = 787
                        TextBlock_Foreground = 788
                        TextBlock_Inlines = 789
                        TextBlock_IsColorFontEnabled = 790
                        TextBlock_IsTextScaleFactorEnabled = 791
                        TextBlock_IsTextSelectionEnabled = 792
                        TextBlock_LineHeight = 793
                        TextBlock_LineStackingStrategy = 794
                        TextBlock_MaxLines = 795
                        TextBlock_OpticalMarginAlignment = 796
                        TextBlock_Padding = 797
                        TextBlock_SelectedText = 798
                        TextBlock_SelectionHighlightColor = 799
                        TextBlock_Text = 800
                        TextBlock_TextAlignment = 801
                        TextBlock_TextDecorations = 802
                        TextBlock_TextLineBounds = 803
                        TextBlock_TextReadingOrder = 804
                        TextBlock_TextTrimming = 805
                        TextBlock_TextWrapping = 806
                        TransformGroup_Children = 811
                        TransformGroup_Value = 812
                        TranslateTransform_X = 814
                        TranslateTransform_Y = 815
                        Viewbox_Child = 819
                        Viewbox_Stretch = 820
                        Viewbox_StretchDirection = 821
                        WebViewBrush_SourceName = 825
                        AppBarSeparator_IsCompact = 826
                        BitmapIcon_UriSource = 827
                        Canvas_Left = 828
                        Canvas_Top = 829
                        Canvas_ZIndex = 830
                        ContentControl_Content = 832
                        ContentControl_ContentTemplate = 833
                        ContentControl_ContentTemplateSelector = 834
                        ContentControl_ContentTransitions = 835
                        DatePicker_CalendarIdentifier = 837
                        DatePicker_Date = 838
                        DatePicker_DayFormat = 839
                        DatePicker_DayVisible = 840
                        DatePicker_Header = 841
                        DatePicker_HeaderTemplate = 842
                        DatePicker_MaxYear = 843
                        DatePicker_MinYear = 844
                        DatePicker_MonthFormat = 845
                        DatePicker_MonthVisible = 846
                        DatePicker_Orientation = 847
                        DatePicker_YearFormat = 848
                        DatePicker_YearVisible = 849
                        FontIcon_FontFamily = 851
                        FontIcon_FontSize = 852
                        FontIcon_FontStyle = 853
                        FontIcon_FontWeight = 854
                        FontIcon_Glyph = 855
                        FontIcon_IsTextScaleFactorEnabled = 856
                        Grid_Column = 857
                        Grid_ColumnDefinitions = 858
                        Grid_ColumnSpan = 859
                        Grid_Row = 860
                        Grid_RowDefinitions = 861
                        Grid_RowSpan = 862
                        Hub_DefaultSectionIndex = 863
                        Hub_Header = 864
                        Hub_HeaderTemplate = 865
                        Hub_IsActiveView = 866
                        Hub_IsZoomedInView = 867
                        Hub_Orientation = 868
                        Hub_SectionHeaders = 869
                        Hub_Sections = 870
                        Hub_SectionsInView = 871
                        Hub_SemanticZoomOwner = 872
                        HubSection_ContentTemplate = 873
                        HubSection_Header = 874
                        HubSection_HeaderTemplate = 875
                        HubSection_IsHeaderInteractive = 876
                        Hyperlink_NavigateUri = 877
                        ItemsControl_DisplayMemberPath = 879
                        ItemsControl_GroupStyle = 880
                        ItemsControl_GroupStyleSelector = 881
                        ItemsControl_IsGrouping = 882
                        ItemsControl_ItemContainerStyle = 884
                        ItemsControl_ItemContainerStyleSelector = 885
                        ItemsControl_ItemContainerTransitions = 886
                        ItemsControl_Items = 887
                        ItemsControl_ItemsPanel = 889
                        ItemsControl_ItemsSource = 890
                        ItemsControl_ItemTemplate = 891
                        ItemsControl_ItemTemplateSelector = 892
                        Line_X1 = 893
                        Line_X2 = 894
                        Line_Y1 = 895
                        Line_Y2 = 896
                        MediaTransportControls_IsFastForwardButtonVisible = 898
                        MediaTransportControls_IsFastRewindButtonVisible = 900
                        MediaTransportControls_IsFullWindowButtonVisible = 902
                        MediaTransportControls_IsPlaybackRateButtonVisible = 904
                        MediaTransportControls_IsSeekBarVisible = 905
                        MediaTransportControls_IsStopButtonVisible = 908
                        MediaTransportControls_IsVolumeButtonVisible = 910
                        MediaTransportControls_IsZoomButtonVisible = 912
                        PasswordBox_Header = 913
                        PasswordBox_HeaderTemplate = 914
                        PasswordBox_IsPasswordRevealButtonEnabled = 915
                        PasswordBox_MaxLength = 916
                        PasswordBox_Password = 917
                        PasswordBox_PasswordChar = 918
                        PasswordBox_PlaceholderText = 919
                        PasswordBox_PreventKeyboardDisplayOnProgrammaticFocus = 920
                        PasswordBox_SelectionHighlightColor = 921
                        Path_Data = 922
                        PathIcon_Data = 923
                        Polygon_FillRule = 924
                        Polygon_Points = 925
                        Polyline_FillRule = 926
                        Polyline_Points = 927
                        ProgressRing_IsActive = 928
                        ProgressRing_TemplateSettings = 929
                        RangeBase_LargeChange = 930
                        RangeBase_Maximum = 931
                        RangeBase_Minimum = 932
                        RangeBase_SmallChange = 933
                        RangeBase_Value = 934
                        Rectangle_RadiusX = 935
                        Rectangle_RadiusY = 936
                        RichEditBox_AcceptsReturn = 937
                        RichEditBox_Header = 938
                        RichEditBox_HeaderTemplate = 939
                        RichEditBox_InputScope = 940
                        RichEditBox_IsColorFontEnabled = 941
                        RichEditBox_IsReadOnly = 942
                        RichEditBox_IsSpellCheckEnabled = 943
                        RichEditBox_IsTextPredictionEnabled = 944
                        RichEditBox_PlaceholderText = 945
                        RichEditBox_PreventKeyboardDisplayOnProgrammaticFocus = 946
                        RichEditBox_SelectionHighlightColor = 947
                        RichEditBox_TextAlignment = 948
                        RichEditBox_TextWrapping = 949
                        SearchBox_ChooseSuggestionOnEnter = 950
                        SearchBox_FocusOnKeyboardInput = 951
                        SearchBox_PlaceholderText = 952
                        SearchBox_QueryText = 953
                        SearchBox_SearchHistoryContext = 954
                        SearchBox_SearchHistoryEnabled = 955
                        SemanticZoom_CanChangeViews = 956
                        SemanticZoom_IsZoomedInViewActive = 957
                        SemanticZoom_IsZoomOutButtonEnabled = 958
                        SemanticZoom_ZoomedInView = 959
                        SemanticZoom_ZoomedOutView = 960
                        StackPanel_AreScrollSnapPointsRegular = 961
                        StackPanel_Orientation = 962
                        SymbolIcon_Symbol = 963
                        TextBox_AcceptsReturn = 964
                        TextBox_Header = 965
                        TextBox_HeaderTemplate = 966
                        TextBox_InputScope = 967
                        TextBox_IsColorFontEnabled = 968
                        TextBox_IsReadOnly = 971
                        TextBox_IsSpellCheckEnabled = 972
                        TextBox_IsTextPredictionEnabled = 973
                        TextBox_MaxLength = 974
                        TextBox_PlaceholderText = 975
                        TextBox_PreventKeyboardDisplayOnProgrammaticFocus = 976
                        TextBox_SelectedText = 977
                        TextBox_SelectionHighlightColor = 978
                        TextBox_SelectionLength = 979
                        TextBox_SelectionStart = 980
                        TextBox_Text = 981
                        TextBox_TextAlignment = 982
                        TextBox_TextWrapping = 983
                        Thumb_IsDragging = 984
                        TickBar_Fill = 985
                        TimePicker_ClockIdentifier = 986
                        TimePicker_Header = 987
                        TimePicker_HeaderTemplate = 988
                        TimePicker_MinuteIncrement = 989
                        TimePicker_Time = 990
                        ToggleSwitch_Header = 991
                        ToggleSwitch_HeaderTemplate = 992
                        ToggleSwitch_IsOn = 993
                        ToggleSwitch_OffContent = 994
                        ToggleSwitch_OffContentTemplate = 995
                        ToggleSwitch_OnContent = 996
                        ToggleSwitch_OnContentTemplate = 997
                        ToggleSwitch_TemplateSettings = 998
                        UserControl_Content = 999
                        VariableSizedWrapGrid_ColumnSpan = 1000
                        VariableSizedWrapGrid_HorizontalChildrenAlignment = 1001
                        VariableSizedWrapGrid_ItemHeight = 1002
                        VariableSizedWrapGrid_ItemWidth = 1003
                        VariableSizedWrapGrid_MaximumRowsOrColumns = 1004
                        VariableSizedWrapGrid_Orientation = 1005
                        VariableSizedWrapGrid_RowSpan = 1006
                        VariableSizedWrapGrid_VerticalChildrenAlignment = 1007
                        WebView_AllowedScriptNotifyUris = 1008
                        WebView_CanGoBack = 1009
                        WebView_CanGoForward = 1010
                        WebView_ContainsFullScreenElement = 1011
                        WebView_DataTransferPackage = 1012
                        WebView_DefaultBackgroundColor = 1013
                        WebView_DocumentTitle = 1014
                        WebView_Source = 1015
                        AppBar_ClosedDisplayMode = 1016
                        AppBar_IsOpen = 1017
                        AppBar_IsSticky = 1018
                        AutoSuggestBox_AutoMaximizeSuggestionArea = 1019
                        AutoSuggestBox_Header = 1020
                        AutoSuggestBox_IsSuggestionListOpen = 1021
                        AutoSuggestBox_MaxSuggestionListHeight = 1022
                        AutoSuggestBox_PlaceholderText = 1023
                        AutoSuggestBox_Text = 1024
                        AutoSuggestBox_TextBoxStyle = 1025
                        AutoSuggestBox_TextMemberPath = 1026
                        AutoSuggestBox_UpdateTextOnSelect = 1027
                        ButtonBase_ClickMode = 1029
                        ButtonBase_Command = 1030
                        ButtonBase_CommandParameter = 1031
                        ButtonBase_IsPointerOver = 1032
                        ButtonBase_IsPressed = 1033
                        ContentDialog_FullSizeDesired = 1034
                        ContentDialog_IsPrimaryButtonEnabled = 1035
                        ContentDialog_IsSecondaryButtonEnabled = 1036
                        ContentDialog_PrimaryButtonCommand = 1037
                        ContentDialog_PrimaryButtonCommandParameter = 1038
                        ContentDialog_PrimaryButtonText = 1039
                        ContentDialog_SecondaryButtonCommand = 1040
                        ContentDialog_SecondaryButtonCommandParameter = 1041
                        ContentDialog_SecondaryButtonText = 1042
                        ContentDialog_Title = 1043
                        ContentDialog_TitleTemplate = 1044
                        Frame_BackStack = 1045
                        Frame_BackStackDepth = 1046
                        Frame_CacheSize = 1047
                        Frame_CanGoBack = 1048
                        Frame_CanGoForward = 1049
                        Frame_CurrentSourcePageType = 1050
                        Frame_ForwardStack = 1051
                        Frame_SourcePageType = 1052
                        GridViewItemPresenter_CheckBrush = 1053
                        GridViewItemPresenter_CheckHintBrush = 1054
                        GridViewItemPresenter_CheckSelectingBrush = 1055
                        GridViewItemPresenter_ContentMargin = 1056
                        GridViewItemPresenter_DisabledOpacity = 1057
                        GridViewItemPresenter_DragBackground = 1058
                        GridViewItemPresenter_DragForeground = 1059
                        GridViewItemPresenter_DragOpacity = 1060
                        GridViewItemPresenter_FocusBorderBrush = 1061
                        GridViewItemPresenter_GridViewItemPresenterHorizontalContentAlignment = 1062
                        GridViewItemPresenter_GridViewItemPresenterPadding = 1063
                        GridViewItemPresenter_PlaceholderBackground = 1064
                        GridViewItemPresenter_PointerOverBackground = 1065
                        GridViewItemPresenter_PointerOverBackgroundMargin = 1066
                        GridViewItemPresenter_ReorderHintOffset = 1067
                        GridViewItemPresenter_SelectedBackground = 1068
                        GridViewItemPresenter_SelectedBorderThickness = 1069
                        GridViewItemPresenter_SelectedForeground = 1070
                        GridViewItemPresenter_SelectedPointerOverBackground = 1071
                        GridViewItemPresenter_SelectedPointerOverBorderBrush = 1072
                        GridViewItemPresenter_SelectionCheckMarkVisualEnabled = 1073
                        GridViewItemPresenter_GridViewItemPresenterVerticalContentAlignment = 1074
                        ItemsStackPanel_CacheLength = 1076
                        ItemsStackPanel_GroupHeaderPlacement = 1077
                        ItemsStackPanel_GroupPadding = 1078
                        ItemsStackPanel_ItemsUpdatingScrollMode = 1079
                        ItemsStackPanel_Orientation = 1080
                        ItemsWrapGrid_CacheLength = 1081
                        ItemsWrapGrid_GroupHeaderPlacement = 1082
                        ItemsWrapGrid_GroupPadding = 1083
                        ItemsWrapGrid_ItemHeight = 1084
                        ItemsWrapGrid_ItemWidth = 1085
                        ItemsWrapGrid_MaximumRowsOrColumns = 1086
                        ItemsWrapGrid_Orientation = 1087
                        ListViewItemPresenter_CheckBrush = 1088
                        ListViewItemPresenter_CheckHintBrush = 1089
                        ListViewItemPresenter_CheckSelectingBrush = 1090
                        ListViewItemPresenter_ContentMargin = 1091
                        ListViewItemPresenter_DisabledOpacity = 1092
                        ListViewItemPresenter_DragBackground = 1093
                        ListViewItemPresenter_DragForeground = 1094
                        ListViewItemPresenter_DragOpacity = 1095
                        ListViewItemPresenter_FocusBorderBrush = 1096
                        ListViewItemPresenter_ListViewItemPresenterHorizontalContentAlignment = 1097
                        ListViewItemPresenter_ListViewItemPresenterPadding = 1098
                        ListViewItemPresenter_PlaceholderBackground = 1099
                        ListViewItemPresenter_PointerOverBackground = 1100
                        ListViewItemPresenter_PointerOverBackgroundMargin = 1101
                        ListViewItemPresenter_ReorderHintOffset = 1102
                        ListViewItemPresenter_SelectedBackground = 1103
                        ListViewItemPresenter_SelectedBorderThickness = 1104
                        ListViewItemPresenter_SelectedForeground = 1105
                        ListViewItemPresenter_SelectedPointerOverBackground = 1106
                        ListViewItemPresenter_SelectedPointerOverBorderBrush = 1107
                        ListViewItemPresenter_SelectionCheckMarkVisualEnabled = 1108
                        ListViewItemPresenter_ListViewItemPresenterVerticalContentAlignment = 1109
                        MenuFlyoutItem_Command = 1110
                        MenuFlyoutItem_CommandParameter = 1111
                        MenuFlyoutItem_Text = 1112
                        Page_BottomAppBar = 1114
                        Page_Frame = 1115
                        Page_NavigationCacheMode = 1116
                        Page_TopAppBar = 1117
                        ProgressBar_IsIndeterminate = 1118
                        ProgressBar_ShowError = 1119
                        ProgressBar_ShowPaused = 1120
                        ProgressBar_TemplateSettings = 1121
                        ScrollBar_IndicatorMode = 1122
                        ScrollBar_Orientation = 1123
                        ScrollBar_ViewportSize = 1124
                        Selector_IsSynchronizedWithCurrentItem = 1126
                        Selector_SelectedIndex = 1127
                        Selector_SelectedItem = 1128
                        Selector_SelectedValue = 1129
                        Selector_SelectedValuePath = 1130
                        SelectorItem_IsSelected = 1131
                        SettingsFlyout_HeaderBackground = 1132
                        SettingsFlyout_HeaderForeground = 1133
                        SettingsFlyout_IconSource = 1134
                        SettingsFlyout_TemplateSettings = 1135
                        SettingsFlyout_Title = 1136
                        Slider_Header = 1137
                        Slider_HeaderTemplate = 1138
                        Slider_IntermediateValue = 1139
                        Slider_IsDirectionReversed = 1140
                        Slider_IsThumbToolTipEnabled = 1141
                        Slider_Orientation = 1142
                        Slider_SnapsTo = 1143
                        Slider_StepFrequency = 1144
                        Slider_ThumbToolTipValueConverter = 1145
                        Slider_TickFrequency = 1146
                        Slider_TickPlacement = 1147
                        SwapChainPanel_CompositionScaleX = 1148
                        SwapChainPanel_CompositionScaleY = 1149
                        ToolTip_HorizontalOffset = 1150
                        ToolTip_IsOpen = 1151
                        ToolTip_Placement = 1152
                        ToolTip_PlacementTarget = 1153
                        ToolTip_TemplateSettings = 1154
                        ToolTip_VerticalOffset = 1155
                        Button_Flyout = 1156
                        ComboBox_Header = 1157
                        ComboBox_HeaderTemplate = 1158
                        ComboBox_IsDropDownOpen = 1159
                        ComboBox_IsEditable = 1160
                        ComboBox_IsSelectionBoxHighlighted = 1161
                        ComboBox_MaxDropDownHeight = 1162
                        ComboBox_PlaceholderText = 1163
                        ComboBox_SelectionBoxItem = 1164
                        ComboBox_SelectionBoxItemTemplate = 1165
                        ComboBox_TemplateSettings = 1166
                        CommandBar_PrimaryCommands = 1167
                        CommandBar_SecondaryCommands = 1168
                        FlipView_UseTouchAnimationsForAllNavigation = 1169
                        HyperlinkButton_NavigateUri = 1170
                        ListBox_SelectedItems = 1171
                        ListBox_SelectionMode = 1172
                        ListViewBase_CanDragItems = 1173
                        ListViewBase_CanReorderItems = 1174
                        ListViewBase_DataFetchSize = 1175
                        ListViewBase_Footer = 1176
                        ListViewBase_FooterTemplate = 1177
                        ListViewBase_FooterTransitions = 1178
                        ListViewBase_Header = 1179
                        ListViewBase_HeaderTemplate = 1180
                        ListViewBase_HeaderTransitions = 1181
                        ListViewBase_IncrementalLoadingThreshold = 1182
                        ListViewBase_IncrementalLoadingTrigger = 1183
                        ListViewBase_IsActiveView = 1184
                        ListViewBase_IsItemClickEnabled = 1185
                        ListViewBase_IsSwipeEnabled = 1186
                        ListViewBase_IsZoomedInView = 1187
                        ListViewBase_ReorderMode = 1188
                        ListViewBase_SelectedItems = 1189
                        ListViewBase_SelectionMode = 1190
                        ListViewBase_SemanticZoomOwner = 1191
                        ListViewBase_ShowsScrollingPlaceholders = 1192
                        RepeatButton_Delay = 1193
                        RepeatButton_Interval = 1194
                        ScrollViewer_BringIntoViewOnFocusChange = 1195
                        ScrollViewer_ComputedHorizontalScrollBarVisibility = 1196
                        ScrollViewer_ComputedVerticalScrollBarVisibility = 1197
                        ScrollViewer_ExtentHeight = 1198
                        ScrollViewer_ExtentWidth = 1199
                        ScrollViewer_HorizontalOffset = 1200
                        ScrollViewer_HorizontalScrollBarVisibility = 1201
                        ScrollViewer_HorizontalScrollMode = 1202
                        ScrollViewer_HorizontalSnapPointsAlignment = 1203
                        ScrollViewer_HorizontalSnapPointsType = 1204
                        ScrollViewer_IsDeferredScrollingEnabled = 1205
                        ScrollViewer_IsHorizontalRailEnabled = 1206
                        ScrollViewer_IsHorizontalScrollChainingEnabled = 1207
                        ScrollViewer_IsScrollInertiaEnabled = 1208
                        ScrollViewer_IsVerticalRailEnabled = 1209
                        ScrollViewer_IsVerticalScrollChainingEnabled = 1210
                        ScrollViewer_IsZoomChainingEnabled = 1211
                        ScrollViewer_IsZoomInertiaEnabled = 1212
                        ScrollViewer_LeftHeader = 1213
                        ScrollViewer_MaxZoomFactor = 1214
                        ScrollViewer_MinZoomFactor = 1215
                        ScrollViewer_ScrollableHeight = 1216
                        ScrollViewer_ScrollableWidth = 1217
                        ScrollViewer_TopHeader = 1218
                        ScrollViewer_TopLeftHeader = 1219
                        ScrollViewer_VerticalOffset = 1220
                        ScrollViewer_VerticalScrollBarVisibility = 1221
                        ScrollViewer_VerticalScrollMode = 1222
                        ScrollViewer_VerticalSnapPointsAlignment = 1223
                        ScrollViewer_VerticalSnapPointsType = 1224
                        ScrollViewer_ViewportHeight = 1225
                        ScrollViewer_ViewportWidth = 1226
                        ScrollViewer_ZoomFactor = 1227
                        ScrollViewer_ZoomMode = 1228
                        ScrollViewer_ZoomSnapPoints = 1229
                        ScrollViewer_ZoomSnapPointsType = 1230
                        ToggleButton_IsChecked = 1231
                        ToggleButton_IsThreeState = 1232
                        ToggleMenuFlyoutItem_IsChecked = 1233
                        VirtualizingStackPanel_AreScrollSnapPointsRegular = 1234
                        VirtualizingStackPanel_IsVirtualizing = 1236
                        VirtualizingStackPanel_Orientation = 1237
                        VirtualizingStackPanel_VirtualizationMode = 1238
                        WrapGrid_HorizontalChildrenAlignment = 1239
                        WrapGrid_ItemHeight = 1240
                        WrapGrid_ItemWidth = 1241
                        WrapGrid_MaximumRowsOrColumns = 1242
                        WrapGrid_Orientation = 1243
                        WrapGrid_VerticalChildrenAlignment = 1244
                        AppBarButton_Icon = 1245
                        AppBarButton_IsCompact = 1246
                        AppBarButton_Label = 1247
                        AppBarToggleButton_Icon = 1248
                        AppBarToggleButton_IsCompact = 1249
                        AppBarToggleButton_Label = 1250
                        GridViewItem_TemplateSettings = 1251
                        ListViewItem_TemplateSettings = 1252
                        RadioButton_GroupName = 1253
                        Glyphs_ColorFontPaletteIndex = 1267
                        Glyphs_IsColorFontEnabled = 1268
                        CalendarViewTemplateSettings_HasMoreContentAfter = 1274
                        CalendarViewTemplateSettings_HasMoreContentBefore = 1275
                        CalendarViewTemplateSettings_HasMoreViews = 1276
                        CalendarViewTemplateSettings_HeaderText = 1277
                        CalendarViewTemplateSettings_WeekDay1 = 1280
                        CalendarViewTemplateSettings_WeekDay2 = 1281
                        CalendarViewTemplateSettings_WeekDay3 = 1282
                        CalendarViewTemplateSettings_WeekDay4 = 1283
                        CalendarViewTemplateSettings_WeekDay5 = 1284
                        CalendarViewTemplateSettings_WeekDay6 = 1285
                        CalendarViewTemplateSettings_WeekDay7 = 1286
                        CalendarView_CalendarIdentifier = 1291
                        CalendarView_DayOfWeekFormat = 1299
                        CalendarView_DisplayMode = 1302
                        CalendarView_FirstDayOfWeek = 1303
                        CalendarView_IsOutOfScopeEnabled = 1317
                        CalendarView_IsTodayHighlighted = 1318
                        CalendarView_MaxDate = 1320
                        CalendarView_MinDate = 1321
                        CalendarView_NumberOfWeeksInView = 1327
                        CalendarView_SelectedDates = 1333
                        CalendarView_SelectionMode = 1335
                        CalendarView_TemplateSettings = 1336
                        CalendarViewDayItem_Date = 1339
                        CalendarViewDayItem_IsBlackout = 1340
                        MediaTransportControls_IsFastForwardEnabled = 1382
                        MediaTransportControls_IsFastRewindEnabled = 1383
                        MediaTransportControls_IsFullWindowEnabled = 1384
                        MediaTransportControls_IsPlaybackRateEnabled = 1385
                        MediaTransportControls_IsSeekEnabled = 1386
                        MediaTransportControls_IsStopEnabled = 1387
                        MediaTransportControls_IsVolumeEnabled = 1388
                        MediaTransportControls_IsZoomEnabled = 1389
                        ContentPresenter_LineHeight = 1425
                        CalendarViewTemplateSettings_MinViewWidth = 1435
                        ListViewBase_SelectedRanges = 1459
                        SplitViewTemplateSettings_CompactPaneGridLength = 1462
                        SplitViewTemplateSettings_NegativeOpenPaneLength = 1463
                        SplitViewTemplateSettings_NegativeOpenPaneLengthMinusCompactLength = 1464
                        SplitViewTemplateSettings_OpenPaneGridLength = 1465
                        SplitViewTemplateSettings_OpenPaneLengthMinusCompactLength = 1466
                        SplitView_CompactPaneLength = 1467
                        SplitView_Content = 1468
                        SplitView_DisplayMode = 1469
                        SplitView_IsPaneOpen = 1470
                        SplitView_OpenPaneLength = 1471
                        SplitView_Pane = 1472
                        SplitView_PanePlacement = 1473
                        SplitView_TemplateSettings = 1474
                        UIElement_Transform3D = 1475
                        CompositeTransform3D_CenterX = 1476
                        CompositeTransform3D_CenterY = 1478
                        CompositeTransform3D_CenterZ = 1480
                        CompositeTransform3D_RotationX = 1482
                        CompositeTransform3D_RotationY = 1484
                        CompositeTransform3D_RotationZ = 1486
                        CompositeTransform3D_ScaleX = 1488
                        CompositeTransform3D_ScaleY = 1490
                        CompositeTransform3D_ScaleZ = 1492
                        CompositeTransform3D_TranslateX = 1494
                        CompositeTransform3D_TranslateY = 1496
                        CompositeTransform3D_TranslateZ = 1498
                        PerspectiveTransform3D_Depth = 1500
                        PerspectiveTransform3D_OffsetX = 1501
                        PerspectiveTransform3D_OffsetY = 1502
                        RelativePanel_Above = 1508
                        RelativePanel_AlignBottomWith = 1509
                        RelativePanel_AlignLeftWith = 1510
                        RelativePanel_AlignRightWith = 1515
                        RelativePanel_AlignTopWith = 1516
                        RelativePanel_Below = 1517
                        RelativePanel_LeftOf = 1520
                        RelativePanel_RightOf = 1521
                        SplitViewTemplateSettings_OpenPaneLength = 1524
                        PasswordBox_PasswordRevealMode = 1527
                        SplitView_PaneBackground = 1528
                        ItemsStackPanel_AreStickyGroupHeadersEnabled = 1529
                        ItemsWrapGrid_AreStickyGroupHeadersEnabled = 1530
                        MenuFlyoutSubItem_Items = 1531
                        MenuFlyoutSubItem_Text = 1532
                        UIElement_CanDrag = 1534
                        DataTemplate_ExtensionInstance = 1535
                        RelativePanel_AlignHorizontalCenterWith = 1552
                        RelativePanel_AlignVerticalCenterWith = 1553
                        TargetPropertyPath_Path = 1555
                        TargetPropertyPath_Target = 1556
                        VisualState_Setters = 1558
                        VisualState_StateTriggers = 1559
                        AdaptiveTrigger_MinWindowHeight = 1560
                        AdaptiveTrigger_MinWindowWidth = 1561
                        Setter_Target = 1562
                        CalendarView_BlackoutForeground = 1565
                        CalendarView_CalendarItemBackground = 1566
                        CalendarView_CalendarItemBorderBrush = 1567
                        CalendarView_CalendarItemBorderThickness = 1568
                        CalendarView_CalendarItemForeground = 1569
                        CalendarView_CalendarViewDayItemStyle = 1570
                        CalendarView_DayItemFontFamily = 1571
                        CalendarView_DayItemFontSize = 1572
                        CalendarView_DayItemFontStyle = 1573
                        CalendarView_DayItemFontWeight = 1574
                        CalendarView_FirstOfMonthLabelFontFamily = 1575
                        CalendarView_FirstOfMonthLabelFontSize = 1576
                        CalendarView_FirstOfMonthLabelFontStyle = 1577
                        CalendarView_FirstOfMonthLabelFontWeight = 1578
                        CalendarView_FirstOfYearDecadeLabelFontFamily = 1579
                        CalendarView_FirstOfYearDecadeLabelFontSize = 1580
                        CalendarView_FirstOfYearDecadeLabelFontStyle = 1581
                        CalendarView_FirstOfYearDecadeLabelFontWeight = 1582
                        CalendarView_FocusBorderBrush = 1583
                        CalendarView_HorizontalDayItemAlignment = 1584
                        CalendarView_HorizontalFirstOfMonthLabelAlignment = 1585
                        CalendarView_HoverBorderBrush = 1586
                        CalendarView_MonthYearItemFontFamily = 1588
                        CalendarView_MonthYearItemFontSize = 1589
                        CalendarView_MonthYearItemFontStyle = 1590
                        CalendarView_MonthYearItemFontWeight = 1591
                        CalendarView_OutOfScopeBackground = 1592
                        CalendarView_OutOfScopeForeground = 1593
                        CalendarView_PressedBorderBrush = 1594
                        CalendarView_PressedForeground = 1595
                        CalendarView_SelectedBorderBrush = 1596
                        CalendarView_SelectedForeground = 1597
                        CalendarView_SelectedHoverBorderBrush = 1598
                        CalendarView_SelectedPressedBorderBrush = 1599
                        CalendarView_TodayFontWeight = 1600
                        CalendarView_TodayForeground = 1601
                        CalendarView_VerticalDayItemAlignment = 1602
                        CalendarView_VerticalFirstOfMonthLabelAlignment = 1603
                        MediaTransportControls_IsCompact = 1605
                        RelativePanel_AlignBottomWithPanel = 1606
                        RelativePanel_AlignHorizontalCenterWithPanel = 1607
                        RelativePanel_AlignLeftWithPanel = 1608
                        RelativePanel_AlignRightWithPanel = 1609
                        RelativePanel_AlignTopWithPanel = 1610
                        RelativePanel_AlignVerticalCenterWithPanel = 1611
                        ListViewBase_IsMultiSelectCheckBoxEnabled = 1612
                        AutomationProperties_Level = 1614
                        AutomationProperties_PositionInSet = 1615
                        AutomationProperties_SizeOfSet = 1616
                        ListViewItemPresenter_CheckBoxBrush = 1617
                        ListViewItemPresenter_CheckMode = 1618
                        ListViewItemPresenter_PressedBackground = 1620
                        ListViewItemPresenter_SelectedPressedBackground = 1621
                        Control_IsTemplateFocusTarget = 1623
                        Control_UseSystemFocusVisuals = 1624
                        ListViewItemPresenter_FocusSecondaryBorderBrush = 1628
                        ListViewItemPresenter_PointerOverForeground = 1630
                        FontIcon_MirroredWhenRightToLeft = 1631
                        CalendarViewTemplateSettings_CenterX = 1632
                        CalendarViewTemplateSettings_CenterY = 1633
                        CalendarViewTemplateSettings_ClipRect = 1634
                        PasswordBox_TextReadingOrder = 1650
                        RichEditBox_TextReadingOrder = 1651
                        TextBox_TextReadingOrder = 1652
                        WebView_ExecutionMode = 1653
                        WebView_DeferredPermissionRequests = 1655
                        WebView_Settings = 1656
                        RichEditBox_DesiredCandidateWindowAlignment = 1660
                        TextBox_DesiredCandidateWindowAlignment = 1662
                        CalendarDatePicker_CalendarIdentifier = 1663
                        CalendarDatePicker_CalendarViewStyle = 1664
                        CalendarDatePicker_Date = 1665
                        CalendarDatePicker_DateFormat = 1666
                        CalendarDatePicker_DayOfWeekFormat = 1667
                        CalendarDatePicker_DisplayMode = 1668
                        CalendarDatePicker_FirstDayOfWeek = 1669
                        CalendarDatePicker_Header = 1670
                        CalendarDatePicker_HeaderTemplate = 1671
                        CalendarDatePicker_IsCalendarOpen = 1672
                        CalendarDatePicker_IsGroupLabelVisible = 1673
                        CalendarDatePicker_IsOutOfScopeEnabled = 1674
                        CalendarDatePicker_IsTodayHighlighted = 1675
                        CalendarDatePicker_MaxDate = 1676
                        CalendarDatePicker_MinDate = 1677
                        CalendarDatePicker_PlaceholderText = 1678
                        CalendarView_IsGroupLabelVisible = 1679
                        ContentPresenter_Background = 1680
                        ContentPresenter_BorderBrush = 1681
                        ContentPresenter_BorderThickness = 1682
                        ContentPresenter_CornerRadius = 1683
                        ContentPresenter_Padding = 1684
                        Grid_BorderBrush = 1685
                        Grid_BorderThickness = 1686
                        Grid_CornerRadius = 1687
                        Grid_Padding = 1688
                        RelativePanel_BorderBrush = 1689
                        RelativePanel_BorderThickness = 1690
                        RelativePanel_CornerRadius = 1691
                        RelativePanel_Padding = 1692
                        StackPanel_BorderBrush = 1693
                        StackPanel_BorderThickness = 1694
                        StackPanel_CornerRadius = 1695
                        StackPanel_Padding = 1696
                        PasswordBox_InputScope = 1697
                        MediaTransportControlsHelper_DropoutOrder = 1698
                        AutoSuggestBoxQuerySubmittedEventArgs_ChosenSuggestion = 1699
                        AutoSuggestBoxQuerySubmittedEventArgs_QueryText = 1700
                        AutoSuggestBox_QueryIcon = 1701
                        StateTrigger_IsActive = 1702
                        ContentPresenter_HorizontalContentAlignment = 1703
                        ContentPresenter_VerticalContentAlignment = 1704
                        AppBarTemplateSettings_ClipRect = 1705
                        AppBarTemplateSettings_CompactRootMargin = 1706
                        AppBarTemplateSettings_CompactVerticalDelta = 1707
                        AppBarTemplateSettings_HiddenRootMargin = 1708
                        AppBarTemplateSettings_HiddenVerticalDelta = 1709
                        AppBarTemplateSettings_MinimalRootMargin = 1710
                        AppBarTemplateSettings_MinimalVerticalDelta = 1711
                        CommandBarTemplateSettings_ContentHeight = 1712
                        CommandBarTemplateSettings_NegativeOverflowContentHeight = 1713
                        CommandBarTemplateSettings_OverflowContentClipRect = 1714
                        CommandBarTemplateSettings_OverflowContentHeight = 1715
                        CommandBarTemplateSettings_OverflowContentHorizontalOffset = 1716
                        CommandBarTemplateSettings_OverflowContentMaxHeight = 1717
                        CommandBarTemplateSettings_OverflowContentMinWidth = 1718
                        AppBar_TemplateSettings = 1719
                        CommandBar_CommandBarOverflowPresenterStyle = 1720
                        CommandBar_CommandBarTemplateSettings = 1721
                        DrillInThemeAnimation_EntranceTarget = 1722
                        DrillInThemeAnimation_EntranceTargetName = 1723
                        DrillInThemeAnimation_ExitTarget = 1724
                        DrillInThemeAnimation_ExitTargetName = 1725
                        DrillOutThemeAnimation_EntranceTarget = 1726
                        DrillOutThemeAnimation_EntranceTargetName = 1727
                        DrillOutThemeAnimation_ExitTarget = 1728
                        DrillOutThemeAnimation_ExitTargetName = 1729
                        XamlBindingHelper_DataTemplateComponent = 1730
                        AutomationProperties_Annotations = 1732
                        AutomationAnnotation_Element = 1733
                        AutomationAnnotation_Type = 1734
                        AutomationPeerAnnotation_Peer = 1735
                        AutomationPeerAnnotation_Type = 1736
                        Hyperlink_UnderlineStyle = 1741
                        CalendarView_DisabledForeground = 1742
                        CalendarView_TodayBackground = 1743
                        CalendarView_TodayBlackoutBackground = 1744
                        CalendarView_TodaySelectedInnerBorderBrush = 1747
                        Control_IsFocusEngaged = 1749
                        Control_IsFocusEngagementEnabled = 1752
                        RichEditBox_ClipboardCopyFormat = 1754
                        CommandBarTemplateSettings_OverflowContentMaxWidth = 1757
                        ComboBoxTemplateSettings_DropDownContentMinWidth = 1758
                        MenuFlyoutPresenterTemplateSettings_FlyoutContentMinWidth = 1762
                        MenuFlyoutPresenter_TemplateSettings = 1763
                        AutomationProperties_LandmarkType = 1766
                        AutomationProperties_LocalizedLandmarkType = 1767
                        RepositionThemeTransition_IsStaggeringEnabled = 1769
                        ListBox_SingleSelectionFollowsFocus = 1770
                        ListViewBase_SingleSelectionFollowsFocus = 1771
                        BitmapImage_AutoPlay = 1773
                        BitmapImage_IsAnimatedBitmap = 1774
                        BitmapImage_IsPlaying = 1775
                        AutomationProperties_FullDescription = 1776
                        AutomationProperties_IsDataValidForForm = 1777
                        AutomationProperties_IsPeripheral = 1778
                        AutomationProperties_LocalizedControlType = 1779
                        FlyoutBase_AllowFocusOnInteraction = 1780
                        TextElement_AllowFocusOnInteraction = 1781
                        FrameworkElement_AllowFocusOnInteraction = 1782
                        Control_RequiresPointer = 1783
                        UIElement_ContextFlyout = 1785
                        TextElement_AccessKey = 1786
                        UIElement_AccessKeyScopeOwner = 1787
                        UIElement_IsAccessKeyScope = 1788
                        AutomationProperties_DescribedBy = 1790
                        UIElement_AccessKey = 1803
                        Control_XYFocusDown = 1804
                        Control_XYFocusLeft = 1805
                        Control_XYFocusRight = 1806
                        Control_XYFocusUp = 1807
                        Hyperlink_XYFocusDown = 1808
                        Hyperlink_XYFocusLeft = 1809
                        Hyperlink_XYFocusRight = 1810
                        Hyperlink_XYFocusUp = 1811
                        WebView_XYFocusDown = 1812
                        WebView_XYFocusLeft = 1813
                        WebView_XYFocusRight = 1814
                        WebView_XYFocusUp = 1815
                        CommandBarTemplateSettings_EffectiveOverflowButtonVisibility = 1816
                        AppBarSeparator_IsInOverflow = 1817
                        CommandBar_DefaultLabelPosition = 1818
                        CommandBar_IsDynamicOverflowEnabled = 1819
                        CommandBar_OverflowButtonVisibility = 1820
                        AppBarButton_IsInOverflow = 1821
                        AppBarButton_LabelPosition = 1822
                        AppBarToggleButton_IsInOverflow = 1823
                        AppBarToggleButton_LabelPosition = 1824
                        FlyoutBase_LightDismissOverlayMode = 1825
                        Popup_LightDismissOverlayMode = 1827
                        CalendarDatePicker_LightDismissOverlayMode = 1829
                        DatePicker_LightDismissOverlayMode = 1830
                        SplitView_LightDismissOverlayMode = 1831
                        TimePicker_LightDismissOverlayMode = 1832
                        AppBar_LightDismissOverlayMode = 1833
                        AutoSuggestBox_LightDismissOverlayMode = 1834
                        ComboBox_LightDismissOverlayMode = 1835
                        AppBarSeparator_DynamicOverflowOrder = 1836
                        AppBarButton_DynamicOverflowOrder = 1837
                        AppBarToggleButton_DynamicOverflowOrder = 1838
                        FrameworkElement_FocusVisualMargin = 1839
                        FrameworkElement_FocusVisualPrimaryBrush = 1840
                        FrameworkElement_FocusVisualPrimaryThickness = 1841
                        FrameworkElement_FocusVisualSecondaryBrush = 1842
                        FrameworkElement_FocusVisualSecondaryThickness = 1843
                        FlyoutBase_AllowFocusWhenDisabled = 1846
                        FrameworkElement_AllowFocusWhenDisabled = 1847
                        ComboBox_IsTextSearchEnabled = 1848
                        TextElement_ExitDisplayModeOnAccessKeyInvoked = 1849
                        UIElement_ExitDisplayModeOnAccessKeyInvoked = 1850
                        MediaPlayerPresenter_IsFullWindow = 1851
                        MediaPlayerPresenter_MediaPlayer = 1852
                        MediaPlayerPresenter_Stretch = 1853
                        MediaPlayerElement_AreTransportControlsEnabled = 1854
                        MediaPlayerElement_AutoPlay = 1855
                        MediaPlayerElement_IsFullWindow = 1856
                        MediaPlayerElement_MediaPlayer = 1857
                        MediaPlayerElement_PosterSource = 1858
                        MediaPlayerElement_Source = 1859
                        MediaPlayerElement_Stretch = 1860
                        MediaPlayerElement_TransportControls = 1861
                        MediaTransportControls_FastPlayFallbackBehaviour = 1862
                        MediaTransportControls_IsNextTrackButtonVisible = 1863
                        MediaTransportControls_IsPreviousTrackButtonVisible = 1864
                        MediaTransportControls_IsSkipBackwardButtonVisible = 1865
                        MediaTransportControls_IsSkipBackwardEnabled = 1866
                        MediaTransportControls_IsSkipForwardButtonVisible = 1867
                        MediaTransportControls_IsSkipForwardEnabled = 1868
                        FlyoutBase_ElementSoundMode = 1869
                        Control_ElementSoundMode = 1870
                        Hyperlink_ElementSoundMode = 1871
                        AutomationProperties_FlowsFrom = 1876
                        AutomationProperties_FlowsTo = 1877
                        TextElement_TextDecorations = 1879
                        RichTextBlock_TextDecorations = 1881
                        Control_DefaultStyleResourceUri = 1882
                        ContentDialog_PrimaryButtonStyle = 1884
                        ContentDialog_SecondaryButtonStyle = 1885
                        TextElement_KeyTipHorizontalOffset = 1890
                        TextElement_KeyTipPlacementMode = 1891
                        TextElement_KeyTipVerticalOffset = 1892
                        UIElement_KeyTipHorizontalOffset = 1893
                        UIElement_KeyTipPlacementMode = 1894
                        UIElement_KeyTipVerticalOffset = 1895
                        FlyoutBase_OverlayInputPassThroughElement = 1896
                        UIElement_XYFocusKeyboardNavigation = 1897
                        AutomationProperties_Culture = 1898
                        UIElement_XYFocusDownNavigationStrategy = 1918
                        UIElement_XYFocusLeftNavigationStrategy = 1919
                        UIElement_XYFocusRightNavigationStrategy = 1920
                        UIElement_XYFocusUpNavigationStrategy = 1921
                        Hyperlink_XYFocusDownNavigationStrategy = 1922
                        Hyperlink_XYFocusLeftNavigationStrategy = 1923
                        Hyperlink_XYFocusRightNavigationStrategy = 1924
                        Hyperlink_XYFocusUpNavigationStrategy = 1925
                        TextElement_AccessKeyScopeOwner = 1926
                        TextElement_IsAccessKeyScope = 1927
                        Hyperlink_FocusState = 1934
                        ContentDialog_CloseButtonCommand = 1936
                        ContentDialog_CloseButtonCommandParameter = 1937
                        ContentDialog_CloseButtonStyle = 1938
                        ContentDialog_CloseButtonText = 1939
                        ContentDialog_DefaultButton = 1940
                        RichEditBox_SelectionHighlightColorWhenNotFocused = 1941
                        TextBox_SelectionHighlightColorWhenNotFocused = 1942
                        SvgImageSource_RasterizePixelHeight = 1948
                        SvgImageSource_RasterizePixelWidth = 1949
                        SvgImageSource_UriSource = 1950
                        LoadedImageSurface_DecodedPhysicalSize = 1955
                        LoadedImageSurface_DecodedSize = 1956
                        LoadedImageSurface_NaturalSize = 1957
                        ComboBox_SelectionChangedTrigger = 1958
                        XamlCompositionBrushBase_FallbackColor = 1960
                        UIElement_Lights = 1962
                        MenuFlyoutItem_Icon = 1963
                        MenuFlyoutSubItem_Icon = 1964
                        BitmapIcon_ShowAsMonochrome = 1965
                        UIElement_HighContrastAdjustment = 1967
                        RichEditBox_MaxLength = 1968
                        UIElement_TabFocusNavigation = 1969
                        Control_IsTemplateKeyTipTarget = 1970
                        Hyperlink_IsTabStop = 1972
                        Hyperlink_TabIndex = 1973
                        MediaTransportControls_IsRepeatButtonVisible = 1974
                        MediaTransportControls_IsRepeatEnabled = 1975
                        MediaTransportControls_ShowAndHideAutomatically = 1976
                        RichEditBox_DisabledFormattingAccelerators = 1977
                        RichEditBox_CharacterCasing = 1978
                        TextBox_CharacterCasing = 1979
                        RichTextBlock_IsTextTrimmed = 1980
                        RichTextBlockOverflow_IsTextTrimmed = 1981
                        TextBlock_IsTextTrimmed = 1982
                        TextHighlighter_Background = 1985
                        TextHighlighter_Foreground = 1986
                        TextHighlighter_Ranges = 1987
                        RichTextBlock_TextHighlighters = 1988
                        TextBlock_TextHighlighters = 1989
                        FrameworkElement_ActualTheme = 1992
                        Grid_ColumnSpacing = 1993
                        Grid_RowSpacing = 1994
                        StackPanel_Spacing = 1995
                        Block_HorizontalTextAlignment = 1996
                        RichTextBlock_HorizontalTextAlignment = 1997
                        TextBlock_HorizontalTextAlignment = 1998
                        RichEditBox_HorizontalTextAlignment = 1999
                        TextBox_HorizontalTextAlignment = 2000
                        TextBox_PlaceholderForeground = 2001
                        ComboBox_PlaceholderForeground = 2002
                        KeyboardAccelerator_IsEnabled = 2003
                        KeyboardAccelerator_Key = 2004
                        KeyboardAccelerator_Modifiers = 2005
                        KeyboardAccelerator_ScopeOwner = 2006
                        UIElement_KeyboardAccelerators = 2007
                        ListViewItemPresenter_RevealBackground = 2009
                        ListViewItemPresenter_RevealBackgroundShowsAboveContent = 2010
                        ListViewItemPresenter_RevealBorderBrush = 2011
                        ListViewItemPresenter_RevealBorderThickness = 2012
                        UIElement_KeyTipTarget = 2014
                        AppBarButtonTemplateSettings_KeyboardAcceleratorTextMinWidth = 2015
                        AppBarToggleButtonTemplateSettings_KeyboardAcceleratorTextMinWidth = 2016
                        MenuFlyoutItemTemplateSettings_KeyboardAcceleratorTextMinWidth = 2017
                        MenuFlyoutItem_TemplateSettings = 2019
                        AppBarButton_TemplateSettings = 2021
                        AppBarToggleButton_TemplateSettings = 2023
                        UIElement_KeyboardAcceleratorPlacementMode = 2028
                        MediaTransportControls_IsCompactOverlayButtonVisible = 2032
                        MediaTransportControls_IsCompactOverlayEnabled = 2033
                        UIElement_KeyboardAcceleratorPlacementTarget = 2061
                        UIElement_CenterPoint = 2062
                        UIElement_Rotation = 2063
                        UIElement_RotationAxis = 2064
                        UIElement_Scale = 2065
                        UIElement_TransformMatrix = 2066
                        UIElement_Translation = 2067
                        TextBox_HandwritingView = 2068
                        AutomationProperties_HeadingLevel = 2069
                        TextBox_IsHandwritingViewEnabled = 2076
                        RichEditBox_ContentLinkProviders = 2078
                        RichEditBox_ContentLinkBackgroundColor = 2079
                        RichEditBox_ContentLinkForegroundColor = 2080
                        HandwritingView_AreCandidatesEnabled = 2081
                        HandwritingView_IsOpen = 2082
                        HandwritingView_PlacementTarget = 2084
                        HandwritingView_PlacementAlignment = 2085
                        RichEditBox_HandwritingView = 2086
                        RichEditBox_IsHandwritingViewEnabled = 2087
                        MenuFlyoutItem_KeyboardAcceleratorTextOverride = 2090
                        AppBarButton_KeyboardAcceleratorTextOverride = 2091
                        AppBarToggleButton_KeyboardAcceleratorTextOverride = 2092
                        ContentLink_Background = 2093
                        ContentLink_Cursor = 2094
                        ContentLink_ElementSoundMode = 2095
                        ContentLink_FocusState = 2096
                        ContentLink_IsTabStop = 2097
                        ContentLink_TabIndex = 2098
                        ContentLink_XYFocusDown = 2099
                        ContentLink_XYFocusDownNavigationStrategy = 2100
                        ContentLink_XYFocusLeft = 2101
                        ContentLink_XYFocusLeftNavigationStrategy = 2102
                        ContentLink_XYFocusRight = 2103
                        ContentLink_XYFocusRightNavigationStrategy = 2104
                        ContentLink_XYFocusUp = 2105
                        ContentLink_XYFocusUpNavigationStrategy = 2106
                        IconSource_Foreground = 2112
                        BitmapIconSource_ShowAsMonochrome = 2113
                        BitmapIconSource_UriSource = 2114
                        FontIconSource_FontFamily = 2115
                        FontIconSource_FontSize = 2116
                        FontIconSource_FontStyle = 2117
                        FontIconSource_FontWeight = 2118
                        FontIconSource_Glyph = 2119
                        FontIconSource_IsTextScaleFactorEnabled = 2120
                        FontIconSource_MirroredWhenRightToLeft = 2121
                        PathIconSource_Data = 2122
                        SymbolIconSource_Symbol = 2123
                        UIElement_Shadow = 2130
                        IconSourceElement_IconSource = 2131
                        PasswordBox_CanPasteClipboardContent = 2137
                        TextBox_CanPasteClipboardContent = 2138
                        TextBox_CanRedo = 2139
                        TextBox_CanUndo = 2140
                        FlyoutBase_ShowMode = 2141
                        FlyoutBase_Target = 2142
                        Control_CornerRadius = 2143
                        AutomationProperties_IsDialog = 2149
                        AppBarElementContainer_DynamicOverflowOrder = 2150
                        AppBarElementContainer_IsCompact = 2151
                        AppBarElementContainer_IsInOverflow = 2152
                        ScrollContentPresenter_CanContentRenderOutsideBounds = 2157
                        ScrollViewer_CanContentRenderOutsideBounds = 2158
                        RichEditBox_SelectionFlyout = 2159
                        TextBox_SelectionFlyout = 2160
                        Border_BackgroundSizing = 2161
                        ContentPresenter_BackgroundSizing = 2162
                        Control_BackgroundSizing = 2163
                        Grid_BackgroundSizing = 2164
                        RelativePanel_BackgroundSizing = 2165
                        StackPanel_BackgroundSizing = 2166
                        ScrollViewer_HorizontalAnchorRatio = 2170
                        ScrollViewer_VerticalAnchorRatio = 2171
                        ComboBox_Text = 2208
                        TextBox_Description = 2217
                        ToolTip_PlacementRect = 2218
                        RichTextBlock_SelectionFlyout = 2219
                        TextBlock_SelectionFlyout = 2220
                        PasswordBox_SelectionFlyout = 2221
                        Border_BackgroundTransition = 2222
                        ContentPresenter_BackgroundTransition = 2223
                        Panel_BackgroundTransition = 2224
                        ColorPaletteResources_Accent = 2227
                        ColorPaletteResources_AltHigh = 2228
                        ColorPaletteResources_AltLow = 2229
                        ColorPaletteResources_AltMedium = 2230
                        ColorPaletteResources_AltMediumHigh = 2231
                        ColorPaletteResources_AltMediumLow = 2232
                        ColorPaletteResources_BaseHigh = 2233
                        ColorPaletteResources_BaseLow = 2234
                        ColorPaletteResources_BaseMedium = 2235
                        ColorPaletteResources_BaseMediumHigh = 2236
                        ColorPaletteResources_BaseMediumLow = 2237
                        ColorPaletteResources_ChromeAltLow = 2238
                        ColorPaletteResources_ChromeBlackHigh = 2239
                        ColorPaletteResources_ChromeBlackLow = 2240
                        ColorPaletteResources_ChromeBlackMedium = 2241
                        ColorPaletteResources_ChromeBlackMediumLow = 2242
                        ColorPaletteResources_ChromeDisabledHigh = 2243
                        ColorPaletteResources_ChromeDisabledLow = 2244
                        ColorPaletteResources_ChromeGray = 2245
                        ColorPaletteResources_ChromeHigh = 2246
                        ColorPaletteResources_ChromeLow = 2247
                        ColorPaletteResources_ChromeMedium = 2248
                        ColorPaletteResources_ChromeMediumLow = 2249
                        ColorPaletteResources_ChromeWhite = 2250
                        ColorPaletteResources_ErrorText = 2252
                        ColorPaletteResources_ListLow = 2253
                        ColorPaletteResources_ListMedium = 2254
                        UIElement_TranslationTransition = 2255
                        UIElement_OpacityTransition = 2256
                        UIElement_RotationTransition = 2257
                        UIElement_ScaleTransition = 2258
                        BrushTransition_Duration = 2261
                        ScalarTransition_Duration = 2262
                        Vector3Transition_Duration = 2263
                        Vector3Transition_Components = 2266
                        FlyoutBase_IsOpen = 2267
                        StandardUICommand_Kind = 2275
                        UIElement_CanBeScrollAnchor = 2276
                        ThemeShadow_Receivers = 2279
                        ScrollContentPresenter_SizesContentToTemplatedParent = 2280
                        ComboBox_TextBoxStyle = 2281
                        Frame_IsNavigationStackEnabled = 2282
                        RichEditBox_ProofingMenuFlyout = 2283
                        TextBox_ProofingMenuFlyout = 2284
                        ScrollViewer_ReduceViewportForCoreInputViewOcclusions = 2295
                        FlyoutBase_AreOpenCloseAnimationsEnabled = 2296
                        FlyoutBase_InputDevicePrefersPrimaryCommands = 2297
                        CalendarDatePicker_Description = 2300
                        PasswordBox_Description = 2308
                        RichEditBox_Description = 2316
                        AutoSuggestBox_Description = 2331
                        ComboBox_Description = 2339
                        XamlUICommand_AccessKey = 2347
                        XamlUICommand_Command = 2348
                        XamlUICommand_Description = 2349
                        XamlUICommand_IconSource = 2350
                        XamlUICommand_KeyboardAccelerators = 2351
                        XamlUICommand_Label = 2352
                        DatePicker_SelectedDate = 2355
                        TimePicker_SelectedTime = 2356
                        AppBarTemplateSettings_NegativeCompactVerticalDelta = 2367
                        AppBarTemplateSettings_NegativeHiddenVerticalDelta = 2368
                        AppBarTemplateSettings_NegativeMinimalVerticalDelta = 2369
                        FlyoutBase_ShouldConstrainToRootBounds = 2378
                        Popup_ShouldConstrainToRootBounds = 2379
                        FlyoutPresenter_IsDefaultShadowEnabled = 2380
                        MenuFlyoutPresenter_IsDefaultShadowEnabled = 2381
                        UIElement_ActualOffset = 2382
                        UIElement_ActualSize = 2383
                        CommandBarTemplateSettings_OverflowContentCompactYTranslation = 2384
                        CommandBarTemplateSettings_OverflowContentHiddenYTranslation = 2385
                        CommandBarTemplateSettings_OverflowContentMinimalYTranslation = 2386
                        HandwritingView_IsCommandBarOpen = 2395
                        HandwritingView_IsSwitchToKeyboardEnabled = 2396
                        ListViewItemPresenter_SelectionIndicatorVisualEnabled = 2399
                        ListViewItemPresenter_SelectionIndicatorBrush = 2400
                        ListViewItemPresenter_SelectionIndicatorMode = 2401
                        ListViewItemPresenter_SelectionIndicatorPointerOverBrush = 2402
                        ListViewItemPresenter_SelectionIndicatorPressedBrush = 2403
                        ListViewItemPresenter_SelectedBorderBrush = 2410
                        ListViewItemPresenter_SelectedInnerBorderBrush = 2411
                        ListViewItemPresenter_CheckBoxCornerRadius = 2412
                        ListViewItemPresenter_SelectionIndicatorCornerRadius = 2413
                        ListViewItemPresenter_SelectedDisabledBorderBrush = 2414
                        ListViewItemPresenter_SelectedPressedBorderBrush = 2415
                        ListViewItemPresenter_SelectedDisabledBackground = 2416
                        ListViewItemPresenter_PointerOverBorderBrush = 2417
                        ListViewItemPresenter_CheckBoxPointerOverBrush = 2418
                        ListViewItemPresenter_CheckBoxPressedBrush = 2419
                        ListViewItemPresenter_CheckDisabledBrush = 2420
                        ListViewItemPresenter_CheckPressedBrush = 2421
                        ListViewItemPresenter_CheckBoxBorderBrush = 2422
                        ListViewItemPresenter_CheckBoxDisabledBorderBrush = 2423
                        ListViewItemPresenter_CheckBoxPressedBorderBrush = 2424
                        ListViewItemPresenter_CheckBoxDisabledBrush = 2425
                        ListViewItemPresenter_CheckBoxSelectedBrush = 2426
                        ListViewItemPresenter_CheckBoxSelectedDisabledBrush = 2427
                        ListViewItemPresenter_CheckBoxSelectedPointerOverBrush = 2428
                        ListViewItemPresenter_CheckBoxSelectedPressedBrush = 2429
                        ListViewItemPresenter_CheckBoxPointerOverBorderBrush = 2430
                        ListViewItemPresenter_SelectionIndicatorDisabledBrush = 2431
                        CalendarView_BlackoutBackground = 2432
                        CalendarView_BlackoutStrikethroughBrush = 2433
                        CalendarView_CalendarItemCornerRadius = 2434
                        CalendarView_CalendarItemDisabledBackground = 2435
                        CalendarView_CalendarItemHoverBackground = 2436
                        CalendarView_CalendarItemPressedBackground = 2437
                        CalendarView_DayItemMargin = 2438
                        CalendarView_FirstOfMonthLabelMargin = 2439
                        CalendarView_FirstOfYearDecadeLabelMargin = 2440
                        CalendarView_MonthYearItemMargin = 2441
                        CalendarView_OutOfScopeHoverForeground = 2442
                        CalendarView_OutOfScopePressedForeground = 2443
                        CalendarView_SelectedDisabledBorderBrush = 2444
                        CalendarView_SelectedDisabledForeground = 2445
                        CalendarView_SelectedHoverForeground = 2446
                        CalendarView_SelectedPressedForeground = 2447
                        CalendarView_TodayBlackoutForeground = 2448
                        CalendarView_TodayDisabledBackground = 2449
                        CalendarView_TodayHoverBackground = 2450
                        CalendarView_TodayPressedBackground = 2451
                        Popup_ActualPlacement = 2452
                        Popup_DesiredPlacement = 2453
                        Popup_PlacementTarget = 2454
                        AutomationProperties_AutomationControlType = 2455

                    class XamlTypeIndex(_Enum):
                        AutoSuggestBoxSuggestionChosenEventArgs = 34
                        AutoSuggestBoxTextChangedEventArgs = 35
                        CollectionViewSource = 41
                        ColumnDefinition = 44
                        GradientStop = 64
                        InputScope = 74
                        InputScopeName = 75
                        KeySpline = 78
                        PathFigure = 93
                        PrintDocument = 100
                        RowDefinition = 106
                        Style = 114
                        TimelineMarker = 126
                        VisualState = 137
                        VisualStateGroup = 138
                        VisualStateManager = 139
                        VisualTransition = 140
                        AddDeleteThemeTransition = 177
                        ArcSegment = 178
                        BackEase = 179
                        BeginStoryboard = 180
                        BezierSegment = 181
                        BindingBase = 182
                        BitmapCache = 183
                        BounceEase = 186
                        CircleEase = 187
                        ColorAnimation = 188
                        ColorAnimationUsingKeyFrames = 189
                        ContentThemeTransition = 190
                        ControlTemplate = 191
                        CubicEase = 192
                        DataTemplate = 194
                        DiscreteColorKeyFrame = 195
                        DiscreteDoubleKeyFrame = 196
                        DiscreteObjectKeyFrame = 197
                        DiscretePointKeyFrame = 198
                        DoubleAnimation = 200
                        DoubleAnimationUsingKeyFrames = 201
                        EasingColorKeyFrame = 204
                        EasingDoubleKeyFrame = 205
                        EasingPointKeyFrame = 206
                        EdgeUIThemeTransition = 207
                        ElasticEase = 208
                        EllipseGeometry = 209
                        EntranceThemeTransition = 210
                        EventTrigger = 211
                        ExponentialEase = 212
                        Flyout = 213
                        GeometryGroup = 216
                        ItemsPanelTemplate = 227
                        LinearColorKeyFrame = 230
                        LinearDoubleKeyFrame = 231
                        LinearPointKeyFrame = 232
                        LineGeometry = 233
                        LineSegment = 234
                        Matrix3DProjection = 236
                        MenuFlyout = 238
                        ObjectAnimationUsingKeyFrames = 240
                        PaneThemeTransition = 241
                        PathGeometry = 243
                        PlaneProjection = 244
                        PointAnimation = 245
                        PointAnimationUsingKeyFrames = 246
                        PolyBezierSegment = 248
                        PolyLineSegment = 249
                        PolyQuadraticBezierSegment = 250
                        PopupThemeTransition = 251
                        PowerEase = 252
                        QuadraticBezierSegment = 254
                        QuadraticEase = 255
                        QuarticEase = 256
                        QuinticEase = 257
                        RectangleGeometry = 258
                        RelativeSource = 259
                        RenderTargetBitmap = 260
                        ReorderThemeTransition = 261
                        RepositionThemeTransition = 262
                        Setter = 263
                        SineEase = 264
                        SolidColorBrush = 265
                        SplineColorKeyFrame = 266
                        SplineDoubleKeyFrame = 267
                        SplinePointKeyFrame = 268
                        BitmapImage = 285
                        Border = 286
                        CaptureElement = 288
                        CompositeTransform = 295
                        ContentPresenter = 296
                        DragItemThemeAnimation = 302
                        DragOverThemeAnimation = 303
                        DropTargetItemThemeAnimation = 304
                        FadeInThemeAnimation = 306
                        FadeOutThemeAnimation = 307
                        Glyphs = 312
                        Image = 326
                        ImageBrush = 328
                        InlineUIContainer = 329
                        ItemsPresenter = 332
                        LinearGradientBrush = 334
                        LineBreak = 335
                        MatrixTransform = 340
                        MediaElement = 342
                        Paragraph = 349
                        PointerDownThemeAnimation = 357
                        PointerUpThemeAnimation = 359
                        PopInThemeAnimation = 361
                        PopOutThemeAnimation = 362
                        Popup = 363
                        RepositionThemeAnimation = 370
                        ResourceDictionary = 371
                        RichTextBlock = 374
                        RichTextBlockOverflow = 376
                        RotateTransform = 378
                        Run = 380
                        ScaleTransform = 381
                        SkewTransform = 389
                        Span = 390
                        SplitCloseThemeAnimation = 391
                        SplitOpenThemeAnimation = 392
                        Storyboard = 393
                        SwipeBackThemeAnimation = 394
                        SwipeHintThemeAnimation = 395
                        TextBlock = 396
                        TransformGroup = 411
                        TranslateTransform = 413
                        Viewbox = 417
                        WebViewBrush = 423
                        AppBarSeparator = 427
                        BitmapIcon = 429
                        Bold = 430
                        Canvas = 432
                        ContentControl = 435
                        DatePicker = 436
                        DependencyObjectCollection = 437
                        Ellipse = 438
                        FontIcon = 440
                        Grid = 442
                        Hub = 445
                        HubSection = 446
                        Hyperlink = 447
                        Italic = 449
                        ItemsControl = 451
                        Line = 452
                        MediaTransportControls = 458
                        PasswordBox = 462
                        Path = 463
                        PathIcon = 464
                        Polygon = 465
                        Polyline = 466
                        ProgressRing = 468
                        Rectangle = 470
                        RichEditBox = 473
                        ScrollContentPresenter = 476
                        SearchBox = 477
                        SemanticZoom = 479
                        StackPanel = 481
                        SymbolIcon = 482
                        TextBox = 483
                        Thumb = 485
                        TickBar = 486
                        TimePicker = 487
                        ToggleSwitch = 489
                        Underline = 490
                        UserControl = 491
                        VariableSizedWrapGrid = 492
                        WebView = 494
                        AppBar = 495
                        AutoSuggestBox = 499
                        CarouselPanel = 502
                        ContentDialog = 506
                        FlyoutPresenter = 508
                        Frame = 509
                        GridViewItemPresenter = 511
                        GroupItem = 512
                        ItemsStackPanel = 514
                        ItemsWrapGrid = 515
                        ListViewItemPresenter = 520
                        MenuFlyoutItem = 521
                        MenuFlyoutPresenter = 522
                        MenuFlyoutSeparator = 523
                        Page = 525
                        ProgressBar = 528
                        ScrollBar = 530
                        SettingsFlyout = 533
                        Slider = 534
                        SwapChainBackgroundPanel = 535
                        SwapChainPanel = 536
                        ToolTip = 538
                        Button = 540
                        ComboBoxItem = 541
                        CommandBar = 542
                        FlipViewItem = 543
                        GridViewHeaderItem = 545
                        HyperlinkButton = 546
                        ListBoxItem = 547
                        ListViewHeaderItem = 550
                        RepeatButton = 551
                        ScrollViewer = 552
                        ToggleButton = 553
                        ToggleMenuFlyoutItem = 554
                        VirtualizingStackPanel = 555
                        WrapGrid = 556
                        AppBarButton = 557
                        AppBarToggleButton = 558
                        CheckBox = 559
                        GridViewItem = 560
                        ListViewItem = 561
                        RadioButton = 562
                        Binding = 564
                        ComboBox = 566
                        FlipView = 567
                        ListBox = 568
                        GridView = 570
                        ListView = 571
                        CalendarView = 707
                        CalendarViewDayItem = 709
                        CalendarPanel = 723
                        SplitView = 728
                        CompositeTransform3D = 732
                        PerspectiveTransform3D = 733
                        RelativePanel = 744
                        InkCanvas = 748
                        MenuFlyoutSubItem = 749
                        AdaptiveTrigger = 757
                        SoftwareBitmapSource = 761
                        StateTrigger = 767
                        CalendarDatePicker = 774
                        AutoSuggestBoxQuerySubmittedEventArgs = 778
                        CommandBarOverflowPresenter = 781
                        DrillInThemeAnimation = 782
                        DrillOutThemeAnimation = 783
                        AutomationAnnotation = 789
                        AutomationPeerAnnotation = 790
                        MediaPlayerPresenter = 828
                        MediaPlayerElement = 829
                        XamlLight = 855
                        SvgImageSource = 860
                        KeyboardAccelerator = 897
                        HandwritingView = 920
                        ContentLink = 925
                        BitmapIconSource = 929
                        FontIconSource = 930
                        PathIconSource = 931
                        SymbolIconSource = 933
                        IconSourceElement = 939
                        AppBarElementContainer = 945
                        ColorPaletteResources = 952
                        StandardUICommand = 961
                        ThemeShadow = 964
                        XamlUICommand = 969

            class Data:
                class BindingMode(_Enum):
                    OneWay = 1
                    OneTime = 2
                    TwoWay = 3

                class RelativeSourceMode(_Enum):
                    None_ = 0
                    TemplatedParent = 1
                    Self = 2

                class UpdateSourceTrigger(_Enum):
                    Default = 0
                    PropertyChanged = 1
                    Explicit = 2
                    LostFocus = 3

            class Documents:
                class LogicalDirection(_Enum):
                    Backward = 0
                    Forward = 1

                class UnderlineStyle(_Enum):
                    None_ = 0
                    Single = 1

            class Hosting:
                class DesignerAppViewState(_Enum):
                    Visible = 0
                    Hidden = 1

                class XamlSourceFocusNavigationReason(_Enum):
                    Programmatic = 0
                    Restore = 1
                    First = 3
                    Last = 4
                    Left = 7
                    Up = 8
                    Right = 9
                    Down = 10

            class Input:
                class FocusInputDeviceKind(_Enum):
                    None_ = 0
                    Mouse = 1
                    Touch = 2
                    Pen = 3
                    Keyboard = 4
                    GameController = 5

                class FocusNavigationDirection(_Enum):
                    Next = 0
                    Previous = 1
                    Up = 2
                    Down = 3
                    Left = 4
                    Right = 5
                    None_ = 6

                class InputScopeNameValue(_Enum):
                    Default = 0
                    Url = 1
                    EmailSmtpAddress = 5
                    PersonalFullName = 7
                    CurrencyAmountAndSymbol = 20
                    CurrencyAmount = 21
                    DateMonthNumber = 23
                    DateDayNumber = 24
                    DateYear = 25
                    Digits = 28
                    Number = 29
                    Password = 31
                    TelephoneNumber = 32
                    TelephoneCountryCode = 33
                    TelephoneAreaCode = 34
                    TelephoneLocalNumber = 35
                    TimeHour = 37
                    TimeMinutesOrSeconds = 38
                    NumberFullWidth = 39
                    AlphanumericHalfWidth = 40
                    AlphanumericFullWidth = 41
                    Hiragana = 44
                    KatakanaHalfWidth = 45
                    KatakanaFullWidth = 46
                    Hanja = 47
                    HangulHalfWidth = 48
                    HangulFullWidth = 49
                    Search = 50
                    Formula = 51
                    SearchIncremental = 52
                    ChineseHalfWidth = 53
                    ChineseFullWidth = 54
                    NativeScript = 55
                    Text = 57
                    Chat = 58
                    NameOrPhoneNumber = 59
                    EmailNameOrAddress = 60
                    Private = 61
                    Maps = 62
                    NumericPassword = 63
                    NumericPin = 64
                    AlphanumericPin = 65
                    FormulaNumber = 67
                    ChatWithoutEmoji = 68

                class KeyTipPlacementMode(_Enum):
                    Auto = 0
                    Bottom = 1
                    Top = 2
                    Left = 3
                    Right = 4
                    Center = 5
                    Hidden = 6

                class KeyboardAcceleratorPlacementMode(_Enum):
                    Auto = 0
                    Hidden = 1

                class KeyboardNavigationMode(_Enum):
                    Local = 0
                    Cycle = 1
                    Once = 2

                class ManipulationModes(_Enum):
                    None_ = 0x0
                    TranslateX = 0x1
                    TranslateY = 0x2
                    TranslateRailsX = 0x4
                    TranslateRailsY = 0x8
                    Rotate = 0x10
                    Scale = 0x20
                    TranslateInertia = 0x40
                    RotateInertia = 0x80
                    ScaleInertia = 0x100
                    System = 0x10000

                class StandardUICommandKind(_Enum):
                    None_ = 0
                    Cut = 1
                    Copy = 2
                    Paste = 3
                    SelectAll = 4
                    Delete = 5
                    Share = 6
                    Save = 7
                    Open = 8
                    Close = 9
                    Pause = 10
                    Play = 11
                    Stop = 12
                    Forward = 13
                    Backward = 14
                    Undo = 15
                    Redo = 16

                class XYFocusKeyboardNavigationMode(_Enum):
                    Auto = 0
                    Enabled = 1
                    Disabled = 2

                class XYFocusNavigationStrategy(_Enum):
                    Auto = 0
                    Projection = 1
                    NavigationDirectionDistance = 2
                    RectilinearDistance = 3

                class XYFocusNavigationStrategyOverride(_Enum):
                    None_ = 0
                    Auto = 1
                    Projection = 2
                    NavigationDirectionDistance = 3
                    RectilinearDistance = 4

            class Interop:
                class NotifyCollectionChangedAction(_Enum):
                    Add = 0
                    Remove = 1
                    Replace = 2
                    Move = 3
                    Reset = 4

                class TypeKind(_Enum):
                    Primitive = 0
                    Metadata = 1
                    Custom = 2

            class Media:
                class AcrylicBackgroundSource(_Enum):
                    HostBackdrop = 0
                    Backdrop = 1

                class AlignmentX(_Enum):
                    Left = 0
                    Center = 1
                    Right = 2

                class AlignmentY(_Enum):
                    Top = 0
                    Center = 1
                    Bottom = 2

                class AudioCategory(_Enum):
                    Other = 0
                    ForegroundOnlyMedia = 1
                    BackgroundCapableMedia = 2
                    Communications = 3
                    Alerts = 4
                    SoundEffects = 5
                    GameEffects = 6
                    GameMedia = 7
                    GameChat = 8
                    Speech = 9
                    Movie = 10
                    Media = 11

                class AudioDeviceType(_Enum):
                    Console = 0
                    Multimedia = 1
                    Communications = 2

                class BrushMappingMode(_Enum):
                    Absolute = 0
                    RelativeToBoundingBox = 1

                class ColorInterpolationMode(_Enum):
                    ScRgbLinearInterpolation = 0
                    SRgbLinearInterpolation = 1

                class ElementCompositeMode(_Enum):
                    Inherit = 0
                    SourceOver = 1
                    MinBlend = 2

                class FastPlayFallbackBehaviour(_Enum):
                    Skip = 0
                    Hide = 1
                    Disable = 2

                class FillRule(_Enum):
                    EvenOdd = 0
                    Nonzero = 1

                class GradientSpreadMethod(_Enum):
                    Pad = 0
                    Reflect = 1
                    Repeat = 2

                class LoadedImageSourceLoadStatus(_Enum):
                    Success = 0
                    NetworkError = 1
                    InvalidFormat = 2
                    Other = 3

                class MediaCanPlayResponse(_Enum):
                    NotSupported = 0
                    Maybe = 1
                    Probably = 2

                class MediaElementState(_Enum):
                    Closed = 0
                    Opening = 1
                    Buffering = 2
                    Playing = 3
                    Paused = 4
                    Stopped = 5

                class PenLineCap(_Enum):
                    Flat = 0
                    Square = 1
                    Round = 2
                    Triangle = 3

                class PenLineJoin(_Enum):
                    Miter = 0
                    Bevel = 1
                    Round = 2

                class RevealBrushState(_Enum):
                    Normal = 0
                    PointerOver = 1
                    Pressed = 2

                class Stereo3DVideoPackingMode(_Enum):
                    None_ = 0
                    SideBySide = 1
                    TopBottom = 2

                class Stereo3DVideoRenderMode(_Enum):
                    Mono = 0
                    Stereo = 1

                class Stretch(_Enum):
                    None_ = 0
                    Fill = 1
                    Uniform = 2
                    UniformToFill = 3

                class StyleSimulations(_Enum):
                    None_ = 0
                    BoldSimulation = 1
                    ItalicSimulation = 2
                    BoldItalicSimulation = 3

                class SweepDirection(_Enum):
                    Counterclockwise = 0
                    Clockwise = 1

                class Animation:
                    class ClockState(_Enum):
                        Active = 0
                        Filling = 1
                        Stopped = 2

                    class ConnectedAnimationComponent(_Enum):
                        OffsetX = 0
                        OffsetY = 1
                        CrossFade = 2
                        Scale = 3

                    class EasingMode(_Enum):
                        EaseOut = 0
                        EaseIn = 1
                        EaseInOut = 2

                    class FillBehavior(_Enum):
                        HoldEnd = 0
                        Stop = 1

                    class RepeatBehaviorType(_Enum):
                        Count = 0
                        Duration = 1
                        Forever = 2

                    class SlideNavigationTransitionEffect(_Enum):
                        FromBottom = 0
                        FromLeft = 1
                        FromRight = 2

                class Imaging:
                    class BitmapCreateOptions(_Enum):
                        None_ = 0x0
                        IgnoreImageCache = 0x8

                    class DecodePixelType(_Enum):
                        Physical = 0
                        Logical = 1

                    class SvgImageSourceLoadStatus(_Enum):
                        Success = 0
                        NetworkError = 1
                        InvalidFormat = 2
                        Other = 3

            class Navigation:
                class NavigationCacheMode(_Enum):
                    Disabled = 0
                    Required = 1
                    Enabled = 2

                class NavigationMode(_Enum):
                    New = 0
                    Back = 1
                    Forward = 2
                    Refresh = 3

            class Printing:
                class PreviewPageCountType(_Enum):
                    Final = 0
                    Intermediate = 1

    class Web:
        class WebErrorStatus(_Enum):
            Unknown = 0
            CertificateCommonNameIsIncorrect = 1
            CertificateExpired = 2
            CertificateContainsErrors = 3
            CertificateRevoked = 4
            CertificateIsInvalid = 5
            ServerUnreachable = 6
            Timeout = 7
            ErrorHttpInvalidServerResponse = 8
            ConnectionAborted = 9
            ConnectionReset = 10
            Disconnected = 11
            HttpToHttpsOnRedirection = 12
            HttpsToHttpOnRedirection = 13
            CannotConnect = 14
            HostNameNotResolved = 15
            OperationCanceled = 16
            RedirectFailed = 17
            UnexpectedStatusCode = 18
            UnexpectedRedirection = 19
            UnexpectedClientError = 20
            UnexpectedServerError = 21
            InsufficientRangeSupport = 22
            MissingContentLengthSupport = 23
            MultipleChoices = 300
            MovedPermanently = 301
            Found = 302
            SeeOther = 303
            NotModified = 304
            UseProxy = 305
            TemporaryRedirect = 307
            BadRequest = 400
            Unauthorized = 401
            PaymentRequired = 402
            Forbidden = 403
            NotFound = 404
            MethodNotAllowed = 405
            NotAcceptable = 406
            ProxyAuthenticationRequired = 407
            RequestTimeout = 408
            Conflict = 409
            Gone = 410
            LengthRequired = 411
            PreconditionFailed = 412
            RequestEntityTooLarge = 413
            RequestUriTooLong = 414
            UnsupportedMediaType = 415
            RequestedRangeNotSatisfiable = 416
            ExpectationFailed = 417
            InternalServerError = 500
            NotImplemented = 501
            BadGateway = 502
            ServiceUnavailable = 503
            GatewayTimeout = 504
            HttpVersionNotSupported = 505

        class Http:
            class HttpCompletionOption(_Enum):
                ResponseContentRead = 0
                ResponseHeadersRead = 1

            class HttpProgressStage(_Enum):
                None_ = 0
                DetectingProxy = 10
                ResolvingName = 20
                ConnectingToServer = 30
                NegotiatingSsl = 40
                SendingHeaders = 50
                SendingContent = 60
                WaitingForResponse = 70
                ReceivingHeaders = 80
                ReceivingContent = 90

            class HttpResponseMessageSource(_Enum):
                None_ = 0
                Cache = 1
                Network = 2

            class HttpStatusCode(_Enum):
                None_ = 0
                Continue = 100
                SwitchingProtocols = 101
                Processing = 102
                Ok = 200
                Created = 201
                Accepted = 202
                NonAuthoritativeInformation = 203
                NoContent = 204
                ResetContent = 205
                PartialContent = 206
                MultiStatus = 207
                AlreadyReported = 208
                IMUsed = 226
                MultipleChoices = 300
                MovedPermanently = 301
                Found = 302
                SeeOther = 303
                NotModified = 304
                UseProxy = 305
                TemporaryRedirect = 307
                PermanentRedirect = 308
                BadRequest = 400
                Unauthorized = 401
                PaymentRequired = 402
                Forbidden = 403
                NotFound = 404
                MethodNotAllowed = 405
                NotAcceptable = 406
                ProxyAuthenticationRequired = 407
                RequestTimeout = 408
                Conflict = 409
                Gone = 410
                LengthRequired = 411
                PreconditionFailed = 412
                RequestEntityTooLarge = 413
                RequestUriTooLong = 414
                UnsupportedMediaType = 415
                RequestedRangeNotSatisfiable = 416
                ExpectationFailed = 417
                UnprocessableEntity = 422
                Locked = 423
                FailedDependency = 424
                UpgradeRequired = 426
                PreconditionRequired = 428
                TooManyRequests = 429
                RequestHeaderFieldsTooLarge = 431
                InternalServerError = 500
                NotImplemented = 501
                BadGateway = 502
                ServiceUnavailable = 503
                GatewayTimeout = 504
                HttpVersionNotSupported = 505
                VariantAlsoNegotiates = 506
                InsufficientStorage = 507
                LoopDetected = 508
                NotExtended = 510
                NetworkAuthenticationRequired = 511

            class HttpVersion(_Enum):
                None_ = 0
                Http10 = 1
                Http11 = 2
                Http20 = 3

            class Diagnostics:
                class HttpDiagnosticRequestInitiator(_Enum):
                    ParsedElement = 0
                    Script = 1
                    Image = 2
                    Link = 3
                    Style = 4
                    XmlHttpRequest = 5
                    Media = 6
                    HtmlDownload = 7
                    Prefetch = 8
                    Other = 9
                    CrossOriginPreFlight = 10
                    Fetch = 11
                    Beacon = 12

            class Filters:
                class HttpCacheReadBehavior(_Enum):
                    Default = 0
                    MostRecent = 1
                    OnlyFromCache = 2
                    NoCache = 3

                class HttpCacheWriteBehavior(_Enum):
                    Default = 0
                    NoCache = 1

                class HttpCookieUsageBehavior(_Enum):
                    Default = 0
                    NoCookies = 1

        class Syndication:
            class SyndicationErrorStatus(_Enum):
                Unknown = 0
                MissingRequiredElement = 1
                MissingRequiredAttribute = 2
                InvalidXml = 3
                UnexpectedContent = 4
                UnsupportedFormat = 5

            class SyndicationFormat(_Enum):
                Atom10 = 0
                Rss20 = 1
                Rss10 = 2
                Rss092 = 3
                Rss091 = 4
                Atom03 = 5

            class SyndicationTextType(_Enum):
                Text = 0
                Html = 1
                Xhtml = 2

        class UI:
            class WebViewControlPermissionState(_Enum):
                Unknown = 0
                Defer = 1
                Allow = 2
                Deny = 3

            class WebViewControlPermissionType(_Enum):
                Geolocation = 0
                UnlimitedIndexedDBQuota = 1
                Media = 2
                PointerLock = 3
                WebNotifications = 4
                Screen = 5
                ImmersiveView = 6

            class Interop:
                class WebViewControlAcceleratorKeyRoutingStage(_Enum):
                    Tunneling = 0
                    Bubbling = 1

                class WebViewControlMoveFocusReason(_Enum):
                    Programmatic = 0
                    Next = 1
                    Previous = 2

                class WebViewControlProcessCapabilityState(_Enum):
                    Default = 0
                    Disabled = 1
                    Enabled = 2

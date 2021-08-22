from __future__ import annotations  # TODO: remove if >= 3.11

__version__ = '0.0.7'  # TODO: split const, func, struct into files

import contextlib
import ctypes
import dataclasses
import functools
import numbers
import operator
import types
import typing
from typing import Any, Callable, ContextManager, Generator, Generic, Optional, Sequence, TypeVar, Union

_WIN32 = True
_WIN64 = ctypes.sizeof(ctypes.c_void_p) == 8
_WIN32_WINNT = 0x0A00
_WIN32_WINDOWS = 0x0410
_CT = TypeVar('_CT')
_CT_BINARY = '__add__', '__sub__', '__mul__', '__matmul__', '__truediv__', '__floordiv__', \
             '__mod__', '__divmod__', '__pow__', '__lshift__', '__rshift__', '__and__', '__xor__', '__or__', \
             '__radd__', '__rsub__', '__rmul__', '__rmatmul__', '__rtruediv__', '__rfloordiv__', \
             '__rmod__', '__rdivmod__', '__rpow__', '__rlshift__', '__rrshift__', '__rand__', '__rxor__', '__ror__'
_CT_I_BINARY = '__iadd__', '__isub__', '__imul__', '__imatmul__', '__itruediv__', '__ifloordiv__', \
               '__imod__', '__ipow__', '__ilshift__', '__irshift__', '__iand__', '__ixor__', '__ior__',
_CT_UNARY = '__neg__', '__pos__', '__abs__', '__invert__', \
            '__round__', '__trunc__', '__floor__', '__ceil__'
_PY_BINARY = '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__'
_PY_UNARY = '__complex__', '__int__', '__float__', '__index__'

CATCH_ERROR = True


class Const:
    # _WIN32_WINNT version constants
    _WIN32_WINNT_NT4 = 0x0400
    _WIN32_WINNT_WIN2K = 0x0500
    _WIN32_WINNT_WINXP = 0x0501
    _WIN32_WINNT_WS03 = 0x0502
    _WIN32_WINNT_WIN6 = 0x0600
    _WIN32_WINNT_VISTA = 0x0600
    _WIN32_WINNT_WS08 = 0x0600
    _WIN32_WINNT_LONGHORN = 0x0600
    _WIN32_WINNT_WIN7 = 0x0601
    _WIN32_WINNT_WIN8 = 0x0602
    _WIN32_WINNT_WINBLUE = 0x0603
    _WIN32_WINNT_WINTHRESHOLD = 0x0A00
    _WIN32_WINNT_WIN10 = 0x0A00
    # _WIN32_IE_ version constants
    _WIN32_IE_IE20 = 0x0200
    _WIN32_IE_IE30 = 0x0300
    _WIN32_IE_IE302 = 0x0302
    _WIN32_IE_IE40 = 0x0400
    _WIN32_IE_IE401 = 0x0401
    _WIN32_IE_IE50 = 0x0500
    _WIN32_IE_IE501 = 0x0501
    _WIN32_IE_IE55 = 0x0550
    _WIN32_IE_IE60 = 0x0600
    _WIN32_IE_IE60SP1 = 0x0601
    _WIN32_IE_IE60SP2 = 0x0603
    _WIN32_IE_IE70 = 0x0700
    _WIN32_IE_IE80 = 0x0800
    _WIN32_IE_IE90 = 0x0900
    _WIN32_IE_IE100 = 0x0A00
    _WIN32_IE_IE110 = 0x0A00
    # NTDDI version constants
    NTDDI_WIN2K = 0x05000000
    NTDDI_WIN2KSP1 = 0x05000100
    NTDDI_WIN2KSP2 = 0x05000200
    NTDDI_WIN2KSP3 = 0x05000300
    NTDDI_WIN2KSP4 = 0x05000400
    NTDDI_WINXP = 0x05010000
    NTDDI_WINXPSP1 = 0x05010100
    NTDDI_WINXPSP2 = 0x05010200
    NTDDI_WINXPSP3 = 0x05010300
    NTDDI_WINXPSP4 = 0x05010400
    NTDDI_WS03 = 0x05020000
    NTDDI_WS03SP1 = 0x05020100
    NTDDI_WS03SP2 = 0x05020200
    NTDDI_WS03SP3 = 0x05020300
    NTDDI_WS03SP4 = 0x05020400
    NTDDI_WIN6 = 0x06000000
    NTDDI_WIN6SP1 = 0x06000100
    NTDDI_WIN6SP2 = 0x06000200
    NTDDI_WIN6SP3 = 0x06000300
    NTDDI_WIN6SP4 = 0x06000400
    NTDDI_VISTA = NTDDI_WIN6
    NTDDI_VISTASP1 = NTDDI_WIN6SP1
    NTDDI_VISTASP2 = NTDDI_WIN6SP2
    NTDDI_VISTASP3 = NTDDI_WIN6SP3
    NTDDI_VISTASP4 = NTDDI_WIN6SP4
    NTDDI_LONGHORN = NTDDI_VISTA
    NTDDI_WS08 = NTDDI_WIN6SP1
    NTDDI_WS08SP2 = NTDDI_WIN6SP2
    NTDDI_WS08SP3 = NTDDI_WIN6SP3
    NTDDI_WS08SP4 = NTDDI_WIN6SP4
    NTDDI_WIN7 = 0x06010000
    NTDDI_WIN8 = 0x06020000
    NTDDI_WINBLUE = 0x06030000
    NTDDI_WINTHRESHOLD = 0x0A000000
    NTDDI_WIN10 = 0x0A000000
    NTDDI_WIN10_TH2 = 0x0A000001
    NTDDI_WIN10_RS1 = 0x0A000002
    NTDDI_WIN10_RS2 = 0x0A000003
    NTDDI_WIN10_RS3 = 0x0A000004
    NTDDI_WIN10_RS4 = 0x0A000005
    NTDDI_WIN10_RS5 = 0x0A000006
    NTDDI_WIN10_19H1 = 0x0A000007
    NTDDI_WIN10_VB = 0x0A000008
    # version
    WINVER = _WIN32_WINNT
    WDK_NTDDI_VERSION = NTDDI_WIN10_VB
    NTDDI_VERSION = WDK_NTDDI_VERSION
    # Flags for IActiveDesktop::ApplyChanges()
    AD_APPLY_SAVE = 0x00000001
    AD_APPLY_HTMLGEN = 0x00000002
    AD_APPLY_REFRESH = 0x00000004
    AD_APPLY_ALL = AD_APPLY_SAVE | AD_APPLY_HTMLGEN | AD_APPLY_REFRESH
    AD_APPLY_FORCE = 0x00000008
    AD_APPLY_BUFFERED_REFRESH = 0x00000010
    AD_APPLY_DYNAMICREFRESH = 0x00000020
    # Flags for IActiveDesktop::GetWallpaper()
    AD_GETWP_BMP = 0x00000000
    AD_GETWP_IMAGE = 0x00000001
    AD_GETWP_LAST_APPLIED = 0x00000002
    # constants for the biCompression field
    BI_RGB = 0
    BI_RLE8 = 1
    BI_RLE4 = 2
    BI_BITFIELDS = 3
    BI_JPEG = 4
    BI_PNG = 5
    # constants for CreateDIBitmap
    CBM_INIT = 0x04
    # Predefined Clipboard Formats
    CF_TEXT = 1
    CF_BITMAP = 2
    CF_METAFILEPICT = 3
    CF_SYLK = 4
    CF_DIF = 5
    CF_TIFF = 6
    CF_OEMTEXT = 7
    CF_DIB = 8
    CF_PALETTE = 9
    CF_PENDATA = 10
    CF_RIFF = 11
    CF_WAVE = 12
    CF_UNICODETEXT = 13
    CF_ENHMETAFILE = 14
    if WINVER >= 0x0400:
        CF_HDROP = 15
        CF_LOCALE = 16
    if WINVER >= 0x0500:
        CF_DIBV5 = 17
    if WINVER >= 0x0500:
        CF_MAX = 18
    elif WINVER >= 0x0400:
        CF_MAX = 17
    else:
        CF_MAX = 15
    # Color Types
    CTLCOLOR_MSGBOX = 0
    CTLCOLOR_EDIT = 1
    CTLCOLOR_LISTBOX = 2
    CTLCOLOR_BTN = 3
    CTLCOLOR_DLG = 4
    CTLCOLOR_SCROLLBAR = 5
    CTLCOLOR_STATIC = 6
    CTLCOLOR_MAX = 7
    COLOR_SCROLLBAR = 0
    COLOR_BACKGROUND = 1
    COLOR_ACTIVECAPTION = 2
    COLOR_INACTIVECAPTION = 3
    COLOR_MENU = 4
    COLOR_WINDOW = 5
    COLOR_WINDOWFRAME = 6
    COLOR_MENUTEXT = 7
    COLOR_WINDOWTEXT = 8
    COLOR_CAPTIONTEXT = 9
    COLOR_ACTIVEBORDER = 10
    COLOR_INACTIVEBORDER = 11
    COLOR_APPWORKSPACE = 12
    COLOR_HIGHLIGHT = 13
    COLOR_HIGHLIGHTTEXT = 14
    COLOR_BTNFACE = 15
    COLOR_BTNSHADOW = 16
    COLOR_GRAYTEXT = 17
    COLOR_BTNTEXT = 18
    COLOR_INACTIVECAPTIONTEXT = 19
    COLOR_BTNHIGHLIGHT = 20
    if WINVER >= 0x0400:
        COLOR_3DDKSHADOW = 21
        COLOR_3DLIGHT = 22
        COLOR_INFOTEXT = 23
        COLOR_INFOBK = 24
    if WINVER >= 0x0500:
        COLOR_HOTLIGHT = 26
        COLOR_GRADIENTACTIVECAPTION = 27
        COLOR_GRADIENTINACTIVECAPTION = 28
        if WINVER >= 0x0501:
            COLOR_MENUHILIGHT = 29
            COLOR_MENUBAR = 30
    if WINVER >= 0x0400:
        COLOR_DESKTOP = COLOR_BACKGROUND
        COLOR_3DFACE = COLOR_BTNFACE
        COLOR_3DSHADOW = COLOR_BTNSHADOW
        COLOR_3DHIGHLIGHT = COLOR_BTNHIGHLIGHT
        COLOR_3DHILIGHT = COLOR_BTNHIGHLIGHT
        COLOR_BTNHILIGHT = COLOR_BTNHIGHLIGHT
    # SHGetSpecialFolderLocation
    CSIDL_DESKTOP = 0x0000
    CSIDL_INTERNET = 0x0001
    CSIDL_PROGRAMS = 0x0002
    CSIDL_CONTROLS = 0x0003
    CSIDL_PRINTERS = 0x0004
    CSIDL_PERSONAL = 0x0005
    CSIDL_FAVORITES = 0x0006
    CSIDL_STARTUP = 0x0007
    CSIDL_RECENT = 0x0008
    CSIDL_SENDTO = 0x0009
    CSIDL_BITBUCKET = 0x000a
    CSIDL_STARTMENU = 0x000b
    CSIDL_MYDOCUMENTS = CSIDL_PERSONAL
    CSIDL_MYMUSIC = 0x000d
    CSIDL_MYVIDEO = 0x000e
    CSIDL_DESKTOPDIRECTORY = 0x0010
    CSIDL_DRIVES = 0x0011
    CSIDL_NETWORK = 0x0012
    CSIDL_NETHOOD = 0x0013
    CSIDL_FONTS = 0x0014
    CSIDL_TEMPLATES = 0x0015
    CSIDL_COMMON_STARTMENU = 0x0016
    CSIDL_COMMON_PROGRAMS = 0X0017
    CSIDL_COMMON_STARTUP = 0x0018
    CSIDL_COMMON_DESKTOPDIRECTORY = 0x0019
    CSIDL_APPDATA = 0x001a
    CSIDL_PRINTHOOD = 0x001b
    CSIDL_LOCAL_APPDATA = 0x001c
    CSIDL_ALTSTARTUP = 0x001d
    CSIDL_COMMON_ALTSTARTUP = 0x001e
    CSIDL_COMMON_FAVORITES = 0x001f
    CSIDL_INTERNET_CACHE = 0x0020
    CSIDL_COOKIES = 0x0021
    CSIDL_HISTORY = 0x0022
    CSIDL_COMMON_APPDATA = 0x0023
    CSIDL_WINDOWS = 0x0024
    CSIDL_SYSTEM = 0x0025
    CSIDL_PROGRAM_FILES = 0x0026
    CSIDL_MYPICTURES = 0x0027
    CSIDL_PROFILE = 0x0028
    CSIDL_SYSTEMX86 = 0x0029
    CSIDL_PROGRAM_FILESX86 = 0x002a
    CSIDL_PROGRAM_FILES_COMMON = 0x002b
    CSIDL_PROGRAM_FILES_COMMONX86 = 0x002c
    CSIDL_COMMON_TEMPLATES = 0x002d
    CSIDL_COMMON_DOCUMENTS = 0x002e
    CSIDL_COMMON_ADMINTOOLS = 0x002f
    CSIDL_ADMINTOOLS = 0x0030
    CSIDL_CONNECTIONS = 0x0031
    CSIDL_COMMON_MUSIC = 0x0035
    CSIDL_COMMON_PICTURES = 0x0036
    CSIDL_COMMON_VIDEO = 0x0037
    CSIDL_RESOURCES = 0x0038
    CSIDL_RESOURCES_LOCALIZED = 0x0039
    CSIDL_COMMON_OEM_LINKS = 0x003a
    CSIDL_CDBURN_AREA = 0x003b
    CSIDL_COMPUTERSNEARME = 0x003d
    CSIDL_FLAG_CREATE = 0x8000
    CSIDL_FLAG_DONT_VERIFY = 0x4000
    CSIDL_FLAG_DONT_UNEXPAND = 0x2000
    if NTDDI_VERSION >= NTDDI_WINXP:
        CSIDL_FLAG_NO_ALIAS = 0x1000
        CSIDL_FLAG_PER_USER_INIT = 0x0800
    CSIDL_FLAG_MASK = 0xFF00
    # DIB color table identifiers
    DIB_RGB_COLORS = 0
    DIB_PAL_COLORS = 1
    # Global Memory Flags
    GMEM_FIXED = 0x0000
    GMEM_MOVEABLE = 0x0002
    GMEM_NOCOMPACT = 0x0010
    GMEM_NODISCARD = 0x0020
    GMEM_ZEROINIT = 0x0040
    GMEM_MODIFY = 0x0080
    GMEM_DISCARDABLE = 0x0100
    GMEM_NOT_BANKED = 0x1000
    GMEM_SHARE = 0x2000
    GMEM_DDESHARE = 0x2000
    GMEM_NOTIFY = 0x4000
    GMEM_LOWER = GMEM_NOT_BANKED
    GMEM_VALID_FLAGS = 0x7F72
    GMEM_INVALID_HANDLE = 0x8000
    GHND = GMEM_MOVEABLE | GMEM_ZEROINIT
    GPTR = GMEM_FIXED | GMEM_ZEROINIT
    # MENUINFO
    if WINVER >= 0x0500:
        # The menu style
        MNS_NOCHECK = 0x80000000
        MNS_MODELESS = 0x40000000
        MNS_DRAGDROP = 0x20000000
        MNS_AUTODISMISS = 0x10000000
        MNS_NOTIFYBYPOS = 0x08000000
        MNS_CHECKORBMP = 0x04000000
        # Indicates the members to be retrieved or set
        MIM_MAXHEIGHT = 0x00000001
        MIM_BACKGROUND = 0x00000002
        MIM_HELPID = 0x00000004
        MIM_MENUDATA = 0x00000008
        MIM_STYLE = 0x00000010
        MIM_APPLYTOSUBMENUS = 0x80000000
    # Parameter for SystemParametersInfo
    SPI_GETBEEP = 0x0001
    SPI_SETBEEP = 0x0002
    SPI_GETMOUSE = 0x0003
    SPI_SETMOUSE = 0x0004
    SPI_GETBORDER = 0x0005
    SPI_SETBORDER = 0x0006
    SPI_GETKEYBOARDSPEED = 0x000A
    SPI_SETKEYBOARDSPEED = 0x000B
    SPI_LANGDRIVER = 0x000C
    SPI_ICONHORIZONTALSPACING = 0x000D
    SPI_GETSCREENSAVETIMEOUT = 0x000E
    SPI_SETSCREENSAVETIMEOUT = 0x000F
    SPI_GETSCREENSAVEACTIVE = 0x0010
    SPI_SETSCREENSAVEACTIVE = 0x0011
    SPI_GETGRIDGRANULARITY = 0x0012
    SPI_SETGRIDGRANULARITY = 0x0013
    SPI_SETDESKWALLPAPER = 0x0014
    SPI_SETDESKPATTERN = 0x0015
    SPI_GETKEYBOARDDELAY = 0x0016
    SPI_SETKEYBOARDDELAY = 0x0017
    SPI_ICONVERTICALSPACING = 0x0018
    SPI_GETICONTITLEWRAP = 0x0019
    SPI_SETICONTITLEWRAP = 0x001A
    SPI_GETMENUDROPALIGNMENT = 0x001B
    SPI_SETMENUDROPALIGNMENT = 0x001C
    SPI_SETDOUBLECLKWIDTH = 0x001D
    SPI_SETDOUBLECLKHEIGHT = 0x001E
    SPI_GETICONTITLELOGFONT = 0x001F
    SPI_SETDOUBLECLICKTIME = 0x0020
    SPI_SETMOUSEBUTTONSWAP = 0x0021
    SPI_SETICONTITLELOGFONT = 0x0022
    SPI_GETFASTTASKSWITCH = 0x0023
    SPI_SETFASTTASKSWITCH = 0x0024
    if WINVER > 0x0400:
        SPI_SETDRAGFULLWINDOWS = 0x0025
        SPI_GETDRAGFULLWINDOWS = 0x0026
        SPI_GETNONCLIENTMETRICS = 0x0029
        SPI_SETNONCLIENTMETRICS = 0x002A
        SPI_GETMINIMIZEDMETRICS = 0x002B
        SPI_SETMINIMIZEDMETRICS = 0x002C
        SPI_GETICONMETRICS = 0x002D
        SPI_SETICONMETRICS = 0x002E
        SPI_SETWORKAREA = 0x002F
        SPI_GETWORKAREA = 0x0030
        SPI_SETPENWINDOWS = 0x0031
        SPI_GETHIGHCONTRAST = 0x0042
        SPI_SETHIGHCONTRAST = 0x0043
        SPI_GETKEYBOARDPREF = 0x0044
        SPI_SETKEYBOARDPREF = 0x0045
        SPI_GETSCREENREADER = 0x0046
        SPI_SETSCREENREADER = 0x0047
        SPI_GETANIMATION = 0x0048
        SPI_SETANIMATION = 0x0049
        SPI_GETFONTSMOOTHING = 0x004A
        SPI_SETFONTSMOOTHING = 0x004B
        SPI_SETDRAGWIDTH = 0x004C
        SPI_SETDRAGHEIGHT = 0x004D
        SPI_SETHANDHELD = 0x004E
        SPI_GETLOWPOWERTIMEOUT = 0x004F
        SPI_GETPOWEROFFTIMEOUT = 0x0050
        SPI_SETLOWPOWERTIMEOUT = 0x0051
        SPI_SETPOWEROFFTIMEOUT = 0x0052
        SPI_GETLOWPOWERACTIVE = 0x0053
        SPI_GETPOWEROFFACTIVE = 0x0054
        SPI_SETLOWPOWERACTIVE = 0x0055
        SPI_SETPOWEROFFACTIVE = 0x0056
        SPI_SETCURSORS = 0x0057
        SPI_SETICONS = 0x0058
        SPI_GETDEFAULTINPUTLANG = 0x0059
        SPI_SETDEFAULTINPUTLANG = 0x005A
        SPI_SETLANGTOGGLE = 0x005B
        SPI_GETWINDOWSEXTENSION = 0x005C
        SPI_SETMOUSETRAILS = 0x005D
        SPI_GETMOUSETRAILS = 0x005E
        SPI_SETSCREENSAVERRUNNING = 0x0061
        SPI_SCREENSAVERRUNNING = SPI_SETSCREENSAVERRUNNING
    SPI_GETFILTERKEYS = 0x0032
    SPI_SETFILTERKEYS = 0x0033
    SPI_GETTOGGLEKEYS = 0x0034
    SPI_SETTOGGLEKEYS = 0x0035
    SPI_GETMOUSEKEYS = 0x0036
    SPI_SETMOUSEKEYS = 0x0037
    SPI_GETSHOWSOUNDS = 0x0038
    SPI_SETSHOWSOUNDS = 0x0039
    SPI_GETSTICKYKEYS = 0x003A
    SPI_SETSTICKYKEYS = 0x003B
    SPI_GETACCESSTIMEOUT = 0x003C
    SPI_SETACCESSTIMEOUT = 0x003D
    if WINVER >= 0x0400:
        SPI_GETSERIALKEYS = 0x003E
        SPI_SETSERIALKEYS = 0x003F
    SPI_GETSOUNDSENTRY = 0x0040
    SPI_SETSOUNDSENTRY = 0x0041
    if _WIN32_WINNT >= 0x0400:
        SPI_GETSNAPTODEFBUTTON = 0x005F1
        SPI_SETSNAPTODEFBUTTON = 0x0060
    if _WIN32_WINNT >= 0x0400 or _WIN32_WINDOWS > 0x0400:
        SPI_GETMOUSEHOVERWIDTH = 0x0062
        SPI_SETMOUSEHOVERWIDTH = 0x0063
        SPI_GETMOUSEHOVERHEIGHT = 0x0064
        SPI_SETMOUSEHOVERHEIGHT = 0x0065
        SPI_GETMOUSEHOVERTIME = 0x0066
        SPI_SETMOUSEHOVERTIME = 0x0067
        SPI_GETWHEELSCROLLLINES = 0x0068
        SPI_SETWHEELSCROLLLINES = 0x0069
        SPI_GETMENUSHOWDELAY = 0x006A
        SPI_SETMENUSHOWDELAY = 0x006B
        if _WIN32_WINNT >= 0x0600:
            SPI_GETWHEELSCROLLCHARS = 0x006C
            SPI_SETWHEELSCROLLCHARS = 0x006D
        SPI_GETSHOWIMEUI = 0x006E
        SPI_SETSHOWIMEUI = 0x006F
    if WINVER >= 0x0500:
        SPI_GETMOUSESPEED = 0x0070
        SPI_SETMOUSESPEED = 0x0071
        SPI_GETSCREENSAVERRUNNING = 0x0072
        SPI_GETDESKWALLPAPER = 0x0073
    if WINVER >= 0x0600:
        SPI_GETAUDIODESCRIPTION = 0x0074
        SPI_SETAUDIODESCRIPTION = 0x0075
        SPI_GETSCREENSAVESECURE = 0x0076
        SPI_SETSCREENSAVESECURE = 0x0077
    if _WIN32_WINNT >= 0x0601:
        SPI_GETHUNGAPPTIMEOUT = 0x0078
        SPI_SETHUNGAPPTIMEOUT = 0x0079
        SPI_GETWAITTOKILLTIMEOUT = 0x007A
        SPI_SETWAITTOKILLTIMEOUT = 0x007B
        SPI_GETWAITTOKILLSERVICETIMEOUT = 0x007C
        SPI_SETWAITTOKILLSERVICETIMEOUT = 0x007D
        SPI_GETMOUSEDOCKTHRESHOLD = 0x007E
        SPI_SETMOUSEDOCKTHRESHOLD = 0x007F
        SPI_GETPENDOCKTHRESHOLD = 0x0080
        SPI_SETPENDOCKTHRESHOLD = 0x0081
        SPI_GETWINARRANGING = 0x0082
        SPI_SETWINARRANGING = 0x0083
        SPI_GETMOUSEDRAGOUTTHRESHOLD = 0x0084
        SPI_SETMOUSEDRAGOUTTHRESHOLD = 0x0085
        SPI_GETPENDRAGOUTTHRESHOLD = 0x0086
        SPI_SETPENDRAGOUTTHRESHOLD = 0x0087
        SPI_GETMOUSESIDEMOVETHRESHOLD = 0x0088
        SPI_SETMOUSESIDEMOVETHRESHOLD = 0x0089
        SPI_GETPENSIDEMOVETHRESHOLD = 0x008A
        SPI_SETPENSIDEMOVETHRESHOLD = 0x008B
        SPI_GETDRAGFROMMAXIMIZE = 0x008C
        SPI_SETDRAGFROMMAXIMIZE = 0x008D
        SPI_GETSNAPSIZING = 0x008E
        SPI_SETSNAPSIZING = 0x008F
        SPI_GETDOCKMOVING = 0x0090
        SPI_SETDOCKMOVING = 0x0091
    if WINVER >= 0x0602:
        MAX_TOUCH_PREDICTION_FILTER_TAPS = 3
    # Flags for SystemParametersInfo
    SPIF_UPDATEINIFILE = 0x0001
    SPIF_SENDWININICHANGE = 0x0002
    SPIF_SENDCHANGE = SPIF_SENDWININICHANGE
    # Stock Logical Objects
    WHITE_BRUSH = 0
    LTGRAY_BRUSH = 1
    GRAY_BRUSH = 2
    DKGRAY_BRUSH = 3
    BLACK_BRUSH = 4
    NULL_BRUSH = 5
    HOLLOW_BRUSH = NULL_BRUSH
    WHITE_PEN = 6
    BLACK_PEN = 7
    NULL_PEN = 8
    OEM_FIXED_FONT = 10
    ANSI_FIXED_FONT = 11
    ANSI_VAR_FONT = 12
    SYSTEM_FONT = 13
    DEVICE_DEFAULT_FONT = 14
    DEFAULT_PALETTE = 15
    SYSTEM_FIXED_FONT = 16
    if WINVER >= 0x0400:
        DEFAULT_GUI_FONT = 17
    if _WIN32_WINNT >= _WIN32_WINNT_WIN2K:
        DC_BRUSH = 18
        DC_PEN = 19
    if _WIN32_WINNT >= _WIN32_WINNT_WIN2K:
        STOCK_LAST = 19
    elif WINVER >= 0x0400:
        STOCK_LAST = 17
    else:
        STOCK_LAST = 16
    # GetPixel
    CLR_INVALID = 0xFFFFFFFF
    # CLSCTX
    CLSCTX_INPROC_SERVER = 0x1
    CLSCTX_INPROC_HANDLER = 0x2
    CLSCTX_LOCAL_SERVER = 0x4
    CLSCTX_INPROC_SERVER16 = 0x8
    CLSCTX_REMOTE_SERVER = 0x10
    CLSCTX_INPROC_HANDLER16 = 0x20
    CLSCTX_RESERVED1 = 0x40
    CLSCTX_RESERVED2 = 0x80
    CLSCTX_RESERVED3 = 0x100
    CLSCTX_RESERVED4 = 0x200
    CLSCTX_NO_CODE_DOWNLOAD = 0x400
    CLSCTX_RESERVED5 = 0x800
    CLSCTX_NO_CUSTOM_MARSHAL = 0x1000
    CLSCTX_ENABLE_CODE_DOWNLOAD = 0x2000
    CLSCTX_NO_FAILURE_LOG = 0x4000
    CLSCTX_DISABLE_AAA = 0x8000
    CLSCTX_ENABLE_AAA = 0x10000
    CLSCTX_FROM_DEFAULT_CONTEXT = 0x20000
    CLSCTX_ACTIVATE_X86_SERVER = 0x40000
    CLSCTX_ACTIVATE_32_BIT_SERVER = CLSCTX_ACTIVATE_X86_SERVER
    CLSCTX_ACTIVATE_64_BIT_SERVER = 0x80000
    CLSCTX_ENABLE_CLOAKING = 0x100000
    CLSCTX_APPCONTAINER = 0x400000
    CLSCTX_ACTIVATE_AAA_AS_IU = 0x800000
    CLSCTX_RESERVED6 = 0x1000000
    CLSCTX_ACTIVATE_ARM32_SERVER = 0x2000000
    CLSCTX_PS_DLL = 0x80000000
    CLSCTX_INPROC = CLSCTX_INPROC_SERVER | CLSCTX_INPROC_HANDLER
    if _WIN32_WINNT >= 0x0400:
        CLSCTX_ALL = CLSCTX_INPROC_SERVER | CLSCTX_INPROC_HANDLER | CLSCTX_LOCAL_SERVER | CLSCTX_REMOTE_SERVER
        CLSCTX_SERVER = CLSCTX_INPROC_SERVER | CLSCTX_LOCAL_SERVER | CLSCTX_REMOTE_SERVER
    else:
        CLSCTX_ALL = CLSCTX_INPROC_SERVER | CLSCTX_INPROC_HANDLER | CLSCTX_LOCAL_SERVER
        CLSCTX_SERVER = CLSCTX_INPROC_SERVER | CLSCTX_LOCAL_SERVER
    # DESKTOP_SLIDESHOW_DIRECTION
    DSD_FORWARD = 0
    DSD_BACKWARD = 1
    # DESKTOP_SLIDESHOW_OPTIONS
    DSO_SHUFFLEIMAGES = 0x1
    # DESKTOP_SLIDESHOW_STATE
    DSS_ENABLED = 0x1
    DSS_SLIDESHOW = 0x2
    DSS_DISABLED_BY_REMOTE_SESSION = 0x4
    # DESKTOP_WALLPAPER_POSITION
    DWPOS_CENTER = 0
    DWPOS_TILE = 1
    DWPOS_STRETCH = 2
    DWPOS_FIT = 3
    DWPOS_FILL = 4
    DWPOS_SPAN = 5
    # SHGFP_TYPE
    SHGFP_TYPE_CURRENT = 0
    SHGFP_TYPE_DEFAULT = 1
    # CLSID
    CLSID_ActiveDesktop = '{75048700-EF1F-11D0-9888-006097DEACF9}'
    CLSID_DesktopWallpaper = '{C2CF3110-460E-4FC1-B9D0-8A1C0C9CC4BD}'
    CLSID_FileOpenDialog = '{DC1C5A9C-E88A-4DDE-A5A1-60F82A20AEF7}'
    # IID
    IID_IUnknown = '{00000000-0000-0000-C000-000000000046}'
    IID_IActiveDesktop = '{F490EB00-1240-11D1-9888-006097DEACF9}'
    IID_IDesktopWallpaper = '{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}'
    IID_IModalWindow = '{B4DB1657-70D7-485E-8E3E-6FCB5A5C1802}'
    IID_IFileDialog = '{42F85136-DB7E-439C-85F1-E4075D135FC8}'
    IID_IFileOpenDialog = '{D57C7288-D4AD-4768-BE02-9D969532D960}'


class Pointer(Generic[_CT]):
    contents: _CT
    value: _CT

    # noinspection PyUnusedLocal,PyTypeChecker
    def __init__(self, type_: type[_CT]) -> type[Pointer[_CT]]:
        pass


# noinspection PyAbstractClass
class Array(Pointer, Sequence[_CT]):
    pass


class Type:
    HRESULT = Union[ctypes.HRESULT, int]
    c_bool = Union[ctypes.c_bool, bool]
    c_byte = Union[ctypes.c_byte, int]
    c_char = Union[ctypes.c_char, str]
    c_char_p = Optional[Union[ctypes.c_char_p, str]]
    c_double = Union[ctypes.c_double, float]
    c_float = Union[ctypes.c_float, float]
    c_int = Union[ctypes.c_int, int]
    c_int16 = Union[ctypes.c_int16, int]
    c_int32 = Union[ctypes.c_int32, int]
    c_int64 = Union[ctypes.c_int64, int]
    c_int8 = Union[ctypes.c_int8, int]
    c_long = Union[ctypes.c_long, int]
    c_longdouble = Union[ctypes.c_longdouble, float]
    c_short = Union[ctypes.c_short, int]
    c_size_t = Union[ctypes.c_size_t, int]
    c_ssize_t = Union[ctypes.c_ssize_t, int]
    c_ubyte = Union[ctypes.c_ubyte, int]
    c_uint = Union[ctypes.c_uint, int]
    c_uint16 = Union[ctypes.c_uint16, int]
    c_uint32 = Union[ctypes.c_uint32, int]
    c_uint64 = Union[ctypes.c_uint64, int]
    c_uint8 = Union[ctypes.c_uint8, int]
    c_ulong = Union[ctypes.c_ulong, int]
    c_ushort = Union[ctypes.c_ushort, int]
    c_void_p = Optional[Union[ctypes.c_void_p, Pointer]]
    c_wchar = Union[ctypes.c_wchar, str]
    c_wchar_p = Optional[Union[ctypes.c_wchar_p, str]]

    c_uchar = c_ubyte
    c_wchar_t = c_wchar

    BOOL = c_int
    BYTE = c_uchar
    CHAR = c_char
    DOUBLE = c_double
    DWORD = c_ulong
    FLOAT = c_float
    INT = c_int
    INT16 = c_short
    INT32 = c_int
    INT64 = c_int32
    INT8 = c_char
    LONG = c_long
    UCHAR = c_uchar
    UINT = c_uint
    UINT16 = c_ushort
    UINT32 = c_uint
    UINT64 = c_uint64
    UINT8 = c_uchar
    ULONG = c_ulong
    USHORT = c_ushort
    WCHAR = c_wchar_t
    WORD = c_ushort

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
    PCNZCH = c_char_p
    PCSTR = c_char_p
    PCWCH = c_wchar_p
    PCWSTR = c_wchar_p
    PCZZSTR = c_char_p
    PNZCH = c_char_p
    PSTR = c_char_p
    PVOID = c_void_p
    PWCH = c_wchar_p
    PWCHAR = c_wchar_p
    PWSTR = c_wchar_p
    PZZSTR = c_char_p
    VOID = c_void_p

    DebugEventProc = c_void_p  # DebugEventProc
    GpBitmap = c_void_p  # GpBitmap
    GpImage = c_void_p  # GpImage
    IUnknown = c_void_p  # IUnknown

    enum = c_uint  # TODO: Enum type
    DESKTOP_SLIDESHOW_DIRECTION = enum
    DESKTOP_SLIDESHOW_OPTIONS = enum
    DESKTOP_SLIDESHOW_STATE = enum
    DESKTOP_WALLPAPER_POSITION = enum

    HALF_PTR = c_int if _WIN64 else c_short
    INT_PTR = c_int64 if _WIN64 else c_int
    LONG_PTR = c_int64 if _WIN64 else c_long
    UHALF_PTR = c_uint if _WIN64 else c_ushort
    UINT_PTR = c_uint64 if _WIN64 else c_uint
    ULONG_PTR = c_uint64 if _WIN64 else c_ulong

    ARGB = DWORD
    ATOM = WORD
    BOOLEAN = BYTE
    COLORREF = DWORD
    DWORD_PTR = ULONG_PTR
    HANDLE = PVOID
    SIZE_T = ULONG_PTR
    Status = HRESULT
    WPARAM = UINT_PTR

    OLECHAR = WCHAR if _WIN32 else c_char
    LPOLESTR = Pointer[OLECHAR] if _WIN32 else LPSTR

    GpStatus = Status
    HACCEL = HANDLE
    HBITMAP = HANDLE
    HBRUSH = HANDLE
    HCOLORSPACE = HANDLE
    HDC = HANDLE
    HDESK = HANDLE
    HDWP = HANDLE
    HENHMETAFILE = HANDLE
    HFONT = HANDLE
    HGDIOBJ = HANDLE
    HGLOBAL = HANDLE
    HHOOK = HANDLE
    HICON = HANDLE
    HINSTANCE = HANDLE
    HKEY = HANDLE
    HKL = HANDLE
    HLOCAL = HANDLE
    HMENU = HANDLE
    HMETAFILE = HANDLE
    HMODULE = HANDLE
    HMONITOR = HANDLE
    HPALETTE = HANDLE
    HPEN = HANDLE
    HRGN = HANDLE
    HRSRC = HANDLE
    HSTR = HANDLE
    HTASK = HANDLE
    HUMPD = HANDLE
    HWINSTA = HANDLE
    HWND = HANDLE
    LPCOLESTR = LPOLESTR
    SC_HANDLE = HANDLE
    SERVICE_STATUS_HANDLE = HANDLE

    HCURSOR = HICON


class Struct:
    @dataclasses.dataclass
    class GdiplusStartupInput:
        GdiplusVersion: Type.UINT32 = 1
        DebugEventCallback: Type.DebugEventProc = None
        SuppressBackgroundThread: Type.BOOL = False
        SuppressExternalCodecs: Type.BOOL = False

    @dataclasses.dataclass
    class RGBQUAD:
        rgbBlue: Type.BYTE = None
        rgbGreen: Type.BYTE = None
        rgbRed: Type.BYTE = None
        rgbReserved: Type.BYTE = 0

    @dataclasses.dataclass
    class BITMAPINFOHEADER:
        biSize: Type.DWORD = None
        biWidth: Type.LONG = None
        biHeight: Type.LONG = None
        biPlanes: Type.WORD = 1
        biBitCount: Type.WORD = None
        biCompression: Type.DWORD = None
        biSizeImage: Type.DWORD = None
        biXPelsPerMeter: Type.LONG = None
        biYPelsPerMeter: Type.LONG = None
        biClrUsed: Type.DWORD = None
        biClrImportant: Type.DWORD = None

    @dataclasses.dataclass
    class BITMAPINFO:
        bmiHeader: Struct.BITMAPINFOHEADER = None
        # noinspection PyTypeChecker
        bmiColors: Struct.RGBQUAD * 1 = None

    @dataclasses.dataclass
    class BITMAP:
        bmType: Type.LONG = None
        bmWidth: Type.LONG = None
        bmHeight: Type.LONG = None
        bmWidthBytes: Type.LONG = None
        bmPlanes: Type.WORD = None
        bmBitsPixel: Type.WORD = None
        bmBits: Type.LPVOID = None

    @dataclasses.dataclass
    class DIBSECTION:
        dsBm: Struct.BITMAP = None
        dsBmih: Struct.BITMAPINFOHEADER = None
        dsBitfields: Type.DWORD * 3 = None
        dshSection: Type.HANDLE = None
        dsOffset: Type.DWORD = None

    @dataclasses.dataclass
    class GUID:
        Data1: Type.c_ulong = None
        Data2: Type.c_ushort = None
        Data3: Type.c_ushort = None
        Data4: Type.c_uchar * 8 = None

    @dataclasses.dataclass
    class WALLPAPEROPT:
        dwSize: Type.DWORD = None
        dwStyle: Type.DWORD = None

    class UUID(GUID):
        pass

    class IID(GUID):
        pass

    class CLSID(GUID):
        pass

    @dataclasses.dataclass
    class RECT:
        left: Type.LONG = None
        top: Type.LONG = None
        right: Type.LONG = None
        bottom: Type.LONG = None

    @dataclasses.dataclass
    class MENUINFO:
        cbSize: Type.DWORD = None
        fMask: Type.DWORD = None
        dwStyle: Type.DWORD = None
        cyMax: Type.UINT = 0
        hbrBack: Type.HBRUSH = None
        dwContextHelpID: Type.DWORD = None
        dwMenuData: Type.ULONG_PTR = None


class COM:
    class IUnknown:
        _CLSID = ''
        QueryInterface: Callable[[Pointer[Struct.IID], Type.c_void_p], Type.HRESULT]
        AddRef: Callable[[], Type.ULONG]
        Release: Callable[[], Type.ULONG]

    class IActiveDesktop(IUnknown):
        _CLSID = Const.CLSID_ActiveDesktop
        ApplyChanges: Callable[[Type.DWORD], Type.HRESULT]
        GetWallpaper: Callable[[Type.PWSTR, Type.UINT, Type.DWORD], Type.HRESULT]
        SetWallpaper: Callable[[Type.PCWSTR, Type.DWORD], Type.HRESULT]
        GetWallpaperOptions: Callable[[Pointer[Struct.WALLPAPEROPT], Type.DWORD], Type.HRESULT]
        SetWallpaperOptions: Callable[[Pointer[Struct.WALLPAPEROPT], Type.DWORD], Type.HRESULT]
        GetPattern: Callable[[Type.PWSTR, Type.UINT, Type.DWORD], Type.HRESULT]
        SetPattern: Callable[[Type.PCWSTR, Type.DWORD], Type.HRESULT]
        GetDesktopItemOptions: Callable
        SetDesktopItemOptions: Callable
        AddDesktopItem: Callable
        AddDesktopItemWithUI: Callable
        ModifyDesktopItem: Callable
        RemoveDesktopItem: Callable
        GetDesktopItemCount: Callable[[Pointer[Type.c_int], Type.DWORD], Type.HRESULT]
        GetDesktopItem: Callable
        GetDesktopItemByID: Callable
        GenerateDesktopItemHtml: Callable
        AddUrl: Callable
        GetDesktopItemBySource: Callable

    class IDesktopWallpaper(IUnknown):
        _CLSID = Const.CLSID_DesktopWallpaper
        SetWallpaper: Callable[[Type.LPCWSTR, Type.LPCWSTR], Type.HRESULT]
        GetWallpaper: Callable[[Type.LPCWSTR, Pointer[Type.LPWSTR]], Type.HRESULT]
        GetMonitorDevicePathAt: Callable[[Type.UINT, Pointer[Type.LPWSTR]], Type.HRESULT]
        GetMonitorDevicePathCount: Callable[[Pointer[Type.UINT]], Type.HRESULT]
        GetMonitorRECT: Callable[[Type.LPCWSTR, Pointer[Struct.RECT]], Type.HRESULT]
        SetBackgroundColor: Callable[[Type.COLORREF], Type.HRESULT]
        GetBackgroundColor: Callable[[Pointer[Type.COLORREF]], Type.HRESULT]
        SetPosition: Callable[[Type.DESKTOP_WALLPAPER_POSITION], Type.HRESULT]
        GetPosition: Callable[[Pointer[Type.DESKTOP_WALLPAPER_POSITION]], Type.HRESULT]
        SetSlideshow: Callable
        GetSlideshow: Callable
        SetSlideshowOptions: Callable[[Type.DESKTOP_SLIDESHOW_OPTIONS, Type.UINT], Type.HRESULT]
        GetSlideshowOptions: Callable[[Type.DESKTOP_SLIDESHOW_OPTIONS, Pointer[Type.UINT]], Type.HRESULT]
        AdvanceSlideshow: Callable[[Type.LPCWSTR, Type.DESKTOP_SLIDESHOW_DIRECTION], Type.HRESULT]
        GetStatus: Callable[[Pointer[Type.DESKTOP_SLIDESHOW_STATE]], Type.HRESULT]
        Enable: Callable[[Type.BOOL], Type.HRESULT]

    class IModalWindow(IUnknown):
        _CLSID = Const.CLSID_FileOpenDialog
        Show: Callable[[Type.HWND], Type.HRESULT]

    class IFileDialog(IModalWindow):
        SetFileTypes: Callable
        SetFileTypeIndex: Callable[[Type.UINT], Type.HRESULT]
        GetFileTypeIndex: Callable[[Type.UINT], Type.HRESULT]
        Advise: Callable
        Unadvise: Callable
        SetOptions: Callable
        GetOptions: Callable
        SetDefaultFolder: Callable
        SetFolder: Callable
        GetFolder: Callable
        GetCurrentSelection: Callable
        SetFileName: Callable[[Type.LPCWSTR], Type.HRESULT]
        GetFileName: Callable[[Type.LPWSTR], Type.HRESULT]
        SetTitle: Callable[[Type.LPCWSTR], Type.HRESULT]
        SetOkButtonLabel: Callable[[Type.LPCWSTR], Type.HRESULT]
        SetFileNameLabel: Callable[[Type.LPCWSTR], Type.HRESULT]
        GetResult: Callable
        AddPlace: Callable
        SetDefaultExtension: Callable[[Type.LPCWSTR], Type.HRESULT]
        Close: Callable[[Type.HRESULT], Type.HRESULT]
        SetClientGuid: Callable[[Pointer[Struct.GUID]], Type.HRESULT]
        ClearClientData: Callable[[], Type.HRESULT]
        SetFilter: Callable

    class IFileOpenDialog(IFileDialog):
        GetResults: Callable
        GetSelectedItems: Callable


class Macro:
    # noinspection PyPep8Naming
    @staticmethod
    def MAKEWORD(a: Type.BYTE,
                 b: Type.BYTE) -> Type.WORD:
        dwa = cast(a, Type.DWORD_PTR).contents
        dwa &= 0xff
        dwb = cast(b, Type.DWORD_PTR).contents
        dwb &= 0xff
        wb = cast(cast(dwb, Type.BYTE), Type.WORD).contents
        wb <<= 8
        return cast(cast(dwa, Type.BYTE), Type.WORD).contents | wb

    # noinspection PyPep8Naming
    @staticmethod
    def MAKELONG(a: Type.WORD,
                 b: Type.WORD) -> Type.DWORD:
        dwa = cast(a, Type.DWORD_PTR).contents
        dwa &= 0xffff
        dwb = cast(b, Type.DWORD_PTR).contents
        dwb &= 0xffff
        wb = cast(cast(dwb, Type.WORD), Type.DWORD).contents
        wb <<= 16
        return cast(cast(dwa, Type.WORD), Type.LONG).contents | wb

    # noinspection PyPep8Naming
    @staticmethod
    def LOWORD(l_: Type.DWORD) -> Type.WORD:
        dword = cast(l_, Type.DWORD_PTR).contents
        dword &= 0xffff
        return cast(dword, Type.WORD).contents

    # noinspection PyPep8Naming
    @staticmethod
    def HIWORD(l_: Type.DWORD) -> Type.WORD:
        dword = cast(l_, Type.DWORD_PTR).contents
        dword >>= 16
        dword &= 0xffff
        return cast(dword, Type.WORD).contents

    # noinspection PyPep8Naming
    @staticmethod
    def LOBYTE(w: Type.WORD) -> Type.BYTE:
        dword = cast(w, Type.DWORD_PTR).contents
        dword &= 0xff
        return cast(dword, Type.BYTE).contents

    # noinspection PyPep8Naming
    @staticmethod
    def HIBYTE(w: Type.WORD) -> Type.BYTE:
        dword = cast(w, Type.DWORD_PTR).contents
        dword >>= 8
        dword &= 0xff
        return cast(dword, Type.BYTE).contents

    # noinspection PyPep8Naming
    @staticmethod
    def RGB(r: Type.BYTE,
            g: Type.BYTE,
            b: Type.BYTE) -> Type.COLORREF:
        return cast(b, Type.DWORD).contents << 16 | cast(g, Type.WORD).contents << 8 | r

    # noinspection PyPep8Naming
    @staticmethod
    def PALETTERGB(r: Type.BYTE,
                   g: Type.BYTE,
                   b: Type.BYTE) -> Type.COLORREF:
        return 0x02000000 | Macro.RGB(r, g, b)

    # noinspection PyPep8Naming
    @staticmethod
    def GetRValue(rgb: Type.COLORREF) -> Type.BYTE:
        return Macro.LOBYTE(rgb)

    # noinspection PyPep8Naming
    @staticmethod
    def GetGValue(rgb: Type.COLORREF) -> Type.BYTE:
        return Macro.LOBYTE(cast(rgb, Type.WORD).contents >> 8)

    # noinspection PyPep8Naming
    @staticmethod
    def GetBValue(rgb: Type.COLORREF) -> Type.BYTE:
        return Macro.LOBYTE(rgb >> 16)


class _Lib:
    def __init_subclass__(cls):
        for var, type_ in typing.get_type_hints(cls).items():
            setattr(cls, var, type_(var, use_last_error=CATCH_ERROR))


class Lib(_Lib):
    gdi32: ctypes.WinDLL
    gdiplus: ctypes.WinDLL
    kernel32: ctypes.WinDLL
    msvcrt: ctypes.WinDLL
    ntdll: ctypes.WinDLL
    ole32: ctypes.WinDLL
    shell32: ctypes.WinDLL
    user32: ctypes.WinDLL


class Func:  # TODO: help
    RtlAreLongPathsEnabled: Callable[[],
                                     Type.c_ubyte] = Lib.ntdll.RtlAreLongPathsEnabled

    GlobalAlloc: Callable[[Type.UINT, Type.SIZE_T],
                          Type.HGLOBAL] = Lib.kernel32.GlobalAlloc
    GlobalLock: Callable[[Type.HGLOBAL],
                         Type.LPVOID] = Lib.kernel32.GlobalLock
    GlobalUnlock: Callable[[Type.HGLOBAL],
                           Type.BOOL] = Lib.kernel32.GlobalUnlock
    CloseHandle: Callable[[Type.HANDLE],
                          Type.BOOL] = Lib.kernel32.CloseHandle
    GetLastError: Callable[[],
                           Type.DWORD] = Lib.kernel32.GetLastError

    GetObjectA: Callable[[Type.HANDLE, Type.c_int, Type.LPVOID],
                         Type.c_int] = Lib.gdi32.GetObjectA
    GetObjectW: Callable[[Type.HANDLE, Type.c_int, Type.LPVOID],
                         Type.c_int] = Lib.gdi32.GetObjectW
    DeleteObject: Callable[[Type.HGDIOBJ],
                           Type.BOOL] = Lib.gdi32.DeleteObject
    CreateDIBitmap: Callable[[Type.HDC, Pointer[Struct.BITMAPINFOHEADER], Type.DWORD,
                              Type.VOID, Pointer[Struct.BITMAPINFO], Type.UINT],
                             Type.HBITMAP] = Lib.gdi32.CreateDIBitmap
    GetDIBits: Callable[[Type.HDC, Type.HBITMAP, Type.UINT, Type.UINT,
                         Optional[Type.LPVOID], Pointer[Struct.BITMAPINFO], Type.UINT],
                        Type.c_int] = Lib.gdi32.GetDIBits
    CreateSolidBrush: Callable[[Type.COLORREF],
                               Type.HBRUSH] = Lib.gdi32.CreateSolidBrush
    GetStockObject: Callable[[Type.c_int],
                             Type.HGDIOBJ] = Lib.gdi32.GetStockObject

    SystemParametersInfoA: Callable[[Type.UINT, Type.UINT, Type.PVOID, Type.UINT],
                                    Type.BOOL] = Lib.user32.SystemParametersInfoA
    SystemParametersInfoW: Callable[[Type.UINT, Type.UINT, Type.PVOID, Type.UINT],
                                    Type.BOOL] = Lib.user32.SystemParametersInfoW
    OpenClipboard: Callable[[Optional[Type.HWND]],
                            Type.BOOL] = Lib.user32.OpenClipboard
    CloseClipboard: Callable[[],
                             Type.BOOL] = Lib.user32.CloseClipboard
    EmptyClipboard: Callable[[],
                             Type.BOOL] = Lib.user32.EmptyClipboard
    GetClipboardData: Callable[[Type.UINT],
                               Type.HANDLE] = Lib.user32.GetClipboardData
    SetClipboardData: Callable[[Type.UINT, Type.HANDLE],
                               Type.HANDLE] = Lib.user32.SetClipboardData
    GetSysColor: Callable[[Type.c_int],
                          Type.DWORD] = Lib.user32.GetSysColor
    SetSysColors: Callable[[Type.c_int, Pointer[Type.INT], Pointer[Type.COLORREF]],
                           Type.BOOL] = Lib.user32.SetSysColors
    GetMenu: Callable[[Type.HWND],
                      Type.HMENU] = Lib.user32.GetMenu
    GetSystemMenu: Callable[[Type.HWND, Type.BOOL],
                            Type.HMENU] = Lib.user32.GetSystemMenu
    GetSubMenu: Callable[[Type.HMENU, Type.c_int],
                         Type.HMENU] = Lib.user32.GetSubMenu
    GetMenuInfo: Callable[[Type.HMENU, Pointer[Struct.MENUINFO]],
                          Type.BOOL] = Lib.user32.GetMenuInfo
    SetMenuInfo: Callable[[Type.HMENU, Pointer[Struct.MENUINFO]],
                          Type.BOOL] = Lib.user32.SetMenuInfo
    DrawMenuBar: Callable[[Type.HWND],
                          Type.BOOL] = Lib.user32.DrawMenuBar
    LoadImageA: Callable[[Type.HINSTANCE, Type.LPCSTR, Type.UINT, Type.c_int, Type.c_int, Type.UINT],
                         Type.HANDLE] = Lib.user32.LoadImageA
    LoadImageW: Callable[[Type.HINSTANCE, Type.LPCWSTR, Type.UINT, Type.c_int, Type.c_int, Type.UINT],
                         Type.HANDLE] = Lib.user32.LoadImageW
    GetDC: Callable[[Optional[Type.HWND]],
                    Type.HDC] = Lib.user32.GetDC
    GetWindowDC: Callable[[Optional[Type.HWND]],
                          Type.HDC] = Lib.user32.GetWindowDC
    ReleaseDC: Callable[[Optional[Type.HWND], Type.HDC],
                        Type.c_int] = Lib.user32.ReleaseDC

    IIDFromString: Callable[[Type.LPCOLESTR, Pointer[Struct.IID]],
                            Type.HRESULT] = Lib.ole32.IIDFromString
    CLSIDFromString: Callable[[Type.LPCOLESTR, Pointer[Struct.CLSID]],
                              Type.HRESULT] = Lib.ole32.CLSIDFromString
    CoInitialize: Callable[[Optional[Type.LPVOID]],
                           Type.HRESULT] = Lib.ole32.CoInitialize
    CoUninitialize: Callable[[],
                             Type.VOID] = Lib.ole32.CoUninitialize
    CoCreateInstance: Callable[[Pointer[Struct.CLSID], Optional[Pointer[Type.IUnknown]],
                                Type.DWORD, Pointer[Struct.IID], Type.LPVOID],
                               Type.HRESULT] = Lib.ole32.CoCreateInstance
    StringFromIID: Callable[[Pointer[Struct.IID], Pointer[Type.LPOLESTR]],
                            Type.HRESULT] = Lib.ole32.StringFromIID
    StringFromCLSID: Callable[[Pointer[Struct.CLSID], Pointer[Type.LPOLESTR]],
                              Type.HRESULT] = Lib.ole32.StringFromCLSID

    memmove: Callable[[Type.c_void_p, Type.c_void_p, Type.c_size_t],
                      Type.c_void_p] = Lib.msvcrt.memmove
    wcslen: Callable[[Type.c_wchar_p],
                     Type.c_size_t] = Lib.msvcrt.wcslen

    GdiplusStartup: Callable[[Pointer[Type.ULONG_PTR], Pointer[Struct.GdiplusStartupInput],
                              Optional[Pointer[Struct.GdiplusStartupInput]]],
                             Type.Status] = Lib.gdiplus.GdiplusStartup
    GdiplusShutdown: Callable[[Type.ULONG_PTR],
                              Type.VOID] = Lib.gdiplus.GdiplusShutdown
    GdipCreateBitmapFromFile: Callable[[Pointer[Type.WCHAR], Pointer[Type.GpBitmap]],
                                       Type.GpStatus] = Lib.gdiplus.GdipCreateBitmapFromFile
    GdipDisposeImage: Callable[[Type.GpImage],
                               Type.GpStatus] = Lib.gdiplus.GdipDisposeImage
    GdipCreateHBITMAPFromBitmap: Callable[[Type.GpBitmap, Pointer[Type.HBITMAP], Type.ARGB],
                                          Type.GpStatus] = Lib.gdiplus.GdipCreateHBITMAPFromBitmap

    SHGetFolderPathA: Callable[[Optional[Type.HWND], Type.c_int,
                                Optional[Type.HANDLE], Type.DWORD, Type.LPSTR],
                               Type.HRESULT] = Lib.shell32.SHGetFolderPathA
    SHGetFolderPathW: Callable[[Optional[Type.HWND], Type.c_int,
                                Optional[Type.HANDLE], Type.DWORD, Type.LPWSTR],
                               Type.HRESULT] = Lib.shell32.SHGetFolderPathW


# noinspection PyPep8Naming
def POINTER(type_: Union[_CT, type[_CT]]) -> Pointer[_CT]:
    try:
        # noinspection PyTypeChecker
        return ctypes.POINTER(type_)
    except TypeError:
        # noinspection PyTypeChecker
        return ctypes.POINTER(type(type_))


def pointer(type_: _CT) -> Pointer[_CT]:
    try:
        # noinspection PyTypeChecker
        return ctypes.pointer(type_)
    except TypeError:
        # noinspection PyTypeChecker
        return ctypes.POINTER(type_())


def byref(obj: _CT) -> Pointer[_CT]:
    # noinspection PyTypeChecker
    return ctypes.byref(obj)


def cast(obj: Any,  # typing.cast
         type_: type[_CT]) -> Pointer[_CT]:
    try:
        # noinspection PyTypeChecker
        return ctypes.cast(obj, type_)
    except ctypes.ArgumentError:
        # noinspection PyTypeChecker
        return cast(ctypes.byref(obj), type_)
    except TypeError:
        # noinspection PyTypeChecker
        return cast(obj, ctypes.POINTER(type_))


def sizeof(obj: _CT) -> int:
    return ctypes.sizeof(obj)


def array(type_: _CT = Type.c_void_p,
          *elements: Any,
          size: Optional[int] = None) -> Array[_CT]:
    return (type_ * (size or len(elements)))(*elements)


def char_array(obj: str,
               type_: _CT = Type.c_wchar) -> Array[_CT]:
    return (type_ * (len(obj) + 1))(*obj)


@functools.cache
def _get_refs(type_: type[COM.IUnknown]) -> tuple[Pointer[Struct.CLSID], Pointer[Struct.IID]]:
    clsid_ref = byref(Struct.CLSID())
    # noinspection PyProtectedMember
    Func.CLSIDFromString(type_._CLSID, clsid_ref)
    iid_ref = byref(Struct.IID())
    Func.IIDFromString(getattr(Const, f'IID_{type_.__name__}'), iid_ref)
    return clsid_ref, iid_ref


@contextlib.contextmanager
def com(type_: type[_CT]) -> ContextManager[_CT]:
    obj = type_()
    Func.CoInitialize(None)
    try:
        refs = _get_refs(type_)
        Func.CoCreateInstance(refs[0], None, Const.CLSCTX_ALL, refs[1], byref(obj))
        yield obj
    finally:
        if obj:
            obj.Release()
        Func.CoUninitialize()


def _method_type(types_: list) -> list:
    types_.insert(1, ctypes.c_void_p)
    return types_


def _resolve_type(type_: Any) -> Any:
    if isinstance(type_, type(Callable)):
        type_ = [None]
    elif isinstance(type_, type(Callable[[], None])):
        types_ = typing.get_args(type_)
        type_ = [_resolve_type(types_[1])]
        type_.extend(_resolve_type(type_) for type_ in types_[0])
    else:
        if isinstance(type_, type(Optional[object])):
            type_ = typing.get_args(type_)[0]
        if typing.get_origin(type_) is Pointer:
            type_ = ctypes.POINTER(_resolve_type(typing.get_args(type_)[0]))
    return type_


def _items(cls: type) -> Generator[tuple[str, Any], None, None]:
    for var, val in vars(cls).items():
        if not var.startswith('_'):
            yield var, val


def _set_magic(magics: dict[str, Callable],
               magic: str,
               func: Callable) -> None:
    magic_ = getattr(operator, magic, None) or getattr(operator, magic.replace(
        'r', '', 1), None) or getattr(int, magic, None) or getattr(numbers.Complex, magic)
    magics[magic] = functools.update_wrapper(func, magic_)


def _init():
    magics = {}
    for var_ in _CT_BINARY:
        _set_magic(magics, var_, lambda self, other, *args, _magic=var_: type(
            self)(getattr(self.value, _magic)(getattr(other, 'value', other), *args)))
    for var_ in _CT_I_BINARY:
        _set_magic(magics, var_, lambda self, other, *args, _magic=var_.replace('i', '', 1): (setattr(
            self, 'value', getattr(self.value, _magic)(getattr(other, 'value', other), *args)), self)[1])
    for var_ in _CT_UNARY:
        _set_magic(magics, var_, lambda self, *args, _magic=var_: type(self)(getattr(self.value, _magic)(*args)))
    for var_ in _PY_BINARY:
        _set_magic(magics, var_, lambda self, other, _magic=var_: getattr(
            self.value, _magic)(getattr(other, 'value', other)))
    for var_ in _PY_UNARY:
        _set_magic(magics, var_, (lambda self: complex(self.value)) if var_ == '__complex__' else (
            lambda self, _magic=var_: getattr(self.value, _magic)()))
    for var, type_ in _items(Type):  # TODO: try not to modify actual ctypes, do not use _magic
        type__ = _resolve_type(type_)
        if type__ not in vars(Type).values():
            for var_, magic in magics.items():
                setattr(type__, var_, magic)
        setattr(Type, var, type__)

    for var, struct in _items(Struct):
        class Wrapper(ctypes.Structure):
            _fields_ = tuple((field, _resolve_type(type_)) for field, type_ in typing.get_type_hints(struct).items())
            _defaults = tuple((field, getattr(struct, field) or type_) for field, type_ in _fields_)

            def __init__(self, *args, **kwargs):
                for i, field in enumerate(self._defaults):
                    if i >= len(args) and field[0] not in kwargs:
                        kwargs[field[0]] = field[1]() if callable(field[1]) else field[1]
                super().__init__(*args, **kwargs)

        # noinspection PyUnresolvedReferences
        functools.update_wrapper(Wrapper, struct, functools.WRAPPER_ASSIGNMENTS + ('__repr__',), ())
        setattr(Struct, var, Wrapper)

    for var, com_ in _items(COM):
        class Wrapper(ctypes.c_void_p):
            # noinspection PyTypeChecker
            _pointer = ctypes.POINTER(type(var, (ctypes.Structure,), {'_fields_': tuple((func, ctypes.WINFUNCTYPE(
                *_method_type(_resolve_type(types)))) for func, types in typing.get_type_hints(com_).items())}))
            # noinspection PyProtectedMember
            _methods = tuple(types[0] for types in _items(_pointer._type_))

            def __getattr__(self, name):
                if name in self._methods:
                    funcs = ctypes.cast(ctypes.cast(self, ctypes.POINTER(
                        ctypes.c_void_p)).contents.value, self._pointer).contents
                    for method in self._methods:
                        setattr(self, method, types.MethodType(getattr(funcs, method), self))
                return super().__getattribute__(name)

        # noinspection PyUnresolvedReferences
        functools.update_wrapper(Wrapper, com_, functools.WRAPPER_ASSIGNMENTS + ('_CLSID',), ())
        setattr(COM, var, Wrapper)

    for var, macro in _items(Macro):
        setattr(Macro, var, functools.update_wrapper(lambda *args, _func=macro.__func__, _types=typing.get_type_hints(
            macro.__func__).values(): _func(*(arg if isinstance(arg, type___) else type___(arg) for arg, type___ in
                                              zip(args, _types))), macro.__func__))

    types_ = typing.get_type_hints(Func)
    for var, func in _items(Func):
        func.restype, *func.argtypes = _resolve_type(types_[var])


_init()

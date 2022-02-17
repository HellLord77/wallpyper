from __future__ import annotations as _

import enum as _enum
import functools as _functools
from typing import Optional as _Optional
from typing import Union as _Union

from . import _type
from .__head__ import _Globals

_ASSIGNED = ('__str__', *(assigned for assigned in _functools.WRAPPER_ASSIGNMENTS))


class _EnumMeta(_enum.EnumMeta):
    # noinspection PyMethodOverriding
    @staticmethod
    def __call__(value: _Optional[int] = None):
        pass


class _Enum(_enum.Enum, metaclass=_EnumMeta):
    pass


class AsyncStatus(_Enum):
    Started = None
    Completed = None
    Canceled = None
    Error = None


class ColorAdjustType(_Enum):
    ColorAdjustTypeDefault = None
    ColorAdjustTypeBitmap = None
    ColorAdjustTypeBrush = None
    ColorAdjustTypePen = None
    ColorAdjustTypeText = None
    ColorAdjustTypeCount = None
    ColorAdjustTypeAny = None


class ColorMatrixFlags(_Enum):
    ColorMatrixFlagsDefault = None
    ColorMatrixFlagsSkipGrays = None
    ColorMatrixFlagsAltGray = None


class CreationCollisionOption(_Enum):
    GenerateUniqueName = None
    ReplaceExisting = None
    FailIfExists = None
    OpenIfExists = None


class ApplicationDataCreateDisposition(_Enum):
    Always = None
    Existing = None


class ApplicationDataLocality(_Enum):
    Local = None
    Roaming = None
    Temporary = None
    LocalCache = None
    SharedLocal = None


class FileAccessMode(_Enum):
    Read = None
    ReadWrite = None


class FileAttributes(_Enum):
    Normal = 0
    ReadOnly = 0x1
    Directory = 0x10
    Archive = 0x20
    Temporary = 0x100
    LocallyIncomplete = 0x200


class KnownFolderId(_Enum):
    AppCaptures = None
    CameraRoll = None
    DocumentsLibrary = None
    HomeGroup = None
    MediaServerDevices = None
    MusicLibrary = None
    Objects3D = None
    PicturesLibrary = None
    Playlists = None
    RecordedCalls = None
    RemovableDevices = None
    SavedPictures = None
    Screenshots = None
    VideosLibrary = None
    AllAppMods = None
    CurrentAppMods = None
    DownloadsFolder = None


class KnownFoldersAccessStatus(_Enum):
    DeniedBySystem = None
    NotDeclaredByApp = None
    DeniedByUser = None
    UserPromptRequired = None
    Allowed = None
    AllowedPerAppFolder = None


class KnownLibraryId(_Enum):
    Music = None
    Pictures = None
    Videos = None
    Documents = None


class NameCollisionOption(_Enum):
    GenerateUniqueName = None
    ReplaceExisting = None
    FailIfExists = None


class StorageDeleteOption(_Enum):
    Default = None
    PermanentDelete = None


class StorageLibraryChangeType(_Enum):
    Created = None
    Deleted = None
    MovedOrRenamed = None
    ContentsChanged = None
    MovedOutOfLibrary = None
    MovedIntoLibrary = None
    ContentsReplaced = None
    IndexingStatusChanged = None
    EncryptionChanged = None
    ChangeTrackingLost = None


class StreamedFileFailureMode(_Enum):
    Failed = None
    CurrentlyUnavailable = None
    Incomplete = None


# noinspection PyPep8Naming
class DESKTOP_SLIDESHOW_DIRECTION(_Enum):
    DSD_FORWARD = None
    DSD_BACKWARD = None


# noinspection PyPep8Naming
class DESKTOP_SLIDESHOW_OPTIONS(_Enum):
    DSO_SHUFFLEIMAGES = 0x1


# noinspection PyPep8Naming
class DESKTOP_SLIDESHOW_STATE(_Enum):
    DSS_ENABLED = 0x1
    DSS_SLIDESHOW = 0x2
    DSS_DISABLED_BY_REMOTE_SESSION = 0x4


# noinspection PyPep8Naming
class DESKTOP_WALLPAPER_POSITION(_Enum):
    DWPOS_CENTER = None
    DWPOS_TILE = None
    DWPOS_STRETCH = None
    DWPOS_FIT = None
    DWPOS_FILL = None
    DWPOS_SPAN = None


class DebugEventLevel(_Enum):
    DebugEventLevelFatal = None
    DebugEventLevelWarning = None


class FILEOPENDIALOGOPTIONS(_Enum):
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


class GETPROPERTYSTOREFLAGS(_Enum):
    GPS_DEFAULT = 0
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


class GenericFontFamily(_Enum):
    GenericFontFamilySerif = None
    GenericFontFamilySansSerif = None
    GenericFontFamilyMonospace = None


class MatrixOrder(_Enum):
    MatrixOrderPrepend = None
    MatrixOrderAppend = None


class WarpMode(_Enum):
    WarpModePerspective = None
    WarpModeBilinear = None


class LinearGradientMode(_Enum):
    LinearGradientModeHorizontal = None
    LinearGradientModeVertical = None
    LinearGradientModeForwardDiagonal = None
    LinearGradientModeBackwardDiagonal = None


class CombineMode(_Enum):
    CombineModeReplace = None
    CombineModeIntersect = None
    CombineModeUnion = None
    CombineModeXor = None
    CombineModeExclude = None
    CombineModeComplement = None


class QualityMode(_Enum):
    QualityModeInvalid = -1
    QualityModeDefault = 0
    QualityModeLow = 1
    QualityModeHigh = 2


class FillMode(_Enum):
    FillModeAlternate = None
    FillModeWinding = None


class InputStreamOptions(_Enum):
    None_ = 0
    Partial = 0x1
    ReadAhead = 0x2


# noinspection PyPep8Naming
class KNOWN_FOLDER_FLAG(_Enum):
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
class RO_INIT_TYPE(_Enum):
    RO_INIT_SINGLETHREADED = None
    RO_INIT_MULTITHREADED = None


class SIGDN(_Enum):
    SIGDN_NORMALDISPLAY = 0
    SIGDN_PARENTRELATIVEPARSING = 0x80018001
    SIGDN_DESKTOPABSOLUTEPARSING = 0x80028000
    SIGDN_PARENTRELATIVEEDITING = 0x80031001
    SIGDN_DESKTOPABSOLUTEEDITING = 0x8004c000
    SIGDN_FILESYSPATH = 0x80058000
    SIGDN_URL = 0x80068000
    SIGDN_PARENTRELATIVEFORADDRESSBAR = 0x8007c001
    SIGDN_PARENTRELATIVE = 0x80080001
    SIGDN_PARENTRELATIVEFORUI = 0x80094001


class TrustLevel(_Enum):
    BaseTrust = None
    PartialTrust = None
    FullTrust = None


class Unit(_Enum):
    UnitWorld = None
    UnitDisplay = None
    UnitPixel = None
    UnitPoint = None
    UnitInch = None
    UnitDocument = None
    UnitMillimeter = None


class Status(_Enum):
    Ok = None
    GenericError = None
    InvalidParameter = None
    OutOfMemory = None
    ObjectBusy = None
    InsufficientBuffer = None
    NotImplemented = None
    Win32Error = None
    WrongState = None
    Aborted = None
    FileNotFound = None
    ValueOverflow = None
    AccessDenied = None
    UnknownImageFormat = None
    FontFamilyNotFound = None
    FontStyleNotFound = None
    NotTrueTypeFont = None
    UnsupportedGdiplusVersion = None
    GdiplusNotInitialized = None
    PropertyNotFound = None
    PropertyNotSupported = None
    ProfileNotFound = None


# noinspection PyPep8Naming
class SHGFP_TYPE(_Enum):
    SHGFP_TYPE_CURRENT = None
    SHGFP_TYPE_DEFAULT = None


class VARENUM(_Enum):
    VT_EMPTY = 0
    VT_NULL = 1
    VT_I2 = 2
    VT_I4 = 3
    VT_R4 = 4
    VT_R8 = 5
    VT_CY = 6
    VT_DATE = 7
    VT_BSTR = 8
    VT_DISPATCH = 9
    VT_ERROR = 10
    VT_BOOL = 11
    VT_VARIANT = 12
    VT_UNKNOWN = 13
    VT_DECIMAL = 14
    VT_I1 = 16
    VT_UI1 = 17
    VT_UI2 = 18
    VT_UI4 = 19
    VT_I8 = 20
    VT_UI8 = 21
    VT_INT = 22
    VT_UINT = 23
    VT_VOID = 24
    VT_HRESULT = 25
    VT_PTR = 26
    VT_SAFEARRAY = 27
    VT_CARRAY = 28
    VT_USERDEFINED = 29
    VT_LPSTR = 30
    VT_LPWSTR = 31
    VT_RECORD = 36
    VT_INT_PTR = 37
    VT_UINT_PTR = 38
    VT_FILETIME = 64
    VT_BLOB = 65
    VT_STREAM = 66
    VT_STORAGE = 67
    VT_STREAMED_OBJECT = 68
    VT_STORED_OBJECT = 69
    VT_BLOB_OBJECT = 70
    VT_CF = 71
    VT_CLSID = 72
    VT_VERSIONED_STREAM = 73
    VT_BSTR_BLOB = 0xfff
    VT_VECTOR = 0x1000
    VT_ARRAY = 0x2000
    VT_BYREF = 0x4000
    VT_RESERVED = 0x8000
    VT_ILLEGAL = 0xffff
    VT_ILLEGALMASKED = 0xfff
    VT_TYPEMASK = 0xfff


# noinspection PyPep8Naming
class SLGP_FLAGS(_Enum):
    SLGP_SHORTPATH = 0x1
    SLGP_UNCPRIORITY = 0x2
    SLGP_RAWPATH = 0x4
    SLGP_RELATIVEPRIORITY = 0x8


# noinspection PyPep8Naming
class SLR_FLAGS(_Enum):
    SLR_NONE = 0
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


class RotateFlipType(_Enum):
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


GpMatrixOrder = MatrixOrder
GpUnit = Unit
GpStatus = Status


class _WrapperMeta(type(_type.c_uint)):
    __members__: dict[str, int]

    def __getattr__(self, name: str):
        if name in self.__members__:
            # noinspection PyCallingNonCallable
            setattr(self, name, self(self.__members__[name]))
        return super().__getattribute__(name)


def _get_members(enum: _Enum) -> dict[int, str]:
    last = -1
    # noinspection PyUnresolvedReferences,PyProtectedMember
    return {name: (last := (last + 1) if val.value is None else val.value) for name, val in enum._member_map_.items()}


def _init(item: str) -> type:
    _globals.check_item(item)

    class Wrapper(_type.c_uint, metaclass=_WrapperMeta):
        __members__ = _get_members(_globals.vars_[item])

        def __init__(self, value: _Optional[int] = None):
            if value is None:
                for val in self.__members__.values():
                    value = val
                    break
            super().__init__(value)

        @property
        def _name_(self) -> _Union[int, str]:
            for name, val in self.__members__.items():
                if self.value == val:
                    return name
            return self.value

        name = _name_

    # TODO docs
    return _functools.update_wrapper(Wrapper, _globals.vars_[item], _ASSIGNED, ())


_globals = _Globals()

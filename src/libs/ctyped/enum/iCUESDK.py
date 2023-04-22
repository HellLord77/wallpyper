from . import _Enum


# iCUESDK
class CorsairError(_Enum):
    """
    contains shared list of all errors which could happen during calling of Corsair*
    functions
    """
    Success = 0
    """
    if previously called function completed successfully
    """
    NotConnected = 1
    """
    if iCUE is not running or was shut down or third-party control is disabled in
    iCUE settings (runtime error), or if developer did not call CorsairConnect after
    calling CorsairDisconnect or on app start (developer error)
    """
    NoControl = 2
    """
    if some other client has or took over exclusive control (runtime error)
    """
    IncompatibleProtocol = 3
    """
    if developer is calling the function that is not supported by the server (either
    because protocol has broken by server or client or because the function is new
    and server is too old. Check CorsairSessionDetails for details) (developer
    error)
    """
    InvalidArguments = 4
    """
    if developer supplied invalid arguments to the function (for specifics look at
    function descriptions) (developer error)
    """
    InvalidOperation = 5
    """
    if developer is calling the function that is not allowed due to current state
    (reading improper properties from device, or setting callback when it has
    already been set) (developer error)
    """
    DeviceNotFound = 6
    """
    if invalid device id has been supplied as an argument to the function (when
    device id refers to disconnected device) (runtime error)
    """
    NotAllowed = 7
    """
    if specific functionality (key interception) is disabled in iCUE settings
    (runtime error)
    """


class CorsairSessionState(_Enum):
    """
    contains a list of all possible session states
    """
    Invalid = 0
    """
    dummy value
    """
    Closed = 1
    """
    client not initialized or client closed connection (initial state)
    """
    Connecting = 2
    """
    client initiated connection but not connected yet
    """
    Timeout = 3
    """
    server did not respond, sdk will try again
    """
    ConnectionRefused = 4
    """
    server did not allow connection
    """
    ConnectionLost = 5
    """
    server closed connection
    """
    Connected = 6
    """
    successfully connected
    """


class CorsairDeviceType(_Enum):
    """
    contains list of available device types
    """
    Unknown = 0
    """
    for unknown/invalid devices
    """
    Keyboard = 1
    """
    for keyboards
    """
    Mouse = 2
    """
    for mice
    """
    Mousemat = 4
    """
    for mousemats
    """
    Headset = 8
    """
    for headsets
    """
    HeadsetStand = 16
    """
    for headset stands
    """
    FanLedController = 32
    """
    for DIY-devices like Commander PRO
    """
    LedController = 64
    """
    for DIY-devices like Lighting Node PRO
    """
    MemoryModule = 128
    """
    for memory modules
    """
    Cooler = 256
    """
    for coolers
    """
    Motherboard = 512
    """
    for motherboards
    """
    GraphicsCard = 1024
    """
    for graphics cards
    """
    Touchbar = 2048
    """
    for touchbars
    """
    All = -1
    """
    for all devices
    """


class CorsairEventId(_Enum):
    """
    contains list of event identifiers
    """
    Invalid = 0
    """
    dummy value,
    """
    DeviceConnectionStatusChangedEvent = 1
    KeyEvent = 2


class CorsairMacroKeyId(_Enum):
    """
    contains a shared list of G, M and S keys (not all available keys!)
    """
    CMKI_Invalid = 0
    CMKI_1 = 1
    CMKI_2 = 2
    CMKI_3 = 3
    CMKI_4 = 4
    CMKI_5 = 5
    CMKI_6 = 6
    CMKI_7 = 7
    CMKI_8 = 8
    CMKI_9 = 9
    CMKI_10 = 10
    CMKI_11 = 11
    CMKI_12 = 12
    CMKI_13 = 13
    CMKI_14 = 14
    CMKI_15 = 15
    CMKI_16 = 16
    CMKI_17 = 17
    CMKI_18 = 18
    CMKI_19 = 19
    CMKI_20 = 20


class CorsairDevicePropertyId(_Enum):
    """
    contains list of properties identifiers which can be read from device
    """
    Invalid = 0
    """
    dummy value
    """
    PropertyArray = 1
    """
    array of CorsairDevicePropertyId members supported by device
    """
    MicEnabled = 2
    """
    indicates Mic state (On or Off); used for headset, headset stand
    """
    SurroundSoundEnabled = 3
    """
    indicates Surround Sound state (On or Off); used for headset, headset stand
    """
    SidetoneEnabled = 4
    """
    indicates Sidetone state (On or Off); used for headset (where applicable)
    """
    EqualizerPreset = 5
    """
    the number of active equalizer preset (integer, 1 - 5); used for headset,
    headset stand
    """
    PhysicalLayout = 6
    """
    keyboard physical layout (see CorsairPhysicalLayout for valid values); used for
    keyboard
    """
    LogicalLayout = 7
    """
    keyboard logical layout (see CorsairLogicalLayout for valid values); used for
    keyboard
    """
    MacroKeyArray = 8
    """
    array of programmable G, M or S keys on device
    """
    BatteryLevel = 9
    """
    battery level (0 - 100); used for wireless devices
    """
    ChannelLedCount = 10
    """
    total number of LEDs connected to the channel
    """
    ChannelDeviceCount = 11
    """
    number of LED-devices (fans, strips, etc.) connected to the channel which is
    controlled by the DIY device
    """
    ChannelDeviceLedCountArray = 12
    """
    array of integers, each element describes the number of LEDs controlled by the
    channel device
    """
    ChannelDeviceTypeArray = 13
    """
    array of CorsairChannelDeviceType members, each element describes the type of
    the channel device
    """


class CorsairDataType(_Enum):
    """
    contains list of available property types
    """
    Boolean = 0
    """
    for property of type Boolean
    """
    Int32 = 1
    """
    for property of type Int32 or Enumeration
    """
    Float64 = 2
    """
    for property of type Float64
    """
    String = 3
    """
    for property of type String
    """
    Boolean_Array = 16
    """
    for array of Boolean
    """
    Int32_Array = 17
    """
    for array of Int32
    """
    Float64_Array = 18
    """
    for array of Float64
    """
    String_Array = 19
    """
    for array of String
    """


class CorsairPropertyFlag(_Enum):
    """
    contains list of operations that can be applied to the property
    """
    None_ = 0
    CanRead = 1
    """
    describes readable property
    """
    CanWrite = 2
    """
    describes writable property
    """
    Indexed = 4
    """
    if flag is set, then index should be used to read/write multiple properties that
    share the same property identifier
    """


class CorsairPhysicalLayout(_Enum):
    """
    contains list of available physical layouts for keyboards
    """
    Invalid = 0
    US = 1
    UK = 2
    JP = 3
    KR = 4
    BR = 5


class CorsairLogicalLayout(_Enum):
    """
    contains list of available logical layouts for keyboards
    """
    Invalid = 0
    US_Int = 1
    NA = 2
    EU = 3
    UK = 4
    BE = 5
    BR = 6
    CH = 7
    CN = 8
    DE = 9
    ES = 10
    FR = 11
    IT = 12
    ND = 13
    RU = 14
    JP = 15
    KR = 16
    TW = 17
    MEX = 18


class CorsairChannelDeviceType(_Enum):
    """
    contains list of the LED-devices which can be connected to the DIY-device,
    memory module or cooler
    """
    CCDT_Invalid = 0
    CCDT_HD_Fan = 1
    CCDT_SP_Fan = 2
    CCDT_LL_Fan = 3
    CCDT_ML_Fan = 4
    CCDT_QL_Fan = 5
    CCDT_8LedSeriesFan = 6
    CCDT_Strip = 7
    CCDT_DAP = 8
    CCDT_Pump = 9
    CCDT_DRAM = 10
    CCDT_WaterBlock = 11


class CorsairAccessLevel(_Enum):
    """
    contains list of available SDK access levels
    """
    Shared = 0
    """
    shared mode (default)
    """
    ExclusiveLightingControl = 1
    """
    exclusive lightings, but shared events
    """
    ExclusiveKeyEventsListening = 2
    """
    exclusive key events, but shared lightings
    """
    ExclusiveLightingControlAndKeyEventsListening = 3
    """
    exclusive mode
    """


# iCUESDKLedIdEnum
class CorsairLedGroup(_Enum):
    """
    contains a list of led groups. Led group is used as a part of led identifier
    """
    Keyboard = 0
    """
    for keyboard leds
    """
    KeyboardGKeys = 1
    """
    for keyboard leds on G keys
    """
    KeyboardEdge = 2
    """
    for keyboard lighting pipe leds
    """
    KeyboardOem = 3
    """
    for vendor specific keyboard leds (ProfileSwitch, DialRing, etc.)
    """
    Mouse = 4
    """
    for mouse leds
    """
    Mousemat = 5
    """
    for mousemat leds
    """
    Headset = 6
    """
    for headset leds
    """
    HeadsetStand = 7
    """
    for headset stand leds
    """
    MemoryModule = 8
    """
    for memory module leds
    """
    Motherboard = 9
    """
    for motherboard leds
    """
    GraphicsCard = 10
    """
    for graphics card leds
    """
    DIY_Channel1 = 11
    """
    for leds on the first channel of DIY devices and coolers
    """
    DIY_Channel2 = 12
    """
    for leds on the second channel of DIY devices and coolers
    """
    DIY_Channel3 = 13
    """
    for leds on the third channel of DIY devices and coolers
    """
    Touchbar = 14
    """
    for touchbar leds
    """


# noinspection PyPep8Naming
class CorsairLedId_Keyboard(_Enum):
    CLK_Invalid = 0
    CLK_Escape = 1
    CLK_F1 = 2
    CLK_F2 = 3
    CLK_F3 = 4
    CLK_F4 = 5
    CLK_F5 = 6
    CLK_F6 = 7
    CLK_F7 = 8
    CLK_F8 = 9
    CLK_F9 = 10
    CLK_F10 = 11
    CLK_F11 = 12
    CLK_F12 = 13
    CLK_GraveAccentAndTilde = 14
    CLK_1 = 15
    CLK_2 = 16
    CLK_3 = 17
    CLK_4 = 18
    CLK_5 = 19
    CLK_6 = 20
    CLK_7 = 21
    CLK_8 = 22
    CLK_9 = 23
    CLK_0 = 24
    CLK_MinusAndUnderscore = 25
    CLK_EqualsAndPlus = 26
    CLK_Backspace = 27
    CLK_Tab = 28
    CLK_Q = 29
    CLK_W = 30
    CLK_E = 31
    CLK_R = 32
    CLK_T = 33
    CLK_Y = 34
    CLK_U = 35
    CLK_I = 36
    CLK_O = 37
    CLK_P = 38
    CLK_BracketLeft = 39
    CLK_BracketRight = 40
    CLK_CapsLock = 41
    CLK_A = 42
    CLK_S = 43
    CLK_D = 44
    CLK_F = 45
    CLK_G = 46
    CLK_H = 47
    CLK_J = 48
    CLK_K = 49
    CLK_L = 50
    CLK_SemicolonAndColon = 51
    CLK_ApostropheAndDoubleQuote = 52
    CLK_Backslash = 53
    CLK_Enter = 54
    CLK_LeftShift = 55
    CLK_NonUsBackslash = 56
    CLK_Z = 57
    CLK_X = 58
    CLK_C = 59
    CLK_V = 60
    CLK_B = 61
    CLK_N = 62
    CLK_M = 63
    CLK_CommaAndLessThan = 64
    CLK_PeriodAndBiggerThan = 65
    CLK_SlashAndQuestionMark = 66
    CLK_RightShift = 67
    CLK_LeftCtrl = 68
    CLK_LeftGui = 69
    CLK_LeftAlt = 70
    CLK_Space = 71
    CLK_RightAlt = 72
    CLK_RightGui = 73
    CLK_Application = 74
    CLK_RightCtrl = 75
    CLK_LedProgramming = 76
    CLK_Lang1 = 77
    CLK_Lang2 = 78
    CLK_International1 = 79
    CLK_International2 = 80
    CLK_International3 = 81
    CLK_International4 = 82
    CLK_International5 = 83
    CLK_PrintScreen = 84
    CLK_ScrollLock = 85
    CLK_PauseBreak = 86
    CLK_Insert = 87
    CLK_Home = 88
    CLK_PageUp = 89
    CLK_Delete = 90
    CLK_End = 91
    CLK_PageDown = 92
    CLK_UpArrow = 93
    CLK_LeftArrow = 94
    CLK_DownArrow = 95
    CLK_RightArrow = 96
    CLK_NonUsTilde = 97
    CLK_Brightness = 98
    CLK_WinLock = 99
    CLK_Mute = 100
    CLK_Stop = 101
    CLK_ScanPreviousTrack = 102
    CLK_PlayPause = 103
    CLK_ScanNextTrack = 104
    CLK_NumLock = 105
    CLK_KeypadSlash = 106
    CLK_KeypadAsterisk = 107
    CLK_KeypadMinus = 108
    CLK_Keypad7 = 109
    CLK_Keypad8 = 110
    CLK_Keypad9 = 111
    CLK_KeypadPlus = 112
    CLK_Keypad4 = 113
    CLK_Keypad5 = 114
    CLK_Keypad6 = 115
    CLK_Keypad1 = 116
    CLK_Keypad2 = 117
    CLK_Keypad3 = 118
    CLK_KeypadComma = 119
    CLK_KeypadEnter = 120
    CLK_Keypad0 = 121
    CLK_KeypadPeriodAndDelete = 122
    CLK_VolumeUp = 123
    CLK_VolumeDown = 124
    CLK_MR = 125
    CLK_M1 = 126
    CLK_M2 = 127
    CLK_M3 = 128
    CLK_Fn = 129

from . import WM_APP as _WM_APP

# RzErrors
RZRESULT_INVALID = -1
"""
Invalid.
"""
RZRESULT_SUCCESS = 0
"""
Success.
"""
RZRESULT_ACCESS_DENIED = 5
"""
Access denied.
"""
RZRESULT_INVALID_HANDLE = 6
"""
Invalid handle.
"""
RZRESULT_NOT_SUPPORTED = 50
"""
Not supported.
"""
RZRESULT_INVALID_PARAMETER = 87
"""
Invalid parameter.
"""
RZRESULT_SERVICE_NOT_ACTIVE = 1062
"""
The service has not been started.
"""
RZRESULT_SINGLE_INSTANCE_APP = 1152
"""
Cannot start more than one instance of the specified program.
"""
RZRESULT_DEVICE_NOT_CONNECTED = 1167
"""
Device not connected.
"""
RZRESULT_NOT_FOUND = 1168
"""
Element not found.
"""
RZRESULT_REQUEST_ABORTED = 1235
"""
Request aborted.
"""
RZRESULT_ALREADY_INITIALIZED = 1247
"""
An attempt was made to perform an initialization operation when initialization has already been completed.
"""
RZRESULT_RESOURCE_DISABLED = 4309
"""
Resource not available or disabled.
"""
RZRESULT_DEVICE_NOT_AVAILABLE = 4319
"""
Device not available or supported.
"""
RZRESULT_NOT_VALID_STATE = 5023
"""
The group or resource is not in the correct state to perform the requested operation.
"""
RZRESULT_NO_MORE_ITEMS = 259
"""
No more items.
"""
RZRESULT_FAILED = 2147500037
"""
General failure.
"""


class ChromaSDK:
    # RzChromaSDKTypes
    WM_CHROMA_EVENT = _WM_APP + 0x2000
    MAX_ROW = 30
    MAX_COLUMN = 30

    class Keyboard:
        MAX_ROW = 6
        MAX_COLUMN = 22
        MAX_KEYS = MAX_ROW * MAX_COLUMN
        MAX_CUSTOM_EFFECTS = MAX_KEYS

        # noinspection PyPep8Naming
        class v2:
            MAX_ROW = 8
            MAX_COLUMN = 24

    class Mouse:
        MAX_LEDS = 30
        MAX_ROW = 9
        MAX_COLUMN = 7
        MAX_LEDS2 = MAX_ROW * MAX_COLUMN

    class Headset:
        MAX_LEDS = 5

    class Mousepad:
        MAX_LEDS = 15

        # noinspection PyPep8Naming
        class v2:
            MAX_LEDS = 20

    class Keypad:
        MAX_ROW = 4
        MAX_COLUMN = 5
        MAX_KEYS = MAX_ROW * MAX_COLUMN

    class ChromaLink:
        MAX_LEDS = 5

    # RzChromaSDKDefines
    BLACKWIDOW_CHROMA = '{2EA1BB63-CA28-428D-9F06-196B88330BBB}'
    BLACKWIDOW_CHROMA_TE = '{ED1C1B82-BFBE-418F-B49D-D03F05B149DF}'
    DEATHSTALKER_CHROMA = '{18C5AD9B-4326-4828-92C4-2669A66D2283}'
    OVERWATCH_KEYBOARD = '{872AB2A9-7959-4478-9FED-15F6186E72E4}'
    BLACKWIDOW_X_CHROMA = '{5AF60076-ADE9-43D4-B574-52599293B554}'
    BLACKWIDOW_X_TE_CHROMA = '{2D84DD51-3290-4AAC-9A89-D8AFDE38B57C}'
    ORNATA_CHROMA = '{803378C1-CC48-4970-8539-D828CC1D420A}'
    BLADE_STEALTH = '{C83BDFE8-E7FC-40E0-99DB-872E23F19891}'
    BLADE = '{F2BEDFAF-A0FE-4651-9D41-B6CE603A3DDD}'
    BLADE_PRO = '{A73AC338-F0E5-4BF7-91AE-DD1F7E1737A5}'
    HUNTSMAN = '{F85E7473-8F03-45B6-A16E-CE26CB8D2441}'
    BLACKWIDOW_ELITE = '{16BB5ABD-C1CD-4CB3-BDF7-62438748BD98}'
    DEATHADDER_CHROMA = '{AEC50D91-B1F1-452F-8E16-7B73F376FDF3}'
    MAMBA_CHROMA_TE = '{7EC00450-E0EE-4289-89D5-0D879C19061A}'
    DIAMONDBACK_CHROMA = '{FF8A5929-4512-4257-8D59-C647BF9935D0}'
    MAMBA_CHROMA = '{D527CBDC-EB0A-483A-9E89-66D50463EC6C}'
    NAGA_EPIC_CHROMA = '{D714C50B-7158-4368-B99C-601ACB985E98}'
    NAGA_CHROMA = '{F1876328-6CA4-46AE-BE04-BE812B414433}'
    OROCHI_CHROMA = '{52C15681-4ECE-4DD9-8A52-A1418459EB34}'
    NAGA_HEX_CHROMA = '{195D70F5-F285-4CFF-99F2-B8C0E9658DB4}'
    DEATHADDER_ELITE_CHROMA = '{77834867-3237-4A9F-AD77-4A46C4183003}'
    KRAKEN71_CHROMA = '{CD1E09A5-D5E6-4A6C-A93B-E6D9BF1D2092}'
    MANOWAR_CHROMA = '{DF3164D7-5408-4A0E-8A7F-A7412F26BEBF}'
    KRAKEN71_REFRESH_CHROMA = '{7FB8A36E-9E74-4BB3-8C86-CAC7F7891EBD}'
    KRAKEN_KITTY = '{FB357780-4617-43A7-960F-D1190ED54806}'
    FIREFLY_CHROMA = '{80F95A94-73D2-48CA-AE9A-0986789A9AF2}'
    TARTARUS_CHROMA = '{00F0545C-E180-4AD1-8E8A-419061CE505E}'
    ORBWEAVER_CHROMA = '{9D24B0AB-0162-466C-9640-7A924AA4D9FD}'
    LENOVO_Y900 = '{35F6F18D-1AE5-436C-A575-AB44A127903A}'
    LENOVO_Y27 = '{47DB1FA7-6B9B-4EE6-B6F4-4071A3B2053B}'
    CORE_CHROMA = '{0201203B-62F3-4C50-83DD-598BABD208E0}'
    CHROMABOX = '{BB2E9C9B-B0D2-461A-BA52-230B5D6C3609}'
    NOMMO_CHROMA = '{45B308F2-CD44-4594-8375-4D5945AD880E}'
    NOMMO_CHROMA_PRO = '{3017280B-D7F9-4D7B-930E-7B47181B46B5}'

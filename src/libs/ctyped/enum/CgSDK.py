from . import _Enum


# CgSDK
class CorsairAccessMode(_Enum):
    """
    contains list of available SDK access modes
    """
    ExclusiveLightingControl = 0


class CorsairError(_Enum):
    """
    contains shared list of all errors which could happen during calling of Corsair*
    functions
    """
    Success = 0
    """
    if previously called function completed successfully
    """
    ServerNotFound = 1
    """
    CUE is not running or was shut down or third-party control is disabled in CUE
    settings(runtime error)
    """
    NoControl = 2
    """
    if some other client has or took over exclusive control (runtime error)
    """
    ProtocolHandshakeMissing = 3
    """
    if developer did not perform protocol handshake(developer error)
    """
    IncompatibleProtocol = 4
    """
    if developer is calling the function that is not supported by the server(either
    because protocol has broken by server or client or because the function is new
    and server is too old. Check CorsairProtocolDetails for details) (developer
    error)
    """
    InvalidArguments = 5
    """
    if developer supplied invalid arguments to the function(for specifics look at
    function descriptions). (developer error)
    """

import dataclasses as _dataclasses

from . import _struct
from .__head__ import _Globals


# noinspection PyPep8Naming
@_dataclasses.dataclass
class PROPVARIANT_U:
    S: _struct.PROPVARIANT_U_S = None
    decVal: _struct.DECIMAL = None


_globals = _Globals()

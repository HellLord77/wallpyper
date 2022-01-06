import dataclasses as _dataclasses

from . import _struct
from .__head__ import _Globals


# noinspection PyPep8Naming
@_dataclasses.dataclass
class PROPVARIANT_u:
    s: _struct.tag_inner_PROPVARIANT = None
    decVal: _struct.DECIMAL = None


_globals = _Globals()

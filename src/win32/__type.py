from __future__ import annotations

from typing import Optional

from libs import ctyped
from libs.ctyped.lib import oleaut32


class BSTR(ctyped.type.BSTR):
    @classmethod
    def from_string(cls, string: Optional[str] = None, size: Optional[int] = None) -> BSTR:
        self = cls()
        if size is not None:
            self.value = oleaut32.SysAllocStringLen(string, size)
        elif string is not None:
            self.value = oleaut32.SysAllocString(string)
        return self

    def __del__(self):
        if self:
            oleaut32.SysFreeString(self)
            self.value = None

    def __str__(self):
        return ctyped.type.c_wchar_p.from_buffer(self).value

    def __len__(self):
        return oleaut32.SysStringLen(self)

    def resize(self, size: int, string: Optional[str] = None) -> bool:
        return bool(oleaut32.SysReAllocStringLen(ctyped.byref(self), string, size))

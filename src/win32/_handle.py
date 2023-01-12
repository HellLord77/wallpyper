from __future__ import annotations as _

from typing import Optional as _Optional

from libs import ctyped
from libs.ctyped.lib import combase, gdi32, user32

_HMENU_MF = ctyped.const.MF_BYCOMMAND, ctyped.const.MF_BYPOSITION


class HSTRING(ctyped.type.HSTRING):
    def __del__(self):
        combase.WindowsDeleteString(self)

    @classmethod
    def from_string(cls, string: str = ''):
        self = cls()
        combase.WindowsCreateString(string, len(string), ctyped.byref(self))
        return self

    def get_string(self) -> str:
        return combase.WindowsGetStringRawBuffer(self, ctyped.NULLPTR)


class HBRUSH(ctyped.type.HBRUSH):
    def __del__(self):
        gdi32.DeleteObject(self)

    @classmethod
    def from_rgb(cls, r: int = 0, g: int = 0, b: int = 0) -> HBRUSH:
        return cls(gdi32.CreateSolidBrush(ctyped.macro.RGB(r, g, b)))

    @classmethod
    def from_color(cls, index: int) -> HBRUSH:
        return cls(user32.GetSysColorBrush(index))

    def get_rgb(self) -> _Optional[tuple[int, int, int]]:
        brush = ctyped.struct.LOGBRUSH()
        if gdi32.GetObjectW(self, ctyped.sizeof(brush), ctyped.byref(brush)):
            return ctyped.macro.GetRValue(brush.lbColor), ctyped.macro.GetGValue(
                brush.lbColor), ctyped.macro.GetBValue(brush.lbColor)


class HDC(ctyped.type.HDC):
    _hwnd = None
    _selected = None

    def __del__(self):
        user32.ReleaseDC(self._hwnd, self)
        if self._selected:
            gdi32.SelectObject(self, self._selected)
            gdi32.DeleteDC(self)

    @classmethod
    def from_hwnd(cls, hwnd: _Optional[ctyped.type.HWND] = None) -> HDC:
        return cls(user32.GetDC(hwnd))

    @classmethod
    def from_hbitmap(cls, hbitmap: ctyped.type.HBITMAP) -> HDC:
        self = cls(gdi32.CreateCompatibleDC(None))
        self._selected = gdi32.SelectObject(self, hbitmap.value)
        return self


class HCURSOR(ctyped.type.HCURSOR):
    def __del__(self):
        user32.DestroyCursor(self)

    @classmethod
    def from_idc(cls, idc: int, hinstance: _Optional[ctyped.type.HINSTANCE] = None) -> HCURSOR:
        return cls(user32.LoadCursorW(hinstance, ctyped.macro.MAKEINTRESOURCEW(idc)))


class HICON(ctyped.type.HICON):
    def __del__(self):
        user32.DestroyIcon(self)

    @classmethod
    def from_idi(cls, idi: int, hinstance: _Optional[ctyped.type.HINSTANCE] = None) -> HICON:
        return cls(user32.LoadIconW(hinstance, ctyped.macro.MAKEINTRESOURCEW(idi)))


class HBITMAP(ctyped.type.HBITMAP):
    _width = None
    _height = None

    def __del__(self):
        gdi32.DeleteObject(self.value)

    @property
    def width(self) -> int:
        if self._width is None:
            self._fill_dimensions()
        return self._width

    @property
    def height(self) -> int:
        if self._height is None:
            self._fill_dimensions()
        return self._height

    @classmethod
    def from_dimension(cls, width: int = 0, height: int = 0, byte: int = 4) -> HBITMAP:
        return cls(gdi32.CreateBitmap(width, height, 1, byte * 8, None))

    def _fill_dimensions(self):
        bitmap = ctyped.struct.BITMAP()
        if not gdi32.GetObjectW(self, ctyped.sizeof(ctyped.struct.BITMAP), ctyped.byref(bitmap)):
            self._width = bitmap.bmWidth
            self._height = bitmap.bmHeight

    def get_hdc(self) -> HDC:
        return HDC.from_hbitmap(self)


class HMENU(ctyped.type.HMENU):
    _hwnd = None

    def __del__(self):
        user32.DestroyMenu(self)

    @classmethod
    def from_type(cls, popup: bool = True) -> HMENU:
        return cls(user32.CreatePopupMenu() if popup else user32.CreateMenu())

    @classmethod
    def from_hwnd(cls, hwnd: ctyped.type.HWND, system: bool = False) -> HMENU:
        self = cls(user32.GetSystemMenu(hwnd, False) if system else user32.GetMenu(hwnd))
        self._hwnd = hwnd
        return self

    @classmethod
    def from_idm(cls, idm: int, hinstance: _Optional[ctyped.type.HINSTANCE] = None) -> HMENU:
        return cls(user32.LoadMenuW(hinstance, ctyped.macro.MAKEINTRESOURCEW(idm)))

    def set_hwnd(self, hwnd: ctyped.type.HWND) -> bool:
        self._hwnd = hwnd
        return bool(user32.SetMenu(hwnd, self))

    def get_item_count(self) -> int:
        return user32.GetMenuItemCount(self)

    def delete_item(self, id_or_pos: int, by_pos: bool = False) -> bool:
        return bool(user32.DeleteMenu(self, id_or_pos, _HMENU_MF[by_pos]))

    def remove_item(self, id_or_pos: int, by_pos: bool = False) -> bool:
        return bool(user32.RemoveMenu(self, id_or_pos, _HMENU_MF[by_pos]))

    def get_item_id(self, pos: int) -> bool:
        return bool(user32.GetMenuItemID(self, pos))

    def get_item_state(self, id_or_pos: int, by_pos: bool = False) -> int:
        return user32.GetMenuState(self, id_or_pos, _HMENU_MF[by_pos])

    def get_item_string(self, id_or_pos: int, by_pos: bool = False) -> str:
        sz = user32.GetMenuStringW(self, id_or_pos, None, 0, _HMENU_MF[by_pos]) + 1
        buff = ctyped.type.LPWSTR('\0' * sz)
        user32.GetMenuStringW(self, id_or_pos, buff, sz, _HMENU_MF[by_pos])
        return buff.value

    def get_item_submenu(self, pos: int) -> HMENU:
        return type(self)(user32.GetSubMenu(self, pos))

    def enable_item(self, id_or_pos: int, enable: bool = True, gray: bool = True, by_pos: bool = False) -> bool:
        return bool(user32.EnableMenuItem(self, id_or_pos, _HMENU_MF[by_pos] | (
            ctyped.const.MF_ENABLED if enable else (ctyped.const.MF_GRAYED if gray else ctyped.const.MF_DISABLED))))

    def check_item(self, id_or_pos: int, check: bool = True, by_pos: bool = False) -> bool:
        return bool(user32.CheckMenuItem(self, id_or_pos, _HMENU_MF[by_pos] | (
            ctyped.const.MF_CHECKED if check else ctyped.const.MF_UNCHECKED)))

    def set_default_item(self, id_or_pos: int, by_pos: bool = False) -> bool:
        return bool(user32.SetMenuDefaultItem(self, id_or_pos, by_pos))

    def set_item_bitmaps(self, id_or_pos: int, checked: _Optional[ctyped.type.HBITMAP] = None,
                         unchecked: _Optional[ctyped.type.HBITMAP] = None, by_pos: bool = False) -> bool:
        return bool(user32.SetMenuItemBitmaps(self, id_or_pos, _HMENU_MF[by_pos], checked, unchecked))

    def check_radio_item(self, id_or_pos: int, id_or_pos_first: int, id_or_pos_last: int, by_pos: bool = False) -> bool:
        return bool(user32.CheckMenuRadioItem(
            self, id_or_pos_first, id_or_pos_last, id_or_pos, _HMENU_MF[by_pos]))

    def track(self, x: int, y: int, alignment: int = ctyped.const.TPM_LEFTALIGN | ctyped.const.TPM_TOPALIGN,
              right_button: bool = False, animation: int = ctyped.const.TPM_NOANIMATION) -> int:
        user32.SetForegroundWindow(self._hwnd)
        return user32.TrackPopupMenu(self, alignment | (
            ctyped.const.TPM_RIGHTBUTTON if right_button else
            ctyped.const.TPM_LEFTBUTTON) | animation, x, y, 0, self._hwnd, None)

    def untrack(self) -> bool:
        return not user32.SendMessageW(self._hwnd, ctyped.const.WM_CANCELMODE, 0, 0)


class HRGN(ctyped.type.HRGN):
    def __del__(self):
        gdi32.DeleteObject(self)

    @classmethod
    def from_corners(cls, x1: int, y1: int, x2: int, y2: int) -> HRGN:
        return cls(gdi32.CreateRectRgn(x1, y1, x2, y2))

    @classmethod
    def from_rect(cls, rect: ctyped.struct.RECT) -> HRGN:
        return cls(gdi32.CreateRectRgnIndirect(ctyped.byref(rect)))

    @classmethod
    def from_combination(cls, self: ctyped.type.HRGN, other: ctyped.type.HRGN, mode: int = ctyped.const.RGN_OR) -> HRGN:
        hrgn = cls.from_corners(0, 0, 0, 0)
        gdi32.CombineRgn(hrgn, self, other, mode)
        return hrgn

    def get_rect(self) -> ctyped.struct.RECT:
        rect = ctyped.struct.RECT()
        gdi32.GetRgnBox(self, ctyped.byref(rect))
        return rect

    def is_empty(self) -> bool:
        return bool(user32.IsRectEmpty(ctyped.byref(self.get_rect())))

    def is_equal(self, other: ctyped.type.HRGN) -> bool:
        return bool(gdi32.EqualRgn(self, other))


class HWND(ctyped.type.HWND):
    def __del__(self):
        user32.DestroyWindow(self)

    def is_visible(self) -> bool:
        return bool(user32.IsWindowVisible(self))

    def send_message(self, msg: int, wparam: int = 0, lparam: int = 0, wait: bool = True) -> int:
        return (user32.SendMessageW if wait else user32.PostMessageW)(self, msg, wparam, lparam)

    def show(self, cmd: int = ctyped.const.SW_SHOW) -> bool:
        return bool(user32.ShowWindow(self, cmd))

    def update(self) -> bool:
        return bool(user32.UpdateWindow(self))

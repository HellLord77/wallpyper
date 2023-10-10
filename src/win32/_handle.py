from __future__ import annotations as _

from typing import Optional

from libs import ctyped
from libs.ctyped.lib import combase
from libs.ctyped.lib import gdi32
from libs.ctyped.lib import user32

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
        return combase.WindowsGetStringRawBuffer(self, ctyped.Pointer.NULL)


class HBRUSH(ctyped.type.HBRUSH):
    def __del__(self):
        gdi32.DeleteObject(self)

    @classmethod
    def from_stock(cls, index: int) -> HBRUSH:
        return cls(gdi32.GetStockObject(index))

    @classmethod
    def from_rgb(cls, r: int = 0, g: int = 0, b: int = 0) -> HBRUSH:
        return cls(gdi32.CreateSolidBrush(ctyped.macro.RGB(r, g, b)))

    @classmethod
    def from_color(cls, index: int) -> HBRUSH:
        return cls(user32.GetSysColorBrush(index))

    def get_rgb(self) -> Optional[tuple[int, int, int]]:
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
    def from_hwnd(cls, hwnd: Optional[ctyped.type.HWND] = None) -> HDC:
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
    def from_idc(cls, idc: int, hinstance: Optional[ctyped.type.HINSTANCE] = None) -> HCURSOR:
        return cls(user32.LoadCursorW(hinstance, ctyped.macro.MAKEINTRESOURCEW(idc)))

    def set(self) -> bool:
        return bool(user32.SetCursor(self))


class HICON(ctyped.type.HICON):
    def __del__(self):
        user32.DestroyIcon(self)

    @classmethod
    def from_idi(cls, idi: int, hinstance: Optional[ctyped.type.HINSTANCE] = None) -> HICON:
        return cls(user32.LoadIconW(hinstance, ctyped.macro.MAKEINTRESOURCEW(idi)))


class HBITMAP(ctyped.type.HBITMAP):
    def __del__(self):
        gdi32.DeleteObject(self.value)

    @classmethod
    def from_dimension(cls, width: int = 0, height: int = 0, byte: int = 4) -> HBITMAP:
        return cls(gdi32.CreateBitmap(width, height, 1, byte * 8, None))

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
    def from_idm(cls, idm: int, hinstance: Optional[ctyped.type.HINSTANCE] = None) -> HMENU:
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

    def set_item_bitmaps(self, id_or_pos: int, checked: Optional[ctyped.type.HBITMAP] = None,
                         unchecked: Optional[ctyped.type.HBITMAP] = None, by_pos: bool = False) -> bool:
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

    @classmethod
    def from_child(cls, child: ctyped.type.HWND) -> HWND:
        return cls(user32.GetParent(child))

    # noinspection PyShadowingBuiltins
    def get_message(self, msg_ref: ctyped.Pointer[ctyped.struct.MSG],
                    min: int = 0, max: int = 0, remove: bool = True) -> int:
        try:
            return user32.GetMessageW(msg_ref, self, min, max)
        finally:
            if remove:
                user32.TranslateMessage(msg_ref)
                user32.DispatchMessageW(msg_ref)

    def send_message(self, msg: int, wparam: int = 0, lparam: int = 0, wait: bool = True) -> int:
        return (user32.SendMessageW if wait else user32.PostMessageW)(self, msg, wparam, lparam)

    def show(self, cmd: int = ctyped.const.SW_SHOW, wait: bool = True) -> bool:
        return bool((user32.ShowWindow if wait else user32.ShowWindowAsync)(self, cmd))

    def flash(self, flash: bool = True) -> bool:
        return bool(user32.FlashWindow(self, flash))

    def open_icon(self) -> bool:
        return bool(user32.OpenIcon(self))

    def close(self) -> bool:
        return bool(user32.CloseWindow(self))

    def _get_x_y_cx_cy(self, x: Optional[int], y: Optional[int], cx: Optional[int], cy: Optional[int]) -> tuple[int, int, int, int]:
        if None in (x, y, cx, cy):
            rect = self.get_rect()
            if x is None:
                x = rect.left
            if y is None:
                y = rect.top
            if cx is None:
                cx = rect.right - rect.left
            if cy is None:
                cy = rect.bottom - rect.top
        return x, y, cx, cy

    def move(self, x: Optional[int] = None, y: Optional[int] = None,
             cx: Optional[int] = None, cy: Optional[int] = None, repaint: bool = True) -> bool:
        return bool(user32.MoveWindow(self, *self._get_x_y_cx_cy(x, y, cx, cy), repaint))

    def set_pos(self, x: Optional[int] = None, y: Optional[int] = None,
                cx: Optional[int] = None, cy: Optional[int] = None, flags: int = 0) -> bool:
        return bool(user32.SetWindowPos(self, 0, *self._get_x_y_cx_cy(x, y, cx, cy), flags))

    def is_visible(self) -> bool:
        return bool(user32.IsWindowVisible(self))

    def is_iconic(self) -> bool:
        return bool(user32.IsIconic(self))

    def bring_to_top(self) -> bool:
        return bool(user32.BringWindowToTop(self))

    def is_zoomed(self) -> bool:
        return bool(user32.IsZoomed(self))

    def update(self) -> bool:
        return bool(user32.UpdateWindow(self))

    def set_active(self) -> bool:
        return bool(user32.SetActiveWindow(self))

    def set_foreground(self) -> bool:
        return bool(user32.SetForegroundWindow(self))

    def invalidate_rect(self, rect: Optional[ctyped.Pointer[ctyped.struct.RECT]] = None, erase: bool = True) -> bool:
        return bool(user32.InvalidateRect(self, rect, erase))

    def invalidate_region(self, region: Optional[ctyped.type.HRGN] = None, erase: bool = True) -> bool:
        return bool(user32.InvalidateRgn(self, region, erase))

    def set_title(self, title: Optional[str] = None) -> bool:
        return bool(user32.SetWindowTextW(self, title))

    def get_client_rect(self) -> ctyped.struct.RECT:
        rect = ctyped.struct.RECT()
        user32.GetClientRect(self, ctyped.byref(rect))
        return rect

    def get_rect(self) -> ctyped.struct.RECT:
        rect = ctyped.struct.RECT()
        user32.GetWindowRect(self, ctyped.byref(rect))
        return rect

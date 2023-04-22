import functools
import ntpath
from typing import Optional

from libs import ctyped
from libs.ctyped.lib import gdi32, user32
from . import _gdiplus, _handle, gui


class ImageWindow:
    _w = 0
    _h = 0
    _dx = 0
    _dy = 0
    _dst_x = 0
    _dst_y = 0
    _zoom = 100
    _panning = False

    def __init__(self, path: str, title: Optional[str] = None,
                 width: int = ctyped.const.CW_USEDEFAULT, height: int = ctyped.const.CW_USEDEFAULT,
                 pan_cursor_idc: int = ctyped.const.IDC_SIZEALL, bg_color_rgb_or_index: int | tuple[
                int, int, int] = ctyped.const.COLOR_WINDOW, topmost: bool = False):
        bitmap = _gdiplus.Bitmap.from_file(path)
        self._src_hdc = bitmap.get_hbitmap().get_hdc()
        self._src_w = bitmap.get_width()
        self._src_h = bitmap.get_height()
        self._title = ntpath.basename(path) if title is None else path
        self._window = gui.Window(self._title, width=width, height=height,
                                  ex_style=topmost * ctyped.const.WS_EX_TOPMOST)
        self._cur_pan = _handle.HCURSOR.from_idc(pan_cursor_idc)
        if isinstance(bg_color_rgb_or_index, tuple):
            self._brush_bg = _handle.HBRUSH.from_rgb(*bg_color_rgb_or_index)
        else:
            self._brush_bg = _handle.HBRUSH.from_color(bg_color_rgb_or_index)
        self._pan_pos = ctyped.struct.POINT()
        self.show = self._window.show
        self._window.bind(gui.WindowEvent.SIZE, self._on_size)
        self._window.bind(gui.WindowEvent.PAINT, self._on_paint)
        self._window.bind(gui.WindowEvent.MOUSE_MOVE, self._on_mouse_move)
        self._window.bind(gui.WindowEvent.MOUSE_LEFT_DOWN, self._on_mouse_left_down)
        self._window.bind(gui.WindowEvent.MOUSE_LEFT_UP, self._on_drag_stop)
        self._window.bind(gui.WindowEvent.MOUSE_LEFT_DOUBLE, self._on_mouse_left_double)
        self._window.bind(gui.WindowEvent.MOUSE_WHEEL_FORWARD, self._on_mouse_wheel)
        self._window.bind(gui.WindowEvent.MOUSE_WHEEL_BACKWARD,
                          functools.partial(self._on_mouse_wheel, out=True))

    def _on_size(self, event: gui.Event):
        self._w = ctyped.macro.LOWORD(event.params[1])
        self._h = ctyped.macro.HIWORD(event.params[1])

    def _on_paint(self, _: gui.Event):
        scale = min(self._w / self._src_w, self._h / self._src_h) * self._zoom / 100
        src_w = self._src_w * scale
        src_h = self._src_h * scale
        dst_x_ = round((self._w - src_w) / 2)
        dst_x = dst_x_ + self._dx
        dst_y_ = round((self._h - src_h) / 2)
        dst_y = dst_y_ + self._dy
        dst_w = round(src_w)
        dst_h = round(src_h)
        if dst_x > 0:
            dst_x = 0
        elif dst_x + dst_w < self._w:
            dst_x = self._w - dst_w
        if dst_w - dst_x < self._w:
            dst_x = dst_x_
        self._dst_x = dst_x
        self._dx = dst_x - dst_x_
        if dst_y > 0:
            dst_y = 0
        elif dst_y + dst_h < self._h:
            dst_y = self._h - dst_h
        if dst_h - dst_y < self._h:
            dst_y = dst_y_
        self._dst_y = dst_y
        self._dy = dst_y - dst_y_
        hrgn = _handle.HRGN.from_combination(_handle.HRGN.from_corners(
            0, 0, self._w, self._h), _handle.HRGN.from_corners(
            dst_x, dst_y, dst_x + dst_w, dst_y + dst_h), ctyped.const.RGN_DIFF)
        hdc = self._window.get_hdc()
        gdi32.SetStretchBltMode(hdc, ctyped.const.STRETCH_HALFTONE)
        gdi32.StretchBlt(hdc, dst_x, dst_y, dst_w, dst_h, self._src_hdc,
                         0, 0, self._src_w, self._src_h, ctyped.const.SRCCOPY)
        gdi32.FillRgn(hdc, hrgn, self._brush_bg)
        self._window.set_title(f'{self._title} ({round(scale * 100)}%)')

    def _on_mouse_move(self, _: gui.Event):
        if self._panning:
            cur_pos = ctyped.struct.POINT()
            user32.GetCursorPos(ctyped.byref(cur_pos))
            dx = cur_pos.x - self._pan_pos.x
            dy = cur_pos.y - self._pan_pos.y
            self._dx += dx
            self._dy += dy
            self._pan_pos = cur_pos
            self._on_paint(_)

    def _on_mouse_left_down(self, _: gui.Event):
        self._panning = True
        self._cur_pan.set()
        user32.SetCapture(self._window.get_id())
        user32.GetCursorPos(ctyped.byref(self._pan_pos))

    def _on_drag_stop(self, _: gui.Event):
        user32.ReleaseCapture()
        self._panning = False

    def _on_mouse_left_double(self, _: gui.Event):
        while self._zoom != 100:
            self._on_mouse_wheel(_, True)

    def _on_mouse_wheel(self, _: gui.Event, out: bool = False):
        dz = -1 if out else 1
        for zoom in range(self._zoom, max(100, min(500, round(
                (1 + dz / 10) * self._zoom))) + dz, dz):
            self._zoom = zoom
            self._on_paint(_)

    def get_window(self) -> gui.Window:
        return self._window

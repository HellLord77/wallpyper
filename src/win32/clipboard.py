import contextlib
from typing import ContextManager, Optional

import libs.ctyped as ctyped
from . import _gdiplus


@contextlib.contextmanager
def _global_memory(sz: ctyped.type.SIZE_T) -> ContextManager[tuple[ctyped.type.HGLOBAL, ctyped.type.LPVOID]]:
    handle = ctyped.lib.kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, sz)
    buff = None
    if handle:
        buff = ctyped.lib.kernel32.GlobalLock(handle)
    try:
        yield handle, buff
    finally:
        ctyped.lib.kernel32.GlobalUnlock(handle)


@contextlib.contextmanager
def _open_clipboard() -> ContextManager[None]:
    ctyped.lib.user32.OpenClipboard(None)
    try:
        yield
    finally:
        ctyped.lib.user32.CloseClipboard()


def _set_clipboard(format_: int, hglobal: ctyped.type.HGLOBAL):
    with _open_clipboard():
        ctyped.lib.user32.EmptyClipboard()
        ctyped.lib.user32.SetClipboardData(format_, hglobal)


def paste_text() -> str:
    with _open_clipboard():
        return ctyped.cast(ctyped.lib.user32.GetClipboardData(
            ctyped.const.CF_UNICODETEXT), ctyped.type.c_wchar_p).value or ''


def copy_text(text: str, quote: Optional[str] = None) -> bool:
    if quote:
        text = f'{quote}{text}{quote}'
    sz = (ctyped.lib.msvcrt.wcslen(text) + 1) * ctyped.sizeof(ctyped.type.c_wchar)
    handle = ctyped.lib.kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, sz)
    if handle:
        buff = ctyped.lib.kernel32.GlobalLock(handle)
        if buff:
            ctyped.lib.msvcrt.memmove(buff, text, sz)
            _set_clipboard(ctyped.const.CF_UNICODETEXT, handle)
    return text == paste_text()


def copy_image(path: str) -> bool:
    hbitmap = _gdiplus.Bitmap.from_file(path).get_hbitmap()
    bmp = ctyped.struct.BITMAP()
    if (sz_bmp := ctyped.sizeof(
            ctyped.struct.BITMAP)) == ctyped.lib.gdi32.GetObjectW(hbitmap.value, sz_bmp, ctyped.byref(bmp)):
        header = ctyped.struct.BITMAPINFOHEADER(
            biWidth=bmp.bmWidth, biHeight=bmp.bmHeight, biBitCount=bmp.bmBitsPixel, biCompression=ctyped.const.BI_RGB)
        sz = bmp.bmWidthBytes * bmp.bmHeight
        data = ctyped.array(type=ctyped.type.BYTE, size=sz)
        hdc = ctyped.handle.HDC.from_hwnd()
        if hdc and ctyped.lib.gdi32.GetDIBits(hdc, hbitmap, 0, header.biHeight, data, ctyped.cast(
                header, ctyped.struct.BITMAPINFO), ctyped.const.DIB_RGB_COLORS):
            sz_header = ctyped.sizeof(ctyped.struct.BITMAPINFOHEADER)
            with _global_memory(sz_header + sz) as (handle, buff):
                if buff:
                    ctyped.lib.msvcrt.memmove(buff, ctyped.byref(header), sz_header)
                    ctyped.lib.msvcrt.memmove(buff + sz_header, data, sz)
                    _set_clipboard(ctyped.const.CF_DIB, handle)
                    return True
    return False

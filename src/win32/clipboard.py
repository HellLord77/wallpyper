import contextlib
from typing import ContextManager, Optional

from libs import ctyped
from libs.ctyped.lib import kernel32, user32, gdi32, msvcrt
from . import _gdiplus, _handle


@contextlib.contextmanager
def _global_memory(sz: ctyped.type.SIZE_T) -> ContextManager[tuple[ctyped.type.HGLOBAL, ctyped.type.LPVOID]]:
    handle = kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, sz)
    buff = None
    if handle:
        buff = kernel32.GlobalLock(handle)
    try:
        yield handle, buff
    finally:
        kernel32.GlobalUnlock(handle)


@contextlib.contextmanager
def _open_clipboard() -> ContextManager[None]:
    user32.OpenClipboard(None)
    try:
        yield
    finally:
        user32.CloseClipboard()


def _set_clipboard(format_: int, hglobal: ctyped.type.HGLOBAL):
    with _open_clipboard():
        user32.EmptyClipboard()
        user32.SetClipboardData(format_, hglobal)


def paste_text() -> str:
    with _open_clipboard():
        return ctyped.cast(user32.GetClipboardData(
            ctyped.const.CF_UNICODETEXT), ctyped.type.c_wchar_p).value or ''


def copy_text(text: str, quote: Optional[str] = None) -> bool:
    if quote:
        text = f'{quote}{text}{quote}'
    sz = (msvcrt.wcslen(text) + 1) * ctyped.sizeof(ctyped.type.c_wchar)
    handle = kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, sz)
    if handle:
        buff = kernel32.GlobalLock(handle)
        if buff:
            msvcrt.memmove(buff, text, sz)
            _set_clipboard(ctyped.const.CF_UNICODETEXT, handle)
    return text == paste_text()


def copy_image(path: str) -> bool:
    hbitmap = _gdiplus.Bitmap.from_file(path).get_hbitmap()
    bmp = ctyped.struct.BITMAP()
    if (sz_bmp := ctyped.sizeof(
            ctyped.struct.BITMAP)) == gdi32.GetObjectW(hbitmap.value, sz_bmp, ctyped.byref(bmp)):
        header = ctyped.struct.BITMAPINFOHEADER(
            biWidth=bmp.bmWidth, biHeight=bmp.bmHeight, biBitCount=bmp.bmBitsPixel, biCompression=ctyped.const.BI_RGB)
        sz = bmp.bmWidthBytes * bmp.bmHeight
        data = ctyped.array(type=ctyped.type.BYTE, size=sz)
        hdc = _handle.HDC.from_hwnd()
        if hdc and gdi32.GetDIBits(hdc, hbitmap, 0, header.biHeight, data, ctyped.cast(
                header, ctyped.struct.BITMAPINFO), ctyped.const.DIB_RGB_COLORS):
            sz_header = ctyped.sizeof(ctyped.struct.BITMAPINFOHEADER)
            with _global_memory(sz_header + sz) as (handle, buff):
                if buff:
                    msvcrt.memmove(buff, ctyped.byref(header), sz_header)
                    msvcrt.memmove(buff + sz_header, data, sz)
                    _set_clipboard(ctyped.const.CF_DIB, handle)
                    return True
    return False

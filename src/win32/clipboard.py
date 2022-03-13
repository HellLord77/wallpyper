import contextlib
from typing import ContextManager, Optional

import libs.ctyped as ctyped
from . import _gdiplus


@contextlib.contextmanager
def _global_memory(sz: ctyped.type.SIZE_T) -> ContextManager[tuple[ctyped.type.HGLOBAL, ctyped.type.LPVOID]]:
    handle = ctyped.func.kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, sz)
    buff = None
    if handle:
        buff = ctyped.func.kernel32.GlobalLock(handle)
    try:
        yield handle, buff
    finally:
        ctyped.func.kernel32.GlobalUnlock(handle)


@contextlib.contextmanager
def _open_clipboard() -> ContextManager[None]:
    ctyped.func.user32.OpenClipboard(None)
    try:
        yield
    finally:
        ctyped.func.user32.CloseClipboard()


def _set_clipboard(format_: int, hglobal: ctyped.type.HGLOBAL):
    with _open_clipboard():
        ctyped.func.user32.EmptyClipboard()
        ctyped.func.user32.SetClipboardData(format_, hglobal)


def paste_text() -> str:
    with _open_clipboard():
        return ctyped.cast(ctyped.func.user32.GetClipboardData(
            ctyped.const.CF_UNICODETEXT), ctyped.type.c_wchar_p).value or ''


def copy_text(text: str, quote: Optional[str] = None) -> bool:
    if quote:
        text = f'{quote}{text}{quote}'
    sz = (ctyped.func.msvcrt.wcslen(text) + 1) * ctyped.sizeof(ctyped.type.c_wchar)
    handle = ctyped.func.kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, sz)
    if handle:
        buff = ctyped.func.kernel32.GlobalLock(handle)
        if buff:
            ctyped.func.msvcrt.memmove(buff, text, sz)
            _set_clipboard(ctyped.const.CF_UNICODETEXT, handle)
    return text == paste_text()


def copy_image(path: str) -> bool:
    hbitmap = _gdiplus.Bitmap.from_file(path).get_hbitmap()
    bm = ctyped.struct.BITMAP()
    if (sz_bi := ctyped.sizeof(ctyped.struct.BITMAP)) == ctyped.func.gdi32.GetObjectW(
            hbitmap, sz_bi, ctyped.byref(bm)):
        sz_bih = ctyped.sizeof(ctyped.struct.BITMAPINFOHEADER)
        bi = ctyped.struct.BITMAPINFOHEADER(sz_bih, bm.bmWidth, bm.bmHeight, 1, bm.bmBitsPixel, ctyped.const.BI_RGB)
        sz = bm.bmWidthBytes * bm.bmHeight
        data = ctyped.array(ctyped.type.BYTE, size=sz)
        hdc = ctyped.handle.HDC.from_hwnd()
        if hdc and ctyped.func.gdi32.GetDIBits(hdc, hbitmap, 0, bi.biHeight, data, ctyped.cast(
                bi, ctyped.struct.BITMAPINFO), ctyped.const.DIB_RGB_COLORS):
            with _global_memory(sz_bih + sz) as handle_buff:
                if handle_buff[1]:
                    ctyped.func.msvcrt.memmove(handle_buff[1], ctyped.byref(bi), sz_bih)
                    ctyped.func.msvcrt.memmove(handle_buff[1] + sz_bih, data, sz)
                    _set_clipboard(ctyped.const.CF_DIB, handle_buff[0])
                    return True
    return False

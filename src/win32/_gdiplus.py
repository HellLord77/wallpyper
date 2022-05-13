from __future__ import annotations as _

import os
from typing import Callable, Generator, Optional

import libs.ctyped as ctyped

_GdiPlus = ctyped.lib.GdiPlus
_GpStatus = ctyped.enum.GpStatus


class Color(int):
    def __str__(self):
        return f'#{self.get_red():02x}{self.get_green():02x}{self.get_blue():02x}{self.get_alpha():02x}'

    @classmethod
    def from_rgba(cls, r: int, g: int, b: int, a: int = 255) -> Color:
        return Color(ctyped.cast_int(b << ctyped.const.BlueShift, ctyped.type.ARGB) |
                     ctyped.cast_int(g << ctyped.const.GreenShift, ctyped.type.ARGB) |
                     ctyped.cast_int(r << ctyped.const.RedShift, ctyped.type.ARGB) |
                     ctyped.cast_int(a << ctyped.const.AlphaShift, ctyped.type.ARGB))

    @classmethod
    def from_colorref(cls, bgr: ctyped.type.COLORREF) -> Color:
        return cls.from_rgba(ctyped.macro.GetRValue(bgr), ctyped.macro.GetGValue(bgr), ctyped.macro.GetBValue(bgr))

    def get_alpha(self) -> int:
        return ctyped.cast_int(self >> ctyped.const.AlphaShift, ctyped.type.BYTE)

    def get_red(self) -> int:
        return ctyped.cast_int(self >> ctyped.const.RedShift, ctyped.type.BYTE)

    def get_green(self) -> int:
        return ctyped.cast_int(self >> ctyped.const.GreenShift, ctyped.type.BYTE)

    def get_blue(self) -> int:
        return ctyped.cast_int(self >> ctyped.const.BlueShift, ctyped.type.BYTE)

    def get_colorref(self) -> int:
        return ctyped.macro.RGB(self.get_red(), self.get_green(), self.get_blue())


class _GdiplusToken(ctyped.type.ULONG_PTR):
    count = 0

    def __init__(self):
        if not self.count:
            _GdiPlus.GdiplusStartup(ctyped.byref(self), ctyped.byref(ctyped.struct.GdiplusStartupInput()), None)
        type(self).count += 1

    def __del__(self):
        type(self).count -= 1
        if not self.count:
            _GdiPlus.GdiplusShutdown(self)


class _GdiplusBase:
    # noinspection PyMissingConstructor
    def __init__(self):
        self._token = _GdiplusToken()

    def __del__(self):
        if self:
            self._del()
            self.value = None
            self._token = None

    def __hash__(self):
        return id(self)

    def __enter__(self) -> _GdiplusBase:  # TODO typing.Self
        return self

    def __exit__(self, *_):
        self.__del__()

    def _del(self):
        raise NotImplementedError


class Graphics(_GdiplusBase, ctyped.type.GpGraphics):
    def _del(self):
        _GdiPlus.GdipDeleteGraphics(self)

    @classmethod
    def from_hdc(cls, hdc: ctyped.type.HDC) -> Graphics:
        self = cls()
        _GdiPlus.GdipCreateFromHDC(hdc, ctyped.byref(self))
        return self

    @classmethod
    def from_image(cls, image: ctyped.type.GpImage) -> Graphics:
        self = cls()
        _GdiPlus.GdipGetImageGraphicsContext(image, ctyped.byref(self))
        return self

    @staticmethod
    def _get_func(float_func: Callable, int_func: Callable, *numbers: Optional[float]) -> Callable:
        for number in numbers:
            if isinstance(number, float):
                return float_func
        return int_func

    def get_dpi_x(self) -> Optional[float]:
        dpi_x = ctyped.type.REAL()
        if _GpStatus.Ok == _GdiPlus.GdipGetDpiX(self, ctyped.byref(dpi_x)):
            return dpi_x.value

    def get_dpi_y(self) -> Optional[float]:
        dpi_y = ctyped.type.REAL()
        if _GpStatus.Ok == _GdiPlus.GdipGetDpiY(self, ctyped.byref(dpi_y)):
            return dpi_y.value

    def set_scale(self, scale_x: float = 1, scale_y: float = 1):
        _GdiPlus.GdipScaleWorldTransform(self, scale_x, scale_y, ctyped.enum.MatrixOrder.Prepend)

    def draw_image(self, src: Image, x: float = 0, y: float = 0):
        self._get_func(_GdiPlus.GdipDrawImage, _GdiPlus.GdipDrawImageI, x, y)(self, src, x, y)

    def draw_image_from_rect(self, src: Image, x: float = 0, y: float = 0, src_x: float = 0, src_y: float = 0,
                             src_w: Optional[float] = None, src_h: Optional[float] = None):
        self._get_func(_GdiPlus.GdipDrawImagePointRect, _GdiPlus.GdipDrawImagePointRectI, x, y,
                       src_x, src_y, src_w, src_h)(self, src, x, y, src_x, src_y,
                                                   src.get_width() if src_w is None else src_w,
                                                   src.get_height() if src_h is None else src_h,
                                                   ctyped.enum.GpUnit.Pixel)

    def draw_image_on_rect_from_rect(self, src: Image, x: float = 0, y: float = 0, w: Optional[float] = None,
                                     h: Optional[float] = None, src_x: float = 0, src_y: float = 0,
                                     src_w: Optional[float] = None, src_h: Optional[float] = None, alpha: float = 1):
        if src_w is None:
            src_w = src.get_width()
        if src_h is None:
            src_h = src.get_height()
        image_attrs = ImageAttributes.from_color_matrix(color_matrix_from_alpha(alpha))
        draw_abort = ctyped.type.DrawImageAbort()
        self._get_func(_GdiPlus.GdipDrawImageRectRect, _GdiPlus.GdipDrawImageRectRectI, x, y,
                       w, h, src_x, src_y, src_w, src_h)(
            self, src, x, y, src_w if w is None else w, src_h if h is None else h,
            src_x, src_y, src_w, src_h, ctyped.enum.GpUnit.Pixel, image_attrs, draw_abort, None)

    def fill_rect(self, brush: ctyped.type.GpBrush, x: float, y: float, width: float, height: float):
        _GdiPlus.GdipFillRectangle(self, brush, x, y, width, height)

    def fill_rect_with_color(self, color: ctyped.type.ARGB, x: float, y: float, width: float, height: float):
        self.fill_rect(SolidFill.from_color(color), x, y, width, height)


class Brush(_GdiplusBase, ctyped.type.GpBrush):
    def _del(self):
        _GdiPlus.GdipDeleteBrush(self)


class Pen(_GdiplusBase, ctyped.type.GpPen):
    def _del(self):
        _GdiPlus.GdipDeletePen(self)

    def get_color(self) -> ctyped.type.ARGB:
        color = ctyped.type.ARGB()
        _GdiPlus.GdipGetPenColor(self, ctyped.byref(color))
        return color.value

    def get_width(self) -> float:
        width = ctyped.type.REAL()
        _GdiPlus.GdipGetPenWidth(self, ctyped.byref(width))
        return width.value

    def set_color(self, color: ctyped.type.ARGB):
        _GdiPlus.GdipSetPenColor(self, color)

    def set_width(self, width: float):
        _GdiPlus.GdipSetPenWidth(self, width)


class SolidFill(Brush, ctyped.type.GpSolidFill):
    @classmethod
    def from_color(cls, color: ctyped.type.ARGB) -> SolidFill:
        self = cls()
        _GdiPlus.GdipCreateSolidFill(color, ctyped.byref(self))
        return self

    def get_color(self) -> ctyped.type.ARGB:
        color = ctyped.type.ARGB()
        _GdiPlus.GdipGetSolidFillColor(self, ctyped.byref(color))
        return color.value

    def set_color(self, color: ctyped.type.ARGB):
        _GdiPlus.GdipSetSolidFillColor(self, color)


class Image(_GdiplusBase, ctyped.type.GpImage):
    def _del(self):
        _GdiPlus.GdipDisposeImage(self)

    @classmethod
    def from_file(cls, path: str) -> Image:
        self = cls()
        _GdiPlus.GdipLoadImageFromFile(path, ctyped.byref(self))
        return self

    @staticmethod
    def _get_encoder_clsid(ext: str) -> Optional[ctyped.Pointer[ctyped.struct.CLSID]]:
        number = ctyped.type.UINT()
        size = ctyped.type.UINT()
        _GdiPlus.GdipGetImageEncodersSize(ctyped.byref(number), ctyped.byref(size))
        with ctyped.buffer(size.value) as buff:
            if buff:
                codec_info = ctyped.cast(buff, ctyped.struct.ImageCodecInfo)
                _GdiPlus.GdipGetImageEncoders(number, size, codec_info)
                for index in range(number.value):
                    if ext in codec_info[index].FilenameExtension:
                        return ctyped.byref(codec_info[index].Clsid)
        return None

    def _get_dimension_id(self) -> ctyped.Pointer[ctyped.struct.GUID]:
        count = ctyped.type.UINT()
        guid_ref = ctyped.byref(ctyped.struct.GUID())
        _GdiPlus.GdipImageGetFrameDimensionsCount(self, ctyped.byref(count))
        _GdiPlus.GdipImageGetFrameDimensionsList(self, guid_ref, count)
        return guid_ref

    def get_graphics(self) -> Graphics:
        return Graphics.from_image(self)

    def get_width(self) -> Optional[int]:
        width = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageWidth(self, ctyped.byref(width)):
            return width.value

    def get_height(self) -> Optional[int]:
        height = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageHeight(self, ctyped.byref(height)):
            return height.value

    def get_frame_count(self, dimension_id: Optional[ctyped.Pointer[ctyped.struct.GUID]] = None) -> int:
        count = ctyped.type.UINT()
        _GdiPlus.GdipImageGetFrameCount(
            self, self._get_dimension_id() if dimension_id is None else dimension_id, ctyped.byref(count))
        return count.value

    def get_pixel_format(self) -> int:
        pixel_format = ctyped.type.PixelFormat()
        _GdiPlus.GdipGetImagePixelFormat(self, ctyped.byref(pixel_format))
        return pixel_format.value

    def select_frame(self, index: int = 0, dimension_id: Optional[ctyped.Pointer[ctyped.struct.GUID]] = None) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipImageSelectActiveFrame(
            self, self._get_dimension_id() if dimension_id is None else dimension_id, index)

    def iter_frames(self) -> Generator[int, None, None]:
        dimension_id = self._get_dimension_id()
        for index in range(self.get_frame_count(dimension_id)):
            self.select_frame(index, dimension_id)
            yield index

    def get_property(self, tag: int) -> Optional[ctyped.Pointer]:
        size = ctyped.type.UINT()
        _GdiPlus.GdipGetPropertyItemSize(self, tag, ctyped.byref(size))
        with ctyped.buffer(size.value) as buff:
            if buff:
                property_item = ctyped.cast(buff, ctyped.struct.PropertyItem)
                _GdiPlus.GdipGetPropertyItem(self, tag, size, property_item)
                if property_item.contents.type == ctyped.const.PropertyTagTypeByte:
                    type_ = ctyped.type.c_byte
                elif property_item.contents.type == ctyped.const.PropertyTagTypeShort:
                    type_ = ctyped.type.c_ushort
                elif property_item.contents.type == ctyped.const.PropertyTagTypeLong:
                    type_ = ctyped.type.c_ulong
                elif property_item.contents.type == ctyped.const.PropertyTagTypeRational:
                    type_ = ctyped.struct.Rational
                elif property_item.contents.type == ctyped.const.PropertyTagTypeUndefined:
                    type_ = ctyped.type.c_byte
                elif property_item.contents.type == ctyped.const.PropertyTagTypeSLONG:
                    type_ = ctyped.type.c_long
                else:
                    type_ = ctyped.type.c_void_p
                return ctyped.cast(property_item.contents.value, ctyped.pointer(type_))

    def save(self, path: str, quality: int = 100) -> bool:
        if encoder := self._get_encoder_clsid(os.path.splitext(path)[1].upper()):
            quality_ = ctyped.type.LONG(quality)
            params = ctyped.struct.EncoderParameters(1, ctyped.array(ctyped.struct.EncoderParameter(
                ctyped.get_guid(ctyped.const.EncoderQuality), 1,
                ctyped.enum.EncoderParameterValueType.Long.value, ctyped.cast(quality_, ctyped.type.PVOID))))
            return _GpStatus.Ok == _GdiPlus.GdipSaveImageToFile(self, path, encoder, ctyped.byref(params))
        return False


class Bitmap(Image, ctyped.type.GpBitmap):
    @classmethod
    def from_dimension(cls, width: int, height: int,
                       pixel_format: ctyped.type.PixelFormat = ctyped.const.PixelFormat24bppRGB) -> Bitmap:
        self = cls()
        _GdiPlus.GdipCreateBitmapFromScan0(
            width, height, 0, pixel_format, None, ctyped.byref(self))
        return self

    @classmethod
    def from_file(cls, path: str) -> Bitmap:
        self = cls()
        _GdiPlus.GdipCreateBitmapFromFile(path, ctyped.byref(self))
        return self

    @classmethod
    def from_graphics(cls, width: int, height: int, graphics: ctyped.type.GpGraphics) -> Bitmap:
        self = cls()
        _GdiPlus.GdipCreateBitmapFromGraphics(width, height, graphics, ctyped.byref(self))
        return self

    def get_hicon(self) -> ctyped.handle.HICON:
        hicon = ctyped.handle.HICON()
        _GdiPlus.GdipCreateHICONFromBitmap(self, ctyped.byref(hicon))
        return hicon

    def get_hbitmap(self) -> ctyped.handle.HBITMAP:
        hbitmap = ctyped.handle.HBITMAP()
        _GdiPlus.GdipCreateHBITMAPFromBitmap(self, ctyped.byref(hbitmap), 0)
        return hbitmap

    def get_resized(self, width: Optional[int] = None, height: Optional[int] = None) -> Bitmap:
        width_ = self.get_width()
        height_ = self.get_height()
        bitmap = self.from_dimension(
            width_ if width is None else width, height_ if height is None else height, self.get_pixel_format())
        graphics = bitmap.get_graphics()
        graphics.set_scale(width / width_, height / height_)
        graphics.draw_image_from_rect(self)
        return bitmap

    def get_pixel(self, x: int, y: int) -> Optional[int]:
        argb = ctyped.type.ARGB()
        if _GpStatus.Ok == _GdiPlus.GdipBitmapGetPixel(self, x, y, ctyped.byref(argb)):
            return argb.value

    def set_pixel(self, x: int, y: int, argb: int) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipBitmapSetPixel(self, x, y, argb)

    def set_resolution(self, dpi_x: float, dpi_y: float) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipBitmapSetResolution(self, dpi_x, dpi_y)


class ImageAttributes(_GdiplusBase, ctyped.type.GpImageAttributes):
    def _del(self):
        _GdiPlus.GdipDisposeImageAttributes(self)

    @classmethod
    def from_color_matrix(cls, color_matrix: ctyped.struct.ColorMatrix) -> ImageAttributes:
        self = cls()
        _GdiPlus.GdipCreateImageAttributes(ctyped.byref(self))
        _GdiPlus.GdipSetImageAttributesColorMatrix(
            self, ctyped.enum.ColorAdjustType.Default, True,
            ctyped.byref(color_matrix), None, ctyped.enum.ColorMatrixFlags.Default)
        return self


def color_matrix_from_alpha(alpha: float = 1) -> ctyped.struct.ColorMatrix:
    self = ctyped.struct.ColorMatrix()
    for index in range(5):
        self.m[index][index] = 1
    self.m[3][3] = alpha
    return self

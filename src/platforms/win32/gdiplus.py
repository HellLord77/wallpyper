from __future__ import annotations as _

import contextlib
import os
from typing import Callable, Generator, NoReturn, Optional

import libs.ctyped as ctyped


class GdiplusError(RuntimeError):
    pass


def _check_status(status: Optional[ctyped.enum.GpStatus], func: Callable, _: tuple) -> Optional[NoReturn]:
    if status:
        raise GdiplusError(f'{status} from {func.__name__}')


ctyped.set_error_handler(ctyped.func.GdiPlus, _check_status)


class _GdiplusToken(ctyped.type.ULONG_PTR):
    def __init__(self):
        ctyped.func.GdiPlus.GdiplusStartup(ctyped.byref(self), ctyped.byref(ctyped.struct.GdiplusStartupInput()), None)

    def __del__(self):
        ctyped.func.GdiPlus.GdiplusShutdown(self)


class _GdiplusBase(ctyped.type.c_void_p):
    # noinspection PyMissingConstructor
    def __init__(self):
        self._token = _GdiplusToken()


class Graphics(_GdiplusBase):
    _dpi_x = None
    _dpi_y = None

    def __del__(self):
        with contextlib.suppress(GdiplusError):
            ctyped.func.GdiPlus.GdipDeleteGraphics(self)

    @property
    def dpi_x(self) -> float:
        if self._dpi_x is None:
            dpi_x = ctyped.type.REAL()
            ctyped.func.GdiPlus.GdipGetDpiX(self, ctyped.byref(dpi_x))
            self._dpi_x = dpi_x.value
        return self._dpi_x

    @property
    def dpi_y(self) -> float:
        if self._dpi_y is None:
            dpi_y = ctyped.type.REAL()
            ctyped.func.GdiPlus.GdipGetDpiY(self, ctyped.byref(dpi_y))
            self._dpi_y = dpi_y.value
        return self._dpi_y

    @classmethod
    def from_hdc(cls, hdc: ctyped.type.HDC) -> Graphics:
        self = cls()
        ctyped.func.GdiPlus.GdipCreateFromHDC(hdc, ctyped.byref(self))
        return self

    @classmethod
    def from_image(cls, image: ctyped.type.GpImage) -> Graphics:
        self = cls()
        ctyped.func.GdiPlus.GdipGetImageGraphicsContext(image, ctyped.byref(self))
        return self

    @staticmethod
    def _get_func(float_func: Callable, int_func: Callable, *numbers: Optional[float]) -> Callable:
        for number in numbers:
            if isinstance(number, float):
                return float_func
        return int_func

    def set_scale(self, scale_x: float = 1, scale_y: float = 1):
        ctyped.func.GdiPlus.GdipScaleWorldTransform(self, scale_x, scale_y, ctyped.enum.MatrixOrder.MatrixOrderPrepend)

    def draw_image(self, src: Image, x: float = 0, y: float = 0):
        self._get_func(ctyped.func.GdiPlus.GdipDrawImage, ctyped.func.GdiPlus.GdipDrawImageI, x, y)(self, src, x, y)

    def draw_image_from_rect(self, src: Image, x: float = 0, y: float = 0, src_x: float = 0, src_y: float = 0,
                             src_w: Optional[float] = None, src_h: Optional[float] = None):
        self._get_func(ctyped.func.GdiPlus.GdipDrawImagePointRect, ctyped.func.GdiPlus.GdipDrawImagePointRectI, x, y,
                       src_x, src_y, src_w, src_h)(self, src, x, y, src_x, src_y, src.width if src_w is None else src_w,
                                                   src.height if src_h is None else src_h, ctyped.enum.GpUnit.UnitPixel)

    def draw_image_on_rect_from_rect(self, src: Image, x: float = 0, y: float = 0, w: Optional[float] = None,
                                     h: Optional[float] = None, src_x: float = 0, src_y: float = 0,
                                     src_w: Optional[float] = None, src_h: Optional[float] = None, alpha: float = 1):
        if src_w is None:
            src_w = src.width
        if src_h is None:
            src_h = src.height
        image_attrs = ImageAttributes.from_color_matrix(color_matrix_from_alpha(alpha))
        draw_abort = ctyped.type.DrawImageAbort()
        self._get_func(ctyped.func.GdiPlus.GdipDrawImageRectRect, ctyped.func.GdiPlus.GdipDrawImageRectRectI, x, y,
                       w, h, src_x, src_y, src_w, src_h)(self, src, x, y, src_w if w is None else w,
                                                         src_h if h is None else h, src_x, src_y, src_w, src_h,
                                                         ctyped.enum.GpUnit.UnitPixel, image_attrs, draw_abort, None)

    def fill_rect(self, brush: ctyped.type.GpBrush, x: float, y: float, width: float, height: float):
        ctyped.func.GdiPlus.GdipFillRectangle(self, brush, x, y, width, height)

    def fill_rect_with_color(self, color: ctyped.type.ARGB, x: float, y: float, width: float, height: float):
        self.fill_rect(SolidFill.from_color(color), x, y, width, height)


class Brush(_GdiplusBase):
    def __del__(self):
        with contextlib.suppress(GdiplusError):
            ctyped.func.GdiPlus.GdipDeleteBrush(self)


class SolidFill(Brush):
    @classmethod
    def from_color(cls, color: ctyped.type.ARGB) -> SolidFill:
        self = cls()
        ctyped.func.GdiPlus.GdipCreateSolidFill(color, ctyped.byref(self))
        return self

    def get_color(self) -> ctyped.type.ARGB:
        color = ctyped.type.ARGB()
        ctyped.func.GdiPlus.GdipGetSolidFillColor(self, ctyped.byref(color))
        return color.value

    def set_color(self, color: ctyped.type.ARGB):
        ctyped.func.GdiPlus.GdipSetSolidFillColor(self, color)


class Image(_GdiplusBase):
    _width = None
    _height = None

    def __del__(self):
        with contextlib.suppress(GdiplusError):
            ctyped.func.GdiPlus.GdipDisposeImage(self)

    @property
    def width(self) -> int:
        if self._width is None:
            width = ctyped.type.UINT()
            ctyped.func.GdiPlus.GdipGetImageWidth(self, ctyped.byref(width))
            self._width = width.value
        return self._width

    @property
    def height(self) -> int:
        if self._height is None:
            height = ctyped.type.UINT()
            ctyped.func.GdiPlus.GdipGetImageHeight(self, ctyped.byref(height))
            self._height = height.value
        return self._height

    @classmethod
    def from_file(cls, path: str) -> Image:
        self = cls()
        ctyped.func.GdiPlus.GdipLoadImageFromFile(path, ctyped.byref(self))
        return self

    @classmethod
    def validate_file(cls, path: str) -> bool:
        try:
            cls.from_file(path)
        except GdiplusError:
            return False
        else:
            return True

    @staticmethod
    def _get_encoder_clsid(ext: str) -> Optional[ctyped.Pointer[ctyped.struct.CLSID]]:
        number = ctyped.type.UINT()
        size = ctyped.type.UINT()
        ctyped.func.GdiPlus.GdipGetImageEncodersSize(ctyped.byref(number), ctyped.byref(size))
        with ctyped.buffer(size.value) as buff:
            if buff:
                codec_info = ctyped.cast(buff, ctyped.struct.ImageCodecInfo)
                ctyped.func.GdiPlus.GdipGetImageEncoders(number, size, codec_info)
                for index in range(number.value):
                    if ext in codec_info[index].FilenameExtension:
                        return ctyped.byref(codec_info[index].Clsid)
        return None

    def _get_dimension_id(self) -> ctyped.Pointer[ctyped.struct.GUID]:
        count = ctyped.type.UINT()
        guid_ref = ctyped.byref(ctyped.struct.GUID())
        ctyped.func.GdiPlus.GdipImageGetFrameDimensionsCount(self, ctyped.byref(count))
        ctyped.func.GdiPlus.GdipImageGetFrameDimensionsList(self, guid_ref, count)
        return guid_ref

    def get_graphics(self) -> Graphics:
        return Graphics.from_image(self)

    def get_frame_count(self, _id: Optional[ctyped.Pointer[ctyped.struct.GUID]] = None) -> int:
        count = ctyped.type.UINT()
        ctyped.func.GdiPlus.GdipImageGetFrameCount(self, self._get_dimension_id() if _id is None else _id,
                                                   ctyped.byref(count))
        return count.value

    def select_frame(self, index: int = 0, _id: Optional[ctyped.Pointer[ctyped.struct.GUID]] = None) -> bool:
        return ctyped.enum.GpStatus.Ok == ctyped.func.GdiPlus.GdipImageSelectActiveFrame(
            self, self._get_dimension_id() if _id is None else _id, index)

    def iter_frames(self) -> Generator[str, None, None]:
        dimension_id = self._get_dimension_id()
        for index in range(self.get_frame_count(dimension_id)):
            self.select_frame(index, dimension_id)
            yield index

    def get_property(self, tag: int) -> Optional[ctyped.Pointer]:
        size = ctyped.type.UINT()
        ctyped.func.GdiPlus.GdipGetPropertyItemSize(self, tag, ctyped.byref(size))
        with ctyped.buffer(size.value) as buff:
            if buff:
                property_item = ctyped.cast(buff, ctyped.struct.PropertyItem)
                ctyped.func.GdiPlus.GdipGetPropertyItem(self, tag, size, property_item)
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
                return ctyped.pointer(type_).from_buffer(property_item.contents.value)

    def save(self, path: str) -> bool:
        if encoder := self._get_encoder_clsid(os.path.splitext(path)[1].upper()):
            return ctyped.enum.GpStatus.Ok == ctyped.func.GdiPlus.GdipSaveImageToFile(self, path, encoder, None)
        return False


class Bitmap(Image):
    @classmethod
    def from_dimension(cls, width: int, height: int,
                       pixel_format: ctyped.type.PixelFormat = ctyped.const.PixelFormat24bppRGB) -> Bitmap:
        self = cls()
        ctyped.func.GdiPlus.GdipCreateBitmapFromScan0(width, height, 0, pixel_format, None, ctyped.byref(self))
        return self

    @classmethod
    def from_file(cls, path: str) -> Bitmap:
        self = cls()
        ctyped.func.GdiPlus.GdipCreateBitmapFromFile(path, ctyped.byref(self))
        return self

    @classmethod
    def from_graphics(cls, width: int, height: int, graphics: ctyped.type.GpGraphics) -> Bitmap:
        self = cls()
        ctyped.func.GdiPlus.GdipCreateBitmapFromGraphics(width, height, graphics, ctyped.byref(self))
        return self

    def get_hicon(self) -> ctyped.handle.HICON:
        hicon = ctyped.handle.HICON()
        ctyped.func.GdiPlus.GdipCreateHICONFromBitmap(self, ctyped.byref(hicon))
        return hicon

    def get_hbitmap(self) -> ctyped.handle.HBITMAP:
        hbitmap = ctyped.handle.HBITMAP()
        ctyped.func.GdiPlus.GdipCreateHBITMAPFromBitmap(self, ctyped.byref(hbitmap), 0)
        return hbitmap

    def set_resolution(self, dpi_x: float, dpi_y: float):
        ctyped.func.GdiPlus.GdipBitmapSetResolution(self, dpi_x, dpi_y)


class ImageAttributes(_GdiplusBase):
    def __del__(self):
        with contextlib.suppress(GdiplusError):
            ctyped.func.GdiPlus.GdipDisposeImageAttributes(self)

    @classmethod
    def from_color_matrix(cls, color_matrix: ctyped.struct.ColorMatrix) -> ImageAttributes:
        self = cls()
        ctyped.func.GdiPlus.GdipCreateImageAttributes(ctyped.byref(self))
        ctyped.func.GdiPlus.GdipSetImageAttributesColorMatrix(self, ctyped.enum.ColorAdjustType.ColorAdjustTypeDefault,
                                                              True, ctyped.byref(color_matrix), None,
                                                              ctyped.enum.ColorMatrixFlags.ColorMatrixFlagsDefault)
        return self


def color_matrix_from_alpha(alpha: float = 1) -> ctyped.struct.ColorMatrix:
    self = ctyped.struct.ColorMatrix()
    for index in range(5):
        self.m[index][index] = 1
    self.m[3][3] = alpha
    return self

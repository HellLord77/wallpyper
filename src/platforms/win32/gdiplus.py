from __future__ import annotations as _

from typing import Generator, Optional

import libs.ctyped as ctyped


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
    def __del__(self):
        ctyped.func.GdiPlus.GdipDeleteGraphics(self)

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

    def set_scale(self, scale_x: float = 1, scale_y: float = 1):
        ctyped.func.GdiPlus.GdipScaleWorldTransform(self, scale_x, scale_y, ctyped.enum.MatrixOrder.MatrixOrderPrepend)

    def draw_image(self, image: Image, x: float = 0, y: float = 0, image_x: float = 0, image_y: float = 0,
                   image_width: Optional[float] = None, image_height: Optional[float] = None):
        ctyped.func.GdiPlus.GdipDrawImagePointRect(
            self, image, x, y, image_x, image_y, image.width if image_width is None else image_width,
            image.height if image_height is None else image_height, ctyped.enum.GpUnit.UnitPixel)

    def fill_rect(self, brush: ctyped.type.GpBrush, x: float, y: float, width: float, height: float):
        ctyped.func.GdiPlus.GdipFillRectangle(self, brush, x, y, width, height)

    def fill_rect_with_color(self, color: ctyped.type.ARGB, x: float, y: float, width: float, height: float):
        self.fill_rect(SolidFill.from_color(color), x, y, width, height)


class Brush(_GdiplusBase):
    def __del__(self):
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

    def get_hicon(self) -> ctyped.handle.HICON:
        hicon = ctyped.handle.HICON()
        ctyped.func.GdiPlus.GdipCreateHICONFromBitmap(self, ctyped.byref(hicon))
        return hicon

    def get_hbitmap(self) -> ctyped.handle.HBITMAP:
        hbitmap = ctyped.handle.HBITMAP()
        ctyped.func.GdiPlus.GdipCreateHBITMAPFromBitmap(self, ctyped.byref(hbitmap), 0)
        return hbitmap


class ImageAttributes(_GdiplusBase):
    def __del__(self):
        ctyped.func.GdiPlus.GdipDisposeImageAttributes(self)

    @classmethod
    def from_color_matrix(cls, color_matrix: ctyped.struct.ColorMatrix) -> ImageAttributes:
        self = cls()
        ctyped.func.GdiPlus.GdipCreateImageAttributes(ctyped.byref(self))
        ctyped.func.GdiPlus.GdipSetImageAttributesColorMatrix(self, ctyped.enum.ColorAdjustType.ColorAdjustTypeDefault,
                                                              True, ctyped.byref(color_matrix), None,
                                                              ctyped.enum.ColorMatrixFlags.ColorMatrixFlagsDefault)
        return self

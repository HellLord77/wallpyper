from __future__ import annotations as _

from typing import Optional

import libs.ctyped as ctyped


class _GdiPlus(ctyped.type.ULONG_PTR):
    def __init__(self):
        ctyped.func.GdiPlus.GdiplusStartup(ctyped.byref(self), ctyped.byref(ctyped.struct.GdiplusStartupInput()), None)

    def __del__(self):
        ctyped.func.GdiPlus.GdiplusShutdown(self)


class _GdiPlusBase(ctyped.type.c_void_p):
    # noinspection PyMissingConstructor
    def __init__(self):
        self._gdi_plus = _GdiPlus()


class GpGraphics(_GdiPlusBase):
    def __del__(self):
        ctyped.func.GdiPlus.GdipDeleteGraphics(self)

    @staticmethod
    def from_hdc(hdc: ctyped.type.HDC) -> GpGraphics:
        self = GpGraphics()
        ctyped.func.GdiPlus.GdipCreateFromHDC(hdc, ctyped.byref(self))
        return self

    @staticmethod
    def from_gp_image(gp_image: ctyped.type.GpImage) -> GpGraphics:
        self = GpGraphics()
        ctyped.func.GdiPlus.GdipGetImageGraphicsContext(gp_image, ctyped.byref(self))
        return self

    def set_scale(self, scale_x: float = 1, scale_y: float = 1):
        ctyped.func.GdiPlus.GdipScaleWorldTransform(self, scale_x, scale_y, ctyped.const.MatrixOrderPrepend)

    def draw_image(self, gp_image: GpImage, x: float = 0, y: float = 0, gp_image_x: float = 0, gp_image_y: float = 0,
                   gp_image_width: Optional[float] = None, gp_image_height: Optional[float] = None):
        ctyped.func.GdiPlus.GdipDrawImagePointRect(
            self, gp_image, x, y, gp_image_x, gp_image_y, gp_image.width if gp_image_width is None else gp_image_width,
            gp_image.height if gp_image_height is None else gp_image_height, ctyped.const.UnitPixel)

    def fill_rect(self, brush: ctyped.type.GpBrush, x: float, y: float, width: float, height: float):
        ctyped.func.GdiPlus.GdipFillRectangle(self, brush, x, y, width, height)

    def fill_rect_with_color(self, color: ctyped.type.ARGB, x: float, y: float, width: float, height: float):
        self.fill_rect(GpSolidFill.from_color(color), x, y, width, height)


class GpBrush(_GdiPlusBase):
    def __del__(self):
        ctyped.func.GdiPlus.GdipDeleteBrush(self)


class GpSolidFill(GpBrush):
    @staticmethod
    def from_color(color: ctyped.type.ARGB) -> GpSolidFill:
        self = GpSolidFill()
        ctyped.func.GdiPlus.GdipCreateSolidFill(color, ctyped.byref(self))
        return self

    def get_color(self) -> ctyped.type.ARGB:
        color = ctyped.type.ARGB()
        ctyped.func.GdiPlus.GdipGetSolidFillColor(self, ctyped.byref(color))
        return color.value

    def set_color(self, color: ctyped.type.ARGB):
        ctyped.func.GdiPlus.GdipSetSolidFillColor(self, color)


class GpImage(_GdiPlusBase):
    _width = None
    _height = None
    _gp_graphics = None

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

    @property
    def gp_graphics(self) -> GpGraphics:
        if self._gp_graphics is None:
            self._gp_graphics = GpGraphics.from_gp_image(self)
        return self._gp_graphics

    @gp_graphics.deleter
    def gp_graphics(self):
        self._gp_graphics = None

    @staticmethod
    def from_file(path: str) -> GpImage:
        self = GpImage()
        ctyped.func.GdiPlus.GdipLoadImageFromFile(path, ctyped.byref(self))
        return self


class GpBitmap(GpImage):
    _hicon = None
    _hbitmap = None

    @property
    def hicon(self) -> ctyped.handle.HICON:
        if self._hicon is None:
            hicon = ctyped.handle.HICON()
            ctyped.func.GdiPlus.GdipCreateHICONFromBitmap(self, ctyped.byref(hicon))
            self._hicon = hicon
        return self._hicon

    @hicon.deleter
    def hicon(self):
        self._hicon = None

    @property
    def hbitmap(self) -> ctyped.handle.HBITMAP:
        if self._hbitmap is None:
            hbitmap = ctyped.handle.HBITMAP()
            ctyped.func.GdiPlus.GdipCreateHBITMAPFromBitmap(self, ctyped.byref(hbitmap), 0)
            self._hbitmap = hbitmap
        return self._hbitmap

    @hbitmap.deleter
    def hbitmap(self):
        self._hbitmap = None

    @staticmethod
    def from_dimension(width: int, height: int,
                       pixel_format: ctyped.type.PixelFormat = ctyped.const.PixelFormat24bppRGB) -> GpBitmap:
        self = GpBitmap()
        ctyped.func.GdiPlus.GdipCreateBitmapFromScan0(width, height, 0, pixel_format, None, ctyped.byref(self))
        return self

    @staticmethod
    def from_file(path: str) -> GpBitmap:
        self = GpBitmap()
        ctyped.func.GdiPlus.GdipCreateBitmapFromFile(path, ctyped.byref(self))
        return self


class GpImageAttributes(_GdiPlusBase):
    def __del__(self):
        ctyped.func.GdiPlus.GdipDisposeImageAttributes(self)

    @staticmethod
    def from_color_matrix(color_matrix: ctyped.struct.ColorMatrix) -> GpImageAttributes:
        self = GpImageAttributes()
        ctyped.func.GdiPlus.GdipCreateImageAttributes(ctyped.byref(self))
        ctyped.func.GdiPlus.GdipSetImageAttributesColorMatrix(self, ctyped.const.ColorAdjustTypeDefault, True,
                                                              ctyped.byref(color_matrix), None,
                                                              ctyped.const.ColorMatrixFlagsDefault)
        return self

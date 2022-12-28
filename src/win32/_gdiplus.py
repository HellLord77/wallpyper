from __future__ import annotations as _

import contextlib
import math
import ntpath
import string as _string
from typing import Callable, ContextManager, Generator, Literal, Optional

from libs import ctyped
from libs.ctyped.interface.um import d2d1_3, d2d1svg, objidlbase
from . import _utils

_GdiPlus = ctyped.lib.GdiPlus
_GpStatus = ctyped.enum.GpStatus


def _get_obj(float_obj: Callable, int_obj: Callable, *numbers: Optional[int | float]) -> Callable:
    for number in numbers:
        if isinstance(number, float):
            return float_obj
    return int_obj


def _calc_src_x_y_w_h(from_w: int, from_h: int, to_w: int, to_h: int,
                      by_h: bool = True) -> tuple[float, float, float, float]:
    ratio = to_w / to_h
    if by_h:
        w = from_h * ratio
        return (from_w - w) / 2, 0, w, from_h
    else:
        h = from_w / ratio
        return 0, (from_h - h) / 2, from_w, h


class _GdiplusToken(ctyped.type.ULONG_PTR):
    count = 0

    def __init__(self):
        if not self.count:
            _GdiPlus.GdiplusStartup(ctyped.byref(self), ctyped.byref(ctyped.struct.GdiplusStartupInput()), None)
        _GdiplusToken.count += 1

    def __del__(self):
        _GdiplusToken.count -= 1
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

    def __enter__(self) -> _GdiplusBase:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__del__()

    def _del(self):
        raise NotImplementedError


class Graphics(_GdiplusBase, ctyped.type.GpGraphics):
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

    def flush(self, intention: ctyped.enum.FlushIntention = ctyped.enum.FlushIntention.Flush) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipFlush(self, intention)

    def get_hdc(self) -> Optional[ctyped.type.HDC]:
        hdc = ctyped.type.HDC()
        if _GpStatus.Ok == _GdiPlus.GdipGetDC(self, ctyped.byref(hdc)):
            return hdc

    def release_hdc(self, hdc: ctyped.type.HDC) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipReleaseDC(self, hdc)

    def set_rendering_origin(self, x: int, y: int) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetRenderingOrigin(self, x, y)

    def get_rendering_origin(self) -> Optional[tuple[int, int]]:
        x = ctyped.type.INT()
        y = ctyped.type.INT()
        if _GpStatus.Ok == _GdiPlus.GdipGetRenderingOrigin(self, ctyped.byref(x), ctyped.byref(y)):
            return x.value, y.value

    def set_composting_mode(self, mode: ctyped.enum.CompositingMode) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetCompositingMode(self, mode)

    def get_composting_mode(self) -> Optional[ctyped.enum.CompositingMode]:
        mode = ctyped.enum.CompositingMode()
        if _GpStatus.Ok == _GdiPlus.GdipGetCompositingMode(self, ctyped.byref(mode)):
            return mode

    def set_compositing_quality(self, quality: ctyped.enum.CompositingQuality) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetCompositingQuality(self, quality)

    def get_compositing_quality(self) -> Optional[ctyped.enum.CompositingQuality]:
        quality = ctyped.enum.CompositingQuality()
        if _GpStatus.Ok == _GdiPlus.GdipGetCompositingQuality(self, ctyped.byref(quality)):
            return quality

    def set_text_rendering_hint(self, mode: ctyped.enum.TextRenderingHint) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetTextRenderingHint(self, mode)

    def get_text_rendering_hint(self) -> Optional[ctyped.enum.TextRenderingHint]:
        mode = ctyped.enum.TextRenderingHint()
        if _GpStatus.Ok == _GdiPlus.GdipGetTextRenderingHint(self, ctyped.byref(mode)):
            return mode

    def set_text_contrast(self, contrast: int) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetTextContrast(self, contrast)

    def get_text_contrast(self) -> Optional[int]:
        contrast = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetTextContrast(self, ctyped.byref(contrast)):
            return contrast.value

    def get_interpolation_mode(self) -> Optional[ctyped.enum.InterpolationMode]:
        mode = ctyped.enum.InterpolationMode()
        if _GpStatus.Ok == _GdiPlus.GdipGetInterpolationMode(self, ctyped.byref(mode)):
            return mode

    def set_interpolation_mode(self, mode: ctyped.enum.InterpolationMode) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetInterpolationMode(self, mode)

    def get_smoothing_mode(self) -> Optional[ctyped.enum.SmoothingMode]:
        mode = ctyped.enum.SmoothingMode()
        if _GpStatus.Ok == _GdiPlus.GdipGetSmoothingMode(self, ctyped.byref(mode)):
            return mode

    def set_smoothing_mode(self, mode: ctyped.enum.SmoothingMode) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetSmoothingMode(self, mode)

    def get_pixel_offset_mode(self) -> Optional[ctyped.enum.PixelOffsetMode]:
        mode = ctyped.enum.PixelOffsetMode()
        if _GpStatus.Ok == _GdiPlus.GdipGetPixelOffsetMode(self, ctyped.byref(mode)):
            return mode

    def set_pixel_offset_mode(self, mode: ctyped.enum.PixelOffsetMode) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPixelOffsetMode(self, mode)

    def set_transform(self, matrix: ctyped.type.GpMatrix) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetWorldTransform(self, matrix)

    def reset_transform(self) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipResetWorldTransform(self)

    def multiply_transform(self, matrix: ctyped.type.GpMatrix,
                           order: ctyped.enum.MatrixOrder = ctyped.enum.MatrixOrder.Prepend) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipMultiplyWorldTransform(self, matrix, order)

    def translate_transform(self, dx: float, dy: float,
                            order: ctyped.enum.MatrixOrder = ctyped.enum.MatrixOrder.Prepend) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipTranslateWorldTransform(self, dx, dy, order)

    def scale_transform(self, sx: float, sy: float,
                        order: ctyped.enum.MatrixOrder = ctyped.enum.MatrixOrder.Prepend) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipScaleWorldTransform(self, sx, sy, order)

    def rotate_transform(self, angle: float,
                         order: ctyped.enum.MatrixOrder = ctyped.enum.MatrixOrder.Prepend) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipRotateWorldTransform(self, angle, order)

    def set_page_unit(self, unit: ctyped.enum.Unit) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPageUnit(self, unit)

    def set_page_scale(self, scale: float) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPageScale(self, scale)

    def get_page_unit(self) -> Optional[ctyped.enum.Unit]:
        unit = ctyped.enum.Unit()
        if _GpStatus.Ok == _GdiPlus.GdipGetPageUnit(self, ctyped.byref(unit)):
            return unit

    def get_page_scale(self) -> Optional[float]:
        scale = ctyped.type.FLOAT()
        if _GpStatus.Ok == _GdiPlus.GdipGetPageScale(self, ctyped.byref(scale)):
            return scale.value

    def get_dpi_x(self) -> Optional[float]:
        dpi = ctyped.type.FLOAT()
        if _GpStatus.Ok == _GdiPlus.GdipGetDpiX(self, ctyped.byref(dpi)):
            return dpi.value

    def get_dpi_y(self) -> Optional[float]:
        dpi = ctyped.type.FLOAT()
        if _GpStatus.Ok == _GdiPlus.GdipGetDpiY(self, ctyped.byref(dpi)):
            return dpi.value

    def get_nearest_color(self, color: ctyped.type.ARGB) -> Optional[Color]:
        argb = ctyped.type.ARGB(color)
        if _GpStatus.Ok == _GdiPlus.GdipGetNearestColor(self, ctyped.byref(argb)):
            return Color(argb.value)

    def draw_line(self, pen: ctyped.type.GpPen, x1: int | float, y1: int | float, x2: int | float, y2: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(
            _GdiPlus.GdipDrawLine, _GdiPlus.GdipDrawLineI, x1, y1, x2, y2)(self, pen, x1, y1, x2, y2)

    def draw_arc(self, pen: ctyped.type.GpPen, x: int | float, y: int | float, width: int | float, height: int | float,
                 start_angle: float, sweep_angle: float) -> bool:
        return _GpStatus.Ok == _get_obj(_GdiPlus.GdipDrawArc, _GdiPlus.GdipDrawArcI, x, y, width, height)(
            self, pen, x, y, width, height, start_angle, sweep_angle)

    def draw_bezier(self, pen: ctyped.type.GpPen, x1: int | float, y1: int | float, x2: int | float, y2: int | float,
                    x3: int | float, y3: int | float, x4: int | float, y4: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(
            _GdiPlus.GdipDrawBezier, _GdiPlus.GdipDrawBezierI, x1, y1, x2, y2, x3, y3, x4, y4)(
            self, pen, x1, y1, x2, y2, x3, y3, x4, y4)

    def draw_rectangle(self, pen: ctyped.type.GpPen, x: int | float, y: int | float, width: int | float, height: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(_GdiPlus.GdipDrawRectangle, _GdiPlus.GdipDrawRectangleI, x, y, width, height)(
            self, pen, x, y, width, height)

    def draw_ellipse(self, pen: ctyped.type.GpPen, x: int | float, y: int | float, width: int | float, height: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(_GdiPlus.GdipDrawEllipse, _GdiPlus.GdipDrawEllipseI, x, y, width, height)(
            self, pen, x, y, width, height)

    def draw_pie(self, pen: ctyped.type.GpPen, x: int | float, y: int | float, width: int | float, height: int | float,
                 start_angle: float, sweep_angle: float) -> bool:
        return _GpStatus.Ok == _get_obj(_GdiPlus.GdipDrawPie, _GdiPlus.GdipDrawPieI, x, y, width, height)(
            self, pen, x, y, width, height, start_angle, sweep_angle)

    def clear(self, color: ctyped.type.ARGB) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipGraphicsClear(self, color)

    def fill_rectangle(self, brush: ctyped.type.GpBrush, x: int | float, y: int | float, width: int | float, height: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(_GdiPlus.GdipFillRectangle, _GdiPlus.GdipFillRectangleI, x, y, width, height)(
            self, brush, x, y, width, height)

    def fill_ellipse(self, brush: ctyped.type.GpBrush, x: int | float, y: int | float, width: int | float, height: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(_GdiPlus.GdipFillEllipse, _GdiPlus.GdipFillEllipseI, x, y, width, height)(
            self, brush, x, y, width, height)

    def fill_pie(self, brush: ctyped.type.GpBrush, x: int | float, y: int | float, width: int | float, height: int | float,
                 start_angle: float, sweep_angle: float) -> bool:
        return _GpStatus.Ok == _get_obj(_GdiPlus.GdipFillPie, _GdiPlus.GdipFillPieI, x, y, width, height)(
            self, brush, x, y, width, height, start_angle, sweep_angle)

    # noinspection PyShadowingBuiltins
    def draw_string(self, string: str, font: ctyped.type.GpFont, brush: ctyped.type.GpBrush,
                    x: float = 0, y: float = 0, width: float = 0, height: float = 0,
                    format: Optional[ctyped.type.GpStringFormat] = None) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipDrawString(self, string, -1, font, ctyped.byref(
            ctyped.struct.RectF(x, y, width, height)), format, brush)

    # noinspection PyShadowingBuiltins
    def measure_string(self, string: str, font: ctyped.type.GpFont, x: float = 0, y: float = 0, width: float = 0, height: float = 0,
                       format: Optional[ctyped.type.GpStringFormat] = None) -> Optional[tuple[tuple[float, float, float, float], int, int]]:
        rect = ctyped.struct.RectF()
        codepoints = ctyped.type.INT()
        lines = ctyped.type.INT()
        if _GpStatus.Ok == _GdiPlus.GdipMeasureString(self, string, -1, font, ctyped.byref(ctyped.struct.RectF(
                x, y, width, height)), format, ctyped.byref(rect), ctyped.byref(codepoints), ctyped.byref(lines)):
            return (rect.X, rect.Y, rect.Width, rect.Height), codepoints.value, lines.value

    # noinspection PyShadowingBuiltins
    def measure_character_ranges(self, string: str, font: ctyped.type.GpFont, count: int, x: float = 0, y: float = 0,
                                 width: float = ctyped.const.FLT_MAX, height: float = ctyped.const.FLT_MAX,
                                 format: Optional[ctyped.type.GpStringFormat] = None) -> Optional[tuple[Region]]:
        regions = tuple(Region.from_empty() for _ in range(count))
        rect = ctyped.struct.RectF(x, y, width, height)
        if _GpStatus.Ok == _GdiPlus.GdipMeasureCharacterRanges(
                self, string, -1, font, ctyped.byref(rect), format, count, ctyped.array(*regions)):
            return regions

    def draw_image(self, src: Image, x: int | float = 0, y: int | float = 0) -> bool:
        return _GpStatus.Ok == _get_obj(_GdiPlus.GdipDrawImage, _GdiPlus.GdipDrawImageI, x, y)(self, src, x, y)

    def _del(self):
        _GdiPlus.GdipDeleteGraphics(self)

    @contextlib.contextmanager
    def get_managed_hdc(self) -> ContextManager[ctyped.type.HDC]:
        hdc = self.get_hdc()
        try:
            yield hdc
        finally:
            if hdc:
                self.release_hdc(hdc)

    def draw_image_from_rect(self, src: Image, x: int | float = 0, y: int | float = 0, src_x: int | float = 0, src_y: int | float = 0,
                             src_w: Optional[int | float] = None, src_h: Optional[int | float] = None) -> bool:
        if src_w is None:
            src_w = src.get_width()
        if src_h is None:
            src_h = src.get_height()
        return _GpStatus.Ok == _get_obj(_GdiPlus.GdipDrawImagePointRect, _GdiPlus.GdipDrawImagePointRectI, x, y, src_x, src_y, src_w, src_h)(
            self, src, x, y, src_x, src_y, src_w, src_h, ctyped.enum.GpUnit.Pixel)

    def draw_image_on_rect_from_rect(self, src: Image, x: int | float = 0, y: int | float = 0, w: Optional[int | float] = None,
                                     h: Optional[int | float] = None, src_x: int | float = 0, src_y: int | float = 0,
                                     src_w: Optional[int | float] = None, src_h: Optional[int | float] = None, alpha: float = 1) -> bool:
        if src_w is None:
            src_w = src.get_width()
        if src_h is None:
            src_h = src.get_height()
        if w is None:
            w = src_w
        if h is None:
            h = src_h
        image_attrs = image_attributes_from_alpha(alpha)
        draw_abort = ctyped.type.DrawImageAbort()
        return _GpStatus.Ok == _get_obj(_GdiPlus.GdipDrawImageRectRect, _GdiPlus.GdipDrawImageRectRectI, x, y,
                                        w, h, src_x, src_y, src_w, src_h)(
            self, src, x, y, w, h, src_x, src_y, src_w, src_h, ctyped.enum.GpUnit.Pixel, image_attrs, draw_abort, None)


class Brush(_GdiplusBase, ctyped.type.GpBrush):
    @classmethod
    def from_brush(cls, brush: ctyped.type.GpBrush) -> Brush:
        self = cls()
        _GdiPlus.GdipCloneBrush(brush, ctyped.byref(self))
        return self

    def get_type(self) -> Optional[ctyped.enum.BrushType]:
        brush_type = ctyped.enum.BrushType()
        if _GpStatus.Ok == _GdiPlus.GdipGetBrushType(self, ctyped.byref(brush_type)):
            return brush_type

    def _del(self):
        _GdiPlus.GdipDeleteBrush(self)


class SolidBrush(Brush, ctyped.type.GpSolidFill):
    @classmethod
    def from_color(cls, color: ctyped.type.ARGB) -> SolidBrush:
        self = cls()
        _GdiPlus.GdipCreateSolidFill(color, ctyped.byref(self))
        return self

    def get_color(self) -> Optional[Color]:
        argb = ctyped.type.ARGB()
        if _GpStatus.Ok == _GdiPlus.GdipGetSolidFillColor(self, ctyped.byref(argb)):
            return Color(argb.value)

    def set_color(self, color: ctyped.type.ARGB) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetSolidFillColor(self, color)


class Pen(_GdiplusBase, ctyped.type.GpPen):
    @classmethod
    def from_color(cls, color: ctyped.type.ARGB, width: float = 1,
                   unit: ctyped.enum.GpUnit = ctyped.enum.GpUnit.Pixel) -> Pen:
        self = cls()
        _GdiPlus.GdipCreatePen1(color, width, unit, ctyped.byref(self))
        return self

    @classmethod
    def from_brush(cls, brush: ctyped.type.GpBrush, width: float = 1,
                   unit: ctyped.enum.Unit = ctyped.enum.Unit.World) -> Pen:
        self = cls()
        _GdiPlus.GdipCreatePen2(brush, width, unit, ctyped.byref(self))
        return self

    @classmethod
    def from_pen(cls, pen: ctyped.type.GpPen) -> Pen:
        self = cls()
        _GdiPlus.GdipClonePen(pen, ctyped.byref(self))
        return self

    def set_width(self, width: float) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenWidth(self, width)

    def get_width(self) -> Optional[float]:
        width = ctyped.type.REAL()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenWidth(self, ctyped.byref(width)):
            return width.value

    def set_line_cap(self, start_cap: ctyped.enum.LineCap,
                     end_cap: ctyped.enum.LineCap, dash_cap: ctyped.enum.DashCap) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenLineCap197819(self, start_cap, end_cap, dash_cap)

    def set_start_cap(self, cap: ctyped.enum.LineCap) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenStartCap(self, cap)

    def set_end_cap(self, cap: ctyped.enum.LineCap) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenEndCap(self, cap)

    def set_dash_cap(self, cap: ctyped.enum.DashCap) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenDashCap197819(self, cap)

    def get_start_cap(self) -> Optional[ctyped.enum.LineCap]:
        start_cap = ctyped.enum.LineCap()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenStartCap(self, ctyped.byref(start_cap)):
            return start_cap

    def get_end_cap(self) -> Optional[ctyped.enum.LineCap]:
        end_cap = ctyped.enum.LineCap()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenEndCap(self, ctyped.byref(end_cap)):
            return end_cap

    def get_dash_cap(self) -> Optional[ctyped.enum.DashCap]:
        dash_cap = ctyped.enum.DashCap()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenDashCap197819(self, ctyped.byref(dash_cap)):
            return dash_cap

    def set_line_join(self, join: ctyped.enum.LineJoin) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenLineJoin(self, join)

    def get_line_join(self) -> Optional[ctyped.enum.LineJoin]:
        line_join = ctyped.enum.LineJoin()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenLineJoin(self, ctyped.byref(line_join)):
            return line_join

    def set_custom_start_cap(self, cap: ctyped.type.GpCustomLineCap):
        return _GpStatus.Ok == _GdiPlus.GdipSetPenCustomStartCap(self, cap)

    def set_custom_end_cap(self, cap: ctyped.type.GpCustomLineCap):
        return _GpStatus.Ok == _GdiPlus.GdipSetPenCustomEndCap(self, cap)

    def set_miter_limit(self, limit: float) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenMiterLimit(self, limit)

    def get_miter_limit(self) -> Optional[float]:
        miter_limit = ctyped.type.REAL()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenMiterLimit(self, ctyped.byref(miter_limit)):
            return miter_limit.value

    def set_alignment(self, align: ctyped.enum.PenAlignment) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenMode(self, align)

    def get_alignment(self) -> Optional[ctyped.enum.PenAlignment]:
        pen_alignment = ctyped.enum.PenAlignment()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenMode(self, ctyped.byref(pen_alignment)):
            return pen_alignment

    def set_transform(self, matrix: ctyped.type.GpMatrix) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenTransform(self, matrix)

    def reset_transform(self) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipResetPenTransform(self)

    def multiply_transform(self, matrix: ctyped.type.GpMatrix,
                           order: ctyped.enum.MatrixOrder = ctyped.enum.MatrixOrder.Prepend) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipMultiplyPenTransform(self, matrix, order)

    def translate_transform(self, dx: float, dy: float,
                            order: ctyped.enum.MatrixOrder = ctyped.enum.MatrixOrder.Prepend) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipTranslatePenTransform(self, dx, dy, order)

    def scale_transform(self, sx: float, sy: float,
                        order: ctyped.enum.MatrixOrder = ctyped.enum.MatrixOrder.Prepend) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipScalePenTransform(self, sx, sy, order)

    def rotate_transform(self, angle: float,
                         order: ctyped.enum.MatrixOrder = ctyped.enum.MatrixOrder.Prepend) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipRotatePenTransform(self, angle, order)

    def get_pen_type(self) -> Optional[ctyped.enum.PenType]:
        pen_type = ctyped.enum.PenType()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenFillType(self, ctyped.byref(pen_type)):
            return pen_type

    def set_color(self, color: ctyped.type.ARGB) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenColor(self, color)

    def set_brush(self, brush: ctyped.type.GpBrush) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenBrushFill(self, brush)

    def get_color(self) -> Optional[Color]:
        color = ctyped.type.ARGB()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenColor(self, ctyped.byref(color)):
            return Color(color.value)

    def get_dash_style(self) -> Optional[ctyped.enum.DashStyle]:
        dash_style = ctyped.enum.DashStyle()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenDashStyle(self, ctyped.byref(dash_style)):
            return dash_style

    def set_dash_style(self, style: ctyped.enum.DashStyle) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenDashStyle(self, style)

    def get_dash_offset(self) -> Optional[float]:
        dash_offset = ctyped.type.REAL()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenDashOffset(self, ctyped.byref(dash_offset)):
            return dash_offset.value

    def set_dash_offset(self, offset: float) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetPenDashOffset(self, offset)

    def get_dash_pattern_count(self) -> Optional[int]:
        dash_pattern_count = ctyped.type.INT()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenDashCount(self, ctyped.byref(dash_pattern_count)):
            return dash_pattern_count.value

    def get_compound_array_count(self) -> Optional[int]:
        compound_array_count = ctyped.type.INT()
        if _GpStatus.Ok == _GdiPlus.GdipGetPenCompoundCount(self, ctyped.byref(compound_array_count)):
            return compound_array_count.value

    def _del(self):
        _GdiPlus.GdipDeletePen(self)


class Image(_GdiplusBase, ctyped.type.GpImage):
    @classmethod
    def from_file(cls, path: str, embedded_color_management: bool = False) -> Image:
        self = cls()
        (_GdiPlus.GdipLoadImageFromFileICM if embedded_color_management else _GdiPlus.GdipLoadImageFromFile)(
            path, ctyped.byref(self))
        return self

    @classmethod
    def from_bytes(cls, data: bytes, embedded_color_management: bool = False) -> Image:
        self = cls()
        if stream := ctyped.lib.shlwapi.SHCreateMemStream(ctyped.array(*data, type=ctyped.type.BYTE), len(data)):
            (_GdiPlus.GdipLoadImageFromStreamICM if embedded_color_management else _GdiPlus.GdipLoadImageFromStream)(
                stream, ctyped.byref(self))
            stream.Release()
        return self

    @classmethod
    def from_image(cls, image: ctyped.type.GpImage) -> Image:
        self = cls()
        _GdiPlus.GdipCloneImage(image, ctyped.byref(self))
        return self

    def get_encoder_parameters_size(self, encoder: ctyped.struct.CLSID) -> Optional[int]:
        size = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetEncoderParameterListSize(self, ctyped.byref(encoder), ctyped.byref(size)):
            return size.value

    def save_to_file(self, path: str, encoder: ctyped.struct.CLSID,
                     encoder_params: ctyped.struct.EncoderParameters) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSaveImageToFile(
            self, path, ctyped.byref(encoder), ctyped.byref(encoder_params))

    def save_to_stream(self, stream: objidlbase.IStream, encoder: ctyped.struct.CLSID,
                       encoder_params: ctyped.struct.EncoderParameters) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSaveImageToStream(
            self, stream, ctyped.byref(encoder), ctyped.byref(encoder_params))

    def get_type(self) -> Optional[ctyped.enum.ImageType]:
        image_type = ctyped.enum.ImageType()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageType(self, ctyped.byref(image_type)):
            return image_type

    def get_physical_dimension(self) -> Optional[tuple[float, float]]:
        width = ctyped.type.REAL()
        height = ctyped.type.REAL()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageDimension(self, ctyped.byref(width), ctyped.byref(height)):
            return width.value, height.value

    def get_bounds(self) -> Optional[tuple[tuple[float, float, float, float], ctyped.enum.Unit]]:
        rect = ctyped.struct.RectF()
        unit = ctyped.enum.Unit()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageBounds(self, ctyped.byref(rect), ctyped.byref(unit)):
            return (rect.X, rect.Y, rect.Width, rect.Height), unit

    def get_width(self) -> Optional[int]:
        width = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageWidth(self, ctyped.byref(width)):
            return width.value

    def get_height(self) -> Optional[int]:
        height = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageHeight(self, ctyped.byref(height)):
            return height.value

    def get_horizontal_resolution(self) -> Optional[float]:
        resolution = ctyped.type.REAL()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageHorizontalResolution(self, ctyped.byref(resolution)):
            return resolution.value

    def get_vertical_resolution(self) -> Optional[float]:
        resolution = ctyped.type.REAL()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageVerticalResolution(self, ctyped.byref(resolution)):
            return resolution.value

    def get_flags(self) -> Optional[int]:
        flags = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageFlags(self, ctyped.byref(flags)):
            return flags.value

    def get_pixel_format(self) -> Optional[int]:
        pixel_format = ctyped.type.PixelFormat()
        if _GpStatus.Ok == _GdiPlus.GdipGetImagePixelFormat(self, ctyped.byref(pixel_format)):
            return pixel_format.value

    def get_palette_size(self) -> Optional[int]:
        palette_size = ctyped.type.INT()
        if _GpStatus.Ok == _GdiPlus.GdipGetImagePaletteSize(self, ctyped.byref(palette_size)):
            return palette_size.value

    def get_palette(self, size: int) -> Optional[ctyped.struct.ColorPalette]:
        palette = ctyped.struct.ColorPalette()
        if _GpStatus.Ok == _GdiPlus.GdipGetImagePalette(self, ctyped.byref(palette), size):
            return palette

    def set_palette(self, palette: ctyped.struct.ColorPalette) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImagePalette(self, ctyped.byref(palette))

    def get_thumbnail(self, width: int = 0, height: int = 0) -> Optional[Image]:
        image = Image()
        image_abort = ctyped.type.GetThumbnailImageAbort()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageThumbnail(self, width, height, ctyped.byref(image), image_abort, None):
            return image

    def get_frame_dimensions_count(self) -> Optional[int]:
        count = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipImageGetFrameDimensionsCount(self, ctyped.byref(count)):
            return count.value

    def get_frame_dimensions(self, count: int = 1) -> Optional[tuple[ctyped.struct.GUID]]:
        dimensions = ctyped.array(type=ctyped.struct.GUID, size=count)
        if _GpStatus.Ok == _GdiPlus.GdipImageGetFrameDimensionsList(self, dimensions, count):
            return tuple(dimensions)

    def get_frame_count(self, dimension: ctyped.struct.GUID) -> Optional[int]:
        count = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipImageGetFrameCount(self, ctyped.byref(dimension), ctyped.byref(count)):
            return count.value

    def select_active_frame(self, dimension: ctyped.struct.GUID, index: int = 0) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipImageSelectActiveFrame(self, ctyped.byref(dimension), index)

    # noinspection PyShadowingBuiltins
    def rotate_flip(self, type: ctyped.enum.RotateFlipType) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipImageRotateFlip(self, type)

    def get_property_count(self) -> Optional[int]:
        count = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetPropertyCount(self, ctyped.byref(count)):
            return count.value

    # noinspection PyShadowingBuiltins
    def get_property_item_size(self, id: ctyped.type.PROPID) -> Optional[int]:
        size = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetPropertyItemSize(self, id, ctyped.byref(size)):
            return size.value

    # noinspection PyShadowingBuiltins
    @contextlib.contextmanager
    def get_property_item(self, id: ctyped.type.PROPID,
                          size: Optional[int] = None) -> ContextManager[Optional[ctyped.struct.PropertyItem]]:
        if size is None:
            size = self.get_property_item_size(id)
        if size is not None:
            with ctyped.buffer(size) as buffer:
                if buffer:
                    property_item_ref = ctyped.cast(buffer, ctyped.struct.PropertyItem)
                    if _GpStatus.Ok == _GdiPlus.GdipGetPropertyItem(self, id, size, property_item_ref):
                        yield property_item_ref.contents
                        return
        yield

    def get_property_size_and_count(self) -> Optional[tuple[int, int]]:
        size = ctyped.type.UINT()
        count = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetPropertySize(self, ctyped.byref(size), ctyped.byref(count)):
            return size.value, count.value

    # noinspection PyShadowingBuiltins
    def remove_property_item(self, id: ctyped.type.PROPID) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipRemovePropertyItem(self, id)

    def force_validation(self) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipImageForceValidation(self)

    def _del(self):
        _GdiPlus.GdipDisposeImage(self)


class Bitmap(Image, ctyped.type.GpBitmap):
    @classmethod
    def from_file(cls, path: str, embedded_color_management: bool = False) -> Bitmap:
        self = cls()
        (_GdiPlus.GdipCreateBitmapFromFileICM if embedded_color_management else _GdiPlus.GdipCreateBitmapFromFile)(
            path, ctyped.byref(self))
        return self

    @classmethod
    def from_bytes(cls, data: bytes, embedded_color_management: bool = False) -> Bitmap:
        self = cls()
        if stream := ctyped.lib.shlwapi.SHCreateMemStream(ctyped.array(*data, type=ctyped.type.BYTE), len(data)):
            (_GdiPlus.GdipCreateBitmapFromStreamICM if embedded_color_management else _GdiPlus.GdipCreateBitmapFromStream)(
                stream, ctyped.byref(self))
            stream.Release()
        return self

    # noinspection PyShadowingBuiltins
    @classmethod
    def from_dimension(cls, width: int, height: int,
                       format: ctyped.type.PixelFormat = ctyped.const.PixelFormat24bppRGB) -> Bitmap:
        self = cls()
        _GdiPlus.GdipCreateBitmapFromScan0(width, height, 0, format, None, ctyped.byref(self))
        return self

    @classmethod
    def from_graphics(cls, width: int, height: int, graphics: ctyped.type.GpGraphics) -> Bitmap:
        self = cls()
        _GdiPlus.GdipCreateBitmapFromGraphics(width, height, graphics, ctyped.byref(self))
        return self

    @classmethod
    def from_hicon(cls, hicon: ctyped.type.HICON) -> Bitmap:
        self = cls()
        _GdiPlus.GdipCreateBitmapFromHICON(hicon, ctyped.byref(self))
        return self

    # noinspection PyShadowingBuiltins
    @classmethod
    def from_bitmap(cls, bitmap: ctyped.type.GpBitmap, x: int | float = 0, y: int | float = 0,
                    width: Optional[int | float] = None, height: Optional[int | float] = None,
                    format: ctyped.type.PixelFormat = ctyped.const.PixelFormat24bppRGB) -> Bitmap:
        if width is None:
            # noinspection PyTypeChecker
            width = Image.get_width(bitmap)
        if height is None:
            # noinspection PyTypeChecker
            height = Image.get_height(bitmap)
        self = cls()
        _get_obj(_GdiPlus.GdipCloneBitmapArea, _GdiPlus.GdipCloneBitmapAreaI, x, y, width, height)(
            x, y, width, height, format, bitmap, ctyped.byref(self))
        return self

    def get_hbitmap(self) -> Optional[ctyped.handle.HBITMAP]:
        hbitmap = ctyped.type.HBITMAP()
        if _GpStatus.Ok == _GdiPlus.GdipCreateHBITMAPFromBitmap(self, ctyped.byref(hbitmap), 0):
            return ctyped.handle.HBITMAP(hbitmap.value)

    def get_hicon(self) -> Optional[ctyped.handle.HICON]:
        hicon = ctyped.type.HICON()
        if _GpStatus.Ok == _GdiPlus.GdipCreateHICONFromBitmap(self, ctyped.byref(hicon)):
            return ctyped.handle.HICON(hicon.value)

    def get_pixel(self, x: int, y: int) -> Optional[Color]:
        argb = ctyped.type.ARGB()
        if _GpStatus.Ok == _GdiPlus.GdipBitmapGetPixel(self, x, y, ctyped.byref(argb)):
            return Color(argb.value)

    def set_pixel(self, x: int, y: int, color: ctyped.type.ARGB) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipBitmapSetPixel(self, x, y, color.value)

    def set_resolution(self, x_dpi: float, y_dpi: float) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipBitmapSetResolution(self, x_dpi, y_dpi)


class ImageAttributes(_GdiplusBase, ctyped.type.GpImageAttributes):
    @classmethod
    def from_empty(cls) -> ImageAttributes:
        self = cls()
        _GdiPlus.GdipCreateImageAttributes(ctyped.byref(self))
        return self

    @classmethod
    def from_image_attributes(cls, attr: ctyped.type.GpImageAttributes) -> ImageAttributes:
        self = cls()
        _GdiPlus.GdipCloneImageAttributes(attr, ctyped.byref(self))
        return self

    # noinspection PyShadowingBuiltins
    def set_to_identity(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesToIdentity(self, type)

    # noinspection PyShadowingBuiltins
    def reset(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipResetImageAttributes(self, type)

    # noinspection PyShadowingBuiltins
    def set_color_matrix(self, matrix: ctyped.struct.ColorMatrix,
                         mode: ctyped.enum.ColorMatrixFlags = ctyped.enum.ColorMatrixFlags.Default,
                         type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesColorMatrix(
            self, type, True, ctyped.byref(matrix), None, mode)

    # noinspection PyShadowingBuiltins
    def clear_color_matrix(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesColorMatrix(
            self, type, False, None, None, ctyped.enum.ColorMatrixFlags.Default)

    # noinspection PyShadowingBuiltins
    def set_color_matrices(self, matrix: ctyped.struct.ColorMatrix, gray_matrix: ctyped.struct.ColorMatrix,
                           mode: ctyped.enum.ColorMatrixFlags = ctyped.enum.ColorMatrixFlags.Default,
                           type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesColorMatrix(
            self, type, True, ctyped.byref(matrix), ctyped.byref(gray_matrix), mode)

    # noinspection PyShadowingBuiltins
    def clear_color_matrices(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesColorMatrix(
            self, type, False, None, None, ctyped.enum.ColorMatrixFlags.Default)

    # noinspection PyShadowingBuiltins
    def set_threshold(self, threshold: float, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesThreshold(self, type, True, threshold)

    # noinspection PyShadowingBuiltins
    def clear_threshold(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesThreshold(self, type, False, 0)

    # noinspection PyShadowingBuiltins
    def set_gamma(self, gamma: float, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesGamma(self, type, True, gamma)

    # noinspection PyShadowingBuiltins
    def clear_gamma(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesGamma(self, type, False, 0)

    # noinspection PyShadowingBuiltins
    def set_noop(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesNoOp(self, type, True)

    # noinspection PyShadowingBuiltins
    def clear_noop(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesNoOp(self, type, False)

    # noinspection PyShadowingBuiltins
    def set_color_key(self, low: ctyped.type.ARGB, high: ctyped.type.ARGB,
                      type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesColorKeys(self, type, True, low, high)

    # noinspection PyShadowingBuiltins
    def clear_color_key(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesColorKeys(self, type, False, 0, 0)

    # noinspection PyShadowingBuiltins
    def set_output_channel(self, flags: ctyped.enum.ColorChannelFlags,
                           type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesOutputChannel(self, type, True, flags)

    # noinspection PyShadowingBuiltins
    def clear_output_channel(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesOutputChannel(
            self, type, False, ctyped.enum.ColorChannelFlags.Last)

    # noinspection PyShadowingBuiltins
    def set_output_channel_color_profile(self, path: str, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesOutputChannelColorProfile(self, type, True, path)

    # noinspection PyShadowingBuiltins
    def clear_output_channel_color_profile(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesOutputChannelColorProfile(self, type, False, None)

    # noinspection PyShadowingBuiltins
    def clear_remap_table(self, type: ctyped.enum.ColorAdjustType = ctyped.enum.ColorAdjustType.Default) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesRemapTable(self, type, False, 0, None)

    def clear_brush_remap_table(self) -> bool:
        return self.clear_remap_table(ctyped.enum.ColorAdjustType.Brush)

    def set_wrap_mode(self, mode: ctyped.enum.WrapMode, color: ctyped.type.ARGB = ctyped.const.Black, clamp: bool = False) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetImageAttributesWrapMode(self, mode, color, clamp)

    def _del(self):
        _GdiPlus.GdipDisposeImageAttributes(self)


class Region(_GdiplusBase, ctyped.type.GpRegion):
    @classmethod
    def from_empty(cls) -> Region:
        self = cls()
        _GdiPlus.GdipCreateRegion(ctyped.byref(self))
        return self

    @classmethod
    def from_rect(cls, x: int | float, y: int | float, width: int | float, height: int | float) -> Region:
        self = cls()
        _get_obj(_GdiPlus.GdipCreateRegionRect, _GdiPlus.GdipCreateRegionRectI, x, y, width, height)(
            ctyped.byref(self), ctyped.byref(_get_obj(
                ctyped.struct.RectF, ctyped.struct.Rect, x, y, width, height)(x, y, width, height)))
        return self

    @classmethod
    def from_hrgn(cls, hrgn: ctyped.type.HRGN) -> Region:
        self = cls()
        _GdiPlus.GdipCreateRegionHrgn(ctyped.byref(self), hrgn)
        return self

    @classmethod
    def from_region(cls, region: Region) -> Region:
        self = cls()
        _GdiPlus.GdipCloneRegion(region, ctyped.byref(self))
        return self

    def make_infinite(self) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetInfinite(self)

    def make_empty(self) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetEmpty(self)

    def intersect_rect(self, x: int | float, y: int | float, width: int | float, height: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(
            _GdiPlus.GdipCombineRegionRect, _GdiPlus.GdipCombineRegionRectI, x, y, width, height)(
            self, ctyped.byref(_get_obj(ctyped.struct.RectF, ctyped.struct.Rect, x, y, width, height)(
                x, y, width, height)), ctyped.enum.CombineMode.Intersect)

    def intersect_region(self, region: Region) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipCombineRegionRegion(self, region, ctyped.enum.CombineMode.Intersect)

    def union_rect(self, x: int | float, y: int | float, width: int | float, height: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(
            _GdiPlus.GdipCombineRegionRect, _GdiPlus.GdipCombineRegionRectI, x, y, width, height)(
            self, ctyped.byref(_get_obj(ctyped.struct.RectF, ctyped.struct.Rect, x, y, width, height)(
                x, y, width, height)), ctyped.enum.CombineMode.Union)

    def union_region(self, region: Region) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipCombineRegionRegion(self, region, ctyped.enum.CombineMode.Union)

    def xor_rect(self, x: int | float, y: int | float, width: int | float, height: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(
            _GdiPlus.GdipCombineRegionRect, _GdiPlus.GdipCombineRegionRectI, x, y, width, height)(
            self, ctyped.byref(_get_obj(ctyped.struct.RectF, ctyped.struct.Rect, x, y, width, height)(
                x, y, width, height)), ctyped.enum.CombineMode.Xor)

    def xor_region(self, region: Region) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipCombineRegionRegion(self, region, ctyped.enum.CombineMode.Xor)

    def exclude_rect(self, x: int | float, y: int | float, width: int | float, height: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(
            _GdiPlus.GdipCombineRegionRect, _GdiPlus.GdipCombineRegionRectI, x, y, width, height)(
            self, ctyped.byref(_get_obj(ctyped.struct.RectF, ctyped.struct.Rect, x, y, width, height)(
                x, y, width, height)), ctyped.enum.CombineMode.Exclude)

    def exclude_region(self, region: Region) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipCombineRegionRegion(self, region, ctyped.enum.CombineMode.Exclude)

    def complement_rect(self, x: int | float, y: int | float, width: int | float, height: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(
            _GdiPlus.GdipCombineRegionRect, _GdiPlus.GdipCombineRegionRectI, x, y, width, height)(
            self, ctyped.byref(_get_obj(ctyped.struct.RectF, ctyped.struct.Rect, x, y, width, height)(
                x, y, width, height)), ctyped.enum.CombineMode.Complement)

    def complement_region(self, region: Region) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipCombineRegionRegion(self, region, ctyped.enum.CombineMode.Complement)

    def translate(self, x: int | float, y: int | float) -> bool:
        return _GpStatus.Ok == _get_obj(_GdiPlus.GdipTranslateRegion, _GdiPlus.GdipTranslateRegionI, x, y)(self, x, y)

    def get_bounds(self, graphics: ctyped.type.GpGraphics) -> Optional[tuple[float, float, float, float]]:
        rect = ctyped.struct.RectF()
        if _GpStatus.Ok == _GdiPlus.GdipGetRegionBounds(self, graphics, ctyped.byref(rect)):
            return rect.X, rect.Y, rect.Width, rect.Height

    def get_hrgn(self, graphics: ctyped.type.GpGraphics) -> Optional[ctyped.handle.HRGN]:
        hrgn = ctyped.type.HRGN()
        if _GpStatus.Ok == _GdiPlus.GdipGetRegionHRgn(self, graphics, ctyped.byref(hrgn)):
            return ctyped.handle.HRGN(hrgn)

    def is_empty(self, graphics: ctyped.type.GpGraphics) -> Optional[bool]:
        empty = ctyped.type.BOOL()
        if _GpStatus.Ok == _GdiPlus.GdipIsEmptyRegion(self, graphics, ctyped.byref(empty)):
            return bool(empty.value)

    def is_infinite(self, graphics: ctyped.type.GpGraphics) -> Optional[bool]:
        infinite = ctyped.type.BOOL()
        if _GpStatus.Ok == _GdiPlus.GdipIsInfiniteRegion(self, graphics, ctyped.byref(infinite)):
            return bool(infinite.value)

    def equals(self, region: Region, graphics: ctyped.type.GpGraphics) -> Optional[bool]:
        equal = ctyped.type.BOOL()
        if _GpStatus.Ok == _GdiPlus.GdipIsEqualRegion(self, region, graphics, ctyped.byref(equal)):
            return bool(equal.value)

    def get_data_size(self) -> Optional[int]:
        size = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetRegionDataSize(self, ctyped.byref(size)):
            return size.value

    def is_visible_point(self, x: int | float, y: int | float, graphics: ctyped.type.GpGraphics) -> Optional[bool]:
        visible = ctyped.type.BOOL()
        if _GpStatus.Ok == _get_obj(_GdiPlus.GdipIsVisibleRegionPoint, _GdiPlus.GdipIsVisibleRegionPointI, x, y)(
                self, x, y, graphics, ctyped.byref(visible)):
            return bool(visible.value)

    def is_visible_rect(self, x: int | float, y: int | float, width: int | float,
                        height: int | float, graphics: ctyped.type.GpGraphics) -> Optional[bool]:
        visible = ctyped.type.BOOL()
        if _GpStatus.Ok == _get_obj(_GdiPlus.GdipIsVisibleRegionRect, _GdiPlus.GdipIsVisibleRegionRectI, x, y, width, height)(
                self, x, y, width, height, graphics, ctyped.byref(visible)):
            return bool(visible.value)

    def _del(self):
        _GdiPlus.GdipDeleteRegion(self)


class FontFamily(_GdiplusBase, ctyped.type.GpFontFamily):
    @classmethod
    def from_name(cls, name: str, collection: Optional[FontCollection] = None) -> FontFamily:
        self = cls()
        _GdiPlus.GdipCreateFontFamilyFromName(name, collection, ctyped.byref(self))
        return self

    @classmethod
    def from_font_family(cls, family: ctyped.type.GpFontFamily) -> FontFamily:
        self = cls()
        _GdiPlus.GdipCloneFontFamily(family, ctyped.byref(self))
        return self

    def get_height(self, style: ctyped.enum.FontStyle) -> Optional[int]:
        height = ctyped.type.UINT16()
        if _GpStatus.Ok == _GdiPlus.GdipGetEmHeight(self, style.value, ctyped.byref(height)):
            return height.value

    def get_ascent(self, style: ctyped.enum.FontStyle) -> Optional[int]:
        ascent = ctyped.type.UINT16()
        if _GpStatus.Ok == _GdiPlus.GdipGetCellAscent(self, style.value, ctyped.byref(ascent)):
            return ascent.value

    def get_descent(self, style: ctyped.enum.FontStyle) -> Optional[int]:
        descent = ctyped.type.UINT16()
        if _GpStatus.Ok == _GdiPlus.GdipGetCellDescent(self, style.value, ctyped.byref(descent)):
            return descent.value

    def get_line_spacing(self, style: ctyped.enum.FontStyle) -> Optional[int]:
        line_spacing = ctyped.type.UINT16()
        if _GpStatus.Ok == _GdiPlus.GdipGetLineSpacing(self, style.value, ctyped.byref(line_spacing)):
            return line_spacing.value

    def get_name(self, language: int = ctyped.const.LANG_NEUTRAL) -> Optional[str]:
        name = ctyped.char_array(size=ctyped.const.LF_FACESIZE)
        if _GpStatus.Ok == _GdiPlus.GdipGetFamilyName(self, name, language):
            return name.value

    def has_style(self, style: ctyped.enum.FontStyle) -> Optional[bool]:
        has = ctyped.type.BOOL()
        if _GpStatus.Ok == _GdiPlus.GdipIsStyleAvailable(self, style.value, ctyped.byref(has)):
            return bool(has.value)

    def _del(self):
        _GdiPlus.GdipDeleteFontFamily(self)


class Font(_GdiplusBase, ctyped.type.GpFont):
    @classmethod
    def from_hdc(cls, hdc: ctyped.type.HDC) -> Font:
        self = cls()
        _GdiPlus.GdipCreateFontFromDC(hdc, ctyped.byref(self))
        return self

    @classmethod
    def from_font_family(cls, family: ctyped.type.GpFontFamily, size: float = 16,
                         style: ctyped.enum.FontStyle = ctyped.enum.FontStyle.Regular,
                         unit: ctyped.enum.Unit = ctyped.enum.Unit.Pixel) -> Font:
        self = cls()
        _GdiPlus.GdipCreateFont(family, size, style.value, unit, ctyped.byref(self))
        return self

    @classmethod
    def from_font(cls, font: ctyped.type.GpFont) -> Font:
        self = cls()
        _GdiPlus.GdipCloneFont(font, ctyped.byref(self))
        return self

    def get_font_family(self) -> FontFamily:
        family = ctyped.type.GpFontFamily()
        _GdiPlus.GdipGetFamily(self, ctyped.byref(family))
        return FontFamily.from_font_family(family)

    def get_style(self) -> Optional[ctyped.enum.FontStyle]:
        style = ctyped.type.INT()
        if _GpStatus.Ok == _GdiPlus.GdipGetFontStyle(self, ctyped.byref(style)):
            return ctyped.enum.FontStyle(style.value)

    def get_size(self) -> Optional[float]:
        size = ctyped.type.REAL()
        if _GpStatus.Ok == _GdiPlus.GdipGetFontSize(self, ctyped.byref(size)):
            return size.value

    def get_unit(self) -> Optional[ctyped.enum.Unit]:
        unit = ctyped.enum.Unit()
        if _GpStatus.Ok == _GdiPlus.GdipGetFontUnit(self, ctyped.byref(unit)):
            return unit

    def get_height_graphics(self, graphics: Graphics) -> Optional[float]:
        height = ctyped.type.REAL()
        if _GpStatus.Ok == _GdiPlus.GdipGetFontHeight(self, graphics, ctyped.byref(height)):
            return height.value

    def get_height_dpi(self, dpi: int) -> Optional[float]:
        height = ctyped.type.REAL()
        if _GpStatus.Ok == _GdiPlus.GdipGetFontHeightGivenDPI(self, dpi, ctyped.byref(height)):
            return height.value

    def _del(self):
        _GdiPlus.GdipDeleteFont(self)


class StringFormat(_GdiplusBase, ctyped.type.GpStringFormat):
    @classmethod
    def from_default(cls) -> StringFormat:
        self = cls()
        _GdiPlus.GdipStringFormatGetGenericDefault(ctyped.byref(self))
        return self

    @classmethod
    def from_typographic(cls) -> StringFormat:
        self = cls()
        _GdiPlus.GdipStringFormatGetGenericTypographic(ctyped.byref(self))
        return self

    @classmethod
    def from_flags(cls, flags: int = 0, language: int = ctyped.const.LANG_NEUTRAL) -> StringFormat:
        self = cls()
        _GdiPlus.GdipCreateStringFormat(flags, language, ctyped.byref(self))
        return self

    # noinspection PyShadowingBuiltins
    @classmethod
    def from_string_format(cls, format: StringFormat) -> StringFormat:
        self = cls()
        _GdiPlus.GdipCloneStringFormat(format, ctyped.byref(self))
        return self

    def set_flags(self, flags: int) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetStringFormatFlags(self, flags)

    def get_flags(self) -> Optional[int]:
        flags = ctyped.type.INT()
        if _GpStatus.Ok == _GdiPlus.GdipGetStringFormatFlags(self, ctyped.byref(flags)):
            return flags.value

    def set_alignment(self, align: ctyped.enum.StringAlignment) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetStringFormatAlign(self, align)

    def get_alignment(self) -> Optional[ctyped.enum.StringAlignment]:
        alignment = ctyped.enum.StringAlignment()
        if _GpStatus.Ok == _GdiPlus.GdipGetStringFormatAlign(self, ctyped.byref(alignment)):
            return alignment

    def set_line_alignment(self, align: ctyped.enum.StringAlignment) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetStringFormatLineAlign(self, align)

    def get_line_alignment(self) -> Optional[ctyped.enum.StringAlignment]:
        alignment = ctyped.enum.StringAlignment()
        if _GpStatus.Ok == _GdiPlus.GdipGetStringFormatLineAlign(self, ctyped.byref(alignment)):
            return alignment

    def set_hotkey_prefix(self, prefix: ctyped.enum.HotkeyPrefix) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetStringFormatHotkeyPrefix(self, prefix.value)

    def get_hotkey_prefix(self) -> Optional[ctyped.enum.HotkeyPrefix]:
        hotkey_prefix = ctyped.type.INT()
        if _GpStatus.Ok == _GdiPlus.GdipGetStringFormatHotkeyPrefix(self, ctyped.byref(hotkey_prefix)):
            return ctyped.enum.HotkeyPrefix(hotkey_prefix.value)

    def get_tab_stop_count(self) -> Optional[int]:
        count = ctyped.type.INT()
        if _GpStatus.Ok == _GdiPlus.GdipGetStringFormatTabStopCount(self, ctyped.byref(count)):
            return count.value

    def set_trimming(self, trimming: ctyped.enum.StringTrimming) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetStringFormatTrimming(self, trimming)

    def get_trimming(self) -> Optional[ctyped.enum.StringTrimming]:
        trimming = ctyped.enum.StringTrimming()
        if _GpStatus.Ok == _GdiPlus.GdipGetStringFormatTrimming(self, ctyped.byref(trimming)):
            return trimming

    def set_measurable_character_ranges(self, *ranges: tuple[int, int]) -> bool:
        return _GpStatus.Ok == _GdiPlus.GdipSetStringFormatMeasurableCharacterRanges(self, len(
            ranges), ctyped.array(*(ctyped.struct.CharacterRange(first, length) for first, length in ranges)))

    def get_measurable_character_range_count(self) -> Optional[int]:
        count = ctyped.type.INT()
        if _GpStatus.Ok == _GdiPlus.GdipGetStringFormatMeasurableCharacterRangeCount(self, ctyped.byref(count)):
            return count.value

    def _del(self):
        _GdiPlus.GdipDeleteStringFormat(self)


class FontCollection(_GdiplusBase, ctyped.type.GpFontCollection):
    def get_family_count(self) -> Optional[int]:
        count = ctyped.type.INT()
        if _GpStatus.Ok == _GdiPlus.GdipGetFontCollectionFamilyCount(self, ctyped.byref(count)):
            return count.value

    def get_font_families(self, count: Optional[int] = None) -> Optional[tuple[FontFamily]]:
        if count is None:
            count = self.get_family_count()
        if count is not None:
            families = ctyped.array(type=ctyped.type.GpFontFamily, size=count)
            found = ctyped.type.INT()
            if _GpStatus.Ok == _GdiPlus.GdipGetFontCollectionFamilyList(
                    self, count, ctyped.byref(families), ctyped.byref(found)):
                return tuple(FontFamily.from_font_family(families[index]) for index in range(found.value))

    def _del(self):
        pass


class InstalledFontCollection(FontCollection, ctyped.type.GpInstalledFontCollection):
    @classmethod
    def from_installed(cls) -> InstalledFontCollection:
        self = cls()
        _GdiPlus.GdipNewInstalledFontCollection(ctyped.byref(self))
        return self


class PrivateFontCollection(FontCollection, ctyped.type.GpPrivateFontCollection):
    @classmethod
    def from_empty(cls) -> PrivateFontCollection:
        self = cls()
        _GdiPlus.GdipNewPrivateFontCollection(ctyped.byref(self))
        return self

    def add_new_font(self, path: str):
        return _GpStatus.Ok == _GdiPlus.GdipPrivateAddFontFile(self, path)

    def _del(self):
        _GdiPlus.GdipDeletePrivateFontCollection(ctyped.byref(self))


class ImageCodec:
    @staticmethod
    def get_decoders_count_and_size() -> Optional[tuple[int, int]]:
        count = ctyped.type.UINT()
        size = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageDecodersSize(ctyped.byref(count), ctyped.byref(size)):
            return count.value, size.value

    @classmethod
    @contextlib.contextmanager
    def get_decoders(cls, count: Optional[int] = None,
                     size: Optional[int] = None) -> ContextManager[Optional[tuple[ctyped.struct.ImageCodecInfo]]]:
        _ = _GdiplusToken()
        if count is None or size is None:
            count, size = cls.get_decoders_count_and_size()
        with ctyped.buffer(size) as buffer:
            if buffer:
                codecs = ctyped.cast(buffer, ctyped.struct.ImageCodecInfo)
                if _GpStatus.Ok == _GdiPlus.GdipGetImageDecoders(count, size, codecs):
                    yield tuple(codecs[index] for index in range(count))
                    return
        yield

    @staticmethod
    def get_encoders_count_and_size() -> Optional[tuple[int, int]]:
        count = ctyped.type.UINT()
        size = ctyped.type.UINT()
        if _GpStatus.Ok == _GdiPlus.GdipGetImageEncodersSize(ctyped.byref(count), ctyped.byref(size)):
            return count.value, size.value

    @classmethod
    @contextlib.contextmanager
    def get_encoders(cls, count: Optional[int] = None,
                     size: Optional[int] = None) -> ContextManager[Optional[tuple[ctyped.struct.ImageCodecInfo]]]:
        _ = _GdiplusToken()
        if count is None or size is None:
            count, size = cls.get_encoders_count_and_size()
        with ctyped.buffer(size) as buffer:
            if buffer:
                codecs = ctyped.cast(buffer, ctyped.struct.ImageCodecInfo)
                if _GpStatus.Ok == _GdiPlus.GdipGetImageEncoders(count, size, codecs):
                    yield tuple(codecs[index] for index in range(count))
                    return
        yield

    @staticmethod
    def _get_codec(prov: Callable[[], ContextManager[tuple[ctyped.struct.ImageCodecInfo]]],
                   prop: Literal['FormatDescription', 'CodecName', 'FilenameExtension', 'MimeType'],
                   val: str) -> Optional[ctyped.struct.ImageCodecInfo]:
        val = val.casefold()
        with prov() as codecs:
            if codecs is not None:
                for codec in codecs:
                    if val in getattr(codec, prop).casefold():
                        return ctyped.struct.ImageCodecInfo.from_buffer_copy(codec)

    @classmethod
    def get_encoder_by_format_description(cls, description: str) -> Optional[ctyped.struct.ImageCodecInfo]:
        return cls._get_codec(cls.get_encoders, 'FormatDescription', description)

    @classmethod
    def get_encoder_by_codec_name(cls, name: str) -> Optional[ctyped.struct.ImageCodecInfo]:
        return cls._get_codec(cls.get_encoders, 'CodecName', name)

    @classmethod
    def get_encoder_by_filename_extension(cls, extension: str) -> Optional[ctyped.struct.ImageCodecInfo]:
        return cls._get_codec(cls.get_encoders, 'FilenameExtension', extension)

    # noinspection PyShadowingBuiltins
    @classmethod
    def get_encoder_by_mime_type(cls, type: str) -> Optional[ctyped.struct.ImageCodecInfo]:
        return cls._get_codec(cls.get_encoders, 'MimeType', type)


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


def image_is_valid(path: str) -> bool:
    image = Image.from_file(path)
    return bool(image and image.get_width() and image.get_height())


def image_save(image: Image, path: str, quality: int = 100) -> bool:
    param_val = ctyped.type.LONG(quality)
    params = ctyped.struct.EncoderParameters(1, ctyped.array(ctyped.struct.EncoderParameter(ctyped.get_guid(
        ctyped.const.EncoderQuality), 1, ctyped.enum.EncoderParameterValueType.Long.value, ctyped.cast(param_val, ctyped.type.PVOID))))
    return image.save_to_file(path, ImageCodec.get_encoder_by_filename_extension(ntpath.splitext(path)[1]).Clsid, params)


def image_iter_frames(image: Image) -> Generator[int, None, None]:
    dim_id = image.get_frame_dimensions()[0]
    for index in range(image.get_frame_count(dim_id)):
        image.select_active_frame(dim_id, index)
        yield index


def image_get_property(image: Image, tag: int) -> Optional[ctyped.Pointer]:
    with image.get_property_item(tag) as property_item:
        if property_item.type == ctyped.const.PropertyTagTypeByte:
            type_ = ctyped.type.c_byte
        elif property_item.type == ctyped.const.PropertyTagTypeShort:
            type_ = ctyped.type.c_ushort
        elif property_item.type == ctyped.const.PropertyTagTypeLong:
            type_ = ctyped.type.c_ulong
        elif property_item.type == ctyped.const.PropertyTagTypeRational:
            type_ = ctyped.struct.Rational
        elif property_item.type == ctyped.const.PropertyTagTypeUndefined:
            type_ = ctyped.type.c_byte
        elif property_item.type == ctyped.const.PropertyTagTypeSLONG:
            type_ = ctyped.type.c_long
        else:
            type_ = ctyped.type.c_void_p
        return ctyped.cast(property_item.value, ctyped.pointer(type_))


def image_attributes_from_alpha(alpha: float = 1) -> ImageAttributes:
    matrix = ctyped.struct.ColorMatrix()
    for index in range(5):
        matrix.m[index][index] = 1
    matrix.m[3][3] = alpha
    self = ImageAttributes.from_empty()
    self.set_color_matrix(matrix)
    return self


def bitmap_from_color(color: ctyped.type.ARGB, width: int = 512, height: int = 512) -> Optional[Bitmap]:
    if bitmap := Bitmap.from_dimension(width, height):
        if Graphics.from_image(bitmap).fill_rectangle(SolidBrush.from_color(color), 0, 0, width, height):
            return bitmap


def bitmap_from_svg(path: str, width: int = 512, height: int = 512) -> Optional[Bitmap]:
    with _utils.get_d2d1_dc_render_target() as target:
        if target and (p_stream := _utils.open_file_stream(path)):
            with p_stream as stream, ctyped.interface.COM[d2d1_3.ID2D1DeviceContext5](target) as context:
                if context:
                    with ctyped.interface.COM[d2d1svg.ID2D1SvgDocument]() as svg:
                        if ctyped.macro.SUCCEEDED(context.CreateSvgDocument(
                                stream, ctyped.struct.D2D_SIZE_F(width, height), ctyped.byref(svg))):
                            _utils.set_svg_doc_viewport(svg)
                            _utils.set_svg_doc_dimension(svg, width, height)
                            bitmap = Bitmap.from_dimension(width, height, ctyped.const.PixelFormat32bppARGB)
                            with Graphics.from_image(bitmap).get_managed_hdc() as hdc:
                                if ctyped.macro.SUCCEEDED(target.BindDC(hdc, ctyped.byref(
                                        ctyped.struct.RECT(right=width, bottom=height)))):
                                    target.BeginDraw()
                                    context.DrawSvgDocument(svg)
                                    if ctyped.macro.SUCCEEDED(target.EndDraw(ctyped.NULLPTR, ctyped.NULLPTR)):
                                        return bitmap


def bitmap_from_string(string: str = _string.printable.replace(_string.whitespace, '', 1), size: int = 1024,
                       r: int = 0, g: int = 0, b: int = 0, font_name_or_path: str = 'Segoe UI') -> Bitmap:
    if ntpath.isfile(font_name_or_path):
        collection = PrivateFontCollection.from_empty()
        collection.add_new_font(font_name_or_path)
        font = Font.from_font_family(collection.get_font_families()[0], size)
    else:
        for family in InstalledFontCollection.from_installed().get_font_families():
            if font_name_or_path == family.get_name():
                font = Font.from_font_family(family, size)
                break
        else:
            return Bitmap()
    format_ = StringFormat.from_typographic()
    format_.set_flags(ctyped.enum.StringFormatFlags.NoFontFallback | ctyped.enum.StringFormatFlags.NoWrap)
    format_.set_measurable_character_ranges((0, len(string)))
    graphics = Graphics.from_image(Bitmap.from_dimension(1, 1, ctyped.const.PixelFormat32bppARGB))
    bounds = graphics.measure_character_ranges(string, font, 1, format=format_)[0].get_bounds(graphics)
    bitmap = Bitmap.from_dimension(math.ceil(bounds[2]), math.ceil(bounds[3]), ctyped.const.PixelFormat32bppARGB)
    graphics = Graphics.from_image(bitmap)
    graphics.draw_string(string, font, SolidBrush.from_color(Color.from_rgba(r, g, b)), format=format_)
    return bitmap


def bitmap_from_resized_bitmap(bitmap: Bitmap, width: int, height: int, fit: bool = False, crop_to_fit: bool = False) -> Bitmap:
    src_w = bitmap.get_width()
    src_h = bitmap.get_height()
    resized_bitmap = bitmap.from_dimension(width, height, bitmap.get_pixel_format())
    resized_bitmap.set_resolution(bitmap.get_horizontal_resolution(), bitmap.get_vertical_resolution())
    graphics = Graphics.from_image(resized_bitmap)
    graphics.set_interpolation_mode(ctyped.enum.InterpolationMode.HighQualityBicubic)
    if fit:
        x, y, w, h = _calc_src_x_y_w_h(
            src_w, src_h, width, height, crop_to_fit ^ (width / src_w > height / src_h))
        graphics.scale_transform(width / w, height / h)
        graphics.draw_image_from_rect(bitmap, -min(0.0, x), -min(0.0, y), max(0.0, x), max(0.0, y))
    else:
        graphics.scale_transform(width / src_w, height / src_h)
        graphics.draw_image(bitmap)
    return resized_bitmap

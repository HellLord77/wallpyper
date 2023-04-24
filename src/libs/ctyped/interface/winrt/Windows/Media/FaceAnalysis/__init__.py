from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Media as _Windows_Media
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics import Imaging as _Windows_Graphics_Imaging
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IDetectedFace(_inspectable.IInspectable):
    get_FaceBox: _Callable[[_Pointer[_struct.Windows.Graphics.Imaging.BitmapBounds]],  # returnValue
                           _type.HRESULT]


class IFaceDetector(_inspectable.IInspectable):
    DetectFacesAsync: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # image
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IDetectedFace]]]],  # returnValue
                                _type.HRESULT]
    DetectFacesWithSearchAreaAsync: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # image
                                               _struct.Windows.Graphics.Imaging.BitmapBounds,  # searchArea
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IDetectedFace]]]],  # returnValue
                                              _type.HRESULT]
    get_MinDetectableFaceSize: _Callable[[_Pointer[_struct.Windows.Graphics.Imaging.BitmapSize]],  # returnValue
                                         _type.HRESULT]
    put_MinDetectableFaceSize: _Callable[[_struct.Windows.Graphics.Imaging.BitmapSize],  # value
                                         _type.HRESULT]
    get_MaxDetectableFaceSize: _Callable[[_Pointer[_struct.Windows.Graphics.Imaging.BitmapSize]],  # returnValue
                                         _type.HRESULT]
    put_MaxDetectableFaceSize: _Callable[[_struct.Windows.Graphics.Imaging.BitmapSize],  # value
                                         _type.HRESULT]


class IFaceDetectorStatics(_inspectable.IInspectable):
    CreateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IFaceDetector]]],  # returnValue
                           _type.HRESULT]
    GetSupportedBitmapPixelFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Graphics.Imaging.BitmapPixelFormat]]],  # result
                                              _type.HRESULT]
    IsBitmapPixelFormatSupported: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # bitmapPixelFormat
                                             _Pointer[_type.boolean]],  # result
                                            _type.HRESULT]
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # returnValue
                               _type.HRESULT]

    _factory = True


class IFaceTracker(_inspectable.IInspectable):
    ProcessNextFrameAsync: _Callable[[_Windows_Media.IVideoFrame,  # videoFrame
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IDetectedFace]]]],  # returnValue
                                     _type.HRESULT]
    get_MinDetectableFaceSize: _Callable[[_Pointer[_struct.Windows.Graphics.Imaging.BitmapSize]],  # returnValue
                                         _type.HRESULT]
    put_MinDetectableFaceSize: _Callable[[_struct.Windows.Graphics.Imaging.BitmapSize],  # value
                                         _type.HRESULT]
    get_MaxDetectableFaceSize: _Callable[[_Pointer[_struct.Windows.Graphics.Imaging.BitmapSize]],  # returnValue
                                         _type.HRESULT]
    put_MaxDetectableFaceSize: _Callable[[_struct.Windows.Graphics.Imaging.BitmapSize],  # value
                                         _type.HRESULT]


class IFaceTrackerStatics(_inspectable.IInspectable):
    CreateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IFaceTracker]]],  # returnValue
                           _type.HRESULT]
    GetSupportedBitmapPixelFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Graphics.Imaging.BitmapPixelFormat]]],  # result
                                              _type.HRESULT]
    IsBitmapPixelFormatSupported: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # bitmapPixelFormat
                                             _Pointer[_type.boolean]],  # result
                                            _type.HRESULT]
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # returnValue
                               _type.HRESULT]

    _factory = True

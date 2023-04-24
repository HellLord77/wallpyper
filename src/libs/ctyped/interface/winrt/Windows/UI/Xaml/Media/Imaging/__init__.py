from __future__ import annotations

from typing import Callable as _Callable

from .... import Xaml as _Windows_UI_Xaml
from ..... import Foundation as _Windows_Foundation
from .....ApplicationModel import Background as _Windows_ApplicationModel_Background
from .....Graphics import Imaging as _Windows_Graphics_Imaging
from .....Storage import Streams as _Windows_Storage_Streams
from ...... import inspectable as _inspectable
from .......um import Unknwnbase as _Unknwnbase
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class _IDownloadProgressEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IDownloadProgressEventArgs],  # e
                      _type.HRESULT]


class IDownloadProgressEventHandler(_IDownloadProgressEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDownloadProgressEventHandler_impl(_IDownloadProgressEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IBitmapImage(_inspectable.IInspectable):
    get_CreateOptions: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Imaging.BitmapCreateOptions]],  # value
                                 _type.HRESULT]
    put_CreateOptions: _Callable[[_enum.Windows.UI.Xaml.Media.Imaging.BitmapCreateOptions],  # value
                                 _type.HRESULT]
    get_UriSource: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                             _type.HRESULT]
    put_UriSource: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                             _type.HRESULT]
    get_DecodePixelWidth: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    put_DecodePixelWidth: _Callable[[_type.INT32],  # value
                                    _type.HRESULT]
    get_DecodePixelHeight: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    put_DecodePixelHeight: _Callable[[_type.INT32],  # value
                                     _type.HRESULT]
    add_DownloadProgress: _Callable[[IDownloadProgressEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_DownloadProgress: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_ImageOpened: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ImageOpened: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_ImageFailed: _Callable[[_Windows_UI_Xaml.IExceptionRoutedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ImageFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]


class IBitmapImage2(_inspectable.IInspectable):
    get_DecodePixelType: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Imaging.DecodePixelType]],  # value
                                   _type.HRESULT]
    put_DecodePixelType: _Callable[[_enum.Windows.UI.Xaml.Media.Imaging.DecodePixelType],  # value
                                   _type.HRESULT]


class IBitmapImage3(_inspectable.IInspectable):
    get_IsAnimatedBitmap: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsPlaying: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_AutoPlay: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_AutoPlay: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    Play: _Callable[[],
                    _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IBitmapImageFactory(_inspectable.IInspectable):
    CreateInstanceWithUriSource: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uriSource
                                            _Pointer[IBitmapImage]],  # value
                                           _type.HRESULT]

    _factory = True


class IBitmapImageStatics(_inspectable.IInspectable):
    get_CreateOptionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_UriSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_DecodePixelWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_DecodePixelHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class IBitmapImageStatics2(_inspectable.IInspectable):
    get_DecodePixelTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]

    _factory = True


class IBitmapImageStatics3(_inspectable.IInspectable):
    get_IsAnimatedBitmapProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_IsPlayingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_AutoPlayProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]

    _factory = True


class IBitmapSource(_inspectable.IInspectable):
    get_PixelWidth: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_PixelHeight: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    SetSource: _Callable[[_Windows_Storage_Streams.IRandomAccessStream],  # streamSource
                         _type.HRESULT]
    SetSourceAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # streamSource
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                              _type.HRESULT]


class IBitmapSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IBitmapSource]],  # value
                              _type.HRESULT]


class IBitmapSourceStatics(_inspectable.IInspectable):
    get_PixelWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_PixelHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IDownloadProgressEventArgs(_inspectable.IInspectable):
    get_Progress: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_Progress: _Callable[[_type.INT32],  # value
                            _type.HRESULT]


class IRenderTargetBitmap(_inspectable.IInspectable):
    get_PixelWidth: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_PixelHeight: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    RenderAsync: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    RenderToSizeAsync: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                  _type.INT32,  # scaledWidth
                                  _type.INT32,  # scaledHeight
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                 _type.HRESULT]
    GetPixelsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # operation
                              _type.HRESULT]


class IRenderTargetBitmapStatics(_inspectable.IInspectable):
    get_PixelWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_PixelHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class ISoftwareBitmapSource(_inspectable.IInspectable):
    SetBitmapAsync: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # softwareBitmap
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                              _type.HRESULT]


class ISurfaceImageSource(_inspectable.IInspectable):
    pass


class ISurfaceImageSourceFactory(_inspectable.IInspectable):
    CreateInstanceWithDimensions: _Callable[[_type.INT32,  # pixelWidth
                                             _type.INT32,  # pixelHeight
                                             _inspectable.IInspectable,  # baseInterface
                                             _Pointer[_inspectable.IInspectable],  # innerInterface
                                             _Pointer[ISurfaceImageSource]],  # value
                                            _type.HRESULT]
    CreateInstanceWithDimensionsAndOpacity: _Callable[[_type.INT32,  # pixelWidth
                                                       _type.INT32,  # pixelHeight
                                                       _type.boolean,  # isOpaque
                                                       _inspectable.IInspectable,  # baseInterface
                                                       _Pointer[_inspectable.IInspectable],  # innerInterface
                                                       _Pointer[ISurfaceImageSource]],  # value
                                                      _type.HRESULT]


class ISvgImageSource(_inspectable.IInspectable):
    get_UriSource: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                             _type.HRESULT]
    put_UriSource: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                             _type.HRESULT]
    get_RasterizePixelWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_RasterizePixelWidth: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_RasterizePixelHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    put_RasterizePixelHeight: _Callable[[_type.DOUBLE],  # value
                                        _type.HRESULT]
    add_Opened: _Callable[[_Windows_Foundation.ITypedEventHandler[ISvgImageSource, ISvgImageSourceOpenedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Opened: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_OpenFailed: _Callable[[_Windows_Foundation.ITypedEventHandler[ISvgImageSource, ISvgImageSourceFailedEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_OpenFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    SetSourceAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # streamSource
                               _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.UI.Xaml.Media.Imaging.SvgImageSourceLoadStatus]]],  # operation
                              _type.HRESULT]


class ISvgImageSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISvgImageSource]],  # value
                              _type.HRESULT]
    CreateInstanceWithUriSource: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uriSource
                                            _inspectable.IInspectable,  # baseInterface
                                            _Pointer[_inspectable.IInspectable],  # innerInterface
                                            _Pointer[ISvgImageSource]],  # value
                                           _type.HRESULT]


class ISvgImageSourceFailedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Imaging.SvgImageSourceLoadStatus]],  # value
                          _type.HRESULT]


class ISvgImageSourceOpenedEventArgs(_inspectable.IInspectable):
    pass


class ISvgImageSourceStatics(_inspectable.IInspectable):
    get_UriSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_RasterizePixelWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_RasterizePixelHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]

    _factory = True


class IVirtualSurfaceImageSource(_inspectable.IInspectable):
    pass


class IVirtualSurfaceImageSourceFactory(_inspectable.IInspectable):
    CreateInstanceWithDimensions: _Callable[[_type.INT32,  # pixelWidth
                                             _type.INT32,  # pixelHeight
                                             _Pointer[IVirtualSurfaceImageSource]],  # value
                                            _type.HRESULT]
    CreateInstanceWithDimensionsAndOpacity: _Callable[[_type.INT32,  # pixelWidth
                                                       _type.INT32,  # pixelHeight
                                                       _type.boolean,  # isOpaque
                                                       _Pointer[IVirtualSurfaceImageSource]],  # value
                                                      _type.HRESULT]

    _factory = True


class IWriteableBitmap(_inspectable.IInspectable):
    get_PixelBuffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]
    Invalidate: _Callable[[],
                          _type.HRESULT]


class IWriteableBitmapFactory(_inspectable.IInspectable):
    CreateInstanceWithDimensions: _Callable[[_type.INT32,  # pixelWidth
                                             _type.INT32,  # pixelHeight
                                             _Pointer[IWriteableBitmap]],  # value
                                            _type.HRESULT]

    _factory = True


class IXamlRenderingBackgroundTask(_inspectable.IInspectable):
    pass


class IXamlRenderingBackgroundTaskFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IXamlRenderingBackgroundTask]],  # value
                              _type.HRESULT]


class IXamlRenderingBackgroundTaskOverrides(_inspectable.IInspectable):
    OnRun: _Callable[[_Windows_ApplicationModel_Background.IBackgroundTaskInstance],  # taskInstance
                     _type.HRESULT]

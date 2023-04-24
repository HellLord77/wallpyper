from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import Media as _Windows_Media
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ......um import Unknwnbase as _Unknwnbase
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class _IPerceptionStartFaceAuthenticationHandler:
    Invoke: _Callable[[IPerceptionFaceAuthenticationGroup,  # sender
                       _Pointer[_type.boolean]],  # result
                      _type.HRESULT]


class IPerceptionStartFaceAuthenticationHandler(_IPerceptionStartFaceAuthenticationHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IPerceptionStartFaceAuthenticationHandler_impl(_IPerceptionStartFaceAuthenticationHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IPerceptionStopFaceAuthenticationHandler:
    Invoke: _Callable[[IPerceptionFaceAuthenticationGroup],  # sender
                      _type.HRESULT]


class IPerceptionStopFaceAuthenticationHandler(_IPerceptionStopFaceAuthenticationHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IPerceptionStopFaceAuthenticationHandler_impl(_IPerceptionStopFaceAuthenticationHandler, _Unknwnbase.IUnknown_impl):
    pass


class IKnownPerceptionFrameKindStatics(_inspectable.IInspectable):
    Color: _Callable[[_Pointer[_type.HSTRING]],  # value
                     _type.HRESULT]
    Depth: _Callable[[_Pointer[_type.HSTRING]],  # value
                     _type.HRESULT]
    Infrared: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]

    _factory = True


class IPerceptionControlGroup(_inspectable.IInspectable):
    FrameProviderIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                _type.HRESULT]


class IPerceptionControlGroupFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # ids
                       _Pointer[IPerceptionControlGroup]],  # result
                      _type.HRESULT]

    _factory = True


class IPerceptionCorrelation(_inspectable.IInspectable):
    TargetId: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    Position: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                        _type.HRESULT]
    Orientation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Quaternion]],  # value
                           _type.HRESULT]


class IPerceptionCorrelationFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # targetId
                       _struct.Windows.Foundation.Numerics.Vector3,  # position
                       _struct.Windows.Foundation.Numerics.Quaternion,  # orientation
                       _Pointer[IPerceptionCorrelation]],  # result
                      _type.HRESULT]

    _factory = True


class IPerceptionCorrelationGroup(_inspectable.IInspectable):
    RelativeLocations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPerceptionCorrelation]]],  # value
                                 _type.HRESULT]


class IPerceptionCorrelationGroupFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Foundation_Collections.IIterable[IPerceptionCorrelation],  # relativeLocations
                       _Pointer[IPerceptionCorrelationGroup]],  # result
                      _type.HRESULT]

    _factory = True


class IPerceptionFaceAuthenticationGroup(_inspectable.IInspectable):
    FrameProviderIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                _type.HRESULT]


class IPerceptionFaceAuthenticationGroupFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # ids
                       IPerceptionStartFaceAuthenticationHandler,  # startHandler
                       IPerceptionStopFaceAuthenticationHandler,  # stopHandler
                       _Pointer[IPerceptionFaceAuthenticationGroup]],  # result
                      _type.HRESULT]

    _factory = True


class IPerceptionFrame(_inspectable.IInspectable):
    RelativeTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                          _type.HRESULT]
    FrameData: _Callable[[_Pointer[_Windows_Foundation.IMemoryBuffer]],  # value
                         _type.HRESULT]


class IPerceptionFrameProvider(_inspectable.IInspectable):
    FrameProviderInfo: _Callable[[_Pointer[IPerceptionFrameProviderInfo]],  # result
                                 _type.HRESULT]
    Available: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]
    Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    SetProperty: _Callable[[IPerceptionPropertyChangeRequest],  # value
                           _type.HRESULT]


class IPerceptionFrameProviderInfo(_inspectable.IInspectable):
    Id: _Callable[[_type.HSTRING],  # value
                  _type.HRESULT]
    DisplayName: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    DeviceKind: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    FrameKind: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    Hidden: _Callable[[_type.boolean],  # value
                      _type.HRESULT]


class IPerceptionFrameProviderManager(_inspectable.IInspectable):
    GetFrameProvider: _Callable[[IPerceptionFrameProviderInfo,  # frameProviderInfo
                                 _Pointer[IPerceptionFrameProvider]],  # result
                                _type.HRESULT]


class IPerceptionFrameProviderManagerServiceStatics(_inspectable.IInspectable):
    RegisterFrameProviderInfo: _Callable[[IPerceptionFrameProviderManager,  # manager
                                          IPerceptionFrameProviderInfo],  # frameProviderInfo
                                         _type.HRESULT]
    UnregisterFrameProviderInfo: _Callable[[IPerceptionFrameProviderManager,  # manager
                                            IPerceptionFrameProviderInfo],  # frameProviderInfo
                                           _type.HRESULT]
    RegisterFaceAuthenticationGroup: _Callable[[IPerceptionFrameProviderManager,  # manager
                                                IPerceptionFaceAuthenticationGroup],  # faceAuthenticationGroup
                                               _type.HRESULT]
    UnregisterFaceAuthenticationGroup: _Callable[[IPerceptionFrameProviderManager,  # manager
                                                  IPerceptionFaceAuthenticationGroup],  # faceAuthenticationGroup
                                                 _type.HRESULT]
    RegisterControlGroup: _Callable[[IPerceptionFrameProviderManager,  # manager
                                     IPerceptionControlGroup],  # controlGroup
                                    _type.HRESULT]
    UnregisterControlGroup: _Callable[[IPerceptionFrameProviderManager,  # manager
                                       IPerceptionControlGroup],  # controlGroup
                                      _type.HRESULT]
    RegisterCorrelationGroup: _Callable[[IPerceptionFrameProviderManager,  # manager
                                         IPerceptionCorrelationGroup],  # correlationGroup
                                        _type.HRESULT]
    UnregisterCorrelationGroup: _Callable[[IPerceptionFrameProviderManager,  # manager
                                           IPerceptionCorrelationGroup],  # correlationGroup
                                          _type.HRESULT]
    UpdateAvailabilityForProvider: _Callable[[IPerceptionFrameProvider,  # provider
                                              _type.boolean],  # available
                                             _type.HRESULT]
    PublishFrameForProvider: _Callable[[IPerceptionFrameProvider,  # provider
                                        IPerceptionFrame],  # frame
                                       _type.HRESULT]

    _factory = True


class IPerceptionPropertyChangeRequest(_inspectable.IInspectable):
    Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                    _type.HRESULT]
    Value: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                     _type.HRESULT]
    Status: _Callable[[_enum.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus],  # value
                      _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPerceptionVideoFrameAllocator(_inspectable.IInspectable):
    AllocateFrame: _Callable[[_Pointer[IPerceptionFrame]],  # value
                             _type.HRESULT]
    CopyFromVideoFrame: _Callable[[_Windows_Media.IVideoFrame,  # frame
                                   _Pointer[IPerceptionFrame]],  # value
                                  _type.HRESULT]


class IPerceptionVideoFrameAllocatorFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # maxOutstandingFrameCountForWrite
                       _enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # format
                       _struct.Windows.Foundation.Size,  # resolution
                       _enum.Windows.Graphics.Imaging.BitmapAlphaMode,  # alpha
                       _Pointer[IPerceptionVideoFrameAllocator]],  # result
                      _type.HRESULT]

    _factory = True

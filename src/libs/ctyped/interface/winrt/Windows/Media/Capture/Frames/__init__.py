from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Capture as _Windows_Media_Capture
from ... import Devices as _Windows_Media_Devices
from ... import MediaProperties as _Windows_Media_MediaProperties
from ...Devices import Core as _Windows_Media_Devices_Core
from .... import Foundation as _Windows_Foundation
from .... import Media as _Windows_Media
from ....Devices import Enumeration as _Windows_Devices_Enumeration
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Graphics import Imaging as _Windows_Graphics_Imaging
from ....Graphics.DirectX import Direct3D11 as _Windows_Graphics_DirectX_Direct3D11
from ....Perception import Spatial as _Windows_Perception_Spatial
from ....Storage import Streams as _Windows_Storage_Streams
from ....UI import WindowManagement as _Windows_UI_WindowManagement
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IAudioMediaFrame(_inspectable.IInspectable):
    get_FrameReference: _Callable[[_Pointer[IMediaFrameReference]],  # value
                                  _type.HRESULT]
    get_AudioEncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IAudioEncodingProperties]],  # value
                                           _type.HRESULT]
    GetAudioFrame: _Callable[[_Pointer[_Windows_Media.IAudioFrame]],  # value
                             _type.HRESULT]


class IBufferMediaFrame(_inspectable.IInspectable):
    get_FrameReference: _Callable[[_Pointer[IMediaFrameReference]],  # value
                                  _type.HRESULT]
    get_Buffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                          _type.HRESULT]


class IDepthMediaFrame(_inspectable.IInspectable):
    get_FrameReference: _Callable[[_Pointer[IMediaFrameReference]],  # value
                                  _type.HRESULT]
    get_VideoMediaFrame: _Callable[[_Pointer[IVideoMediaFrame]],  # value
                                   _type.HRESULT]
    get_DepthFormat: _Callable[[_Pointer[IDepthMediaFrameFormat]],  # value
                               _type.HRESULT]
    TryCreateCoordinateMapper: _Callable[[_Windows_Media_Devices_Core.ICameraIntrinsics,  # cameraIntrinsics
                                          _Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                          _Pointer[_Windows_Media_Devices_Core.IDepthCorrelatedCoordinateMapper]],  # value
                                         _type.HRESULT]


class IDepthMediaFrame2(_inspectable.IInspectable):
    get_MaxReliableDepth: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    get_MinReliableDepth: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]


class IDepthMediaFrameFormat(_inspectable.IInspectable):
    get_VideoFormat: _Callable[[_Pointer[IVideoMediaFrameFormat]],  # value
                               _type.HRESULT]
    get_DepthScaleInMeters: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]


class IInfraredMediaFrame(_inspectable.IInspectable):
    get_FrameReference: _Callable[[_Pointer[IMediaFrameReference]],  # value
                                  _type.HRESULT]
    get_VideoMediaFrame: _Callable[[_Pointer[IVideoMediaFrame]],  # value
                                   _type.HRESULT]
    get_IsIlluminated: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IMediaFrameArrivedEventArgs(_inspectable.IInspectable):
    pass


class IMediaFrameFormat(_inspectable.IInspectable):
    get_MajorType: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Subtype: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_FrameRate: _Callable[[_Pointer[_Windows_Media_MediaProperties.IMediaRatio]],  # value
                             _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    get_VideoFormat: _Callable[[_Pointer[IVideoMediaFrameFormat]],  # value
                               _type.HRESULT]


class IMediaFrameFormat2(_inspectable.IInspectable):
    get_AudioEncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IAudioEncodingProperties]],  # value
                                           _type.HRESULT]


class IMediaFrameReader(_inspectable.IInspectable):
    add_FrameArrived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaFrameReader, IMediaFrameArrivedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_FrameArrived: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    TryAcquireLatestFrame: _Callable[[_Pointer[IMediaFrameReference]],  # value
                                     _type.HRESULT]
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.Capture.Frames.MediaFrameReaderStartStatus]]],  # operation
                          _type.HRESULT]
    StopAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                         _type.HRESULT]


class IMediaFrameReader2(_inspectable.IInspectable):
    put_AcquisitionMode: _Callable[[_enum.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode],  # value
                                   _type.HRESULT]
    get_AcquisitionMode: _Callable[[_Pointer[_enum.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode]],  # value
                                   _type.HRESULT]


class IMediaFrameReference(_inspectable.IInspectable):
    get_SourceKind: _Callable[[_Pointer[_enum.Windows.Media.Capture.Frames.MediaFrameSourceKind]],  # value
                              _type.HRESULT]
    get_Format: _Callable[[_Pointer[IMediaFrameFormat]],  # value
                          _type.HRESULT]
    get_SystemRelativeTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                      _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    get_BufferMediaFrame: _Callable[[_Pointer[IBufferMediaFrame]],  # value
                                    _type.HRESULT]
    get_VideoMediaFrame: _Callable[[_Pointer[IVideoMediaFrame]],  # value
                                   _type.HRESULT]
    get_CoordinateSystem: _Callable[[_Pointer[_Windows_Perception_Spatial.ISpatialCoordinateSystem]],  # value
                                    _type.HRESULT]


class IMediaFrameReference2(_inspectable.IInspectable):
    get_AudioMediaFrame: _Callable[[_Pointer[IAudioMediaFrame]],  # value
                                   _type.HRESULT]


class IMediaFrameSource(_inspectable.IInspectable):
    get_Info: _Callable[[_Pointer[IMediaFrameSourceInfo]],  # value
                        _type.HRESULT]
    get_Controller: _Callable[[_Pointer[IMediaFrameSourceController]],  # value
                              _type.HRESULT]
    get_SupportedFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaFrameFormat]]],  # value
                                    _type.HRESULT]
    get_CurrentFormat: _Callable[[_Pointer[IMediaFrameFormat]],  # value
                                 _type.HRESULT]
    SetFormatAsync: _Callable[[IMediaFrameFormat,  # format
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                              _type.HRESULT]
    add_FormatChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaFrameSource, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_FormatChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    TryGetCameraIntrinsics: _Callable[[IMediaFrameFormat,  # format
                                       _Pointer[_Windows_Media_Devices_Core.ICameraIntrinsics]],  # value
                                      _type.HRESULT]


class IMediaFrameSourceController(_inspectable.IInspectable):
    GetPropertyAsync: _Callable[[_type.HSTRING,  # propertyId
                                 _Pointer[_Windows_Foundation.IAsyncOperation[IMediaFrameSourceGetPropertyResult]]],  # value
                                _type.HRESULT]
    SetPropertyAsync: _Callable[[_type.HSTRING,  # propertyId
                                 _inspectable.IInspectable,  # propertyValue
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.Capture.Frames.MediaFrameSourceSetPropertyStatus]]],  # value
                                _type.HRESULT]
    get_VideoDeviceController: _Callable[[_Pointer[_Windows_Media_Devices.IVideoDeviceController]],  # value
                                         _type.HRESULT]


class IMediaFrameSourceController2(_inspectable.IInspectable):
    GetPropertyByExtendedIdAsync: _Callable[[_type.UINT32,  # __extendedPropertyIdSize
                                             _Pointer[_type.BYTE],  # extendedPropertyId
                                             _Windows_Foundation.IReference[_type.UINT32],  # maxPropertyValueSize
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IMediaFrameSourceGetPropertyResult]]],  # operation
                                            _type.HRESULT]
    SetPropertyByExtendedIdAsync: _Callable[[_type.UINT32,  # __extendedPropertyIdSize
                                             _Pointer[_type.BYTE],  # extendedPropertyId
                                             _type.UINT32,  # __propertyValueSize
                                             _Pointer[_type.BYTE],  # propertyValue
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.Capture.Frames.MediaFrameSourceSetPropertyStatus]]],  # operation
                                            _type.HRESULT]


class IMediaFrameSourceController3(_inspectable.IInspectable):
    get_AudioDeviceController: _Callable[[_Pointer[_Windows_Media_Devices.IAudioDeviceController]],  # value
                                         _type.HRESULT]


class IMediaFrameSourceGetPropertyResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyStatus]],  # value
                          _type.HRESULT]
    get_Value: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]


class IMediaFrameSourceGroup(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_SourceInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaFrameSourceInfo]]],  # value
                               _type.HRESULT]


class IMediaFrameSourceGroupStatics(_inspectable.IInspectable, factory=True):
    FindAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IMediaFrameSourceGroup]]]],  # value
                            _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # id
                            _Pointer[_Windows_Foundation.IAsyncOperation[IMediaFrameSourceGroup]]],  # value
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IMediaFrameSourceInfo(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_MediaStreamType: _Callable[[_Pointer[_enum.Windows.Media.Capture.MediaStreamType]],  # value
                                   _type.HRESULT]
    get_SourceKind: _Callable[[_Pointer[_enum.Windows.Media.Capture.Frames.MediaFrameSourceKind]],  # value
                              _type.HRESULT]
    get_SourceGroup: _Callable[[_Pointer[IMediaFrameSourceGroup]],  # value
                               _type.HRESULT]
    get_DeviceInformation: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                                     _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    get_CoordinateSystem: _Callable[[_Pointer[_Windows_Perception_Spatial.ISpatialCoordinateSystem]],  # value
                                    _type.HRESULT]


class IMediaFrameSourceInfo2(_inspectable.IInspectable):
    get_ProfileId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_VideoProfileMediaDescription: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Media_Capture.IMediaCaptureVideoProfileMediaDescription]]],  # value
                                                _type.HRESULT]


class IMediaFrameSourceInfo3(_inspectable.IInspectable):
    GetRelativePanel: _Callable[[_Windows_UI_WindowManagement.IDisplayRegion,  # displayRegion
                                 _Pointer[_enum.Windows.Devices.Enumeration.Panel]],  # result
                                _type.HRESULT]


class IMediaFrameSourceInfo4(_inspectable.IInspectable):
    get_IsShareable: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]


class IMultiSourceMediaFrameArrivedEventArgs(_inspectable.IInspectable):
    pass


class IMultiSourceMediaFrameReader(_inspectable.IInspectable):
    add_FrameArrived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMultiSourceMediaFrameReader, IMultiSourceMediaFrameArrivedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_FrameArrived: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    TryAcquireLatestFrame: _Callable[[_Pointer[IMultiSourceMediaFrameReference]],  # value
                                     _type.HRESULT]
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.Capture.Frames.MultiSourceMediaFrameReaderStartStatus]]],  # operation
                          _type.HRESULT]
    StopAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                         _type.HRESULT]


class IMultiSourceMediaFrameReader2(_inspectable.IInspectable):
    put_AcquisitionMode: _Callable[[_enum.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode],  # value
                                   _type.HRESULT]
    get_AcquisitionMode: _Callable[[_Pointer[_enum.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode]],  # value
                                   _type.HRESULT]


class IMultiSourceMediaFrameReference(_inspectable.IInspectable):
    TryGetFrameReferenceBySourceId: _Callable[[_type.HSTRING,  # sourceId
                                               _Pointer[IMediaFrameReference]],  # value
                                              _type.HRESULT]


class IVideoMediaFrame(_inspectable.IInspectable):
    get_FrameReference: _Callable[[_Pointer[IMediaFrameReference]],  # value
                                  _type.HRESULT]
    get_VideoFormat: _Callable[[_Pointer[IVideoMediaFrameFormat]],  # value
                               _type.HRESULT]
    get_SoftwareBitmap: _Callable[[_Pointer[_Windows_Graphics_Imaging.ISoftwareBitmap]],  # value
                                  _type.HRESULT]
    get_Direct3DSurface: _Callable[[_Pointer[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface]],  # value
                                   _type.HRESULT]
    get_CameraIntrinsics: _Callable[[_Pointer[_Windows_Media_Devices_Core.ICameraIntrinsics]],  # value
                                    _type.HRESULT]
    get_InfraredMediaFrame: _Callable[[_Pointer[IInfraredMediaFrame]],  # value
                                      _type.HRESULT]
    get_DepthMediaFrame: _Callable[[_Pointer[IDepthMediaFrame]],  # value
                                   _type.HRESULT]
    GetVideoFrame: _Callable[[_Pointer[_Windows_Media.IVideoFrame]],  # value
                             _type.HRESULT]


class IVideoMediaFrameFormat(_inspectable.IInspectable):
    get_MediaFrameFormat: _Callable[[_Pointer[IMediaFrameFormat]],  # value
                                    _type.HRESULT]
    get_DepthFormat: _Callable[[_Pointer[IDepthMediaFrameFormat]],  # value
                               _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]

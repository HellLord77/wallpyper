from __future__ import annotations

from typing import Callable as _Callable

from ... import Display as _Windows_Devices_Display
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IDisplayAdapter(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_struct.Windows.Graphics.DisplayAdapterId]],  # value
                      _type.HRESULT]
    get_DeviceInterfacePath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_SourceCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_PciVendorId: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_PciDeviceId: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_PciSubSystemId: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    get_PciRevision: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IDisplayAdapterStatics(_inspectable.IInspectable):
    FromId: _Callable[[_struct.Windows.Graphics.DisplayAdapterId,  # id
                       _Pointer[IDisplayAdapter]],  # result
                      _type.HRESULT]

    _factory = True


class IDisplayDevice(_inspectable.IInspectable):
    CreateScanoutSource: _Callable[[IDisplayTarget,  # target
                                    _Pointer[IDisplaySource]],  # result
                                   _type.HRESULT]
    CreatePrimary: _Callable[[IDisplayTarget,  # target
                              IDisplayPrimaryDescription,  # desc
                              _Pointer[IDisplaySurface]],  # result
                             _type.HRESULT]
    CreateTaskPool: _Callable[[_Pointer[IDisplayTaskPool]],  # result
                              _type.HRESULT]
    CreatePeriodicFence: _Callable[[IDisplayTarget,  # target
                                    _struct.Windows.Foundation.TimeSpan,  # offsetFromVBlank
                                    _Pointer[IDisplayFence]],  # result
                                   _type.HRESULT]
    WaitForVBlank: _Callable[[IDisplaySource],  # source
                             _type.HRESULT]
    CreateSimpleScanout: _Callable[[IDisplaySource,  # pSource
                                    IDisplaySurface,  # pSurface
                                    _type.UINT32,  # SubResourceIndex
                                    _type.UINT32,  # SyncInterval
                                    _Pointer[IDisplayScanout]],  # result
                                   _type.HRESULT]
    IsCapabilitySupported: _Callable[[_enum.Windows.Devices.Display.Core.DisplayDeviceCapability,  # capability
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]


class IDisplayDevice2(_inspectable.IInspectable):
    CreateSimpleScanoutWithDirtyRectsAndOptions: _Callable[[IDisplaySource,  # source
                                                            IDisplaySurface,  # surface
                                                            _type.UINT32,  # subresourceIndex
                                                            _type.UINT32,  # syncInterval
                                                            _Windows_Foundation_Collections.IIterable[_struct.Windows.Graphics.RectInt32],  # dirtyRects
                                                            _enum.Windows.Devices.Display.Core.DisplayScanoutOptions,  # options
                                                            _Pointer[IDisplayScanout]],  # result
                                                           _type.HRESULT]


class IDisplayFence(_inspectable.IInspectable):
    pass


class IDisplayManager(_inspectable.IInspectable):
    GetCurrentTargets: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IDisplayTarget]]],  # result
                                 _type.HRESULT]
    GetCurrentAdapters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IDisplayAdapter]]],  # result
                                  _type.HRESULT]
    TryAcquireTarget: _Callable[[IDisplayTarget,  # target
                                 _Pointer[_enum.Windows.Devices.Display.Core.DisplayManagerResult]],  # result
                                _type.HRESULT]
    ReleaseTarget: _Callable[[IDisplayTarget],  # target
                             _type.HRESULT]
    TryReadCurrentStateForAllTargets: _Callable[[_Pointer[IDisplayManagerResultWithState]],  # result
                                                _type.HRESULT]
    TryAcquireTargetsAndReadCurrentState: _Callable[[_Windows_Foundation_Collections.IIterable[IDisplayTarget],  # targets
                                                     _Pointer[IDisplayManagerResultWithState]],  # result
                                                    _type.HRESULT]
    TryAcquireTargetsAndCreateEmptyState: _Callable[[_Windows_Foundation_Collections.IIterable[IDisplayTarget],  # targets
                                                     _Pointer[IDisplayManagerResultWithState]],  # result
                                                    _type.HRESULT]
    TryAcquireTargetsAndCreateSubstate: _Callable[[IDisplayState,  # existingState
                                                   _Windows_Foundation_Collections.IIterable[IDisplayTarget],  # targets
                                                   _Pointer[IDisplayManagerResultWithState]],  # result
                                                  _type.HRESULT]
    CreateDisplayDevice: _Callable[[IDisplayAdapter,  # adapter
                                    _Pointer[IDisplayDevice]],  # result
                                   _type.HRESULT]
    add_Enabled: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayManager, IDisplayManagerEnabledEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Enabled: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Disabled: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayManager, IDisplayManagerDisabledEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Disabled: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayManager, IDisplayManagerChangedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_PathsFailedOrInvalidated: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayManager, IDisplayManagerPathsFailedOrInvalidatedEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_PathsFailedOrInvalidated: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IDisplayManagerChangedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IDisplayManagerDisabledEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IDisplayManagerEnabledEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IDisplayManagerPathsFailedOrInvalidatedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IDisplayManagerResultWithState(_inspectable.IInspectable):
    get_ErrorCode: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplayManagerResult]],  # value
                             _type.HRESULT]
    get_ExtendedErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # value
                                     _type.HRESULT]
    get_State: _Callable[[_Pointer[IDisplayState]],  # value
                         _type.HRESULT]


class IDisplayManagerStatics(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.Devices.Display.Core.DisplayManagerOptions,  # options
                       _Pointer[IDisplayManager]],  # result
                      _type.HRESULT]

    _factory = True


class IDisplayModeInfo(_inspectable.IInspectable):
    get_SourceResolution: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                                    _type.HRESULT]
    get_IsStereo: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_SourcePixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]],  # value
                                     _type.HRESULT]
    get_TargetResolution: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                                    _type.HRESULT]
    get_PresentationRate: _Callable[[_Pointer[_struct.Windows.Devices.Display.Core.DisplayPresentationRate]],  # value
                                    _type.HRESULT]
    get_IsInterlaced: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    GetWireFormatSupportedBitsPerChannel: _Callable[[_enum.Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding,  # encoding
                                                     _Pointer[_enum.Windows.Devices.Display.Core.DisplayBitsPerChannel]],  # result
                                                    _type.HRESULT]
    IsWireFormatSupported: _Callable[[IDisplayWireFormat,  # wireFormat
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IDisplayModeInfo2(_inspectable.IInspectable):
    get_PhysicalPresentationRate: _Callable[[_Pointer[_struct.Windows.Devices.Display.Core.DisplayPresentationRate]],  # value
                                            _type.HRESULT]


class IDisplayPath(_inspectable.IInspectable):
    get_View: _Callable[[_Pointer[IDisplayView]],  # value
                        _type.HRESULT]
    get_Target: _Callable[[_Pointer[IDisplayTarget]],  # value
                          _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplayPathStatus]],  # value
                          _type.HRESULT]
    get_SourceResolution: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Graphics.SizeInt32]]],  # value
                                    _type.HRESULT]
    put_SourceResolution: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Graphics.SizeInt32]],  # value
                                    _type.HRESULT]
    get_SourcePixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]],  # value
                                     _type.HRESULT]
    put_SourcePixelFormat: _Callable[[_enum.Windows.Graphics.DirectX.DirectXPixelFormat],  # value
                                     _type.HRESULT]
    get_IsStereo: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsStereo: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_TargetResolution: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Graphics.SizeInt32]]],  # value
                                    _type.HRESULT]
    put_TargetResolution: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Graphics.SizeInt32]],  # value
                                    _type.HRESULT]
    get_PresentationRate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Devices.Display.Core.DisplayPresentationRate]]],  # value
                                    _type.HRESULT]
    put_PresentationRate: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Devices.Display.Core.DisplayPresentationRate]],  # value
                                    _type.HRESULT]
    get_IsInterlaced: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                                _type.HRESULT]
    put_IsInterlaced: _Callable[[_Windows_Foundation.IReference[_type.boolean]],  # value
                                _type.HRESULT]
    get_WireFormat: _Callable[[_Pointer[IDisplayWireFormat]],  # value
                              _type.HRESULT]
    put_WireFormat: _Callable[[IDisplayWireFormat],  # value
                              _type.HRESULT]
    get_Rotation: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplayRotation]],  # value
                            _type.HRESULT]
    put_Rotation: _Callable[[_enum.Windows.Devices.Display.Core.DisplayRotation],  # value
                            _type.HRESULT]
    get_Scaling: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplayPathScaling]],  # value
                           _type.HRESULT]
    put_Scaling: _Callable[[_enum.Windows.Devices.Display.Core.DisplayPathScaling],  # value
                           _type.HRESULT]
    FindModes: _Callable[[_enum.Windows.Devices.Display.Core.DisplayModeQueryOptions,  # flags
                          _Pointer[_Windows_Foundation_Collections.IVectorView[IDisplayModeInfo]]],  # result
                         _type.HRESULT]
    ApplyPropertiesFromMode: _Callable[[IDisplayModeInfo],  # modeResult
                                       _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IDisplayPath2(_inspectable.IInspectable):
    get_PhysicalPresentationRate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Devices.Display.Core.DisplayPresentationRate]]],  # value
                                            _type.HRESULT]
    put_PhysicalPresentationRate: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Devices.Display.Core.DisplayPresentationRate]],  # value
                                            _type.HRESULT]


class IDisplayPrimaryDescription(_inspectable.IInspectable):
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Format: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]],  # value
                          _type.HRESULT]
    get_ColorSpace: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXColorSpace]],  # value
                              _type.HRESULT]
    get_IsStereo: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_MultisampleDescription: _Callable[[_Pointer[_struct.Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription]],  # value
                                          _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IDisplayPrimaryDescriptionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.UINT32,  # width
                               _type.UINT32,  # height
                               _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # pixelFormat
                               _enum.Windows.Graphics.DirectX.DirectXColorSpace,  # colorSpace
                               _type.boolean,  # isStereo
                               _struct.Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription,  # multisampleDescription
                               _Pointer[IDisplayPrimaryDescription]],  # value
                              _type.HRESULT]

    _factory = True


class IDisplayPrimaryDescriptionStatics(_inspectable.IInspectable):
    CreateWithProperties: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_struct.GUID, _inspectable.IInspectable]],  # extraProperties
                                     _type.UINT32,  # width
                                     _type.UINT32,  # height
                                     _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # pixelFormat
                                     _enum.Windows.Graphics.DirectX.DirectXColorSpace,  # colorSpace
                                     _type.boolean,  # isStereo
                                     _struct.Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription,  # multisampleDescription
                                     _Pointer[IDisplayPrimaryDescription]],  # result
                                    _type.HRESULT]

    _factory = True


class IDisplayScanout(_inspectable.IInspectable):
    pass


class IDisplaySource(_inspectable.IInspectable):
    get_AdapterId: _Callable[[_Pointer[_struct.Windows.Graphics.DisplayAdapterId]],  # value
                             _type.HRESULT]
    get_SourceId: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    GetMetadata: _Callable[[_struct.GUID,  # Key
                            _Pointer[_Windows_Storage_Streams.IBuffer]],  # result
                           _type.HRESULT]


class IDisplaySource2(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplaySourceStatus]],  # value
                          _type.HRESULT]
    add_StatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplaySource, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IDisplayState(_inspectable.IInspectable):
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsStale: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_Targets: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IDisplayTarget]]],  # value
                           _type.HRESULT]
    get_Views: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IDisplayView]]],  # value
                         _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    ConnectTarget: _Callable[[IDisplayTarget,  # target
                              _Pointer[IDisplayPath]],  # result
                             _type.HRESULT]
    ConnectTargetToView: _Callable[[IDisplayTarget,  # target
                                    IDisplayView,  # view
                                    _Pointer[IDisplayPath]],  # result
                                   _type.HRESULT]
    CanConnectTargetToView: _Callable[[IDisplayTarget,  # target
                                       IDisplayView,  # view
                                       _Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    GetViewForTarget: _Callable[[IDisplayTarget,  # target
                                 _Pointer[IDisplayView]],  # result
                                _type.HRESULT]
    GetPathForTarget: _Callable[[IDisplayTarget,  # target
                                 _Pointer[IDisplayPath]],  # result
                                _type.HRESULT]
    DisconnectTarget: _Callable[[IDisplayTarget],  # target
                                _type.HRESULT]
    TryFunctionalize: _Callable[[_enum.Windows.Devices.Display.Core.DisplayStateFunctionalizeOptions,  # options
                                 _Pointer[IDisplayStateOperationResult]],  # result
                                _type.HRESULT]
    TryApply: _Callable[[_enum.Windows.Devices.Display.Core.DisplayStateApplyOptions,  # options
                         _Pointer[IDisplayStateOperationResult]],  # result
                        _type.HRESULT]
    Clone: _Callable[[_Pointer[IDisplayState]],  # result
                     _type.HRESULT]


class IDisplayStateOperationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplayStateOperationStatus]],  # value
                          _type.HRESULT]
    get_ExtendedErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # value
                                     _type.HRESULT]


class IDisplaySurface(_inspectable.IInspectable):
    pass


class IDisplayTarget(_inspectable.IInspectable):
    get_Adapter: _Callable[[_Pointer[IDisplayAdapter]],  # value
                           _type.HRESULT]
    get_DeviceInterfacePath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_AdapterRelativeId: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    get_IsConnected: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsVirtualModeEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsVirtualTopologyEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_UsageKind: _Callable[[_Pointer[_enum.Windows.Devices.Display.DisplayMonitorUsageKind]],  # value
                             _type.HRESULT]
    get_MonitorPersistence: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplayTargetPersistence]],  # value
                                      _type.HRESULT]
    get_StableMonitorId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    TryGetMonitor: _Callable[[_Pointer[_Windows_Devices_Display.IDisplayMonitor]],  # result
                             _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    get_IsStale: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    IsSame: _Callable[[IDisplayTarget,  # otherTarget
                       _Pointer[_type.boolean]],  # result
                      _type.HRESULT]
    IsEqual: _Callable[[IDisplayTarget,  # otherTarget
                        _Pointer[_type.boolean]],  # result
                       _type.HRESULT]


class IDisplayTask(_inspectable.IInspectable):
    SetScanout: _Callable[[IDisplayScanout],  # scanout
                          _type.HRESULT]
    SetWait: _Callable[[IDisplayFence,  # readyFence
                        _type.UINT64],  # readyFenceValue
                       _type.HRESULT]


class IDisplayTask2(_inspectable.IInspectable):
    SetSignal: _Callable[[_enum.Windows.Devices.Display.Core.DisplayTaskSignalKind,  # signalKind
                          IDisplayFence],  # fence
                         _type.HRESULT]


class IDisplayTaskPool(_inspectable.IInspectable):
    CreateTask: _Callable[[_Pointer[IDisplayTask]],  # result
                          _type.HRESULT]
    ExecuteTask: _Callable[[IDisplayTask],  # task
                           _type.HRESULT]


class IDisplayTaskPool2(_inspectable.IInspectable):
    TryExecuteTask: _Callable[[IDisplayTask,  # task
                               _Pointer[IDisplayTaskResult]],  # result
                              _type.HRESULT]


class IDisplayTaskResult(_inspectable.IInspectable):
    get_PresentStatus: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplayPresentStatus]],  # value
                                 _type.HRESULT]
    get_PresentId: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    get_SourceStatus: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplaySourceStatus]],  # value
                                _type.HRESULT]


class IDisplayView(_inspectable.IInspectable):
    get_Paths: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IDisplayPath]]],  # value
                         _type.HRESULT]
    get_ContentResolution: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Graphics.SizeInt32]]],  # value
                                     _type.HRESULT]
    put_ContentResolution: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Graphics.SizeInt32]],  # value
                                     _type.HRESULT]
    SetPrimaryPath: _Callable[[IDisplayPath],  # path
                              _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IDisplayWireFormat(_inspectable.IInspectable):
    get_PixelEncoding: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding]],  # value
                                 _type.HRESULT]
    get_BitsPerChannel: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    get_ColorSpace: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplayWireFormatColorSpace]],  # value
                              _type.HRESULT]
    get_Eotf: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplayWireFormatEotf]],  # value
                        _type.HRESULT]
    get_HdrMetadata: _Callable[[_Pointer[_enum.Windows.Devices.Display.Core.DisplayWireFormatHdrMetadata]],  # value
                               _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IDisplayWireFormatFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_enum.Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding,  # pixelEncoding
                               _type.INT32,  # bitsPerChannel
                               _enum.Windows.Devices.Display.Core.DisplayWireFormatColorSpace,  # colorSpace
                               _enum.Windows.Devices.Display.Core.DisplayWireFormatEotf,  # eotf
                               _enum.Windows.Devices.Display.Core.DisplayWireFormatHdrMetadata,  # hdrMetadata
                               _Pointer[IDisplayWireFormat]],  # value
                              _type.HRESULT]

    _factory = True


class IDisplayWireFormatStatics(_inspectable.IInspectable):
    CreateWithProperties: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_struct.GUID, _inspectable.IInspectable]],  # extraProperties
                                     _enum.Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding,  # pixelEncoding
                                     _type.INT32,  # bitsPerChannel
                                     _enum.Windows.Devices.Display.Core.DisplayWireFormatColorSpace,  # colorSpace
                                     _enum.Windows.Devices.Display.Core.DisplayWireFormatEotf,  # eotf
                                     _enum.Windows.Devices.Display.Core.DisplayWireFormatHdrMetadata,  # hdrMetadata
                                     _Pointer[IDisplayWireFormat]],  # result
                                    _type.HRESULT]

    _factory = True

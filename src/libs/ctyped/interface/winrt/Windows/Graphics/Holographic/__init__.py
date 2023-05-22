from __future__ import annotations

from typing import Callable as _Callable

from ..DirectX import Direct3D11 as _Windows_Graphics_DirectX_Direct3D11
from ... import Foundation as _Windows_Foundation
from ... import Perception as _Windows_Perception
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Perception import Spatial as _Windows_Perception_Spatial
from ...UI import Core as _Windows_UI_Core
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IHolographicCamera(_inspectable.IInspectable):
    get_RenderTargetSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                    _type.HRESULT]
    get_ViewportScaleFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_ViewportScaleFactor: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_IsStereo: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    SetNearPlaneDistance: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    SetFarPlaneDistance: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]


class IHolographicCamera2(_inspectable.IInspectable):
    get_LeftViewportParameters: _Callable[[_Pointer[IHolographicCameraViewportParameters]],  # result
                                          _type.HRESULT]
    get_RightViewportParameters: _Callable[[_Pointer[IHolographicCameraViewportParameters]],  # result
                                           _type.HRESULT]
    get_Display: _Callable[[_Pointer[IHolographicDisplay]],  # result
                           _type.HRESULT]


class IHolographicCamera3(_inspectable.IInspectable):
    get_IsPrimaryLayerEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsPrimaryLayerEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_MaxQuadLayerCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    get_QuadLayers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHolographicQuadLayer]]],  # value
                              _type.HRESULT]


class IHolographicCamera4(_inspectable.IInspectable):
    get_CanOverrideViewport: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]


class IHolographicCamera5(_inspectable.IInspectable):
    get_IsHardwareContentProtectionSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                        _type.HRESULT]
    get_IsHardwareContentProtectionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                      _type.HRESULT]
    put_IsHardwareContentProtectionEnabled: _Callable[[_type.boolean],  # value
                                                      _type.HRESULT]


class IHolographicCamera6(_inspectable.IInspectable):
    get_ViewConfiguration: _Callable[[_Pointer[IHolographicViewConfiguration]],  # value
                                     _type.HRESULT]


class IHolographicCameraPose(_inspectable.IInspectable):
    get_HolographicCamera: _Callable[[_Pointer[IHolographicCamera]],  # value
                                     _type.HRESULT]
    get_Viewport: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                            _type.HRESULT]
    TryGetViewTransform: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                    _Pointer[_Windows_Foundation.IReference[_struct.Windows.Graphics.Holographic.HolographicStereoTransform]]],  # value
                                   _type.HRESULT]
    get_ProjectionTransform: _Callable[[_Pointer[_struct.Windows.Graphics.Holographic.HolographicStereoTransform]],  # value
                                       _type.HRESULT]
    TryGetCullingFrustum: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                     _Pointer[_Windows_Foundation.IReference[_struct.Windows.Perception.Spatial.SpatialBoundingFrustum]]],  # value
                                    _type.HRESULT]
    TryGetVisibleFrustum: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                     _Pointer[_Windows_Foundation.IReference[_struct.Windows.Perception.Spatial.SpatialBoundingFrustum]]],  # value
                                    _type.HRESULT]
    get_NearPlaneDistance: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    get_FarPlaneDistance: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]


class IHolographicCameraPose2(_inspectable.IInspectable):
    OverrideViewTransform: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                      _struct.Windows.Graphics.Holographic.HolographicStereoTransform],  # coordinateSystemToViewTransform
                                     _type.HRESULT]
    OverrideProjectionTransform: _Callable[[_struct.Windows.Graphics.Holographic.HolographicStereoTransform],  # projectionTransform
                                           _type.HRESULT]
    OverrideViewport: _Callable[[_struct.Windows.Foundation.Rect,  # leftViewport
                                 _struct.Windows.Foundation.Rect],  # rightViewport
                                _type.HRESULT]


class IHolographicCameraRenderingParameters(_inspectable.IInspectable):
    SetFocusPoint: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                              _struct.Windows.Foundation.Numerics.Vector3],  # position
                             _type.HRESULT]
    SetFocusPointWithNormal: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                        _struct.Windows.Foundation.Numerics.Vector3,  # position
                                        _struct.Windows.Foundation.Numerics.Vector3],  # normal
                                       _type.HRESULT]
    SetFocusPointWithNormalLinearVelocity: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                                      _struct.Windows.Foundation.Numerics.Vector3,  # position
                                                      _struct.Windows.Foundation.Numerics.Vector3,  # normal
                                                      _struct.Windows.Foundation.Numerics.Vector3],  # linearVelocity
                                                     _type.HRESULT]
    get_Direct3D11Device: _Callable[[_Pointer[_Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice]],  # value
                                    _type.HRESULT]
    get_Direct3D11BackBuffer: _Callable[[_Pointer[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface]],  # value
                                        _type.HRESULT]


class IHolographicCameraRenderingParameters2(_inspectable.IInspectable):
    get_ReprojectionMode: _Callable[[_Pointer[_enum.Windows.Graphics.Holographic.HolographicReprojectionMode]],  # value
                                    _type.HRESULT]
    put_ReprojectionMode: _Callable[[_enum.Windows.Graphics.Holographic.HolographicReprojectionMode],  # value
                                    _type.HRESULT]
    CommitDirect3D11DepthBuffer: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface],  # value
                                           _type.HRESULT]


class IHolographicCameraRenderingParameters3(_inspectable.IInspectable):
    get_IsContentProtectionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_IsContentProtectionEnabled: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]


class IHolographicCameraRenderingParameters4(_inspectable.IInspectable):
    get_DepthReprojectionMethod: _Callable[[_Pointer[_enum.Windows.Graphics.Holographic.HolographicDepthReprojectionMethod]],  # value
                                           _type.HRESULT]
    put_DepthReprojectionMethod: _Callable[[_enum.Windows.Graphics.Holographic.HolographicDepthReprojectionMethod],  # value
                                           _type.HRESULT]


class IHolographicCameraViewportParameters(_inspectable.IInspectable):
    get_HiddenAreaMesh: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                   _Pointer[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]]],  # value
                                  _type.HRESULT]
    get_VisibleAreaMesh: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                    _Pointer[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]]],  # value
                                   _type.HRESULT]


class IHolographicDisplay(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_MaxViewportSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                   _type.HRESULT]
    get_IsStereo: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsOpaque: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_AdapterId: _Callable[[_Pointer[_struct.Windows.Graphics.Holographic.HolographicAdapterId]],  # value
                             _type.HRESULT]
    get_SpatialLocator: _Callable[[_Pointer[_Windows_Perception_Spatial.ISpatialLocator]],  # value
                                  _type.HRESULT]


class IHolographicDisplay2(_inspectable.IInspectable):
    get_RefreshRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]


class IHolographicDisplay3(_inspectable.IInspectable):
    TryGetViewConfiguration: _Callable[[_enum.Windows.Graphics.Holographic.HolographicViewConfigurationKind,  # kind
                                        _Pointer[IHolographicViewConfiguration]],  # result
                                       _type.HRESULT]


class IHolographicDisplayStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IHolographicDisplay]],  # result
                          _type.HRESULT]


class IHolographicFrame(_inspectable.IInspectable):
    get_AddedCameras: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IHolographicCamera]]],  # value
                                _type.HRESULT]
    get_RemovedCameras: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IHolographicCamera]]],  # value
                                  _type.HRESULT]
    GetRenderingParameters: _Callable[[IHolographicCameraPose,  # cameraPose
                                       _Pointer[IHolographicCameraRenderingParameters]],  # value
                                      _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_CurrentPrediction: _Callable[[_Pointer[IHolographicFramePrediction]],  # value
                                     _type.HRESULT]
    UpdateCurrentPrediction: _Callable[[],
                                       _type.HRESULT]
    PresentUsingCurrentPrediction: _Callable[[_Pointer[_enum.Windows.Graphics.Holographic.HolographicFramePresentResult]],  # result
                                             _type.HRESULT]
    PresentUsingCurrentPredictionWithBehavior: _Callable[[_enum.Windows.Graphics.Holographic.HolographicFramePresentWaitBehavior,  # waitBehavior
                                                          _Pointer[_enum.Windows.Graphics.Holographic.HolographicFramePresentResult]],  # result
                                                         _type.HRESULT]
    WaitForFrameToFinish: _Callable[[],
                                    _type.HRESULT]


class IHolographicFrame2(_inspectable.IInspectable):
    GetQuadLayerUpdateParameters: _Callable[[IHolographicQuadLayer,  # layer
                                             _Pointer[IHolographicQuadLayerUpdateParameters]],  # value
                                            _type.HRESULT]


class IHolographicFrame3(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_struct.Windows.Graphics.Holographic.HolographicFrameId]],  # value
                      _type.HRESULT]


class IHolographicFramePrediction(_inspectable.IInspectable):
    get_CameraPoses: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IHolographicCameraPose]]],  # value
                               _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_Windows_Perception.IPerceptionTimestamp]],  # value
                             _type.HRESULT]


class IHolographicFramePresentationMonitor(_inspectable.IInspectable):
    ReadReports: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IHolographicFramePresentationReport]]],  # result
                           _type.HRESULT]


class IHolographicFramePresentationReport(_inspectable.IInspectable):
    CompositorGpuDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    AppGpuDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                              _type.HRESULT]
    AppGpuOverrun: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    MissedPresentationOpportunityCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                                  _type.HRESULT]
    PresentationCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]


class IHolographicFrameRenderingReport(_inspectable.IInspectable):
    get_FrameId: _Callable[[_Pointer[_struct.Windows.Graphics.Holographic.HolographicFrameId]],  # value
                           _type.HRESULT]
    get_MissedLatchCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    get_SystemRelativeFrameReadyTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                                _type.HRESULT]
    get_SystemRelativeActualGpuFinishTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                                     _type.HRESULT]
    get_SystemRelativeTargetLatchTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                                 _type.HRESULT]


class IHolographicFrameScanoutMonitor(_inspectable.IInspectable):
    ReadReports: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHolographicFrameScanoutReport]]],  # result
                           _type.HRESULT]


class IHolographicFrameScanoutReport(_inspectable.IInspectable):
    get_RenderingReport: _Callable[[_Pointer[IHolographicFrameRenderingReport]],  # value
                                   _type.HRESULT]
    get_MissedScanoutCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    get_SystemRelativeLatchTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                           _type.HRESULT]
    get_SystemRelativeScanoutStartTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                                  _type.HRESULT]
    get_SystemRelativePhotonTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                            _type.HRESULT]


class IHolographicQuadLayer(_inspectable.IInspectable):
    get_PixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]],  # value
                               _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                        _type.HRESULT]


class IHolographicQuadLayerFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_struct.Windows.Foundation.Size,  # size
                       _Pointer[IHolographicQuadLayer]],  # value
                      _type.HRESULT]
    CreateWithPixelFormat: _Callable[[_struct.Windows.Foundation.Size,  # size
                                      _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # pixelFormat
                                      _Pointer[IHolographicQuadLayer]],  # value
                                     _type.HRESULT]


class IHolographicQuadLayerUpdateParameters(_inspectable.IInspectable):
    AcquireBufferToUpdateContent: _Callable[[_Pointer[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface]],  # value
                                            _type.HRESULT]
    UpdateViewport: _Callable[[_struct.Windows.Foundation.Rect],  # value
                              _type.HRESULT]
    UpdateContentProtectionEnabled: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    UpdateExtents: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                             _type.HRESULT]
    UpdateLocationWithStationaryMode: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                                 _struct.Windows.Foundation.Numerics.Vector3,  # position
                                                 _struct.Windows.Foundation.Numerics.Quaternion],  # orientation
                                                _type.HRESULT]
    UpdateLocationWithDisplayRelativeMode: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # position
                                                      _struct.Windows.Foundation.Numerics.Quaternion],  # orientation
                                                     _type.HRESULT]


class IHolographicQuadLayerUpdateParameters2(_inspectable.IInspectable):
    get_CanAcquireWithHardwareProtection: _Callable[[_Pointer[_type.boolean]],  # value
                                                    _type.HRESULT]
    AcquireBufferToUpdateContentWithHardwareProtection: _Callable[[_Pointer[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface]],  # value
                                                                  _type.HRESULT]


class IHolographicSpace(_inspectable.IInspectable):
    get_PrimaryAdapterId: _Callable[[_Pointer[_struct.Windows.Graphics.Holographic.HolographicAdapterId]],  # value
                                    _type.HRESULT]
    SetDirect3D11Device: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice],  # value
                                   _type.HRESULT]
    add_CameraAdded: _Callable[[_Windows_Foundation.ITypedEventHandler[IHolographicSpace, IHolographicSpaceCameraAddedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # cookie
                               _type.HRESULT]
    remove_CameraAdded: _Callable[[_struct.EventRegistrationToken],  # cookie
                                  _type.HRESULT]
    add_CameraRemoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IHolographicSpace, IHolographicSpaceCameraRemovedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                 _type.HRESULT]
    remove_CameraRemoved: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]
    CreateNextFrame: _Callable[[_Pointer[IHolographicFrame]],  # value
                               _type.HRESULT]


class IHolographicSpace2(_inspectable.IInspectable):
    get_UserPresence: _Callable[[_Pointer[_enum.Windows.Graphics.Holographic.HolographicSpaceUserPresence]],  # value
                                _type.HRESULT]
    add_UserPresenceChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IHolographicSpace, _inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_UserPresenceChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    WaitForNextFrameReady: _Callable[[],
                                     _type.HRESULT]
    WaitForNextFrameReadyWithHeadStart: _Callable[[_struct.Windows.Foundation.TimeSpan],  # requestedHeadStartDuration
                                                  _type.HRESULT]
    CreateFramePresentationMonitor: _Callable[[_type.UINT32,  # maxQueuedReports
                                               _Pointer[IHolographicFramePresentationMonitor]],  # result
                                              _type.HRESULT]


class IHolographicSpace3(_inspectable.IInspectable):
    CreateFrameScanoutMonitor: _Callable[[_type.UINT32,  # maxQueuedReports
                                          _Pointer[IHolographicFrameScanoutMonitor]],  # result
                                         _type.HRESULT]


class IHolographicSpaceCameraAddedEventArgs(_inspectable.IInspectable):
    get_Camera: _Callable[[_Pointer[IHolographicCamera]],  # value
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IHolographicSpaceCameraRemovedEventArgs(_inspectable.IInspectable):
    get_Camera: _Callable[[_Pointer[IHolographicCamera]],  # value
                          _type.HRESULT]


class IHolographicSpaceStatics(_inspectable.IInspectable, factory=True):
    CreateForCoreWindow: _Callable[[_Windows_UI_Core.ICoreWindow,  # window
                                    _Pointer[IHolographicSpace]],  # value
                                   _type.HRESULT]


class IHolographicSpaceStatics2(_inspectable.IInspectable, factory=True):
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    add_IsAvailableChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_IsAvailableChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class IHolographicSpaceStatics3(_inspectable.IInspectable, factory=True):
    get_IsConfigured: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]


class IHolographicViewConfiguration(_inspectable.IInspectable):
    get_NativeRenderTargetSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                          _type.HRESULT]
    get_RenderTargetSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                    _type.HRESULT]
    RequestRenderTargetSize: _Callable[[_struct.Windows.Foundation.Size,  # size
                                        _Pointer[_struct.Windows.Foundation.Size]],  # result
                                       _type.HRESULT]
    get_SupportedPixelFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]]],  # value
                                         _type.HRESULT]
    get_PixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]],  # value
                               _type.HRESULT]
    put_PixelFormat: _Callable[[_enum.Windows.Graphics.DirectX.DirectXPixelFormat],  # value
                               _type.HRESULT]
    get_IsStereo: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_RefreshRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.Graphics.Holographic.HolographicViewConfigurationKind]],  # value
                        _type.HRESULT]
    get_Display: _Callable[[_Pointer[IHolographicDisplay]],  # value
                           _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]


class IHolographicViewConfiguration2(_inspectable.IInspectable):
    get_SupportedDepthReprojectionMethods: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Graphics.Holographic.HolographicDepthReprojectionMethod]]],  # value
                                                     _type.HRESULT]

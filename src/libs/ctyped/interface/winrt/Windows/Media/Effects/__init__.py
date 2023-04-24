from __future__ import annotations

from typing import Callable as _Callable

from .. import Editing as _Windows_Media_Editing
from .. import MediaProperties as _Windows_Media_MediaProperties
from ... import Foundation as _Windows_Foundation
from ... import Media as _Windows_Media
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics.DirectX import Direct3D11 as _Windows_Graphics_DirectX_Direct3D11
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAudioCaptureEffectsManager(_inspectable.IInspectable):
    add_AudioCaptureEffectsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAudioCaptureEffectsManager, _inspectable.IInspectable],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_AudioCaptureEffectsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    GetAudioCaptureEffects: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAudioEffect]]],  # effects
                                      _type.HRESULT]


class IAudioEffect(_inspectable.IInspectable):
    get_AudioEffectType: _Callable[[_Pointer[_enum.Windows.Media.Effects.AudioEffectType]],  # value
                                   _type.HRESULT]


class IAudioEffectDefinition(_inspectable.IInspectable):
    get_ActivatableClassId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]


class IAudioEffectDefinitionFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # activatableClassId
                       _Pointer[IAudioEffectDefinition]],  # value
                      _type.HRESULT]
    CreateWithProperties: _Callable[[_type.HSTRING,  # activatableClassId
                                     _Windows_Foundation_Collections.IPropertySet,  # props
                                     _Pointer[IAudioEffectDefinition]],  # value
                                    _type.HRESULT]

    _factory = True


class IAudioEffectsManagerStatics(_inspectable.IInspectable):
    CreateAudioRenderEffectsManager: _Callable[[_type.HSTRING,  # deviceId
                                                _enum.Windows.Media.Render.AudioRenderCategory,  # category
                                                _Pointer[IAudioRenderEffectsManager]],  # value
                                               _type.HRESULT]
    CreateAudioRenderEffectsManagerWithMode: _Callable[[_type.HSTRING,  # deviceId
                                                        _enum.Windows.Media.Render.AudioRenderCategory,  # category
                                                        _enum.Windows.Media.AudioProcessing,  # mode
                                                        _Pointer[IAudioRenderEffectsManager]],  # value
                                                       _type.HRESULT]
    CreateAudioCaptureEffectsManager: _Callable[[_type.HSTRING,  # deviceId
                                                 _enum.Windows.Media.Capture.MediaCategory,  # category
                                                 _Pointer[IAudioCaptureEffectsManager]],  # value
                                                _type.HRESULT]
    CreateAudioCaptureEffectsManagerWithMode: _Callable[[_type.HSTRING,  # deviceId
                                                         _enum.Windows.Media.Capture.MediaCategory,  # category
                                                         _enum.Windows.Media.AudioProcessing,  # mode
                                                         _Pointer[IAudioCaptureEffectsManager]],  # value
                                                        _type.HRESULT]

    _factory = True


class IAudioRenderEffectsManager(_inspectable.IInspectable):
    add_AudioRenderEffectsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAudioRenderEffectsManager, _inspectable.IInspectable],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_AudioRenderEffectsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    GetAudioRenderEffects: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAudioEffect]]],  # effects
                                     _type.HRESULT]


class IAudioRenderEffectsManager2(_inspectable.IInspectable):
    EffectsProviderThumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]],  # value
                                        _type.HRESULT]
    EffectsProviderSettingsLabel: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]
    ShowSettingsUI: _Callable[[],
                              _type.HRESULT]


class IBasicAudioEffect(_inspectable.IInspectable):
    get_UseInputFrameForOutput: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_SupportedEncodingProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Media_MediaProperties.IAudioEncodingProperties]]],  # value
                                               _type.HRESULT]
    SetEncodingProperties: _Callable[[_Windows_Media_MediaProperties.IAudioEncodingProperties],  # encodingProperties
                                     _type.HRESULT]
    ProcessFrame: _Callable[[IProcessAudioFrameContext],  # context
                            _type.HRESULT]
    Close: _Callable[[_enum.Windows.Media.Effects.MediaEffectClosedReason],  # reason
                     _type.HRESULT]
    DiscardQueuedFrames: _Callable[[],
                                   _type.HRESULT]


class IBasicVideoEffect(_inspectable.IInspectable):
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_SupportedMemoryTypes: _Callable[[_Pointer[_enum.Windows.Media.Effects.MediaMemoryTypes]],  # value
                                        _type.HRESULT]
    get_TimeIndependent: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_SupportedEncodingProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Media_MediaProperties.IVideoEncodingProperties]]],  # value
                                               _type.HRESULT]
    SetEncodingProperties: _Callable[[_Windows_Media_MediaProperties.IVideoEncodingProperties,  # encodingProperties
                                      _Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice],  # device
                                     _type.HRESULT]
    ProcessFrame: _Callable[[IProcessVideoFrameContext],  # context
                            _type.HRESULT]
    Close: _Callable[[_enum.Windows.Media.Effects.MediaEffectClosedReason],  # reason
                     _type.HRESULT]
    DiscardQueuedFrames: _Callable[[],
                                   _type.HRESULT]


class ICompositeVideoFrameContext(_inspectable.IInspectable):
    get_SurfacesToOverlay: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface]]],  # value
                                     _type.HRESULT]
    get_BackgroundFrame: _Callable[[_Pointer[_Windows_Media.IVideoFrame]],  # value
                                   _type.HRESULT]
    get_OutputFrame: _Callable[[_Pointer[_Windows_Media.IVideoFrame]],  # value
                               _type.HRESULT]
    GetOverlayForSurface: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface,  # surfaceToOverlay
                                     _Pointer[_Windows_Media_Editing.IMediaOverlay]],  # value
                                    _type.HRESULT]


class IProcessAudioFrameContext(_inspectable.IInspectable):
    get_InputFrame: _Callable[[_Pointer[_Windows_Media.IAudioFrame]],  # value
                              _type.HRESULT]
    get_OutputFrame: _Callable[[_Pointer[_Windows_Media.IAudioFrame]],  # value
                               _type.HRESULT]


class IProcessVideoFrameContext(_inspectable.IInspectable):
    get_InputFrame: _Callable[[_Pointer[_Windows_Media.IVideoFrame]],  # value
                              _type.HRESULT]
    get_OutputFrame: _Callable[[_Pointer[_Windows_Media.IVideoFrame]],  # value
                               _type.HRESULT]


class IVideoCompositor(_inspectable.IInspectable):
    get_TimeIndependent: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    SetEncodingProperties: _Callable[[_Windows_Media_MediaProperties.IVideoEncodingProperties,  # backgroundProperties
                                      _Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice],  # device
                                     _type.HRESULT]
    CompositeFrame: _Callable[[ICompositeVideoFrameContext],  # context
                              _type.HRESULT]
    Close: _Callable[[_enum.Windows.Media.Effects.MediaEffectClosedReason],  # reason
                     _type.HRESULT]
    DiscardQueuedFrames: _Callable[[],
                                   _type.HRESULT]


class IVideoCompositorDefinition(_inspectable.IInspectable):
    get_ActivatableClassId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]


class IVideoCompositorDefinitionFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # activatableClassId
                       _Pointer[IVideoCompositorDefinition]],  # value
                      _type.HRESULT]
    CreateWithProperties: _Callable[[_type.HSTRING,  # activatableClassId
                                     _Windows_Foundation_Collections.IPropertySet,  # props
                                     _Pointer[IVideoCompositorDefinition]],  # value
                                    _type.HRESULT]

    _factory = True


class IVideoEffectDefinition(_inspectable.IInspectable):
    get_ActivatableClassId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]


class IVideoEffectDefinitionFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # activatableClassId
                       _Pointer[IVideoEffectDefinition]],  # value
                      _type.HRESULT]
    CreateWithProperties: _Callable[[_type.HSTRING,  # activatableClassId
                                     _Windows_Foundation_Collections.IPropertySet,  # props
                                     _Pointer[IVideoEffectDefinition]],  # value
                                    _type.HRESULT]

    _factory = True


class IVideoTransformEffectDefinition(_inspectable.IInspectable):
    get_PaddingColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    put_PaddingColor: _Callable[[_struct.Windows.UI.Color],  # value
                                _type.HRESULT]
    get_OutputSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                              _type.HRESULT]
    put_OutputSize: _Callable[[_struct.Windows.Foundation.Size],  # value
                              _type.HRESULT]
    get_CropRectangle: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]
    put_CropRectangle: _Callable[[_struct.Windows.Foundation.Rect],  # value
                                 _type.HRESULT]
    get_Rotation: _Callable[[_Pointer[_enum.Windows.Media.MediaProperties.MediaRotation]],  # value
                            _type.HRESULT]
    put_Rotation: _Callable[[_enum.Windows.Media.MediaProperties.MediaRotation],  # value
                            _type.HRESULT]
    get_Mirror: _Callable[[_Pointer[_enum.Windows.Media.MediaProperties.MediaMirroringOptions]],  # value
                          _type.HRESULT]
    put_Mirror: _Callable[[_enum.Windows.Media.MediaProperties.MediaMirroringOptions],  # value
                          _type.HRESULT]
    put_ProcessingAlgorithm: _Callable[[_enum.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm],  # value
                                       _type.HRESULT]
    get_ProcessingAlgorithm: _Callable[[_Pointer[_enum.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm]],  # value
                                       _type.HRESULT]


class IVideoTransformEffectDefinition2(_inspectable.IInspectable):
    get_SphericalProjection: _Callable[[_Pointer[IVideoTransformSphericalProjection]],  # value
                                       _type.HRESULT]


class IVideoTransformSphericalProjection(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_FrameFormat: _Callable[[_Pointer[_enum.Windows.Media.MediaProperties.SphericalVideoFrameFormat]],  # value
                               _type.HRESULT]
    put_FrameFormat: _Callable[[_enum.Windows.Media.MediaProperties.SphericalVideoFrameFormat],  # value
                               _type.HRESULT]
    get_ProjectionMode: _Callable[[_Pointer[_enum.Windows.Media.Playback.SphericalVideoProjectionMode]],  # value
                                  _type.HRESULT]
    put_ProjectionMode: _Callable[[_enum.Windows.Media.Playback.SphericalVideoProjectionMode],  # value
                                  _type.HRESULT]
    get_HorizontalFieldOfViewInDegrees: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                  _type.HRESULT]
    put_HorizontalFieldOfViewInDegrees: _Callable[[_type.DOUBLE],  # value
                                                  _type.HRESULT]
    get_ViewOrientation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Quaternion]],  # value
                                   _type.HRESULT]
    put_ViewOrientation: _Callable[[_struct.Windows.Foundation.Numerics.Quaternion],  # value
                                   _type.HRESULT]

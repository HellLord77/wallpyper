from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Composition as _Windows_UI_Composition
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ISceneBoundingBox(_inspectable.IInspectable):
    get_Center: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                          _type.HRESULT]
    get_Extents: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                           _type.HRESULT]
    get_Max: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                       _type.HRESULT]
    get_Min: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                       _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                        _type.HRESULT]


class ISceneComponent(_inspectable.IInspectable):
    get_ComponentType: _Callable[[_Pointer[_enum.Windows.UI.Composition.Scenes.SceneComponentType]],  # value
                                 _type.HRESULT]


class ISceneComponentCollection(_inspectable.IInspectable):
    pass


class ISceneComponentFactory(_inspectable.IInspectable):
    pass


class ISceneMaterial(_inspectable.IInspectable):
    pass


class ISceneMaterialFactory(_inspectable.IInspectable):
    pass


class ISceneMaterialInput(_inspectable.IInspectable):
    pass


class ISceneMaterialInputFactory(_inspectable.IInspectable):
    pass


class ISceneMesh(_inspectable.IInspectable):
    get_Bounds: _Callable[[_Pointer[ISceneBoundingBox]],  # value
                          _type.HRESULT]
    get_PrimitiveTopology: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPrimitiveTopology]],  # value
                                     _type.HRESULT]
    put_PrimitiveTopology: _Callable[[_enum.Windows.Graphics.DirectX.DirectXPrimitiveTopology],  # value
                                     _type.HRESULT]
    FillMeshAttribute: _Callable[[_enum.Windows.UI.Composition.Scenes.SceneAttributeSemantic,  # semantic
                                  _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # format
                                  _Windows_Foundation.IMemoryBuffer],  # memory
                                 _type.HRESULT]


class ISceneMeshMaterialAttributeMap(_inspectable.IInspectable):
    pass


class ISceneMeshRendererComponent(_inspectable.IInspectable):
    get_Material: _Callable[[_Pointer[ISceneMaterial]],  # value
                            _type.HRESULT]
    put_Material: _Callable[[ISceneMaterial],  # value
                            _type.HRESULT]
    get_Mesh: _Callable[[_Pointer[ISceneMesh]],  # value
                        _type.HRESULT]
    put_Mesh: _Callable[[ISceneMesh],  # value
                        _type.HRESULT]
    get_UVMappings: _Callable[[_Pointer[ISceneMeshMaterialAttributeMap]],  # value
                              _type.HRESULT]


class ISceneMeshRendererComponentStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_UI_Composition.ICompositor,  # compositor
                       _Pointer[ISceneMeshRendererComponent]],  # result
                      _type.HRESULT]


class ISceneMeshStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_UI_Composition.ICompositor,  # compositor
                       _Pointer[ISceneMesh]],  # result
                      _type.HRESULT]


class ISceneMetallicRoughnessMaterial(_inspectable.IInspectable):
    get_BaseColorInput: _Callable[[_Pointer[ISceneMaterialInput]],  # value
                                  _type.HRESULT]
    put_BaseColorInput: _Callable[[ISceneMaterialInput],  # value
                                  _type.HRESULT]
    get_BaseColorFactor: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector4]],  # value
                                   _type.HRESULT]
    put_BaseColorFactor: _Callable[[_struct.Windows.Foundation.Numerics.Vector4],  # value
                                   _type.HRESULT]
    get_MetallicFactor: _Callable[[_Pointer[_type.FLOAT]],  # value
                                  _type.HRESULT]
    put_MetallicFactor: _Callable[[_type.FLOAT],  # value
                                  _type.HRESULT]
    get_MetallicRoughnessInput: _Callable[[_Pointer[ISceneMaterialInput]],  # value
                                          _type.HRESULT]
    put_MetallicRoughnessInput: _Callable[[ISceneMaterialInput],  # value
                                          _type.HRESULT]
    get_RoughnessFactor: _Callable[[_Pointer[_type.FLOAT]],  # value
                                   _type.HRESULT]
    put_RoughnessFactor: _Callable[[_type.FLOAT],  # value
                                   _type.HRESULT]


class ISceneMetallicRoughnessMaterialStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_UI_Composition.ICompositor,  # compositor
                       _Pointer[ISceneMetallicRoughnessMaterial]],  # result
                      _type.HRESULT]


class ISceneModelTransform(_inspectable.IInspectable):
    get_Orientation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Quaternion]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_struct.Windows.Foundation.Numerics.Quaternion],  # value
                               _type.HRESULT]
    get_RotationAngle: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_RotationAngle: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_RotationAngleInDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                          _type.HRESULT]
    put_RotationAngleInDegrees: _Callable[[_type.FLOAT],  # value
                                          _type.HRESULT]
    get_RotationAxis: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                _type.HRESULT]
    put_RotationAxis: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                                _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                         _type.HRESULT]
    put_Scale: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                         _type.HRESULT]
    get_Translation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                               _type.HRESULT]
    put_Translation: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                               _type.HRESULT]


class ISceneNode(_inspectable.IInspectable):
    get_Children: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISceneNode]]],  # value
                            _type.HRESULT]
    get_Components: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISceneComponent]]],  # value
                              _type.HRESULT]
    get_Parent: _Callable[[_Pointer[ISceneNode]],  # value
                          _type.HRESULT]
    get_Transform: _Callable[[_Pointer[ISceneModelTransform]],  # value
                             _type.HRESULT]
    FindFirstComponentOfType: _Callable[[_enum.Windows.UI.Composition.Scenes.SceneComponentType,  # value
                                         _Pointer[ISceneComponent]],  # result
                                        _type.HRESULT]


class ISceneNodeCollection(_inspectable.IInspectable):
    pass


class ISceneNodeStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_UI_Composition.ICompositor,  # compositor
                       _Pointer[ISceneNode]],  # result
                      _type.HRESULT]


class ISceneObject(_inspectable.IInspectable):
    pass


class ISceneObjectFactory(_inspectable.IInspectable):
    pass


class IScenePbrMaterial(_inspectable.IInspectable):
    get_AlphaCutoff: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_AlphaCutoff: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]
    get_AlphaMode: _Callable[[_Pointer[_enum.Windows.UI.Composition.Scenes.SceneAlphaMode]],  # value
                             _type.HRESULT]
    put_AlphaMode: _Callable[[_enum.Windows.UI.Composition.Scenes.SceneAlphaMode],  # value
                             _type.HRESULT]
    get_EmissiveInput: _Callable[[_Pointer[ISceneMaterialInput]],  # value
                                 _type.HRESULT]
    put_EmissiveInput: _Callable[[ISceneMaterialInput],  # value
                                 _type.HRESULT]
    get_EmissiveFactor: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                  _type.HRESULT]
    put_EmissiveFactor: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                                  _type.HRESULT]
    get_IsDoubleSided: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsDoubleSided: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_NormalInput: _Callable[[_Pointer[ISceneMaterialInput]],  # value
                               _type.HRESULT]
    put_NormalInput: _Callable[[ISceneMaterialInput],  # value
                               _type.HRESULT]
    get_NormalScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_NormalScale: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]
    get_OcclusionInput: _Callable[[_Pointer[ISceneMaterialInput]],  # value
                                  _type.HRESULT]
    put_OcclusionInput: _Callable[[ISceneMaterialInput],  # value
                                  _type.HRESULT]
    get_OcclusionStrength: _Callable[[_Pointer[_type.FLOAT]],  # value
                                     _type.HRESULT]
    put_OcclusionStrength: _Callable[[_type.FLOAT],  # value
                                     _type.HRESULT]


class IScenePbrMaterialFactory(_inspectable.IInspectable):
    pass


class ISceneRendererComponent(_inspectable.IInspectable):
    pass


class ISceneRendererComponentFactory(_inspectable.IInspectable):
    pass


class ISceneSurfaceMaterialInput(_inspectable.IInspectable):
    get_BitmapInterpolationMode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionBitmapInterpolationMode]],  # value
                                           _type.HRESULT]
    put_BitmapInterpolationMode: _Callable[[_enum.Windows.UI.Composition.CompositionBitmapInterpolationMode],  # value
                                           _type.HRESULT]
    get_Surface: _Callable[[_Pointer[_Windows_UI_Composition.ICompositionSurface]],  # value
                           _type.HRESULT]
    put_Surface: _Callable[[_Windows_UI_Composition.ICompositionSurface],  # value
                           _type.HRESULT]
    get_WrappingUMode: _Callable[[_Pointer[_enum.Windows.UI.Composition.Scenes.SceneWrappingMode]],  # value
                                 _type.HRESULT]
    put_WrappingUMode: _Callable[[_enum.Windows.UI.Composition.Scenes.SceneWrappingMode],  # value
                                 _type.HRESULT]
    get_WrappingVMode: _Callable[[_Pointer[_enum.Windows.UI.Composition.Scenes.SceneWrappingMode]],  # value
                                 _type.HRESULT]
    put_WrappingVMode: _Callable[[_enum.Windows.UI.Composition.Scenes.SceneWrappingMode],  # value
                                 _type.HRESULT]


class ISceneSurfaceMaterialInputStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_UI_Composition.ICompositor,  # compositor
                       _Pointer[ISceneSurfaceMaterialInput]],  # result
                      _type.HRESULT]


class ISceneVisual(_inspectable.IInspectable):
    get_Root: _Callable[[_Pointer[ISceneNode]],  # value
                        _type.HRESULT]
    put_Root: _Callable[[ISceneNode],  # value
                        _type.HRESULT]


class ISceneVisualStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_UI_Composition.ICompositor,  # compositor
                       _Pointer[ISceneVisual]],  # result
                      _type.HRESULT]

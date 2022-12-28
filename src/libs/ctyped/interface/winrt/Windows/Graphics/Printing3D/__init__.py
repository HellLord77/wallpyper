from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IPrint3DTaskSourceRequestedHandler:
    Invoke: _Callable[[IPrint3DTaskSourceRequestedArgs],  # args
                      _type.HRESULT]


class IPrint3DTaskSourceRequestedHandler(_IPrint3DTaskSourceRequestedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IPrint3DTaskSourceRequestedHandler_impl(_IPrint3DTaskSourceRequestedHandler, _Unknwnbase.IUnknown_impl):
    pass


class IPrint3DManager(_inspectable.IInspectable):
    add_TaskRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrint3DManager, IPrint3DTaskRequestedEventArgs],  # eventHandler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_TaskRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IPrint3DManagerStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IPrint3DManager]],  # result
                                 _type.HRESULT]
    ShowPrintUIAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                _type.HRESULT]

    _factory = True


class IPrint3DTask(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[IPrinting3D3MFPackage]],  # value
                          _type.HRESULT]
    add_Submitting: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrint3DTask, _inspectable.IInspectable],  # eventHandler
                               _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                              _type.HRESULT]
    remove_Submitting: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                 _type.HRESULT]
    add_Completed: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrint3DTask, IPrint3DTaskCompletedEventArgs],  # eventHandler
                              _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                             _type.HRESULT]
    remove_Completed: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                _type.HRESULT]
    add_SourceChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrint3DTask, IPrint3DTaskSourceChangedEventArgs],  # eventHandler
                                  _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                 _type.HRESULT]
    remove_SourceChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                    _type.HRESULT]


class IPrint3DTaskCompletedEventArgs(_inspectable.IInspectable):
    get_Completion: _Callable[[_Pointer[_enum.Windows.Graphics.Printing3D.Print3DTaskCompletion]],  # value
                              _type.HRESULT]
    get_ExtendedStatus: _Callable[[_Pointer[_enum.Windows.Graphics.Printing3D.Print3DTaskDetail]],  # value
                                  _type.HRESULT]


class IPrint3DTaskRequest(_inspectable.IInspectable):
    CreateTask: _Callable[[_type.HSTRING,  # title
                           _type.HSTRING,  # printerId
                           IPrint3DTaskSourceRequestedHandler,  # handler
                           _Pointer[IPrint3DTask]],  # result
                          _type.HRESULT]


class IPrint3DTaskRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IPrint3DTaskRequest]],  # value
                           _type.HRESULT]


class IPrint3DTaskSourceChangedEventArgs(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[IPrinting3D3MFPackage]],  # value
                          _type.HRESULT]


class IPrint3DTaskSourceRequestedArgs(_inspectable.IInspectable):
    SetSource: _Callable[[IPrinting3D3MFPackage],  # source
                         _type.HRESULT]


class IPrinting3D3MFPackage(_inspectable.IInspectable):
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStream]]],  # operation
                         _type.HRESULT]
    get_PrintTicket: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                               _type.HRESULT]
    put_PrintTicket: _Callable[[_Windows_Storage_Streams.IRandomAccessStream],  # value
                               _type.HRESULT]
    get_ModelPart: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                             _type.HRESULT]
    put_ModelPart: _Callable[[_Windows_Storage_Streams.IRandomAccessStream],  # value
                             _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[IPrinting3DTextureResource]],  # value
                             _type.HRESULT]
    put_Thumbnail: _Callable[[IPrinting3DTextureResource],  # value
                             _type.HRESULT]
    get_Textures: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DTextureResource]]],  # value
                            _type.HRESULT]
    LoadModelFromPackageAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # value
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IPrinting3DModel]]],  # operation
                                         _type.HRESULT]
    SaveModelToPackageAsync: _Callable[[IPrinting3DModel,  # value
                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                       _type.HRESULT]


class IPrinting3D3MFPackage2(_inspectable.IInspectable):
    get_Compression: _Callable[[_Pointer[_enum.Windows.Graphics.Printing3D.Printing3DPackageCompression]],  # value
                               _type.HRESULT]
    put_Compression: _Callable[[_enum.Windows.Graphics.Printing3D.Printing3DPackageCompression],  # value
                               _type.HRESULT]


class IPrinting3D3MFPackageStatics(_inspectable.IInspectable):
    LoadAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # value
                          _Pointer[_Windows_Foundation.IAsyncOperation[IPrinting3D3MFPackage]]],  # operation
                         _type.HRESULT]

    _factory = True


class IPrinting3DBaseMaterial(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Color: _Callable[[_Pointer[IPrinting3DColorMaterial]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[IPrinting3DColorMaterial],  # value
                         _type.HRESULT]


class IPrinting3DBaseMaterialGroup(_inspectable.IInspectable):
    get_Bases: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DBaseMaterial]]],  # value
                         _type.HRESULT]
    get_MaterialGroupId: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]


class IPrinting3DBaseMaterialGroupFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # MaterialGroupId
                       _Pointer[IPrinting3DBaseMaterialGroup]],  # result
                      _type.HRESULT]

    _factory = True


class IPrinting3DBaseMaterialStatics(_inspectable.IInspectable):
    get_Abs: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Pla: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]

    _factory = True


class IPrinting3DColorMaterial(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.UINT32],  # value
                         _type.HRESULT]


class IPrinting3DColorMaterial2(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]


class IPrinting3DColorMaterialGroup(_inspectable.IInspectable):
    get_Colors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DColorMaterial]]],  # value
                          _type.HRESULT]
    get_MaterialGroupId: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]


class IPrinting3DColorMaterialGroupFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # MaterialGroupId
                       _Pointer[IPrinting3DColorMaterialGroup]],  # result
                      _type.HRESULT]

    _factory = True


class IPrinting3DComponent(_inspectable.IInspectable):
    get_Mesh: _Callable[[_Pointer[IPrinting3DMesh]],  # value
                        _type.HRESULT]
    put_Mesh: _Callable[[IPrinting3DMesh],  # value
                        _type.HRESULT]
    get_Components: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DComponentWithMatrix]]],  # value
                              _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[IPrinting3DTextureResource]],  # value
                             _type.HRESULT]
    put_Thumbnail: _Callable[[IPrinting3DTextureResource],  # value
                             _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.Graphics.Printing3D.Printing3DObjectType]],  # value
                        _type.HRESULT]
    put_Type: _Callable[[_enum.Windows.Graphics.Printing3D.Printing3DObjectType],  # value
                        _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_PartNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_PartNumber: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IPrinting3DComponentWithMatrix(_inspectable.IInspectable):
    get_Component: _Callable[[_Pointer[IPrinting3DComponent]],  # value
                             _type.HRESULT]
    put_Component: _Callable[[IPrinting3DComponent],  # value
                             _type.HRESULT]
    get_Matrix: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix4x4]],  # value
                          _type.HRESULT]
    put_Matrix: _Callable[[_struct.Windows.Foundation.Numerics.Matrix4x4],  # value
                          _type.HRESULT]


class IPrinting3DCompositeMaterial(_inspectable.IInspectable):
    get_Values: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.DOUBLE]]],  # value
                          _type.HRESULT]


class IPrinting3DCompositeMaterialGroup(_inspectable.IInspectable):
    get_Composites: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DCompositeMaterial]]],  # value
                              _type.HRESULT]
    get_MaterialGroupId: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    get_MaterialIndices: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.UINT32]]],  # value
                                   _type.HRESULT]


class IPrinting3DCompositeMaterialGroup2(_inspectable.IInspectable):
    get_BaseMaterialGroup: _Callable[[_Pointer[IPrinting3DBaseMaterialGroup]],  # value
                                     _type.HRESULT]
    put_BaseMaterialGroup: _Callable[[IPrinting3DBaseMaterialGroup],  # value
                                     _type.HRESULT]


class IPrinting3DCompositeMaterialGroupFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # MaterialGroupId
                       _Pointer[IPrinting3DCompositeMaterialGroup]],  # result
                      _type.HRESULT]

    _factory = True


class IPrinting3DFaceReductionOptions(_inspectable.IInspectable):
    get_MaxReductionArea: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_MaxReductionArea: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_TargetTriangleCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    put_TargetTriangleCount: _Callable[[_type.UINT32],  # value
                                       _type.HRESULT]
    get_MaxEdgeLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_MaxEdgeLength: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]


class IPrinting3DMaterial(_inspectable.IInspectable):
    get_BaseGroups: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DBaseMaterialGroup]]],  # value
                              _type.HRESULT]
    get_ColorGroups: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DColorMaterialGroup]]],  # value
                               _type.HRESULT]
    get_Texture2CoordGroups: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DTexture2CoordMaterialGroup]]],  # value
                                       _type.HRESULT]
    get_CompositeGroups: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DCompositeMaterialGroup]]],  # value
                                   _type.HRESULT]
    get_MultiplePropertyGroups: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DMultiplePropertyMaterialGroup]]],  # value
                                          _type.HRESULT]


class IPrinting3DMesh(_inspectable.IInspectable):
    get_VertexCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    put_VertexCount: _Callable[[_type.UINT32],  # value
                               _type.HRESULT]
    get_IndexCount: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    put_IndexCount: _Callable[[_type.UINT32],  # value
                              _type.HRESULT]
    get_VertexPositionsDescription: _Callable[[_Pointer[_struct.Windows.Graphics.Printing3D.Printing3DBufferDescription]],  # value
                                              _type.HRESULT]
    put_VertexPositionsDescription: _Callable[[_struct.Windows.Graphics.Printing3D.Printing3DBufferDescription],  # value
                                              _type.HRESULT]
    get_VertexNormalsDescription: _Callable[[_Pointer[_struct.Windows.Graphics.Printing3D.Printing3DBufferDescription]],  # value
                                            _type.HRESULT]
    put_VertexNormalsDescription: _Callable[[_struct.Windows.Graphics.Printing3D.Printing3DBufferDescription],  # value
                                            _type.HRESULT]
    get_TriangleIndicesDescription: _Callable[[_Pointer[_struct.Windows.Graphics.Printing3D.Printing3DBufferDescription]],  # value
                                              _type.HRESULT]
    put_TriangleIndicesDescription: _Callable[[_struct.Windows.Graphics.Printing3D.Printing3DBufferDescription],  # value
                                              _type.HRESULT]
    get_TriangleMaterialIndicesDescription: _Callable[[_Pointer[_struct.Windows.Graphics.Printing3D.Printing3DBufferDescription]],  # value
                                                      _type.HRESULT]
    put_TriangleMaterialIndicesDescription: _Callable[[_struct.Windows.Graphics.Printing3D.Printing3DBufferDescription],  # value
                                                      _type.HRESULT]
    GetVertexPositions: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # buffer
                                  _type.HRESULT]
    CreateVertexPositions: _Callable[[_type.UINT32],  # value
                                     _type.HRESULT]
    GetVertexNormals: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # buffer
                                _type.HRESULT]
    CreateVertexNormals: _Callable[[_type.UINT32],  # value
                                   _type.HRESULT]
    GetTriangleIndices: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # buffer
                                  _type.HRESULT]
    CreateTriangleIndices: _Callable[[_type.UINT32],  # value
                                     _type.HRESULT]
    GetTriangleMaterialIndices: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # buffer
                                          _type.HRESULT]
    CreateTriangleMaterialIndices: _Callable[[_type.UINT32],  # value
                                             _type.HRESULT]
    get_BufferDescriptionSet: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                        _type.HRESULT]
    get_BufferSet: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                             _type.HRESULT]
    VerifyAsync: _Callable[[_enum.Windows.Graphics.Printing3D.Printing3DMeshVerificationMode,  # value
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPrinting3DMeshVerificationResult]]],  # operation
                           _type.HRESULT]


class IPrinting3DMeshVerificationResult(_inspectable.IInspectable):
    get_IsValid: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_NonmanifoldTriangles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                                        _type.HRESULT]
    get_ReversedNormalTriangles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                                           _type.HRESULT]


class IPrinting3DModel(_inspectable.IInspectable):
    get_Unit: _Callable[[_Pointer[_enum.Windows.Graphics.Printing3D.Printing3DModelUnit]],  # value
                        _type.HRESULT]
    put_Unit: _Callable[[_enum.Windows.Graphics.Printing3D.Printing3DModelUnit],  # value
                        _type.HRESULT]
    get_Textures: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DModelTexture]]],  # value
                            _type.HRESULT]
    get_Meshes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DMesh]]],  # value
                          _type.HRESULT]
    get_Components: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DComponent]]],  # value
                              _type.HRESULT]
    get_Material: _Callable[[_Pointer[IPrinting3DMaterial]],  # value
                            _type.HRESULT]
    put_Material: _Callable[[IPrinting3DMaterial],  # value
                            _type.HRESULT]
    get_Build: _Callable[[_Pointer[IPrinting3DComponent]],  # value
                         _type.HRESULT]
    put_Build: _Callable[[IPrinting3DComponent],  # value
                         _type.HRESULT]
    get_Version: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Version: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_RequiredExtensions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                      _type.HRESULT]
    get_Metadata: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                            _type.HRESULT]
    RepairAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    Clone: _Callable[[_Pointer[IPrinting3DModel]],  # value
                     _type.HRESULT]


class IPrinting3DModel2(_inspectable.IInspectable):
    TryPartialRepairAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]
    TryPartialRepairWithTimeAsync: _Callable[[_struct.Windows.Foundation.TimeSpan,  # maxWaitTime
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                             _type.HRESULT]
    TryReduceFacesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.boolean, _type.DOUBLE]]],  # operation
                                   _type.HRESULT]
    TryReduceFacesWithOptionsAsync: _Callable[[IPrinting3DFaceReductionOptions,  # printing3DFaceReductionOptions
                                               _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.boolean, _type.DOUBLE]]],  # operation
                                              _type.HRESULT]
    TryReduceFacesWithOptionsAndTimeAsync: _Callable[[IPrinting3DFaceReductionOptions,  # printing3DFaceReductionOptions
                                                      _struct.Windows.Foundation.TimeSpan,  # maxWait
                                                      _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.boolean, _type.DOUBLE]]],  # operation
                                                     _type.HRESULT]
    RepairWithProgressAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.boolean, _type.DOUBLE]]],  # operation
                                       _type.HRESULT]


class IPrinting3DModelTexture(_inspectable.IInspectable):
    get_TextureResource: _Callable[[_Pointer[IPrinting3DTextureResource]],  # value
                                   _type.HRESULT]
    put_TextureResource: _Callable[[IPrinting3DTextureResource],  # value
                                   _type.HRESULT]
    get_TileStyleU: _Callable[[_Pointer[_enum.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior]],  # value
                              _type.HRESULT]
    put_TileStyleU: _Callable[[_enum.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior],  # value
                              _type.HRESULT]
    get_TileStyleV: _Callable[[_Pointer[_enum.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior]],  # value
                              _type.HRESULT]
    put_TileStyleV: _Callable[[_enum.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior],  # value
                              _type.HRESULT]


class IPrinting3DMultiplePropertyMaterial(_inspectable.IInspectable):
    get_MaterialIndices: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.UINT32]]],  # value
                                   _type.HRESULT]


class IPrinting3DMultiplePropertyMaterialGroup(_inspectable.IInspectable):
    get_MultipleProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DMultiplePropertyMaterial]]],  # value
                                      _type.HRESULT]
    get_MaterialGroupIndices: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.UINT32]]],  # value
                                        _type.HRESULT]
    get_MaterialGroupId: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]


class IPrinting3DMultiplePropertyMaterialGroupFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # MaterialGroupId
                       _Pointer[IPrinting3DMultiplePropertyMaterialGroup]],  # result
                      _type.HRESULT]

    _factory = True


class IPrinting3DTexture2CoordMaterial(_inspectable.IInspectable):
    get_Texture: _Callable[[_Pointer[IPrinting3DModelTexture]],  # value
                           _type.HRESULT]
    put_Texture: _Callable[[IPrinting3DModelTexture],  # value
                           _type.HRESULT]
    get_U: _Callable[[_Pointer[_type.DOUBLE]],  # value
                     _type.HRESULT]
    put_U: _Callable[[_type.DOUBLE],  # value
                     _type.HRESULT]
    get_V: _Callable[[_Pointer[_type.DOUBLE]],  # value
                     _type.HRESULT]
    put_V: _Callable[[_type.DOUBLE],  # value
                     _type.HRESULT]


class IPrinting3DTexture2CoordMaterialGroup(_inspectable.IInspectable):
    get_Texture2Coords: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrinting3DTexture2CoordMaterial]]],  # value
                                  _type.HRESULT]
    get_MaterialGroupId: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]


class IPrinting3DTexture2CoordMaterialGroup2(_inspectable.IInspectable):
    get_Texture: _Callable[[_Pointer[IPrinting3DModelTexture]],  # value
                           _type.HRESULT]
    put_Texture: _Callable[[IPrinting3DModelTexture],  # value
                           _type.HRESULT]


class IPrinting3DTexture2CoordMaterialGroupFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # MaterialGroupId
                       _Pointer[IPrinting3DTexture2CoordMaterialGroup]],  # result
                      _type.HRESULT]

    _factory = True


class IPrinting3DTextureResource(_inspectable.IInspectable):
    get_TextureData: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]],  # value
                               _type.HRESULT]
    put_TextureData: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamWithContentType],  # value
                               _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]

from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import objidl as _objidl
from . import objidlbase as _objidlbase
from . import ocidl as _ocidl
from . import wincodec as _wincodec
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IWICMetadataBlockReader(_Unknwnbase.IUnknown):
    GetContainerFormat: _Callable[[_Pointer[_struct.GUID]],  # pguidContainerFormat
                                  _type.HRESULT]
    GetCount: _Callable[[_Pointer[_type.UINT]],  # pcCount
                        _type.HRESULT]
    GetReaderByIndex: _Callable[[_type.UINT,  # nIndex
                                 _Pointer[IWICMetadataReader]],  # ppIMetadataReader
                                _type.HRESULT]
    GetEnumerator: _Callable[[_Pointer[_objidlbase.IEnumUnknown]],  # ppIEnumMetadata
                             _type.HRESULT]


class IWICMetadataBlockWriter(IWICMetadataBlockReader):
    InitializeFromBlockReader: _Callable[[IWICMetadataBlockReader],  # pIMDBlockReader
                                         _type.HRESULT]
    GetWriterByIndex: _Callable[[_type.UINT,  # nIndex
                                 _Pointer[IWICMetadataWriter]],  # ppIMetadataWriter
                                _type.HRESULT]
    AddWriter: _Callable[[IWICMetadataWriter],  # pIMetadataWriter
                         _type.HRESULT]
    SetWriterByIndex: _Callable[[_type.UINT,  # nIndex
                                 IWICMetadataWriter],  # pIMetadataWriter
                                _type.HRESULT]
    RemoveWriterByIndex: _Callable[[_type.UINT],  # nIndex
                                   _type.HRESULT]


class IWICMetadataReader(_Unknwnbase.IUnknown):
    GetMetadataFormat: _Callable[[_Pointer[_struct.GUID]],  # pguidMetadataFormat
                                 _type.HRESULT]
    GetMetadataHandlerInfo: _Callable[[_Pointer[IWICMetadataHandlerInfo]],  # ppIHandler
                                      _type.HRESULT]
    GetCount: _Callable[[_Pointer[_type.UINT]],  # pcCount
                        _type.HRESULT]
    GetValueByIndex: _Callable[[_type.UINT,  # nIndex
                                _Pointer[_struct.PROPVARIANT],  # pvarSchema
                                _Pointer[_struct.PROPVARIANT],  # pvarId
                                _Pointer[_struct.PROPVARIANT]],  # pvarValue
                               _type.HRESULT]
    GetValue: _Callable[[_Pointer[_struct.PROPVARIANT],  # pvarSchema
                         _Pointer[_struct.PROPVARIANT],  # pvarId
                         _Pointer[_struct.PROPVARIANT]],  # pvarValue
                        _type.HRESULT]
    GetEnumerator: _Callable[[_Pointer[_wincodec.IWICEnumMetadataItem]],  # ppIEnumMetadata
                             _type.HRESULT]


class IWICMetadataWriter(IWICMetadataReader):
    SetValue: _Callable[[_Pointer[_struct.PROPVARIANT],  # pvarSchema
                         _Pointer[_struct.PROPVARIANT],  # pvarId
                         _Pointer[_struct.PROPVARIANT]],  # pvarValue
                        _type.HRESULT]
    SetValueByIndex: _Callable[[_type.UINT,  # nIndex
                                _Pointer[_struct.PROPVARIANT],  # pvarSchema
                                _Pointer[_struct.PROPVARIANT],  # pvarId
                                _Pointer[_struct.PROPVARIANT]],  # pvarValue
                               _type.HRESULT]
    RemoveValue: _Callable[[_Pointer[_struct.PROPVARIANT],  # pvarSchema
                            _Pointer[_struct.PROPVARIANT]],  # pvarId
                           _type.HRESULT]
    RemoveValueByIndex: _Callable[[_type.UINT],  # nIndex
                                  _type.HRESULT]


class IWICStreamProvider(_Unknwnbase.IUnknown):
    GetStream: _Callable[[_Pointer[_objidlbase.IStream]],  # ppIStream
                         _type.HRESULT]
    GetPersistOptions: _Callable[[_Pointer[_type.DWORD]],  # pdwPersistOptions
                                 _type.HRESULT]
    GetPreferredVendorGUID: _Callable[[_Pointer[_struct.GUID]],  # pguidPreferredVendor
                                      _type.HRESULT]
    RefreshStream: _Callable[[],
                             _type.HRESULT]


class IWICPersistStream(_objidl.IPersistStream):
    LoadEx: _Callable[[_objidlbase.IStream,  # pIStream
                       _Pointer[_struct.GUID],  # pguidPreferredVendor
                       _type.DWORD],  # dwPersistOptions
                      _type.HRESULT]
    SaveEx: _Callable[[_objidlbase.IStream,  # pIStream
                       _type.DWORD,  # dwPersistOptions
                       _type.BOOL],  # fClearDirty
                      _type.HRESULT]


class IWICMetadataHandlerInfo(_wincodec.IWICComponentInfo):
    GetMetadataFormat: _Callable[[_Pointer[_struct.GUID]],  # pguidMetadataFormat
                                 _type.HRESULT]
    GetContainerFormats: _Callable[[_type.UINT,  # cContainerFormats
                                    _Pointer[_struct.GUID],  # pguidContainerFormats
                                    _Pointer[_type.UINT]],  # pcchActual
                                   _type.HRESULT]
    GetDeviceManufacturer: _Callable[[_type.UINT,  # cchDeviceManufacturer
                                      _Pointer[_type.WCHAR],  # wzDeviceManufacturer
                                      _Pointer[_type.UINT]],  # pcchActual
                                     _type.HRESULT]
    GetDeviceModels: _Callable[[_type.UINT,  # cchDeviceModels
                                _Pointer[_type.WCHAR],  # wzDeviceModels
                                _Pointer[_type.UINT]],  # pcchActual
                               _type.HRESULT]
    DoesRequireFullStream: _Callable[[_Pointer[_type.BOOL]],  # pfRequiresFullStream
                                     _type.HRESULT]
    DoesSupportPadding: _Callable[[_Pointer[_type.BOOL]],  # pfSupportsPadding
                                  _type.HRESULT]
    DoesRequireFixedSize: _Callable[[_Pointer[_type.BOOL]],  # pfFixedSize
                                    _type.HRESULT]


class IWICMetadataReaderInfo(IWICMetadataHandlerInfo):
    GetPatterns: _Callable[[_Pointer[_struct.GUID],  # guidContainerFormat
                            _type.UINT,  # cbSize
                            _Pointer[_struct.WICMetadataPattern],  # pPattern
                            _Pointer[_type.UINT],  # pcCount
                            _Pointer[_type.UINT]],  # pcbActual
                           _type.HRESULT]
    MatchesPattern: _Callable[[_Pointer[_struct.GUID],  # guidContainerFormat
                               _objidlbase.IStream,  # pIStream
                               _Pointer[_type.BOOL]],  # pfMatches
                              _type.HRESULT]
    CreateInstance: _Callable[[_Pointer[IWICMetadataReader]],  # ppIReader
                              _type.HRESULT]


class IWICMetadataWriterInfo(IWICMetadataHandlerInfo):
    GetHeader: _Callable[[_Pointer[_struct.GUID],  # guidContainerFormat
                          _type.UINT,  # cbSize
                          _Pointer[_struct.WICMetadataHeader],  # pHeader
                          _Pointer[_type.UINT]],  # pcbActual
                         _type.HRESULT]
    CreateInstance: _Callable[[_Pointer[IWICMetadataWriter]],  # ppIWriter
                              _type.HRESULT]


class IWICComponentFactory(_wincodec.IWICImagingFactory):
    CreateMetadataReader: _Callable[[_Pointer[_struct.GUID],  # guidMetadataFormat
                                     _Pointer[_struct.GUID],  # pguidVendor
                                     _type.DWORD,  # dwOptions
                                     _objidlbase.IStream,  # pIStream
                                     _Pointer[IWICMetadataReader]],  # ppIReader
                                    _type.HRESULT]
    CreateMetadataReaderFromContainer: _Callable[[_Pointer[_struct.GUID],  # guidContainerFormat
                                                  _Pointer[_struct.GUID],  # pguidVendor
                                                  _type.DWORD,  # dwOptions
                                                  _objidlbase.IStream,  # pIStream
                                                  _Pointer[IWICMetadataReader]],  # ppIReader
                                                 _type.HRESULT]
    CreateMetadataWriter: _Callable[[_Pointer[_struct.GUID],  # guidMetadataFormat
                                     _Pointer[_struct.GUID],  # pguidVendor
                                     _type.DWORD,  # dwMetadataOptions
                                     _Pointer[IWICMetadataWriter]],  # ppIWriter
                                    _type.HRESULT]
    CreateMetadataWriterFromReader: _Callable[[IWICMetadataReader,  # pIReader
                                               _Pointer[_struct.GUID],  # pguidVendor
                                               _Pointer[IWICMetadataWriter]],  # ppIWriter
                                              _type.HRESULT]
    CreateQueryReaderFromBlockReader: _Callable[[IWICMetadataBlockReader,  # pIBlockReader
                                                 _Pointer[_wincodec.IWICMetadataQueryReader]],  # ppIQueryReader
                                                _type.HRESULT]
    CreateQueryWriterFromBlockWriter: _Callable[[IWICMetadataBlockWriter,  # pIBlockWriter
                                                 _Pointer[_wincodec.IWICMetadataQueryWriter]],  # ppIQueryWriter
                                                _type.HRESULT]
    CreateEncoderPropertyBag: _Callable[[_Pointer[_struct.PROPBAG2],  # ppropOptions
                                         _type.UINT,  # cCount
                                         _Pointer[_ocidl.IPropertyBag2]],  # ppIPropertyBag
                                        _type.HRESULT]

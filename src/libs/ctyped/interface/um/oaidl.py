from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import objidlbase as _objidlbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ... import union as _union
from ..._utils import _Pointer


class ICreateTypeInfo(_Unknwnbase.IUnknown):
    SetGuid: _Callable[[_Pointer[_struct.GUID]],  # guid
                       _type.HRESULT]
    SetTypeFlags: _Callable[[_type.UINT],  # uTypeFlags
                            _type.HRESULT]
    SetDocString: _Callable[[_type.LPOLESTR],  # pStrDoc
                            _type.HRESULT]
    SetHelpContext: _Callable[[_type.DWORD],  # dwHelpContext
                              _type.HRESULT]
    SetVersion: _Callable[[_type.WORD,  # wMajorVerNum
                           _type.WORD],  # wMinorVerNum
                          _type.HRESULT]
    AddRefTypeInfo: _Callable[[ITypeInfo,  # pTInfo
                               _Pointer[_type.HREFTYPE]],  # phRefType
                              _type.HRESULT]
    AddFuncDesc: _Callable[[_type.UINT,  # index
                            _Pointer[_struct.FUNCDESC]],  # pFuncDesc
                           _type.HRESULT]
    AddImplType: _Callable[[_type.UINT,  # index
                            _type.HREFTYPE],  # hRefType
                           _type.HRESULT]
    SetImplTypeFlags: _Callable[[_type.UINT,  # index
                                 _type.INT],  # implTypeFlags
                                _type.HRESULT]
    SetAlignment: _Callable[[_type.WORD],  # cbAlignment
                            _type.HRESULT]
    SetSchema: _Callable[[_type.LPOLESTR],  # pStrSchema
                         _type.HRESULT]
    AddVarDesc: _Callable[[_type.UINT,  # index
                           _Pointer[_struct.VARDESC]],  # pVarDesc
                          _type.HRESULT]
    SetFuncAndParamNames: _Callable[[_type.UINT,  # index
                                     _Pointer[_type.LPOLESTR],  # rgszNames
                                     _type.UINT],  # cNames
                                    _type.HRESULT]
    SetVarName: _Callable[[_type.UINT,  # index
                           _type.LPOLESTR],  # szName
                          _type.HRESULT]
    SetTypeDescAlias: _Callable[[_Pointer[_struct.TYPEDESC]],  # pTDescAlias
                                _type.HRESULT]
    DefineFuncAsDllEntry: _Callable[[_type.UINT,  # index
                                     _type.LPOLESTR,  # szDllName
                                     _type.LPOLESTR],  # szProcName
                                    _type.HRESULT]
    SetFuncDocString: _Callable[[_type.UINT,  # index
                                 _type.LPOLESTR],  # szDocString
                                _type.HRESULT]
    SetVarDocString: _Callable[[_type.UINT,  # index
                                _type.LPOLESTR],  # szDocString
                               _type.HRESULT]
    SetFuncHelpContext: _Callable[[_type.UINT,  # index
                                   _type.DWORD],  # dwHelpContext
                                  _type.HRESULT]
    SetVarHelpContext: _Callable[[_type.UINT,  # index
                                  _type.DWORD],  # dwHelpContext
                                 _type.HRESULT]
    SetMops: _Callable[[_type.UINT,  # index
                        _type.BSTR],  # bstrMops
                       _type.HRESULT]
    SetTypeIdldesc: _Callable[[_Pointer[_struct.IDLDESC]],  # pIdlDesc
                              _type.HRESULT]
    LayOut: _Callable[[],
                      _type.HRESULT]


class ICreateTypeInfo2(ICreateTypeInfo):
    DeleteFuncDesc: _Callable[[_type.UINT],  # index
                              _type.HRESULT]
    DeleteFuncDescByMemId: _Callable[[_type.MEMBERID,  # memid
                                      _enum.INVOKEKIND],  # invKind
                                     _type.HRESULT]
    DeleteVarDesc: _Callable[[_type.UINT],  # index
                             _type.HRESULT]
    DeleteVarDescByMemId: _Callable[[_type.MEMBERID],  # memid
                                    _type.HRESULT]
    DeleteImplType: _Callable[[_type.UINT],  # index
                              _type.HRESULT]
    SetCustData: _Callable[[_Pointer[_struct.GUID],  # guid
                            _Pointer[_struct.VARIANT]],  # pVarVal
                           _type.HRESULT]
    SetFuncCustData: _Callable[[_type.UINT,  # index
                                _Pointer[_struct.GUID],  # guid
                                _Pointer[_struct.VARIANT]],  # pVarVal
                               _type.HRESULT]
    SetParamCustData: _Callable[[_type.UINT,  # indexFunc
                                 _type.UINT,  # indexParam
                                 _Pointer[_struct.GUID],  # guid
                                 _Pointer[_struct.VARIANT]],  # pVarVal
                                _type.HRESULT]
    SetVarCustData: _Callable[[_type.UINT,  # index
                               _Pointer[_struct.GUID],  # guid
                               _Pointer[_struct.VARIANT]],  # pVarVal
                              _type.HRESULT]
    SetImplTypeCustData: _Callable[[_type.UINT,  # index
                                    _Pointer[_struct.GUID],  # guid
                                    _Pointer[_struct.VARIANT]],  # pVarVal
                                   _type.HRESULT]
    SetHelpStringContext: _Callable[[_type.ULONG],  # dwHelpStringContext
                                    _type.HRESULT]
    SetFuncHelpStringContext: _Callable[[_type.UINT,  # index
                                         _type.ULONG],  # dwHelpStringContext
                                        _type.HRESULT]
    SetVarHelpStringContext: _Callable[[_type.UINT,  # index
                                        _type.ULONG],  # dwHelpStringContext
                                       _type.HRESULT]
    Invalidate: _Callable[[],
                          _type.HRESULT]
    SetName: _Callable[[_type.LPOLESTR],  # szName
                       _type.HRESULT]


class ICreateTypeLib(_Unknwnbase.IUnknown):
    CreateTypeInfo: _Callable[[_type.LPOLESTR,  # szName
                               _enum.TYPEKIND,  # tkind
                               _Pointer[ICreateTypeInfo]],  # ppCTInfo
                              _type.HRESULT]
    SetName: _Callable[[_type.LPOLESTR],  # szName
                       _type.HRESULT]
    SetVersion: _Callable[[_type.WORD,  # wMajorVerNum
                           _type.WORD],  # wMinorVerNum
                          _type.HRESULT]
    SetGuid: _Callable[[_Pointer[_struct.GUID]],  # guid
                       _type.HRESULT]
    SetDocString: _Callable[[_type.LPOLESTR],  # szDoc
                            _type.HRESULT]
    SetHelpFileName: _Callable[[_type.LPOLESTR],  # szHelpFileName
                               _type.HRESULT]
    SetHelpContext: _Callable[[_type.DWORD],  # dwHelpContext
                              _type.HRESULT]
    SetLcid: _Callable[[_type.LCID],  # lcid
                       _type.HRESULT]
    SetLibFlags: _Callable[[_type.UINT],  # uLibFlags
                           _type.HRESULT]
    SaveAllChanges: _Callable[[],
                              _type.HRESULT]


class ICreateTypeLib2(ICreateTypeLib):
    DeleteTypeInfo: _Callable[[_type.LPOLESTR],  # szName
                              _type.HRESULT]
    SetCustData: _Callable[[_Pointer[_struct.GUID],  # guid
                            _Pointer[_struct.VARIANT]],  # pVarVal
                           _type.HRESULT]
    SetHelpStringContext: _Callable[[_type.ULONG],  # dwHelpStringContext
                                    _type.HRESULT]
    SetHelpStringDll: _Callable[[_type.LPOLESTR],  # szFileName
                                _type.HRESULT]


class IDispatch(_Unknwnbase.IUnknown):
    GetTypeInfoCount: _Callable[[_Pointer[_type.UINT]],  # pctinfo
                                _type.HRESULT]
    GetTypeInfo: _Callable[[_type.UINT,  # iTInfo
                            _type.LCID,  # lcid
                            _Pointer[ITypeInfo]],  # ppTInfo
                           _type.HRESULT]
    GetIDsOfNames: _Callable[[_Pointer[_struct.IID],  # riid
                              _Pointer[_type.LPOLESTR],  # rgszNames
                              _type.UINT,  # cNames
                              _type.LCID,  # lcid
                              _Pointer[_type.DISPID]],  # rgDispId
                             _type.HRESULT]
    Invoke: _Callable[[_type.DISPID,  # dispIdMember
                       _Pointer[_struct.IID],  # riid
                       _type.LCID,  # lcid
                       _type.WORD,  # wFlags
                       _Pointer[_struct.DISPPARAMS],  # pDispParams
                       _Pointer[_struct.VARIANT],  # pVarResult
                       _Pointer[_struct.EXCEPINFO],  # pExcepInfo
                       _Pointer[_type.UINT]],  # puArgErr
                      _type.HRESULT]


class IEnumVARIANT(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_struct.VARIANT],  # rgVar
                     _Pointer[_type.ULONG]],  # pCeltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumVARIANT]],  # ppEnum
                     _type.HRESULT]


class ITypeComp(_Unknwnbase.IUnknown):
    Bind: _Callable[[_type.LPOLESTR,  # szName
                     _type.ULONG,  # lHashVal
                     _type.WORD,  # wFlags
                     _Pointer[ITypeInfo],  # ppTInfo
                     _Pointer[_enum.DESCKIND],  # pDescKind
                     _Pointer[_union.BINDPTR]],  # pBindPtr
                    _type.HRESULT]
    BindType: _Callable[[_type.LPOLESTR,  # szName
                         _type.ULONG,  # lHashVal
                         _Pointer[ITypeInfo],  # ppTInfo
                         _Pointer[ITypeComp]],  # ppTComp
                        _type.HRESULT]


class ITypeInfo(_Unknwnbase.IUnknown):
    GetTypeAttr: _Callable[[_Pointer[_Pointer[_struct.TYPEATTR]]],  # ppTypeAttr
                           _type.HRESULT]
    GetTypeComp: _Callable[[_Pointer[ITypeComp]],  # ppTComp
                           _type.HRESULT]
    GetFuncDesc: _Callable[[_type.UINT,  # index
                            _Pointer[_Pointer[_struct.FUNCDESC]]],  # ppFuncDesc
                           _type.HRESULT]
    GetVarDesc: _Callable[[_type.UINT,  # index
                           _Pointer[_Pointer[_struct.VARDESC]]],  # ppVarDesc
                          _type.HRESULT]
    GetNames: _Callable[[_type.MEMBERID,  # memid
                         _Pointer[_type.BSTR],  # rgBstrNames
                         _type.UINT,  # cMaxNames
                         _Pointer[_type.UINT]],  # pcNames
                        _type.HRESULT]
    GetRefTypeOfImplType: _Callable[[_type.UINT,  # index
                                     _Pointer[_type.HREFTYPE]],  # pRefType
                                    _type.HRESULT]
    GetImplTypeFlags: _Callable[[_type.UINT,  # index
                                 _Pointer[_type.INT]],  # pImplTypeFlags
                                _type.HRESULT]
    GetIDsOfNames: _Callable[[_Pointer[_type.LPOLESTR],  # rgszNames
                              _type.UINT,  # cNames
                              _Pointer[_type.MEMBERID]],  # pMemId
                             _type.HRESULT]
    Invoke: _Callable[[_type.PVOID,  # pvInstance
                       _type.MEMBERID,  # memid
                       _type.WORD,  # wFlags
                       _Pointer[_struct.DISPPARAMS],  # pDispParams
                       _Pointer[_struct.VARIANT],  # pVarResult
                       _Pointer[_struct.EXCEPINFO],  # pExcepInfo
                       _Pointer[_type.UINT]],  # puArgErr
                      _type.HRESULT]
    GetDocumentation: _Callable[[_type.MEMBERID,  # memid
                                 _Pointer[_type.BSTR],  # pBstrName
                                 _Pointer[_type.BSTR],  # pBstrDocString
                                 _Pointer[_type.DWORD],  # pdwHelpContext
                                 _Pointer[_type.BSTR]],  # pBstrHelpFile
                                _type.HRESULT]
    GetDllEntry: _Callable[[_type.MEMBERID,  # memid
                            _enum.INVOKEKIND,  # invKind
                            _Pointer[_type.BSTR],  # pBstrDllName
                            _Pointer[_type.BSTR],  # pBstrName
                            _Pointer[_type.WORD]],  # pwOrdinal
                           _type.HRESULT]
    GetRefTypeInfo: _Callable[[_type.HREFTYPE,  # hRefType
                               _Pointer[ITypeInfo]],  # ppTInfo
                              _type.HRESULT]
    AddressOfMember: _Callable[[_type.MEMBERID,  # memid
                                _enum.INVOKEKIND,  # invKind
                                _Pointer[_type.PVOID]],  # ppv
                               _type.HRESULT]
    CreateInstance: _Callable[[_Unknwnbase.IUnknown,  # pUnkOuter
                               _Pointer[_struct.IID],  # riid
                               _Pointer[_type.PVOID]],  # ppvObj
                              _type.HRESULT]
    GetMops: _Callable[[_type.MEMBERID,  # memid
                        _Pointer[_type.BSTR]],  # pBstrMops
                       _type.HRESULT]
    GetContainingTypeLib: _Callable[[_Pointer[ITypeLib],  # ppTLib
                                     _Pointer[_type.UINT]],  # pIndex
                                    _type.HRESULT]
    ReleaseTypeAttr: _Callable[[_Pointer[_struct.TYPEATTR]],  # pTypeAttr
                               _type.c_void]
    ReleaseFuncDesc: _Callable[[_Pointer[_struct.FUNCDESC]],  # pFuncDesc
                               _type.c_void]
    ReleaseVarDesc: _Callable[[_Pointer[_struct.VARDESC]],  # pVarDesc
                              _type.c_void]


class ITypeInfo2(ITypeInfo):
    GetTypeKind: _Callable[[_Pointer[_enum.TYPEKIND]],  # pTypeKind
                           _type.HRESULT]
    GetTypeFlags: _Callable[[_Pointer[_type.ULONG]],  # pTypeFlags
                            _type.HRESULT]
    GetFuncIndexOfMemId: _Callable[[_type.MEMBERID,  # memid
                                    _enum.INVOKEKIND,  # invKind
                                    _Pointer[_type.UINT]],  # pFuncIndex
                                   _type.HRESULT]
    GetVarIndexOfMemId: _Callable[[_type.MEMBERID,  # memid
                                   _Pointer[_type.UINT]],  # pVarIndex
                                  _type.HRESULT]
    GetCustData: _Callable[[_Pointer[_struct.GUID],  # guid
                            _Pointer[_struct.VARIANT]],  # pVarVal
                           _type.HRESULT]
    GetFuncCustData: _Callable[[_type.UINT,  # index
                                _Pointer[_struct.GUID],  # guid
                                _Pointer[_struct.VARIANT]],  # pVarVal
                               _type.HRESULT]
    GetParamCustData: _Callable[[_type.UINT,  # indexFunc
                                 _type.UINT,  # indexParam
                                 _Pointer[_struct.GUID],  # guid
                                 _Pointer[_struct.VARIANT]],  # pVarVal
                                _type.HRESULT]
    GetVarCustData: _Callable[[_type.UINT,  # index
                               _Pointer[_struct.GUID],  # guid
                               _Pointer[_struct.VARIANT]],  # pVarVal
                              _type.HRESULT]
    GetImplTypeCustData: _Callable[[_type.UINT,  # index
                                    _Pointer[_struct.GUID],  # guid
                                    _Pointer[_struct.VARIANT]],  # pVarVal
                                   _type.HRESULT]
    GetDocumentation2: _Callable[[_type.MEMBERID,  # memid
                                  _type.LCID,  # lcid
                                  _Pointer[_type.BSTR],  # pbstrHelpString
                                  _Pointer[_type.DWORD],  # pdwHelpStringContext
                                  _Pointer[_type.BSTR]],  # pbstrHelpStringDll
                                 _type.HRESULT]
    GetAllCustData: _Callable[[_Pointer[_struct.CUSTDATA]],  # pCustData
                              _type.HRESULT]
    GetAllFuncCustData: _Callable[[_type.UINT,  # index
                                   _Pointer[_struct.CUSTDATA]],  # pCustData
                                  _type.HRESULT]
    GetAllParamCustData: _Callable[[_type.UINT,  # indexFunc
                                    _type.UINT,  # indexParam
                                    _Pointer[_struct.CUSTDATA]],  # pCustData
                                   _type.HRESULT]
    GetAllVarCustData: _Callable[[_type.UINT,  # index
                                  _Pointer[_struct.CUSTDATA]],  # pCustData
                                 _type.HRESULT]
    GetAllImplTypeCustData: _Callable[[_type.UINT,  # index
                                       _Pointer[_struct.CUSTDATA]],  # pCustData
                                      _type.HRESULT]


class ITypeLib(_Unknwnbase.IUnknown):
    GetTypeInfoCount: _Callable[[],
                                _type.UINT]
    GetTypeInfo: _Callable[[_type.UINT,  # index
                            _Pointer[ITypeInfo]],  # ppTInfo
                           _type.HRESULT]
    GetTypeInfoType: _Callable[[_type.UINT,  # index
                                _Pointer[_enum.TYPEKIND]],  # pTKind
                               _type.HRESULT]
    GetTypeInfoOfGuid: _Callable[[_Pointer[_struct.GUID],  # guid
                                  _Pointer[ITypeInfo]],  # ppTinfo
                                 _type.HRESULT]
    GetLibAttr: _Callable[[_Pointer[_Pointer[_struct.TLIBATTR]]],  # ppTLibAttr
                          _type.HRESULT]
    GetTypeComp: _Callable[[_Pointer[ITypeComp]],  # ppTComp
                           _type.HRESULT]
    GetDocumentation: _Callable[[_type.INT,  # index
                                 _Pointer[_type.BSTR],  # pBstrName
                                 _Pointer[_type.BSTR],  # pBstrDocString
                                 _Pointer[_type.DWORD],  # pdwHelpContext
                                 _Pointer[_type.BSTR]],  # pBstrHelpFile
                                _type.HRESULT]
    IsName: _Callable[[_type.LPOLESTR,  # szNameBuf
                       _type.ULONG,  # lHashVal
                       _Pointer[_type.BOOL]],  # pfName
                      _type.HRESULT]
    FindName: _Callable[[_type.LPOLESTR,  # szNameBuf
                         _type.ULONG,  # lHashVal
                         _Pointer[ITypeInfo],  # ppTInfo
                         _Pointer[_type.MEMBERID],  # rgMemId
                         _Pointer[_type.USHORT]],  # pcFound
                        _type.HRESULT]
    ReleaseTLibAttr: _Callable[[_Pointer[_struct.TLIBATTR]],  # pTLibAttr
                               _type.c_void]


class ITypeLib2(ITypeLib):
    GetCustData: _Callable[[_Pointer[_struct.GUID],  # guid
                            _Pointer[_struct.VARIANT]],  # pVarVal
                           _type.HRESULT]
    GetLibStatistics: _Callable[[_Pointer[_type.ULONG],  # pcUniqueNames
                                 _Pointer[_type.ULONG]],  # pcchUniqueNames
                                _type.HRESULT]
    GetDocumentation2: _Callable[[_type.INT,  # index
                                  _type.LCID,  # lcid
                                  _Pointer[_type.BSTR],  # pbstrHelpString
                                  _Pointer[_type.DWORD],  # pdwHelpStringContext
                                  _Pointer[_type.BSTR]],  # pbstrHelpStringDll
                                 _type.HRESULT]
    GetAllCustData: _Callable[[_Pointer[_struct.CUSTDATA]],  # pCustData
                              _type.HRESULT]


class ITypeChangeEvents(_Unknwnbase.IUnknown):
    RequestTypeChange: _Callable[[_enum.CHANGEKIND,  # changeKind
                                  ITypeInfo,  # pTInfoBefore
                                  _type.LPOLESTR,  # pStrName
                                  _Pointer[_type.INT]],  # pfCancel
                                 _type.HRESULT]
    AfterTypeChange: _Callable[[_enum.CHANGEKIND,  # changeKind
                                ITypeInfo,  # pTInfoAfter
                                _type.LPOLESTR],  # pStrName
                               _type.HRESULT]


class IErrorInfo(_Unknwnbase.IUnknown):
    GetGUID: _Callable[[_Pointer[_struct.GUID]],  # pGUID
                       _type.HRESULT]
    GetSource: _Callable[[_Pointer[_type.BSTR]],  # pBstrSource
                         _type.HRESULT]
    GetDescription: _Callable[[_Pointer[_type.BSTR]],  # pBstrDescription
                              _type.HRESULT]
    GetHelpFile: _Callable[[_Pointer[_type.BSTR]],  # pBstrHelpFile
                           _type.HRESULT]
    GetHelpContext: _Callable[[_Pointer[_type.DWORD]],  # pdwHelpContext
                              _type.HRESULT]


class ICreateErrorInfo(_Unknwnbase.IUnknown):
    SetGUID: _Callable[[_Pointer[_struct.GUID]],  # rguid
                       _type.HRESULT]
    SetSource: _Callable[[_type.LPOLESTR],  # szSource
                         _type.HRESULT]
    SetDescription: _Callable[[_type.LPOLESTR],  # szDescription
                              _type.HRESULT]
    SetHelpFile: _Callable[[_type.LPOLESTR],  # szHelpFile
                           _type.HRESULT]
    SetHelpContext: _Callable[[_type.DWORD],  # dwHelpContext
                              _type.HRESULT]


class ISupportErrorInfo(_Unknwnbase.IUnknown):
    InterfaceSupportsErrorInfo: _Callable[[_Pointer[_struct.IID]],  # riid
                                          _type.HRESULT]


class ITypeFactory(_Unknwnbase.IUnknown):
    CreateFromTypeInfo: _Callable[[ITypeInfo,  # pTypeInfo
                                   _Pointer[_struct.IID],  # riid
                                   _Pointer[_Unknwnbase.IUnknown]],  # ppv
                                  _type.HRESULT]


class ITypeMarshal(_Unknwnbase.IUnknown):
    Size: _Callable[[_type.PVOID,  # pvType
                     _type.DWORD,  # dwDestContext
                     _type.PVOID,  # pvDestContext
                     _Pointer[_type.ULONG]],  # pSize
                    _type.HRESULT]
    Marshal: _Callable[[_type.PVOID,  # pvType
                        _type.DWORD,  # dwDestContext
                        _type.PVOID,  # pvDestContext
                        _type.ULONG,  # cbBufferLength
                        _Pointer[_type.BYTE],  # pBuffer
                        _Pointer[_type.ULONG]],  # pcbWritten
                       _type.HRESULT]
    Unmarshal: _Callable[[_type.PVOID,  # pvType
                          _type.DWORD,  # dwFlags
                          _type.ULONG,  # cbBufferLength
                          _Pointer[_type.BYTE],  # pBuffer
                          _Pointer[_type.ULONG]],  # pcbRead
                         _type.HRESULT]
    Free: _Callable[[_type.PVOID],  # pvType
                    _type.HRESULT]


class IRecordInfo(_Unknwnbase.IUnknown):
    RecordInit: _Callable[[_type.PVOID],  # pvNew
                          _type.HRESULT]
    RecordClear: _Callable[[_type.PVOID],  # pvExisting
                           _type.HRESULT]
    RecordCopy: _Callable[[_type.PVOID,  # pvExisting
                           _type.PVOID],  # pvNew
                          _type.HRESULT]
    GetGuid: _Callable[[_Pointer[_struct.GUID]],  # pguid
                       _type.HRESULT]
    GetName: _Callable[[_Pointer[_type.BSTR]],  # pbstrName
                       _type.HRESULT]
    GetSize: _Callable[[_Pointer[_type.ULONG]],  # pcbSize
                       _type.HRESULT]
    GetTypeInfo: _Callable[[_Pointer[ITypeInfo]],  # ppTypeInfo
                           _type.HRESULT]
    GetField: _Callable[[_type.PVOID,  # pvData
                         _type.LPCOLESTR,  # szFieldName
                         _Pointer[_struct.VARIANT]],  # pvarField
                        _type.HRESULT]
    GetFieldNoCopy: _Callable[[_type.PVOID,  # pvData
                               _type.LPCOLESTR,  # szFieldName
                               _Pointer[_struct.VARIANT],  # pvarField
                               _Pointer[_type.PVOID]],  # ppvDataCArray
                              _type.HRESULT]
    PutField: _Callable[[_type.ULONG,  # wFlags
                         _type.PVOID,  # pvData
                         _type.LPCOLESTR,  # szFieldName
                         _Pointer[_struct.VARIANT]],  # pvarField
                        _type.HRESULT]
    PutFieldNoCopy: _Callable[[_type.ULONG,  # wFlags
                               _type.PVOID,  # pvData
                               _type.LPCOLESTR,  # szFieldName
                               _Pointer[_struct.VARIANT]],  # pvarField
                              _type.HRESULT]
    GetFieldNames: _Callable[[_Pointer[_type.ULONG],  # pcNames
                              _Pointer[_type.BSTR]],  # rgBstrNames
                             _type.HRESULT]
    IsMatchingType: _Callable[[IRecordInfo],  # pRecordInfo
                              _type.BOOL]
    RecordCreate: _Callable[[],
                            _type.PVOID]
    RecordCreateCopy: _Callable[[_type.PVOID,  # pvSource
                                 _Pointer[_type.PVOID]],  # ppvDest
                                _type.HRESULT]
    RecordDestroy: _Callable[[_type.PVOID],  # pvRecord
                             _type.HRESULT]


class IErrorLog(_Unknwnbase.IUnknown):
    AddError: _Callable[[_type.LPCOLESTR,  # pszPropName
                         _Pointer[_struct.EXCEPINFO]],  # pExcepInfo
                        _type.HRESULT]


class IPropertyBag(_Unknwnbase.IUnknown):
    Read: _Callable[[_type.LPCOLESTR,  # pszPropName
                     _Pointer[_struct.VARIANT],  # pVar
                     IErrorLog],  # pErrorLog
                    _type.HRESULT]
    Write: _Callable[[_type.LPCOLESTR,  # pszPropName
                      _Pointer[_struct.VARIANT]],  # pVar
                     _type.HRESULT]


class ITypeLibRegistrationReader(_Unknwnbase.IUnknown):
    EnumTypeLibRegistrations: _Callable[[_Pointer[_objidlbase.IEnumUnknown]],  # ppEnumUnknown
                                        _type.HRESULT]


class ITypeLibRegistration(_Unknwnbase.IUnknown):
    GetGuid: _Callable[[_Pointer[_struct.GUID]],  # pGuid
                       _type.HRESULT]
    GetVersion: _Callable[[_Pointer[_type.BSTR]],  # pVersion
                          _type.HRESULT]
    GetLcid: _Callable[[_Pointer[_type.LCID]],  # pLcid
                       _type.HRESULT]
    GetWin32Path: _Callable[[_Pointer[_type.BSTR]],  # pWin32Path
                            _type.HRESULT]
    GetWin64Path: _Callable[[_Pointer[_type.BSTR]],  # pWin64Path
                            _type.HRESULT]
    GetDisplayName: _Callable[[_Pointer[_type.BSTR]],  # pDisplayName
                              _type.HRESULT]
    GetFlags: _Callable[[_Pointer[_type.DWORD]],  # pFlags
                        _type.HRESULT]
    GetHelpDir: _Callable[[_Pointer[_type.BSTR]],  # pHelpDir
                          _type.HRESULT]

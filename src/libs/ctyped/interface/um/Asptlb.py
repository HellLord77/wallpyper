from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import oaidl as _oaidl
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IStringList(_oaidl.IDispatch):
    get_Item: _Callable[[_struct.VARIANT,  # i
                         _Pointer[_struct.VARIANT]],  # pVariantReturn
                        _type.HRESULT]
    get_Count: _Callable[[_Pointer[_type.c_int]],  # cStrRet
                         _type.HRESULT]
    get__NewEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppEnumReturn
                            _type.HRESULT]


class IRequestDictionary(_oaidl.IDispatch):
    get_Item: _Callable[[_struct.VARIANT,  # Var
                         _Pointer[_struct.VARIANT]],  # pVariantReturn
                        _type.HRESULT]
    get__NewEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppEnumReturn
                            _type.HRESULT]
    get_Count: _Callable[[_Pointer[_type.c_int]],  # cStrRet
                         _type.HRESULT]
    get_Key: _Callable[[_struct.VARIANT,  # VarKey
                        _Pointer[_struct.VARIANT]],  # pvar
                       _type.HRESULT]


class IRequest(_oaidl.IDispatch):
    get_Item: _Callable[[_type.BSTR,  # bstrVar
                         _Pointer[_oaidl.IDispatch]],  # ppObjReturn
                        _type.HRESULT]
    get_QueryString: _Callable[[_Pointer[IRequestDictionary]],  # ppDictReturn
                               _type.HRESULT]
    get_Form: _Callable[[_Pointer[IRequestDictionary]],  # ppDictReturn
                        _type.HRESULT]
    get_Body: _Callable[[_Pointer[IRequestDictionary]],  # ppDictReturn
                        _type.HRESULT]
    get_ServerVariables: _Callable[[_Pointer[IRequestDictionary]],  # ppDictReturn
                                   _type.HRESULT]
    get_ClientCertificate: _Callable[[_Pointer[IRequestDictionary]],  # ppDictReturn
                                     _type.HRESULT]
    get_Cookies: _Callable[[_Pointer[IRequestDictionary]],  # ppDictReturn
                           _type.HRESULT]
    get_TotalBytes: _Callable[[_Pointer[_type.c_long]],  # pcbTotal
                              _type.HRESULT]
    BinaryRead: _Callable[[_Pointer[_struct.VARIANT],  # pvarCountToRead
                           _Pointer[_struct.VARIANT]],  # pvarReturn
                          _type.HRESULT]


class IReadCookie(_oaidl.IDispatch):
    get_Item: _Callable[[_struct.VARIANT,  # Var
                         _Pointer[_struct.VARIANT]],  # pVariantReturn
                        _type.HRESULT]
    get_HasKeys: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfHasKeys
                           _type.HRESULT]
    get__NewEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppEnumReturn
                            _type.HRESULT]
    get_Count: _Callable[[_Pointer[_type.c_int]],  # cStrRet
                         _type.HRESULT]
    get_Key: _Callable[[_struct.VARIANT,  # VarKey
                        _Pointer[_struct.VARIANT]],  # pvar
                       _type.HRESULT]


class IWriteCookie(_oaidl.IDispatch):
    put_Item: _Callable[[_struct.VARIANT,  # key
                         _type.BSTR],  # bstrValue
                        _type.HRESULT]
    put_Expires: _Callable[[_type.DATE],  # dtExpires
                           _type.HRESULT]
    put_Domain: _Callable[[_type.BSTR],  # bstrDomain
                          _type.HRESULT]
    put_Path: _Callable[[_type.BSTR],  # bstrPath
                        _type.HRESULT]
    put_Secure: _Callable[[_type.VARIANT_BOOL],  # fSecure
                          _type.HRESULT]
    get_HasKeys: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfHasKeys
                           _type.HRESULT]
    get__NewEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppEnumReturn
                            _type.HRESULT]


class IResponse(_oaidl.IDispatch):
    get_Buffer: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # fIsBuffering
                          _type.HRESULT]
    put_Buffer: _Callable[[_type.VARIANT_BOOL],  # fIsBuffering
                          _type.HRESULT]
    get_ContentType: _Callable[[_Pointer[_type.BSTR]],  # pbstrContentTypeRet
                               _type.HRESULT]
    put_ContentType: _Callable[[_type.BSTR],  # bstrContentType
                               _type.HRESULT]
    get_Expires: _Callable[[_Pointer[_struct.VARIANT]],  # pvarExpiresMinutesRet
                           _type.HRESULT]
    put_Expires: _Callable[[_type.c_long],  # lExpiresMinutes
                           _type.HRESULT]
    get_ExpiresAbsolute: _Callable[[_Pointer[_struct.VARIANT]],  # pvarExpiresRet
                                   _type.HRESULT]
    put_ExpiresAbsolute: _Callable[[_type.DATE],  # dtExpires
                                   _type.HRESULT]
    get_Cookies: _Callable[[_Pointer[IRequestDictionary]],  # ppCookies
                           _type.HRESULT]
    get_Status: _Callable[[_Pointer[_type.BSTR]],  # pbstrStatusRet
                          _type.HRESULT]
    put_Status: _Callable[[_type.BSTR],  # bstrStatus
                          _type.HRESULT]
    Add: _Callable[[_type.BSTR,  # bstrHeaderValue
                    _type.BSTR],  # bstrHeaderName
                   _type.HRESULT]
    AddHeader: _Callable[[_type.BSTR,  # bstrHeaderName
                          _type.BSTR],  # bstrHeaderValue
                         _type.HRESULT]
    AppendToLog: _Callable[[_type.BSTR],  # bstrLogEntry
                           _type.HRESULT]
    BinaryWrite: _Callable[[_struct.VARIANT],  # varInput
                           _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    End: _Callable[[],
                   _type.HRESULT]
    Flush: _Callable[[],
                     _type.HRESULT]
    Redirect: _Callable[[_type.BSTR],  # bstrURL
                        _type.HRESULT]
    Write: _Callable[[_struct.VARIANT],  # varText
                     _type.HRESULT]
    WriteBlock: _Callable[[_type.c_short],  # iBlockNumber
                          _type.HRESULT]
    IsClientConnected: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfIsClientConnected
                                 _type.HRESULT]
    get_CharSet: _Callable[[_Pointer[_type.BSTR]],  # pbstrCharSetRet
                           _type.HRESULT]
    put_CharSet: _Callable[[_type.BSTR],  # bstrCharSet
                           _type.HRESULT]
    Pics: _Callable[[_type.BSTR],  # bstrHeaderValue
                    _type.HRESULT]
    get_CacheControl: _Callable[[_Pointer[_type.BSTR]],  # pbstrCacheControl
                                _type.HRESULT]
    put_CacheControl: _Callable[[_type.BSTR],  # bstrCacheControl
                                _type.HRESULT]
    get_CodePage: _Callable[[_Pointer[_type.c_long]],  # plvar
                            _type.HRESULT]
    put_CodePage: _Callable[[_type.c_long],  # lvar
                            _type.HRESULT]
    get_LCID: _Callable[[_Pointer[_type.c_long]],  # plvar
                        _type.HRESULT]
    put_LCID: _Callable[[_type.c_long],  # lvar
                        _type.HRESULT]


class IVariantDictionary(_oaidl.IDispatch):
    get_Item: _Callable[[_struct.VARIANT,  # VarKey
                         _Pointer[_struct.VARIANT]],  # pvar
                        _type.HRESULT]
    put_Item: _Callable[[_struct.VARIANT,  # VarKey
                         _struct.VARIANT],  # var
                        _type.HRESULT]
    putref_Item: _Callable[[_struct.VARIANT,  # VarKey
                            _struct.VARIANT],  # var
                           _type.HRESULT]
    get_Key: _Callable[[_struct.VARIANT,  # VarKey
                        _Pointer[_struct.VARIANT]],  # pvar
                       _type.HRESULT]
    get_Count: _Callable[[_Pointer[_type.c_int]],  # cStrRet
                         _type.HRESULT]
    get__NewEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppEnumReturn
                            _type.HRESULT]
    Remove: _Callable[[_struct.VARIANT],  # VarKey
                      _type.HRESULT]
    RemoveAll: _Callable[[],
                         _type.HRESULT]


class ISessionObject(_oaidl.IDispatch):
    get_SessionID: _Callable[[_Pointer[_type.BSTR]],  # pbstrRet
                             _type.HRESULT]
    get_Value: _Callable[[_type.BSTR,  # bstrValue
                          _Pointer[_struct.VARIANT]],  # pvar
                         _type.HRESULT]
    put_Value: _Callable[[_type.BSTR,  # bstrValue
                          _struct.VARIANT],  # var
                         _type.HRESULT]
    putref_Value: _Callable[[_type.BSTR,  # bstrValue
                             _struct.VARIANT],  # var
                            _type.HRESULT]
    get_Timeout: _Callable[[_Pointer[_type.c_long]],  # plvar
                           _type.HRESULT]
    put_Timeout: _Callable[[_type.c_long],  # lvar
                           _type.HRESULT]
    Abandon: _Callable[[],
                       _type.HRESULT]
    get_CodePage: _Callable[[_Pointer[_type.c_long]],  # plvar
                            _type.HRESULT]
    put_CodePage: _Callable[[_type.c_long],  # lvar
                            _type.HRESULT]
    get_LCID: _Callable[[_Pointer[_type.c_long]],  # plvar
                        _type.HRESULT]
    put_LCID: _Callable[[_type.c_long],  # lvar
                        _type.HRESULT]
    get_StaticObjects: _Callable[[_Pointer[IVariantDictionary]],  # ppTaggedObjects
                                 _type.HRESULT]
    get_Contents: _Callable[[_Pointer[IVariantDictionary]],  # ppProperties
                            _type.HRESULT]


class IApplicationObject(_oaidl.IDispatch):
    get_Value: _Callable[[_type.BSTR,  # bstrValue
                          _Pointer[_struct.VARIANT]],  # pvar
                         _type.HRESULT]
    put_Value: _Callable[[_type.BSTR,  # bstrValue
                          _struct.VARIANT],  # var
                         _type.HRESULT]
    putref_Value: _Callable[[_type.BSTR,  # bstrValue
                             _struct.VARIANT],  # var
                            _type.HRESULT]
    Lock: _Callable[[],
                    _type.HRESULT]
    UnLock: _Callable[[],
                      _type.HRESULT]
    get_StaticObjects: _Callable[[_Pointer[IVariantDictionary]],  # ppProperties
                                 _type.HRESULT]
    get_Contents: _Callable[[_Pointer[IVariantDictionary]],  # ppProperties
                            _type.HRESULT]


class IASPError(_oaidl.IDispatch):
    get_ASPCode: _Callable[[_Pointer[_type.BSTR]],  # pbstrASPCode
                           _type.HRESULT]
    get_Number: _Callable[[_Pointer[_type.c_long]],  # plNumber
                          _type.HRESULT]
    get_Category: _Callable[[_Pointer[_type.BSTR]],  # pbstrSource
                            _type.HRESULT]
    get_File: _Callable[[_Pointer[_type.BSTR]],  # pbstrFileName
                        _type.HRESULT]
    get_Line: _Callable[[_Pointer[_type.c_long]],  # plLineNumber
                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.BSTR]],  # pbstrDescription
                               _type.HRESULT]
    get_ASPDescription: _Callable[[_Pointer[_type.BSTR]],  # pbstrDescription
                                  _type.HRESULT]
    get_Column: _Callable[[_Pointer[_type.c_long]],  # plColumn
                          _type.HRESULT]
    get_Source: _Callable[[_Pointer[_type.BSTR]],  # pbstrLineText
                          _type.HRESULT]


class IServer(_oaidl.IDispatch):
    get_ScriptTimeout: _Callable[[_Pointer[_type.c_long]],  # plTimeoutSeconds
                                 _type.HRESULT]
    put_ScriptTimeout: _Callable[[_type.c_long],  # lTimeoutSeconds
                                 _type.HRESULT]
    CreateObject: _Callable[[_type.BSTR,  # bstrProgID
                             _Pointer[_oaidl.IDispatch]],  # ppDispObject
                            _type.HRESULT]
    HTMLEncode: _Callable[[_type.BSTR,  # bstrIn
                           _Pointer[_type.BSTR]],  # pbstrEncoded
                          _type.HRESULT]
    MapPath: _Callable[[_type.BSTR,  # bstrLogicalPath
                        _Pointer[_type.BSTR]],  # pbstrPhysicalPath
                       _type.HRESULT]
    URLEncode: _Callable[[_type.BSTR,  # bstrIn
                          _Pointer[_type.BSTR]],  # pbstrEncoded
                         _type.HRESULT]
    URLPathEncode: _Callable[[_type.BSTR,  # bstrIn
                              _Pointer[_type.BSTR]],  # pbstrEncoded
                             _type.HRESULT]
    Execute: _Callable[[_type.BSTR],  # bstrLogicalPath
                       _type.HRESULT]
    Transfer: _Callable[[_type.BSTR],  # bstrLogicalPath
                        _type.HRESULT]
    GetLastError: _Callable[[_Pointer[IASPError]],  # ppASPErrorObject
                            _type.HRESULT]


class IScriptingContext(_oaidl.IDispatch):
    get_Request: _Callable[[_Pointer[IRequest]],  # ppRequest
                           _type.HRESULT]
    get_Response: _Callable[[_Pointer[IResponse]],  # ppResponse
                            _type.HRESULT]
    get_Server: _Callable[[_Pointer[IServer]],  # ppServer
                          _type.HRESULT]
    get_Session: _Callable[[_Pointer[ISessionObject]],  # ppSession
                           _type.HRESULT]
    get_Application: _Callable[[_Pointer[IApplicationObject]],  # ppApplication
                               _type.HRESULT]

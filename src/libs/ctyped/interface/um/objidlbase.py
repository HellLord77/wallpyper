from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ... import union as _union
from ..._utils import _Pointer


class IMarshal(_Unknwnbase.IUnknown):
    GetUnmarshalClass: _Callable[[_Pointer[_struct.IID],  # riid
                                  _type.c_void_p,  # pv
                                  _type.DWORD,  # dwDestContext
                                  _type.c_void_p,  # pvDestContext
                                  _type.DWORD,  # mshlflags
                                  _Pointer[_struct.CLSID]],  # pCid
                                 _type.HRESULT]
    GetMarshalSizeMax: _Callable[[_Pointer[_struct.IID],  # riid
                                  _type.c_void_p,  # pv
                                  _type.DWORD,  # dwDestContext
                                  _type.c_void_p,  # pvDestContext
                                  _type.DWORD,  # mshlflags
                                  _Pointer[_type.DWORD]],  # pSize
                                 _type.HRESULT]
    MarshalInterface: _Callable[[IStream,  # pStm
                                 _Pointer[_struct.IID],  # riid
                                 _type.c_void_p,  # pv
                                 _type.DWORD,  # dwDestContext
                                 _type.c_void_p,  # pvDestContext
                                 _type.DWORD],  # mshlflags
                                _type.HRESULT]
    UnmarshalInterface: _Callable[[IStream,  # pStm
                                   _Pointer[_struct.IID],  # riid
                                   _type.c_void_p],  # ppv
                                  _type.HRESULT]
    ReleaseMarshalData: _Callable[[IStream],  # pStm
                                  _type.HRESULT]
    DisconnectObject: _Callable[[_type.DWORD],  # dwReserved
                                _type.HRESULT]


class INoMarshal(_Unknwnbase.IUnknown):
    pass


class IAgileObject(_Unknwnbase.IUnknown):
    pass


class IActivationFilter(_Unknwnbase.IUnknown):
    HandleActivation: _Callable[[_type.DWORD,  # dwActivationType
                                 _Pointer[_struct.IID],  # rclsid
                                 _Pointer[_struct.CLSID]],  # pReplacementClsId
                                _type.HRESULT]


class IMarshal2(IMarshal):
    pass


class IMalloc(_Unknwnbase.IUnknown):
    Alloc: _Callable[[_type.SIZE_T],  # cb
                     _type.c_void_p]
    Realloc: _Callable[[_type.c_void_p,  # pv
                        _type.SIZE_T],  # cb
                       _type.c_void_p]
    Free: _Callable[[_type.c_void_p],  # pv
                    _type.c_void]
    GetSize: _Callable[[_type.c_void_p],  # pv
                       _type.SIZE_T]
    DidAlloc: _Callable[[_type.c_void_p],  # pv
                        _type.c_int]
    HeapMinimize: _Callable[[],
                            _type.c_void]


class IStdMarshalInfo(_Unknwnbase.IUnknown):
    GetClassForHandler: _Callable[[_type.DWORD,  # dwDestContext
                                   _type.c_void_p,  # pvDestContext
                                   _Pointer[_struct.CLSID]],  # pClsid
                                  _type.HRESULT]


class IExternalConnection(_Unknwnbase.IUnknown):
    AddConnection: _Callable[[_type.DWORD,  # extconn
                              _type.DWORD],  # reserved
                             _type.DWORD]
    ReleaseConnection: _Callable[[_type.DWORD,  # extconn
                                  _type.DWORD,  # reserved
                                  _type.BOOL],  # fLastReleaseCloses
                                 _type.DWORD]


class IMultiQI(_Unknwnbase.IUnknown):
    QueryMultipleInterfaces: _Callable[[_type.ULONG,  # cMQIs
                                        _Pointer[_struct.MULTI_QI]],  # pMQIs
                                       _type.HRESULT]


class AsyncIMultiQI(_Unknwnbase.IUnknown):
    Begin_QueryMultipleInterfaces: _Callable[[_type.ULONG,  # cMQIs
                                              _Pointer[_struct.MULTI_QI]],  # pMQIs
                                             _type.HRESULT]
    Finish_QueryMultipleInterfaces: _Callable[[_Pointer[_struct.MULTI_QI]],  # pMQIs
                                              _type.HRESULT]


class IInternalUnknown(_Unknwnbase.IUnknown):
    QueryInternalInterface: _Callable[[_Pointer[_struct.IID],  # riid
                                       _type.c_void_p],  # ppv
                                      _type.HRESULT]


class IEnumUnknown(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_Unknwnbase.IUnknown],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumUnknown]],  # ppenum
                     _type.HRESULT]


class IEnumString(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_type.LPOLESTR],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumString]],  # ppenum
                     _type.HRESULT]


class ISequentialStream(_Unknwnbase.IUnknown):
    Read: _Callable[[_type.c_void_p,  # pv
                     _type.ULONG,  # cb
                     _Pointer[_type.ULONG]],  # pcbRead
                    _type.HRESULT]
    Write: _Callable[[_type.c_void_p,  # pv
                      _type.ULONG,  # cb
                      _Pointer[_type.ULONG]],  # pcbWritten
                     _type.HRESULT]


class IStream(ISequentialStream):
    Seek: _Callable[[_union.LARGE_INTEGER,  # dlibMove
                     _type.DWORD,  # dwOrigin
                     _Pointer[_union.ULARGE_INTEGER]],  # plibNewPosition
                    _type.HRESULT]
    SetSize: _Callable[[_union.ULARGE_INTEGER],  # libNewSize
                       _type.HRESULT]
    CopyTo: _Callable[[IStream,  # pstm
                       _union.ULARGE_INTEGER,  # cb
                       _Pointer[_union.ULARGE_INTEGER],  # pcbRead
                       _Pointer[_union.ULARGE_INTEGER]],  # pcbWritten
                      _type.HRESULT]
    Commit: _Callable[[_type.DWORD],  # grfCommitFlags
                      _type.HRESULT]
    Revert: _Callable[[],
                      _type.HRESULT]
    LockRegion: _Callable[[_union.ULARGE_INTEGER,  # libOffset
                           _union.ULARGE_INTEGER,  # cb
                           _type.DWORD],  # dwLockType
                          _type.HRESULT]
    UnlockRegion: _Callable[[_union.ULARGE_INTEGER,  # libOffset
                             _union.ULARGE_INTEGER,  # cb
                             _type.DWORD],  # dwLockType
                            _type.HRESULT]
    Stat: _Callable[[_Pointer[_struct.STATSTG],  # pstatstg
                     _type.DWORD],  # grfStatFlag
                    _type.HRESULT]
    Clone: _Callable[[_Pointer[IStream]],  # ppstm
                     _type.HRESULT]


class IRpcChannelBuffer(_Unknwnbase.IUnknown):
    GetBuffer: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMessage
                          _Pointer[_struct.IID]],  # riid
                         _type.HRESULT]
    SendReceive: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMessage
                            _Pointer[_type.ULONG]],  # pStatus
                           _type.HRESULT]
    FreeBuffer: _Callable[[_Pointer[_struct.RPCOLEMESSAGE]],  # pMessage
                          _type.HRESULT]
    GetDestCtx: _Callable[[_Pointer[_type.DWORD],  # pdwDestContext
                           _type.c_void_p],  # ppvDestContext
                          _type.HRESULT]
    IsConnected: _Callable[[],
                           _type.HRESULT]


class IRpcChannelBuffer2(IRpcChannelBuffer):
    GetProtocolVersion: _Callable[[_Pointer[_type.DWORD]],  # pdwVersion
                                  _type.HRESULT]


class IAsyncRpcChannelBuffer(IRpcChannelBuffer2):
    Send: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMsg
                     ISynchronize,  # pSync
                     _Pointer[_type.ULONG]],  # pulStatus
                    _type.HRESULT]
    Receive: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMsg
                        _Pointer[_type.ULONG]],  # pulStatus
                       _type.HRESULT]
    GetDestCtxEx: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMsg
                             _Pointer[_type.DWORD],  # pdwDestContext
                             _type.c_void_p],  # ppvDestContext
                            _type.HRESULT]


class IRpcChannelBuffer3(IRpcChannelBuffer2):
    Send: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMsg
                     _Pointer[_type.ULONG]],  # pulStatus
                    _type.HRESULT]
    Receive: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMsg
                        _type.ULONG,  # ulSize
                        _Pointer[_type.ULONG]],  # pulStatus
                       _type.HRESULT]
    Cancel: _Callable[[_Pointer[_struct.RPCOLEMESSAGE]],  # pMsg
                      _type.HRESULT]
    GetCallContext: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMsg
                               _Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # pInterface
                              _type.HRESULT]
    GetDestCtxEx: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMsg
                             _Pointer[_type.DWORD],  # pdwDestContext
                             _type.c_void_p],  # ppvDestContext
                            _type.HRESULT]
    GetState: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMsg
                         _Pointer[_type.DWORD]],  # pState
                        _type.HRESULT]
    RegisterAsync: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMsg
                              IAsyncManager],  # pAsyncMgr
                             _type.HRESULT]


class IRpcSyntaxNegotiate(_Unknwnbase.IUnknown):
    NegotiateSyntax: _Callable[[_Pointer[_struct.RPCOLEMESSAGE]],  # pMsg
                               _type.HRESULT]


class IRpcProxyBuffer(_Unknwnbase.IUnknown):
    Connect: _Callable[[IRpcChannelBuffer],  # pRpcChannelBuffer
                       _type.HRESULT]
    Disconnect: _Callable[[],
                          _type.c_void]


class IRpcStubBuffer(_Unknwnbase.IUnknown):
    Connect: _Callable[[_Unknwnbase.IUnknown],  # pUnkServer
                       _type.HRESULT]
    Disconnect: _Callable[[],
                          _type.c_void]
    Invoke: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # _prpcmsg
                       IRpcChannelBuffer],  # _pRpcChannelBuffer
                      _type.HRESULT]
    IsIIDSupported: _Callable[[_Pointer[_struct.IID]],  # riid
                              IRpcStubBuffer]
    CountRefs: _Callable[[],
                         _type.ULONG]
    DebugServerQueryInterface: _Callable[[_type.c_void_p],  # ppv
                                         _type.HRESULT]
    DebugServerRelease: _Callable[[_type.c_void_p],  # pv
                                  _type.c_void]


class IPSFactoryBuffer(_Unknwnbase.IUnknown):
    CreateProxy: _Callable[[_Unknwnbase.IUnknown,  # pUnkOuter
                            _Pointer[_struct.IID],  # riid
                            _Pointer[IRpcProxyBuffer],  # ppProxy
                            _type.c_void_p],  # ppv
                           _type.HRESULT]
    CreateStub: _Callable[[_Pointer[_struct.IID],  # riid
                           _Unknwnbase.IUnknown,  # pUnkServer
                           _Pointer[IRpcStubBuffer]],  # ppStub
                          _type.HRESULT]


class IChannelHook(_Unknwnbase.IUnknown):
    ClientGetSize: _Callable[[_Pointer[_struct.GUID],  # uExtent
                              _Pointer[_struct.IID],  # riid
                              _Pointer[_type.ULONG]],  # pDataSize
                             _type.c_void]
    ClientFillBuffer: _Callable[[_Pointer[_struct.GUID],  # uExtent
                                 _Pointer[_struct.IID],  # riid
                                 _Pointer[_type.ULONG],  # pDataSize
                                 _type.c_void_p],  # pDataBuffer
                                _type.c_void]
    ClientNotify: _Callable[[_Pointer[_struct.GUID],  # uExtent
                             _Pointer[_struct.IID],  # riid
                             _type.ULONG,  # cbDataSize
                             _type.c_void_p,  # pDataBuffer
                             _type.DWORD,  # lDataRep
                             _type.HRESULT],  # hrFault
                            _type.c_void]
    ServerNotify: _Callable[[_Pointer[_struct.GUID],  # uExtent
                             _Pointer[_struct.IID],  # riid
                             _type.ULONG,  # cbDataSize
                             _type.c_void_p,  # pDataBuffer
                             _type.DWORD],  # lDataRep
                            _type.c_void]
    ServerGetSize: _Callable[[_Pointer[_struct.GUID],  # uExtent
                              _Pointer[_struct.IID],  # riid
                              _type.HRESULT,  # hrFault
                              _Pointer[_type.ULONG]],  # pDataSize
                             _type.c_void]
    ServerFillBuffer: _Callable[[_Pointer[_struct.GUID],  # uExtent
                                 _Pointer[_struct.IID],  # riid
                                 _Pointer[_type.ULONG],  # pDataSize
                                 _type.c_void_p,  # pDataBuffer
                                 _type.HRESULT],  # hrFault
                                _type.c_void]


class IClientSecurity(_Unknwnbase.IUnknown):
    QueryBlanket: _Callable[[_Unknwnbase.IUnknown,  # pProxy
                             _Pointer[_type.DWORD],  # pAuthnSvc
                             _Pointer[_type.DWORD],  # pAuthzSvc
                             _Pointer[_Pointer[_type.OLECHAR]],  # pServerPrincName
                             _Pointer[_type.DWORD],  # pAuthnLevel
                             _Pointer[_type.DWORD],  # pImpLevel
                             _type.c_void_p,  # pAuthInfo
                             _Pointer[_type.DWORD]],  # pCapabilites
                            _type.HRESULT]
    SetBlanket: _Callable[[_Unknwnbase.IUnknown,  # pProxy
                           _type.DWORD,  # dwAuthnSvc
                           _type.DWORD,  # dwAuthzSvc
                           _Pointer[_type.OLECHAR],  # pServerPrincName
                           _type.DWORD,  # dwAuthnLevel
                           _type.DWORD,  # dwImpLevel
                           _type.c_void_p,  # pAuthInfo
                           _type.DWORD],  # dwCapabilities
                          _type.HRESULT]
    CopyProxy: _Callable[[_Unknwnbase.IUnknown,  # pProxy
                          _Pointer[_Unknwnbase.IUnknown]],  # ppCopy
                         _type.HRESULT]


class IServerSecurity(_Unknwnbase.IUnknown):
    QueryBlanket: _Callable[[_Pointer[_type.DWORD],  # pAuthnSvc
                             _Pointer[_type.DWORD],  # pAuthzSvc
                             _Pointer[_Pointer[_type.OLECHAR]],  # pServerPrincName
                             _Pointer[_type.DWORD],  # pAuthnLevel
                             _Pointer[_type.DWORD],  # pImpLevel
                             _type.c_void_p,  # pPrivs
                             _Pointer[_type.DWORD]],  # pCapabilities
                            _type.HRESULT]
    ImpersonateClient: _Callable[[],
                                 _type.HRESULT]
    RevertToSelf: _Callable[[],
                            _type.HRESULT]
    IsImpersonating: _Callable[[],
                               _type.BOOL]


class IRpcOptions(_Unknwnbase.IUnknown):
    Set: _Callable[[_Unknwnbase.IUnknown,  # pPrx
                    _enum.RPCOPT_PROPERTIES,  # dwProperty
                    _type.ULONG_PTR],  # dwValue
                   _type.HRESULT]
    Query: _Callable[[_Unknwnbase.IUnknown,  # pPrx
                      _enum.RPCOPT_PROPERTIES,  # dwProperty
                      _Pointer[_type.ULONG_PTR]],  # pdwValue
                     _type.HRESULT]


class IGlobalOptions(_Unknwnbase.IUnknown):
    Set: _Callable[[_enum.GLOBALOPT_PROPERTIES,  # dwProperty
                    _type.ULONG_PTR],  # dwValue
                   _type.HRESULT]
    Query: _Callable[[_enum.GLOBALOPT_PROPERTIES,  # dwProperty
                      _Pointer[_type.ULONG_PTR]],  # pdwValue
                     _type.HRESULT]


class ISurrogate(_Unknwnbase.IUnknown):
    LoadDllServer: _Callable[[_Pointer[_struct.IID]],  # Clsid
                             _type.HRESULT]
    FreeSurrogate: _Callable[[],
                             _type.HRESULT]


class IGlobalInterfaceTable(_Unknwnbase.IUnknown):
    RegisterInterfaceInGlobal: _Callable[[_Unknwnbase.IUnknown,  # pUnk
                                          _Pointer[_struct.IID],  # riid
                                          _Pointer[_type.DWORD]],  # pdwCookie
                                         _type.HRESULT]
    RevokeInterfaceFromGlobal: _Callable[[_type.DWORD],  # dwCookie
                                         _type.HRESULT]
    GetInterfaceFromGlobal: _Callable[[_type.DWORD,  # dwCookie
                                       _Pointer[_struct.IID],  # riid
                                       _type.c_void_p],  # ppv
                                      _type.HRESULT]


class ISynchronize(_Unknwnbase.IUnknown):
    Wait: _Callable[[_type.DWORD,  # dwFlags
                     _type.DWORD],  # dwMilliseconds
                    _type.HRESULT]
    Signal: _Callable[[],
                      _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]


class ISynchronizeHandle(_Unknwnbase.IUnknown):
    GetHandle: _Callable[[_Pointer[_type.HANDLE]],  # ph
                         _type.HRESULT]


class ISynchronizeEvent(ISynchronizeHandle):
    SetEventHandle: _Callable[[_Pointer[_type.HANDLE]],  # ph
                              _type.HRESULT]


class ISynchronizeContainer(_Unknwnbase.IUnknown):
    AddSynchronize: _Callable[[ISynchronize],  # pSync
                              _type.HRESULT]
    WaitMultiple: _Callable[[_type.DWORD,  # dwFlags
                             _type.DWORD,  # dwTimeOut
                             _Pointer[ISynchronize]],  # ppSync
                            _type.HRESULT]


class ISynchronizeMutex(ISynchronize):
    ReleaseMutex: _Callable[[],
                            _type.HRESULT]


class ICancelMethodCalls(_Unknwnbase.IUnknown):
    Cancel: _Callable[[_type.ULONG],  # ulSeconds
                      _type.HRESULT]
    TestCancel: _Callable[[],
                          _type.HRESULT]


class IAsyncManager(_Unknwnbase.IUnknown):
    CompleteCall: _Callable[[_type.HRESULT],  # Result
                            _type.HRESULT]
    GetCallContext: _Callable[[_Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # pInterface
                              _type.HRESULT]
    GetState: _Callable[[_Pointer[_type.ULONG]],  # pulStateFlags
                        _type.HRESULT]


class ICallFactory(_Unknwnbase.IUnknown):
    CreateCall: _Callable[[_Pointer[_struct.IID],  # riid
                           _Unknwnbase.IUnknown,  # pCtrlUnk
                           _Pointer[_struct.IID],  # riid2
                           _Pointer[_Unknwnbase.IUnknown]],  # ppv
                          _type.HRESULT]


class IRpcHelper(_Unknwnbase.IUnknown):
    GetDCOMProtocolVersion: _Callable[[_Pointer[_type.DWORD]],  # pComVersion
                                      _type.HRESULT]
    GetIIDFromOBJREF: _Callable[[_type.c_void_p,  # pObjRef
                                 _Pointer[_Pointer[_struct.IID]]],  # piid
                                _type.HRESULT]


class IReleaseMarshalBuffers(_Unknwnbase.IUnknown):
    ReleaseMarshalBuffer: _Callable[[_Pointer[_struct.RPCOLEMESSAGE],  # pMsg
                                     _type.DWORD,  # dwFlags
                                     _Unknwnbase.IUnknown],  # pChnl
                                    _type.HRESULT]


class IWaitMultiple(_Unknwnbase.IUnknown):
    WaitMultiple: _Callable[[_type.DWORD,  # timeout
                             _Pointer[ISynchronize]],  # pSync
                            _type.HRESULT]
    AddSynchronize: _Callable[[ISynchronize],  # pSync
                              _type.HRESULT]


class IAddrTrackingControl(_Unknwnbase.IUnknown):
    EnableCOMDynamicAddrTracking: _Callable[[],
                                            _type.HRESULT]
    DisableCOMDynamicAddrTracking: _Callable[[],
                                             _type.HRESULT]


class IAddrExclusionControl(_Unknwnbase.IUnknown):
    GetCurrentAddrExclusionList: _Callable[[_Pointer[_struct.IID],  # riid
                                            _type.c_void_p],  # ppEnumerator
                                           _type.HRESULT]
    UpdateAddrExclusionList: _Callable[[_Unknwnbase.IUnknown],  # pEnumerator
                                       _type.HRESULT]


class IPipeByte(_Unknwnbase.IUnknown):
    Pull: _Callable[[_Pointer[_type.BYTE],  # buf
                     _type.ULONG,  # cRequest
                     _Pointer[_type.ULONG]],  # pcReturned
                    _type.HRESULT]
    Push: _Callable[[_Pointer[_type.BYTE],  # buf
                     _type.ULONG],  # cSent
                    _type.HRESULT]


class AsyncIPipeByte(_Unknwnbase.IUnknown):
    Begin_Pull: _Callable[[_type.ULONG],  # cRequest
                          _type.HRESULT]
    Finish_Pull: _Callable[[_Pointer[_type.BYTE],  # buf
                            _Pointer[_type.ULONG]],  # pcReturned
                           _type.HRESULT]
    Begin_Push: _Callable[[_Pointer[_type.BYTE],  # buf
                           _type.ULONG],  # cSent
                          _type.HRESULT]
    Finish_Push: _Callable[[],
                           _type.HRESULT]


class IPipeLong(_Unknwnbase.IUnknown):
    Pull: _Callable[[_Pointer[_type.LONG],  # buf
                     _type.ULONG,  # cRequest
                     _Pointer[_type.ULONG]],  # pcReturned
                    _type.HRESULT]
    Push: _Callable[[_Pointer[_type.LONG],  # buf
                     _type.ULONG],  # cSent
                    _type.HRESULT]


class AsyncIPipeLong(_Unknwnbase.IUnknown):
    Begin_Pull: _Callable[[_type.ULONG],  # cRequest
                          _type.HRESULT]
    Finish_Pull: _Callable[[_Pointer[_type.LONG],  # buf
                            _Pointer[_type.ULONG]],  # pcReturned
                           _type.HRESULT]
    Begin_Push: _Callable[[_Pointer[_type.LONG],  # buf
                           _type.ULONG],  # cSent
                          _type.HRESULT]
    Finish_Push: _Callable[[],
                           _type.HRESULT]


class IPipeDouble(_Unknwnbase.IUnknown):
    Pull: _Callable[[_Pointer[_type.DOUBLE],  # buf
                     _type.ULONG,  # cRequest
                     _Pointer[_type.ULONG]],  # pcReturned
                    _type.HRESULT]
    Push: _Callable[[_Pointer[_type.DOUBLE],  # buf
                     _type.ULONG],  # cSent
                    _type.HRESULT]


class AsyncIPipeDouble(_Unknwnbase.IUnknown):
    Begin_Pull: _Callable[[_type.ULONG],  # cRequest
                          _type.HRESULT]
    Finish_Pull: _Callable[[_Pointer[_type.DOUBLE],  # buf
                            _Pointer[_type.ULONG]],  # pcReturned
                           _type.HRESULT]
    Begin_Push: _Callable[[_Pointer[_type.DOUBLE],  # buf
                           _type.ULONG],  # cSent
                          _type.HRESULT]
    Finish_Push: _Callable[[],
                           _type.HRESULT]


class IComThreadingInfo(_Unknwnbase.IUnknown):
    GetCurrentApartmentType: _Callable[[_Pointer[_enum.APTTYPE]],  # pAptType
                                       _type.HRESULT]
    GetCurrentThreadType: _Callable[[_Pointer[_enum.THDTYPE]],  # pThreadType
                                    _type.HRESULT]
    GetCurrentLogicalThreadId: _Callable[[_Pointer[_struct.GUID]],  # pguidLogicalThreadId
                                         _type.HRESULT]
    SetCurrentLogicalThreadId: _Callable[[_Pointer[_struct.GUID]],  # rguid
                                         _type.HRESULT]


class IProcessInitControl(_Unknwnbase.IUnknown):
    ResetInitializerTimeout: _Callable[[_type.DWORD],  # dwSecondsRemaining
                                       _type.HRESULT]


class IFastRundown(_Unknwnbase.IUnknown):
    pass


class IMarshalingStream(IStream):
    GetMarshalingContextAttribute: _Callable[[_enum.CO_MARSHALING_CONTEXT_ATTRIBUTES,  # attribute
                                              _Pointer[_type.ULONG_PTR]],  # pAttributeValue
                                             _type.HRESULT]


class IAgileReference(_Unknwnbase.IUnknown):
    Resolve: _Callable[[_Pointer[_struct.IID],  # riid
                        _type.c_void_p],  # ppvObjectReference
                       _type.HRESULT]


class IMachineGlobalObjectTable(_Unknwnbase.IUnknown):
    RegisterObject: _Callable[[_Pointer[_struct.IID],  # clsid
                               _type.LPCWSTR,  # identifier
                               _Unknwnbase.IUnknown,  # object
                               _Pointer[_struct.MachineGlobalObjectTableRegistrationToken]],  # token
                              _type.HRESULT]
    GetObjectA: _Callable[[_Pointer[_struct.IID],  # clsid
                           _type.LPCWSTR,  # identifier
                           _Pointer[_struct.IID],  # riid
                           _type.c_void_p],  # ppv
                          _type.HRESULT]
    RevokeObject: _Callable[[_struct.MachineGlobalObjectTableRegistrationToken],  # token
                            _type.HRESULT]


class ISupportAllowLowerTrustActivation(_Unknwnbase.IUnknown):
    pass

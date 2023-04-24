from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import objidlbase as _objidlbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ... import union as _union
from ..._utils import _Pointer


class IMallocSpy(_Unknwnbase.IUnknown):
    PreAlloc: _Callable[[_type.SIZE_T],  # cbRequest
                        _type.SIZE_T]
    PostAlloc: _Callable[[_type.c_void_p],  # pActual
                         _type.c_void_p]
    PreFree: _Callable[[_type.c_void_p,  # pRequest
                        _type.BOOL],  # fSpyed
                       _type.c_void_p]
    PostFree: _Callable[[_type.BOOL],  # fSpyed
                        _type.c_void]
    PreRealloc: _Callable[[_type.c_void_p,  # pRequest
                           _type.SIZE_T,  # cbRequest
                           _type.c_void_p,  # ppNewRequest
                           _type.BOOL],  # fSpyed
                          _type.SIZE_T]
    PostRealloc: _Callable[[_type.c_void_p,  # pActual
                            _type.BOOL],  # fSpyed
                           _type.c_void_p]
    PreGetSize: _Callable[[_type.c_void_p,  # pRequest
                           _type.BOOL],  # fSpyed
                          _type.c_void_p]
    PostGetSize: _Callable[[_type.SIZE_T,  # cbActual
                            _type.BOOL],  # fSpyed
                           _type.SIZE_T]
    PreDidAlloc: _Callable[[_type.c_void_p,  # pRequest
                            _type.BOOL],  # fSpyed
                           _type.c_void_p]
    PostDidAlloc: _Callable[[_type.c_void_p,  # pRequest
                             _type.BOOL,  # fSpyed
                             _type.c_int],  # fActual
                            _type.c_int]
    PreHeapMinimize: _Callable[[],
                               _type.c_void]
    PostHeapMinimize: _Callable[[],
                                _type.c_void]


class IBindCtx(_Unknwnbase.IUnknown):
    RegisterObjectBound: _Callable[[_Unknwnbase.IUnknown],  # punk
                                   _type.HRESULT]
    RevokeObjectBound: _Callable[[_Unknwnbase.IUnknown],  # punk
                                 _type.HRESULT]
    ReleaseBoundObjects: _Callable[[],
                                   _type.HRESULT]
    SetBindOptions: _Callable[[_Pointer[_struct.BIND_OPTS]],  # pbindopts
                              _type.HRESULT]
    GetBindOptions: _Callable[[_Pointer[_struct.BIND_OPTS]],  # pbindopts
                              _type.HRESULT]
    GetRunningObjectTable: _Callable[[_Pointer[IRunningObjectTable]],  # pprot
                                     _type.HRESULT]
    RegisterObjectParam: _Callable[[_type.LPOLESTR,  # pszKey
                                    _Unknwnbase.IUnknown],  # punk
                                   _type.HRESULT]
    GetObjectParam: _Callable[[_type.LPOLESTR,  # pszKey
                               _Pointer[_Unknwnbase.IUnknown]],  # ppunk
                              _type.HRESULT]
    EnumObjectParam: _Callable[[_Pointer[_objidlbase.IEnumString]],  # ppenum
                               _type.HRESULT]
    RevokeObjectParam: _Callable[[_type.LPOLESTR],  # pszKey
                                 _type.HRESULT]


class IEnumMoniker(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[IMoniker],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumMoniker]],  # ppenum
                     _type.HRESULT]


class IRunnableObject(_Unknwnbase.IUnknown):
    GetRunningClass: _Callable[[_Pointer[_struct.CLSID]],  # lpClsid
                               _type.HRESULT]
    Run: _Callable[[IBindCtx],  # pbc
                   _type.HRESULT]
    IsRunning: _Callable[[],
                         _type.BOOL]
    LockRunning: _Callable[[_type.BOOL,  # fLock
                            _type.BOOL],  # fLastUnlockCloses
                           _type.HRESULT]
    SetContainedObject: _Callable[[_type.BOOL],  # fContained
                                  _type.HRESULT]


class IRunningObjectTable(_Unknwnbase.IUnknown):
    Register: _Callable[[_type.DWORD,  # grfFlags
                         _Unknwnbase.IUnknown,  # punkObject
                         IMoniker,  # pmkObjectName
                         _Pointer[_type.DWORD]],  # pdwRegister
                        _type.HRESULT]
    Revoke: _Callable[[_type.DWORD],  # dwRegister
                      _type.HRESULT]
    IsRunning: _Callable[[IMoniker],  # pmkObjectName
                         _type.HRESULT]
    GetObjectA: _Callable[[IMoniker,  # pmkObjectName
                           _Pointer[_Unknwnbase.IUnknown]],  # ppunkObject
                          _type.HRESULT]
    NoteChangeTime: _Callable[[_type.DWORD,  # dwRegister
                               _Pointer[_struct.FILETIME]],  # pfiletime
                              _type.HRESULT]
    GetTimeOfLastChange: _Callable[[IMoniker,  # pmkObjectName
                                    _Pointer[_struct.FILETIME]],  # pfiletime
                                   _type.HRESULT]
    EnumRunning: _Callable[[_Pointer[IEnumMoniker]],  # ppenumMoniker
                           _type.HRESULT]


class IPersist(_Unknwnbase.IUnknown):
    GetClassID: _Callable[[_Pointer[_struct.CLSID]],  # pClassID
                          _type.HRESULT]


class IPersistStream(IPersist):
    IsDirty: _Callable[[],
                       _type.HRESULT]
    Load: _Callable[[_objidlbase.IStream],  # pStm
                    _type.HRESULT]
    Save: _Callable[[_objidlbase.IStream,  # pStm
                     _type.BOOL],  # fClearDirty
                    _type.HRESULT]
    GetSizeMax: _Callable[[_Pointer[_union.ULARGE_INTEGER]],  # pcbSize
                          _type.HRESULT]


class IMoniker(IPersistStream):
    BindToObject: _Callable[[IBindCtx,  # pbc
                             IMoniker,  # pmkToLeft
                             _Pointer[_struct.IID],  # riidResult
                             _type.c_void_p],  # ppvResult
                            _type.HRESULT]
    BindToStorage: _Callable[[IBindCtx,  # pbc
                              IMoniker,  # pmkToLeft
                              _Pointer[_struct.IID],  # riid
                              _type.c_void_p],  # ppvObj
                             _type.HRESULT]
    Reduce: _Callable[[IBindCtx,  # pbc
                       _type.DWORD,  # dwReduceHowFar
                       _Pointer[IMoniker],  # ppmkToLeft
                       _Pointer[IMoniker]],  # ppmkReduced
                      _type.HRESULT]
    ComposeWith: _Callable[[IMoniker,  # pmkRight
                            _type.BOOL,  # fOnlyIfNotGeneric
                            _Pointer[IMoniker]],  # ppmkComposite
                           _type.HRESULT]
    Enum: _Callable[[_type.BOOL,  # fForward
                     _Pointer[IEnumMoniker]],  # ppenumMoniker
                    _type.HRESULT]
    IsEqual: _Callable[[IMoniker],  # pmkOtherMoniker
                       _type.HRESULT]
    Hash: _Callable[[_Pointer[_type.DWORD]],  # pdwHash
                    _type.HRESULT]
    IsRunning: _Callable[[IBindCtx,  # pbc
                          IMoniker,  # pmkToLeft
                          IMoniker],  # pmkNewlyRunning
                         _type.HRESULT]
    GetTimeOfLastChange: _Callable[[IBindCtx,  # pbc
                                    IMoniker,  # pmkToLeft
                                    _Pointer[_struct.FILETIME]],  # pFileTime
                                   _type.HRESULT]
    Inverse: _Callable[[_Pointer[IMoniker]],  # ppmk
                       _type.HRESULT]
    CommonPrefixWith: _Callable[[IMoniker,  # pmkOther
                                 _Pointer[IMoniker]],  # ppmkPrefix
                                _type.HRESULT]
    RelativePathTo: _Callable[[IMoniker,  # pmkOther
                               _Pointer[IMoniker]],  # ppmkRelPath
                              _type.HRESULT]
    GetDisplayName: _Callable[[IBindCtx,  # pbc
                               IMoniker,  # pmkToLeft
                               _Pointer[_type.LPOLESTR]],  # ppszDisplayName
                              _type.HRESULT]
    ParseDisplayName: _Callable[[IBindCtx,  # pbc
                                 IMoniker,  # pmkToLeft
                                 _type.LPOLESTR,  # pszDisplayName
                                 _Pointer[_type.ULONG],  # pchEaten
                                 _Pointer[IMoniker]],  # ppmkOut
                                _type.HRESULT]
    IsSystemMoniker: _Callable[[_Pointer[_type.DWORD]],  # pdwMksys
                               _type.HRESULT]


class IROTData(_Unknwnbase.IUnknown):
    GetComparisonData: _Callable[[_Pointer[_type.byte],  # pbData
                                  _type.ULONG,  # cbMax
                                  _Pointer[_type.ULONG]],  # pcbData
                                 _type.HRESULT]


class IEnumSTATSTG(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_struct.STATSTG],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumSTATSTG]],  # ppenum
                     _type.HRESULT]


class IStorage(_Unknwnbase.IUnknown):
    CreateStream: _Callable[[_Pointer[_type.OLECHAR],  # pwcsName
                             _type.DWORD,  # grfMode
                             _type.DWORD,  # reserved1
                             _type.DWORD,  # reserved2
                             _Pointer[_objidlbase.IStream]],  # ppstm
                            _type.HRESULT]
    OpenStream: _Callable[[_Pointer[_type.OLECHAR],  # pwcsName
                           _type.c_void_p,  # reserved1
                           _type.DWORD,  # grfMode
                           _type.DWORD,  # reserved2
                           _Pointer[_objidlbase.IStream]],  # ppstm
                          _type.HRESULT]
    CreateStorage: _Callable[[_Pointer[_type.OLECHAR],  # pwcsName
                              _type.DWORD,  # grfMode
                              _type.DWORD,  # reserved1
                              _type.DWORD,  # reserved2
                              _Pointer[IStorage]],  # ppstg
                             _type.HRESULT]
    OpenStorage: _Callable[[_Pointer[_type.OLECHAR],  # pwcsName
                            IStorage,  # pstgPriority
                            _type.DWORD,  # grfMode
                            _Pointer[_type.OLECHAR],  # snbExclude
                            _type.DWORD,  # reserved
                            _Pointer[IStorage]],  # ppstg
                           _type.HRESULT]
    CopyTo: _Callable[[_type.DWORD,  # ciidExclude
                       _Pointer[_struct.IID],  # rgiidExclude
                       _Pointer[_type.OLECHAR],  # snbExclude
                       IStorage],  # pstgDest
                      _type.HRESULT]
    MoveElementTo: _Callable[[_Pointer[_type.OLECHAR],  # pwcsName
                              IStorage,  # pstgDest
                              _Pointer[_type.OLECHAR],  # pwcsNewName
                              _type.DWORD],  # grfFlags
                             _type.HRESULT]
    Commit: _Callable[[_type.DWORD],  # grfCommitFlags
                      _type.HRESULT]
    Revert: _Callable[[],
                      _type.HRESULT]
    EnumElements: _Callable[[_type.DWORD,  # reserved1
                             _type.c_void_p,  # reserved2
                             _type.DWORD,  # reserved3
                             _Pointer[IEnumSTATSTG]],  # ppenum
                            _type.HRESULT]
    DestroyElement: _Callable[[_Pointer[_type.OLECHAR]],  # pwcsName
                              _type.HRESULT]
    RenameElement: _Callable[[_Pointer[_type.OLECHAR],  # pwcsOldName
                              _Pointer[_type.OLECHAR]],  # pwcsNewName
                             _type.HRESULT]
    SetElementTimes: _Callable[[_Pointer[_type.OLECHAR],  # pwcsName
                                _Pointer[_struct.FILETIME],  # pctime
                                _Pointer[_struct.FILETIME],  # patime
                                _Pointer[_struct.FILETIME]],  # pmtime
                               _type.HRESULT]
    SetClass: _Callable[[_Pointer[_struct.IID]],  # clsid
                        _type.HRESULT]
    SetStateBits: _Callable[[_type.DWORD,  # grfStateBits
                             _type.DWORD],  # grfMask
                            _type.HRESULT]
    Stat: _Callable[[_Pointer[_struct.STATSTG],  # pstatstg
                     _type.DWORD],  # grfStatFlag
                    _type.HRESULT]


class IPersistFile(IPersist):
    IsDirty: _Callable[[],
                       _type.HRESULT]
    Load: _Callable[[_type.LPCOLESTR,  # pszFileName
                     _type.DWORD],  # dwMode
                    _type.HRESULT]
    Save: _Callable[[_type.LPCOLESTR,  # pszFileName
                     _type.BOOL],  # fRemember
                    _type.HRESULT]
    SaveCompleted: _Callable[[_type.LPCOLESTR],  # pszFileName
                             _type.HRESULT]
    GetCurFile: _Callable[[_Pointer[_type.LPOLESTR]],  # ppszFileName
                          _type.HRESULT]


class IPersistStorage(IPersist):
    IsDirty: _Callable[[],
                       _type.HRESULT]
    InitNew: _Callable[[IStorage],  # pStg
                       _type.HRESULT]
    Load: _Callable[[IStorage],  # pStg
                    _type.HRESULT]
    Save: _Callable[[IStorage,  # pStgSave
                     _type.BOOL],  # fSameAsLoad
                    _type.HRESULT]
    SaveCompleted: _Callable[[IStorage],  # pStgNew
                             _type.HRESULT]
    HandsOffStorage: _Callable[[],
                               _type.HRESULT]


class ILockBytes(_Unknwnbase.IUnknown):
    ReadAt: _Callable[[_union.ULARGE_INTEGER,  # ulOffset
                       _type.c_void_p,  # pv
                       _type.ULONG,  # cb
                       _Pointer[_type.ULONG]],  # pcbRead
                      _type.HRESULT]
    WriteAt: _Callable[[_union.ULARGE_INTEGER,  # ulOffset
                        _type.c_void_p,  # pv
                        _type.ULONG,  # cb
                        _Pointer[_type.ULONG]],  # pcbWritten
                       _type.HRESULT]
    Flush: _Callable[[],
                     _type.HRESULT]
    SetSize: _Callable[[_union.ULARGE_INTEGER],  # cb
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


class IEnumFORMATETC(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_struct.FORMATETC],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumFORMATETC]],  # ppenum
                     _type.HRESULT]


class IEnumSTATDATA(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_struct.STATDATA],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumSTATDATA]],  # ppenum
                     _type.HRESULT]


class IRootStorage(_Unknwnbase.IUnknown):
    SwitchToFile: _Callable[[_type.LPOLESTR],  # pszFile
                            _type.HRESULT]


class IAdviseSink(_Unknwnbase.IUnknown):
    OnDataChange: _Callable[[_Pointer[_struct.FORMATETC],  # pFormatetc
                             _Pointer[_struct.STGMEDIUM]],  # pStgmed
                            _type.c_void]
    OnViewChange: _Callable[[_type.DWORD,  # dwAspect
                             _type.LONG],  # lindex
                            _type.c_void]
    OnRename: _Callable[[IMoniker],  # pmk
                        _type.c_void]
    OnSave: _Callable[[],
                      _type.c_void]
    OnClose: _Callable[[],
                       _type.c_void]


class AsyncIAdviseSink(_Unknwnbase.IUnknown):
    Begin_OnDataChange: _Callable[[_Pointer[_struct.FORMATETC],  # pFormatetc
                                   _Pointer[_struct.STGMEDIUM]],  # pStgmed
                                  _type.c_void]
    Finish_OnDataChange: _Callable[[],
                                   _type.c_void]
    Begin_OnViewChange: _Callable[[_type.DWORD,  # dwAspect
                                   _type.LONG],  # lindex
                                  _type.c_void]
    Finish_OnViewChange: _Callable[[],
                                   _type.c_void]
    Begin_OnRename: _Callable[[IMoniker],  # pmk
                              _type.c_void]
    Finish_OnRename: _Callable[[],
                               _type.c_void]
    Begin_OnSave: _Callable[[],
                            _type.c_void]
    Finish_OnSave: _Callable[[],
                             _type.c_void]
    Begin_OnClose: _Callable[[],
                             _type.c_void]
    Finish_OnClose: _Callable[[],
                              _type.c_void]


class IAdviseSink2(IAdviseSink):
    OnLinkSrcChange: _Callable[[IMoniker],  # pmk
                               _type.c_void]


class AsyncIAdviseSink2(AsyncIAdviseSink):
    Begin_OnLinkSrcChange: _Callable[[IMoniker],  # pmk
                                     _type.c_void]
    Finish_OnLinkSrcChange: _Callable[[],
                                      _type.c_void]


class IDataObject(_Unknwnbase.IUnknown):
    GetData: _Callable[[_Pointer[_struct.FORMATETC],  # pformatetcIn
                        _Pointer[_struct.STGMEDIUM]],  # pmedium
                       _type.HRESULT]
    GetDataHere: _Callable[[_Pointer[_struct.FORMATETC],  # pformatetc
                            _Pointer[_struct.STGMEDIUM]],  # pmedium
                           _type.HRESULT]
    QueryGetData: _Callable[[_Pointer[_struct.FORMATETC]],  # pformatetc
                            _type.HRESULT]
    GetCanonicalFormatEtc: _Callable[[_Pointer[_struct.FORMATETC],  # pformatectIn
                                      _Pointer[_struct.FORMATETC]],  # pformatetcOut
                                     _type.HRESULT]
    SetData: _Callable[[_Pointer[_struct.FORMATETC],  # pformatetc
                        _Pointer[_struct.STGMEDIUM],  # pmedium
                        _type.BOOL],  # fRelease
                       _type.HRESULT]
    EnumFormatEtc: _Callable[[_type.DWORD,  # dwDirection
                              _Pointer[IEnumFORMATETC]],  # ppenumFormatEtc
                             _type.HRESULT]
    DAdvise: _Callable[[_Pointer[_struct.FORMATETC],  # pformatetc
                        _type.DWORD,  # advf
                        IAdviseSink,  # pAdvSink
                        _Pointer[_type.DWORD]],  # pdwConnection
                       _type.HRESULT]
    DUnadvise: _Callable[[_type.DWORD],  # dwConnection
                         _type.HRESULT]
    EnumDAdvise: _Callable[[_Pointer[IEnumSTATDATA]],  # ppenumAdvise
                           _type.HRESULT]


class IDataAdviseHolder(_Unknwnbase.IUnknown):
    Advise: _Callable[[IDataObject,  # pDataObject
                       _Pointer[_struct.FORMATETC],  # pFetc
                       _type.DWORD,  # advf
                       IAdviseSink,  # pAdvise
                       _Pointer[_type.DWORD]],  # pdwConnection
                      _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD],  # dwConnection
                        _type.HRESULT]
    EnumAdvise: _Callable[[_Pointer[IEnumSTATDATA]],  # ppenumAdvise
                          _type.HRESULT]
    SendOnDataChange: _Callable[[IDataObject,  # pDataObject
                                 _type.DWORD,  # dwReserved
                                 _type.DWORD],  # advf
                                _type.HRESULT]


class IMessageFilter(_Unknwnbase.IUnknown):
    HandleInComingCall: _Callable[[_type.DWORD,  # dwCallType
                                   _type.HTASK,  # htaskCaller
                                   _type.DWORD,  # dwTickCount
                                   _Pointer[_struct.INTERFACEINFO]],  # lpInterfaceInfo
                                  _type.DWORD]
    RetryRejectedCall: _Callable[[_type.HTASK,  # htaskCallee
                                  _type.DWORD,  # dwTickCount
                                  _type.DWORD],  # dwRejectType
                                 _type.DWORD]
    MessagePending: _Callable[[_type.HTASK,  # htaskCallee
                               _type.DWORD,  # dwTickCount
                               _type.DWORD],  # dwPendingType
                              _type.DWORD]


class IClassActivator(_Unknwnbase.IUnknown):
    GetClassObject: _Callable[[_Pointer[_struct.IID],  # rclsid
                               _type.DWORD,  # dwClassContext
                               _type.LCID,  # locale
                               _Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppv
                              _type.HRESULT]


class IFillLockBytes(_Unknwnbase.IUnknown):
    FillAppend: _Callable[[_type.c_void_p,  # pv
                           _type.ULONG,  # cb
                           _Pointer[_type.ULONG]],  # pcbWritten
                          _type.HRESULT]
    FillAt: _Callable[[_union.ULARGE_INTEGER,  # ulOffset
                       _type.c_void_p,  # pv
                       _type.ULONG,  # cb
                       _Pointer[_type.ULONG]],  # pcbWritten
                      _type.HRESULT]
    SetFillSize: _Callable[[_union.ULARGE_INTEGER],  # ulSize
                           _type.HRESULT]
    Terminate: _Callable[[_type.BOOL],  # bCanceled
                         _type.HRESULT]


class IProgressNotify(_Unknwnbase.IUnknown):
    OnProgress: _Callable[[_type.DWORD,  # dwProgressCurrent
                           _type.DWORD,  # dwProgressMaximum
                           _type.BOOL,  # fAccurate
                           _type.BOOL],  # fOwner
                          _type.HRESULT]


class ILayoutStorage(_Unknwnbase.IUnknown):
    LayoutScript: _Callable[[_Pointer[_struct.StorageLayout],  # pStorageLayout
                             _type.DWORD,  # nEntries
                             _type.DWORD],  # glfInterleavedFlag
                            _type.HRESULT]
    BeginMonitor: _Callable[[],
                            _type.HRESULT]
    EndMonitor: _Callable[[],
                          _type.HRESULT]
    ReLayoutDocfile: _Callable[[_Pointer[_type.OLECHAR]],  # pwcsNewDfName
                               _type.HRESULT]
    ReLayoutDocfileOnILockBytes: _Callable[[ILockBytes],  # pILockBytes
                                           _type.HRESULT]


class IBlockingLock(_Unknwnbase.IUnknown):
    Lock: _Callable[[_type.DWORD],  # dwTimeout
                    _type.HRESULT]
    Unlock: _Callable[[],
                      _type.HRESULT]


class ITimeAndNoticeControl(_Unknwnbase.IUnknown):
    SuppressChanges: _Callable[[_type.DWORD,  # res1
                                _type.DWORD],  # res2
                               _type.HRESULT]


class IOplockStorage(_Unknwnbase.IUnknown):
    CreateStorageEx: _Callable[[_type.LPCWSTR,  # pwcsName
                                _type.DWORD,  # grfMode
                                _type.DWORD,  # stgfmt
                                _type.DWORD,  # grfAttrs
                                _Pointer[_struct.IID],  # riid
                                _type.c_void_p],  # ppstgOpen
                               _type.HRESULT]
    OpenStorageEx: _Callable[[_type.LPCWSTR,  # pwcsName
                              _type.DWORD,  # grfMode
                              _type.DWORD,  # stgfmt
                              _type.DWORD,  # grfAttrs
                              _Pointer[_struct.IID],  # riid
                              _type.c_void_p],  # ppstgOpen
                             _type.HRESULT]


class IDirectWriterLock(_Unknwnbase.IUnknown):
    WaitForWriteAccess: _Callable[[_type.DWORD],  # dwTimeout
                                  _type.HRESULT]
    ReleaseWriteAccess: _Callable[[],
                                  _type.HRESULT]
    HaveWriteAccess: _Callable[[],
                               _type.HRESULT]


class IUrlMon(_Unknwnbase.IUnknown):
    AsyncGetClassBits: _Callable[[_Pointer[_struct.IID],  # rclsid
                                  _type.LPCWSTR,  # pszTYPE
                                  _type.LPCWSTR,  # pszExt
                                  _type.DWORD,  # dwFileVersionMS
                                  _type.DWORD,  # dwFileVersionLS
                                  _type.LPCWSTR,  # pszCodeBase
                                  IBindCtx,  # pbc
                                  _type.DWORD,  # dwClassContext
                                  _Pointer[_struct.IID],  # riid
                                  _type.DWORD],  # flags
                                 _type.HRESULT]


class IForegroundTransfer(_Unknwnbase.IUnknown):
    AllowForegroundTransfer: _Callable[[_type.c_void_p],  # lpvReserved
                                       _type.HRESULT]


class IThumbnailExtractor(_Unknwnbase.IUnknown):
    ExtractThumbnail: _Callable[[IStorage,  # pStg
                                 _type.ULONG,  # ulLength
                                 _type.ULONG,  # ulHeight
                                 _Pointer[_type.ULONG],  # pulOutputLength
                                 _Pointer[_type.ULONG],  # pulOutputHeight
                                 _Pointer[_type.HBITMAP]],  # phOutputBitmap
                                _type.HRESULT]
    OnFileUpdated: _Callable[[IStorage],  # pStg
                             _type.HRESULT]


class IDummyHICONIncluder(_Unknwnbase.IUnknown):
    Dummy: _Callable[[_type.HICON,  # h1
                      _type.HDC],  # h2
                     _type.HRESULT]


class IProcessLock(_Unknwnbase.IUnknown):
    AddRefOnProcess: _Callable[[],
                               _type.ULONG]
    ReleaseRefOnProcess: _Callable[[],
                                   _type.ULONG]


class ISurrogateService(_Unknwnbase.IUnknown):
    Init: _Callable[[_Pointer[_struct.GUID],  # rguidProcessID
                     IProcessLock,  # pProcessLock
                     _Pointer[_type.BOOL]],  # pfApplicationAware
                    _type.HRESULT]
    ApplicationLaunch: _Callable[[_Pointer[_struct.GUID],  # rguidApplID
                                  _enum.ApplicationType],  # appType
                                 _type.HRESULT]
    ApplicationFree: _Callable[[_Pointer[_struct.GUID]],  # rguidApplID
                               _type.HRESULT]
    CatalogRefresh: _Callable[[_type.ULONG],  # ulReserved
                              _type.HRESULT]
    ProcessShutdown: _Callable[[_enum.ShutdownType],  # shutdownType
                               _type.HRESULT]


class IInitializeSpy(_Unknwnbase.IUnknown):
    PreInitialize: _Callable[[_type.DWORD,  # dwCoInit
                              _type.DWORD],  # dwCurThreadAptRefs
                             _type.HRESULT]
    PostInitialize: _Callable[[_type.HRESULT,  # hrCoInit
                               _type.DWORD,  # dwCoInit
                               _type.DWORD],  # dwNewThreadAptRefs
                              _type.HRESULT]
    PreUninitialize: _Callable[[_type.DWORD],  # dwCurThreadAptRefs
                               _type.HRESULT]
    PostUninitialize: _Callable[[_type.DWORD],  # dwNewThreadAptRefs
                                _type.HRESULT]


class IApartmentShutdown(_Unknwnbase.IUnknown):
    OnUninitialize: _Callable[[_type.UINT64],  # ui64ApartmentIdentifier
                              _type.c_void]

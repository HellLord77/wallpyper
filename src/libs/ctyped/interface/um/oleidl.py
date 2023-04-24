from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import objidl as _objidl
from . import objidlbase as _objidlbase
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IOleAdviseHolder(_Unknwnbase.IUnknown):
    Advise: _Callable[[_objidl.IAdviseSink,  # pAdvise
                       _Pointer[_type.DWORD]],  # pdwConnection
                      _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD],  # dwConnection
                        _type.HRESULT]
    EnumAdvise: _Callable[[_Pointer[_objidl.IEnumSTATDATA]],  # ppenumAdvise
                          _type.HRESULT]
    SendOnRename: _Callable[[_objidl.IMoniker],  # pmk
                            _type.HRESULT]
    SendOnSave: _Callable[[],
                          _type.HRESULT]
    SendOnClose: _Callable[[],
                           _type.HRESULT]


class IOleCache(_Unknwnbase.IUnknown):
    Cache: _Callable[[_Pointer[_struct.FORMATETC],  # pformatetc
                      _type.DWORD,  # advf
                      _Pointer[_type.DWORD]],  # pdwConnection
                     _type.HRESULT]
    Uncache: _Callable[[_type.DWORD],  # dwConnection
                       _type.HRESULT]
    EnumCache: _Callable[[_Pointer[_objidl.IEnumSTATDATA]],  # ppenumSTATDATA
                         _type.HRESULT]
    InitCache: _Callable[[_objidl.IDataObject],  # pDataObject
                         _type.HRESULT]
    SetData: _Callable[[_Pointer[_struct.FORMATETC],  # pformatetc
                        _Pointer[_struct.STGMEDIUM],  # pmedium
                        _type.BOOL],  # fRelease
                       _type.HRESULT]


class IOleCache2(IOleCache):
    UpdateCache: _Callable[[_objidl.IDataObject,  # pDataObject
                            _type.DWORD,  # grfUpdf
                            _type.LPVOID],  # pReserved
                           _type.HRESULT]
    DiscardCache: _Callable[[_type.DWORD],  # dwDiscardOptions
                            _type.HRESULT]


class IOleCacheControl(_Unknwnbase.IUnknown):
    OnRun: _Callable[[_objidl.IDataObject],  # pDataObject
                     _type.HRESULT]
    OnStop: _Callable[[],
                      _type.HRESULT]


class IParseDisplayName(_Unknwnbase.IUnknown):
    ParseDisplayName: _Callable[[_objidl.IBindCtx,  # pbc
                                 _type.LPOLESTR,  # pszDisplayName
                                 _Pointer[_type.ULONG],  # pchEaten
                                 _Pointer[_objidl.IMoniker]],  # ppmkOut
                                _type.HRESULT]


class IOleContainer(IParseDisplayName):
    EnumObjects: _Callable[[_type.DWORD,  # grfFlags
                            _Pointer[_objidlbase.IEnumUnknown]],  # ppenum
                           _type.HRESULT]
    LockContainer: _Callable[[_type.BOOL],  # fLock
                             _type.HRESULT]


class IOleClientSite(_Unknwnbase.IUnknown):
    SaveObject: _Callable[[],
                          _type.HRESULT]
    GetMoniker: _Callable[[_type.DWORD,  # dwAssign
                           _type.DWORD,  # dwWhichMoniker
                           _Pointer[_objidl.IMoniker]],  # ppmk
                          _type.HRESULT]
    GetContainer: _Callable[[_Pointer[IOleContainer]],  # ppContainer
                            _type.HRESULT]
    ShowObject: _Callable[[],
                          _type.HRESULT]
    OnShowWindow: _Callable[[_type.BOOL],  # fShow
                            _type.HRESULT]
    RequestNewObjectLayout: _Callable[[],
                                      _type.HRESULT]


class IOleObject(_Unknwnbase.IUnknown):
    SetClientSite: _Callable[[IOleClientSite],  # pClientSite
                             _type.HRESULT]
    GetClientSite: _Callable[[_Pointer[IOleClientSite]],  # ppClientSite
                             _type.HRESULT]
    SetHostNames: _Callable[[_type.LPCOLESTR,  # szContainerApp
                             _type.LPCOLESTR],  # szContainerObj
                            _type.HRESULT]
    Close: _Callable[[_type.DWORD],  # dwSaveOption
                     _type.HRESULT]
    SetMoniker: _Callable[[_type.DWORD,  # dwWhichMoniker
                           _objidl.IMoniker],  # pmk
                          _type.HRESULT]
    GetMoniker: _Callable[[_type.DWORD,  # dwAssign
                           _type.DWORD,  # dwWhichMoniker
                           _Pointer[_objidl.IMoniker]],  # ppmk
                          _type.HRESULT]
    InitFromData: _Callable[[_objidl.IDataObject,  # pDataObject
                             _type.BOOL,  # fCreation
                             _type.DWORD],  # dwReserved
                            _type.HRESULT]
    GetClipboardData: _Callable[[_type.DWORD,  # dwReserved
                                 _Pointer[_objidl.IDataObject]],  # ppDataObject
                                _type.HRESULT]
    DoVerb: _Callable[[_type.LONG,  # iVerb
                       _Pointer[_struct.MSG],  # lpmsg
                       IOleClientSite,  # pActiveSite
                       _type.LONG,  # lindex
                       _type.HWND,  # hwndParent
                       _Pointer[_struct.RECT]],  # lprcPosRect
                      _type.HRESULT]
    EnumVerbs: _Callable[[_Pointer[IEnumOLEVERB]],  # ppEnumOleVerb
                         _type.HRESULT]
    Update: _Callable[[],
                      _type.HRESULT]
    IsUpToDate: _Callable[[],
                          _type.HRESULT]
    GetUserClassID: _Callable[[_Pointer[_struct.CLSID]],  # pClsid
                              _type.HRESULT]
    GetUserType: _Callable[[_type.DWORD,  # dwFormOfType
                            _Pointer[_type.LPOLESTR]],  # pszUserType
                           _type.HRESULT]
    SetExtent: _Callable[[_type.DWORD,  # dwDrawAspect
                          _Pointer[_struct.SIZEL]],  # psizel
                         _type.HRESULT]
    GetExtent: _Callable[[_type.DWORD,  # dwDrawAspect
                          _Pointer[_struct.SIZEL]],  # psizel
                         _type.HRESULT]
    Advise: _Callable[[_objidl.IAdviseSink,  # pAdvSink
                       _Pointer[_type.DWORD]],  # pdwConnection
                      _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD],  # dwConnection
                        _type.HRESULT]
    EnumAdvise: _Callable[[_Pointer[_objidl.IEnumSTATDATA]],  # ppenumAdvise
                          _type.HRESULT]
    GetMiscStatus: _Callable[[_type.DWORD,  # dwAspect
                              _Pointer[_type.DWORD]],  # pdwStatus
                             _type.HRESULT]
    SetColorScheme: _Callable[[_Pointer[_struct.LOGPALETTE]],  # pLogpal
                              _type.HRESULT]


class IOleWindow(_Unknwnbase.IUnknown):
    GetWindow: _Callable[[_Pointer[_type.HWND]],  # phwnd
                         _type.HRESULT]
    ContextSensitiveHelp: _Callable[[_type.BOOL],  # fEnterMode
                                    _type.HRESULT]


class IOleLink(_Unknwnbase.IUnknown):
    SetUpdateOptions: _Callable[[_type.DWORD],  # dwUpdateOpt
                                _type.HRESULT]
    GetUpdateOptions: _Callable[[_Pointer[_type.DWORD]],  # pdwUpdateOpt
                                _type.HRESULT]
    SetSourceMoniker: _Callable[[_objidl.IMoniker,  # pmk
                                 _Pointer[_struct.IID]],  # rclsid
                                _type.HRESULT]
    GetSourceMoniker: _Callable[[_Pointer[_objidl.IMoniker]],  # ppmk
                                _type.HRESULT]
    SetSourceDisplayName: _Callable[[_type.LPCOLESTR],  # pszStatusText
                                    _type.HRESULT]
    GetSourceDisplayName: _Callable[[_Pointer[_type.LPOLESTR]],  # ppszDisplayName
                                    _type.HRESULT]
    BindToSource: _Callable[[_type.DWORD,  # bindflags
                             _objidl.IBindCtx],  # pbc
                            _type.HRESULT]
    BindIfRunning: _Callable[[],
                             _type.HRESULT]
    GetBoundSource: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppunk
                              _type.HRESULT]
    UnbindSource: _Callable[[],
                            _type.HRESULT]
    Update: _Callable[[_objidl.IBindCtx],  # pbc
                      _type.HRESULT]


class IOleItemContainer(IOleContainer):
    GetObjectA: _Callable[[_type.LPOLESTR,  # pszItem
                           _type.DWORD,  # dwSpeedNeeded
                           _objidl.IBindCtx,  # pbc
                           _Pointer[_struct.IID],  # riid
                           _type.c_void_p],  # ppvObject
                          _type.HRESULT]
    GetObjectStorage: _Callable[[_type.LPOLESTR,  # pszItem
                                 _objidl.IBindCtx,  # pbc
                                 _Pointer[_struct.IID],  # riid
                                 _type.c_void_p],  # ppvStorage
                                _type.HRESULT]
    IsRunning: _Callable[[_type.LPOLESTR],  # pszItem
                         _type.HRESULT]


class IOleInPlaceUIWindow(IOleWindow):
    GetBorder: _Callable[[_Pointer[_struct.RECT]],  # lprectBorder
                         _type.HRESULT]
    RequestBorderSpace: _Callable[[_Pointer[_struct.RECT]],  # pborderwidths
                                  _type.HRESULT]
    SetBorderSpace: _Callable[[_Pointer[_struct.RECT]],  # pborderwidths
                              _type.HRESULT]
    SetActiveObject: _Callable[[IOleInPlaceActiveObject,  # pActiveObject
                                _type.LPCOLESTR],  # pszObjName
                               _type.HRESULT]


class IOleInPlaceActiveObject(IOleWindow):
    TranslateAcceleratorA: _Callable[[_Pointer[_struct.MSG]],  # lpmsg
                                     _type.HRESULT]
    OnFrameWindowActivate: _Callable[[_type.BOOL],  # fActivate
                                     _type.HRESULT]
    OnDocWindowActivate: _Callable[[_type.BOOL],  # fActivate
                                   _type.HRESULT]
    ResizeBorder: _Callable[[_Pointer[_struct.RECT],  # prcBorder
                             IOleInPlaceUIWindow,  # pUIWindow
                             _type.BOOL],  # fFrameWindow
                            _type.HRESULT]
    EnableModeless: _Callable[[_type.BOOL],  # fEnable
                              _type.HRESULT]


class IOleInPlaceFrame(IOleInPlaceUIWindow):
    InsertMenus: _Callable[[_type.HMENU,  # hmenuShared
                            _Pointer[_struct.OLEMENUGROUPWIDTHS]],  # lpMenuWidths
                           _type.HRESULT]
    SetMenu: _Callable[[_type.HMENU,  # hmenuShared
                        _type.HOLEMENU,  # holemenu
                        _type.HWND],  # hwndActiveObject
                       _type.HRESULT]
    RemoveMenus: _Callable[[_type.HMENU],  # hmenuShared
                           _type.HRESULT]
    SetStatusText: _Callable[[_type.LPCOLESTR],  # pszStatusText
                             _type.HRESULT]
    EnableModeless: _Callable[[_type.BOOL],  # fEnable
                              _type.HRESULT]
    TranslateAcceleratorA: _Callable[[_Pointer[_struct.MSG],  # lpmsg
                                      _type.WORD],  # wID
                                     _type.HRESULT]


class IOleInPlaceObject(IOleWindow):
    InPlaceDeactivate: _Callable[[],
                                 _type.HRESULT]
    UIDeactivate: _Callable[[],
                            _type.HRESULT]
    SetObjectRects: _Callable[[_Pointer[_struct.RECT],  # lprcPosRect
                               _Pointer[_struct.RECT]],  # lprcClipRect
                              _type.HRESULT]
    ReactivateAndUndo: _Callable[[],
                                 _type.HRESULT]


class IOleInPlaceSite(IOleWindow):
    CanInPlaceActivate: _Callable[[],
                                  _type.HRESULT]
    OnInPlaceActivate: _Callable[[],
                                 _type.HRESULT]
    OnUIActivate: _Callable[[],
                            _type.HRESULT]
    GetWindowContext: _Callable[[_Pointer[IOleInPlaceFrame],  # ppFrame
                                 _Pointer[IOleInPlaceUIWindow],  # ppDoc
                                 _Pointer[_struct.RECT],  # lprcPosRect
                                 _Pointer[_struct.RECT],  # lprcClipRect
                                 _Pointer[_struct.OLEINPLACEFRAMEINFO]],  # lpFrameInfo
                                _type.HRESULT]
    Scroll: _Callable[[_struct.SIZE],  # scrollExtant
                      _type.HRESULT]
    OnUIDeactivate: _Callable[[_type.BOOL],  # fUndoable
                              _type.HRESULT]
    OnInPlaceDeactivate: _Callable[[],
                                   _type.HRESULT]
    DiscardUndoState: _Callable[[],
                                _type.HRESULT]
    DeactivateAndUndo: _Callable[[],
                                 _type.HRESULT]
    OnPosRectChange: _Callable[[_Pointer[_struct.RECT]],  # lprcPosRect
                               _type.HRESULT]


class IContinue(_Unknwnbase.IUnknown):
    FContinue: _Callable[[],
                         _type.HRESULT]


class IViewObject(_Unknwnbase.IUnknown):
    Draw: _Callable[[_type.DWORD,  # dwDrawAspect
                     _type.LONG,  # lindex
                     _type.c_void_p,  # pvAspect
                     _Pointer[_struct.DVTARGETDEVICE],  # ptd
                     _type.HDC,  # hdcTargetDev
                     _type.HDC,  # hdcDraw
                     _Pointer[_struct.RECTL],  # lprcBounds
                     _Pointer[_struct.RECTL],  # lprcWBounds
                     _type.IViewObject_Draw_pfnContinue,  # pfnContinue
                     _type.ULONG_PTR],  # dwContinue
                    _type.HRESULT]
    GetColorSet: _Callable[[_type.DWORD,  # dwDrawAspect
                            _type.LONG,  # lindex
                            _type.c_void_p,  # pvAspect
                            _Pointer[_struct.DVTARGETDEVICE],  # ptd
                            _type.HDC,  # hicTargetDev
                            _Pointer[_Pointer[_struct.LOGPALETTE]]],  # ppColorSet
                           _type.HRESULT]
    Freeze: _Callable[[_type.DWORD,  # dwDrawAspect
                       _type.LONG,  # lindex
                       _type.c_void_p,  # pvAspect
                       _Pointer[_type.DWORD]],  # pdwFreeze
                      _type.HRESULT]
    Unfreeze: _Callable[[_type.DWORD],  # dwFreeze
                        _type.HRESULT]
    SetAdvise: _Callable[[_type.DWORD,  # aspects
                          _type.DWORD,  # advf
                          _objidl.IAdviseSink],  # pAdvSink
                         _type.HRESULT]
    GetAdvise: _Callable[[_Pointer[_type.DWORD],  # pAspects
                          _Pointer[_type.DWORD],  # pAdvf
                          _Pointer[_objidl.IAdviseSink]],  # ppAdvSink
                         _type.HRESULT]


class IViewObject2(IViewObject):
    GetExtent: _Callable[[_type.DWORD,  # dwDrawAspect
                          _type.LONG,  # lindex
                          _Pointer[_struct.DVTARGETDEVICE],  # ptd
                          _Pointer[_struct.SIZEL]],  # lpsizel
                         _type.HRESULT]


class IDropSource(_Unknwnbase.IUnknown):
    QueryContinueDrag: _Callable[[_type.BOOL,  # fEscapePressed
                                  _type.DWORD],  # grfKeyState
                                 _type.HRESULT]
    GiveFeedback: _Callable[[_type.DWORD],  # dwEffect
                            _type.HRESULT]


class IDropTarget(_Unknwnbase.IUnknown):
    DragEnter: _Callable[[_objidl.IDataObject,  # pDataObj
                          _type.DWORD,  # grfKeyState
                          _struct.POINTL,  # pt
                          _Pointer[_type.DWORD]],  # pdwEffect
                         _type.HRESULT]
    DragOver: _Callable[[_type.DWORD,  # grfKeyState
                         _struct.POINTL,  # pt
                         _Pointer[_type.DWORD]],  # pdwEffect
                        _type.HRESULT]
    DragLeave: _Callable[[],
                         _type.HRESULT]
    Drop: _Callable[[_objidl.IDataObject,  # pDataObj
                     _type.DWORD,  # grfKeyState
                     _struct.POINTL,  # pt
                     _Pointer[_type.DWORD]],  # pdwEffect
                    _type.HRESULT]


class IDropSourceNotify(_Unknwnbase.IUnknown):
    DragEnterTarget: _Callable[[_type.HWND],  # hwndTarget
                               _type.HRESULT]
    DragLeaveTarget: _Callable[[],
                               _type.HRESULT]


class IEnterpriseDropTarget(_Unknwnbase.IUnknown):
    SetDropSourceEnterpriseId: _Callable[[_type.LPCWSTR],  # identity
                                         _type.HRESULT]
    IsEvaluatingEdpPolicy: _Callable[[_Pointer[_type.BOOL]],  # value
                                     _type.HRESULT]


class IEnumOLEVERB(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_struct.OLEVERB],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumOLEVERB]],  # ppenum
                     _type.HRESULT]

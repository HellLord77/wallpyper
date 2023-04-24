from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import oaidl as _oaidl
from . import objidl as _objidl
from . import objidlbase as _objidlbase
from . import oleidl as _oleidl
from ... import struct as _struct
from ... import type as _type
from ... import union as _union
from ..._utils import _Pointer


class IEnumConnections(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # cConnections
                     _Pointer[_struct.CONNECTDATA],  # rgcd
                     _Pointer[_type.ULONG]],  # pcFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # cConnections
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumConnections]],  # ppEnum
                     _type.HRESULT]


class IConnectionPoint(_Unknwnbase.IUnknown):
    GetConnectionInterface: _Callable[[_Pointer[_struct.IID]],  # pIID
                                      _type.HRESULT]
    GetConnectionPointContainer: _Callable[[_Pointer[IConnectionPointContainer]],  # ppCPC
                                           _type.HRESULT]
    Advise: _Callable[[_Unknwnbase.IUnknown,  # pUnkSink
                       _Pointer[_type.DWORD]],  # pdwCookie
                      _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD],  # dwCookie
                        _type.HRESULT]
    EnumConnections: _Callable[[_Pointer[IEnumConnections]],  # ppEnum
                               _type.HRESULT]


class IEnumConnectionPoints(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # cConnections
                     _Pointer[IConnectionPoint],  # ppCP
                     _Pointer[_type.ULONG]],  # pcFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # cConnections
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumConnectionPoints]],  # ppEnum
                     _type.HRESULT]


class IConnectionPointContainer(_Unknwnbase.IUnknown):
    EnumConnectionPoints: _Callable[[_Pointer[IEnumConnectionPoints]],  # ppEnum
                                    _type.HRESULT]
    FindConnectionPoint: _Callable[[_Pointer[_struct.IID],  # riid
                                    _Pointer[IConnectionPoint]],  # ppCP
                                   _type.HRESULT]


class IClassFactory2(_Unknwnbase.IClassFactory):
    GetLicInfo: _Callable[[_Pointer[_struct.LICINFO]],  # pLicInfo
                          _type.HRESULT]
    RequestLicKey: _Callable[[_type.DWORD,  # dwReserved
                              _Pointer[_type.BSTR]],  # pBstrKey
                             _type.HRESULT]
    CreateInstanceLic: _Callable[[_Unknwnbase.IUnknown,  # pUnkOuter
                                  _Unknwnbase.IUnknown,  # pUnkReserved
                                  _Pointer[_struct.IID],  # riid
                                  _type.BSTR,  # bstrKey
                                  _Pointer[_type.PVOID]],  # ppvObj
                                 _type.HRESULT]


class IProvideClassInfo(_Unknwnbase.IUnknown):
    GetClassInfo: _Callable[[_Pointer[_oaidl.ITypeInfo]],  # ppTI
                            _type.HRESULT]


class IProvideClassInfo2(IProvideClassInfo):
    GetGUID: _Callable[[_type.DWORD,  # dwGuidKind
                        _Pointer[_struct.GUID]],  # pGUID
                       _type.HRESULT]


class IProvideMultipleClassInfo(IProvideClassInfo2):
    GetMultiTypeInfoCount: _Callable[[_Pointer[_type.ULONG]],  # pcti
                                     _type.HRESULT]
    GetInfoOfIndex: _Callable[[_type.ULONG,  # iti
                               _type.DWORD,  # dwFlags
                               _Pointer[_oaidl.ITypeInfo],  # pptiCoClass
                               _Pointer[_type.DWORD],  # pdwTIFlags
                               _Pointer[_type.ULONG],  # pcdispidReserved
                               _Pointer[_struct.IID],  # piidPrimary
                               _Pointer[_struct.IID]],  # piidSource
                              _type.HRESULT]


class IOleControl(_Unknwnbase.IUnknown):
    GetControlInfo: _Callable[[_Pointer[_struct.CONTROLINFO]],  # pCI
                              _type.HRESULT]
    OnMnemonic: _Callable[[_Pointer[_struct.MSG]],  # pMsg
                          _type.HRESULT]
    OnAmbientPropertyChange: _Callable[[_type.DISPID],  # dispID
                                       _type.HRESULT]
    FreezeEvents: _Callable[[_type.BOOL],  # bFreeze
                            _type.HRESULT]


class IOleControlSite(_Unknwnbase.IUnknown):
    OnControlInfoChanged: _Callable[[],
                                    _type.HRESULT]
    LockInPlaceActive: _Callable[[_type.BOOL],  # fLock
                                 _type.HRESULT]
    GetExtendedControl: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppDisp
                                  _type.HRESULT]
    TransformCoords: _Callable[[_Pointer[_struct.POINTL],  # pPtlHimetric
                                _Pointer[_struct.POINTF],  # pPtfContainer
                                _type.DWORD],  # dwFlags
                               _type.HRESULT]
    TranslateAccelerator: _Callable[[_Pointer[_struct.MSG],  # pMsg
                                     _type.DWORD],  # grfModifiers
                                    _type.HRESULT]
    OnFocus: _Callable[[_type.BOOL],  # fGotFocus
                       _type.HRESULT]
    ShowPropertyFrame: _Callable[[],
                                 _type.HRESULT]


class IPropertyPage(_Unknwnbase.IUnknown):
    SetPageSite: _Callable[[IPropertyPageSite],  # pPageSite
                           _type.HRESULT]
    Activate: _Callable[[_type.HWND,  # hWndParent
                         _Pointer[_struct.RECT],  # pRect
                         _type.BOOL],  # bModal
                        _type.HRESULT]
    Deactivate: _Callable[[],
                          _type.HRESULT]
    GetPageInfo: _Callable[[_Pointer[_struct.PROPPAGEINFO]],  # pPageInfo
                           _type.HRESULT]
    SetObjects: _Callable[[_type.ULONG,  # cObjects
                           _Pointer[_Unknwnbase.IUnknown]],  # ppUnk
                          _type.HRESULT]
    Show: _Callable[[_type.UINT],  # nCmdShow
                    _type.HRESULT]
    Move: _Callable[[_Pointer[_struct.RECT]],  # pRect
                    _type.HRESULT]
    IsPageDirty: _Callable[[],
                           _type.HRESULT]
    Apply: _Callable[[],
                     _type.HRESULT]
    Help: _Callable[[_type.LPCOLESTR],  # pszHelpDir
                    _type.HRESULT]
    TranslateAccelerator: _Callable[[_Pointer[_struct.MSG]],  # pMsg
                                    _type.HRESULT]


class IPropertyPage2(IPropertyPage):
    EditProperty: _Callable[[_type.DISPID],  # dispID
                            _type.HRESULT]


class IPropertyPageSite(_Unknwnbase.IUnknown):
    OnStatusChange: _Callable[[_type.DWORD],  # dwFlags
                              _type.HRESULT]
    GetLocaleID: _Callable[[_Pointer[_type.LCID]],  # pLocaleID
                           _type.HRESULT]
    GetPageContainer: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppUnk
                                _type.HRESULT]
    TranslateAccelerator: _Callable[[_Pointer[_struct.MSG]],  # pMsg
                                    _type.HRESULT]


class IPropertyNotifySink(_Unknwnbase.IUnknown):
    OnChanged: _Callable[[_type.DISPID],  # dispID
                         _type.HRESULT]
    OnRequestEdit: _Callable[[_type.DISPID],  # dispID
                             _type.HRESULT]


class ISpecifyPropertyPages(_Unknwnbase.IUnknown):
    GetPages: _Callable[[_Pointer[_struct.CAUUID]],  # pPages
                        _type.HRESULT]


class IPersistMemory(_objidl.IPersist):
    IsDirty: _Callable[[],
                       _type.HRESULT]
    Load: _Callable[[_type.LPVOID,  # pMem
                     _type.ULONG],  # cbSize
                    _type.HRESULT]
    Save: _Callable[[_type.LPVOID,  # pMem
                     _type.BOOL,  # fClearDirty
                     _type.ULONG],  # cbSize
                    _type.HRESULT]
    GetSizeMax: _Callable[[_Pointer[_type.ULONG]],  # pCbSize
                          _type.HRESULT]
    InitNew: _Callable[[],
                       _type.HRESULT]


class IPersistStreamInit(_objidl.IPersist):
    IsDirty: _Callable[[],
                       _type.HRESULT]
    Load: _Callable[[_objidlbase.IStream],  # pStm
                    _type.HRESULT]
    Save: _Callable[[_objidlbase.IStream,  # pStm
                     _type.BOOL],  # fClearDirty
                    _type.HRESULT]
    GetSizeMax: _Callable[[_Pointer[_union.ULARGE_INTEGER]],  # pCbSize
                          _type.HRESULT]
    InitNew: _Callable[[],
                       _type.HRESULT]


class IPersistPropertyBag(_objidl.IPersist):
    InitNew: _Callable[[],
                       _type.HRESULT]
    Load: _Callable[[_oaidl.IPropertyBag,  # pPropBag
                     _oaidl.IErrorLog],  # pErrorLog
                    _type.HRESULT]
    Save: _Callable[[_oaidl.IPropertyBag,  # pPropBag
                     _type.BOOL,  # fClearDirty
                     _type.BOOL],  # fSaveAllProperties
                    _type.HRESULT]


class ISimpleFrameSite(_Unknwnbase.IUnknown):
    PreMessageFilter: _Callable[[_type.HWND,  # hWnd
                                 _type.UINT,  # msg
                                 _type.WPARAM,  # wp
                                 _type.LPARAM,  # lp
                                 _Pointer[_type.LRESULT],  # plResult
                                 _Pointer[_type.DWORD]],  # pdwCookie
                                _type.HRESULT]
    PostMessageFilter: _Callable[[_type.HWND,  # hWnd
                                  _type.UINT,  # msg
                                  _type.WPARAM,  # wp
                                  _type.LPARAM,  # lp
                                  _Pointer[_type.LRESULT],  # plResult
                                  _type.DWORD],  # dwCookie
                                 _type.HRESULT]


class IFont(_Unknwnbase.IUnknown):
    get_Name: _Callable[[_Pointer[_type.BSTR]],  # pName
                        _type.HRESULT]
    put_Name: _Callable[[_type.BSTR],  # name
                        _type.HRESULT]
    get_Size: _Callable[[_Pointer[_union.CY]],  # pSize
                        _type.HRESULT]
    put_Size: _Callable[[_union.CY],  # size
                        _type.HRESULT]
    get_Bold: _Callable[[_Pointer[_type.BOOL]],  # pBold
                        _type.HRESULT]
    put_Bold: _Callable[[_type.BOOL],  # bold
                        _type.HRESULT]
    get_Italic: _Callable[[_Pointer[_type.BOOL]],  # pItalic
                          _type.HRESULT]
    put_Italic: _Callable[[_type.BOOL],  # italic
                          _type.HRESULT]
    get_Underline: _Callable[[_Pointer[_type.BOOL]],  # pUnderline
                             _type.HRESULT]
    put_Underline: _Callable[[_type.BOOL],  # underline
                             _type.HRESULT]
    get_Strikethrough: _Callable[[_Pointer[_type.BOOL]],  # pStrikethrough
                                 _type.HRESULT]
    put_Strikethrough: _Callable[[_type.BOOL],  # strikethrough
                                 _type.HRESULT]
    get_Weight: _Callable[[_Pointer[_type.SHORT]],  # pWeight
                          _type.HRESULT]
    put_Weight: _Callable[[_type.SHORT],  # weight
                          _type.HRESULT]
    get_Charset: _Callable[[_Pointer[_type.SHORT]],  # pCharset
                           _type.HRESULT]
    put_Charset: _Callable[[_type.SHORT],  # charset
                           _type.HRESULT]
    get_hFont: _Callable[[_Pointer[_type.HFONT]],  # phFont
                         _type.HRESULT]
    Clone: _Callable[[_Pointer[IFont]],  # ppFont
                     _type.HRESULT]
    IsEqual: _Callable[[IFont],  # pFontOther
                       _type.HRESULT]
    SetRatio: _Callable[[_type.LONG,  # cyLogical
                         _type.LONG],  # cyHimetric
                        _type.HRESULT]
    QueryTextMetrics: _Callable[[_Pointer[_struct.TEXTMETRICOLE]],  # pTM
                                _type.HRESULT]
    AddRefHfont: _Callable[[_type.HFONT],  # hFont
                           _type.HRESULT]
    ReleaseHfont: _Callable[[_type.HFONT],  # hFont
                            _type.HRESULT]
    SetHdc: _Callable[[_type.HDC],  # hDC
                      _type.HRESULT]


class IPicture(_Unknwnbase.IUnknown):
    get_Handle: _Callable[[_Pointer[_type.OLE_HANDLE]],  # pHandle
                          _type.HRESULT]
    get_hPal: _Callable[[_Pointer[_type.OLE_HANDLE]],  # phPal
                        _type.HRESULT]
    get_Type: _Callable[[_Pointer[_type.SHORT]],  # pType
                        _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.OLE_XSIZE_HIMETRIC]],  # pWidth
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.OLE_YSIZE_HIMETRIC]],  # pHeight
                          _type.HRESULT]
    Render: _Callable[[_type.HDC,  # hDC
                       _type.LONG,  # x
                       _type.LONG,  # y
                       _type.LONG,  # cx
                       _type.LONG,  # cy
                       _type.OLE_XPOS_HIMETRIC,  # xSrc
                       _type.OLE_YPOS_HIMETRIC,  # ySrc
                       _type.OLE_XSIZE_HIMETRIC,  # cxSrc
                       _type.OLE_YSIZE_HIMETRIC,  # cySrc
                       _Pointer[_struct.RECT]],  # pRcWBounds
                      _type.HRESULT]
    set_hPal: _Callable[[_type.OLE_HANDLE],  # hPal
                        _type.HRESULT]
    get_CurDC: _Callable[[_Pointer[_type.HDC]],  # phDC
                         _type.HRESULT]
    SelectPicture: _Callable[[_type.HDC,  # hDCIn
                              _Pointer[_type.HDC],  # phDCOut
                              _Pointer[_type.OLE_HANDLE]],  # phBmpOut
                             _type.HRESULT]
    get_KeepOriginalFormat: _Callable[[_Pointer[_type.BOOL]],  # pKeep
                                      _type.HRESULT]
    put_KeepOriginalFormat: _Callable[[_type.BOOL],  # keep
                                      _type.HRESULT]
    PictureChanged: _Callable[[],
                              _type.HRESULT]
    SaveAsFile: _Callable[[_objidlbase.IStream,  # pStream
                           _type.BOOL,  # fSaveMemCopy
                           _Pointer[_type.LONG]],  # pCbSize
                          _type.HRESULT]
    get_Attributes: _Callable[[_Pointer[_type.DWORD]],  # pDwAttr
                              _type.HRESULT]


class IPicture2(_Unknwnbase.IUnknown):
    get_Handle: _Callable[[_Pointer[_type.HHANDLE]],  # pHandle
                          _type.HRESULT]
    get_hPal: _Callable[[_Pointer[_type.HHANDLE]],  # phPal
                        _type.HRESULT]
    get_Type: _Callable[[_Pointer[_type.SHORT]],  # pType
                        _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.OLE_XSIZE_HIMETRIC]],  # pWidth
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.OLE_YSIZE_HIMETRIC]],  # pHeight
                          _type.HRESULT]
    Render: _Callable[[_type.HDC,  # hDC
                       _type.LONG,  # x
                       _type.LONG,  # y
                       _type.LONG,  # cx
                       _type.LONG,  # cy
                       _type.OLE_XPOS_HIMETRIC,  # xSrc
                       _type.OLE_YPOS_HIMETRIC,  # ySrc
                       _type.OLE_XSIZE_HIMETRIC,  # cxSrc
                       _type.OLE_YSIZE_HIMETRIC,  # cySrc
                       _Pointer[_struct.RECT]],  # pRcWBounds
                      _type.HRESULT]
    set_hPal: _Callable[[_type.HHANDLE],  # hPal
                        _type.HRESULT]
    get_CurDC: _Callable[[_Pointer[_type.HDC]],  # phDC
                         _type.HRESULT]
    SelectPicture: _Callable[[_type.HDC,  # hDCIn
                              _Pointer[_type.HDC],  # phDCOut
                              _Pointer[_type.HHANDLE]],  # phBmpOut
                             _type.HRESULT]
    get_KeepOriginalFormat: _Callable[[_Pointer[_type.BOOL]],  # pKeep
                                      _type.HRESULT]
    put_KeepOriginalFormat: _Callable[[_type.BOOL],  # keep
                                      _type.HRESULT]
    PictureChanged: _Callable[[],
                              _type.HRESULT]
    SaveAsFile: _Callable[[_objidlbase.IStream,  # pStream
                           _type.BOOL,  # fSaveMemCopy
                           _Pointer[_type.LONG]],  # pCbSize
                          _type.HRESULT]
    get_Attributes: _Callable[[_Pointer[_type.DWORD]],  # pDwAttr
                              _type.HRESULT]


class IFontEventsDisp(_oaidl.IDispatch):
    pass


class IFontDisp(_oaidl.IDispatch):
    pass


class IPictureDisp(_oaidl.IDispatch):
    pass


class IOleInPlaceObjectWindowless(_oleidl.IOleInPlaceObject):
    OnWindowMessage: _Callable[[_type.UINT,  # msg
                                _type.WPARAM,  # wParam
                                _type.LPARAM,  # lParam
                                _Pointer[_type.LRESULT]],  # plResult
                               _type.HRESULT]
    GetDropTarget: _Callable[[_Pointer[_oleidl.IDropTarget]],  # ppDropTarget
                             _type.HRESULT]


class IOleInPlaceSiteEx(_oleidl.IOleInPlaceSite):
    OnInPlaceActivateEx: _Callable[[_Pointer[_type.BOOL],  # pfNoRedraw
                                    _type.DWORD],  # dwFlags
                                   _type.HRESULT]
    OnInPlaceDeactivateEx: _Callable[[_type.BOOL],  # fNoRedraw
                                     _type.HRESULT]
    RequestUIActivate: _Callable[[],
                                 _type.HRESULT]


class IOleInPlaceSiteWindowless(IOleInPlaceSiteEx):
    CanWindowlessActivate: _Callable[[],
                                     _type.HRESULT]
    GetCapture: _Callable[[],
                          _type.HRESULT]
    SetCapture: _Callable[[_type.BOOL],  # fCapture
                          _type.HRESULT]
    GetFocus: _Callable[[],
                        _type.HRESULT]
    SetFocus: _Callable[[_type.BOOL],  # fFocus
                        _type.HRESULT]
    GetDC: _Callable[[_Pointer[_struct.RECT],  # pRect
                      _type.DWORD,  # grfFlags
                      _Pointer[_type.HDC]],  # phDC
                     _type.HRESULT]
    ReleaseDC: _Callable[[_type.HDC],  # hDC
                         _type.HRESULT]
    InvalidateRect: _Callable[[_Pointer[_struct.RECT],  # pRect
                               _type.BOOL],  # fErase
                              _type.HRESULT]
    InvalidateRgn: _Callable[[_type.HRGN,  # hRGN
                              _type.BOOL],  # fErase
                             _type.HRESULT]
    ScrollRect: _Callable[[_type.INT,  # dx
                           _type.INT,  # dy
                           _Pointer[_struct.RECT],  # pRectScroll
                           _Pointer[_struct.RECT]],  # pRectClip
                          _type.HRESULT]
    AdjustRect: _Callable[[_Pointer[_struct.RECT]],  # prc
                          _type.HRESULT]
    OnDefWindowMessage: _Callable[[_type.UINT,  # msg
                                   _type.WPARAM,  # wParam
                                   _type.LPARAM,  # lParam
                                   _Pointer[_type.LRESULT]],  # plResult
                                  _type.HRESULT]


class IViewObjectEx(_oleidl.IViewObject2):
    GetRect: _Callable[[_type.DWORD,  # dwAspect
                        _Pointer[_struct.RECTL]],  # pRect
                       _type.HRESULT]
    GetViewStatus: _Callable[[_Pointer[_type.DWORD]],  # pdwStatus
                             _type.HRESULT]
    QueryHitPoint: _Callable[[_type.DWORD,  # dwAspect
                              _Pointer[_struct.RECT],  # pRectBounds
                              _struct.POINT,  # ptlLoc
                              _type.LONG,  # lCloseHint
                              _Pointer[_type.DWORD]],  # pHitResult
                             _type.HRESULT]
    QueryHitRect: _Callable[[_type.DWORD,  # dwAspect
                             _Pointer[_struct.RECT],  # pRectBounds
                             _Pointer[_struct.RECT],  # pRectLoc
                             _type.LONG,  # lCloseHint
                             _Pointer[_type.DWORD]],  # pHitResult
                            _type.HRESULT]
    GetNaturalExtent: _Callable[[_type.DWORD,  # dwAspect
                                 _type.LONG,  # lindex
                                 _Pointer[_struct.DVTARGETDEVICE],  # ptd
                                 _type.HDC,  # hicTargetDev
                                 _Pointer[_struct.DVEXTENTINFO],  # pExtentInfo
                                 _Pointer[_struct.SIZEL]],  # pSizel
                                _type.HRESULT]


class IOleUndoUnit(_Unknwnbase.IUnknown):
    Do: _Callable[[IOleUndoManager],  # pUndoManager
                  _type.HRESULT]
    GetDescription: _Callable[[_Pointer[_type.BSTR]],  # pBstr
                              _type.HRESULT]
    GetUnitType: _Callable[[_Pointer[_struct.CLSID],  # pClsid
                            _Pointer[_type.LONG]],  # plID
                           _type.HRESULT]
    OnNextAdd: _Callable[[],
                         _type.HRESULT]


class IOleParentUndoUnit(IOleUndoUnit):
    Open: _Callable[[IOleParentUndoUnit],  # pPUU
                    _type.HRESULT]
    Close: _Callable[[IOleParentUndoUnit,  # pPUU
                      _type.BOOL],  # fCommit
                     _type.HRESULT]
    Add: _Callable[[IOleUndoUnit],  # pUU
                   _type.HRESULT]
    FindUnit: _Callable[[IOleUndoUnit],  # pUU
                        _type.HRESULT]
    GetParentState: _Callable[[_Pointer[_type.DWORD]],  # pdwState
                              _type.HRESULT]


class IEnumOleUndoUnits(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # cElt
                     _Pointer[IOleUndoUnit],  # rgElt
                     _Pointer[_type.ULONG]],  # pcEltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # cElt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumOleUndoUnits]],  # ppEnum
                     _type.HRESULT]


class IOleUndoManager(_Unknwnbase.IUnknown):
    Open: _Callable[[IOleParentUndoUnit],  # pPUU
                    _type.HRESULT]
    Close: _Callable[[IOleParentUndoUnit,  # pPUU
                      _type.BOOL],  # fCommit
                     _type.HRESULT]
    Add: _Callable[[IOleUndoUnit],  # pUU
                   _type.HRESULT]
    GetOpenParentState: _Callable[[_Pointer[_type.DWORD]],  # pdwState
                                  _type.HRESULT]
    DiscardFrom: _Callable[[IOleUndoUnit],  # pUU
                           _type.HRESULT]
    UndoTo: _Callable[[IOleUndoUnit],  # pUU
                      _type.HRESULT]
    RedoTo: _Callable[[IOleUndoUnit],  # pUU
                      _type.HRESULT]
    EnumUndoable: _Callable[[_Pointer[IEnumOleUndoUnits]],  # ppEnum
                            _type.HRESULT]
    EnumRedoable: _Callable[[_Pointer[IEnumOleUndoUnits]],  # ppEnum
                            _type.HRESULT]
    GetLastUndoDescription: _Callable[[_Pointer[_type.BSTR]],  # pBstr
                                      _type.HRESULT]
    GetLastRedoDescription: _Callable[[_Pointer[_type.BSTR]],  # pBstr
                                      _type.HRESULT]
    Enable: _Callable[[_type.BOOL],  # fEnable
                      _type.HRESULT]


class IPointerInactive(_Unknwnbase.IUnknown):
    GetActivationPolicy: _Callable[[_Pointer[_type.DWORD]],  # pdwPolicy
                                   _type.HRESULT]
    OnInactiveMouseMove: _Callable[[_Pointer[_struct.RECT],  # pRectBounds
                                    _type.LONG,  # x
                                    _type.LONG,  # y
                                    _type.DWORD],  # grfKeyState
                                   _type.HRESULT]
    OnInactiveSetCursor: _Callable[[_Pointer[_struct.RECT],  # pRectBounds
                                    _type.LONG,  # x
                                    _type.LONG,  # y
                                    _type.DWORD,  # dwMouseMsg
                                    _type.BOOL],  # fSetAlways
                                   _type.HRESULT]


class IObjectWithSite(_Unknwnbase.IUnknown):
    SetSite: _Callable[[_Unknwnbase.IUnknown],  # pUnkSite
                       _type.HRESULT]
    GetSite: _Callable[[_Pointer[_struct.IID],  # riid
                        _type.c_void_p],  # ppvSite
                       _type.HRESULT]


class IPerPropertyBrowsing(_Unknwnbase.IUnknown):
    GetDisplayString: _Callable[[_type.DISPID,  # dispID
                                 _Pointer[_type.BSTR]],  # pBstr
                                _type.HRESULT]
    MapPropertyToPage: _Callable[[_type.DISPID,  # dispID
                                  _Pointer[_struct.CLSID]],  # pClsid
                                 _type.HRESULT]
    GetPredefinedStrings: _Callable[[_type.DISPID,  # dispID
                                     _Pointer[_struct.CALPOLESTR],  # pCaStringsOut
                                     _Pointer[_struct.CADWORD]],  # pCaCookiesOut
                                    _type.HRESULT]
    GetPredefinedValue: _Callable[[_type.DISPID,  # dispID
                                   _type.DWORD,  # dwCookie
                                   _Pointer[_struct.VARIANT]],  # pVarOut
                                  _type.HRESULT]


class IPropertyBag2(_Unknwnbase.IUnknown):
    Read: _Callable[[_type.ULONG,  # cProperties
                     _Pointer[_struct.PROPBAG2],  # pPropBag
                     _oaidl.IErrorLog,  # pErrLog
                     _Pointer[_struct.VARIANT],  # pvarValue
                     _Pointer[_type.HRESULT]],  # phrError
                    _type.HRESULT]
    Write: _Callable[[_type.ULONG,  # cProperties
                      _Pointer[_struct.PROPBAG2],  # pPropBag
                      _Pointer[_struct.VARIANT]],  # pvarValue
                     _type.HRESULT]
    CountProperties: _Callable[[_Pointer[_type.ULONG]],  # pcProperties
                               _type.HRESULT]
    GetPropertyInfo: _Callable[[_type.ULONG,  # iProperty
                                _type.ULONG,  # cProperties
                                _Pointer[_struct.PROPBAG2],  # pPropBag
                                _Pointer[_type.ULONG]],  # pcProperties
                               _type.HRESULT]
    LoadObject: _Callable[[_type.LPCOLESTR,  # pstrName
                           _type.DWORD,  # dwHint
                           _Unknwnbase.IUnknown,  # pUnkObject
                           _oaidl.IErrorLog],  # pErrLog
                          _type.HRESULT]


class IPersistPropertyBag2(_objidl.IPersist):
    InitNew: _Callable[[],
                       _type.HRESULT]
    Load: _Callable[[IPropertyBag2,  # pPropBag
                     _oaidl.IErrorLog],  # pErrLog
                    _type.HRESULT]
    Save: _Callable[[IPropertyBag2,  # pPropBag
                     _type.BOOL,  # fClearDirty
                     _type.BOOL],  # fSaveAllProperties
                    _type.HRESULT]
    IsDirty: _Callable[[],
                       _type.HRESULT]


class IAdviseSinkEx(_objidl.IAdviseSink):
    OnViewStatusChange: _Callable[[_type.DWORD],  # dwViewStatus
                                  _type.c_void]


class IQuickActivate(_Unknwnbase.IUnknown):
    QuickActivate: _Callable[[_Pointer[_struct.QACONTAINER],  # pQaContainer
                              _Pointer[_struct.QACONTROL]],  # pQaControl
                             _type.HRESULT]
    SetContentExtent: _Callable[[_Pointer[_struct.SIZEL]],  # pSizel
                                _type.HRESULT]
    GetContentExtent: _Callable[[_Pointer[_struct.SIZEL]],  # pSizel
                                _type.HRESULT]

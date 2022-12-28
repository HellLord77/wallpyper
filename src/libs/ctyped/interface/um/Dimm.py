from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IEnumRegisterWordA(_Unknwnbase.IUnknown):
    Clone: _Callable[[_Pointer[IEnumRegisterWordA]],  # ppEnum
                     _type.HRESULT]
    Next: _Callable[[_type.ULONG,  # ulCount
                     _Pointer[_struct.REGISTERWORDA],  # rgRegisterWord
                     _Pointer[_type.ULONG]],  # pcFetched
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # ulCount
                    _type.HRESULT]


class IEnumRegisterWordW(_Unknwnbase.IUnknown):
    Clone: _Callable[[_Pointer[IEnumRegisterWordW]],  # ppEnum
                     _type.HRESULT]
    Next: _Callable[[_type.ULONG,  # ulCount
                     _Pointer[_struct.REGISTERWORDW],  # rgRegisterWord
                     _Pointer[_type.ULONG]],  # pcFetched
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # ulCount
                    _type.HRESULT]


class IEnumInputContext(_Unknwnbase.IUnknown):
    Clone: _Callable[[_Pointer[IEnumInputContext]],  # ppEnum
                     _type.HRESULT]
    Next: _Callable[[_type.ULONG,  # ulCount
                     _Pointer[_type.HIMC],  # rgInputContext
                     _Pointer[_type.ULONG]],  # pcFetched
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # ulCount
                    _type.HRESULT]


class IActiveIMMRegistrar(_Unknwnbase.IUnknown):
    RegisterIME: _Callable[[_Pointer[_struct.IID],  # rclsid
                            _type.LANGID,  # lgid
                            _type.LPCWSTR,  # pszIconFile
                            _type.LPCWSTR],  # pszDesc
                           _type.HRESULT]
    UnregisterIME: _Callable[[_Pointer[_struct.IID]],  # rclsid
                             _type.HRESULT]


class IActiveIMMMessagePumpOwner(_Unknwnbase.IUnknown):
    Start: _Callable[[],
                     _type.HRESULT]
    End: _Callable[[],
                   _type.HRESULT]
    OnTranslateMessage: _Callable[[_Pointer[_struct.MSG]],  # pMsg
                                  _type.HRESULT]
    Pause: _Callable[[_Pointer[_type.DWORD]],  # pdwCookie
                     _type.HRESULT]
    Resume: _Callable[[_type.DWORD],  # dwCookie
                      _type.HRESULT]


class IActiveIMMApp(_Unknwnbase.IUnknown):
    AssociateContext: _Callable[[_type.HWND,  # hWnd
                                 _type.HIMC,  # hIME
                                 _Pointer[_type.HIMC]],  # phPrev
                                _type.HRESULT]
    ConfigureIMEA: _Callable[[_type.HKL,  # hKL
                              _type.HWND,  # hWnd
                              _type.DWORD,  # dwMode
                              _Pointer[_struct.REGISTERWORDA]],  # pData
                             _type.HRESULT]
    ConfigureIMEW: _Callable[[_type.HKL,  # hKL
                              _type.HWND,  # hWnd
                              _type.DWORD,  # dwMode
                              _Pointer[_struct.REGISTERWORDW]],  # pData
                             _type.HRESULT]
    CreateContext: _Callable[[_Pointer[_type.HIMC]],  # phIMC
                             _type.HRESULT]
    DestroyContext: _Callable[[_type.HIMC],  # hIME
                              _type.HRESULT]
    EnumRegisterWordA: _Callable[[_type.HKL,  # hKL
                                  _type.LPSTR,  # szReading
                                  _type.DWORD,  # dwStyle
                                  _type.LPSTR,  # szRegister
                                  _type.LPVOID,  # pData
                                  _Pointer[IEnumRegisterWordA]],  # pEnum
                                 _type.HRESULT]
    EnumRegisterWordW: _Callable[[_type.HKL,  # hKL
                                  _type.LPWSTR,  # szReading
                                  _type.DWORD,  # dwStyle
                                  _type.LPWSTR,  # szRegister
                                  _type.LPVOID,  # pData
                                  _Pointer[IEnumRegisterWordW]],  # pEnum
                                 _type.HRESULT]
    EscapeA: _Callable[[_type.HKL,  # hKL
                        _type.HIMC,  # hIMC
                        _type.UINT,  # uEscape
                        _type.LPVOID,  # pData
                        _Pointer[_type.LRESULT]],  # plResult
                       _type.HRESULT]
    EscapeW: _Callable[[_type.HKL,  # hKL
                        _type.HIMC,  # hIMC
                        _type.UINT,  # uEscape
                        _type.LPVOID,  # pData
                        _Pointer[_type.LRESULT]],  # plResult
                       _type.HRESULT]
    GetCandidateListA: _Callable[[_type.HIMC,  # hIMC
                                  _type.DWORD,  # dwIndex
                                  _type.UINT,  # uBufLen
                                  _Pointer[_struct.CANDIDATELIST],  # pCandList
                                  _Pointer[_type.UINT]],  # puCopied
                                 _type.HRESULT]
    GetCandidateListW: _Callable[[_type.HIMC,  # hIMC
                                  _type.DWORD,  # dwIndex
                                  _type.UINT,  # uBufLen
                                  _Pointer[_struct.CANDIDATELIST],  # pCandList
                                  _Pointer[_type.UINT]],  # puCopied
                                 _type.HRESULT]
    GetCandidateListCountA: _Callable[[_type.HIMC,  # hIMC
                                       _Pointer[_type.DWORD],  # pdwListSize
                                       _Pointer[_type.DWORD]],  # pdwBufLen
                                      _type.HRESULT]
    GetCandidateListCountW: _Callable[[_type.HIMC,  # hIMC
                                       _Pointer[_type.DWORD],  # pdwListSize
                                       _Pointer[_type.DWORD]],  # pdwBufLen
                                      _type.HRESULT]
    GetCandidateWindow: _Callable[[_type.HIMC,  # hIMC
                                   _type.DWORD,  # dwIndex
                                   _Pointer[_struct.CANDIDATEFORM]],  # pCandidate
                                  _type.HRESULT]
    GetCompositionFontA: _Callable[[_type.HIMC,  # hIMC
                                    _Pointer[_struct.LOGFONTA]],  # plf
                                   _type.HRESULT]
    GetCompositionFontW: _Callable[[_type.HIMC,  # hIMC
                                    _Pointer[_struct.LOGFONTW]],  # plf
                                   _type.HRESULT]
    GetCompositionStringA: _Callable[[_type.HIMC,  # hIMC
                                      _type.DWORD,  # dwIndex
                                      _type.DWORD,  # dwBufLen
                                      _Pointer[_type.LONG],  # plCopied
                                      _type.LPVOID],  # pBuf
                                     _type.HRESULT]
    GetCompositionStringW: _Callable[[_type.HIMC,  # hIMC
                                      _type.DWORD,  # dwIndex
                                      _type.DWORD,  # dwBufLen
                                      _Pointer[_type.LONG],  # plCopied
                                      _type.LPVOID],  # pBuf
                                     _type.HRESULT]
    GetCompositionWindow: _Callable[[_type.HIMC,  # hIMC
                                     _Pointer[_struct.COMPOSITIONFORM]],  # pCompForm
                                    _type.HRESULT]
    GetContext: _Callable[[_type.HWND,  # hWnd
                           _Pointer[_type.HIMC]],  # phIMC
                          _type.HRESULT]
    GetConversionListA: _Callable[[_type.HKL,  # hKL
                                   _type.HIMC,  # hIMC
                                   _type.LPSTR,  # pSrc
                                   _type.UINT,  # uBufLen
                                   _type.UINT,  # uFlag
                                   _Pointer[_struct.CANDIDATELIST],  # pDst
                                   _Pointer[_type.UINT]],  # puCopied
                                  _type.HRESULT]
    GetConversionListW: _Callable[[_type.HKL,  # hKL
                                   _type.HIMC,  # hIMC
                                   _type.LPWSTR,  # pSrc
                                   _type.UINT,  # uBufLen
                                   _type.UINT,  # uFlag
                                   _Pointer[_struct.CANDIDATELIST],  # pDst
                                   _Pointer[_type.UINT]],  # puCopied
                                  _type.HRESULT]
    GetConversionStatus: _Callable[[_type.HIMC,  # hIMC
                                    _Pointer[_type.DWORD],  # pfdwConversion
                                    _Pointer[_type.DWORD]],  # pfdwSentence
                                   _type.HRESULT]
    GetDefaultIMEWnd: _Callable[[_type.HWND,  # hWnd
                                 _Pointer[_type.HWND]],  # phDefWnd
                                _type.HRESULT]
    GetDescriptionA: _Callable[[_type.HKL,  # hKL
                                _type.UINT,  # uBufLen
                                _type.LPSTR,  # szDescription
                                _Pointer[_type.UINT]],  # puCopied
                               _type.HRESULT]
    GetDescriptionW: _Callable[[_type.HKL,  # hKL
                                _type.UINT,  # uBufLen
                                _type.LPWSTR,  # szDescription
                                _Pointer[_type.UINT]],  # puCopied
                               _type.HRESULT]
    GetGuideLineA: _Callable[[_type.HIMC,  # hIMC
                              _type.DWORD,  # dwIndex
                              _type.DWORD,  # dwBufLen
                              _type.LPSTR,  # pBuf
                              _Pointer[_type.DWORD]],  # pdwResult
                             _type.HRESULT]
    GetGuideLineW: _Callable[[_type.HIMC,  # hIMC
                              _type.DWORD,  # dwIndex
                              _type.DWORD,  # dwBufLen
                              _type.LPWSTR,  # pBuf
                              _Pointer[_type.DWORD]],  # pdwResult
                             _type.HRESULT]
    GetIMEFileNameA: _Callable[[_type.HKL,  # hKL
                                _type.UINT,  # uBufLen
                                _type.LPSTR,  # szFileName
                                _Pointer[_type.UINT]],  # puCopied
                               _type.HRESULT]
    GetIMEFileNameW: _Callable[[_type.HKL,  # hKL
                                _type.UINT,  # uBufLen
                                _type.LPWSTR,  # szFileName
                                _Pointer[_type.UINT]],  # puCopied
                               _type.HRESULT]
    GetOpenStatus: _Callable[[_type.HIMC],  # hIMC
                             _type.HRESULT]
    GetProperty: _Callable[[_type.HKL,  # hKL
                            _type.DWORD,  # fdwIndex
                            _Pointer[_type.DWORD]],  # pdwProperty
                           _type.HRESULT]
    GetRegisterWordStyleA: _Callable[[_type.HKL,  # hKL
                                      _type.UINT,  # nItem
                                      _Pointer[_struct.STYLEBUFA],  # pStyleBuf
                                      _Pointer[_type.UINT]],  # puCopied
                                     _type.HRESULT]
    GetRegisterWordStyleW: _Callable[[_type.HKL,  # hKL
                                      _type.UINT,  # nItem
                                      _Pointer[_struct.STYLEBUFW],  # pStyleBuf
                                      _Pointer[_type.UINT]],  # puCopied
                                     _type.HRESULT]
    GetStatusWindowPos: _Callable[[_type.HIMC,  # hIMC
                                   _Pointer[_struct.POINT]],  # pptPos
                                  _type.HRESULT]
    GetVirtualKey: _Callable[[_type.HWND,  # hWnd
                              _Pointer[_type.UINT]],  # puVirtualKey
                             _type.HRESULT]
    InstallIMEA: _Callable[[_type.LPSTR,  # szIMEFileName
                            _type.LPSTR,  # szLayoutText
                            _Pointer[_type.HKL]],  # phKL
                           _type.HRESULT]
    InstallIMEW: _Callable[[_type.LPWSTR,  # szIMEFileName
                            _type.LPWSTR,  # szLayoutText
                            _Pointer[_type.HKL]],  # phKL
                           _type.HRESULT]
    IsIME: _Callable[[_type.HKL],  # hKL
                     _type.HRESULT]
    IsUIMessageA: _Callable[[_type.HWND,  # hWndIME
                             _type.UINT,  # msg
                             _type.WPARAM,  # wParam
                             _type.LPARAM],  # lParam
                            _type.HRESULT]
    IsUIMessageW: _Callable[[_type.HWND,  # hWndIME
                             _type.UINT,  # msg
                             _type.WPARAM,  # wParam
                             _type.LPARAM],  # lParam
                            _type.HRESULT]
    NotifyIME: _Callable[[_type.HIMC,  # hIMC
                          _type.DWORD,  # dwAction
                          _type.DWORD,  # dwIndex
                          _type.DWORD],  # dwValue
                         _type.HRESULT]
    RegisterWordA: _Callable[[_type.HKL,  # hKL
                              _type.LPSTR,  # szReading
                              _type.DWORD,  # dwStyle
                              _type.LPSTR],  # szRegister
                             _type.HRESULT]
    RegisterWordW: _Callable[[_type.HKL,  # hKL
                              _type.LPWSTR,  # szReading
                              _type.DWORD,  # dwStyle
                              _type.LPWSTR],  # szRegister
                             _type.HRESULT]
    ReleaseContext: _Callable[[_type.HWND,  # hWnd
                               _type.HIMC],  # hIMC
                              _type.HRESULT]
    SetCandidateWindow: _Callable[[_type.HIMC,  # hIMC
                                   _Pointer[_struct.CANDIDATEFORM]],  # pCandidate
                                  _type.HRESULT]
    SetCompositionFontA: _Callable[[_type.HIMC,  # hIMC
                                    _Pointer[_struct.LOGFONTA]],  # plf
                                   _type.HRESULT]
    SetCompositionFontW: _Callable[[_type.HIMC,  # hIMC
                                    _Pointer[_struct.LOGFONTW]],  # plf
                                   _type.HRESULT]
    SetCompositionStringA: _Callable[[_type.HIMC,  # hIMC
                                      _type.DWORD,  # dwIndex
                                      _type.LPVOID,  # pComp
                                      _type.DWORD,  # dwCompLen
                                      _type.LPVOID,  # pRead
                                      _type.DWORD],  # dwReadLen
                                     _type.HRESULT]
    SetCompositionStringW: _Callable[[_type.HIMC,  # hIMC
                                      _type.DWORD,  # dwIndex
                                      _type.LPVOID,  # pComp
                                      _type.DWORD,  # dwCompLen
                                      _type.LPVOID,  # pRead
                                      _type.DWORD],  # dwReadLen
                                     _type.HRESULT]
    SetCompositionWindow: _Callable[[_type.HIMC,  # hIMC
                                     _Pointer[_struct.COMPOSITIONFORM]],  # pCompForm
                                    _type.HRESULT]
    SetConversionStatus: _Callable[[_type.HIMC,  # hIMC
                                    _type.DWORD,  # fdwConversion
                                    _type.DWORD],  # fdwSentence
                                   _type.HRESULT]
    SetOpenStatus: _Callable[[_type.HIMC,  # hIMC
                              _type.BOOL],  # fOpen
                             _type.HRESULT]
    SetStatusWindowPos: _Callable[[_type.HIMC,  # hIMC
                                   _Pointer[_struct.POINT]],  # pptPos
                                  _type.HRESULT]
    SimulateHotKey: _Callable[[_type.HWND,  # hWnd
                               _type.DWORD],  # dwHotKeyID
                              _type.HRESULT]
    UnregisterWordA: _Callable[[_type.HKL,  # hKL
                                _type.LPSTR,  # szReading
                                _type.DWORD,  # dwStyle
                                _type.LPSTR],  # szUnregister
                               _type.HRESULT]
    UnregisterWordW: _Callable[[_type.HKL,  # hKL
                                _type.LPWSTR,  # szReading
                                _type.DWORD,  # dwStyle
                                _type.LPWSTR],  # szUnregister
                               _type.HRESULT]
    Activate: _Callable[[_type.BOOL],  # fRestoreLayout
                        _type.HRESULT]
    Deactivate: _Callable[[],
                          _type.HRESULT]
    OnDefWindowProc: _Callable[[_type.HWND,  # hWnd
                                _type.UINT,  # Msg
                                _type.WPARAM,  # wParam
                                _type.LPARAM,  # lParam
                                _Pointer[_type.LRESULT]],  # plResult
                               _type.HRESULT]
    FilterClientWindows: _Callable[[_Pointer[_type.ATOM],  # aaClassList
                                    _type.UINT],  # uSize
                                   _type.HRESULT]
    GetCodePageA: _Callable[[_type.HKL,  # hKL
                             _Pointer[_type.UINT]],  # uCodePage
                            _type.HRESULT]
    GetLangId: _Callable[[_type.HKL,  # hKL
                          _Pointer[_type.LANGID]],  # plid
                         _type.HRESULT]
    AssociateContextEx: _Callable[[_type.HWND,  # hWnd
                                   _type.HIMC,  # hIMC
                                   _type.DWORD],  # dwFlags
                                  _type.HRESULT]
    DisableIME: _Callable[[_type.DWORD],  # idThread
                          _type.HRESULT]
    GetImeMenuItemsA: _Callable[[_type.HIMC,  # hIMC
                                 _type.DWORD,  # dwFlags
                                 _type.DWORD,  # dwType
                                 _Pointer[_struct.IMEMENUITEMINFOA],  # pImeParentMenu
                                 _Pointer[_struct.IMEMENUITEMINFOA],  # pImeMenu
                                 _type.DWORD,  # dwSize
                                 _Pointer[_type.DWORD]],  # pdwResult
                                _type.HRESULT]
    GetImeMenuItemsW: _Callable[[_type.HIMC,  # hIMC
                                 _type.DWORD,  # dwFlags
                                 _type.DWORD,  # dwType
                                 _Pointer[_struct.IMEMENUITEMINFOW],  # pImeParentMenu
                                 _Pointer[_struct.IMEMENUITEMINFOW],  # pImeMenu
                                 _type.DWORD,  # dwSize
                                 _Pointer[_type.DWORD]],  # pdwResult
                                _type.HRESULT]
    EnumInputContext: _Callable[[_type.DWORD,  # idThread
                                 _Pointer[IEnumInputContext]],  # ppEnum
                                _type.HRESULT]


class IActiveIMMIME(_Unknwnbase.IUnknown):
    AssociateContext: _Callable[[_type.HWND,  # hWnd
                                 _type.HIMC,  # hIME
                                 _Pointer[_type.HIMC]],  # phPrev
                                _type.HRESULT]
    ConfigureIMEA: _Callable[[_type.HKL,  # hKL
                              _type.HWND,  # hWnd
                              _type.DWORD,  # dwMode
                              _Pointer[_struct.REGISTERWORDA]],  # pData
                             _type.HRESULT]
    ConfigureIMEW: _Callable[[_type.HKL,  # hKL
                              _type.HWND,  # hWnd
                              _type.DWORD,  # dwMode
                              _Pointer[_struct.REGISTERWORDW]],  # pData
                             _type.HRESULT]
    CreateContext: _Callable[[_Pointer[_type.HIMC]],  # phIMC
                             _type.HRESULT]
    DestroyContext: _Callable[[_type.HIMC],  # hIME
                              _type.HRESULT]
    EnumRegisterWordA: _Callable[[_type.HKL,  # hKL
                                  _type.LPSTR,  # szReading
                                  _type.DWORD,  # dwStyle
                                  _type.LPSTR,  # szRegister
                                  _type.LPVOID,  # pData
                                  _Pointer[IEnumRegisterWordA]],  # pEnum
                                 _type.HRESULT]
    EnumRegisterWordW: _Callable[[_type.HKL,  # hKL
                                  _type.LPWSTR,  # szReading
                                  _type.DWORD,  # dwStyle
                                  _type.LPWSTR,  # szRegister
                                  _type.LPVOID,  # pData
                                  _Pointer[IEnumRegisterWordW]],  # pEnum
                                 _type.HRESULT]
    EscapeA: _Callable[[_type.HKL,  # hKL
                        _type.HIMC,  # hIMC
                        _type.UINT,  # uEscape
                        _type.LPVOID,  # pData
                        _Pointer[_type.LRESULT]],  # plResult
                       _type.HRESULT]
    EscapeW: _Callable[[_type.HKL,  # hKL
                        _type.HIMC,  # hIMC
                        _type.UINT,  # uEscape
                        _type.LPVOID,  # pData
                        _Pointer[_type.LRESULT]],  # plResult
                       _type.HRESULT]
    GetCandidateListA: _Callable[[_type.HIMC,  # hIMC
                                  _type.DWORD,  # dwIndex
                                  _type.UINT,  # uBufLen
                                  _Pointer[_struct.CANDIDATELIST],  # pCandList
                                  _Pointer[_type.UINT]],  # puCopied
                                 _type.HRESULT]
    GetCandidateListW: _Callable[[_type.HIMC,  # hIMC
                                  _type.DWORD,  # dwIndex
                                  _type.UINT,  # uBufLen
                                  _Pointer[_struct.CANDIDATELIST],  # pCandList
                                  _Pointer[_type.UINT]],  # puCopied
                                 _type.HRESULT]
    GetCandidateListCountA: _Callable[[_type.HIMC,  # hIMC
                                       _Pointer[_type.DWORD],  # pdwListSize
                                       _Pointer[_type.DWORD]],  # pdwBufLen
                                      _type.HRESULT]
    GetCandidateListCountW: _Callable[[_type.HIMC,  # hIMC
                                       _Pointer[_type.DWORD],  # pdwListSize
                                       _Pointer[_type.DWORD]],  # pdwBufLen
                                      _type.HRESULT]
    GetCandidateWindow: _Callable[[_type.HIMC,  # hIMC
                                   _type.DWORD,  # dwIndex
                                   _Pointer[_struct.CANDIDATEFORM]],  # pCandidate
                                  _type.HRESULT]
    GetCompositionFontA: _Callable[[_type.HIMC,  # hIMC
                                    _Pointer[_struct.LOGFONTA]],  # plf
                                   _type.HRESULT]
    GetCompositionFontW: _Callable[[_type.HIMC,  # hIMC
                                    _Pointer[_struct.LOGFONTW]],  # plf
                                   _type.HRESULT]
    GetCompositionStringA: _Callable[[_type.HIMC,  # hIMC
                                      _type.DWORD,  # dwIndex
                                      _type.DWORD,  # dwBufLen
                                      _Pointer[_type.LONG],  # plCopied
                                      _type.LPVOID],  # pBuf
                                     _type.HRESULT]
    GetCompositionStringW: _Callable[[_type.HIMC,  # hIMC
                                      _type.DWORD,  # dwIndex
                                      _type.DWORD,  # dwBufLen
                                      _Pointer[_type.LONG],  # plCopied
                                      _type.LPVOID],  # pBuf
                                     _type.HRESULT]
    GetCompositionWindow: _Callable[[_type.HIMC,  # hIMC
                                     _Pointer[_struct.COMPOSITIONFORM]],  # pCompForm
                                    _type.HRESULT]
    GetContext: _Callable[[_type.HWND,  # hWnd
                           _Pointer[_type.HIMC]],  # phIMC
                          _type.HRESULT]
    GetConversionListA: _Callable[[_type.HKL,  # hKL
                                   _type.HIMC,  # hIMC
                                   _type.LPSTR,  # pSrc
                                   _type.UINT,  # uBufLen
                                   _type.UINT,  # uFlag
                                   _Pointer[_struct.CANDIDATELIST],  # pDst
                                   _Pointer[_type.UINT]],  # puCopied
                                  _type.HRESULT]
    GetConversionListW: _Callable[[_type.HKL,  # hKL
                                   _type.HIMC,  # hIMC
                                   _type.LPWSTR,  # pSrc
                                   _type.UINT,  # uBufLen
                                   _type.UINT,  # uFlag
                                   _Pointer[_struct.CANDIDATELIST],  # pDst
                                   _Pointer[_type.UINT]],  # puCopied
                                  _type.HRESULT]
    GetConversionStatus: _Callable[[_type.HIMC,  # hIMC
                                    _Pointer[_type.DWORD],  # pfdwConversion
                                    _Pointer[_type.DWORD]],  # pfdwSentence
                                   _type.HRESULT]
    GetDefaultIMEWnd: _Callable[[_type.HWND,  # hWnd
                                 _Pointer[_type.HWND]],  # phDefWnd
                                _type.HRESULT]
    GetDescriptionA: _Callable[[_type.HKL,  # hKL
                                _type.UINT,  # uBufLen
                                _type.LPSTR,  # szDescription
                                _Pointer[_type.UINT]],  # puCopied
                               _type.HRESULT]
    GetDescriptionW: _Callable[[_type.HKL,  # hKL
                                _type.UINT,  # uBufLen
                                _type.LPWSTR,  # szDescription
                                _Pointer[_type.UINT]],  # puCopied
                               _type.HRESULT]
    GetGuideLineA: _Callable[[_type.HIMC,  # hIMC
                              _type.DWORD,  # dwIndex
                              _type.DWORD,  # dwBufLen
                              _type.LPSTR,  # pBuf
                              _Pointer[_type.DWORD]],  # pdwResult
                             _type.HRESULT]
    GetGuideLineW: _Callable[[_type.HIMC,  # hIMC
                              _type.DWORD,  # dwIndex
                              _type.DWORD,  # dwBufLen
                              _type.LPWSTR,  # pBuf
                              _Pointer[_type.DWORD]],  # pdwResult
                             _type.HRESULT]
    GetIMEFileNameA: _Callable[[_type.HKL,  # hKL
                                _type.UINT,  # uBufLen
                                _type.LPSTR,  # szFileName
                                _Pointer[_type.UINT]],  # puCopied
                               _type.HRESULT]
    GetIMEFileNameW: _Callable[[_type.HKL,  # hKL
                                _type.UINT,  # uBufLen
                                _type.LPWSTR,  # szFileName
                                _Pointer[_type.UINT]],  # puCopied
                               _type.HRESULT]
    GetOpenStatus: _Callable[[_type.HIMC],  # hIMC
                             _type.HRESULT]
    GetProperty: _Callable[[_type.HKL,  # hKL
                            _type.DWORD,  # fdwIndex
                            _Pointer[_type.DWORD]],  # pdwProperty
                           _type.HRESULT]
    GetRegisterWordStyleA: _Callable[[_type.HKL,  # hKL
                                      _type.UINT,  # nItem
                                      _Pointer[_struct.STYLEBUFA],  # pStyleBuf
                                      _Pointer[_type.UINT]],  # puCopied
                                     _type.HRESULT]
    GetRegisterWordStyleW: _Callable[[_type.HKL,  # hKL
                                      _type.UINT,  # nItem
                                      _Pointer[_struct.STYLEBUFW],  # pStyleBuf
                                      _Pointer[_type.UINT]],  # puCopied
                                     _type.HRESULT]
    GetStatusWindowPos: _Callable[[_type.HIMC,  # hIMC
                                   _Pointer[_struct.POINT]],  # pptPos
                                  _type.HRESULT]
    GetVirtualKey: _Callable[[_type.HWND,  # hWnd
                              _Pointer[_type.UINT]],  # puVirtualKey
                             _type.HRESULT]
    InstallIMEA: _Callable[[_type.LPSTR,  # szIMEFileName
                            _type.LPSTR,  # szLayoutText
                            _Pointer[_type.HKL]],  # phKL
                           _type.HRESULT]
    InstallIMEW: _Callable[[_type.LPWSTR,  # szIMEFileName
                            _type.LPWSTR,  # szLayoutText
                            _Pointer[_type.HKL]],  # phKL
                           _type.HRESULT]
    IsIME: _Callable[[_type.HKL],  # hKL
                     _type.HRESULT]
    IsUIMessageA: _Callable[[_type.HWND,  # hWndIME
                             _type.UINT,  # msg
                             _type.WPARAM,  # wParam
                             _type.LPARAM],  # lParam
                            _type.HRESULT]
    IsUIMessageW: _Callable[[_type.HWND,  # hWndIME
                             _type.UINT,  # msg
                             _type.WPARAM,  # wParam
                             _type.LPARAM],  # lParam
                            _type.HRESULT]
    NotifyIME: _Callable[[_type.HIMC,  # hIMC
                          _type.DWORD,  # dwAction
                          _type.DWORD,  # dwIndex
                          _type.DWORD],  # dwValue
                         _type.HRESULT]
    RegisterWordA: _Callable[[_type.HKL,  # hKL
                              _type.LPSTR,  # szReading
                              _type.DWORD,  # dwStyle
                              _type.LPSTR],  # szRegister
                             _type.HRESULT]
    RegisterWordW: _Callable[[_type.HKL,  # hKL
                              _type.LPWSTR,  # szReading
                              _type.DWORD,  # dwStyle
                              _type.LPWSTR],  # szRegister
                             _type.HRESULT]
    ReleaseContext: _Callable[[_type.HWND,  # hWnd
                               _type.HIMC],  # hIMC
                              _type.HRESULT]
    SetCandidateWindow: _Callable[[_type.HIMC,  # hIMC
                                   _Pointer[_struct.CANDIDATEFORM]],  # pCandidate
                                  _type.HRESULT]
    SetCompositionFontA: _Callable[[_type.HIMC,  # hIMC
                                    _Pointer[_struct.LOGFONTA]],  # plf
                                   _type.HRESULT]
    SetCompositionFontW: _Callable[[_type.HIMC,  # hIMC
                                    _Pointer[_struct.LOGFONTW]],  # plf
                                   _type.HRESULT]
    SetCompositionStringA: _Callable[[_type.HIMC,  # hIMC
                                      _type.DWORD,  # dwIndex
                                      _type.LPVOID,  # pComp
                                      _type.DWORD,  # dwCompLen
                                      _type.LPVOID,  # pRead
                                      _type.DWORD],  # dwReadLen
                                     _type.HRESULT]
    SetCompositionStringW: _Callable[[_type.HIMC,  # hIMC
                                      _type.DWORD,  # dwIndex
                                      _type.LPVOID,  # pComp
                                      _type.DWORD,  # dwCompLen
                                      _type.LPVOID,  # pRead
                                      _type.DWORD],  # dwReadLen
                                     _type.HRESULT]
    SetCompositionWindow: _Callable[[_type.HIMC,  # hIMC
                                     _Pointer[_struct.COMPOSITIONFORM]],  # pCompForm
                                    _type.HRESULT]
    SetConversionStatus: _Callable[[_type.HIMC,  # hIMC
                                    _type.DWORD,  # fdwConversion
                                    _type.DWORD],  # fdwSentence
                                   _type.HRESULT]
    SetOpenStatus: _Callable[[_type.HIMC,  # hIMC
                              _type.BOOL],  # fOpen
                             _type.HRESULT]
    SetStatusWindowPos: _Callable[[_type.HIMC,  # hIMC
                                   _Pointer[_struct.POINT]],  # pptPos
                                  _type.HRESULT]
    SimulateHotKey: _Callable[[_type.HWND,  # hWnd
                               _type.DWORD],  # dwHotKeyID
                              _type.HRESULT]
    UnregisterWordA: _Callable[[_type.HKL,  # hKL
                                _type.LPSTR,  # szReading
                                _type.DWORD,  # dwStyle
                                _type.LPSTR],  # szUnregister
                               _type.HRESULT]
    UnregisterWordW: _Callable[[_type.HKL,  # hKL
                                _type.LPWSTR,  # szReading
                                _type.DWORD,  # dwStyle
                                _type.LPWSTR],  # szUnregister
                               _type.HRESULT]
    GenerateMessage: _Callable[[_type.HIMC],  # hIMC
                               _type.HRESULT]
    LockIMC: _Callable[[_type.HIMC,  # hIMC
                        _Pointer[_Pointer[_struct.INPUTCONTEXT]]],  # ppIMC
                       _type.HRESULT]
    UnlockIMC: _Callable[[_type.HIMC],  # hIMC
                         _type.HRESULT]
    GetIMCLockCount: _Callable[[_type.HIMC,  # hIMC
                                _Pointer[_type.DWORD]],  # pdwLockCount
                               _type.HRESULT]
    CreateIMCC: _Callable[[_type.DWORD,  # dwSize
                           _Pointer[_type.HIMCC]],  # phIMCC
                          _type.HRESULT]
    DestroyIMCC: _Callable[[_type.HIMCC],  # hIMCC
                           _type.HRESULT]
    LockIMCC: _Callable[[_type.HIMCC,  # hIMCC
                         _type.c_void_p],  # ppv
                        _type.HRESULT]
    UnlockIMCC: _Callable[[_type.HIMCC],  # hIMCC
                          _type.HRESULT]
    ReSizeIMCC: _Callable[[_type.HIMCC,  # hIMCC
                           _type.DWORD,  # dwSize
                           _Pointer[_type.HIMCC]],  # phIMCC
                          _type.HRESULT]
    GetIMCCSize: _Callable[[_type.HIMCC,  # hIMCC
                            _Pointer[_type.DWORD]],  # pdwSize
                           _type.HRESULT]
    GetIMCCLockCount: _Callable[[_type.HIMCC,  # hIMCC
                                 _Pointer[_type.DWORD]],  # pdwLockCount
                                _type.HRESULT]
    GetHotKey: _Callable[[_type.DWORD,  # dwHotKeyID
                          _Pointer[_type.UINT],  # puModifiers
                          _Pointer[_type.UINT],  # puVKey
                          _Pointer[_type.HKL]],  # phKL
                         _type.HRESULT]
    SetHotKey: _Callable[[_type.DWORD,  # dwHotKeyID
                          _type.UINT,  # uModifiers
                          _type.UINT,  # uVKey
                          _type.HKL],  # hKL
                         _type.HRESULT]
    CreateSoftKeyboard: _Callable[[_type.UINT,  # uType
                                   _type.HWND,  # hOwner
                                   _type.c_int,  # x
                                   _type.c_int,  # y
                                   _Pointer[_type.HWND]],  # phSoftKbdWnd
                                  _type.HRESULT]
    DestroySoftKeyboard: _Callable[[_type.HWND],  # hSoftKbdWnd
                                   _type.HRESULT]
    ShowSoftKeyboard: _Callable[[_type.HWND,  # hSoftKbdWnd
                                 _type.c_int],  # nCmdShow
                                _type.HRESULT]
    GetCodePageA: _Callable[[_type.HKL,  # hKL
                             _Pointer[_type.UINT]],  # uCodePage
                            _type.HRESULT]
    GetLangId: _Callable[[_type.HKL,  # hKL
                          _Pointer[_type.LANGID]],  # plid
                         _type.HRESULT]
    KeybdEvent: _Callable[[_type.LANGID,  # lgidIME
                           _type.BYTE,  # bVk
                           _type.BYTE,  # bScan
                           _type.DWORD,  # dwFlags
                           _type.DWORD],  # dwExtraInfo
                          _type.HRESULT]
    LockModal: _Callable[[],
                         _type.HRESULT]
    UnlockModal: _Callable[[],
                           _type.HRESULT]
    AssociateContextEx: _Callable[[_type.HWND,  # hWnd
                                   _type.HIMC,  # hIMC
                                   _type.DWORD],  # dwFlags
                                  _type.HRESULT]
    DisableIME: _Callable[[_type.DWORD],  # idThread
                          _type.HRESULT]
    GetImeMenuItemsA: _Callable[[_type.HIMC,  # hIMC
                                 _type.DWORD,  # dwFlags
                                 _type.DWORD,  # dwType
                                 _Pointer[_struct.IMEMENUITEMINFOA],  # pImeParentMenu
                                 _Pointer[_struct.IMEMENUITEMINFOA],  # pImeMenu
                                 _type.DWORD,  # dwSize
                                 _Pointer[_type.DWORD]],  # pdwResult
                                _type.HRESULT]
    GetImeMenuItemsW: _Callable[[_type.HIMC,  # hIMC
                                 _type.DWORD,  # dwFlags
                                 _type.DWORD,  # dwType
                                 _Pointer[_struct.IMEMENUITEMINFOW],  # pImeParentMenu
                                 _Pointer[_struct.IMEMENUITEMINFOW],  # pImeMenu
                                 _type.DWORD,  # dwSize
                                 _Pointer[_type.DWORD]],  # pdwResult
                                _type.HRESULT]
    EnumInputContext: _Callable[[_type.DWORD,  # idThread
                                 _Pointer[IEnumInputContext]],  # ppEnum
                                _type.HRESULT]
    RequestMessageA: _Callable[[_type.HIMC,  # hIMC
                                _type.WPARAM,  # wParam
                                _type.LPARAM,  # lParam
                                _Pointer[_type.LRESULT]],  # plResult
                               _type.HRESULT]
    RequestMessageW: _Callable[[_type.HIMC,  # hIMC
                                _type.WPARAM,  # wParam
                                _type.LPARAM,  # lParam
                                _Pointer[_type.LRESULT]],  # plResult
                               _type.HRESULT]
    SendIMCA: _Callable[[_type.HWND,  # hWnd
                         _type.UINT,  # uMsg
                         _type.WPARAM,  # wParam
                         _type.LPARAM,  # lParam
                         _Pointer[_type.LRESULT]],  # plResult
                        _type.HRESULT]
    SendIMCW: _Callable[[_type.HWND,  # hWnd
                         _type.UINT,  # uMsg
                         _type.WPARAM,  # wParam
                         _type.LPARAM,  # lParam
                         _Pointer[_type.LRESULT]],  # plResult
                        _type.HRESULT]
    IsSleeping: _Callable[[],
                          _type.HRESULT]


class IActiveIME(_Unknwnbase.IUnknown):
    Inquire: _Callable[[_type.DWORD,  # dwSystemInfoFlags
                        _Pointer[_struct.IMEINFO],  # pIMEInfo
                        _type.LPWSTR,  # szWndClass
                        _Pointer[_type.DWORD]],  # pdwPrivate
                       _type.HRESULT]
    ConversionList: _Callable[[_type.HIMC,  # hIMC
                               _type.LPWSTR,  # szSource
                               _type.UINT,  # uFlag
                               _type.UINT,  # uBufLen
                               _Pointer[_struct.CANDIDATELIST],  # pDest
                               _Pointer[_type.UINT]],  # puCopied
                              _type.HRESULT]
    Configure: _Callable[[_type.HKL,  # hKL
                          _type.HWND,  # hWnd
                          _type.DWORD,  # dwMode
                          _Pointer[_struct.REGISTERWORDW]],  # pRegisterWord
                         _type.HRESULT]
    Destroy: _Callable[[_type.UINT],  # uReserved
                       _type.HRESULT]
    Escape: _Callable[[_type.HIMC,  # hIMC
                       _type.UINT,  # uEscape
                       _type.c_void_p,  # pData
                       _Pointer[_type.LRESULT]],  # plResult
                      _type.HRESULT]
    SetActiveContext: _Callable[[_type.HIMC,  # hIMC
                                 _type.BOOL],  # fFlag
                                _type.HRESULT]
    ProcessKey: _Callable[[_type.HIMC,  # hIMC
                           _type.UINT,  # uVirKey
                           _type.DWORD,  # lParam
                           _Pointer[_type.BYTE]],  # pbKeyState
                          _type.HRESULT]
    Notify: _Callable[[_type.HIMC,  # hIMC
                       _type.DWORD,  # dwAction
                       _type.DWORD,  # dwIndex
                       _type.DWORD],  # dwValue
                      _type.HRESULT]
    Select: _Callable[[_type.HIMC,  # hIMC
                       _type.BOOL],  # fSelect
                      _type.HRESULT]
    SetCompositionString: _Callable[[_type.HIMC,  # hIMC
                                     _type.DWORD,  # dwIndex
                                     _type.c_void_p,  # pComp
                                     _type.DWORD,  # dwCompLen
                                     _type.c_void_p,  # pRead
                                     _type.DWORD],  # dwReadLen
                                    _type.HRESULT]
    ToAsciiEx: _Callable[[_type.UINT,  # uVirKey
                          _type.UINT,  # uScanCode
                          _Pointer[_type.BYTE],  # pbKeyState
                          _type.UINT,  # fuState
                          _type.HIMC,  # hIMC
                          _Pointer[_type.DWORD],  # pdwTransBuf
                          _Pointer[_type.UINT]],  # puSize
                         _type.HRESULT]
    RegisterWord: _Callable[[_type.LPWSTR,  # szReading
                             _type.DWORD,  # dwStyle
                             _type.LPWSTR],  # szString
                            _type.HRESULT]
    UnregisterWord: _Callable[[_type.LPWSTR,  # szReading
                               _type.DWORD,  # dwStyle
                               _type.LPWSTR],  # szString
                              _type.HRESULT]
    GetRegisterWordStyle: _Callable[[_type.UINT,  # nItem
                                     _Pointer[_struct.STYLEBUFW],  # pStyleBuf
                                     _Pointer[_type.UINT]],  # puBufSize
                                    _type.HRESULT]
    EnumRegisterWord: _Callable[[_type.LPWSTR,  # szReading
                                 _type.DWORD,  # dwStyle
                                 _type.LPWSTR,  # szRegister
                                 _type.LPVOID,  # pData
                                 _Pointer[IEnumRegisterWordW]],  # ppEnum
                                _type.HRESULT]
    GetCodePageA: _Callable[[_Pointer[_type.UINT]],  # uCodePage
                            _type.HRESULT]
    GetLangId: _Callable[[_Pointer[_type.LANGID]],  # plid
                         _type.HRESULT]


class IActiveIME2(IActiveIME):
    Sleep: _Callable[[],
                     _type.HRESULT]
    Unsleep: _Callable[[_type.BOOL],  # fDead
                       _type.HRESULT]

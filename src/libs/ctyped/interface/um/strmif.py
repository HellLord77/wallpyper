from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import ddraw as _ddraw
from . import oaidl as _oaidl
from . import objidl as _objidl
from . import objidlbase as _objidlbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ICreateDevEnum(_Unknwnbase.IUnknown):
    CreateClassEnumerator: _Callable[[_Pointer[_struct.IID],  # clsidDeviceClass
                                      _Pointer[_objidl.IEnumMoniker],  # ppEnumMoniker
                                      _type.DWORD],  # dwFlags
                                     _type.HRESULT]


class IPin(_Unknwnbase.IUnknown):
    Connect: _Callable[[IPin,  # pReceivePin
                        _Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                       _type.HRESULT]
    ReceiveConnection: _Callable[[IPin,  # pConnector
                                  _Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                                 _type.HRESULT]
    Disconnect: _Callable[[],
                          _type.HRESULT]
    ConnectedTo: _Callable[[_Pointer[IPin]],  # pPin
                           _type.HRESULT]
    ConnectionMediaType: _Callable[[_Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                                   _type.HRESULT]
    QueryPinInfo: _Callable[[_Pointer[_struct.PIN_INFO]],  # pInfo
                            _type.HRESULT]
    QueryDirection: _Callable[[_Pointer[_enum.PIN_DIRECTION]],  # pPinDir
                              _type.HRESULT]
    QueryId: _Callable[[_Pointer[_type.LPWSTR]],  # Id
                       _type.HRESULT]
    QueryAccept: _Callable[[_Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                           _type.HRESULT]
    EnumMediaTypes: _Callable[[_Pointer[IEnumMediaTypes]],  # ppEnum
                              _type.HRESULT]
    QueryInternalConnections: _Callable[[_Pointer[IPin],  # apPin
                                         _Pointer[_type.ULONG]],  # nPin
                                        _type.HRESULT]
    EndOfStream: _Callable[[],
                           _type.HRESULT]
    BeginFlush: _Callable[[],
                          _type.HRESULT]
    EndFlush: _Callable[[],
                        _type.HRESULT]
    NewSegment: _Callable[[_type.REFERENCE_TIME,  # tStart
                           _type.REFERENCE_TIME,  # tStop
                           _type.c_double],  # dRate
                          _type.HRESULT]


class IEnumPins(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # cPins
                     _Pointer[IPin],  # ppPins
                     _Pointer[_type.ULONG]],  # pcFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # cPins
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumPins]],  # ppEnum
                     _type.HRESULT]


class IEnumMediaTypes(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # cMediaTypes
                     _Pointer[_Pointer[_struct.AM_MEDIA_TYPE]],  # ppMediaTypes
                     _Pointer[_type.ULONG]],  # pcFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # cMediaTypes
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumMediaTypes]],  # ppEnum
                     _type.HRESULT]


class IFilterGraph(_Unknwnbase.IUnknown):
    AddFilter: _Callable[[IBaseFilter,  # pFilter
                          _type.LPCWSTR],  # pName
                         _type.HRESULT]
    RemoveFilter: _Callable[[IBaseFilter],  # pFilter
                            _type.HRESULT]
    EnumFilters: _Callable[[_Pointer[IEnumFilters]],  # ppEnum
                           _type.HRESULT]
    FindFilterByName: _Callable[[_type.LPCWSTR,  # pName
                                 _Pointer[IBaseFilter]],  # ppFilter
                                _type.HRESULT]
    ConnectDirect: _Callable[[IPin,  # ppinOut
                              IPin,  # ppinIn
                              _Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                             _type.HRESULT]
    Reconnect: _Callable[[IPin],  # ppin
                         _type.HRESULT]
    Disconnect: _Callable[[IPin],  # ppin
                          _type.HRESULT]
    SetDefaultSyncSource: _Callable[[],
                                    _type.HRESULT]


class IEnumFilters(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # cFilters
                     _Pointer[IBaseFilter],  # ppFilter
                     _Pointer[_type.ULONG]],  # pcFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # cFilters
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumFilters]],  # ppEnum
                     _type.HRESULT]


class IMediaFilter(_objidl.IPersist):
    Stop: _Callable[[],
                    _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    Run: _Callable[[_type.REFERENCE_TIME],  # tStart
                   _type.HRESULT]
    GetState: _Callable[[_type.DWORD,  # dwMilliSecsTimeout
                         _Pointer[_enum.FILTER_STATE]],  # State
                        _type.HRESULT]
    SetSyncSource: _Callable[[IReferenceClock],  # pClock
                             _type.HRESULT]
    GetSyncSource: _Callable[[_Pointer[IReferenceClock]],  # pClock
                             _type.HRESULT]


class IBaseFilter(IMediaFilter):
    EnumPins: _Callable[[_Pointer[IEnumPins]],  # ppEnum
                        _type.HRESULT]
    FindPin: _Callable[[_type.LPCWSTR,  # Id
                        _Pointer[IPin]],  # ppPin
                       _type.HRESULT]
    QueryFilterInfo: _Callable[[_Pointer[_struct.FILTER_INFO]],  # pInfo
                               _type.HRESULT]
    JoinFilterGraph: _Callable[[IFilterGraph,  # pGraph
                                _type.LPCWSTR],  # pName
                               _type.HRESULT]
    QueryVendorInfo: _Callable[[_Pointer[_type.LPWSTR]],  # pVendorInfo
                               _type.HRESULT]


class IReferenceClock(_Unknwnbase.IUnknown):
    GetTime: _Callable[[_Pointer[_type.REFERENCE_TIME]],  # pTime
                       _type.HRESULT]
    AdviseTime: _Callable[[_type.REFERENCE_TIME,  # baseTime
                           _type.REFERENCE_TIME,  # streamTime
                           _type.HEVENT,  # hEvent
                           _Pointer[_type.DWORD_PTR]],  # pdwAdviseCookie
                          _type.HRESULT]
    AdvisePeriodic: _Callable[[_type.REFERENCE_TIME,  # startTime
                               _type.REFERENCE_TIME,  # periodTime
                               _type.HSEMAPHORE,  # hSemaphore
                               _Pointer[_type.DWORD_PTR]],  # pdwAdviseCookie
                              _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD_PTR],  # dwAdviseCookie
                        _type.HRESULT]


class IReferenceClockTimerControl(_Unknwnbase.IUnknown):
    SetDefaultTimerResolution: _Callable[[_type.REFERENCE_TIME],  # timerResolution
                                         _type.HRESULT]
    GetDefaultTimerResolution: _Callable[[_Pointer[_type.REFERENCE_TIME]],  # pTimerResolution
                                         _type.HRESULT]


class IReferenceClock2(IReferenceClock):
    pass


class IMediaSample(_Unknwnbase.IUnknown):
    GetPointer: _Callable[[_Pointer[_Pointer[_type.BYTE]]],  # ppBuffer
                          _type.HRESULT]
    GetSize: _Callable[[],
                       _type.c_long]
    GetTime: _Callable[[_Pointer[_type.REFERENCE_TIME],  # pTimeStart
                        _Pointer[_type.REFERENCE_TIME]],  # pTimeEnd
                       _type.HRESULT]
    SetTime: _Callable[[_Pointer[_type.REFERENCE_TIME],  # pTimeStart
                        _Pointer[_type.REFERENCE_TIME]],  # pTimeEnd
                       _type.HRESULT]
    IsSyncPoint: _Callable[[],
                           _type.HRESULT]
    SetSyncPoint: _Callable[[_type.BOOL],  # bIsSyncPoint
                            _type.HRESULT]
    IsPreroll: _Callable[[],
                         _type.HRESULT]
    SetPreroll: _Callable[[_type.BOOL],  # bIsPreroll
                          _type.HRESULT]
    GetActualDataLength: _Callable[[],
                                   _type.c_long]
    SetActualDataLength: _Callable[[_type.c_long],  # __MIDL__IMediaSample0000
                                   _type.HRESULT]
    GetMediaType: _Callable[[_Pointer[_Pointer[_struct.AM_MEDIA_TYPE]]],  # ppMediaType
                            _type.HRESULT]
    SetMediaType: _Callable[[_Pointer[_struct.AM_MEDIA_TYPE]],  # pMediaType
                            _type.HRESULT]
    IsDiscontinuity: _Callable[[],
                               _type.HRESULT]
    SetDiscontinuity: _Callable[[_type.BOOL],  # bDiscontinuity
                                _type.HRESULT]
    GetMediaTime: _Callable[[_Pointer[_type.LONGLONG],  # pTimeStart
                             _Pointer[_type.LONGLONG]],  # pTimeEnd
                            _type.HRESULT]
    SetMediaTime: _Callable[[_Pointer[_type.LONGLONG],  # pTimeStart
                             _Pointer[_type.LONGLONG]],  # pTimeEnd
                            _type.HRESULT]


class IMediaSample2(IMediaSample):
    GetProperties: _Callable[[_type.DWORD,  # cbProperties
                              _Pointer[_type.BYTE]],  # pbProperties
                             _type.HRESULT]
    SetProperties: _Callable[[_type.DWORD,  # cbProperties
                              _Pointer[_type.BYTE]],  # pbProperties
                             _type.HRESULT]


class IMediaSample2Config(_Unknwnbase.IUnknown):
    GetSurface: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppDirect3DSurface9
                          _type.HRESULT]


class IMemAllocator(_Unknwnbase.IUnknown):
    SetProperties: _Callable[[_Pointer[_struct.ALLOCATOR_PROPERTIES],  # pRequest
                              _Pointer[_struct.ALLOCATOR_PROPERTIES]],  # pActual
                             _type.HRESULT]
    GetProperties: _Callable[[_Pointer[_struct.ALLOCATOR_PROPERTIES]],  # pProps
                             _type.HRESULT]
    Commit: _Callable[[],
                      _type.HRESULT]
    Decommit: _Callable[[],
                        _type.HRESULT]
    GetBuffer: _Callable[[_Pointer[IMediaSample],  # ppBuffer
                          _Pointer[_type.REFERENCE_TIME],  # pStartTime
                          _Pointer[_type.REFERENCE_TIME],  # pEndTime
                          _type.DWORD],  # dwFlags
                         _type.HRESULT]
    ReleaseBuffer: _Callable[[IMediaSample],  # pBuffer
                             _type.HRESULT]


class IMemAllocatorCallbackTemp(IMemAllocator):
    SetNotify: _Callable[[IMemAllocatorNotifyCallbackTemp],  # pNotify
                         _type.HRESULT]
    GetFreeCount: _Callable[[_Pointer[_type.LONG]],  # plBuffersFree
                            _type.HRESULT]


class IMemAllocatorNotifyCallbackTemp(_Unknwnbase.IUnknown):
    NotifyRelease: _Callable[[],
                             _type.HRESULT]


class IMemInputPin(_Unknwnbase.IUnknown):
    GetAllocator: _Callable[[_Pointer[IMemAllocator]],  # ppAllocator
                            _type.HRESULT]
    NotifyAllocator: _Callable[[IMemAllocator,  # pAllocator
                                _type.BOOL],  # bReadOnly
                               _type.HRESULT]
    GetAllocatorRequirements: _Callable[[_Pointer[_struct.ALLOCATOR_PROPERTIES]],  # pProps
                                        _type.HRESULT]
    Receive: _Callable[[IMediaSample],  # pSample
                       _type.HRESULT]
    ReceiveMultiple: _Callable[[_Pointer[IMediaSample],  # pSamples
                                _type.c_long,  # nSamples
                                _Pointer[_type.c_long]],  # nSamplesProcessed
                               _type.HRESULT]
    ReceiveCanBlock: _Callable[[],
                               _type.HRESULT]


class IAMovieSetup(_Unknwnbase.IUnknown):
    Register: _Callable[[],
                        _type.HRESULT]
    Unregister: _Callable[[],
                          _type.HRESULT]


class IMediaSeeking(_Unknwnbase.IUnknown):
    GetCapabilities: _Callable[[_Pointer[_type.DWORD]],  # pCapabilities
                               _type.HRESULT]
    CheckCapabilities: _Callable[[_Pointer[_type.DWORD]],  # pCapabilities
                                 _type.HRESULT]
    IsFormatSupported: _Callable[[_Pointer[_struct.GUID]],  # pFormat
                                 _type.HRESULT]
    QueryPreferredFormat: _Callable[[_Pointer[_struct.GUID]],  # pFormat
                                    _type.HRESULT]
    GetTimeFormatW: _Callable[[_Pointer[_struct.GUID]],  # pFormat
                              _type.HRESULT]
    IsUsingTimeFormat: _Callable[[_Pointer[_struct.GUID]],  # pFormat
                                 _type.HRESULT]
    SetTimeFormat: _Callable[[_Pointer[_struct.GUID]],  # pFormat
                             _type.HRESULT]
    GetDuration: _Callable[[_Pointer[_type.LONGLONG]],  # pDuration
                           _type.HRESULT]
    GetStopPosition: _Callable[[_Pointer[_type.LONGLONG]],  # pStop
                               _type.HRESULT]
    GetCurrentPosition: _Callable[[_Pointer[_type.LONGLONG]],  # pCurrent
                                  _type.HRESULT]
    ConvertTimeFormat: _Callable[[_Pointer[_type.LONGLONG],  # pTarget
                                  _Pointer[_struct.GUID],  # pTargetFormat
                                  _type.LONGLONG,  # Source
                                  _Pointer[_struct.GUID]],  # pSourceFormat
                                 _type.HRESULT]
    SetPositions: _Callable[[_Pointer[_type.LONGLONG],  # pCurrent
                             _type.DWORD,  # dwCurrentFlags
                             _Pointer[_type.LONGLONG],  # pStop
                             _type.DWORD],  # dwStopFlags
                            _type.HRESULT]
    GetPositions: _Callable[[_Pointer[_type.LONGLONG],  # pCurrent
                             _Pointer[_type.LONGLONG]],  # pStop
                            _type.HRESULT]
    GetAvailable: _Callable[[_Pointer[_type.LONGLONG],  # pEarliest
                             _Pointer[_type.LONGLONG]],  # pLatest
                            _type.HRESULT]
    SetRate: _Callable[[_type.c_double],  # dRate
                       _type.HRESULT]
    GetRate: _Callable[[_Pointer[_type.c_double]],  # pdRate
                       _type.HRESULT]
    GetPreroll: _Callable[[_Pointer[_type.LONGLONG]],  # pllPreroll
                          _type.HRESULT]


class ICodecAPI(_Unknwnbase.IUnknown):
    IsSupported: _Callable[[_Pointer[_struct.GUID]],  # Api
                           _type.HRESULT]
    IsModifiable: _Callable[[_Pointer[_struct.GUID]],  # Api
                            _type.HRESULT]
    GetParameterRange: _Callable[[_Pointer[_struct.GUID],  # Api
                                  _Pointer[_struct.VARIANT],  # ValueMin
                                  _Pointer[_struct.VARIANT],  # ValueMax
                                  _Pointer[_struct.VARIANT]],  # SteppingDelta
                                 _type.HRESULT]
    GetParameterValues: _Callable[[_Pointer[_struct.GUID],  # Api
                                   _Pointer[_Pointer[_struct.VARIANT]],  # Values
                                   _Pointer[_type.ULONG]],  # ValuesCount
                                  _type.HRESULT]
    GetDefaultValue: _Callable[[_Pointer[_struct.GUID],  # Api
                                _Pointer[_struct.VARIANT]],  # Value
                               _type.HRESULT]
    GetValue: _Callable[[_Pointer[_struct.GUID],  # Api
                         _Pointer[_struct.VARIANT]],  # Value
                        _type.HRESULT]
    SetValue: _Callable[[_Pointer[_struct.GUID],  # Api
                         _Pointer[_struct.VARIANT]],  # Value
                        _type.HRESULT]
    RegisterForEvent: _Callable[[_Pointer[_struct.GUID],  # Api
                                 _type.LONG_PTR],  # userData
                                _type.HRESULT]
    UnregisterForEvent: _Callable[[_Pointer[_struct.GUID]],  # Api
                                  _type.HRESULT]
    SetAllDefaults: _Callable[[],
                              _type.HRESULT]
    SetValueWithNotify: _Callable[[_Pointer[_struct.GUID],  # Api
                                   _Pointer[_struct.VARIANT],  # Value
                                   _Pointer[_Pointer[_struct.GUID]],  # ChangedParam
                                   _Pointer[_type.ULONG]],  # ChangedParamCount
                                  _type.HRESULT]
    SetAllDefaultsWithNotify: _Callable[[_Pointer[_Pointer[_struct.GUID]],  # ChangedParam
                                         _Pointer[_type.ULONG]],  # ChangedParamCount
                                        _type.HRESULT]
    GetAllSettings: _Callable[[_objidlbase.IStream],  # __MIDL__ICodecAPI0000
                              _type.HRESULT]
    SetAllSettings: _Callable[[_objidlbase.IStream],  # __MIDL__ICodecAPI0001
                              _type.HRESULT]
    SetAllSettingsWithNotify: _Callable[[_objidlbase.IStream,  # __MIDL__ICodecAPI0002
                                         _Pointer[_Pointer[_struct.GUID]],  # ChangedParam
                                         _Pointer[_type.ULONG]],  # ChangedParamCount
                                        _type.HRESULT]


class IEnumRegFilters(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # cFilters
                     _Pointer[_Pointer[_struct.REGFILTER]],  # apRegFilter
                     _Pointer[_type.ULONG]],  # pcFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # cFilters
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumRegFilters]],  # ppEnum
                     _type.HRESULT]


class IFilterMapper(_Unknwnbase.IUnknown):
    RegisterFilter: _Callable[[_struct.CLSID,  # clsid
                               _type.LPCWSTR,  # Name
                               _type.DWORD],  # dwMerit
                              _type.HRESULT]
    RegisterFilterInstance: _Callable[[_struct.CLSID,  # clsid
                                       _type.LPCWSTR,  # Name
                                       _Pointer[_struct.CLSID]],  # MRId
                                      _type.HRESULT]
    RegisterPin: _Callable[[_struct.CLSID,  # Filter
                            _type.LPCWSTR,  # Name
                            _type.BOOL,  # bRendered
                            _type.BOOL,  # bOutput
                            _type.BOOL,  # bZero
                            _type.BOOL,  # bMany
                            _struct.CLSID,  # ConnectsToFilter
                            _type.LPCWSTR],  # ConnectsToPin
                           _type.HRESULT]
    RegisterPinType: _Callable[[_struct.CLSID,  # clsFilter
                                _type.LPCWSTR,  # strName
                                _struct.CLSID,  # clsMajorType
                                _struct.CLSID],  # clsSubType
                               _type.HRESULT]
    UnregisterFilter: _Callable[[_struct.CLSID],  # Filter
                                _type.HRESULT]
    UnregisterFilterInstance: _Callable[[_struct.CLSID],  # MRId
                                        _type.HRESULT]
    UnregisterPin: _Callable[[_struct.CLSID,  # Filter
                              _type.LPCWSTR],  # Name
                             _type.HRESULT]
    EnumMatchingFilters: _Callable[[_Pointer[IEnumRegFilters],  # ppEnum
                                    _type.DWORD,  # dwMerit
                                    _type.BOOL,  # bInputNeeded
                                    _struct.CLSID,  # clsInMaj
                                    _struct.CLSID,  # clsInSub
                                    _type.BOOL,  # bRender
                                    _type.BOOL,  # bOututNeeded
                                    _struct.CLSID,  # clsOutMaj
                                    _struct.CLSID],  # clsOutSub
                                   _type.HRESULT]


class IFilterMapper2(_Unknwnbase.IUnknown):
    CreateCategory: _Callable[[_Pointer[_struct.IID],  # clsidCategory
                               _type.DWORD,  # dwCategoryMerit
                               _type.LPCWSTR],  # Description
                              _type.HRESULT]
    UnregisterFilter: _Callable[[_Pointer[_struct.CLSID],  # pclsidCategory
                                 _type.LPCOLESTR,  # szInstance
                                 _Pointer[_struct.IID]],  # Filter
                                _type.HRESULT]
    RegisterFilter: _Callable[[_Pointer[_struct.IID],  # clsidFilter
                               _type.LPCWSTR,  # Name
                               _Pointer[_objidl.IMoniker],  # ppMoniker
                               _Pointer[_struct.CLSID],  # pclsidCategory
                               _type.LPCOLESTR,  # szInstance
                               _Pointer[_struct.REGFILTER2]],  # prf2
                              _type.HRESULT]
    EnumMatchingFilters: _Callable[[_Pointer[_objidl.IEnumMoniker],  # ppEnum
                                    _type.DWORD,  # dwFlags
                                    _type.BOOL,  # bExactMatch
                                    _type.DWORD,  # dwMerit
                                    _type.BOOL,  # bInputNeeded
                                    _type.DWORD,  # cInputTypes
                                    _Pointer[_struct.GUID],  # pInputTypes
                                    _Pointer[_struct.REGPINMEDIUM],  # pMedIn
                                    _Pointer[_struct.CLSID],  # pPinCategoryIn
                                    _type.BOOL,  # bRender
                                    _type.BOOL,  # bOutputNeeded
                                    _type.DWORD,  # cOutputTypes
                                    _Pointer[_struct.GUID],  # pOutputTypes
                                    _Pointer[_struct.REGPINMEDIUM],  # pMedOut
                                    _Pointer[_struct.CLSID]],  # pPinCategoryOut
                                   _type.HRESULT]


class IFilterMapper3(IFilterMapper2):
    GetICreateDevEnum: _Callable[[_Pointer[ICreateDevEnum]],  # ppEnum
                                 _type.HRESULT]


class IQualityControl(_Unknwnbase.IUnknown):
    Notify: _Callable[[IBaseFilter,  # pSelf
                       _struct.Quality],  # q
                      _type.HRESULT]
    SetSink: _Callable[[IQualityControl],  # piqc
                       _type.HRESULT]


class IOverlayNotify(_Unknwnbase.IUnknown):
    OnPaletteChange: _Callable[[_type.DWORD,  # dwColors
                                _Pointer[_struct.PALETTEENTRY]],  # pPalette
                               _type.HRESULT]
    OnClipChange: _Callable[[_Pointer[_struct.RECT],  # pSourceRect
                             _Pointer[_struct.RECT],  # pDestinationRect
                             _Pointer[_struct.RGNDATA]],  # pRgnData
                            _type.HRESULT]
    OnColorKeyChange: _Callable[[_Pointer[_struct.COLORKEY]],  # pColorKey
                                _type.HRESULT]
    OnPositionChange: _Callable[[_Pointer[_struct.RECT],  # pSourceRect
                                 _Pointer[_struct.RECT]],  # pDestinationRect
                                _type.HRESULT]


class IOverlayNotify2(IOverlayNotify):
    OnDisplayChange: _Callable[[_type.HMONITOR],  # hMonitor
                               _type.HRESULT]


class IOverlay(_Unknwnbase.IUnknown):
    GetPalette: _Callable[[_Pointer[_type.DWORD],  # pdwColors
                           _Pointer[_Pointer[_struct.PALETTEENTRY]]],  # ppPalette
                          _type.HRESULT]
    SetPalette: _Callable[[_type.DWORD,  # dwColors
                           _Pointer[_struct.PALETTEENTRY]],  # pPalette
                          _type.HRESULT]
    GetDefaultColorKey: _Callable[[_Pointer[_struct.COLORKEY]],  # pColorKey
                                  _type.HRESULT]
    GetColorKey: _Callable[[_Pointer[_struct.COLORKEY]],  # pColorKey
                           _type.HRESULT]
    SetColorKey: _Callable[[_Pointer[_struct.COLORKEY]],  # pColorKey
                           _type.HRESULT]
    GetWindowHandle: _Callable[[_Pointer[_type.HWND]],  # pHwnd
                               _type.HRESULT]
    GetClipList: _Callable[[_Pointer[_struct.RECT],  # pSourceRect
                            _Pointer[_struct.RECT],  # pDestinationRect
                            _Pointer[_Pointer[_struct.RGNDATA]]],  # ppRgnData
                           _type.HRESULT]
    GetVideoPosition: _Callable[[_Pointer[_struct.RECT],  # pSourceRect
                                 _Pointer[_struct.RECT]],  # pDestinationRect
                                _type.HRESULT]
    Advise: _Callable[[IOverlayNotify,  # pOverlayNotify
                       _type.DWORD],  # dwInterests
                      _type.HRESULT]
    Unadvise: _Callable[[],
                        _type.HRESULT]


class IMediaEventSink(_Unknwnbase.IUnknown):
    Notify: _Callable[[_type.c_long,  # EventCode
                       _type.LONG_PTR,  # EventParam1
                       _type.LONG_PTR],  # EventParam2
                      _type.HRESULT]


class IFileSourceFilter(_Unknwnbase.IUnknown):
    Load: _Callable[[_type.LPCOLESTR,  # pszFileName
                     _Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                    _type.HRESULT]
    GetCurFile: _Callable[[_Pointer[_type.LPOLESTR],  # ppszFileName
                           _Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                          _type.HRESULT]


class IFileSinkFilter(_Unknwnbase.IUnknown):
    SetFileName: _Callable[[_type.LPCOLESTR,  # pszFileName
                            _Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                           _type.HRESULT]
    GetCurFile: _Callable[[_Pointer[_type.LPOLESTR],  # ppszFileName
                           _Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                          _type.HRESULT]


class IFileSinkFilter2(IFileSinkFilter):
    SetMode: _Callable[[_type.DWORD],  # dwFlags
                       _type.HRESULT]
    GetMode: _Callable[[_Pointer[_type.DWORD]],  # pdwFlags
                       _type.HRESULT]


class IGraphBuilder(IFilterGraph):
    Connect: _Callable[[IPin,  # ppinOut
                        IPin],  # ppinIn
                       _type.HRESULT]
    Render: _Callable[[IPin],  # ppinOut
                      _type.HRESULT]
    RenderFile: _Callable[[_type.LPCWSTR,  # lpcwstrFile
                           _type.LPCWSTR],  # lpcwstrPlayList
                          _type.HRESULT]
    AddSourceFilter: _Callable[[_type.LPCWSTR,  # lpcwstrFileName
                                _type.LPCWSTR,  # lpcwstrFilterName
                                _Pointer[IBaseFilter]],  # ppFilter
                               _type.HRESULT]
    SetLogFile: _Callable[[_type.DWORD_PTR],  # hFile
                          _type.HRESULT]
    Abort: _Callable[[],
                     _type.HRESULT]
    ShouldOperationContinue: _Callable[[],
                                       _type.HRESULT]


class ICaptureGraphBuilder(_Unknwnbase.IUnknown):
    SetFiltergraph: _Callable[[IGraphBuilder],  # pfg
                              _type.HRESULT]
    GetFiltergraph: _Callable[[_Pointer[IGraphBuilder]],  # ppfg
                              _type.HRESULT]
    SetOutputFileName: _Callable[[_Pointer[_struct.GUID],  # pType
                                  _type.LPCOLESTR,  # lpstrFile
                                  _Pointer[IBaseFilter],  # ppf
                                  _Pointer[IFileSinkFilter]],  # ppSink
                                 _type.HRESULT]
    FindInterface: _Callable[[_Pointer[_struct.GUID],  # pCategory
                              IBaseFilter,  # pf
                              _Pointer[_struct.IID],  # riid
                              _type.c_void_p],  # ppint
                             _type.HRESULT]
    RenderStream: _Callable[[_Pointer[_struct.GUID],  # pCategory
                             _Unknwnbase.IUnknown,  # pSource
                             IBaseFilter,  # pfCompressor
                             IBaseFilter],  # pfRenderer
                            _type.HRESULT]
    ControlStream: _Callable[[_Pointer[_struct.GUID],  # pCategory
                              IBaseFilter,  # pFilter
                              _Pointer[_type.REFERENCE_TIME],  # pstart
                              _Pointer[_type.REFERENCE_TIME],  # pstop
                              _type.WORD,  # wStartCookie
                              _type.WORD],  # wStopCookie
                             _type.HRESULT]
    AllocCapFile: _Callable[[_type.LPCOLESTR,  # lpstr
                             _type.DWORDLONG],  # dwlSize
                            _type.HRESULT]
    CopyCaptureFile: _Callable[[_type.LPOLESTR,  # lpwstrOld
                                _type.LPOLESTR,  # lpwstrNew
                                _type.c_int,  # fAllowEscAbort
                                IAMCopyCaptureFileProgress],  # pCallback
                               _type.HRESULT]


class IAMCopyCaptureFileProgress(_Unknwnbase.IUnknown):
    Progress: _Callable[[_type.c_int],  # iProgress
                        _type.HRESULT]


class ICaptureGraphBuilder2(_Unknwnbase.IUnknown):
    SetFiltergraph: _Callable[[IGraphBuilder],  # pfg
                              _type.HRESULT]
    GetFiltergraph: _Callable[[_Pointer[IGraphBuilder]],  # ppfg
                              _type.HRESULT]
    SetOutputFileName: _Callable[[_Pointer[_struct.GUID],  # pType
                                  _type.LPCOLESTR,  # lpstrFile
                                  _Pointer[IBaseFilter],  # ppf
                                  _Pointer[IFileSinkFilter]],  # ppSink
                                 _type.HRESULT]
    FindInterface: _Callable[[_Pointer[_struct.GUID],  # pCategory
                              _Pointer[_struct.GUID],  # pType
                              IBaseFilter,  # pf
                              _Pointer[_struct.IID],  # riid
                              _type.c_void_p],  # ppint
                             _type.HRESULT]
    RenderStream: _Callable[[_Pointer[_struct.GUID],  # pCategory
                             _Pointer[_struct.GUID],  # pType
                             _Unknwnbase.IUnknown,  # pSource
                             IBaseFilter,  # pfCompressor
                             IBaseFilter],  # pfRenderer
                            _type.HRESULT]
    ControlStream: _Callable[[_Pointer[_struct.GUID],  # pCategory
                              _Pointer[_struct.GUID],  # pType
                              IBaseFilter,  # pFilter
                              _Pointer[_type.REFERENCE_TIME],  # pstart
                              _Pointer[_type.REFERENCE_TIME],  # pstop
                              _type.WORD,  # wStartCookie
                              _type.WORD],  # wStopCookie
                             _type.HRESULT]
    AllocCapFile: _Callable[[_type.LPCOLESTR,  # lpstr
                             _type.DWORDLONG],  # dwlSize
                            _type.HRESULT]
    CopyCaptureFile: _Callable[[_type.LPOLESTR,  # lpwstrOld
                                _type.LPOLESTR,  # lpwstrNew
                                _type.c_int,  # fAllowEscAbort
                                IAMCopyCaptureFileProgress],  # pCallback
                               _type.HRESULT]
    FindPin: _Callable[[_Unknwnbase.IUnknown,  # pSource
                        _enum.PIN_DIRECTION,  # pindir
                        _Pointer[_struct.GUID],  # pCategory
                        _Pointer[_struct.GUID],  # pType
                        _type.BOOL,  # fUnconnected
                        _type.c_int,  # num
                        _Pointer[IPin]],  # ppPin
                       _type.HRESULT]


class IFilterGraph2(IGraphBuilder):
    AddSourceFilterForMoniker: _Callable[[_objidl.IMoniker,  # pMoniker
                                          _objidl.IBindCtx,  # pCtx
                                          _type.LPCWSTR,  # lpcwstrFilterName
                                          _Pointer[IBaseFilter]],  # ppFilter
                                         _type.HRESULT]
    ReconnectEx: _Callable[[IPin,  # ppin
                            _Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                           _type.HRESULT]
    RenderEx: _Callable[[IPin,  # pPinOut
                         _type.DWORD,  # dwFlags
                         _Pointer[_type.DWORD]],  # pvContext
                        _type.HRESULT]


class IFilterGraph3(IFilterGraph2):
    SetSyncSourceEx: _Callable[[IReferenceClock,  # pClockForMostOfFilterGraph
                                IReferenceClock,  # pClockForFilter
                                IBaseFilter],  # pFilter
                               _type.HRESULT]


class IStreamBuilder(_Unknwnbase.IUnknown):
    Render: _Callable[[IPin,  # ppinOut
                       IGraphBuilder],  # pGraph
                      _type.HRESULT]
    Backout: _Callable[[IPin,  # ppinOut
                        IGraphBuilder],  # pGraph
                       _type.HRESULT]


class IAsyncReader(_Unknwnbase.IUnknown):
    RequestAllocator: _Callable[[IMemAllocator,  # pPreferred
                                 _Pointer[_struct.ALLOCATOR_PROPERTIES],  # pProps
                                 _Pointer[IMemAllocator]],  # ppActual
                                _type.HRESULT]
    Request: _Callable[[IMediaSample,  # pSample
                        _type.DWORD_PTR],  # dwUser
                       _type.HRESULT]
    WaitForNext: _Callable[[_type.DWORD,  # dwTimeout
                            _Pointer[IMediaSample],  # ppSample
                            _Pointer[_type.DWORD_PTR]],  # pdwUser
                           _type.HRESULT]
    SyncReadAligned: _Callable[[IMediaSample],  # pSample
                               _type.HRESULT]
    SyncRead: _Callable[[_type.LONGLONG,  # llPosition
                         _type.LONG,  # lLength
                         _Pointer[_type.BYTE]],  # pBuffer
                        _type.HRESULT]
    Length: _Callable[[_Pointer[_type.LONGLONG],  # pTotal
                       _Pointer[_type.LONGLONG]],  # pAvailable
                      _type.HRESULT]
    BeginFlush: _Callable[[],
                          _type.HRESULT]
    EndFlush: _Callable[[],
                        _type.HRESULT]


class IGraphVersion(_Unknwnbase.IUnknown):
    QueryVersion: _Callable[[_Pointer[_type.LONG]],  # pVersion
                            _type.HRESULT]


class IResourceConsumer(_Unknwnbase.IUnknown):
    AcquireResource: _Callable[[_type.LONG],  # idResource
                               _type.HRESULT]
    ReleaseResource: _Callable[[_type.LONG],  # idResource
                               _type.HRESULT]


class IResourceManager(_Unknwnbase.IUnknown):
    Register: _Callable[[_type.LPCWSTR,  # pName
                         _type.LONG,  # cResource
                         _Pointer[_type.LONG]],  # plToken
                        _type.HRESULT]
    RegisterGroup: _Callable[[_type.LPCWSTR,  # pName
                              _type.LONG,  # cResource
                              _Pointer[_type.LONG],  # palTokens
                              _Pointer[_type.LONG]],  # plToken
                             _type.HRESULT]
    RequestResource: _Callable[[_type.LONG,  # idResource
                                _Unknwnbase.IUnknown,  # pFocusObject
                                IResourceConsumer],  # pConsumer
                               _type.HRESULT]
    NotifyAcquire: _Callable[[_type.LONG,  # idResource
                              IResourceConsumer,  # pConsumer
                              _type.HRESULT],  # hr
                             _type.HRESULT]
    NotifyRelease: _Callable[[_type.LONG,  # idResource
                              IResourceConsumer,  # pConsumer
                              _type.BOOL],  # bStillWant
                             _type.HRESULT]
    CancelRequest: _Callable[[_type.LONG,  # idResource
                              IResourceConsumer],  # pConsumer
                             _type.HRESULT]
    SetFocus: _Callable[[_Unknwnbase.IUnknown],  # pFocusObject
                        _type.HRESULT]
    ReleaseFocus: _Callable[[_Unknwnbase.IUnknown],  # pFocusObject
                            _type.HRESULT]


class IDistributorNotify(_Unknwnbase.IUnknown):
    Stop: _Callable[[],
                    _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    Run: _Callable[[_type.REFERENCE_TIME],  # tStart
                   _type.HRESULT]
    SetSyncSource: _Callable[[IReferenceClock],  # pClock
                             _type.HRESULT]
    NotifyGraphChange: _Callable[[],
                                 _type.HRESULT]


class IAMStreamControl(_Unknwnbase.IUnknown):
    StartAt: _Callable[[_Pointer[_type.REFERENCE_TIME],  # ptStart
                        _type.DWORD],  # dwCookie
                       _type.HRESULT]
    StopAt: _Callable[[_Pointer[_type.REFERENCE_TIME],  # ptStop
                       _type.BOOL,  # bSendExtra
                       _type.DWORD],  # dwCookie
                      _type.HRESULT]
    GetInfo: _Callable[[_Pointer[_struct.AM_STREAM_INFO]],  # pInfo
                       _type.HRESULT]


class ISeekingPassThru(_Unknwnbase.IUnknown):
    Init: _Callable[[_type.BOOL,  # bSupportRendering
                     IPin],  # pPin
                    _type.HRESULT]


class IAMStreamConfig(_Unknwnbase.IUnknown):
    SetFormat: _Callable[[_Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                         _type.HRESULT]
    GetFormat: _Callable[[_Pointer[_Pointer[_struct.AM_MEDIA_TYPE]]],  # ppmt
                         _type.HRESULT]
    GetNumberOfCapabilities: _Callable[[_Pointer[_type.c_int],  # piCount
                                        _Pointer[_type.c_int]],  # piSize
                                       _type.HRESULT]
    GetStreamCaps: _Callable[[_type.c_int,  # iIndex
                              _Pointer[_Pointer[_struct.AM_MEDIA_TYPE]],  # ppmt
                              _Pointer[_type.BYTE]],  # pSCC
                             _type.HRESULT]


class IConfigInterleaving(_Unknwnbase.IUnknown):
    put_Mode: _Callable[[_enum.InterleavingMode],  # mode
                        _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.InterleavingMode]],  # pMode
                        _type.HRESULT]
    put_Interleaving: _Callable[[_Pointer[_type.REFERENCE_TIME],  # prtInterleave
                                 _Pointer[_type.REFERENCE_TIME]],  # prtPreroll
                                _type.HRESULT]
    get_Interleaving: _Callable[[_Pointer[_type.REFERENCE_TIME],  # prtInterleave
                                 _Pointer[_type.REFERENCE_TIME]],  # prtPreroll
                                _type.HRESULT]


class IConfigAviMux(_Unknwnbase.IUnknown):
    SetMasterStream: _Callable[[_type.LONG],  # iStream
                               _type.HRESULT]
    GetMasterStream: _Callable[[_Pointer[_type.LONG]],  # pStream
                               _type.HRESULT]
    SetOutputCompatibilityIndex: _Callable[[_type.BOOL],  # fOldIndex
                                           _type.HRESULT]
    GetOutputCompatibilityIndex: _Callable[[_Pointer[_type.BOOL]],  # pfOldIndex
                                           _type.HRESULT]


class IAMVideoCompression(_Unknwnbase.IUnknown):
    put_KeyFrameRate: _Callable[[_type.c_long],  # KeyFrameRate
                                _type.HRESULT]
    get_KeyFrameRate: _Callable[[_Pointer[_type.c_long]],  # pKeyFrameRate
                                _type.HRESULT]
    put_PFramesPerKeyFrame: _Callable[[_type.c_long],  # PFramesPerKeyFrame
                                      _type.HRESULT]
    get_PFramesPerKeyFrame: _Callable[[_Pointer[_type.c_long]],  # pPFramesPerKeyFrame
                                      _type.HRESULT]
    put_Quality: _Callable[[_type.c_double],  # Quality
                           _type.HRESULT]
    get_Quality: _Callable[[_Pointer[_type.c_double]],  # pQuality
                           _type.HRESULT]
    put_WindowSize: _Callable[[_type.DWORDLONG],  # WindowSize
                              _type.HRESULT]
    get_WindowSize: _Callable[[_Pointer[_type.DWORDLONG]],  # pWindowSize
                              _type.HRESULT]
    GetInfo: _Callable[[_type.LPWSTR,  # pszVersion
                        _Pointer[_type.c_int],  # pcbVersion
                        _type.LPWSTR,  # pszDescription
                        _Pointer[_type.c_int],  # pcbDescription
                        _Pointer[_type.c_long],  # pDefaultKeyFrameRate
                        _Pointer[_type.c_long],  # pDefaultPFramesPerKey
                        _Pointer[_type.c_double],  # pDefaultQuality
                        _Pointer[_type.c_long]],  # pCapabilities
                       _type.HRESULT]
    OverrideKeyFrame: _Callable[[_type.c_long],  # FrameNumber
                                _type.HRESULT]
    OverrideFrameSize: _Callable[[_type.c_long,  # FrameNumber
                                  _type.c_long],  # Size
                                 _type.HRESULT]


class IAMVfwCaptureDialogs(_Unknwnbase.IUnknown):
    HasDialog: _Callable[[_type.c_int],  # iDialog
                         _type.HRESULT]
    ShowDialog: _Callable[[_type.c_int,  # iDialog
                           _type.HWND],  # hwnd
                          _type.HRESULT]
    SendDriverMessage: _Callable[[_type.c_int,  # iDialog
                                  _type.c_int,  # uMsg
                                  _type.c_long,  # dw1
                                  _type.c_long],  # dw2
                                 _type.HRESULT]


class IAMVfwCompressDialogs(_Unknwnbase.IUnknown):
    ShowDialog: _Callable[[_type.c_int,  # iDialog
                           _type.HWND],  # hwnd
                          _type.HRESULT]
    GetState: _Callable[[_type.LPVOID,  # pState
                         _Pointer[_type.c_int]],  # pcbState
                        _type.HRESULT]
    SetState: _Callable[[_type.LPVOID,  # pState
                         _type.c_int],  # cbState
                        _type.HRESULT]
    SendDriverMessage: _Callable[[_type.c_int,  # uMsg
                                  _type.c_long,  # dw1
                                  _type.c_long],  # dw2
                                 _type.HRESULT]


class IAMDroppedFrames(_Unknwnbase.IUnknown):
    GetNumDropped: _Callable[[_Pointer[_type.c_long]],  # plDropped
                             _type.HRESULT]
    GetNumNotDropped: _Callable[[_Pointer[_type.c_long]],  # plNotDropped
                                _type.HRESULT]
    GetDroppedInfo: _Callable[[_type.c_long,  # lSize
                               _Pointer[_type.c_long],  # plArray
                               _Pointer[_type.c_long]],  # plNumCopied
                              _type.HRESULT]
    GetAverageFrameSize: _Callable[[_Pointer[_type.c_long]],  # plAverageSize
                                   _type.HRESULT]


class IAMAudioInputMixer(_Unknwnbase.IUnknown):
    put_Enable: _Callable[[_type.BOOL],  # fEnable
                          _type.HRESULT]
    get_Enable: _Callable[[_Pointer[_type.BOOL]],  # pfEnable
                          _type.HRESULT]
    put_Mono: _Callable[[_type.BOOL],  # fMono
                        _type.HRESULT]
    get_Mono: _Callable[[_Pointer[_type.BOOL]],  # pfMono
                        _type.HRESULT]
    put_MixLevel: _Callable[[_type.c_double],  # Level
                            _type.HRESULT]
    get_MixLevel: _Callable[[_Pointer[_type.c_double]],  # pLevel
                            _type.HRESULT]
    put_Pan: _Callable[[_type.c_double],  # Pan
                       _type.HRESULT]
    get_Pan: _Callable[[_Pointer[_type.c_double]],  # pPan
                       _type.HRESULT]
    put_Loudness: _Callable[[_type.BOOL],  # fLoudness
                            _type.HRESULT]
    get_Loudness: _Callable[[_Pointer[_type.BOOL]],  # pfLoudness
                            _type.HRESULT]
    put_Treble: _Callable[[_type.c_double],  # Treble
                          _type.HRESULT]
    get_Treble: _Callable[[_Pointer[_type.c_double]],  # pTreble
                          _type.HRESULT]
    get_TrebleRange: _Callable[[_Pointer[_type.c_double]],  # pRange
                               _type.HRESULT]
    put_Bass: _Callable[[_type.c_double],  # Bass
                        _type.HRESULT]
    get_Bass: _Callable[[_Pointer[_type.c_double]],  # pBass
                        _type.HRESULT]
    get_BassRange: _Callable[[_Pointer[_type.c_double]],  # pRange
                             _type.HRESULT]


class IAMBufferNegotiation(_Unknwnbase.IUnknown):
    SuggestAllocatorProperties: _Callable[[_Pointer[_struct.ALLOCATOR_PROPERTIES]],  # pprop
                                          _type.HRESULT]
    GetAllocatorProperties: _Callable[[_Pointer[_struct.ALLOCATOR_PROPERTIES]],  # pprop
                                      _type.HRESULT]


class IAMAnalogVideoDecoder(_Unknwnbase.IUnknown):
    get_AvailableTVFormats: _Callable[[_Pointer[_type.c_long]],  # lAnalogVideoStandard
                                      _type.HRESULT]
    put_TVFormat: _Callable[[_type.c_long],  # lAnalogVideoStandard
                            _type.HRESULT]
    get_TVFormat: _Callable[[_Pointer[_type.c_long]],  # plAnalogVideoStandard
                            _type.HRESULT]
    get_HorizontalLocked: _Callable[[_Pointer[_type.c_long]],  # plLocked
                                    _type.HRESULT]
    put_VCRHorizontalLocking: _Callable[[_type.c_long],  # lVCRHorizontalLocking
                                        _type.HRESULT]
    get_VCRHorizontalLocking: _Callable[[_Pointer[_type.c_long]],  # plVCRHorizontalLocking
                                        _type.HRESULT]
    get_NumberOfLines: _Callable[[_Pointer[_type.c_long]],  # plNumberOfLines
                                 _type.HRESULT]
    put_OutputEnable: _Callable[[_type.c_long],  # lOutputEnable
                                _type.HRESULT]
    get_OutputEnable: _Callable[[_Pointer[_type.c_long]],  # plOutputEnable
                                _type.HRESULT]


class IAMVideoProcAmp(_Unknwnbase.IUnknown):
    GetRange: _Callable[[_type.c_long,  # Property
                         _Pointer[_type.c_long],  # pMin
                         _Pointer[_type.c_long],  # pMax
                         _Pointer[_type.c_long],  # pSteppingDelta
                         _Pointer[_type.c_long],  # pDefault
                         _Pointer[_type.c_long]],  # pCapsFlags
                        _type.HRESULT]
    Set: _Callable[[_type.c_long,  # Property
                    _type.c_long,  # lValue
                    _type.c_long],  # Flags
                   _type.HRESULT]
    Get: _Callable[[_type.c_long,  # Property
                    _Pointer[_type.c_long],  # lValue
                    _Pointer[_type.c_long]],  # Flags
                   _type.HRESULT]


class IAMCameraControl(_Unknwnbase.IUnknown):
    GetRange: _Callable[[_type.c_long,  # Property
                         _Pointer[_type.c_long],  # pMin
                         _Pointer[_type.c_long],  # pMax
                         _Pointer[_type.c_long],  # pSteppingDelta
                         _Pointer[_type.c_long],  # pDefault
                         _Pointer[_type.c_long]],  # pCapsFlags
                        _type.HRESULT]
    Set: _Callable[[_type.c_long,  # Property
                    _type.c_long,  # lValue
                    _type.c_long],  # Flags
                   _type.HRESULT]
    Get: _Callable[[_type.c_long,  # Property
                    _Pointer[_type.c_long],  # lValue
                    _Pointer[_type.c_long]],  # Flags
                   _type.HRESULT]


class IAMVideoControl(_Unknwnbase.IUnknown):
    GetCaps: _Callable[[IPin,  # pPin
                        _Pointer[_type.c_long]],  # pCapsFlags
                       _type.HRESULT]
    SetMode: _Callable[[IPin,  # pPin
                        _type.c_long],  # Mode
                       _type.HRESULT]
    GetMode: _Callable[[IPin,  # pPin
                        _Pointer[_type.c_long]],  # Mode
                       _type.HRESULT]
    GetCurrentActualFrameRate: _Callable[[IPin,  # pPin
                                          _Pointer[_type.LONGLONG]],  # ActualFrameRate
                                         _type.HRESULT]
    GetMaxAvailableFrameRate: _Callable[[IPin,  # pPin
                                         _type.c_long,  # iIndex
                                         _struct.SIZE,  # Dimensions
                                         _Pointer[_type.LONGLONG]],  # MaxAvailableFrameRate
                                        _type.HRESULT]
    GetFrameRateList: _Callable[[IPin,  # pPin
                                 _type.c_long,  # iIndex
                                 _struct.SIZE,  # Dimensions
                                 _Pointer[_type.c_long],  # ListSize
                                 _Pointer[_Pointer[_type.LONGLONG]]],  # FrameRates
                                _type.HRESULT]


class IAMCrossbar(_Unknwnbase.IUnknown):
    get_PinCounts: _Callable[[_Pointer[_type.c_long],  # OutputPinCount
                              _Pointer[_type.c_long]],  # InputPinCount
                             _type.HRESULT]
    CanRoute: _Callable[[_type.c_long,  # OutputPinIndex
                         _type.c_long],  # InputPinIndex
                        _type.HRESULT]
    Route: _Callable[[_type.c_long,  # OutputPinIndex
                      _type.c_long],  # InputPinIndex
                     _type.HRESULT]
    get_IsRoutedTo: _Callable[[_type.c_long,  # OutputPinIndex
                               _Pointer[_type.c_long]],  # InputPinIndex
                              _type.HRESULT]
    get_CrossbarPinInfo: _Callable[[_type.BOOL,  # IsInputPin
                                    _type.c_long,  # PinIndex
                                    _Pointer[_type.c_long],  # PinIndexRelated
                                    _Pointer[_type.c_long]],  # PhysicalType
                                   _type.HRESULT]


class IAMTuner(_Unknwnbase.IUnknown):
    put_Channel: _Callable[[_type.c_long,  # lChannel
                            _type.c_long,  # lVideoSubChannel
                            _type.c_long],  # lAudioSubChannel
                           _type.HRESULT]
    get_Channel: _Callable[[_Pointer[_type.c_long],  # plChannel
                            _Pointer[_type.c_long],  # plVideoSubChannel
                            _Pointer[_type.c_long]],  # plAudioSubChannel
                           _type.HRESULT]
    ChannelMinMax: _Callable[[_Pointer[_type.c_long],  # lChannelMin
                              _Pointer[_type.c_long]],  # lChannelMax
                             _type.HRESULT]
    put_CountryCode: _Callable[[_type.c_long],  # lCountryCode
                               _type.HRESULT]
    get_CountryCode: _Callable[[_Pointer[_type.c_long]],  # plCountryCode
                               _type.HRESULT]
    put_TuningSpace: _Callable[[_type.c_long],  # lTuningSpace
                               _type.HRESULT]
    get_TuningSpace: _Callable[[_Pointer[_type.c_long]],  # plTuningSpace
                               _type.HRESULT]
    Logon: _Callable[[_type.HANDLE],  # hCurrentUser
                     _type.HRESULT]
    Logout: _Callable[[],
                      _type.HRESULT]
    SignalPresent: _Callable[[_Pointer[_type.c_long]],  # plSignalStrength
                             _type.HRESULT]
    put_Mode: _Callable[[_enum.AMTunerModeType],  # lMode
                        _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.AMTunerModeType]],  # plMode
                        _type.HRESULT]
    GetAvailableModes: _Callable[[_Pointer[_type.c_long]],  # plModes
                                 _type.HRESULT]
    RegisterNotificationCallBack: _Callable[[IAMTunerNotification,  # pNotify
                                             _type.c_long],  # lEvents
                                            _type.HRESULT]
    UnRegisterNotificationCallBack: _Callable[[IAMTunerNotification],  # pNotify
                                              _type.HRESULT]


class IAMTunerNotification(_Unknwnbase.IUnknown):
    OnEvent: _Callable[[_enum.AMTunerEventType],  # Event
                       _type.HRESULT]


class IAMTVTuner(IAMTuner):
    get_AvailableTVFormats: _Callable[[_Pointer[_type.c_long]],  # lAnalogVideoStandard
                                      _type.HRESULT]
    get_TVFormat: _Callable[[_Pointer[_type.c_long]],  # plAnalogVideoStandard
                            _type.HRESULT]
    AutoTune: _Callable[[_type.c_long,  # lChannel
                         _Pointer[_type.c_long]],  # plFoundSignal
                        _type.HRESULT]
    StoreAutoTune: _Callable[[],
                             _type.HRESULT]
    get_NumInputConnections: _Callable[[_Pointer[_type.c_long]],  # plNumInputConnections
                                       _type.HRESULT]
    put_InputType: _Callable[[_type.c_long,  # lIndex
                              _enum.TunerInputType],  # InputType
                             _type.HRESULT]
    get_InputType: _Callable[[_type.c_long,  # lIndex
                              _Pointer[_enum.TunerInputType]],  # pInputType
                             _type.HRESULT]
    put_ConnectInput: _Callable[[_type.c_long],  # lIndex
                                _type.HRESULT]
    get_ConnectInput: _Callable[[_Pointer[_type.c_long]],  # plIndex
                                _type.HRESULT]
    get_VideoFrequency: _Callable[[_Pointer[_type.c_long]],  # lFreq
                                  _type.HRESULT]
    get_AudioFrequency: _Callable[[_Pointer[_type.c_long]],  # lFreq
                                  _type.HRESULT]


class IBPCSatelliteTuner(IAMTuner):
    get_DefaultSubChannelTypes: _Callable[[_Pointer[_type.c_long],  # plDefaultVideoType
                                           _Pointer[_type.c_long]],  # plDefaultAudioType
                                          _type.HRESULT]
    put_DefaultSubChannelTypes: _Callable[[_type.c_long,  # lDefaultVideoType
                                           _type.c_long],  # lDefaultAudioType
                                          _type.HRESULT]
    IsTapingPermitted: _Callable[[],
                                 _type.HRESULT]


class IAMTVAudio(_Unknwnbase.IUnknown):
    GetHardwareSupportedTVAudioModes: _Callable[[_Pointer[_type.c_long]],  # plModes
                                                _type.HRESULT]
    GetAvailableTVAudioModes: _Callable[[_Pointer[_type.c_long]],  # plModes
                                        _type.HRESULT]
    get_TVAudioMode: _Callable[[_Pointer[_type.c_long]],  # plMode
                               _type.HRESULT]
    put_TVAudioMode: _Callable[[_type.c_long],  # lMode
                               _type.HRESULT]
    RegisterNotificationCallBack: _Callable[[IAMTunerNotification,  # pNotify
                                             _type.c_long],  # lEvents
                                            _type.HRESULT]
    UnRegisterNotificationCallBack: _Callable[[IAMTunerNotification],  # pNotify
                                              _type.HRESULT]


class IAMTVAudioNotification(_Unknwnbase.IUnknown):
    OnEvent: _Callable[[_enum.AMTVAudioEventType],  # Event
                       _type.HRESULT]


class IAMAnalogVideoEncoder(_Unknwnbase.IUnknown):
    get_AvailableTVFormats: _Callable[[_Pointer[_type.c_long]],  # lAnalogVideoStandard
                                      _type.HRESULT]
    put_TVFormat: _Callable[[_type.c_long],  # lAnalogVideoStandard
                            _type.HRESULT]
    get_TVFormat: _Callable[[_Pointer[_type.c_long]],  # plAnalogVideoStandard
                            _type.HRESULT]
    put_CopyProtection: _Callable[[_type.c_long],  # lVideoCopyProtection
                                  _type.HRESULT]
    get_CopyProtection: _Callable[[_Pointer[_type.c_long]],  # lVideoCopyProtection
                                  _type.HRESULT]
    put_CCEnable: _Callable[[_type.c_long],  # lCCEnable
                            _type.HRESULT]
    get_CCEnable: _Callable[[_Pointer[_type.c_long]],  # lCCEnable
                            _type.HRESULT]


class IKsPropertySet(_Unknwnbase.IUnknown):
    Set: _Callable[[_Pointer[_struct.GUID],  # guidPropSet
                    _type.DWORD,  # dwPropID
                    _type.LPVOID,  # pInstanceData
                    _type.DWORD,  # cbInstanceData
                    _type.LPVOID,  # pPropData
                    _type.DWORD],  # cbPropData
                   _type.HRESULT]
    Get: _Callable[[_Pointer[_struct.GUID],  # guidPropSet
                    _type.DWORD,  # dwPropID
                    _type.LPVOID,  # pInstanceData
                    _type.DWORD,  # cbInstanceData
                    _type.LPVOID,  # pPropData
                    _type.DWORD,  # cbPropData
                    _Pointer[_type.DWORD]],  # pcbReturned
                   _type.HRESULT]
    QuerySupported: _Callable[[_Pointer[_struct.GUID],  # guidPropSet
                               _type.DWORD,  # dwPropID
                               _Pointer[_type.DWORD]],  # pTypeSupport
                              _type.HRESULT]


class IMediaPropertyBag(_oaidl.IPropertyBag):
    EnumProperty: _Callable[[_type.ULONG,  # iProperty
                             _Pointer[_struct.VARIANT],  # pvarPropertyName
                             _Pointer[_struct.VARIANT]],  # pvarPropertyValue
                            _type.HRESULT]


class IPersistMediaPropertyBag(_objidl.IPersist):
    InitNew: _Callable[[],
                       _type.HRESULT]
    Load: _Callable[[IMediaPropertyBag,  # pPropBag
                     _oaidl.IErrorLog],  # pErrorLog
                    _type.HRESULT]
    Save: _Callable[[IMediaPropertyBag,  # pPropBag
                     _type.BOOL,  # fClearDirty
                     _type.BOOL],  # fSaveAllProperties
                    _type.HRESULT]


class IAMPhysicalPinInfo(_Unknwnbase.IUnknown):
    GetPhysicalType: _Callable[[_Pointer[_type.c_long],  # pType
                                _Pointer[_type.LPOLESTR]],  # ppszType
                               _type.HRESULT]


class IAMExtDevice(_Unknwnbase.IUnknown):
    GetCapability: _Callable[[_type.c_long,  # Capability
                              _Pointer[_type.c_long],  # pValue
                              _Pointer[_type.c_double]],  # pdblValue
                             _type.HRESULT]
    get_ExternalDeviceID: _Callable[[_Pointer[_type.LPOLESTR]],  # ppszData
                                    _type.HRESULT]
    get_ExternalDeviceVersion: _Callable[[_Pointer[_type.LPOLESTR]],  # ppszData
                                         _type.HRESULT]
    put_DevicePower: _Callable[[_type.c_long],  # PowerMode
                               _type.HRESULT]
    get_DevicePower: _Callable[[_Pointer[_type.c_long]],  # pPowerMode
                               _type.HRESULT]
    Calibrate: _Callable[[_type.HEVENT,  # hEvent
                          _type.c_long,  # Mode
                          _Pointer[_type.c_long]],  # pStatus
                         _type.HRESULT]
    put_DevicePort: _Callable[[_type.c_long],  # DevicePort
                              _type.HRESULT]
    get_DevicePort: _Callable[[_Pointer[_type.c_long]],  # pDevicePort
                              _type.HRESULT]


class IAMExtTransport(_Unknwnbase.IUnknown):
    GetCapability: _Callable[[_type.c_long,  # Capability
                              _Pointer[_type.c_long],  # pValue
                              _Pointer[_type.c_double]],  # pdblValue
                             _type.HRESULT]
    put_MediaState: _Callable[[_type.c_long],  # State
                              _type.HRESULT]
    get_MediaState: _Callable[[_Pointer[_type.c_long]],  # pState
                              _type.HRESULT]
    put_LocalControl: _Callable[[_type.c_long],  # State
                                _type.HRESULT]
    get_LocalControl: _Callable[[_Pointer[_type.c_long]],  # pState
                                _type.HRESULT]
    GetStatus: _Callable[[_type.c_long,  # StatusItem
                          _Pointer[_type.c_long]],  # pValue
                         _type.HRESULT]
    GetTransportBasicParameters: _Callable[[_type.c_long,  # Param
                                            _Pointer[_type.c_long],  # pValue
                                            _Pointer[_type.LPOLESTR]],  # ppszData
                                           _type.HRESULT]
    SetTransportBasicParameters: _Callable[[_type.c_long,  # Param
                                            _type.c_long,  # Value
                                            _type.LPCOLESTR],  # pszData
                                           _type.HRESULT]
    GetTransportVideoParameters: _Callable[[_type.c_long,  # Param
                                            _Pointer[_type.c_long]],  # pValue
                                           _type.HRESULT]
    SetTransportVideoParameters: _Callable[[_type.c_long,  # Param
                                            _type.c_long],  # Value
                                           _type.HRESULT]
    GetTransportAudioParameters: _Callable[[_type.c_long,  # Param
                                            _Pointer[_type.c_long]],  # pValue
                                           _type.HRESULT]
    SetTransportAudioParameters: _Callable[[_type.c_long,  # Param
                                            _type.c_long],  # Value
                                           _type.HRESULT]
    put_Mode: _Callable[[_type.c_long],  # Mode
                        _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_type.c_long]],  # pMode
                        _type.HRESULT]
    put_Rate: _Callable[[_type.c_double],  # dblRate
                        _type.HRESULT]
    get_Rate: _Callable[[_Pointer[_type.c_double]],  # pdblRate
                        _type.HRESULT]
    GetChase: _Callable[[_Pointer[_type.c_long],  # pEnabled
                         _Pointer[_type.c_long],  # pOffset
                         _Pointer[_type.HEVENT]],  # phEvent
                        _type.HRESULT]
    SetChase: _Callable[[_type.c_long,  # Enable
                         _type.c_long,  # Offset
                         _type.HEVENT],  # hEvent
                        _type.HRESULT]
    GetBump: _Callable[[_Pointer[_type.c_long],  # pSpeed
                        _Pointer[_type.c_long]],  # pDuration
                       _type.HRESULT]
    SetBump: _Callable[[_type.c_long,  # Speed
                        _type.c_long],  # Duration
                       _type.HRESULT]
    get_AntiClogControl: _Callable[[_Pointer[_type.c_long]],  # pEnabled
                                   _type.HRESULT]
    put_AntiClogControl: _Callable[[_type.c_long],  # Enable
                                   _type.HRESULT]
    GetEditPropertySet: _Callable[[_type.c_long,  # EditID
                                   _Pointer[_type.c_long]],  # pState
                                  _type.HRESULT]
    SetEditPropertySet: _Callable[[_Pointer[_type.c_long],  # pEditID
                                   _type.c_long],  # State
                                  _type.HRESULT]
    GetEditProperty: _Callable[[_type.c_long,  # EditID
                                _type.c_long,  # Param
                                _Pointer[_type.c_long]],  # pValue
                               _type.HRESULT]
    SetEditProperty: _Callable[[_type.c_long,  # EditID
                                _type.c_long,  # Param
                                _type.c_long],  # Value
                               _type.HRESULT]
    get_EditStart: _Callable[[_Pointer[_type.c_long]],  # pValue
                             _type.HRESULT]
    put_EditStart: _Callable[[_type.c_long],  # Value
                             _type.HRESULT]


class IAMTimecodeReader(_Unknwnbase.IUnknown):
    GetTCRMode: _Callable[[_type.c_long,  # Param
                           _Pointer[_type.c_long]],  # pValue
                          _type.HRESULT]
    SetTCRMode: _Callable[[_type.c_long,  # Param
                           _type.c_long],  # Value
                          _type.HRESULT]
    put_VITCLine: _Callable[[_type.c_long],  # Line
                            _type.HRESULT]
    get_VITCLine: _Callable[[_Pointer[_type.c_long]],  # pLine
                            _type.HRESULT]
    GetTimecode: _Callable[[_Pointer[_struct.TIMECODE_SAMPLE]],  # pTimecodeSample
                           _type.HRESULT]


class IAMTimecodeGenerator(_Unknwnbase.IUnknown):
    GetTCGMode: _Callable[[_type.c_long,  # Param
                           _Pointer[_type.c_long]],  # pValue
                          _type.HRESULT]
    SetTCGMode: _Callable[[_type.c_long,  # Param
                           _type.c_long],  # Value
                          _type.HRESULT]
    put_VITCLine: _Callable[[_type.c_long],  # Line
                            _type.HRESULT]
    get_VITCLine: _Callable[[_Pointer[_type.c_long]],  # pLine
                            _type.HRESULT]
    SetTimecode: _Callable[[_Pointer[_struct.TIMECODE_SAMPLE]],  # pTimecodeSample
                           _type.HRESULT]
    GetTimecode: _Callable[[_Pointer[_struct.TIMECODE_SAMPLE]],  # pTimecodeSample
                           _type.HRESULT]


class IAMTimecodeDisplay(_Unknwnbase.IUnknown):
    GetTCDisplayEnable: _Callable[[_Pointer[_type.c_long]],  # pState
                                  _type.HRESULT]
    SetTCDisplayEnable: _Callable[[_type.c_long],  # State
                                  _type.HRESULT]
    GetTCDisplay: _Callable[[_type.c_long,  # Param
                             _Pointer[_type.c_long]],  # pValue
                            _type.HRESULT]
    SetTCDisplay: _Callable[[_type.c_long,  # Param
                             _type.c_long],  # Value
                            _type.HRESULT]


class IAMDevMemoryAllocator(_Unknwnbase.IUnknown):
    GetInfo: _Callable[[_Pointer[_type.DWORD],  # pdwcbTotalFree
                        _Pointer[_type.DWORD],  # pdwcbLargestFree
                        _Pointer[_type.DWORD],  # pdwcbTotalMemory
                        _Pointer[_type.DWORD]],  # pdwcbMinimumChunk
                       _type.HRESULT]
    CheckMemory: _Callable[[_Pointer[_type.BYTE]],  # pBuffer
                           _type.HRESULT]
    Alloc: _Callable[[_Pointer[_Pointer[_type.BYTE]],  # ppBuffer
                      _Pointer[_type.DWORD]],  # pdwcbBuffer
                     _type.HRESULT]
    Free: _Callable[[_Pointer[_type.BYTE]],  # pBuffer
                    _type.HRESULT]
    GetDevMemoryObject: _Callable[[_Pointer[_Unknwnbase.IUnknown],  # ppUnkInnner
                                   _Unknwnbase.IUnknown],  # pUnkOuter
                                  _type.HRESULT]


class IAMDevMemoryControl(_Unknwnbase.IUnknown):
    QueryWriteSync: _Callable[[],
                              _type.HRESULT]
    WriteSync: _Callable[[],
                         _type.HRESULT]
    GetDevId: _Callable[[_Pointer[_type.DWORD]],  # pdwDevId
                        _type.HRESULT]


class IAMStreamSelect(_Unknwnbase.IUnknown):
    Count: _Callable[[_Pointer[_type.DWORD]],  # pcStreams
                     _type.HRESULT]
    Info: _Callable[[_type.c_long,  # lIndex
                     _Pointer[_Pointer[_struct.AM_MEDIA_TYPE]],  # ppmt
                     _Pointer[_type.DWORD],  # pdwFlags
                     _Pointer[_type.LCID],  # plcid
                     _Pointer[_type.DWORD],  # pdwGroup
                     _Pointer[_type.LPWSTR],  # ppszName
                     _Pointer[_Unknwnbase.IUnknown],  # ppObject
                     _Pointer[_Unknwnbase.IUnknown]],  # ppUnk
                    _type.HRESULT]
    Enable: _Callable[[_type.c_long,  # lIndex
                       _type.DWORD],  # dwFlags
                      _type.HRESULT]


class IAMResourceControl(_Unknwnbase.IUnknown):
    Reserve: _Callable[[_type.DWORD,  # dwFlags
                        _type.PVOID],  # pvReserved
                       _type.HRESULT]


class IAMClockAdjust(_Unknwnbase.IUnknown):
    SetClockDelta: _Callable[[_type.REFERENCE_TIME],  # rtDelta
                             _type.HRESULT]


class IAMFilterMiscFlags(_Unknwnbase.IUnknown):
    GetMiscFlags: _Callable[[],
                            _type.ULONG]


class IDrawVideoImage(_Unknwnbase.IUnknown):
    DrawVideoImageBegin: _Callable[[],
                                   _type.HRESULT]
    DrawVideoImageEnd: _Callable[[],
                                 _type.HRESULT]
    DrawVideoImageDraw: _Callable[[_type.HDC,  # hdc
                                   _Pointer[_struct.RECT],  # lprcSrc
                                   _Pointer[_struct.RECT]],  # lprcDst
                                  _type.HRESULT]


class IDecimateVideoImage(_Unknwnbase.IUnknown):
    SetDecimationImageSize: _Callable[[_type.c_long,  # lWidth
                                       _type.c_long],  # lHeight
                                      _type.HRESULT]
    ResetDecimationImageSize: _Callable[[],
                                        _type.HRESULT]


class IAMVideoDecimationProperties(_Unknwnbase.IUnknown):
    QueryDecimationUsage: _Callable[[_Pointer[_enum.DECIMATION_USAGE]],  # lpUsage
                                    _type.HRESULT]
    SetDecimationUsage: _Callable[[_enum.DECIMATION_USAGE],  # Usage
                                  _type.HRESULT]


class IVideoFrameStep(_Unknwnbase.IUnknown):
    Step: _Callable[[_type.DWORD,  # dwFrames
                     _Unknwnbase.IUnknown],  # pStepObject
                    _type.HRESULT]
    CanStep: _Callable[[_type.c_long,  # bMultiple
                        _Unknwnbase.IUnknown],  # pStepObject
                       _type.HRESULT]
    CancelStep: _Callable[[],
                          _type.HRESULT]


class IAMLatency(_Unknwnbase.IUnknown):
    GetLatency: _Callable[[_Pointer[_type.REFERENCE_TIME]],  # prtLatency
                          _type.HRESULT]


class IAMPushSource(IAMLatency):
    GetPushSourceFlags: _Callable[[_Pointer[_type.ULONG]],  # pFlags
                                  _type.HRESULT]
    SetPushSourceFlags: _Callable[[_type.ULONG],  # Flags
                                  _type.HRESULT]
    SetStreamOffset: _Callable[[_type.REFERENCE_TIME],  # rtOffset
                               _type.HRESULT]
    GetStreamOffset: _Callable[[_Pointer[_type.REFERENCE_TIME]],  # prtOffset
                               _type.HRESULT]
    GetMaxStreamOffset: _Callable[[_Pointer[_type.REFERENCE_TIME]],  # prtMaxOffset
                                  _type.HRESULT]
    SetMaxStreamOffset: _Callable[[_type.REFERENCE_TIME],  # rtMaxOffset
                                  _type.HRESULT]


class IAMDeviceRemoval(_Unknwnbase.IUnknown):
    DeviceInfo: _Callable[[_Pointer[_struct.CLSID],  # pclsidInterfaceClass
                           _Pointer[_type.LPWSTR]],  # pwszSymbolicLink
                          _type.HRESULT]
    Reassociate: _Callable[[],
                           _type.HRESULT]
    Disassociate: _Callable[[],
                            _type.HRESULT]


class IDVEnc(_Unknwnbase.IUnknown):
    get_IFormatResolution: _Callable[[_Pointer[_type.c_int],  # VideoFormat
                                      _Pointer[_type.c_int],  # DVFormat
                                      _Pointer[_type.c_int],  # Resolution
                                      _type.BYTE,  # fDVInfo
                                      _Pointer[_struct.DVINFO]],  # sDVInfo
                                     _type.HRESULT]
    put_IFormatResolution: _Callable[[_type.c_int,  # VideoFormat
                                      _type.c_int,  # DVFormat
                                      _type.c_int,  # Resolution
                                      _type.BYTE,  # fDVInfo
                                      _Pointer[_struct.DVINFO]],  # sDVInfo
                                     _type.HRESULT]


class IIPDVDec(_Unknwnbase.IUnknown):
    get_IPDisplay: _Callable[[_Pointer[_type.c_int]],  # displayPix
                             _type.HRESULT]
    put_IPDisplay: _Callable[[_type.c_int],  # displayPix
                             _type.HRESULT]


class IDVRGB219(_Unknwnbase.IUnknown):
    SetRGB219: _Callable[[_type.BOOL],  # bState
                         _type.HRESULT]


class IDVSplitter(_Unknwnbase.IUnknown):
    DiscardAlternateVideoFrames: _Callable[[_type.c_int],  # nDiscard
                                           _type.HRESULT]


class IAMAudioRendererStats(_Unknwnbase.IUnknown):
    GetStatParam: _Callable[[_type.DWORD,  # dwParam
                             _Pointer[_type.DWORD],  # pdwParam1
                             _Pointer[_type.DWORD]],  # pdwParam2
                            _type.HRESULT]


class IAMGraphStreams(_Unknwnbase.IUnknown):
    FindUpstreamInterface: _Callable[[IPin,  # pPin
                                      _Pointer[_struct.IID],  # riid
                                      _type.c_void_p,  # ppvInterface
                                      _type.DWORD],  # dwFlags
                                     _type.HRESULT]
    SyncUsingStreamOffset: _Callable[[_type.BOOL],  # bUseStreamOffset
                                     _type.HRESULT]
    SetMaxGraphLatency: _Callable[[_type.REFERENCE_TIME],  # rtMaxGraphLatency
                                  _type.HRESULT]


class IAMOverlayFX(_Unknwnbase.IUnknown):
    QueryOverlayFXCaps: _Callable[[_Pointer[_type.DWORD]],  # lpdwOverlayFXCaps
                                  _type.HRESULT]
    SetOverlayFX: _Callable[[_type.DWORD],  # dwOverlayFX
                            _type.HRESULT]
    GetOverlayFX: _Callable[[_Pointer[_type.DWORD]],  # lpdwOverlayFX
                            _type.HRESULT]


class IAMOpenProgress(_Unknwnbase.IUnknown):
    QueryProgress: _Callable[[_Pointer[_type.LONGLONG],  # pllTotal
                              _Pointer[_type.LONGLONG]],  # pllCurrent
                             _type.HRESULT]
    AbortOperation: _Callable[[],
                              _type.HRESULT]


class IMpeg2Demultiplexer(_Unknwnbase.IUnknown):
    CreateOutputPin: _Callable[[_Pointer[_struct.AM_MEDIA_TYPE],  # pMediaType
                                _type.LPWSTR,  # pszPinName
                                _Pointer[IPin]],  # ppIPin
                               _type.HRESULT]
    SetOutputPinMediaType: _Callable[[_type.LPWSTR,  # pszPinName
                                      _Pointer[_struct.AM_MEDIA_TYPE]],  # pMediaType
                                     _type.HRESULT]
    DeleteOutputPin: _Callable[[_type.LPWSTR],  # pszPinName
                               _type.HRESULT]


class IEnumStreamIdMap(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # cRequest
                     _Pointer[_struct.STREAM_ID_MAP],  # pStreamIdMap
                     _Pointer[_type.ULONG]],  # pcReceived
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # cRecords
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumStreamIdMap]],  # ppIEnumStreamIdMap
                     _type.HRESULT]


class IMPEG2StreamIdMap(_Unknwnbase.IUnknown):
    MapStreamId: _Callable[[_type.ULONG,  # ulStreamId
                            _type.DWORD,  # MediaSampleContent
                            _type.ULONG,  # ulSubstreamFilterValue
                            _type.c_int],  # iDataOffset
                           _type.HRESULT]
    UnmapStreamId: _Callable[[_type.ULONG,  # culStreamId
                              _Pointer[_type.ULONG]],  # pulStreamId
                             _type.HRESULT]
    EnumStreamIdMap: _Callable[[_Pointer[IEnumStreamIdMap]],  # ppIEnumStreamIdMap
                               _type.HRESULT]


class IRegisterServiceProvider(_Unknwnbase.IUnknown):
    RegisterService: _Callable[[_Pointer[_struct.GUID],  # guidService
                                _Unknwnbase.IUnknown],  # pUnkObject
                               _type.HRESULT]


class IAMClockSlave(_Unknwnbase.IUnknown):
    SetErrorTolerance: _Callable[[_type.DWORD],  # dwTolerance
                                 _type.HRESULT]
    GetErrorTolerance: _Callable[[_Pointer[_type.DWORD]],  # pdwTolerance
                                 _type.HRESULT]


class IAMGraphBuilderCallback(_Unknwnbase.IUnknown):
    SelectedFilter: _Callable[[_objidl.IMoniker],  # pMon
                              _type.HRESULT]
    CreatedFilter: _Callable[[IBaseFilter],  # pFil
                             _type.HRESULT]


class IAMFilterGraphCallback(_Unknwnbase.IUnknown):
    UnableToRender: _Callable[[IPin],  # pPin
                              _type.HRESULT]


class IGetCapabilitiesKey(_Unknwnbase.IUnknown):
    GetCapabilitiesKey: _Callable[[_Pointer[_type.HKEY]],  # pHKey
                                  _type.HRESULT]


class IEncoderAPI(_Unknwnbase.IUnknown):
    IsSupported: _Callable[[_Pointer[_struct.GUID]],  # Api
                           _type.HRESULT]
    IsAvailable: _Callable[[_Pointer[_struct.GUID]],  # Api
                           _type.HRESULT]
    GetParameterRange: _Callable[[_Pointer[_struct.GUID],  # Api
                                  _Pointer[_struct.VARIANT],  # ValueMin
                                  _Pointer[_struct.VARIANT],  # ValueMax
                                  _Pointer[_struct.VARIANT]],  # SteppingDelta
                                 _type.HRESULT]
    GetParameterValues: _Callable[[_Pointer[_struct.GUID],  # Api
                                   _Pointer[_Pointer[_struct.VARIANT]],  # Values
                                   _Pointer[_type.ULONG]],  # ValuesCount
                                  _type.HRESULT]
    GetDefaultValue: _Callable[[_Pointer[_struct.GUID],  # Api
                                _Pointer[_struct.VARIANT]],  # Value
                               _type.HRESULT]
    GetValue: _Callable[[_Pointer[_struct.GUID],  # Api
                         _Pointer[_struct.VARIANT]],  # Value
                        _type.HRESULT]
    SetValue: _Callable[[_Pointer[_struct.GUID],  # Api
                         _Pointer[_struct.VARIANT]],  # Value
                        _type.HRESULT]


class IVideoEncoder(IEncoderAPI):
    pass


class IAMDecoderCaps(_Unknwnbase.IUnknown):
    GetDecoderCaps: _Callable[[_type.DWORD,  # dwCapIndex
                               _Pointer[_type.DWORD]],  # lpdwCap
                              _type.HRESULT]


class IAMCertifiedOutputProtection(_Unknwnbase.IUnknown):
    KeyExchange: _Callable[[_Pointer[_struct.GUID],  # pRandom
                            _Pointer[_Pointer[_type.BYTE]],  # VarLenCertGH
                            _Pointer[_type.DWORD]],  # pdwLengthCertGH
                           _type.HRESULT]
    SessionSequenceStart: _Callable[[_Pointer[_struct.AMCOPPSignature]],  # pSig
                                    _type.HRESULT]
    ProtectionCommand: _Callable[[_Pointer[_struct.AMCOPPCommand]],  # cmd
                                 _type.HRESULT]
    ProtectionStatus: _Callable[[_Pointer[_struct.AMCOPPStatusInput],  # pStatusInput
                                 _Pointer[_struct.AMCOPPStatusOutput]],  # pStatusOutput
                                _type.HRESULT]


class IAMAsyncReaderTimestampScaling(_Unknwnbase.IUnknown):
    GetTimestampMode: _Callable[[_Pointer[_type.BOOL]],  # pfRaw
                                _type.HRESULT]
    SetTimestampMode: _Callable[[_type.BOOL],  # fRaw
                                _type.HRESULT]


class IAMPluginControl(_Unknwnbase.IUnknown):
    GetPreferredClsid: _Callable[[_Pointer[_struct.GUID],  # subType
                                  _Pointer[_struct.CLSID]],  # clsid
                                 _type.HRESULT]
    GetPreferredClsidByIndex: _Callable[[_type.DWORD,  # index
                                         _Pointer[_struct.GUID],  # subType
                                         _Pointer[_struct.CLSID]],  # clsid
                                        _type.HRESULT]
    SetPreferredClsid: _Callable[[_Pointer[_struct.GUID],  # subType
                                  _Pointer[_struct.CLSID]],  # clsid
                                 _type.HRESULT]
    IsDisabled: _Callable[[_Pointer[_struct.IID]],  # clsid
                          _type.HRESULT]
    GetDisabledByIndex: _Callable[[_type.DWORD,  # index
                                   _Pointer[_struct.CLSID]],  # clsid
                                  _type.HRESULT]
    SetDisabled: _Callable[[_Pointer[_struct.IID],  # clsid
                            _type.BOOL],  # disabled
                           _type.HRESULT]
    IsLegacyDisabled: _Callable[[_type.LPCWSTR],  # dllName
                                _type.HRESULT]


class IPinConnection(_Unknwnbase.IUnknown):
    DynamicQueryAccept: _Callable[[_Pointer[_struct.AM_MEDIA_TYPE]],  # pmt
                                  _type.HRESULT]
    NotifyEndOfStream: _Callable[[_type.HANDLE],  # hNotifyEvent
                                 _type.HRESULT]
    IsEndPin: _Callable[[],
                        _type.HRESULT]
    DynamicDisconnect: _Callable[[],
                                 _type.HRESULT]


class IPinFlowControl(_Unknwnbase.IUnknown):
    Block: _Callable[[_type.DWORD,  # dwBlockFlags
                      _type.HANDLE],  # hEvent
                     _type.HRESULT]


class IGraphConfig(_Unknwnbase.IUnknown):
    Reconnect: _Callable[[IPin,  # pOutputPin
                          IPin,  # pInputPin
                          _Pointer[_struct.AM_MEDIA_TYPE],  # pmtFirstConnection
                          IBaseFilter,  # pUsingFilter
                          _type.HANDLE,  # hAbortEvent
                          _type.DWORD],  # dwFlags
                         _type.HRESULT]
    Reconfigure: _Callable[[IGraphConfigCallback,  # pCallback
                            _type.PVOID,  # pvContext
                            _type.DWORD,  # dwFlags
                            _type.HANDLE],  # hAbortEvent
                           _type.HRESULT]
    AddFilterToCache: _Callable[[IBaseFilter],  # pFilter
                                _type.HRESULT]
    EnumCacheFilter: _Callable[[_Pointer[IEnumFilters]],  # pEnum
                               _type.HRESULT]
    RemoveFilterFromCache: _Callable[[IBaseFilter],  # pFilter
                                     _type.HRESULT]
    GetStartTime: _Callable[[_Pointer[_type.REFERENCE_TIME]],  # prtStart
                            _type.HRESULT]
    PushThroughData: _Callable[[IPin,  # pOutputPin
                                IPinConnection,  # pConnection
                                _type.HANDLE],  # hEventAbort
                               _type.HRESULT]
    SetFilterFlags: _Callable[[IBaseFilter,  # pFilter
                               _type.DWORD],  # dwFlags
                              _type.HRESULT]
    GetFilterFlags: _Callable[[IBaseFilter,  # pFilter
                               _Pointer[_type.DWORD]],  # pdwFlags
                              _type.HRESULT]
    RemoveFilterEx: _Callable[[IBaseFilter,  # pFilter
                               _type.DWORD],  # Flags
                              _type.HRESULT]


class IGraphConfigCallback(_Unknwnbase.IUnknown):
    Reconfigure: _Callable[[_type.PVOID,  # pvContext
                            _type.DWORD],  # dwFlags
                           _type.HRESULT]


class IFilterChain(_Unknwnbase.IUnknown):
    StartChain: _Callable[[IBaseFilter,  # pStartFilter
                           IBaseFilter],  # pEndFilter
                          _type.HRESULT]
    PauseChain: _Callable[[IBaseFilter,  # pStartFilter
                           IBaseFilter],  # pEndFilter
                          _type.HRESULT]
    StopChain: _Callable[[IBaseFilter,  # pStartFilter
                          IBaseFilter],  # pEndFilter
                         _type.HRESULT]
    RemoveChain: _Callable[[IBaseFilter,  # pStartFilter
                            IBaseFilter],  # pEndFilter
                           _type.HRESULT]


class IVMRImagePresenter(_Unknwnbase.IUnknown):
    StartPresenting: _Callable[[_type.DWORD_PTR],  # dwUserID
                               _type.HRESULT]
    StopPresenting: _Callable[[_type.DWORD_PTR],  # dwUserID
                              _type.HRESULT]
    PresentImage: _Callable[[_type.DWORD_PTR,  # dwUserID
                             _Pointer[_struct.VMRPRESENTATIONINFO]],  # lpPresInfo
                            _type.HRESULT]


class IVMRSurfaceAllocator(_Unknwnbase.IUnknown):
    AllocateSurface: _Callable[[_type.DWORD_PTR,  # dwUserID
                                _Pointer[_struct.VMRALLOCATIONINFO],  # lpAllocInfo
                                _Pointer[_type.DWORD],  # lpdwActualBuffers
                                _Pointer[_ddraw.IDirectDrawSurface7]],  # lplpSurface
                               _type.HRESULT]
    FreeSurface: _Callable[[_type.DWORD_PTR],  # dwID
                           _type.HRESULT]
    PrepareSurface: _Callable[[_type.DWORD_PTR,  # dwUserID
                               _ddraw.IDirectDrawSurface7,  # lpSurface
                               _type.DWORD],  # dwSurfaceFlags
                              _type.HRESULT]
    AdviseNotify: _Callable[[IVMRSurfaceAllocatorNotify],  # lpIVMRSurfAllocNotify
                            _type.HRESULT]


class IVMRSurfaceAllocatorNotify(_Unknwnbase.IUnknown):
    AdviseSurfaceAllocator: _Callable[[_type.DWORD_PTR,  # dwUserID
                                       IVMRSurfaceAllocator],  # lpIVRMSurfaceAllocator
                                      _type.HRESULT]
    SetDDrawDevice: _Callable[[_ddraw.IDirectDraw7,  # lpDDrawDevice
                               _type.HMONITOR],  # hMonitor
                              _type.HRESULT]
    ChangeDDrawDevice: _Callable[[_ddraw.IDirectDraw7,  # lpDDrawDevice
                                  _type.HMONITOR],  # hMonitor
                                 _type.HRESULT]
    RestoreDDrawSurfaces: _Callable[[],
                                    _type.HRESULT]
    NotifyEvent: _Callable[[_type.LONG,  # EventCode
                            _type.LONG_PTR,  # Param1
                            _type.LONG_PTR],  # Param2
                           _type.HRESULT]
    SetBorderColor: _Callable[[_type.COLORREF],  # clrBorder
                              _type.HRESULT]


class IVMRWindowlessControl(_Unknwnbase.IUnknown):
    GetNativeVideoSize: _Callable[[_Pointer[_type.LONG],  # lpWidth
                                   _Pointer[_type.LONG],  # lpHeight
                                   _Pointer[_type.LONG],  # lpARWidth
                                   _Pointer[_type.LONG]],  # lpARHeight
                                  _type.HRESULT]
    GetMinIdealVideoSize: _Callable[[_Pointer[_type.LONG],  # lpWidth
                                     _Pointer[_type.LONG]],  # lpHeight
                                    _type.HRESULT]
    GetMaxIdealVideoSize: _Callable[[_Pointer[_type.LONG],  # lpWidth
                                     _Pointer[_type.LONG]],  # lpHeight
                                    _type.HRESULT]
    SetVideoPosition: _Callable[[_Pointer[_struct.RECT],  # lpSRCRect
                                 _Pointer[_struct.RECT]],  # lpDSTRect
                                _type.HRESULT]
    GetVideoPosition: _Callable[[_Pointer[_struct.RECT],  # lpSRCRect
                                 _Pointer[_struct.RECT]],  # lpDSTRect
                                _type.HRESULT]
    GetAspectRatioMode: _Callable[[_Pointer[_type.DWORD]],  # lpAspectRatioMode
                                  _type.HRESULT]
    SetAspectRatioMode: _Callable[[_type.DWORD],  # AspectRatioMode
                                  _type.HRESULT]
    SetVideoClippingWindow: _Callable[[_type.HWND],  # hwnd
                                      _type.HRESULT]
    RepaintVideo: _Callable[[_type.HWND,  # hwnd
                             _type.HDC],  # hdc
                            _type.HRESULT]
    DisplayModeChanged: _Callable[[],
                                  _type.HRESULT]
    GetCurrentImage: _Callable[[_Pointer[_Pointer[_type.BYTE]]],  # lpDib
                               _type.HRESULT]
    SetBorderColor: _Callable[[_type.COLORREF],  # Clr
                              _type.HRESULT]
    GetBorderColor: _Callable[[_Pointer[_type.COLORREF]],  # lpClr
                              _type.HRESULT]
    SetColorKey: _Callable[[_type.COLORREF],  # Clr
                           _type.HRESULT]
    GetColorKey: _Callable[[_Pointer[_type.COLORREF]],  # lpClr
                           _type.HRESULT]


class IVMRMixerControl(_Unknwnbase.IUnknown):
    SetAlpha: _Callable[[_type.DWORD,  # dwStreamID
                         _type.c_float],  # Alpha
                        _type.HRESULT]
    GetAlpha: _Callable[[_type.DWORD,  # dwStreamID
                         _Pointer[_type.c_float]],  # pAlpha
                        _type.HRESULT]
    SetZOrder: _Callable[[_type.DWORD,  # dwStreamID
                          _type.DWORD],  # dwZ
                         _type.HRESULT]
    GetZOrder: _Callable[[_type.DWORD,  # dwStreamID
                          _Pointer[_type.DWORD]],  # pZ
                         _type.HRESULT]
    SetOutputRect: _Callable[[_type.DWORD,  # dwStreamID
                              _Pointer[_struct.NORMALIZEDRECT]],  # pRect
                             _type.HRESULT]
    GetOutputRect: _Callable[[_type.DWORD,  # dwStreamID
                              _Pointer[_struct.NORMALIZEDRECT]],  # pRect
                             _type.HRESULT]
    SetBackgroundClr: _Callable[[_type.COLORREF],  # ClrBkg
                                _type.HRESULT]
    GetBackgroundClr: _Callable[[_Pointer[_type.COLORREF]],  # lpClrBkg
                                _type.HRESULT]
    SetMixingPrefs: _Callable[[_type.DWORD],  # dwMixerPrefs
                              _type.HRESULT]
    GetMixingPrefs: _Callable[[_Pointer[_type.DWORD]],  # pdwMixerPrefs
                              _type.HRESULT]


class IVMRMonitorConfig(_Unknwnbase.IUnknown):
    SetMonitor: _Callable[[_Pointer[_struct.VMRGUID]],  # pGUID
                          _type.HRESULT]
    GetMonitor: _Callable[[_Pointer[_struct.VMRGUID]],  # pGUID
                          _type.HRESULT]
    SetDefaultMonitor: _Callable[[_Pointer[_struct.VMRGUID]],  # pGUID
                                 _type.HRESULT]
    GetDefaultMonitor: _Callable[[_Pointer[_struct.VMRGUID]],  # pGUID
                                 _type.HRESULT]
    GetAvailableMonitors: _Callable[[_Pointer[_struct.VMRMONITORINFO],  # pInfo
                                     _type.DWORD,  # dwMaxInfoArraySize
                                     _Pointer[_type.DWORD]],  # pdwNumDevices
                                    _type.HRESULT]


class IVMRFilterConfig(_Unknwnbase.IUnknown):
    SetImageCompositor: _Callable[[IVMRImageCompositor],  # lpVMRImgCompositor
                                  _type.HRESULT]
    SetNumberOfStreams: _Callable[[_type.DWORD],  # dwMaxStreams
                                  _type.HRESULT]
    GetNumberOfStreams: _Callable[[_Pointer[_type.DWORD]],  # pdwMaxStreams
                                  _type.HRESULT]
    SetRenderingPrefs: _Callable[[_type.DWORD],  # dwRenderFlags
                                 _type.HRESULT]
    GetRenderingPrefs: _Callable[[_Pointer[_type.DWORD]],  # pdwRenderFlags
                                 _type.HRESULT]
    SetRenderingMode: _Callable[[_type.DWORD],  # Mode
                                _type.HRESULT]
    GetRenderingMode: _Callable[[_Pointer[_type.DWORD]],  # pMode
                                _type.HRESULT]


class IVMRAspectRatioControl(_Unknwnbase.IUnknown):
    GetAspectRatioMode: _Callable[[_Pointer[_type.DWORD]],  # lpdwARMode
                                  _type.HRESULT]
    SetAspectRatioMode: _Callable[[_type.DWORD],  # dwARMode
                                  _type.HRESULT]


class IVMRDeinterlaceControl(_Unknwnbase.IUnknown):
    GetNumberOfDeinterlaceModes: _Callable[[_Pointer[_struct.VMRVideoDesc],  # lpVideoDescription
                                            _Pointer[_type.DWORD],  # lpdwNumDeinterlaceModes
                                            _Pointer[_struct.GUID]],  # lpDeinterlaceModes
                                           _type.HRESULT]
    GetDeinterlaceModeCaps: _Callable[[_Pointer[_struct.GUID],  # lpDeinterlaceMode
                                       _Pointer[_struct.VMRVideoDesc],  # lpVideoDescription
                                       _Pointer[_struct.VMRDeinterlaceCaps]],  # lpDeinterlaceCaps
                                      _type.HRESULT]
    GetDeinterlaceMode: _Callable[[_type.DWORD,  # dwStreamID
                                   _Pointer[_struct.GUID]],  # lpDeinterlaceMode
                                  _type.HRESULT]
    SetDeinterlaceMode: _Callable[[_type.DWORD,  # dwStreamID
                                   _Pointer[_struct.GUID]],  # lpDeinterlaceMode
                                  _type.HRESULT]
    GetDeinterlacePrefs: _Callable[[_Pointer[_type.DWORD]],  # lpdwDeinterlacePrefs
                                   _type.HRESULT]
    SetDeinterlacePrefs: _Callable[[_type.DWORD],  # dwDeinterlacePrefs
                                   _type.HRESULT]
    GetActualDeinterlaceMode: _Callable[[_type.DWORD,  # dwStreamID
                                         _Pointer[_struct.GUID]],  # lpDeinterlaceMode
                                        _type.HRESULT]


class IVMRMixerBitmap(_Unknwnbase.IUnknown):
    SetAlphaBitmap: _Callable[[_Pointer[_struct.VMRALPHABITMAP]],  # pBmpParms
                              _type.HRESULT]
    UpdateAlphaBitmapParameters: _Callable[[_Pointer[_struct.VMRALPHABITMAP]],  # pBmpParms
                                           _type.HRESULT]
    GetAlphaBitmapParameters: _Callable[[_Pointer[_struct.VMRALPHABITMAP]],  # pBmpParms
                                        _type.HRESULT]


class IVMRImageCompositor(_Unknwnbase.IUnknown):
    InitCompositionTarget: _Callable[[_Unknwnbase.IUnknown,  # pD3DDevice
                                      _ddraw.IDirectDrawSurface7],  # pddsRenderTarget
                                     _type.HRESULT]
    TermCompositionTarget: _Callable[[_Unknwnbase.IUnknown,  # pD3DDevice
                                      _ddraw.IDirectDrawSurface7],  # pddsRenderTarget
                                     _type.HRESULT]
    SetStreamMediaType: _Callable[[_type.DWORD,  # dwStrmID
                                   _Pointer[_struct.AM_MEDIA_TYPE],  # pmt
                                   _type.BOOL],  # fTexture
                                  _type.HRESULT]
    CompositeImage: _Callable[[_Unknwnbase.IUnknown,  # pD3DDevice
                               _ddraw.IDirectDrawSurface7,  # pddsRenderTarget
                               _Pointer[_struct.AM_MEDIA_TYPE],  # pmtRenderTarget
                               _type.REFERENCE_TIME,  # rtStart
                               _type.REFERENCE_TIME,  # rtEnd
                               _type.DWORD,  # dwClrBkGnd
                               _Pointer[_struct.VMRVIDEOSTREAMINFO],  # pVideoStreamInfo
                               _type.UINT],  # cStreams
                              _type.HRESULT]


class IVMRVideoStreamControl(_Unknwnbase.IUnknown):
    SetColorKey: _Callable[[_Pointer[_struct.DDCOLORKEY]],  # lpClrKey
                           _type.HRESULT]
    GetColorKey: _Callable[[_Pointer[_struct.DDCOLORKEY]],  # lpClrKey
                           _type.HRESULT]
    SetStreamActiveState: _Callable[[_type.BOOL],  # fActive
                                    _type.HRESULT]
    GetStreamActiveState: _Callable[[_Pointer[_type.BOOL]],  # lpfActive
                                    _type.HRESULT]


class IVMRSurface(_Unknwnbase.IUnknown):
    IsSurfaceLocked: _Callable[[],
                               _type.HRESULT]
    LockSurface: _Callable[[_Pointer[_Pointer[_type.BYTE]]],  # lpSurface
                           _type.HRESULT]
    UnlockSurface: _Callable[[],
                             _type.HRESULT]
    GetSurface: _Callable[[_Pointer[_ddraw.IDirectDrawSurface7]],  # lplpSurface
                          _type.HRESULT]


class IVMRImagePresenterConfig(_Unknwnbase.IUnknown):
    SetRenderingPrefs: _Callable[[_type.DWORD],  # dwRenderFlags
                                 _type.HRESULT]
    GetRenderingPrefs: _Callable[[_Pointer[_type.DWORD]],  # dwRenderFlags
                                 _type.HRESULT]


class IVMRImagePresenterExclModeConfig(IVMRImagePresenterConfig):
    SetXlcModeDDObjAndPrimarySurface: _Callable[[_ddraw.IDirectDraw7,  # lpDDObj
                                                 _ddraw.IDirectDrawSurface7],  # lpPrimarySurf
                                                _type.HRESULT]
    GetXlcModeDDObjAndPrimarySurface: _Callable[[_Pointer[_ddraw.IDirectDraw7],  # lpDDObj
                                                 _Pointer[_ddraw.IDirectDrawSurface7]],  # lpPrimarySurf
                                                _type.HRESULT]


class IVPManager(_Unknwnbase.IUnknown):
    SetVideoPortIndex: _Callable[[_type.DWORD],  # dwVideoPortIndex
                                 _type.HRESULT]
    GetVideoPortIndex: _Callable[[_Pointer[_type.DWORD]],  # pdwVideoPortIndex
                                 _type.HRESULT]


class IDvdControl(_Unknwnbase.IUnknown):
    TitlePlay: _Callable[[_type.ULONG],  # ulTitle
                         _type.HRESULT]
    ChapterPlay: _Callable[[_type.ULONG,  # ulTitle
                            _type.ULONG],  # ulChapter
                           _type.HRESULT]
    TimePlay: _Callable[[_type.ULONG,  # ulTitle
                         _type.ULONG],  # bcdTime
                        _type.HRESULT]
    StopForResume: _Callable[[],
                             _type.HRESULT]
    GoUp: _Callable[[],
                    _type.HRESULT]
    TimeSearch: _Callable[[_type.ULONG],  # bcdTime
                          _type.HRESULT]
    ChapterSearch: _Callable[[_type.ULONG],  # ulChapter
                             _type.HRESULT]
    PrevPGSearch: _Callable[[],
                            _type.HRESULT]
    TopPGSearch: _Callable[[],
                           _type.HRESULT]
    NextPGSearch: _Callable[[],
                            _type.HRESULT]
    ForwardScan: _Callable[[_type.c_double],  # dwSpeed
                           _type.HRESULT]
    BackwardScan: _Callable[[_type.c_double],  # dwSpeed
                            _type.HRESULT]
    MenuCall: _Callable[[_enum.DVD_MENU_ID],  # MenuID
                        _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    UpperButtonSelect: _Callable[[],
                                 _type.HRESULT]
    LowerButtonSelect: _Callable[[],
                                 _type.HRESULT]
    LeftButtonSelect: _Callable[[],
                                _type.HRESULT]
    RightButtonSelect: _Callable[[],
                                 _type.HRESULT]
    ButtonActivate: _Callable[[],
                              _type.HRESULT]
    ButtonSelectAndActivate: _Callable[[_type.ULONG],  # ulButton
                                       _type.HRESULT]
    StillOff: _Callable[[],
                        _type.HRESULT]
    PauseOn: _Callable[[],
                       _type.HRESULT]
    PauseOff: _Callable[[],
                        _type.HRESULT]
    MenuLanguageSelect: _Callable[[_type.LCID],  # Language
                                  _type.HRESULT]
    AudioStreamChange: _Callable[[_type.ULONG],  # ulAudio
                                 _type.HRESULT]
    SubpictureStreamChange: _Callable[[_type.ULONG,  # ulSubPicture
                                       _type.BOOL],  # bDisplay
                                      _type.HRESULT]
    AngleChange: _Callable[[_type.ULONG],  # ulAngle
                           _type.HRESULT]
    ParentalLevelSelect: _Callable[[_type.ULONG],  # ulParentalLevel
                                   _type.HRESULT]
    ParentalCountrySelect: _Callable[[_type.WORD],  # wCountry
                                     _type.HRESULT]
    KaraokeAudioPresentationModeChange: _Callable[[_type.ULONG],  # ulMode
                                                  _type.HRESULT]
    VideoModePreferrence: _Callable[[_type.ULONG],  # ulPreferredDisplayMode
                                    _type.HRESULT]
    SetRoot: _Callable[[_type.LPCWSTR],  # pszPath
                       _type.HRESULT]
    MouseActivate: _Callable[[_struct.POINT],  # point
                             _type.HRESULT]
    MouseSelect: _Callable[[_struct.POINT],  # point
                           _type.HRESULT]
    ChapterPlayAutoStop: _Callable[[_type.ULONG,  # ulTitle
                                    _type.ULONG,  # ulChapter
                                    _type.ULONG],  # ulChaptersToPlay
                                   _type.HRESULT]


class IDvdInfo(_Unknwnbase.IUnknown):
    GetCurrentDomain: _Callable[[_Pointer[_enum.DVD_DOMAIN]],  # pDomain
                                _type.HRESULT]
    GetCurrentLocation: _Callable[[_Pointer[_struct.DVD_PLAYBACK_LOCATION]],  # pLocation
                                  _type.HRESULT]
    GetTotalTitleTime: _Callable[[_Pointer[_type.ULONG]],  # pulTotalTime
                                 _type.HRESULT]
    GetCurrentButton: _Callable[[_Pointer[_type.ULONG],  # pulButtonsAvailable
                                 _Pointer[_type.ULONG]],  # pulCurrentButton
                                _type.HRESULT]
    GetCurrentAngle: _Callable[[_Pointer[_type.ULONG],  # pulAnglesAvailable
                                _Pointer[_type.ULONG]],  # pulCurrentAngle
                               _type.HRESULT]
    GetCurrentAudio: _Callable[[_Pointer[_type.ULONG],  # pulStreamsAvailable
                                _Pointer[_type.ULONG]],  # pulCurrentStream
                               _type.HRESULT]
    GetCurrentSubpicture: _Callable[[_Pointer[_type.ULONG],  # pulStreamsAvailable
                                     _Pointer[_type.ULONG],  # pulCurrentStream
                                     _Pointer[_type.BOOL]],  # pIsDisabled
                                    _type.HRESULT]
    GetCurrentUOPS: _Callable[[_Pointer[_type.VALID_UOP_SOMTHING_OR_OTHER]],  # pUOP
                              _type.HRESULT]
    GetAllSPRMs: _Callable[[_Pointer[_Pointer[_type.DVD_REGISTER]]],  # pRegisterArray
                           _type.HRESULT]
    GetAllGPRMs: _Callable[[_Pointer[_Pointer[_type.DVD_REGISTER]]],  # pRegisterArray
                           _type.HRESULT]
    GetAudioLanguage: _Callable[[_type.ULONG,  # ulStream
                                 _Pointer[_type.LCID]],  # pLanguage
                                _type.HRESULT]
    GetSubpictureLanguage: _Callable[[_type.ULONG,  # ulStream
                                      _Pointer[_type.LCID]],  # pLanguage
                                     _type.HRESULT]
    GetTitleAttributes: _Callable[[_type.ULONG,  # ulTitle
                                   _Pointer[_struct.DVD_ATR]],  # pATR
                                  _type.HRESULT]
    GetVMGAttributes: _Callable[[_Pointer[_struct.DVD_ATR]],  # pATR
                                _type.HRESULT]
    GetCurrentVideoAttributes: _Callable[[_Pointer[_Pointer[_type.BYTE]]],  # pATR
                                         _type.HRESULT]
    GetCurrentAudioAttributes: _Callable[[_Pointer[_Pointer[_type.BYTE]]],  # pATR
                                         _type.HRESULT]
    GetCurrentSubpictureAttributes: _Callable[[_Pointer[_Pointer[_type.BYTE]]],  # pATR
                                              _type.HRESULT]
    GetCurrentVolumeInfo: _Callable[[_Pointer[_type.ULONG],  # pulNumOfVol
                                     _Pointer[_type.ULONG],  # pulThisVolNum
                                     _Pointer[_enum.DVD_DISC_SIDE],  # pSide
                                     _Pointer[_type.ULONG]],  # pulNumOfTitles
                                    _type.HRESULT]
    GetDVDTextInfo: _Callable[[_Pointer[_type.BYTE],  # pTextManager
                               _type.ULONG,  # ulBufSize
                               _Pointer[_type.ULONG]],  # pulActualSize
                              _type.HRESULT]
    GetPlayerParentalLevel: _Callable[[_Pointer[_type.ULONG],  # pulParentalLevel
                                       _Pointer[_type.ULONG]],  # pulCountryCode
                                      _type.HRESULT]
    GetNumberOfChapters: _Callable[[_type.ULONG,  # ulTitle
                                    _Pointer[_type.ULONG]],  # pulNumberOfChapters
                                   _type.HRESULT]
    GetTitleParentalLevels: _Callable[[_type.ULONG,  # ulTitle
                                       _Pointer[_type.ULONG]],  # pulParentalLevels
                                      _type.HRESULT]
    GetRoot: _Callable[[_type.LPSTR,  # pRoot
                        _type.ULONG,  # ulBufSize
                        _Pointer[_type.ULONG]],  # pulActualSize
                       _type.HRESULT]


class IDvdCmd(_Unknwnbase.IUnknown):
    WaitForStart: _Callable[[],
                            _type.HRESULT]
    WaitForEnd: _Callable[[],
                          _type.HRESULT]


class IDvdState(_Unknwnbase.IUnknown):
    GetDiscID: _Callable[[_Pointer[_type.ULONGLONG]],  # pullUniqueID
                         _type.HRESULT]
    GetParentalLevel: _Callable[[_Pointer[_type.ULONG]],  # pulParentalLevel
                                _type.HRESULT]


class IDvdControl2(_Unknwnbase.IUnknown):
    PlayTitle: _Callable[[_type.ULONG,  # ulTitle
                          _type.DWORD,  # dwFlags
                          _Pointer[IDvdCmd]],  # ppCmd
                         _type.HRESULT]
    PlayChapterInTitle: _Callable[[_type.ULONG,  # ulTitle
                                   _type.ULONG,  # ulChapter
                                   _type.DWORD,  # dwFlags
                                   _Pointer[IDvdCmd]],  # ppCmd
                                  _type.HRESULT]
    PlayAtTimeInTitle: _Callable[[_type.ULONG,  # ulTitle
                                  _Pointer[_struct.DVD_HMSF_TIMECODE],  # pStartTime
                                  _type.DWORD,  # dwFlags
                                  _Pointer[IDvdCmd]],  # ppCmd
                                 _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    ReturnFromSubmenu: _Callable[[_type.DWORD,  # dwFlags
                                  _Pointer[IDvdCmd]],  # ppCmd
                                 _type.HRESULT]
    PlayAtTime: _Callable[[_Pointer[_struct.DVD_HMSF_TIMECODE],  # pTime
                           _type.DWORD,  # dwFlags
                           _Pointer[IDvdCmd]],  # ppCmd
                          _type.HRESULT]
    PlayChapter: _Callable[[_type.ULONG,  # ulChapter
                            _type.DWORD,  # dwFlags
                            _Pointer[IDvdCmd]],  # ppCmd
                           _type.HRESULT]
    PlayPrevChapter: _Callable[[_type.DWORD,  # dwFlags
                                _Pointer[IDvdCmd]],  # ppCmd
                               _type.HRESULT]
    ReplayChapter: _Callable[[_type.DWORD,  # dwFlags
                              _Pointer[IDvdCmd]],  # ppCmd
                             _type.HRESULT]
    PlayNextChapter: _Callable[[_type.DWORD,  # dwFlags
                                _Pointer[IDvdCmd]],  # ppCmd
                               _type.HRESULT]
    PlayForwards: _Callable[[_type.c_double,  # dSpeed
                             _type.DWORD,  # dwFlags
                             _Pointer[IDvdCmd]],  # ppCmd
                            _type.HRESULT]
    PlayBackwards: _Callable[[_type.c_double,  # dSpeed
                              _type.DWORD,  # dwFlags
                              _Pointer[IDvdCmd]],  # ppCmd
                             _type.HRESULT]
    ShowMenu: _Callable[[_enum.DVD_MENU_ID,  # MenuID
                         _type.DWORD,  # dwFlags
                         _Pointer[IDvdCmd]],  # ppCmd
                        _type.HRESULT]
    Resume: _Callable[[_type.DWORD,  # dwFlags
                       _Pointer[IDvdCmd]],  # ppCmd
                      _type.HRESULT]
    SelectRelativeButton: _Callable[[_enum.DVD_RELATIVE_BUTTON],  # buttonDir
                                    _type.HRESULT]
    ActivateButton: _Callable[[],
                              _type.HRESULT]
    SelectButton: _Callable[[_type.ULONG],  # ulButton
                            _type.HRESULT]
    SelectAndActivateButton: _Callable[[_type.ULONG],  # ulButton
                                       _type.HRESULT]
    StillOff: _Callable[[],
                        _type.HRESULT]
    Pause: _Callable[[_type.BOOL],  # bState
                     _type.HRESULT]
    SelectAudioStream: _Callable[[_type.ULONG,  # ulAudio
                                  _type.DWORD,  # dwFlags
                                  _Pointer[IDvdCmd]],  # ppCmd
                                 _type.HRESULT]
    SelectSubpictureStream: _Callable[[_type.ULONG,  # ulSubPicture
                                       _type.DWORD,  # dwFlags
                                       _Pointer[IDvdCmd]],  # ppCmd
                                      _type.HRESULT]
    SetSubpictureState: _Callable[[_type.BOOL,  # bState
                                   _type.DWORD,  # dwFlags
                                   _Pointer[IDvdCmd]],  # ppCmd
                                  _type.HRESULT]
    SelectAngle: _Callable[[_type.ULONG,  # ulAngle
                            _type.DWORD,  # dwFlags
                            _Pointer[IDvdCmd]],  # ppCmd
                           _type.HRESULT]
    SelectParentalLevel: _Callable[[_type.ULONG],  # ulParentalLevel
                                   _type.HRESULT]
    SelectParentalCountry: _Callable[[_Pointer[_type.BYTE]],  # bCountry
                                     _type.HRESULT]
    SelectKaraokeAudioPresentationMode: _Callable[[_type.ULONG],  # ulMode
                                                  _type.HRESULT]
    SelectVideoModePreference: _Callable[[_type.ULONG],  # ulPreferredDisplayMode
                                         _type.HRESULT]
    SetDVDDirectory: _Callable[[_type.LPCWSTR],  # pszwPath
                               _type.HRESULT]
    ActivateAtPosition: _Callable[[_struct.POINT],  # point
                                  _type.HRESULT]
    SelectAtPosition: _Callable[[_struct.POINT],  # point
                                _type.HRESULT]
    PlayChaptersAutoStop: _Callable[[_type.ULONG,  # ulTitle
                                     _type.ULONG,  # ulChapter
                                     _type.ULONG,  # ulChaptersToPlay
                                     _type.DWORD,  # dwFlags
                                     _Pointer[IDvdCmd]],  # ppCmd
                                    _type.HRESULT]
    AcceptParentalLevelChange: _Callable[[_type.BOOL],  # bAccept
                                         _type.HRESULT]
    SetOption: _Callable[[_enum.DVD_OPTION_FLAG,  # flag
                          _type.BOOL],  # fState
                         _type.HRESULT]
    SetState: _Callable[[IDvdState,  # pState
                         _type.DWORD,  # dwFlags
                         _Pointer[IDvdCmd]],  # ppCmd
                        _type.HRESULT]
    PlayPeriodInTitleAutoStop: _Callable[[_type.ULONG,  # ulTitle
                                          _Pointer[_struct.DVD_HMSF_TIMECODE],  # pStartTime
                                          _Pointer[_struct.DVD_HMSF_TIMECODE],  # pEndTime
                                          _type.DWORD,  # dwFlags
                                          _Pointer[IDvdCmd]],  # ppCmd
                                         _type.HRESULT]
    SetGPRM: _Callable[[_type.ULONG,  # ulIndex
                        _type.WORD,  # wValue
                        _type.DWORD,  # dwFlags
                        _Pointer[IDvdCmd]],  # ppCmd
                       _type.HRESULT]
    SelectDefaultMenuLanguage: _Callable[[_type.LCID],  # Language
                                         _type.HRESULT]
    SelectDefaultAudioLanguage: _Callable[[_type.LCID,  # Language
                                           _enum.DVD_AUDIO_LANG_EXT],  # audioExtension
                                          _type.HRESULT]
    SelectDefaultSubpictureLanguage: _Callable[[_type.LCID,  # Language
                                                _enum.DVD_SUBPICTURE_LANG_EXT],  # subpictureExtension
                                               _type.HRESULT]


class IDvdInfo2(_Unknwnbase.IUnknown):
    GetCurrentDomain: _Callable[[_Pointer[_enum.DVD_DOMAIN]],  # pDomain
                                _type.HRESULT]
    GetCurrentLocation: _Callable[[_Pointer[_struct.DVD_PLAYBACK_LOCATION2]],  # pLocation
                                  _type.HRESULT]
    GetTotalTitleTime: _Callable[[_Pointer[_struct.DVD_HMSF_TIMECODE],  # pTotalTime
                                  _Pointer[_type.ULONG]],  # ulTimeCodeFlags
                                 _type.HRESULT]
    GetCurrentButton: _Callable[[_Pointer[_type.ULONG],  # pulButtonsAvailable
                                 _Pointer[_type.ULONG]],  # pulCurrentButton
                                _type.HRESULT]
    GetCurrentAngle: _Callable[[_Pointer[_type.ULONG],  # pulAnglesAvailable
                                _Pointer[_type.ULONG]],  # pulCurrentAngle
                               _type.HRESULT]
    GetCurrentAudio: _Callable[[_Pointer[_type.ULONG],  # pulStreamsAvailable
                                _Pointer[_type.ULONG]],  # pulCurrentStream
                               _type.HRESULT]
    GetCurrentSubpicture: _Callable[[_Pointer[_type.ULONG],  # pulStreamsAvailable
                                     _Pointer[_type.ULONG],  # pulCurrentStream
                                     _Pointer[_type.BOOL]],  # pbIsDisabled
                                    _type.HRESULT]
    GetCurrentUOPS: _Callable[[_Pointer[_type.ULONG]],  # pulUOPs
                              _type.HRESULT]
    GetAllSPRMs: _Callable[[_Pointer[_Pointer[_type.DVD_REGISTER]]],  # pRegisterArray
                           _type.HRESULT]
    GetAllGPRMs: _Callable[[_Pointer[_Pointer[_type.DVD_REGISTER]]],  # pRegisterArray
                           _type.HRESULT]
    GetAudioLanguage: _Callable[[_type.ULONG,  # ulStream
                                 _Pointer[_type.LCID]],  # pLanguage
                                _type.HRESULT]
    GetSubpictureLanguage: _Callable[[_type.ULONG,  # ulStream
                                      _Pointer[_type.LCID]],  # pLanguage
                                     _type.HRESULT]
    GetTitleAttributes: _Callable[[_type.ULONG,  # ulTitle
                                   _Pointer[_struct.DVD_MenuAttributes],  # pMenu
                                   _Pointer[_struct.DVD_TitleAttributes]],  # pTitle
                                  _type.HRESULT]
    GetVMGAttributes: _Callable[[_Pointer[_struct.DVD_MenuAttributes]],  # pATR
                                _type.HRESULT]
    GetCurrentVideoAttributes: _Callable[[_Pointer[_struct.DVD_VideoAttributes]],  # pATR
                                         _type.HRESULT]
    GetAudioAttributes: _Callable[[_type.ULONG,  # ulStream
                                   _Pointer[_struct.DVD_AudioAttributes]],  # pATR
                                  _type.HRESULT]
    GetKaraokeAttributes: _Callable[[_type.ULONG,  # ulStream
                                     _Pointer[_struct.DVD_KaraokeAttributes]],  # pAttributes
                                    _type.HRESULT]
    GetSubpictureAttributes: _Callable[[_type.ULONG,  # ulStream
                                        _Pointer[_struct.DVD_SubpictureAttributes]],  # pATR
                                       _type.HRESULT]
    GetDVDVolumeInfo: _Callable[[_Pointer[_type.ULONG],  # pulNumOfVolumes
                                 _Pointer[_type.ULONG],  # pulVolume
                                 _Pointer[_enum.DVD_DISC_SIDE],  # pSide
                                 _Pointer[_type.ULONG]],  # pulNumOfTitles
                                _type.HRESULT]
    GetDVDTextNumberOfLanguages: _Callable[[_Pointer[_type.ULONG]],  # pulNumOfLangs
                                           _type.HRESULT]
    GetDVDTextLanguageInfo: _Callable[[_type.ULONG,  # ulLangIndex
                                       _Pointer[_type.ULONG],  # pulNumOfStrings
                                       _Pointer[_type.LCID],  # pLangCode
                                       _Pointer[_enum.DVD_TextCharSet]],  # pbCharacterSet
                                      _type.HRESULT]
    GetDVDTextStringAsNative: _Callable[[_type.ULONG,  # ulLangIndex
                                         _type.ULONG,  # ulStringIndex
                                         _Pointer[_type.BYTE],  # pbBuffer
                                         _type.ULONG,  # ulMaxBufferSize
                                         _Pointer[_type.ULONG],  # pulActualSize
                                         _Pointer[_enum.DVD_TextStringType]],  # pType
                                        _type.HRESULT]
    GetDVDTextStringAsUnicode: _Callable[[_type.ULONG,  # ulLangIndex
                                          _type.ULONG,  # ulStringIndex
                                          _Pointer[_type.WCHAR],  # pchwBuffer
                                          _type.ULONG,  # ulMaxBufferSize
                                          _Pointer[_type.ULONG],  # pulActualSize
                                          _Pointer[_enum.DVD_TextStringType]],  # pType
                                         _type.HRESULT]
    GetPlayerParentalLevel: _Callable[[_Pointer[_type.ULONG],  # pulParentalLevel
                                       _Pointer[_type.BYTE]],  # pbCountryCode
                                      _type.HRESULT]
    GetNumberOfChapters: _Callable[[_type.ULONG,  # ulTitle
                                    _Pointer[_type.ULONG]],  # pulNumOfChapters
                                   _type.HRESULT]
    GetTitleParentalLevels: _Callable[[_type.ULONG,  # ulTitle
                                       _Pointer[_type.ULONG]],  # pulParentalLevels
                                      _type.HRESULT]
    GetDVDDirectory: _Callable[[_type.LPWSTR,  # pszwPath
                                _type.ULONG,  # ulMaxSize
                                _Pointer[_type.ULONG]],  # pulActualSize
                               _type.HRESULT]
    IsAudioStreamEnabled: _Callable[[_type.ULONG,  # ulStreamNum
                                     _Pointer[_type.BOOL]],  # pbEnabled
                                    _type.HRESULT]
    GetDiscID: _Callable[[_type.LPCWSTR,  # pszwPath
                          _Pointer[_type.ULONGLONG]],  # pullDiscID
                         _type.HRESULT]
    GetState: _Callable[[_Pointer[IDvdState]],  # pStateData
                        _type.HRESULT]
    GetMenuLanguages: _Callable[[_Pointer[_type.LCID],  # pLanguages
                                 _type.ULONG,  # ulMaxLanguages
                                 _Pointer[_type.ULONG]],  # pulActualLanguages
                                _type.HRESULT]
    GetButtonAtPosition: _Callable[[_struct.POINT,  # point
                                    _Pointer[_type.ULONG]],  # pulButtonIndex
                                   _type.HRESULT]
    GetCmdFromEvent: _Callable[[_type.LONG_PTR,  # lParam1
                                _Pointer[IDvdCmd]],  # pCmdObj
                               _type.HRESULT]
    GetDefaultMenuLanguage: _Callable[[_Pointer[_type.LCID]],  # pLanguage
                                      _type.HRESULT]
    GetDefaultAudioLanguage: _Callable[[_Pointer[_type.LCID],  # pLanguage
                                        _Pointer[_enum.DVD_AUDIO_LANG_EXT]],  # pAudioExtension
                                       _type.HRESULT]
    GetDefaultSubpictureLanguage: _Callable[[_Pointer[_type.LCID],  # pLanguage
                                             _Pointer[_enum.DVD_SUBPICTURE_LANG_EXT]],  # pSubpictureExtension
                                            _type.HRESULT]
    GetDecoderCaps: _Callable[[_Pointer[_struct.DVD_DECODER_CAPS]],  # pCaps
                              _type.HRESULT]
    GetButtonRect: _Callable[[_type.ULONG,  # ulButton
                              _Pointer[_struct.RECT]],  # pRect
                             _type.HRESULT]
    IsSubpictureStreamEnabled: _Callable[[_type.ULONG,  # ulStreamNum
                                          _Pointer[_type.BOOL]],  # pbEnabled
                                         _type.HRESULT]


class IDvdGraphBuilder(_Unknwnbase.IUnknown):
    GetFiltergraph: _Callable[[_Pointer[IGraphBuilder]],  # ppGB
                              _type.HRESULT]
    GetDvdInterface: _Callable[[_Pointer[_struct.IID],  # riid
                                _type.c_void_p],  # ppvIF
                               _type.HRESULT]
    RenderDvdVideoVolume: _Callable[[_type.LPCWSTR,  # lpcwszPathName
                                     _type.DWORD,  # dwFlags
                                     _Pointer[_struct.AM_DVD_RENDERSTATUS]],  # pStatus
                                    _type.HRESULT]


class IDDrawExclModeVideo(_Unknwnbase.IUnknown):
    SetDDrawObject: _Callable[[_ddraw.IDirectDraw],  # pDDrawObject
                              _type.HRESULT]
    GetDDrawObject: _Callable[[_Pointer[_ddraw.IDirectDraw],  # ppDDrawObject
                               _Pointer[_type.BOOL]],  # pbUsingExternal
                              _type.HRESULT]
    SetDDrawSurface: _Callable[[_ddraw.IDirectDrawSurface],  # pDDrawSurface
                               _type.HRESULT]
    GetDDrawSurface: _Callable[[_Pointer[_ddraw.IDirectDrawSurface],  # ppDDrawSurface
                                _Pointer[_type.BOOL]],  # pbUsingExternal
                               _type.HRESULT]
    SetDrawParameters: _Callable[[_Pointer[_struct.RECT],  # prcSource
                                  _Pointer[_struct.RECT]],  # prcTarget
                                 _type.HRESULT]
    GetNativeVideoProps: _Callable[[_Pointer[_type.DWORD],  # pdwVideoWidth
                                    _Pointer[_type.DWORD],  # pdwVideoHeight
                                    _Pointer[_type.DWORD],  # pdwPictAspectRatioX
                                    _Pointer[_type.DWORD]],  # pdwPictAspectRatioY
                                   _type.HRESULT]
    SetCallbackInterface: _Callable[[IDDrawExclModeVideoCallback,  # pCallback
                                     _type.DWORD],  # dwFlags
                                    _type.HRESULT]


class IDDrawExclModeVideoCallback(_Unknwnbase.IUnknown):
    OnUpdateOverlay: _Callable[[_type.BOOL,  # bBefore
                                _type.DWORD,  # dwFlags
                                _type.BOOL,  # bOldVisible
                                _Pointer[_struct.RECT],  # prcOldSrc
                                _Pointer[_struct.RECT],  # prcOldDest
                                _type.BOOL,  # bNewVisible
                                _Pointer[_struct.RECT],  # prcNewSrc
                                _Pointer[_struct.RECT]],  # prcNewDest
                               _type.HRESULT]
    OnUpdateColorKey: _Callable[[_Pointer[_struct.COLORKEY],  # pKey
                                 _type.DWORD],  # dwColor
                                _type.HRESULT]
    OnUpdateSize: _Callable[[_type.DWORD,  # dwWidth
                             _type.DWORD,  # dwHeight
                             _type.DWORD,  # dwARWidth
                             _type.DWORD],  # dwARHeight
                            _type.HRESULT]

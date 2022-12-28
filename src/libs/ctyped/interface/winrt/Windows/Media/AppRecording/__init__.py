from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAppRecordingManager(_inspectable.IInspectable):
    GetStatus: _Callable[[_Pointer[IAppRecordingStatus]],  # result
                         _type.HRESULT]
    StartRecordingToFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IAppRecordingResult]]],  # operation
                                         _type.HRESULT]
    RecordTimeSpanToFileAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # startTime
                                          _struct.Windows.Foundation.TimeSpan,  # duration
                                          _Windows_Storage.IStorageFile,  # file
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IAppRecordingResult]]],  # operation
                                         _type.HRESULT]
    get_SupportedScreenshotMediaEncodingSubtypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                                            _type.HRESULT]
    SaveScreenshotToFilesAsync: _Callable[[_Windows_Storage.IStorageFolder,  # folder
                                           _type.HSTRING,  # filenamePrefix
                                           _enum.Windows.Media.AppRecording.AppRecordingSaveScreenshotOption,  # option
                                           _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # requestedFormats
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IAppRecordingSaveScreenshotResult]]],  # operation
                                          _type.HRESULT]


class IAppRecordingManagerStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[IAppRecordingManager]],  # result
                          _type.HRESULT]

    _factory = True


class IAppRecordingResult(_inspectable.IInspectable):
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_IsFileTruncated: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]


class IAppRecordingSaveScreenshotResult(_inspectable.IInspectable):
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_SavedScreenshotInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAppRecordingSavedScreenshotInfo]]],  # value
                                        _type.HRESULT]


class IAppRecordingSavedScreenshotInfo(_inspectable.IInspectable):
    get_File: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                        _type.HRESULT]
    get_MediaEncodingSubtype: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]


class IAppRecordingStatus(_inspectable.IInspectable):
    get_CanRecord: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_CanRecordTimeSpan: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_HistoricalBufferDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                            _type.HRESULT]
    get_Details: _Callable[[_Pointer[IAppRecordingStatusDetails]],  # value
                           _type.HRESULT]


class IAppRecordingStatusDetails(_inspectable.IInspectable):
    get_IsAnyAppBroadcasting: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsCaptureResourceUnavailable: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    get_IsGameStreamInProgress: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_IsTimeSpanRecordingDisabled: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    get_IsGpuConstrained: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsAppInactive: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsBlockedForApp: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsDisabledByUser: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsDisabledBySystem: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]

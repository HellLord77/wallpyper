from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import oaidl as _oaidl
from . import objidlbase as _objidlbase
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IPrintDocumentPackageTarget(_Unknwnbase.IUnknown):
    GetPackageTargetTypes: _Callable[[_Pointer[_type.UINT32],  # targetCount
                                      _Pointer[_Pointer[_struct.GUID]]],  # targetTypes
                                     _type.HRESULT]
    GetPackageTarget: _Callable[[_Pointer[_struct.GUID],  # guidTargetType
                                 _Pointer[_struct.IID],  # riid
                                 _type.c_void_p],  # ppvTarget
                                _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]


class IPrintDocumentPackageTarget2(_Unknwnbase.IUnknown):
    GetIsTargetIppPrinter: _Callable[[_Pointer[_type.BOOL]],  # isIppPrinter
                                     _type.HRESULT]
    GetTargetIppPrintDevice: _Callable[[_Pointer[_struct.IID],  # riid
                                        _type.c_void_p],  # ppvTarget
                                       _type.HRESULT]


class IPrintDocumentPackageStatusEvent(_oaidl.IDispatch):
    PackageStatusUpdated: _Callable[[_Pointer[_struct.PrintDocumentPackageStatus]],  # packageStatus
                                    _type.HRESULT]


class IPrintDocumentPackageTargetFactory(_Unknwnbase.IUnknown):
    CreateDocumentPackageTargetForPrintJob: _Callable[[_type.LPCWSTR,  # printerName
                                                       _type.LPCWSTR,  # jobName
                                                       _objidlbase.IStream,  # jobOutputStream
                                                       _objidlbase.IStream,  # jobPrintTicketStream
                                                       _Pointer[IPrintDocumentPackageTarget]],  # docPackageTarget
                                                      _type.HRESULT]

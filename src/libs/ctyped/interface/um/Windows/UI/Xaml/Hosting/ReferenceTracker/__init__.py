from __future__ import annotations

from typing import Callable as _Callable

from ...... import Unknwnbase as _Unknwnbase
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IReferenceTrackerTarget(_Unknwnbase.IUnknown):
    AddRefFromReferenceTracker: _Callable[[],
                                          _type.ULONG]
    ReleaseFromReferenceTracker: _Callable[[],
                                           _type.ULONG]
    Peg: _Callable[[],
                   _type.HRESULT]
    Unpeg: _Callable[[],
                     _type.HRESULT]


class IReferenceTracker(_Unknwnbase.IUnknown):
    ConnectFromTrackerSource: _Callable[[],
                                        _type.HRESULT]
    DisconnectFromTrackerSource: _Callable[[],
                                           _type.HRESULT]
    FindTrackerTargets: _Callable[[IFindReferenceTargetsCallback],  # callback
                                  _type.HRESULT]
    GetReferenceTrackerManager: _Callable[[_Pointer[IReferenceTrackerManager]],  # value
                                          _type.HRESULT]
    AddRefFromTrackerSource: _Callable[[],
                                       _type.HRESULT]
    ReleaseFromTrackerSource: _Callable[[],
                                        _type.HRESULT]
    PegFromTrackerSource: _Callable[[],
                                    _type.HRESULT]


class IReferenceTrackerManager(_Unknwnbase.IUnknown):
    ReferenceTrackingStarted: _Callable[[],
                                        _type.HRESULT]
    FindTrackerTargetsCompleted: _Callable[[_type.boolean],  # findFailed
                                           _type.HRESULT]
    ReferenceTrackingCompleted: _Callable[[],
                                          _type.HRESULT]
    SetReferenceTrackerHost: _Callable[[IReferenceTrackerHost],  # value
                                       _type.HRESULT]


class IFindReferenceTargetsCallback(_Unknwnbase.IUnknown):
    FoundTrackerTarget: _Callable[[IReferenceTrackerTarget],  # target
                                  _type.HRESULT]


class IReferenceTrackerHost(_Unknwnbase.IUnknown):
    DisconnectUnusedReferenceSources: _Callable[[_enum.XAML_REFERENCETRACKER_DISCONNECT],  # options
                                                _type.HRESULT]
    ReleaseDisconnectedReferenceSources: _Callable[[],
                                                   _type.HRESULT]
    NotifyEndOfReferenceTrackingOnThread: _Callable[[],
                                                    _type.HRESULT]
    GetTrackerTarget: _Callable[[_Unknwnbase.IUnknown,  # unknown
                                 _Pointer[IReferenceTrackerTarget]],  # newReference
                                _type.HRESULT]
    AddMemoryPressure: _Callable[[_type.UINT64],  # bytesAllocated
                                 _type.HRESULT]
    RemoveMemoryPressure: _Callable[[_type.UINT64],  # bytesAllocated
                                    _type.HRESULT]


class IReferenceTrackerExtension(_Unknwnbase.IUnknown):
    pass


class ITrackerOwner(_Unknwnbase.IUnknown):
    CreateTrackerHandle: _Callable[[_Pointer[_Pointer[_struct.TrackerHandle]]],  # returnValue
                                   _type.HRESULT]
    DeleteTrackerHandle: _Callable[[_Pointer[_struct.TrackerHandle]],  # handle
                                   _type.HRESULT]
    SetTrackerValue: _Callable[[_Pointer[_struct.TrackerHandle],  # handle
                                _Unknwnbase.IUnknown],  # value
                               _type.HRESULT]
    TryGetSafeTrackerValue: _Callable[[_Pointer[_struct.TrackerHandle],  # handle
                                       _Pointer[_Unknwnbase.IUnknown]],  # returnValue
                                      _type.boolean]

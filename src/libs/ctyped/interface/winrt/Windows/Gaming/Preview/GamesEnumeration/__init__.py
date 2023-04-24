from __future__ import annotations

from typing import Callable as _Callable

from .... import ApplicationModel as _Windows_ApplicationModel
from .... import Foundation as _Windows_Foundation
from .... import Storage as _Windows_Storage
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ......um import Unknwnbase as _Unknwnbase
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class _IGameListChangedEventHandler:
    Invoke: _Callable[[IGameListEntry],  # game
                      _type.HRESULT]


class IGameListChangedEventHandler(_IGameListChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IGameListChangedEventHandler_impl(_IGameListChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IGameListRemovedEventHandler:
    Invoke: _Callable[[_type.HSTRING],  # identifier
                      _type.HRESULT]


class IGameListRemovedEventHandler(_IGameListRemovedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IGameListRemovedEventHandler_impl(_IGameListRemovedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IGameListEntry(_inspectable.IInspectable):
    get_DisplayInfo: _Callable[[_Pointer[_Windows_ApplicationModel.IAppDisplayInfo]],  # value
                               _type.HRESULT]
    LaunchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                           _type.HRESULT]
    get_Category: _Callable[[_Pointer[_enum.Windows.Gaming.Preview.GamesEnumeration.GameListCategory]],  # value
                            _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    SetCategoryAsync: _Callable[[_enum.Windows.Gaming.Preview.GamesEnumeration.GameListCategory,  # value
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                _type.HRESULT]


class IGameListEntry2(_inspectable.IInspectable):
    get_LaunchableState: _Callable[[_Pointer[_enum.Windows.Gaming.Preview.GamesEnumeration.GameListEntryLaunchableState]],  # value
                                   _type.HRESULT]
    get_LauncherExecutable: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                                      _type.HRESULT]
    get_LaunchParameters: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    SetLauncherExecutableFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # executableFile
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                              _type.HRESULT]
    SetLauncherExecutableFileWithParamsAsync: _Callable[[_Windows_Storage.IStorageFile,  # executableFile
                                                         _type.HSTRING,  # launchParams
                                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                        _type.HRESULT]
    get_TitleId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    SetTitleIdAsync: _Callable[[_type.HSTRING,  # id
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]
    get_GameModeConfiguration: _Callable[[_Pointer[IGameModeConfiguration]],  # value
                                         _type.HRESULT]


class IGameListStatics(_inspectable.IInspectable):
    FindAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IGameListEntry]]]],  # operation
                            _type.HRESULT]
    FindAllAsyncPackageFamilyName: _Callable[[_type.HSTRING,  # packageFamilyName
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IGameListEntry]]]],  # operation
                                             _type.HRESULT]
    add_GameAdded: _Callable[[IGameListChangedEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_GameAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_GameRemoved: _Callable[[IGameListRemovedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_GameRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_GameUpdated: _Callable[[IGameListChangedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_GameUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]

    _factory = True


class IGameListStatics2(_inspectable.IInspectable):
    MergeEntriesAsync: _Callable[[IGameListEntry,  # left
                                  IGameListEntry,  # right
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IGameListEntry]]],  # operation
                                 _type.HRESULT]
    UnmergeEntryAsync: _Callable[[IGameListEntry,  # mergedEntry
                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IGameListEntry]]]],  # operation
                                 _type.HRESULT]

    _factory = True


class IGameModeConfiguration(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_RelatedProcessNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                       _type.HRESULT]
    get_PercentGpuTimeAllocatedToGame: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                                 _type.HRESULT]
    put_PercentGpuTimeAllocatedToGame: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                                 _type.HRESULT]
    get_PercentGpuMemoryAllocatedToGame: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                                   _type.HRESULT]
    put_PercentGpuMemoryAllocatedToGame: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                                   _type.HRESULT]
    get_PercentGpuMemoryAllocatedToSystemCompositor: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                                               _type.HRESULT]
    put_PercentGpuMemoryAllocatedToSystemCompositor: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                                               _type.HRESULT]
    get_MaxCpuCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                               _type.HRESULT]
    put_MaxCpuCount: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                               _type.HRESULT]
    get_CpuExclusivityMaskLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                         _type.HRESULT]
    put_CpuExclusivityMaskLow: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                         _type.HRESULT]
    get_CpuExclusivityMaskHigh: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                          _type.HRESULT]
    put_CpuExclusivityMaskHigh: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                          _type.HRESULT]
    get_AffinitizeToExclusiveCpus: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_AffinitizeToExclusiveCpus: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                         _type.HRESULT]


class IGameModeUserConfiguration(_inspectable.IInspectable):
    get_GamingRelatedProcessNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # processNames
                                             _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                         _type.HRESULT]


class IGameModeUserConfigurationStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[IGameModeUserConfiguration]],  # userConfiguration
                          _type.HRESULT]

    _factory = True

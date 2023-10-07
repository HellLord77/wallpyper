from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Printing as _Windows_Graphics_Printing
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IPrintBindingOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintBorderingOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintCollationOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintColorModeOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintCopiesOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintCustomItemDetails(_inspectable.IInspectable):
    get_ItemId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_ItemDisplayName: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_ItemDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class IPrintCustomItemListOptionDetails(_inspectable.IInspectable):
    AddItem: _Callable[[_type.HSTRING,  # itemId
                        _type.HSTRING],  # displayName
                       _type.HRESULT]


class IPrintCustomItemListOptionDetails2(_inspectable.IInspectable):
    AddItem: _Callable[[_type.HSTRING,  # itemId
                        _type.HSTRING,  # displayName
                        _type.HSTRING,  # description
                        _Windows_Storage_Streams.IRandomAccessStreamWithContentType],  # icon
                       _type.HRESULT]


class IPrintCustomItemListOptionDetails3(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintCustomOptionDetails(_inspectable.IInspectable):
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintCustomTextOptionDetails(_inspectable.IInspectable):
    put_MaxCharacters: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_MaxCharacters: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]


class IPrintCustomTextOptionDetails2(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintCustomToggleOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintDuplexOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintHolePunchOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintItemListOptionDetails(_inspectable.IInspectable):
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_inspectable.IInspectable]]],  # value
                         _type.HRESULT]


class IPrintMediaSizeOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintMediaTypeOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintNumberOptionDetails(_inspectable.IInspectable):
    get_MinValue: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_MaxValue: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]


class IPrintOptionDetails(_inspectable.IInspectable):
    get_OptionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_OptionType: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.OptionDetails.PrintOptionType]],  # value
                              _type.HRESULT]
    put_ErrorText: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_ErrorText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_State: _Callable[[_enum.Windows.Graphics.Printing.OptionDetails.PrintOptionStates],  # value
                         _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.OptionDetails.PrintOptionStates]],  # value
                         _type.HRESULT]
    get_Value: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]
    TrySetValue: _Callable[[_inspectable.IInspectable,  # value
                            _Pointer[_type.boolean]],  # succeeded
                           _type.HRESULT]


class IPrintOrientationOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintPageRangeOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintQualityOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintStapleOptionDetails(_inspectable.IInspectable):
    put_WarningText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_WarningText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintTaskOptionChangedEventArgs(_inspectable.IInspectable):
    get_OptionId: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                            _type.HRESULT]


class IPrintTaskOptionDetails(_inspectable.IInspectable):
    get_Options: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IPrintOptionDetails]]],  # value
                           _type.HRESULT]
    CreateItemListOption: _Callable[[_type.HSTRING,  # optionId
                                     _type.HSTRING,  # displayName
                                     _Pointer[IPrintOptionDetails]],  # itemListOption
                                    _type.HRESULT]
    CreateTextOption: _Callable[[_type.HSTRING,  # optionId
                                 _type.HSTRING,  # displayName
                                 _Pointer[IPrintOptionDetails]],  # textOption
                                _type.HRESULT]
    add_OptionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintTaskOptionDetails, IPrintTaskOptionChangedEventArgs],  # eventHandler
                                  _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                 _type.HRESULT]
    remove_OptionChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                    _type.HRESULT]
    add_BeginValidation: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintTaskOptionDetails, _inspectable.IInspectable],  # eventHandler
                                    _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                   _type.HRESULT]
    remove_BeginValidation: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                      _type.HRESULT]


class IPrintTaskOptionDetails2(_inspectable.IInspectable):
    CreateToggleOption: _Callable[[_type.HSTRING,  # optionId
                                   _type.HSTRING,  # displayName
                                   _Pointer[IPrintOptionDetails]],  # toggleOption
                                  _type.HRESULT]


class IPrintTaskOptionDetailsStatic(_inspectable.IInspectable, factory=True):
    GetFromPrintTaskOptions: _Callable[[_Windows_Graphics_Printing.IPrintTaskOptionsCore,  # printTaskOptions
                                        _Pointer[IPrintTaskOptionDetails]],  # printTaskOptionDetails
                                       _type.HRESULT]


class IPrintTextOptionDetails(_inspectable.IInspectable):
    get_MaxCharacters: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]

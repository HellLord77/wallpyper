from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Payments as _Windows_ApplicationModel_Payments
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IPaymentAppCanMakePaymentTriggerDetails(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[_Windows_ApplicationModel_Payments.IPaymentRequest]],  # result
                           _type.HRESULT]
    ReportCanMakePaymentResult: _Callable[[_Windows_ApplicationModel_Payments.IPaymentCanMakePaymentResult],  # value
                                          _type.HRESULT]


class IPaymentAppManager(_inspectable.IInspectable):
    RegisterAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # supportedPaymentMethodIds
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                             _type.HRESULT]
    UnregisterAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                               _type.HRESULT]


class IPaymentAppManagerStatics(_inspectable.IInspectable):
    get_Current: _Callable[[_Pointer[IPaymentAppManager]],  # value
                           _type.HRESULT]

    _factory = True


class IPaymentTransaction(_inspectable.IInspectable):
    get_PaymentRequest: _Callable[[_Pointer[_Windows_ApplicationModel_Payments.IPaymentRequest]],  # value
                                  _type.HRESULT]
    get_PayerEmail: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_PayerEmail: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_PayerName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_PayerName: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_PayerPhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_PayerPhoneNumber: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    UpdateShippingAddressAsync: _Callable[[_Windows_ApplicationModel_Payments.IPaymentAddress,  # shippingAddress
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_ApplicationModel_Payments.IPaymentRequestChangedResult]]],  # result
                                          _type.HRESULT]
    UpdateSelectedShippingOptionAsync: _Callable[[_Windows_ApplicationModel_Payments.IPaymentShippingOption,  # selectedShippingOption
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_ApplicationModel_Payments.IPaymentRequestChangedResult]]],  # result
                                                 _type.HRESULT]
    AcceptAsync: _Callable[[_Windows_ApplicationModel_Payments.IPaymentToken,  # paymentToken
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPaymentTransactionAcceptResult]]],  # result
                           _type.HRESULT]
    Reject: _Callable[[],
                      _type.HRESULT]


class IPaymentTransactionAcceptResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Payments.PaymentRequestCompletionStatus]],  # value
                          _type.HRESULT]


class IPaymentTransactionStatics(_inspectable.IInspectable):
    FromIdAsync: _Callable[[_type.HSTRING,  # id
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPaymentTransaction]]],  # result
                           _type.HRESULT]

    _factory = True

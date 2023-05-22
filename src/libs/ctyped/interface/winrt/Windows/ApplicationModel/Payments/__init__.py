from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class _IPaymentRequestChangedHandler:
    Invoke: _Callable[[IPaymentRequest,  # paymentRequest
                       IPaymentRequestChangedArgs],  # args
                      _type.HRESULT]


class IPaymentRequestChangedHandler(_IPaymentRequestChangedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IPaymentRequestChangedHandler_impl(_IPaymentRequestChangedHandler, _Unknwnbase.IUnknown_impl):
    pass


class IPaymentAddress(_inspectable.IInspectable):
    get_Country: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Country: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_AddressLines: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                _type.HRESULT]
    put_AddressLines: _Callable[[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Region: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Region: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_City: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_City: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_DependentLocality: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_DependentLocality: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_PostalCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_PostalCode: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_SortingCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_SortingCode: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_LanguageCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_LanguageCode: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_Organization: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_Organization: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_Recipient: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_Recipient: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_PhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_PhoneNumber: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]


class IPaymentCanMakePaymentResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResultStatus]],  # value
                          _type.HRESULT]


class IPaymentCanMakePaymentResultFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResultStatus,  # value
                       _Pointer[IPaymentCanMakePaymentResult]],  # result
                      _type.HRESULT]


class IPaymentCurrencyAmount(_inspectable.IInspectable):
    get_Currency: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Currency: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_CurrencySystem: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_CurrencySystem: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]


class IPaymentCurrencyAmountFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # value
                       _type.HSTRING,  # currency
                       _Pointer[IPaymentCurrencyAmount]],  # result
                      _type.HRESULT]
    CreateWithCurrencySystem: _Callable[[_type.HSTRING,  # value
                                         _type.HSTRING,  # currency
                                         _type.HSTRING,  # currencySystem
                                         _Pointer[IPaymentCurrencyAmount]],  # result
                                        _type.HRESULT]


class IPaymentDetails(_inspectable.IInspectable):
    get_Total: _Callable[[_Pointer[IPaymentItem]],  # value
                         _type.HRESULT]
    put_Total: _Callable[[IPaymentItem],  # value
                         _type.HRESULT]
    get_DisplayItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPaymentItem]]],  # value
                                _type.HRESULT]
    put_DisplayItems: _Callable[[_Windows_Foundation_Collections.IVectorView[IPaymentItem]],  # value
                                _type.HRESULT]
    get_ShippingOptions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPaymentShippingOption]]],  # value
                                   _type.HRESULT]
    put_ShippingOptions: _Callable[[_Windows_Foundation_Collections.IVectorView[IPaymentShippingOption]],  # value
                                   _type.HRESULT]
    get_Modifiers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPaymentDetailsModifier]]],  # value
                             _type.HRESULT]
    put_Modifiers: _Callable[[_Windows_Foundation_Collections.IVectorView[IPaymentDetailsModifier]],  # value
                             _type.HRESULT]


class IPaymentDetailsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IPaymentItem,  # total
                       _Pointer[IPaymentDetails]],  # result
                      _type.HRESULT]
    CreateWithDisplayItems: _Callable[[IPaymentItem,  # total
                                       _Windows_Foundation_Collections.IIterable[IPaymentItem],  # displayItems
                                       _Pointer[IPaymentDetails]],  # result
                                      _type.HRESULT]


class IPaymentDetailsModifier(_inspectable.IInspectable):
    get_JsonData: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_SupportedMethodIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                      _type.HRESULT]
    get_Total: _Callable[[_Pointer[IPaymentItem]],  # value
                         _type.HRESULT]
    get_AdditionalDisplayItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPaymentItem]]],  # value
                                          _type.HRESULT]


class IPaymentDetailsModifierFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # supportedMethodIds
                       IPaymentItem,  # total
                       _Pointer[IPaymentDetailsModifier]],  # result
                      _type.HRESULT]
    CreateWithAdditionalDisplayItems: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # supportedMethodIds
                                                 IPaymentItem,  # total
                                                 _Windows_Foundation_Collections.IIterable[IPaymentItem],  # additionalDisplayItems
                                                 _Pointer[IPaymentDetailsModifier]],  # result
                                                _type.HRESULT]
    CreateWithAdditionalDisplayItemsAndJsonData: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # supportedMethodIds
                                                            IPaymentItem,  # total
                                                            _Windows_Foundation_Collections.IIterable[IPaymentItem],  # additionalDisplayItems
                                                            _type.HSTRING,  # jsonData
                                                            _Pointer[IPaymentDetailsModifier]],  # result
                                                           _type.HRESULT]


class IPaymentItem(_inspectable.IInspectable):
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Label: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Amount: _Callable[[_Pointer[IPaymentCurrencyAmount]],  # value
                          _type.HRESULT]
    put_Amount: _Callable[[IPaymentCurrencyAmount],  # value
                          _type.HRESULT]
    get_Pending: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Pending: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IPaymentItemFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # label
                       IPaymentCurrencyAmount,  # amount
                       _Pointer[IPaymentItem]],  # result
                      _type.HRESULT]


class IPaymentMediator(_inspectable.IInspectable):
    GetSupportedMethodIdsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # result
                                          _type.HRESULT]
    SubmitPaymentRequestAsync: _Callable[[IPaymentRequest,  # paymentRequest
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IPaymentRequestSubmitResult]]],  # result
                                         _type.HRESULT]
    SubmitPaymentRequestWithChangeHandlerAsync: _Callable[[IPaymentRequest,  # paymentRequest
                                                           IPaymentRequestChangedHandler,  # changeHandler
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IPaymentRequestSubmitResult]]],  # result
                                                          _type.HRESULT]


class IPaymentMediator2(_inspectable.IInspectable):
    CanMakePaymentAsync: _Callable[[IPaymentRequest,  # paymentRequest
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IPaymentCanMakePaymentResult]]],  # result
                                   _type.HRESULT]


class IPaymentMerchantInfo(_inspectable.IInspectable):
    get_PackageFullName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]


class IPaymentMerchantInfoFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                       _Pointer[IPaymentMerchantInfo]],  # result
                      _type.HRESULT]


class IPaymentMethodData(_inspectable.IInspectable):
    get_SupportedMethodIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                      _type.HRESULT]
    get_JsonData: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IPaymentMethodDataFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # supportedMethodIds
                       _Pointer[IPaymentMethodData]],  # result
                      _type.HRESULT]
    CreateWithJsonData: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # supportedMethodIds
                                   _type.HSTRING,  # jsonData
                                   _Pointer[IPaymentMethodData]],  # result
                                  _type.HRESULT]


class IPaymentOptions(_inspectable.IInspectable):
    get_RequestPayerEmail: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Payments.PaymentOptionPresence]],  # value
                                     _type.HRESULT]
    put_RequestPayerEmail: _Callable[[_enum.Windows.ApplicationModel.Payments.PaymentOptionPresence],  # value
                                     _type.HRESULT]
    get_RequestPayerName: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Payments.PaymentOptionPresence]],  # value
                                    _type.HRESULT]
    put_RequestPayerName: _Callable[[_enum.Windows.ApplicationModel.Payments.PaymentOptionPresence],  # value
                                    _type.HRESULT]
    get_RequestPayerPhoneNumber: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Payments.PaymentOptionPresence]],  # value
                                           _type.HRESULT]
    put_RequestPayerPhoneNumber: _Callable[[_enum.Windows.ApplicationModel.Payments.PaymentOptionPresence],  # value
                                           _type.HRESULT]
    get_RequestShipping: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_RequestShipping: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_ShippingType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Payments.PaymentShippingType]],  # value
                                _type.HRESULT]
    put_ShippingType: _Callable[[_enum.Windows.ApplicationModel.Payments.PaymentShippingType],  # value
                                _type.HRESULT]


class IPaymentRequest(_inspectable.IInspectable):
    get_MerchantInfo: _Callable[[_Pointer[IPaymentMerchantInfo]],  # value
                                _type.HRESULT]
    get_Details: _Callable[[_Pointer[IPaymentDetails]],  # value
                           _type.HRESULT]
    get_MethodData: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPaymentMethodData]]],  # value
                              _type.HRESULT]
    get_Options: _Callable[[_Pointer[IPaymentOptions]],  # value
                           _type.HRESULT]


class IPaymentRequest2(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]


class IPaymentRequestChangedArgs(_inspectable.IInspectable):
    get_ChangeKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Payments.PaymentRequestChangeKind]],  # value
                              _type.HRESULT]
    get_ShippingAddress: _Callable[[_Pointer[IPaymentAddress]],  # value
                                   _type.HRESULT]
    get_SelectedShippingOption: _Callable[[_Pointer[IPaymentShippingOption]],  # value
                                          _type.HRESULT]
    Acknowledge: _Callable[[IPaymentRequestChangedResult],  # changeResult
                           _type.HRESULT]


class IPaymentRequestChangedResult(_inspectable.IInspectable):
    get_ChangeAcceptedByMerchant: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_ChangeAcceptedByMerchant: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Message: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_UpdatedPaymentDetails: _Callable[[_Pointer[IPaymentDetails]],  # value
                                         _type.HRESULT]
    put_UpdatedPaymentDetails: _Callable[[IPaymentDetails],  # value
                                         _type.HRESULT]


class IPaymentRequestChangedResultFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.boolean,  # changeAcceptedByMerchant
                       _Pointer[IPaymentRequestChangedResult]],  # result
                      _type.HRESULT]
    CreateWithPaymentDetails: _Callable[[_type.boolean,  # changeAcceptedByMerchant
                                         IPaymentDetails,  # updatedPaymentDetails
                                         _Pointer[IPaymentRequestChangedResult]],  # result
                                        _type.HRESULT]


class IPaymentRequestFactory(_inspectable.IInspectable):
    Create: _Callable[[IPaymentDetails,  # details
                       _Windows_Foundation_Collections.IIterable[IPaymentMethodData],  # methodData
                       _Pointer[IPaymentRequest]],  # result
                      _type.HRESULT]
    CreateWithMerchantInfo: _Callable[[IPaymentDetails,  # details
                                       _Windows_Foundation_Collections.IIterable[IPaymentMethodData],  # methodData
                                       IPaymentMerchantInfo,  # merchantInfo
                                       _Pointer[IPaymentRequest]],  # result
                                      _type.HRESULT]
    CreateWithMerchantInfoAndOptions: _Callable[[IPaymentDetails,  # details
                                                 _Windows_Foundation_Collections.IIterable[IPaymentMethodData],  # methodData
                                                 IPaymentMerchantInfo,  # merchantInfo
                                                 IPaymentOptions,  # options
                                                 _Pointer[IPaymentRequest]],  # result
                                                _type.HRESULT]


class IPaymentRequestFactory2(_inspectable.IInspectable, factory=True):
    CreateWithMerchantInfoOptionsAndId: _Callable[[IPaymentDetails,  # details
                                                   _Windows_Foundation_Collections.IIterable[IPaymentMethodData],  # methodData
                                                   IPaymentMerchantInfo,  # merchantInfo
                                                   IPaymentOptions,  # options
                                                   _type.HSTRING,  # id
                                                   _Pointer[IPaymentRequest]],  # result
                                                  _type.HRESULT]


class IPaymentRequestSubmitResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Payments.PaymentRequestStatus]],  # value
                          _type.HRESULT]
    get_Response: _Callable[[_Pointer[IPaymentResponse]],  # value
                            _type.HRESULT]


class IPaymentResponse(_inspectable.IInspectable):
    get_PaymentToken: _Callable[[_Pointer[IPaymentToken]],  # value
                                _type.HRESULT]
    get_ShippingOption: _Callable[[_Pointer[IPaymentShippingOption]],  # value
                                  _type.HRESULT]
    get_ShippingAddress: _Callable[[_Pointer[IPaymentAddress]],  # value
                                   _type.HRESULT]
    get_PayerEmail: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_PayerName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_PayerPhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    CompleteAsync: _Callable[[_enum.Windows.ApplicationModel.Payments.PaymentRequestCompletionStatus,  # status
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                             _type.HRESULT]


class IPaymentShippingOption(_inspectable.IInspectable):
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Label: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Amount: _Callable[[_Pointer[IPaymentCurrencyAmount]],  # value
                          _type.HRESULT]
    put_Amount: _Callable[[IPaymentCurrencyAmount],  # value
                          _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    put_Tag: _Callable[[_type.HSTRING],  # value
                       _type.HRESULT]
    get_IsSelected: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsSelected: _Callable[[_type.boolean],  # value
                              _type.HRESULT]


class IPaymentShippingOptionFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # label
                       IPaymentCurrencyAmount,  # amount
                       _Pointer[IPaymentShippingOption]],  # result
                      _type.HRESULT]
    CreateWithSelected: _Callable[[_type.HSTRING,  # label
                                   IPaymentCurrencyAmount,  # amount
                                   _type.boolean,  # selected
                                   _Pointer[IPaymentShippingOption]],  # result
                                  _type.HRESULT]
    CreateWithSelectedAndTag: _Callable[[_type.HSTRING,  # label
                                         IPaymentCurrencyAmount,  # amount
                                         _type.boolean,  # selected
                                         _type.HSTRING,  # tag
                                         _Pointer[IPaymentShippingOption]],  # result
                                        _type.HRESULT]


class IPaymentToken(_inspectable.IInspectable):
    get_PaymentMethodId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_JsonDetails: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPaymentTokenFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # paymentMethodId
                       _Pointer[IPaymentToken]],  # result
                      _type.HRESULT]
    CreateWithJsonDetails: _Callable[[_type.HSTRING,  # paymentMethodId
                                      _type.HSTRING,  # jsonDetails
                                      _Pointer[IPaymentToken]],  # result
                                     _type.HRESULT]

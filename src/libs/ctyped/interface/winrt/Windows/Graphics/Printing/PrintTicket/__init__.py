from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Data.Xml import Dom as _Windows_Data_Xml_Dom
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IPrintTicketCapabilities(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_XmlNamespace: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_XmlNode: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlNode]],  # value
                           _type.HRESULT]
    get_DocumentBindingFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                          _type.HRESULT]
    get_DocumentCollateFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                          _type.HRESULT]
    get_DocumentDuplexFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                         _type.HRESULT]
    get_DocumentHolePunchFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                            _type.HRESULT]
    get_DocumentInputBinFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                           _type.HRESULT]
    get_DocumentNUpFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                      _type.HRESULT]
    get_DocumentStapleFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                         _type.HRESULT]
    get_JobPasscodeFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                      _type.HRESULT]
    get_PageBorderlessFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                         _type.HRESULT]
    get_PageMediaSizeFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                        _type.HRESULT]
    get_PageMediaTypeFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                        _type.HRESULT]
    get_PageOrientationFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                          _type.HRESULT]
    get_PageOutputColorFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                          _type.HRESULT]
    get_PageOutputQualityFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                            _type.HRESULT]
    get_PageResolutionFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                         _type.HRESULT]
    GetFeature: _Callable[[_type.HSTRING,  # name
                           _type.HSTRING,  # xmlNamespace
                           _Pointer[IPrintTicketFeature]],  # result
                          _type.HRESULT]
    GetParameterDefinition: _Callable[[_type.HSTRING,  # name
                                       _type.HSTRING,  # xmlNamespace
                                       _Pointer[IPrintTicketParameterDefinition]],  # result
                                      _type.HRESULT]


class IPrintTicketFeature(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_XmlNamespace: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_XmlNode: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlNode]],  # value
                           _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    GetOption: _Callable[[_type.HSTRING,  # name
                          _type.HSTRING,  # xmlNamespace
                          _Pointer[IPrintTicketOption]],  # result
                         _type.HRESULT]
    get_Options: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPrintTicketOption]]],  # result
                           _type.HRESULT]
    GetSelectedOption: _Callable[[_Pointer[IPrintTicketOption]],  # value
                                 _type.HRESULT]
    SetSelectedOption: _Callable[[IPrintTicketOption],  # value
                                 _type.HRESULT]
    get_SelectionType: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintTicket.PrintTicketFeatureSelectionType]],  # value
                                 _type.HRESULT]


class IPrintTicketOption(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_XmlNamespace: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_XmlNode: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlNode]],  # value
                           _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    GetPropertyNode: _Callable[[_type.HSTRING,  # name
                                _type.HSTRING,  # xmlNamespace
                                _Pointer[_Windows_Data_Xml_Dom.IXmlNode]],  # result
                               _type.HRESULT]
    GetScoredPropertyNode: _Callable[[_type.HSTRING,  # name
                                      _type.HSTRING,  # xmlNamespace
                                      _Pointer[_Windows_Data_Xml_Dom.IXmlNode]],  # result
                                     _type.HRESULT]
    GetPropertyValue: _Callable[[_type.HSTRING,  # name
                                 _type.HSTRING,  # xmlNamespace
                                 _Pointer[IPrintTicketValue]],  # result
                                _type.HRESULT]
    GetScoredPropertyValue: _Callable[[_type.HSTRING,  # name
                                       _type.HSTRING,  # xmlNamespace
                                       _Pointer[IPrintTicketValue]],  # result
                                      _type.HRESULT]


class IPrintTicketParameterDefinition(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_XmlNamespace: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_XmlNode: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlNode]],  # value
                           _type.HRESULT]
    get_DataType: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintTicket.PrintTicketParameterDataType]],  # value
                            _type.HRESULT]
    get_UnitType: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_RangeMin: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_RangeMax: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]


class IPrintTicketParameterInitializer(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_XmlNamespace: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_XmlNode: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlNode]],  # value
                           _type.HRESULT]
    put_Value: _Callable[[IPrintTicketValue],  # value
                         _type.HRESULT]
    get_Value: _Callable[[_Pointer[IPrintTicketValue]],  # value
                         _type.HRESULT]


class IPrintTicketValue(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintTicket.PrintTicketValueType]],  # value
                        _type.HRESULT]
    GetValueAsInteger: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    GetValueAsString: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IWorkflowPrintTicket(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_XmlNamespace: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_XmlNode: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlNode]],  # value
                           _type.HRESULT]
    GetCapabilities: _Callable[[_Pointer[IPrintTicketCapabilities]],  # result
                               _type.HRESULT]
    get_DocumentBindingFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                          _type.HRESULT]
    get_DocumentCollateFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                          _type.HRESULT]
    get_DocumentDuplexFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                         _type.HRESULT]
    get_DocumentHolePunchFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                            _type.HRESULT]
    get_DocumentInputBinFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                           _type.HRESULT]
    get_DocumentNUpFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                      _type.HRESULT]
    get_DocumentStapleFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                         _type.HRESULT]
    get_JobPasscodeFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                      _type.HRESULT]
    get_PageBorderlessFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                         _type.HRESULT]
    get_PageMediaSizeFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                        _type.HRESULT]
    get_PageMediaTypeFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                        _type.HRESULT]
    get_PageOrientationFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                          _type.HRESULT]
    get_PageOutputColorFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                          _type.HRESULT]
    get_PageOutputQualityFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                            _type.HRESULT]
    get_PageResolutionFeature: _Callable[[_Pointer[IPrintTicketFeature]],  # value
                                         _type.HRESULT]
    GetFeature: _Callable[[_type.HSTRING,  # name
                           _type.HSTRING,  # xmlNamespace
                           _Pointer[IPrintTicketFeature]],  # result
                          _type.HRESULT]
    NotifyXmlChangedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                     _type.HRESULT]
    ValidateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IWorkflowPrintTicketValidationResult]]],  # operation
                             _type.HRESULT]
    GetParameterInitializer: _Callable[[_type.HSTRING,  # name
                                        _type.HSTRING,  # xmlNamespace
                                        _Pointer[IPrintTicketParameterInitializer]],  # result
                                       _type.HRESULT]
    SetParameterInitializerAsInteger: _Callable[[_type.HSTRING,  # name
                                                 _type.HSTRING,  # xmlNamespace
                                                 _type.INT32,  # integerValue
                                                 _Pointer[IPrintTicketParameterInitializer]],  # result
                                                _type.HRESULT]
    SetParameterInitializerAsString: _Callable[[_type.HSTRING,  # name
                                                _type.HSTRING,  # xmlNamespace
                                                _type.HSTRING,  # stringValue
                                                _Pointer[IPrintTicketParameterInitializer]],  # result
                                               _type.HRESULT]
    MergeAndValidateTicket: _Callable[[IWorkflowPrintTicket,  # deltaShemaTicket
                                       _Pointer[IWorkflowPrintTicket]],  # result
                                      _type.HRESULT]


class IWorkflowPrintTicketValidationResult(_inspectable.IInspectable):
    get_Validated: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]

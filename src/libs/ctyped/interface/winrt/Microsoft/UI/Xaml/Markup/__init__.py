from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Xaml as _Microsoft_UI_Xaml
from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from .....Windows.Foundation import Collections as _Windows_Foundation_Collections
from .....Windows.Storage import Streams as _Windows_Storage_Streams
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IComponentConnector(_inspectable.IInspectable):
    Connect: _Callable[[_type.INT32,  # connectionId
                        _inspectable.IInspectable],  # target
                       _type.HRESULT]
    GetBindingConnector: _Callable[[_type.INT32,  # connectionId
                                    _inspectable.IInspectable,  # target
                                    _Pointer[IComponentConnector]],  # result
                                   _type.HRESULT]


class IDataTemplateComponent(_inspectable.IInspectable):
    Recycle: _Callable[[],
                       _type.HRESULT]
    ProcessBindings: _Callable[[_inspectable.IInspectable,  # item
                                _type.INT32,  # itemIndex
                                _type.INT32,  # phase
                                _Pointer[_type.INT32]],  # nextPhase
                               _type.HRESULT]


class IMarkupExtension(_inspectable.IInspectable):
    pass


class IMarkupExtensionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMarkupExtension]],  # value
                              _type.HRESULT]


class IMarkupExtensionOverrides(_inspectable.IInspectable):
    ProvideValue: _Callable[[_Pointer[_inspectable.IInspectable]],  # result
                            _type.HRESULT]
    ProvideValueWithIXamlServiceProvider: _Callable[[_Microsoft_UI_Xaml.IXamlServiceProvider,  # serviceProvider
                                                     _Pointer[_inspectable.IInspectable]],  # result
                                                    _type.HRESULT]


class IProvideValueTarget(_inspectable.IInspectable):
    get_TargetObject: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                _type.HRESULT]
    get_TargetProperty: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                  _type.HRESULT]


class IProvideValueTargetProperty(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Type: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                        _type.HRESULT]
    get_DeclaringType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                                 _type.HRESULT]


class IRootObjectProvider(_inspectable.IInspectable):
    get_RootObject: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                              _type.HRESULT]


class IUriContext(_inspectable.IInspectable):
    get_BaseUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]


class IXamlBinaryWriter(_inspectable.IInspectable):
    pass


class IXamlBinaryWriterStatics(_inspectable.IInspectable, factory=True):
    Write: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_Storage_Streams.IRandomAccessStream],  # inputStreams
                      _Windows_Foundation_Collections.IVector[_Windows_Storage_Streams.IRandomAccessStream],  # outputStreams
                      IXamlMetadataProvider,  # xamlMetadataProvider
                      _Pointer[_struct.Microsoft.UI.Xaml.Markup.XamlBinaryWriterErrorInformation]],  # result
                     _type.HRESULT]


class IXamlBindScopeDiagnostics(_inspectable.IInspectable):
    Disable: _Callable[[_type.INT32,  # lineNumber
                        _type.INT32],  # columnNumber
                       _type.HRESULT]


class IXamlBindingHelper(_inspectable.IInspectable):
    pass


class IXamlBindingHelperStatics(_inspectable.IInspectable, factory=True):
    get_DataTemplateComponentProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    GetDataTemplateComponent: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                         _Pointer[IDataTemplateComponent]],  # result
                                        _type.HRESULT]
    SetDataTemplateComponent: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                         IDataTemplateComponent],  # value
                                        _type.HRESULT]
    SuspendRendering: _Callable[[_Microsoft_UI_Xaml.IUIElement],  # target
                                _type.HRESULT]
    ResumeRendering: _Callable[[_Microsoft_UI_Xaml.IUIElement],  # target
                               _type.HRESULT]
    ConvertValue: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,  # type
                             _inspectable.IInspectable,  # value
                             _Pointer[_inspectable.IInspectable]],  # result
                            _type.HRESULT]
    SetPropertyFromString: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                      _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                      _type.HSTRING],  # value
                                     _type.HRESULT]
    SetPropertyFromBoolean: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                       _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                       _type.boolean],  # value
                                      _type.HRESULT]
    SetPropertyFromChar16: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                      _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                      _type.WCHAR],  # value
                                     _type.HRESULT]
    SetPropertyFromDateTime: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                        _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                        _struct.Windows.Foundation.DateTime],  # value
                                       _type.HRESULT]
    SetPropertyFromDouble: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                      _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                      _type.DOUBLE],  # value
                                     _type.HRESULT]
    SetPropertyFromInt32: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                     _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                     _type.INT32],  # value
                                    _type.HRESULT]
    SetPropertyFromUInt32: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                      _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                      _type.UINT32],  # value
                                     _type.HRESULT]
    SetPropertyFromInt64: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                     _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                     _type.INT64],  # value
                                    _type.HRESULT]
    SetPropertyFromUInt64: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                      _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                      _type.UINT64],  # value
                                     _type.HRESULT]
    SetPropertyFromSingle: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                      _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                      _type.FLOAT],  # value
                                     _type.HRESULT]
    SetPropertyFromPoint: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                     _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                     _struct.Windows.Foundation.Point],  # value
                                    _type.HRESULT]
    SetPropertyFromRect: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                    _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                    _struct.Windows.Foundation.Rect],  # value
                                   _type.HRESULT]
    SetPropertyFromSize: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                    _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                    _struct.Windows.Foundation.Size],  # value
                                   _type.HRESULT]
    SetPropertyFromTimeSpan: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                        _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                        _struct.Windows.Foundation.TimeSpan],  # value
                                       _type.HRESULT]
    SetPropertyFromByte: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                    _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                    _type.BYTE],  # value
                                   _type.HRESULT]
    SetPropertyFromUri: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                   _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                   _Windows_Foundation.IUriRuntimeClass],  # value
                                  _type.HRESULT]
    SetPropertyFromObject: _Callable[[_inspectable.IInspectable,  # dependencyObject
                                      _Microsoft_UI_Xaml.IDependencyProperty,  # propertyToSet
                                      _inspectable.IInspectable],  # value
                                     _type.HRESULT]


class IXamlMarkupHelper(_inspectable.IInspectable):
    pass


class IXamlMarkupHelperStatics(_inspectable.IInspectable, factory=True):
    UnloadObject: _Callable[[_Microsoft_UI_Xaml.IDependencyObject],  # element
                            _type.HRESULT]


class IXamlMember(_inspectable.IInspectable):
    get_IsAttachable: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_IsDependencyProperty: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_TargetType: _Callable[[_Pointer[IXamlType]],  # value
                              _type.HRESULT]
    get_Type: _Callable[[_Pointer[IXamlType]],  # value
                        _type.HRESULT]
    GetValue: _Callable[[_inspectable.IInspectable,  # instance
                         _Pointer[_inspectable.IInspectable]],  # result
                        _type.HRESULT]
    SetValue: _Callable[[_inspectable.IInspectable,  # instance
                         _inspectable.IInspectable],  # value
                        _type.HRESULT]


class IXamlMetadataProvider(_inspectable.IInspectable):
    GetXamlType: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,  # type
                            _Pointer[IXamlType]],  # result
                           _type.HRESULT]
    GetXamlTypeByFullName: _Callable[[_type.HSTRING,  # fullName
                                      _Pointer[IXamlType]],  # result
                                     _type.HRESULT]
    GetXmlnsDefinitions: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                                    _Pointer[_Pointer[_struct.Microsoft.UI.Xaml.Markup.XmlnsDefinition]]],  # result
                                   _type.HRESULT]


class IXamlReader(_inspectable.IInspectable):
    pass


class IXamlReaderStatics(_inspectable.IInspectable, factory=True):
    Load: _Callable[[_type.HSTRING,  # xaml
                     _Pointer[_inspectable.IInspectable]],  # result
                    _type.HRESULT]
    LoadWithInitialTemplateValidation: _Callable[[_type.HSTRING,  # xaml
                                                  _Pointer[_inspectable.IInspectable]],  # result
                                                 _type.HRESULT]


class IXamlType(_inspectable.IInspectable):
    get_BaseType: _Callable[[_Pointer[IXamlType]],  # value
                            _type.HRESULT]
    get_ContentProperty: _Callable[[_Pointer[IXamlMember]],  # value
                                   _type.HRESULT]
    get_FullName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_IsArray: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_IsCollection: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_IsConstructible: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsDictionary: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_IsMarkupExtension: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsBindable: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_ItemType: _Callable[[_Pointer[IXamlType]],  # value
                            _type.HRESULT]
    get_KeyType: _Callable[[_Pointer[IXamlType]],  # value
                           _type.HRESULT]
    get_BoxedType: _Callable[[_Pointer[IXamlType]],  # value
                             _type.HRESULT]
    get_UnderlyingType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                                  _type.HRESULT]
    ActivateInstance: _Callable[[_Pointer[_inspectable.IInspectable]],  # result
                                _type.HRESULT]
    CreateFromString: _Callable[[_type.HSTRING,  # value
                                 _Pointer[_inspectable.IInspectable]],  # result
                                _type.HRESULT]
    GetMember: _Callable[[_type.HSTRING,  # name
                          _Pointer[IXamlMember]],  # result
                         _type.HRESULT]
    AddToVector: _Callable[[_inspectable.IInspectable,  # instance
                            _inspectable.IInspectable],  # value
                           _type.HRESULT]
    AddToMap: _Callable[[_inspectable.IInspectable,  # instance
                         _inspectable.IInspectable,  # key
                         _inspectable.IInspectable],  # value
                        _type.HRESULT]
    RunInitializer: _Callable[[],
                              _type.HRESULT]


class IXamlTypeResolver(_inspectable.IInspectable):
    Resolve: _Callable[[_type.HSTRING,  # qualifiedTypeName
                        _Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # result
                       _type.HRESULT]

from __future__ import annotations as _

from typing import Callable as _Callable

from ..um import Unknwnbase as _Unknwnbase
from ..um import oaidl as _oaidl
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IMetaDataDispenser(_Unknwnbase.IUnknown):
    DefineScope: _Callable[[_Pointer[_struct.IID],  # rclsid
                            _type.DWORD,  # dwCreateFlags
                            _Pointer[_struct.IID],  # riid
                            _Pointer[_Unknwnbase.IUnknown]],  # ppIUnk
                           _type.HRESULT]
    OpenScope: _Callable[[_type.LPCWSTR,  # szScope
                          _type.DWORD,  # dwOpenFlags
                          _Pointer[_struct.IID],  # riid
                          _Pointer[_Unknwnbase.IUnknown]],  # ppIUnk
                         _type.HRESULT]
    OpenScopeOnMemory: _Callable[[_Pointer[_type.BYTE],  # pData
                                  _type.ULONG,  # cbData
                                  _type.DWORD,  # dwOpenFlags
                                  _Pointer[_struct.IID],  # riid
                                  _Pointer[_Unknwnbase.IUnknown]],  # ppIUnk
                                 _type.HRESULT]


class IMetaDataDispenserEx(IMetaDataDispenser):
    SetOption: _Callable[[_Pointer[_struct.GUID],  # optionId
                          _Pointer[_struct.VARIANT]],  # pValue
                         _type.HRESULT]
    GetOption: _Callable[[_Pointer[_struct.GUID],  # optionId
                          _Pointer[_struct.VARIANT]],  # pValue
                         _type.HRESULT]
    OpenScopeOnITypeInfo: _Callable[[_oaidl.ITypeInfo,  # pITI
                                     _type.DWORD,  # dwOpenFlags
                                     _Pointer[_struct.IID],  # riid
                                     _Pointer[_Unknwnbase.IUnknown]],  # ppIUnk
                                    _type.HRESULT]
    GetCORSystemDirectory: _Callable[[_type.LPWSTR,  # szBuffer
                                      _type.DWORD,  # cchBuffer
                                      _Pointer[_type.DWORD]],  # pchBuffer
                                     _type.HRESULT]
    FindAssembly: _Callable[[_type.LPCWSTR,  # szAppBase
                             _type.LPCWSTR,  # szPrivateBin
                             _type.LPCWSTR,  # szGlobalBin
                             _type.LPCWSTR,  # szAssemblyName
                             _type.LPWSTR,  # szName
                             _type.ULONG,  # cchName
                             _Pointer[_type.ULONG]],  # pchName
                            _type.HRESULT]
    FindAssemblyModule: _Callable[[_type.LPCWSTR,  # szAppBase
                                   _type.LPCWSTR,  # szPrivateBin
                                   _type.LPCWSTR,  # szGlobalBin
                                   _type.LPCWSTR,  # szAssemblyName
                                   _type.LPCWSTR,  # szModuleName
                                   _type.LPWSTR,  # szName
                                   _type.ULONG,  # cchName
                                   _Pointer[_type.ULONG]],  # pcName
                                  _type.HRESULT]


class IMetaDataAssemblyImport(_Unknwnbase.IUnknown):
    GetAssemblyProps: _Callable[[_type.mdAssembly,  # mda
                                 _Pointer[_Pointer[_type.BYTE]],  # ppbPublicKey
                                 _Pointer[_type.ULONG],  # pcbPublicKey
                                 _Pointer[_type.ULONG],  # pulHashAlgId
                                 _type.LPWSTR,  # szName
                                 _type.ULONG,  # cchName
                                 _Pointer[_type.ULONG],  # pchName
                                 _Pointer[_struct.ASSEMBLYMETADATA],  # pMetaData
                                 _Pointer[_type.DWORD]],  # pdwAssemblyFlags
                                _type.HRESULT]
    GetAssemblyRefProps: _Callable[[_type.mdAssemblyRef,  # mdar
                                    _Pointer[_Pointer[_type.BYTE]],  # ppbPublicKeyOrToken
                                    _Pointer[_type.ULONG],  # pcbPublicKeyOrToken
                                    _type.LPWSTR,  # szName
                                    _type.ULONG,  # cchName
                                    _Pointer[_type.ULONG],  # pchName
                                    _Pointer[_struct.ASSEMBLYMETADATA],  # pMetaData
                                    _Pointer[_Pointer[_type.BYTE]],  # ppbHashValue
                                    _Pointer[_type.ULONG],  # pcbHashValue
                                    _Pointer[_type.DWORD]],  # pdwAssemblyRefFlags
                                   _type.HRESULT]
    GetFileProps: _Callable[[_type.mdFile,  # mdf
                             _type.LPWSTR,  # szName
                             _type.ULONG,  # cchName
                             _Pointer[_type.ULONG],  # pchName
                             _Pointer[_Pointer[_type.BYTE]],  # ppbHashValue
                             _Pointer[_type.ULONG],  # pcbHashValue
                             _Pointer[_type.DWORD]],  # pdwFileFlags
                            _type.HRESULT]
    GetExportedTypeProps: _Callable[[_type.mdExportedType,  # mdct
                                     _type.LPWSTR,  # szName
                                     _type.ULONG,  # cchName
                                     _Pointer[_type.ULONG],  # pchName
                                     _Pointer[_type.mdToken],  # ptkImplementation
                                     _Pointer[_type.mdTypeDef],  # ptkTypeDef
                                     _Pointer[_type.DWORD]],  # pdwExportedTypeFlags
                                    _type.HRESULT]
    GetManifestResourceProps: _Callable[[_type.mdManifestResource,  # mdmr
                                         _type.LPWSTR,  # szName
                                         _type.ULONG,  # cchName
                                         _Pointer[_type.ULONG],  # pchName
                                         _Pointer[_type.mdToken],  # ptkImplementation
                                         _Pointer[_type.DWORD],  # pdwOffset
                                         _Pointer[_type.DWORD]],  # pdwResourceFlags
                                        _type.HRESULT]
    EnumAssemblyRefs: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                 _Pointer[_type.mdAssemblyRef],  # rAssemblyRefs
                                 _type.ULONG,  # cMax
                                 _Pointer[_type.ULONG]],  # pcTokens
                                _type.HRESULT]
    EnumFiles: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                          _Pointer[_type.mdFile],  # rFiles
                          _type.ULONG,  # cMax
                          _Pointer[_type.ULONG]],  # pcTokens
                         _type.HRESULT]
    EnumExportedTypes: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                  _Pointer[_type.mdExportedType],  # rExportedTypes
                                  _type.ULONG,  # cMax
                                  _Pointer[_type.ULONG]],  # pcTokens
                                 _type.HRESULT]
    EnumManifestResources: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                      _Pointer[_type.mdManifestResource],  # rManifestResources
                                      _type.ULONG,  # cMax
                                      _Pointer[_type.ULONG]],  # pcTokens
                                     _type.HRESULT]
    GetAssemblyFromScope: _Callable[[_Pointer[_type.mdAssembly]],  # ptkAssembly
                                    _type.HRESULT]
    FindExportedTypeByName: _Callable[[_type.LPCWSTR,  # szName
                                       _type.mdToken,  # mdtExportedType
                                       _Pointer[_type.mdExportedType]],  # ptkExportedType
                                      _type.HRESULT]
    FindManifestResourceByName: _Callable[[_type.LPCWSTR,  # szName
                                           _Pointer[_type.mdManifestResource]],  # ptkManifestResource
                                          _type.HRESULT]
    CloseEnum: _Callable[[_type.HCORENUM],  # hEnum
                         _type.c_void]
    FindAssembliesByName: _Callable[[_type.LPCWSTR,  # szAppBase
                                     _type.LPCWSTR,  # szPrivateBin
                                     _type.LPCWSTR,  # szAssemblyName
                                     _Pointer[_Unknwnbase.IUnknown],  # ppIUnk
                                     _type.ULONG,  # cMax
                                     _Pointer[_type.ULONG]],  # pcAssemblies
                                    _type.HRESULT]


class IMetaDataImport(_Unknwnbase.IUnknown):
    CloseEnum: _Callable[[_type.HCORENUM],  # hEnum
                         _type.c_void]
    CountEnum: _Callable[[_type.HCORENUM,  # hEnum
                          _Pointer[_type.ULONG]],  # pulCount
                         _type.HRESULT]
    ResetEnum: _Callable[[_type.HCORENUM,  # hEnum
                          _type.ULONG],  # ulPos
                         _type.HRESULT]
    EnumTypeDefs: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                             _Pointer[_type.mdTypeDef],  # rgTypeDefs
                             _type.ULONG,  # cMax
                             _Pointer[_type.ULONG]],  # pcTypeDefs
                            _type.HRESULT]
    EnumInterfaceImpls: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                   _type.mdTypeDef,  # td
                                   _Pointer[_type.mdInterfaceImpl],  # rImpls
                                   _type.ULONG,  # cMax
                                   _Pointer[_type.ULONG]],  # pcImpls
                                  _type.HRESULT]
    EnumTypeRefs: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                             _Pointer[_type.mdTypeRef],  # rgTypeRefs
                             _type.ULONG,  # cMax
                             _Pointer[_type.ULONG]],  # pcTypeRefs
                            _type.HRESULT]
    FindTypeDefByName: _Callable[[_type.LPCWSTR,  # szTypeDef
                                  _type.mdToken,  # tkEnclosingClass
                                  _Pointer[_type.mdTypeDef]],  # ptkTypeDef
                                 _type.HRESULT]
    GetScopeProps: _Callable[[_type.LPWSTR,  # szName
                              _type.ULONG,  # cchName
                              _Pointer[_type.ULONG],  # pchName
                              _Pointer[_struct.GUID]],  # pmvid
                             _type.HRESULT]
    GetModuleFromScope: _Callable[[_Pointer[_type.mdModule]],  # ptkModule
                                  _type.HRESULT]
    GetTypeDefProps: _Callable[[_type.mdTypeDef,  # tkTypeDef
                                _type.LPWSTR,  # szTypeDef
                                _type.ULONG,  # cchTypeDef
                                _Pointer[_type.ULONG],  # pchTypeDef
                                _Pointer[_type.DWORD],  # pdwTypeDefFlags
                                _Pointer[_type.mdToken]],  # ptkExtends
                               _type.HRESULT]
    GetInterfaceImplProps: _Callable[[_type.mdInterfaceImpl,  # tkInterfaceImpl
                                      _Pointer[_type.mdTypeDef],  # ptkClass
                                      _Pointer[_type.mdToken]],  # ptkIface
                                     _type.HRESULT]
    GetTypeRefProps: _Callable[[_type.mdTypeRef,  # tkTypeRef
                                _Pointer[_type.mdToken],  # ptkResolutionScope
                                _type.LPWSTR,  # szName
                                _type.ULONG,  # cchName
                                _Pointer[_type.ULONG]],  # pchName
                               _type.HRESULT]
    ResolveTypeRef: _Callable[[_type.mdTypeRef,  # tkTypeRef
                               _Pointer[_struct.IID],  # riid
                               _Pointer[_Unknwnbase.IUnknown],  # ppIScope
                               _Pointer[_type.mdTypeDef]],  # ptkTypeDef
                              _type.HRESULT]
    EnumMembers: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                            _type.mdTypeDef,  # tkTypeDef
                            _Pointer[_type.mdToken],  # rgMembers
                            _type.ULONG,  # cMax
                            _Pointer[_type.ULONG]],  # pcTokens
                           _type.HRESULT]
    EnumMembersWithName: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                    _type.mdTypeDef,  # tkTypeDef
                                    _type.LPCWSTR,  # szName
                                    _Pointer[_type.mdToken],  # rgMembers
                                    _type.ULONG,  # cMax
                                    _Pointer[_type.ULONG]],  # pcTokens
                                   _type.HRESULT]
    EnumMethods: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                            _type.mdTypeDef,  # tkTypeDef
                            _Pointer[_type.mdMethodDef],  # rgMethods
                            _type.ULONG,  # cMax
                            _Pointer[_type.ULONG]],  # pcTokens
                           _type.HRESULT]
    EnumMethodsWithName: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                    _type.mdTypeDef,  # tkTypeDef
                                    _type.LPCWSTR,  # szName
                                    _Pointer[_type.mdMethodDef],  # rgMethods
                                    _type.ULONG,  # cMax
                                    _Pointer[_type.ULONG]],  # pcTokens
                                   _type.HRESULT]
    EnumFields: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                           _type.mdTypeDef,  # tkTypeDef
                           _Pointer[_type.mdFieldDef],  # rgFields
                           _type.ULONG,  # cMax
                           _Pointer[_type.ULONG]],  # pcTokens
                          _type.HRESULT]
    EnumFieldsWithName: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                   _type.mdTypeDef,  # tkTypeDef
                                   _type.LPCWSTR,  # szName
                                   _Pointer[_type.mdFieldDef],  # rFields
                                   _type.ULONG,  # cMax
                                   _Pointer[_type.ULONG]],  # pcTokens
                                  _type.HRESULT]
    EnumParams: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                           _type.mdMethodDef,  # tkMethodDef
                           _Pointer[_type.mdParamDef],  # rParams
                           _type.ULONG,  # cMax
                           _Pointer[_type.ULONG]],  # pcTokens
                          _type.HRESULT]
    EnumMemberRefs: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                               _type.mdToken,  # tkParent
                               _Pointer[_type.mdMemberRef],  # rgMemberRefs
                               _type.ULONG,  # cMax
                               _Pointer[_type.ULONG]],  # pcTokens
                              _type.HRESULT]
    EnumMethodImpls: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                _type.mdTypeDef,  # tkTypeDef
                                _Pointer[_type.mdToken],  # rMethodBody
                                _Pointer[_type.mdToken],  # rMethodDecl
                                _type.ULONG,  # cMax
                                _Pointer[_type.ULONG]],  # pcTokens
                               _type.HRESULT]
    EnumPermissionSets: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                   _type.mdToken,  # tk
                                   _type.DWORD,  # dwActions
                                   _Pointer[_type.mdPermission],  # rPermission
                                   _type.ULONG,  # cMax
                                   _Pointer[_type.ULONG]],  # pcTokens
                                  _type.HRESULT]
    FindMember: _Callable[[_type.mdTypeDef,  # tkTypeDef
                           _type.LPCWSTR,  # szName
                           _Pointer[_type.COR_SIGNATURE],  # pvSigBlob
                           _type.ULONG,  # cbSigBlob
                           _Pointer[_type.mdToken]],  # pmb
                          _type.HRESULT]
    FindMethod: _Callable[[_type.mdTypeDef,  # tkTypeDef
                           _type.LPCWSTR,  # szName
                           _Pointer[_type.COR_SIGNATURE],  # pvSigBlob
                           _type.ULONG,  # cbSigBlob
                           _Pointer[_type.mdMethodDef]],  # ptkMethodDef
                          _type.HRESULT]
    FindField: _Callable[[_type.mdTypeDef,  # tkTypeDef
                          _type.LPCWSTR,  # szName
                          _Pointer[_type.COR_SIGNATURE],  # pvSigBlob
                          _type.ULONG,  # cbSigBlob
                          _Pointer[_type.mdFieldDef]],  # ptkFieldDef
                         _type.HRESULT]
    FindMemberRef: _Callable[[_type.mdTypeRef,  # tkTypeRef
                              _type.LPCWSTR,  # szName
                              _Pointer[_type.COR_SIGNATURE],  # pvSigBlob
                              _type.ULONG,  # cbSigBlob
                              _Pointer[_type.mdMemberRef]],  # pMemberRef
                             _type.HRESULT]
    GetMethodProps: _Callable[[_type.mdMethodDef,  # tkMethodDef
                               _Pointer[_type.mdTypeDef],  # ptkClass
                               _type.LPWSTR,  # szMethod
                               _type.ULONG,  # cchMethod
                               _Pointer[_type.ULONG],  # pchMethod
                               _Pointer[_type.DWORD],  # pdwAttr
                               _Pointer[_Pointer[_type.COR_SIGNATURE]],  # ppvSigBlob
                               _Pointer[_type.ULONG],  # pcbSigBlob
                               _Pointer[_type.ULONG],  # pulCodeRVA
                               _Pointer[_type.DWORD]],  # pdwImplFlags
                              _type.HRESULT]
    GetMemberRefProps: _Callable[[_type.mdMemberRef,  # tkMemberRef
                                  _Pointer[_type.mdToken],  # ptk
                                  _type.LPWSTR,  # szMember
                                  _type.ULONG,  # cchMember
                                  _Pointer[_type.ULONG],  # pchMember
                                  _Pointer[_Pointer[_type.COR_SIGNATURE]],  # ppvSigBlob
                                  _Pointer[_type.ULONG]],  # pcbSigBlob
                                 _type.HRESULT]
    EnumProperties: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                               _type.mdTypeDef,  # tkTypDef
                               _Pointer[_type.mdProperty],  # rgProperties
                               _type.ULONG,  # cMax
                               _Pointer[_type.ULONG]],  # pcProperties
                              _type.HRESULT]
    EnumEvents: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                           _type.mdTypeDef,  # tkTypDef
                           _Pointer[_type.mdEvent],  # rgEvents
                           _type.ULONG,  # cMax
                           _Pointer[_type.ULONG]],  # pcEvents
                          _type.HRESULT]
    GetEventProps: _Callable[[_type.mdEvent,  # tkEvent
                              _Pointer[_type.mdTypeDef],  # ptkClass
                              _type.LPWSTR,  # szEvent
                              _type.ULONG,  # cchEvent
                              _Pointer[_type.ULONG],  # pchEvent
                              _Pointer[_type.DWORD],  # pdwEventFlags
                              _Pointer[_type.mdToken],  # ptkEventType
                              _Pointer[_type.mdMethodDef],  # ptkAddOn
                              _Pointer[_type.mdMethodDef],  # ptkRemoveOn
                              _Pointer[_type.mdMethodDef],  # tkkFire
                              _Pointer[_type.mdMethodDef],  # rgOtherMethod
                              _type.ULONG,  # cMax
                              _Pointer[_type.ULONG]],  # pcOtherMethod
                             _type.HRESULT]
    EnumMethodSemantics: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                    _type.mdMethodDef,  # tkMethodDef
                                    _Pointer[_type.mdToken],  # rgEventProp
                                    _type.ULONG,  # cMax
                                    _Pointer[_type.ULONG]],  # pcEventProp
                                   _type.HRESULT]
    GetMethodSemantics: _Callable[[_type.mdMethodDef,  # tkMethodDef
                                   _type.mdToken,  # tkEventProp
                                   _Pointer[_type.DWORD]],  # pdwSemanticsFlags
                                  _type.HRESULT]
    GetClassLayout: _Callable[[_type.mdTypeDef,  # tkTypeDef
                               _Pointer[_type.DWORD],  # pdwPackSize
                               _Pointer[_struct.COR_FIELD_OFFSET],  # rgFieldOffset
                               _type.ULONG,  # cMax
                               _Pointer[_type.ULONG],  # pcFieldOffset
                               _Pointer[_type.ULONG]],  # pulClassSize
                              _type.HRESULT]
    GetFieldMarshal: _Callable[[_type.mdToken,  # tk
                                _Pointer[_Pointer[_type.COR_SIGNATURE]],  # ppvNativeType
                                _Pointer[_type.ULONG]],  # pcbNativeType
                               _type.HRESULT]
    GetRVA: _Callable[[_type.mdToken,  # tk
                       _Pointer[_type.ULONG],  # pulCodeRVA
                       _Pointer[_type.DWORD]],  # pdwImplFlags
                      _type.HRESULT]
    GetPermissionSetProps: _Callable[[_type.mdPermission,  # tk
                                      _Pointer[_type.DWORD],  # pdwAction
                                      _Pointer[_Pointer[_type.BYTE]],  # ppvPermission
                                      _Pointer[_type.ULONG]],  # pcbPermission
                                     _type.HRESULT]
    GetSigFromToken: _Callable[[_type.mdSignature,  # tkSignature
                                _Pointer[_Pointer[_type.COR_SIGNATURE]],  # ppvSig
                                _Pointer[_type.ULONG]],  # pcbSig
                               _type.HRESULT]
    GetModuleRefProps: _Callable[[_type.mdModuleRef,  # tkModuleRef
                                  _type.LPWSTR,  # szName
                                  _type.ULONG,  # cchName
                                  _Pointer[_type.ULONG]],  # pchName
                                 _type.HRESULT]
    EnumModuleRefs: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                               _Pointer[_type.mdModuleRef],  # rgModuleRefs
                               _type.ULONG,  # cMax
                               _Pointer[_type.ULONG]],  # pcModuleRefs
                              _type.HRESULT]
    GetTypeSpecFromToken: _Callable[[_type.mdTypeSpec,  # tkTypeSpec
                                     _Pointer[_Pointer[_type.COR_SIGNATURE]],  # ppvSig
                                     _Pointer[_type.ULONG]],  # pcbSig
                                    _type.HRESULT]
    GetNameFromToken: _Callable[[_type.mdToken,  # tk
                                 _Pointer[_type.c_char_p]],  # pszUtf8NamePtr
                                _type.HRESULT]
    EnumUnresolvedMethods: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                      _Pointer[_type.mdToken],  # rgMethods
                                      _type.ULONG,  # cMax
                                      _Pointer[_type.ULONG]],  # pcTokens
                                     _type.HRESULT]
    GetUserString: _Callable[[_type.mdString,  # tkString
                              _type.LPWSTR,  # szString
                              _type.ULONG,  # cchString
                              _Pointer[_type.ULONG]],  # pchString
                             _type.HRESULT]
    GetPinvokeMap: _Callable[[_type.mdToken,  # tk
                              _Pointer[_type.DWORD],  # pdwMappingFlags
                              _type.LPWSTR,  # szImportName
                              _type.ULONG,  # cchImportName
                              _Pointer[_type.ULONG],  # pchImportName
                              _Pointer[_type.mdModuleRef]],  # ptkImportDLL
                             _type.HRESULT]
    EnumSignatures: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                               _Pointer[_type.mdSignature],  # rgSignatures
                               _type.ULONG,  # cMax
                               _Pointer[_type.ULONG]],  # pcSignatures
                              _type.HRESULT]
    EnumTypeSpecs: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                              _Pointer[_type.mdTypeSpec],  # rgTypeSpecs
                              _type.ULONG,  # cMax
                              _Pointer[_type.ULONG]],  # pcTypeSpecs
                             _type.HRESULT]
    EnumUserStrings: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                _Pointer[_type.mdString],  # rgStrings
                                _type.ULONG,  # cMax
                                _Pointer[_type.ULONG]],  # pcStrings
                               _type.HRESULT]
    GetParamForMethodIndex: _Callable[[_type.mdMethodDef,  # tkMethodDef
                                       _type.ULONG,  # ulParamSeq
                                       _Pointer[_type.mdParamDef]],  # ptkParamDef
                                      _type.HRESULT]
    EnumCustomAttributes: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                     _type.mdToken,  # tk
                                     _type.mdToken,  # tkType
                                     _Pointer[_type.mdCustomAttribute],  # rgCustomAttributes
                                     _type.ULONG,  # cMax
                                     _Pointer[_type.ULONG]],  # pcCustomAttributes
                                    _type.HRESULT]
    GetCustomAttributeProps: _Callable[[_type.mdCustomAttribute,  # cv
                                        _Pointer[_type.mdToken],  # ptkObj
                                        _Pointer[_type.mdToken],  # ptkType
                                        _Pointer[_Pointer[_type.BYTE]],  # ppBlob
                                        _Pointer[_type.ULONG]],  # pcbBlob
                                       _type.HRESULT]
    FindTypeRef: _Callable[[_type.mdToken,  # tkResolutionScope
                            _type.LPCWSTR,  # szName
                            _Pointer[_type.mdTypeRef]],  # tkTypeRef
                           _type.HRESULT]
    GetMemberProps: _Callable[[_type.mdToken,  # tkMember
                               _Pointer[_type.mdTypeDef],  # ptkTypeDef
                               _type.LPWSTR,  # szMember
                               _type.ULONG,  # cchMember
                               _Pointer[_type.ULONG],  # pchMember
                               _Pointer[_type.DWORD],  # pdwAttr
                               _Pointer[_Pointer[_type.COR_SIGNATURE]],  # ppvSigBlob
                               _Pointer[_type.ULONG],  # pcbSigBlob
                               _Pointer[_type.ULONG],  # pulCodeRVA
                               _Pointer[_type.DWORD],  # pdwImplFlags
                               _Pointer[_type.DWORD],  # pdwCPlusTypeFlag
                               _Pointer[_type.c_char_p],  # ppValue
                               _Pointer[_type.ULONG]],  # pcchValue
                              _type.HRESULT]
    GetFieldProps: _Callable[[_type.mdFieldDef,  # tkFieldDef
                              _Pointer[_type.mdTypeDef],  # ptkTypeDef
                              _type.LPWSTR,  # szField
                              _type.ULONG,  # cchField
                              _Pointer[_type.ULONG],  # pchField
                              _Pointer[_type.DWORD],  # pdwAttr
                              _Pointer[_Pointer[_type.COR_SIGNATURE]],  # ppvSigBlob
                              _Pointer[_type.ULONG],  # pcbSigBlob
                              _Pointer[_type.DWORD],  # pdwCPlusTypeFlag
                              _Pointer[_type.c_char_p],  # ppValue
                              _Pointer[_type.ULONG]],  # pcchValue
                             _type.HRESULT]
    GetPropertyProps: _Callable[[_type.mdProperty,  # prop
                                 _Pointer[_type.mdTypeDef],  # ptkTypeDef
                                 _type.LPWSTR,  # szProperty
                                 _type.ULONG,  # cchProperty
                                 _Pointer[_type.ULONG],  # pchProperty
                                 _Pointer[_type.DWORD],  # pdwPropFlags
                                 _Pointer[_Pointer[_type.COR_SIGNATURE]],  # ppvSigBlob
                                 _Pointer[_type.ULONG],  # pcbSigBlob
                                 _Pointer[_type.DWORD],  # pdwCPlusTypeFlag
                                 _Pointer[_type.c_char_p],  # ppDefaultValue
                                 _Pointer[_type.ULONG],  # pcchDefaultValue
                                 _Pointer[_type.mdMethodDef],  # ptkSetter
                                 _Pointer[_type.mdMethodDef],  # ptkGetter
                                 _Pointer[_type.mdMethodDef],  # rgOtherMethod
                                 _type.ULONG,  # cMax
                                 _Pointer[_type.ULONG]],  # pcOtherMethod
                                _type.HRESULT]
    GetParamProps: _Callable[[_type.mdParamDef,  # tkParamDef
                              _Pointer[_type.mdMethodDef],  # ptkMethodDef
                              _Pointer[_type.ULONG],  # pulSequence
                              _type.LPWSTR,  # szName
                              _type.ULONG,  # cchName
                              _Pointer[_type.ULONG],  # pchName
                              _Pointer[_type.DWORD],  # pdwAttr
                              _Pointer[_type.DWORD],  # pdwCPlusTypeFlag
                              _Pointer[_type.c_char_p],  # ppValue
                              _Pointer[_type.ULONG]],  # pcchValue
                             _type.HRESULT]
    GetCustomAttributeByName: _Callable[[_type.mdToken,  # tkObj
                                         _type.LPCWSTR,  # szName
                                         _Pointer[_Pointer[_type.BYTE]],  # ppData
                                         _Pointer[_type.ULONG]],  # pcbData
                                        _type.HRESULT]
    IsValidToken: _Callable[[_type.mdToken],  # tk
                            _type.BOOL]
    GetNestedClassProps: _Callable[[_type.mdTypeDef,  # tdNestedClass
                                    _Pointer[_type.mdTypeDef]],  # ptdEnclosingClass
                                   _type.HRESULT]
    GetNativeCallConvFromSig: _Callable[[_Pointer[_type.BYTE],  # pvSig
                                         _type.ULONG,  # cbSig
                                         _Pointer[_type.ULONG]],  # pCallConv
                                        _type.HRESULT]
    IsGlobal: _Callable[[_type.mdToken,  # tk
                         _Pointer[_type.c_int]],  # pbIsGlobal
                        _type.HRESULT]


class IMetaDataImport2(IMetaDataImport):
    EnumGenericParams: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                  _type.mdToken,  # tk
                                  _Pointer[_type.mdGenericParam],  # rGenericParams
                                  _type.ULONG,  # cMax
                                  _Pointer[_type.ULONG]],  # pcGenericParams
                                 _type.HRESULT]
    GetGenericParamProps: _Callable[[_type.mdGenericParam,  # gp
                                     _Pointer[_type.ULONG],  # pulParamSeq
                                     _Pointer[_type.DWORD],  # pdwParamFlags
                                     _Pointer[_type.mdToken],  # ptOwner
                                     _Pointer[_type.DWORD],  # reserved
                                     _type.LPWSTR,  # wzname
                                     _type.ULONG,  # cchName
                                     _Pointer[_type.ULONG]],  # pchName
                                    _type.HRESULT]
    GetMethodSpecProps: _Callable[[_type.mdMethodSpec,  # mi
                                   _Pointer[_type.mdToken],  # tkParent
                                   _Pointer[_Pointer[_type.COR_SIGNATURE]],  # ppvSigBlob
                                   _Pointer[_type.ULONG]],  # pcbSigBlob
                                  _type.HRESULT]
    EnumGenericParamConstraints: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                            _type.mdGenericParam,  # tk
                                            _Pointer[_type.mdGenericParamConstraint],  # rGenericParamConstraints
                                            _type.ULONG,  # cMax
                                            _Pointer[_type.ULONG]],  # pcGenericParamConstraints
                                           _type.HRESULT]
    GetGenericParamConstraintProps: _Callable[[_type.mdGenericParamConstraint,  # gpc
                                               _Pointer[_type.mdGenericParam],  # ptGenericParam
                                               _Pointer[_type.mdToken]],  # ptkConstraintType
                                              _type.HRESULT]
    GetPEKind: _Callable[[_Pointer[_type.DWORD],  # pdwPEKind
                          _Pointer[_type.DWORD]],  # pdwMAchine
                         _type.HRESULT]
    GetVersionString: _Callable[[_type.LPWSTR,  # pwzBuf
                                 _type.DWORD,  # ccBufSize
                                 _Pointer[_type.DWORD]],  # pccBufSize
                                _type.HRESULT]
    EnumMethodSpecs: _Callable[[_Pointer[_type.HCORENUM],  # phEnum
                                _type.mdToken,  # tk
                                _Pointer[_type.mdMethodSpec],  # rMethodSpecs
                                _type.ULONG,  # cMax
                                _Pointer[_type.ULONG]],  # pcMethodSpecs
                               _type.HRESULT]


class IMetaDataTables(_Unknwnbase.IUnknown):
    GetStringHeapSize: _Callable[[_Pointer[_type.ULONG]],  # pcbStrings
                                 _type.HRESULT]
    GetBlobHeapSize: _Callable[[_Pointer[_type.ULONG]],  # pcbBlobs
                               _type.HRESULT]
    GetGuidHeapSize: _Callable[[_Pointer[_type.ULONG]],  # pcbGuids
                               _type.HRESULT]
    GetUserStringHeapSize: _Callable[[_Pointer[_type.ULONG]],  # pcbUserStrings
                                     _type.HRESULT]
    GetNumTables: _Callable[[_Pointer[_type.ULONG]],  # pcTables
                            _type.HRESULT]
    GetTableIndex: _Callable[[_type.ULONG,  # token
                              _Pointer[_type.ULONG]],  # pixTbl
                             _type.HRESULT]
    GetTableInfo: _Callable[[_type.ULONG,  # ixTbl
                             _Pointer[_type.ULONG],  # pcbRow
                             _Pointer[_type.ULONG],  # pcRows
                             _Pointer[_type.ULONG],  # pcCols
                             _Pointer[_type.ULONG],  # piKey
                             _Pointer[_type.LPCSTR]],  # ppName
                            _type.HRESULT]
    GetColumnInfo: _Callable[[_type.ULONG,  # ixTbl
                              _type.ULONG,  # ixCol
                              _Pointer[_type.ULONG],  # poCol
                              _Pointer[_type.ULONG],  # pcbCol
                              _Pointer[_type.ULONG],  # pType
                              _Pointer[_type.LPCSTR]],  # ppName
                             _type.HRESULT]
    GetCodedTokenInfo: _Callable[[_type.ULONG,  # ixCdTkn
                                  _Pointer[_type.ULONG],  # pcTokens
                                  _Pointer[_Pointer[_type.ULONG]],  # ppTokens
                                  _Pointer[_type.LPCSTR]],  # ppName
                                 _type.HRESULT]
    GetRow: _Callable[[_type.ULONG,  # ixTbl
                       _type.ULONG,  # rid
                       _Pointer[_type.BYTE]],  # ppRow
                      _type.HRESULT]
    GetColumn: _Callable[[_type.ULONG,  # ixTbl
                          _type.ULONG,  # ixCol
                          _type.ULONG,  # rid
                          _Pointer[_type.ULONG]],  # pVal
                         _type.HRESULT]
    GetString: _Callable[[_type.ULONG,  # ixString
                          _Pointer[_type.LPCSTR]],  # ppString
                         _type.HRESULT]
    GetBlob: _Callable[[_type.ULONG,  # ixBlob
                        _Pointer[_type.ULONG],  # pcbData
                        _Pointer[_Pointer[_type.BYTE]]],  # ppData
                       _type.HRESULT]
    GetGuid: _Callable[[_type.ULONG,  # ixGuid
                        _Pointer[_Pointer[_struct.GUID]]],  # ppGUID
                       _type.HRESULT]
    GetUserString: _Callable[[_type.ULONG,  # ixUserString
                              _Pointer[_type.ULONG],  # pcbData
                              _Pointer[_Pointer[_type.BYTE]]],  # ppData
                             _type.HRESULT]
    GetNextString: _Callable[[_type.ULONG,  # ixString
                              _Pointer[_type.ULONG]],  # pNext
                             _type.HRESULT]
    GetNextBlob: _Callable[[_type.ULONG,  # ixBlob
                            _Pointer[_type.ULONG]],  # pNext
                           _type.HRESULT]
    GetNextGuid: _Callable[[_type.ULONG,  # ixGuid
                            _Pointer[_type.ULONG]],  # pNext
                           _type.HRESULT]
    GetNextUserString: _Callable[[_type.ULONG,  # ixUserString
                                  _Pointer[_type.ULONG]],  # pNext
                                 _type.HRESULT]


class IMetaDataTables2(IMetaDataTables):
    GetMetaDataStorage: _Callable[[_Pointer[_Pointer[_type.BYTE]],  # ppvMd
                                   _Pointer[_type.ULONG]],  # pcbMd
                                  _type.HRESULT]
    GetMetaDataStreamInfo: _Callable[[_type.ULONG,  # ix
                                      _Pointer[_type.LPCSTR],  # ppchName
                                      _Pointer[_Pointer[_type.BYTE]],  # ppv
                                      _Pointer[_type.ULONG]],  # pcb
                                     _type.HRESULT]

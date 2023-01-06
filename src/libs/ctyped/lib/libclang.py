from __future__ import annotations as _

from typing import Callable as _Callable

from . import _CLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# BuildSystem
clang_getBuildSessionTimestamp: _Callable[[],
                                          _type.c_ulonglong]
clang_VirtualFileOverlay_create: _Callable[[_type.c_uint],  # options
                                           _type.CXVirtualFileOverlay]
clang_VirtualFileOverlay_addFileMapping: _Callable[[_type.CXVirtualFileOverlay,
                                                    _type.c_char_p,  # virtualPath
                                                    _type.c_char_p],  # realPath
                                                   _enum.CXErrorCode]
clang_VirtualFileOverlay_setCaseSensitivity: _Callable[[_type.CXVirtualFileOverlay,
                                                        _type.c_int],  # caseSensitive
                                                       _enum.CXErrorCode]
clang_VirtualFileOverlay_writeToBuffer: _Callable[[_type.CXVirtualFileOverlay,
                                                   _type.c_uint,  # options
                                                   _Pointer[_type.c_char_p],  # out_buffer_ptr
                                                   _Pointer[_type.c_uint]],  # out_buffer_size
                                                  _enum.CXErrorCode]
clang_free: _Callable[[_type.c_void_p],  # buffer
                      _type.c_void]
clang_VirtualFileOverlay_dispose: _Callable[[_type.CXVirtualFileOverlay],
                                            _type.c_void]
clang_ModuleMapDescriptor_create: _Callable[[_type.c_uint],  # options
                                            _type.CXModuleMapDescriptor]
clang_ModuleMapDescriptor_setFrameworkModuleName: _Callable[[_type.CXModuleMapDescriptor,
                                                             _type.c_char_p],  # name
                                                            _enum.CXErrorCode]
clang_ModuleMapDescriptor_setUmbrellaHeader: _Callable[[_type.CXModuleMapDescriptor,
                                                        _type.c_char_p],  # name
                                                       _enum.CXErrorCode]
clang_ModuleMapDescriptor_writeToBuffer: _Callable[[_type.CXModuleMapDescriptor,
                                                    _type.c_uint,  # options
                                                    _Pointer[_type.c_char_p],  # out_buffer_ptr
                                                    _Pointer[_type.c_uint]],  # out_buffer_size
                                                   _enum.CXErrorCode]
clang_ModuleMapDescriptor_dispose: _Callable[[_type.CXModuleMapDescriptor],
                                             _type.c_void]
# CXCompilationDatabase
clang_CompilationDatabase_fromDirectory: _Callable[[_type.c_char_p,  # BuildDir
                                                    _Pointer[_enum.CXCompilationDatabase_Error]],  # ErrorCode
                                                   _type.CXCompilationDatabase]
clang_CompilationDatabase_dispose: _Callable[[_type.CXCompilationDatabase],
                                             _type.c_void]
clang_CompilationDatabase_getCompileCommands: _Callable[[_type.CXCompilationDatabase,
                                                         _type.c_char_p],  # CompleteFileName
                                                        _type.CXCompileCommands]
clang_CompilationDatabase_getAllCompileCommands: _Callable[[_type.CXCompilationDatabase],
                                                           _type.CXCompileCommands]
clang_CompileCommands_dispose: _Callable[[_type.CXCompileCommands],
                                         _type.c_void]
clang_CompileCommands_getSize: _Callable[[_type.CXCompileCommands],
                                         _type.c_uint]
clang_CompileCommands_getCommand: _Callable[[_type.CXCompileCommands,
                                             _type.c_uint],  # I
                                            _type.CXCompileCommand]
clang_CompileCommand_getDirectory: _Callable[[_type.CXCompileCommand],
                                             _struct.CXString]
clang_CompileCommand_getFilename: _Callable[[_type.CXCompileCommand],
                                            _struct.CXString]
clang_CompileCommand_getNumArgs: _Callable[[_type.CXCompileCommand],
                                           _type.c_uint]
clang_CompileCommand_getArg: _Callable[[_type.CXCompileCommand,
                                        _type.c_uint],  # I
                                       _struct.CXString]
clang_CompileCommand_getNumMappedSources: _Callable[[_type.CXCompileCommand],
                                                    _type.c_uint]
clang_CompileCommand_getMappedSourcePath: _Callable[[_type.CXCompileCommand,
                                                     _type.c_uint],  # I
                                                    _struct.CXString]
clang_CompileCommand_getMappedSourceContent: _Callable[[_type.CXCompileCommand,
                                                        _type.c_uint],  # I
                                                       _struct.CXString]
# CXString
clang_getCString: _Callable[[_struct.CXString],  # string
                            _type.c_char_p]
clang_disposeString: _Callable[[_struct.CXString],  # string
                               _type.c_void]
clang_disposeStringSet: _Callable[[_Pointer[_struct.CXStringSet]],  # set
                                  _type.c_void]
# Documentation
clang_Cursor_getParsedComment: _Callable[[_struct.CXCursor],  # C
                                         _struct.CXComment]
clang_Comment_getKind: _Callable[[_struct.CXComment],  # Comment
                                 _enum.CXCommentKind]
clang_Comment_getNumChildren: _Callable[[_struct.CXComment],  # Comment
                                        _type.c_uint]
clang_Comment_getChild: _Callable[[_struct.CXComment,  # Comment
                                   _type.c_uint],  # ChildIdx
                                  _struct.CXComment]
clang_Comment_isWhitespace: _Callable[[_struct.CXComment],  # Comment
                                      _type.c_uint]
clang_InlineContentComment_hasTrailingNewline: _Callable[[_struct.CXComment],  # Comment
                                                         _type.c_uint]
clang_TextComment_getText: _Callable[[_struct.CXComment],  # Comment
                                     _struct.CXString]
clang_InlineCommandComment_getCommandName: _Callable[[_struct.CXComment],  # Comment
                                                     _struct.CXString]
clang_InlineCommandComment_getRenderKind: _Callable[[_struct.CXComment],  # Comment
                                                    _enum.CXCommentInlineCommandRenderKind]
clang_InlineCommandComment_getNumArgs: _Callable[[_struct.CXComment],  # Comment
                                                 _type.c_uint]
clang_InlineCommandComment_getArgText: _Callable[[_struct.CXComment,  # Comment
                                                  _type.c_uint],  # ArgIdx
                                                 _struct.CXString]
clang_HTMLTagComment_getTagName: _Callable[[_struct.CXComment],  # Comment
                                           _struct.CXString]
clang_HTMLStartTagComment_isSelfClosing: _Callable[[_struct.CXComment],  # Comment
                                                   _type.c_uint]
clang_HTMLStartTag_getNumAttrs: _Callable[[_struct.CXComment],  # Comment
                                          _type.c_uint]
clang_HTMLStartTag_getAttrName: _Callable[[_struct.CXComment,  # Comment
                                           _type.c_uint],  # AttrIdx
                                          _struct.CXString]
clang_HTMLStartTag_getAttrValue: _Callable[[_struct.CXComment,  # Comment
                                            _type.c_uint],  # AttrIdx
                                           _struct.CXString]
clang_BlockCommandComment_getCommandName: _Callable[[_struct.CXComment],  # Comment
                                                    _struct.CXString]
clang_BlockCommandComment_getNumArgs: _Callable[[_struct.CXComment],  # Comment
                                                _type.c_uint]
clang_BlockCommandComment_getArgText: _Callable[[_struct.CXComment,  # Comment
                                                 _type.c_uint],  # ArgIdx
                                                _struct.CXString]
clang_BlockCommandComment_getParagraph: _Callable[[_struct.CXComment],  # Comment
                                                  _struct.CXComment]
clang_ParamCommandComment_getParamName: _Callable[[_struct.CXComment],  # Comment
                                                  _struct.CXString]
clang_ParamCommandComment_isParamIndexValid: _Callable[[_struct.CXComment],  # Comment
                                                       _type.c_uint]
clang_ParamCommandComment_getParamIndex: _Callable[[_struct.CXComment],  # Comment
                                                   _type.c_uint]
clang_ParamCommandComment_isDirectionExplicit: _Callable[[_struct.CXComment],  # Comment
                                                         _type.c_uint]
clang_ParamCommandComment_getDirection: _Callable[[_struct.CXComment],  # Comment
                                                  _enum.CXCommentParamPassDirection]
clang_TParamCommandComment_getParamName: _Callable[[_struct.CXComment],  # Comment
                                                   _struct.CXString]
clang_TParamCommandComment_isParamPositionValid: _Callable[[_struct.CXComment],  # Comment
                                                           _type.c_uint]
clang_TParamCommandComment_getDepth: _Callable[[_struct.CXComment],  # Comment
                                               _type.c_uint]
clang_TParamCommandComment_getIndex: _Callable[[_struct.CXComment,  # Comment
                                                _type.c_uint],  # Depth
                                               _type.c_uint]
clang_VerbatimBlockLineComment_getText: _Callable[[_struct.CXComment],  # Comment
                                                  _struct.CXString]
clang_VerbatimLineComment_getText: _Callable[[_struct.CXComment],  # Comment
                                             _struct.CXString]
clang_HTMLTagComment_getAsString: _Callable[[_struct.CXComment],  # Comment
                                            _struct.CXString]
clang_FullComment_getAsHTML: _Callable[[_struct.CXComment],  # Comment
                                       _struct.CXString]
clang_FullComment_getAsXML: _Callable[[_struct.CXComment],  # Comment
                                      _struct.CXString]
# FatalErrorHandler
clang_install_aborting_llvm_fatal_error_handler: _Callable[[],
                                                           _type.c_void]
clang_uninstall_llvm_fatal_error_handler: _Callable[[],
                                                    _type.c_void]
# Index
clang_createIndex: _Callable[[_type.c_int,  # excludeDeclarationsFromPCH
                              _type.c_int],  # displayDiagnostics
                             _type.CXIndex]
clang_disposeIndex: _Callable[[_type.CXIndex],  # index
                              _type.c_void]
clang_CXIndex_setGlobalOptions: _Callable[[_type.CXIndex,
                                           _type.c_uint],  # options
                                          _type.c_void]
clang_CXIndex_getGlobalOptions: _Callable[[_type.CXIndex],
                                          _type.c_uint]
clang_CXIndex_setInvocationEmissionPathOption: _Callable[[_type.CXIndex,
                                                          _type.c_char_p],  # Path
                                                         _type.c_void]
clang_getFileName: _Callable[[_type.CXFile],  # SFile
                             _struct.CXString]
clang_getFileTime: _Callable[[_type.CXFile],  # SFile
                             _type.time_t]
clang_getFileUniqueID: _Callable[[_type.CXFile,  # file
                                  _Pointer[_struct.CXFileUniqueID]],  # outID
                                 _type.c_int]
clang_isFileMultipleIncludeGuarded: _Callable[[_type.CXTranslationUnit,  # tu
                                               _type.CXFile],  # file
                                              _type.c_uint]
clang_getFile: _Callable[[_type.CXTranslationUnit,  # tu
                          _type.c_char_p],  # file_name
                         _type.CXFile]
clang_getFileContents: _Callable[[_type.CXTranslationUnit,  # tu
                                  _type.CXFile,  # file
                                  _Pointer[_type.c_size_t]],  # size
                                 _type.c_char_p]
clang_File_isEqual: _Callable[[_type.CXFile,  # file1
                               _type.CXFile],  # file2
                              _type.c_int]
clang_File_tryGetRealPathName: _Callable[[_type.CXFile],  # file
                                         _struct.CXString]
clang_getNullLocation: _Callable[[],
                                 _struct.CXSourceLocation]
clang_equalLocations: _Callable[[_struct.CXSourceLocation,  # loc1
                                 _struct.CXSourceLocation],  # loc2
                                _type.c_uint]
clang_getLocation: _Callable[[_type.CXTranslationUnit,  # tu
                              _type.CXFile,  # file
                              _type.c_uint,  # line
                              _type.c_uint],  # column
                             _struct.CXSourceLocation]
clang_getLocationForOffset: _Callable[[_type.CXTranslationUnit,  # tu
                                       _type.CXFile,  # file
                                       _type.c_uint],  # offset
                                      _struct.CXSourceLocation]
clang_Location_isInSystemHeader: _Callable[[_struct.CXSourceLocation],  # location
                                           _type.c_int]
clang_Location_isFromMainFile: _Callable[[_struct.CXSourceLocation],  # location
                                         _type.c_int]
clang_getNullRange: _Callable[[],
                              _struct.CXSourceRange]
clang_getRange: _Callable[[_struct.CXSourceLocation,  # begin
                           _struct.CXSourceLocation],  # end
                          _struct.CXSourceRange]
clang_equalRanges: _Callable[[_struct.CXSourceRange,  # range1
                              _struct.CXSourceRange],  # range2
                             _type.c_uint]
clang_Range_isNull: _Callable[[_struct.CXSourceRange],  # range
                              _type.c_int]
clang_getExpansionLocation: _Callable[[_struct.CXSourceLocation,  # location
                                       _Pointer[_type.CXFile],  # file
                                       _Pointer[_type.c_uint],  # line
                                       _Pointer[_type.c_uint],  # column
                                       _Pointer[_type.c_uint]],  # offset
                                      _type.c_void]
clang_getPresumedLocation: _Callable[[_struct.CXSourceLocation,  # location
                                      _Pointer[_struct.CXString],  # filename
                                      _Pointer[_type.c_uint],  # line
                                      _Pointer[_type.c_uint]],  # column
                                     _type.c_void]
clang_getInstantiationLocation: _Callable[[_struct.CXSourceLocation,  # location
                                           _Pointer[_type.CXFile],  # file
                                           _Pointer[_type.c_uint],  # line
                                           _Pointer[_type.c_uint],  # column
                                           _Pointer[_type.c_uint]],  # offset
                                          _type.c_void]
clang_getSpellingLocation: _Callable[[_struct.CXSourceLocation,  # location
                                      _Pointer[_type.CXFile],  # file
                                      _Pointer[_type.c_uint],  # line
                                      _Pointer[_type.c_uint],  # column
                                      _Pointer[_type.c_uint]],  # offset
                                     _type.c_void]
clang_getFileLocation: _Callable[[_struct.CXSourceLocation,  # location
                                  _Pointer[_type.CXFile],  # file
                                  _Pointer[_type.c_uint],  # line
                                  _Pointer[_type.c_uint],  # column
                                  _Pointer[_type.c_uint]],  # offset
                                 _type.c_void]
clang_getRangeStart: _Callable[[_struct.CXSourceRange],  # range
                               _struct.CXSourceLocation]
clang_getRangeEnd: _Callable[[_struct.CXSourceRange],  # range
                             _struct.CXSourceLocation]
clang_getSkippedRanges: _Callable[[_type.CXTranslationUnit,  # tu
                                   _type.CXFile],  # file
                                  _Pointer[_struct.CXSourceRangeList]]
clang_getAllSkippedRanges: _Callable[[_type.CXTranslationUnit],  # tu
                                     _Pointer[_struct.CXSourceRangeList]]
clang_disposeSourceRangeList: _Callable[[_Pointer[_struct.CXSourceRangeList]],  # ranges
                                        _type.c_void]
clang_getNumDiagnosticsInSet: _Callable[[_type.CXDiagnosticSet],  # Diags
                                        _type.c_uint]
clang_getDiagnosticInSet: _Callable[[_type.CXDiagnosticSet,  # Diags
                                     _type.c_uint],  # Index
                                    _type.CXDiagnostic]
clang_loadDiagnostics: _Callable[[_type.c_char_p,  # file
                                  _Pointer[_enum.CXLoadDiag_Error],  # error
                                  _Pointer[_struct.CXString]],  # errorString
                                 _type.CXDiagnosticSet]
clang_disposeDiagnosticSet: _Callable[[_type.CXDiagnosticSet],  # Diags
                                      _type.c_void]
clang_getChildDiagnostics: _Callable[[_type.CXDiagnostic],  # D
                                     _type.CXDiagnosticSet]
clang_getNumDiagnostics: _Callable[[_type.CXTranslationUnit],  # Unit
                                   _type.c_uint]
clang_getDiagnostic: _Callable[[_type.CXTranslationUnit,  # Unit
                                _type.c_uint],  # Index
                               _type.CXDiagnostic]
clang_getDiagnosticSetFromTU: _Callable[[_type.CXTranslationUnit],  # Unit
                                        _type.CXDiagnosticSet]
clang_disposeDiagnostic: _Callable[[_type.CXDiagnostic],  # Diagnostic
                                   _type.c_void]
clang_formatDiagnostic: _Callable[[_type.CXDiagnostic,  # Diagnostic
                                   _type.c_uint],  # Options
                                  _struct.CXString]
clang_defaultDiagnosticDisplayOptions: _Callable[[],
                                                 _type.c_uint]
clang_getDiagnosticSeverity: _Callable[[_type.CXDiagnostic],
                                       _enum.CXDiagnosticSeverity]
clang_getDiagnosticLocation: _Callable[[_type.CXDiagnostic],
                                       _struct.CXSourceLocation]
clang_getDiagnosticSpelling: _Callable[[_type.CXDiagnostic],
                                       _struct.CXString]
clang_getDiagnosticOption: _Callable[[_type.CXDiagnostic,  # Diag
                                      _Pointer[_struct.CXString]],  # Disable
                                     _struct.CXString]
clang_getDiagnosticCategory: _Callable[[_type.CXDiagnostic],
                                       _type.c_uint]
clang_getDiagnosticCategoryName: _Callable[[_type.c_uint],  # Category
                                           _struct.CXString]
clang_getDiagnosticCategoryText: _Callable[[_type.CXDiagnostic],
                                           _struct.CXString]
clang_getDiagnosticNumRanges: _Callable[[_type.CXDiagnostic],
                                        _type.c_uint]
clang_getDiagnosticRange: _Callable[[_type.CXDiagnostic,  # Diagnostic
                                     _type.c_uint],  # Range
                                    _struct.CXSourceRange]
clang_getDiagnosticNumFixIts: _Callable[[_type.CXDiagnostic],  # Diagnostic
                                        _type.c_uint]
clang_getDiagnosticFixIt: _Callable[[_type.CXDiagnostic,  # Diagnostic
                                     _type.c_uint,  # FixIt
                                     _Pointer[_struct.CXSourceRange]],  # ReplacementRange
                                    _struct.CXString]
clang_getTranslationUnitSpelling: _Callable[[_type.CXTranslationUnit],  # CTUnit
                                            _struct.CXString]
clang_createTranslationUnitFromSourceFile: _Callable[[_type.CXIndex,  # CIdx
                                                      _type.c_char_p,  # source_filename
                                                      _type.c_int,  # num_clang_command_line_args
                                                      _Pointer[_type.c_char_p],  # clang_command_line_args
                                                      _type.c_uint,  # num_unsaved_files
                                                      _Pointer[_struct.CXUnsavedFile]],  # unsaved_files
                                                     _type.CXTranslationUnit]
clang_createTranslationUnit: _Callable[[_type.CXIndex,  # CIdx
                                        _type.c_char_p],  # ast_filename
                                       _type.CXTranslationUnit]
clang_createTranslationUnit2: _Callable[[_type.CXIndex,  # CIdx
                                         _type.c_char_p,  # ast_filename
                                         _Pointer[_type.CXTranslationUnit]],  # out_TU
                                        _enum.CXErrorCode]
clang_defaultEditingTranslationUnitOptions: _Callable[[],
                                                      _type.c_uint]
clang_parseTranslationUnit: _Callable[[_type.CXIndex,  # CIdx
                                       _type.c_char_p,  # source_filename
                                       _Pointer[_type.c_char_p],  # command_line_args
                                       _type.c_int,  # num_command_line_args
                                       _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                       _type.c_uint,  # num_unsaved_files
                                       _type.c_uint],  # options
                                      _type.CXTranslationUnit]
clang_parseTranslationUnit2: _Callable[[_type.CXIndex,  # CIdx
                                        _type.c_char_p,  # source_filename
                                        _Pointer[_type.c_char_p],  # command_line_args
                                        _type.c_int,  # num_command_line_args
                                        _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                        _type.c_uint,  # num_unsaved_files
                                        _type.c_uint,  # options
                                        _Pointer[_type.CXTranslationUnit]],  # out_TU
                                       _enum.CXErrorCode]
clang_parseTranslationUnit2FullArgv: _Callable[[_type.CXIndex,  # CIdx
                                                _type.c_char_p,  # source_filename
                                                _Pointer[_type.c_char_p],  # command_line_args
                                                _type.c_int,  # num_command_line_args
                                                _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                                _type.c_uint,  # num_unsaved_files
                                                _type.c_uint,  # options
                                                _Pointer[_type.CXTranslationUnit]],  # out_TU
                                               _enum.CXErrorCode]
clang_defaultSaveOptions: _Callable[[_type.CXTranslationUnit],  # TU
                                    _type.c_uint]
clang_saveTranslationUnit: _Callable[[_type.CXTranslationUnit,  # TU
                                      _type.c_char_p,  # FileName
                                      _type.c_uint],  # options
                                     _type.c_int]
clang_suspendTranslationUnit: _Callable[[_type.CXTranslationUnit],
                                        _type.c_uint]
clang_disposeTranslationUnit: _Callable[[_type.CXTranslationUnit],
                                        _type.c_void]
clang_defaultReparseOptions: _Callable[[_type.CXTranslationUnit],  # TU
                                       _type.c_uint]
clang_reparseTranslationUnit: _Callable[[_type.CXTranslationUnit,  # TU
                                         _type.c_uint,  # num_unsaved_files
                                         _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                         _type.c_uint],  # options
                                        _type.c_int]
clang_getTUResourceUsageName: _Callable[[_enum.CXTUResourceUsageKind],  # kind
                                        _type.c_char_p]
clang_getCXTUResourceUsage: _Callable[[_type.CXTranslationUnit],  # TU
                                      _struct.CXTUResourceUsage]
clang_disposeCXTUResourceUsage: _Callable[[_struct.CXTUResourceUsage],  # usage
                                          _type.c_void]
clang_getTranslationUnitTargetInfo: _Callable[[_type.CXTranslationUnit],  # CTUnit
                                              _type.CXTargetInfo]
clang_TargetInfo_dispose: _Callable[[_type.CXTargetInfo],  # Info
                                    _type.c_void]
clang_TargetInfo_getTriple: _Callable[[_type.CXTargetInfo],  # Info
                                      _struct.CXString]
clang_TargetInfo_getPointerWidth: _Callable[[_type.CXTargetInfo],  # Info
                                            _type.c_int]
clang_getNullCursor: _Callable[[],
                               _struct.CXCursor]
clang_getTranslationUnitCursor: _Callable[[_type.CXTranslationUnit],
                                          _struct.CXCursor]
clang_equalCursors: _Callable[[_struct.CXCursor,
                               _struct.CXCursor],
                              _type.c_uint]
clang_Cursor_isNull: _Callable[[_struct.CXCursor],  # cursor
                               _type.c_int]
clang_hashCursor: _Callable[[_struct.CXCursor],
                            _type.c_uint]
clang_getCursorKind: _Callable[[_struct.CXCursor],
                               _enum.CXCursorKind]
clang_isDeclaration: _Callable[[_enum.CXCursorKind],
                               _type.c_uint]
clang_isInvalidDeclaration: _Callable[[_struct.CXCursor],
                                      _type.c_uint]
clang_isReference: _Callable[[_enum.CXCursorKind],
                             _type.c_uint]
clang_isExpression: _Callable[[_enum.CXCursorKind],
                              _type.c_uint]
clang_isStatement: _Callable[[_enum.CXCursorKind],
                             _type.c_uint]
clang_isAttribute: _Callable[[_enum.CXCursorKind],
                             _type.c_uint]
clang_Cursor_hasAttrs: _Callable[[_struct.CXCursor],  # C
                                 _type.c_uint]
clang_isInvalid: _Callable[[_enum.CXCursorKind],
                           _type.c_uint]
clang_isTranslationUnit: _Callable[[_enum.CXCursorKind],
                                   _type.c_uint]
clang_isPreprocessing: _Callable[[_enum.CXCursorKind],
                                 _type.c_uint]
clang_isUnexposed: _Callable[[_enum.CXCursorKind],
                             _type.c_uint]
clang_getCursorLinkage: _Callable[[_struct.CXCursor],  # cursor
                                  _enum.CXLinkageKind]
clang_getCursorVisibility: _Callable[[_struct.CXCursor],  # cursor
                                     _enum.CXVisibilityKind]
clang_getCursorAvailability: _Callable[[_struct.CXCursor],  # cursor
                                       _enum.CXAvailabilityKind]
clang_getCursorPlatformAvailability: _Callable[[_struct.CXCursor,  # cursor
                                                _Pointer[_type.c_int],  # always_deprecated
                                                _Pointer[_struct.CXString],  # deprecated_message
                                                _Pointer[_type.c_int],  # always_unavailable
                                                _Pointer[_struct.CXString],  # unavailable_message
                                                _Pointer[_struct.CXPlatformAvailability],  # availability
                                                _type.c_int],  # availability_size
                                               _type.c_int]
clang_disposeCXPlatformAvailability: _Callable[[_Pointer[_struct.CXPlatformAvailability]],  # availability
                                               _type.c_void]
clang_Cursor_getVarDeclInitializer: _Callable[[_struct.CXCursor],  # cursor
                                              _struct.CXCursor]
clang_Cursor_hasVarDeclGlobalStorage: _Callable[[_struct.CXCursor],  # cursor
                                                _type.c_int]
clang_Cursor_hasVarDeclExternalStorage: _Callable[[_struct.CXCursor],  # cursor
                                                  _type.c_int]
clang_getCursorLanguage: _Callable[[_struct.CXCursor],  # cursor
                                   _enum.CXLanguageKind]
clang_getCursorTLSKind: _Callable[[_struct.CXCursor],  # cursor
                                  _enum.CXTLSKind]
clang_Cursor_getTranslationUnit: _Callable[[_struct.CXCursor],
                                           _type.CXTranslationUnit]
clang_createCXCursorSet: _Callable[[],
                                   _type.CXCursorSet]
clang_disposeCXCursorSet: _Callable[[_type.CXCursorSet],  # cset
                                    _type.c_void]
clang_CXCursorSet_contains: _Callable[[_type.CXCursorSet,  # cset
                                       _struct.CXCursor],  # cursor
                                      _type.c_uint]
clang_CXCursorSet_insert: _Callable[[_type.CXCursorSet,  # cset
                                     _struct.CXCursor],  # cursor
                                    _type.c_uint]
clang_getCursorSemanticParent: _Callable[[_struct.CXCursor],  # cursor
                                         _struct.CXCursor]
clang_getCursorLexicalParent: _Callable[[_struct.CXCursor],  # cursor
                                        _struct.CXCursor]
clang_getOverriddenCursors: _Callable[[_struct.CXCursor,  # cursor
                                       _Pointer[_Pointer[_struct.CXCursor]],  # overridden
                                       _Pointer[_type.c_uint]],  # num_overridden
                                      _type.c_void]
clang_disposeOverriddenCursors: _Callable[[_Pointer[_struct.CXCursor]],  # overridden
                                          _type.c_void]
clang_getIncludedFile: _Callable[[_struct.CXCursor],  # cursor
                                 _type.CXFile]
clang_getCursor: _Callable[[_type.CXTranslationUnit,
                            _struct.CXSourceLocation],
                           _struct.CXCursor]
clang_getCursorLocation: _Callable[[_struct.CXCursor],
                                   _struct.CXSourceLocation]
clang_getCursorExtent: _Callable[[_struct.CXCursor],
                                 _struct.CXSourceRange]
clang_getCursorType: _Callable[[_struct.CXCursor],  # C
                               _struct.CXType]
clang_getTypeSpelling: _Callable[[_struct.CXType],  # CT
                                 _struct.CXString]
clang_getTypedefDeclUnderlyingType: _Callable[[_struct.CXCursor],  # C
                                              _struct.CXType]
clang_getEnumDeclIntegerType: _Callable[[_struct.CXCursor],  # C
                                        _struct.CXType]
clang_getEnumConstantDeclValue: _Callable[[_struct.CXCursor],  # C
                                          _type.c_longlong]
clang_getEnumConstantDeclUnsignedValue: _Callable[[_struct.CXCursor],  # C
                                                  _type.c_ulonglong]
clang_getFieldDeclBitWidth: _Callable[[_struct.CXCursor],  # C
                                      _type.c_int]
clang_Cursor_getNumArguments: _Callable[[_struct.CXCursor],  # C
                                        _type.c_int]
clang_Cursor_getArgument: _Callable[[_struct.CXCursor,  # C
                                     _type.c_uint],  # i
                                    _struct.CXCursor]
clang_Cursor_getNumTemplateArguments: _Callable[[_struct.CXCursor],  # C
                                                _type.c_int]
clang_Cursor_getTemplateArgumentKind: _Callable[[_struct.CXCursor,  # C
                                                 _type.c_uint],  # I
                                                _enum.CXTemplateArgumentKind]
clang_Cursor_getTemplateArgumentType: _Callable[[_struct.CXCursor,  # C
                                                 _type.c_uint],  # I
                                                _struct.CXType]
clang_Cursor_getTemplateArgumentValue: _Callable[[_struct.CXCursor,  # C
                                                  _type.c_uint],  # I
                                                 _type.c_longlong]
clang_Cursor_getTemplateArgumentUnsignedValue: _Callable[[_struct.CXCursor,  # C
                                                          _type.c_uint],  # I
                                                         _type.c_ulonglong]
clang_equalTypes: _Callable[[_struct.CXType,  # A
                             _struct.CXType],  # B
                            _type.c_uint]
clang_getCanonicalType: _Callable[[_struct.CXType],  # T
                                  _struct.CXType]
clang_isConstQualifiedType: _Callable[[_struct.CXType],  # T
                                      _type.c_uint]
clang_Cursor_isMacroFunctionLike: _Callable[[_struct.CXCursor],  # C
                                            _type.c_uint]
clang_Cursor_isMacroBuiltin: _Callable[[_struct.CXCursor],  # C
                                       _type.c_uint]
clang_Cursor_isFunctionInlined: _Callable[[_struct.CXCursor],  # C
                                          _type.c_uint]
clang_isVolatileQualifiedType: _Callable[[_struct.CXType],  # T
                                         _type.c_uint]
clang_isRestrictQualifiedType: _Callable[[_struct.CXType],  # T
                                         _type.c_uint]
clang_getAddressSpace: _Callable[[_struct.CXType],  # T
                                 _type.c_uint]
clang_getTypedefName: _Callable[[_struct.CXType],  # CT
                                _struct.CXString]
clang_getPointeeType: _Callable[[_struct.CXType],  # T
                                _struct.CXType]
clang_getTypeDeclaration: _Callable[[_struct.CXType],  # T
                                    _struct.CXCursor]
clang_getDeclObjCTypeEncoding: _Callable[[_struct.CXCursor],  # C
                                         _struct.CXString]
clang_Type_getObjCEncoding: _Callable[[_struct.CXType],  # type
                                      _struct.CXString]
clang_getTypeKindSpelling: _Callable[[_enum.CXTypeKind],  # K
                                     _struct.CXString]
clang_getFunctionTypeCallingConv: _Callable[[_struct.CXType],  # T
                                            _enum.CXCallingConv]
clang_getResultType: _Callable[[_struct.CXType],  # T
                               _struct.CXType]
clang_getExceptionSpecificationType: _Callable[[_struct.CXType],  # T
                                               _type.c_int]
clang_getNumArgTypes: _Callable[[_struct.CXType],  # T
                                _type.c_int]
clang_getArgType: _Callable[[_struct.CXType,  # T
                             _type.c_uint],  # i
                            _struct.CXType]
clang_Type_getObjCObjectBaseType: _Callable[[_struct.CXType],  # T
                                            _struct.CXType]
clang_Type_getNumObjCProtocolRefs: _Callable[[_struct.CXType],  # T
                                             _type.c_uint]
clang_Type_getObjCProtocolDecl: _Callable[[_struct.CXType,  # T
                                           _type.c_uint],  # i
                                          _struct.CXCursor]
clang_Type_getNumObjCTypeArgs: _Callable[[_struct.CXType],  # T
                                         _type.c_uint]
clang_Type_getObjCTypeArg: _Callable[[_struct.CXType,  # T
                                      _type.c_uint],  # i
                                     _struct.CXType]
clang_isFunctionTypeVariadic: _Callable[[_struct.CXType],  # T
                                        _type.c_uint]
clang_getCursorResultType: _Callable[[_struct.CXCursor],  # C
                                     _struct.CXType]
clang_getCursorExceptionSpecificationType: _Callable[[_struct.CXCursor],  # C
                                                     _type.c_int]
clang_isPODType: _Callable[[_struct.CXType],  # T
                           _type.c_uint]
clang_getElementType: _Callable[[_struct.CXType],  # T
                                _struct.CXType]
clang_getNumElements: _Callable[[_struct.CXType],  # T
                                _type.c_longlong]
clang_getArrayElementType: _Callable[[_struct.CXType],  # T
                                     _struct.CXType]
clang_getArraySize: _Callable[[_struct.CXType],  # T
                              _type.c_longlong]
clang_Type_getNamedType: _Callable[[_struct.CXType],  # T
                                   _struct.CXType]
clang_Type_isTransparentTagTypedef: _Callable[[_struct.CXType],  # T
                                              _type.c_uint]
clang_Type_getNullability: _Callable[[_struct.CXType],  # T
                                     _enum.CXTypeNullabilityKind]
clang_Type_getAlignOf: _Callable[[_struct.CXType],  # T
                                 _type.c_longlong]
clang_Type_getClassType: _Callable[[_struct.CXType],  # T
                                   _struct.CXType]
clang_Type_getSizeOf: _Callable[[_struct.CXType],  # T
                                _type.c_longlong]
clang_Type_getOffsetOf: _Callable[[_struct.CXType,  # T
                                   _type.c_char_p],  # S
                                  _type.c_longlong]
clang_Type_getModifiedType: _Callable[[_struct.CXType],  # T
                                      _struct.CXType]
clang_Type_getValueType: _Callable[[_struct.CXType],  # CT
                                   _struct.CXType]
clang_Cursor_getOffsetOfField: _Callable[[_struct.CXCursor],  # C
                                         _type.c_longlong]
clang_Cursor_isAnonymous: _Callable[[_struct.CXCursor],  # C
                                    _type.c_uint]
clang_Cursor_isAnonymousRecordDecl: _Callable[[_struct.CXCursor],  # C
                                              _type.c_uint]
clang_Cursor_isInlineNamespace: _Callable[[_struct.CXCursor],  # C
                                          _type.c_uint]
clang_Type_getNumTemplateArguments: _Callable[[_struct.CXType],  # T
                                              _type.c_int]
clang_Type_getTemplateArgumentAsType: _Callable[[_struct.CXType,  # T
                                                 _type.c_uint],  # i
                                                _struct.CXType]
clang_Type_getCXXRefQualifier: _Callable[[_struct.CXType],  # T
                                         _enum.CXRefQualifierKind]
clang_Cursor_isBitField: _Callable[[_struct.CXCursor],  # C
                                   _type.c_uint]
clang_isVirtualBase: _Callable[[_struct.CXCursor],
                               _type.c_uint]
clang_getCXXAccessSpecifier: _Callable[[_struct.CXCursor],
                                       _enum.CX_CXXAccessSpecifier]
clang_Cursor_getStorageClass: _Callable[[_struct.CXCursor],
                                        _enum.CX_StorageClass]
clang_getNumOverloadedDecls: _Callable[[_struct.CXCursor],  # cursor
                                       _type.c_uint]
clang_getOverloadedDecl: _Callable[[_struct.CXCursor,  # cursor
                                    _type.c_uint],  # index
                                   _struct.CXCursor]
clang_getIBOutletCollectionType: _Callable[[_struct.CXCursor],
                                           _struct.CXType]
clang_visitChildren: _Callable[[_struct.CXCursor,  # parent
                                _type.CXCursorVisitor,  # visitor
                                _type.CXClientData],  # client_data
                               _type.c_uint]
clang_getCursorUSR: _Callable[[_struct.CXCursor],
                              _struct.CXString]
clang_constructUSR_ObjCClass: _Callable[[_type.c_char_p],  # class_name
                                        _struct.CXString]
clang_constructUSR_ObjCCategory: _Callable[[_type.c_char_p,  # class_name
                                            _type.c_char_p],  # category_name
                                           _struct.CXString]
clang_constructUSR_ObjCProtocol: _Callable[[_type.c_char_p],  # protocol_name
                                           _struct.CXString]
clang_constructUSR_ObjCIvar: _Callable[[_type.c_char_p,  # name
                                        _struct.CXString],  # classUSR
                                       _struct.CXString]
clang_constructUSR_ObjCMethod: _Callable[[_type.c_char_p,  # name
                                          _type.c_uint,  # isInstanceMethod
                                          _struct.CXString],  # classUSR
                                         _struct.CXString]
clang_constructUSR_ObjCProperty: _Callable[[_type.c_char_p,  # property
                                            _struct.CXString],  # classUSR
                                           _struct.CXString]
clang_getCursorSpelling: _Callable[[_struct.CXCursor],
                                   _struct.CXString]
clang_Cursor_getSpellingNameRange: _Callable[[_struct.CXCursor,
                                              _type.c_uint,  # pieceIndex
                                              _type.c_uint],  # options
                                             _struct.CXSourceRange]
clang_PrintingPolicy_getProperty: _Callable[[_type.CXPrintingPolicy,  # Policy
                                             _enum.CXPrintingPolicyProperty],  # Property
                                            _type.c_uint]
clang_PrintingPolicy_setProperty: _Callable[[_type.CXPrintingPolicy,  # Policy
                                             _enum.CXPrintingPolicyProperty,  # Property
                                             _type.c_uint],  # Value
                                            _type.c_void]
clang_getCursorPrintingPolicy: _Callable[[_struct.CXCursor],
                                         _type.CXPrintingPolicy]
clang_PrintingPolicy_dispose: _Callable[[_type.CXPrintingPolicy],  # Policy
                                        _type.c_void]
clang_getCursorPrettyPrinted: _Callable[[_struct.CXCursor,  # Cursor
                                         _type.CXPrintingPolicy],  # Policy
                                        _struct.CXString]
clang_getCursorDisplayName: _Callable[[_struct.CXCursor],
                                      _struct.CXString]
clang_getCursorReferenced: _Callable[[_struct.CXCursor],
                                     _struct.CXCursor]
clang_getCursorDefinition: _Callable[[_struct.CXCursor],
                                     _struct.CXCursor]
clang_isCursorDefinition: _Callable[[_struct.CXCursor],
                                    _type.c_uint]
clang_getCanonicalCursor: _Callable[[_struct.CXCursor],
                                    _struct.CXCursor]
clang_Cursor_getObjCSelectorIndex: _Callable[[_struct.CXCursor],
                                             _type.c_int]
clang_Cursor_isDynamicCall: _Callable[[_struct.CXCursor],  # C
                                      _type.c_int]
clang_Cursor_getReceiverType: _Callable[[_struct.CXCursor],  # C
                                        _struct.CXType]
clang_Cursor_getObjCPropertyAttributes: _Callable[[_struct.CXCursor,  # C
                                                   _type.c_uint],  # reserved
                                                  _type.c_uint]
clang_Cursor_getObjCPropertyGetterName: _Callable[[_struct.CXCursor],  # C
                                                  _struct.CXString]
clang_Cursor_getObjCPropertySetterName: _Callable[[_struct.CXCursor],  # C
                                                  _struct.CXString]
clang_Cursor_getObjCDeclQualifiers: _Callable[[_struct.CXCursor],  # C
                                              _type.c_uint]
clang_Cursor_isObjCOptional: _Callable[[_struct.CXCursor],  # C
                                       _type.c_uint]
clang_Cursor_isVariadic: _Callable[[_struct.CXCursor],  # C
                                   _type.c_uint]
clang_Cursor_isExternalSymbol: _Callable[[_struct.CXCursor,  # C
                                          _Pointer[_struct.CXString],  # language
                                          _Pointer[_struct.CXString],  # definedIn
                                          _Pointer[_type.c_uint]],  # isGenerated
                                         _type.c_uint]
clang_Cursor_getCommentRange: _Callable[[_struct.CXCursor],  # C
                                        _struct.CXSourceRange]
clang_Cursor_getRawCommentText: _Callable[[_struct.CXCursor],  # C
                                          _struct.CXString]
clang_Cursor_getBriefCommentText: _Callable[[_struct.CXCursor],  # C
                                            _struct.CXString]
clang_Cursor_getMangling: _Callable[[_struct.CXCursor],
                                    _struct.CXString]
clang_Cursor_getCXXManglings: _Callable[[_struct.CXCursor],
                                        _Pointer[_struct.CXStringSet]]
clang_Cursor_getObjCManglings: _Callable[[_struct.CXCursor],
                                         _Pointer[_struct.CXStringSet]]
clang_Cursor_getModule: _Callable[[_struct.CXCursor],  # C
                                  _type.CXModule]
clang_getModuleForFile: _Callable[[_type.CXTranslationUnit,
                                   _type.CXFile],
                                  _type.CXModule]
clang_Module_getASTFile: _Callable[[_type.CXModule],  # Module
                                   _type.CXFile]
clang_Module_getParent: _Callable[[_type.CXModule],  # Module
                                  _type.CXModule]
clang_Module_getName: _Callable[[_type.CXModule],  # Module
                                _struct.CXString]
clang_Module_getFullName: _Callable[[_type.CXModule],  # Module
                                    _struct.CXString]
clang_Module_isSystem: _Callable[[_type.CXModule],  # Module
                                 _type.c_int]
clang_Module_getNumTopLevelHeaders: _Callable[[_type.CXTranslationUnit,
                                               _type.CXModule],  # Module
                                              _type.c_uint]
clang_Module_getTopLevelHeader: _Callable[[_type.CXTranslationUnit,
                                           _type.CXModule,  # Module
                                           _type.c_uint],  # Index
                                          _type.CXFile]
clang_CXXConstructor_isConvertingConstructor: _Callable[[_struct.CXCursor],  # C
                                                        _type.c_uint]
clang_CXXConstructor_isCopyConstructor: _Callable[[_struct.CXCursor],  # C
                                                  _type.c_uint]
clang_CXXConstructor_isDefaultConstructor: _Callable[[_struct.CXCursor],  # C
                                                     _type.c_uint]
clang_CXXConstructor_isMoveConstructor: _Callable[[_struct.CXCursor],  # C
                                                  _type.c_uint]
clang_CXXField_isMutable: _Callable[[_struct.CXCursor],  # C
                                    _type.c_uint]
clang_CXXMethod_isDefaulted: _Callable[[_struct.CXCursor],  # C
                                       _type.c_uint]
clang_CXXMethod_isPureVirtual: _Callable[[_struct.CXCursor],  # C
                                         _type.c_uint]
clang_CXXMethod_isStatic: _Callable[[_struct.CXCursor],  # C
                                    _type.c_uint]
clang_CXXMethod_isVirtual: _Callable[[_struct.CXCursor],  # C
                                     _type.c_uint]
clang_CXXRecord_isAbstract: _Callable[[_struct.CXCursor],  # C
                                      _type.c_uint]
clang_EnumDecl_isScoped: _Callable[[_struct.CXCursor],  # C
                                   _type.c_uint]
clang_CXXMethod_isConst: _Callable[[_struct.CXCursor],  # C
                                   _type.c_uint]
clang_getTemplateCursorKind: _Callable[[_struct.CXCursor],  # C
                                       _enum.CXCursorKind]
clang_getSpecializedCursorTemplate: _Callable[[_struct.CXCursor],  # C
                                              _struct.CXCursor]
clang_getCursorReferenceNameRange: _Callable[[_struct.CXCursor,  # C
                                              _type.c_uint,  # NameFlags
                                              _type.c_uint],  # PieceIndex
                                             _struct.CXSourceRange]
clang_getToken: _Callable[[_type.CXTranslationUnit,  # TU
                           _struct.CXSourceLocation],  # Location
                          _Pointer[_struct.CXToken]]
clang_getTokenKind: _Callable[[_struct.CXToken],
                              _enum.CXTokenKind]
clang_getTokenSpelling: _Callable[[_type.CXTranslationUnit,
                                   _struct.CXToken],
                                  _struct.CXString]
clang_getTokenLocation: _Callable[[_type.CXTranslationUnit,
                                   _struct.CXToken],
                                  _struct.CXSourceLocation]
clang_getTokenExtent: _Callable[[_type.CXTranslationUnit,
                                 _struct.CXToken],
                                _struct.CXSourceRange]
clang_tokenize: _Callable[[_type.CXTranslationUnit,  # TU
                           _struct.CXSourceRange,  # Range
                           _Pointer[_Pointer[_struct.CXToken]],  # Tokens
                           _Pointer[_type.c_uint]],  # NumTokens
                          _type.c_void]
clang_annotateTokens: _Callable[[_type.CXTranslationUnit,  # TU
                                 _Pointer[_struct.CXToken],  # Tokens
                                 _type.c_uint,  # NumTokens
                                 _Pointer[_struct.CXCursor]],  # Cursors
                                _type.c_void]
clang_disposeTokens: _Callable[[_type.CXTranslationUnit,  # TU
                                _Pointer[_struct.CXToken],  # Tokens
                                _type.c_uint],  # NumTokens
                               _type.c_void]
clang_getCursorKindSpelling: _Callable[[_enum.CXCursorKind],  # Kind
                                       _struct.CXString]
clang_getDefinitionSpellingAndExtent: _Callable[[_struct.CXCursor,
                                                 _Pointer[_type.c_char_p],  # startBuf
                                                 _Pointer[_type.c_char_p],  # endBuf
                                                 _Pointer[_type.c_uint],  # startLine
                                                 _Pointer[_type.c_uint],  # startColumn
                                                 _Pointer[_type.c_uint],  # endLine
                                                 _Pointer[_type.c_uint]],  # endColumn
                                                _type.c_void]
clang_enableStackTraces: _Callable[[],
                                   _type.c_void]
clang_executeOnThread: _Callable[[_type.c_void_p,  # fn
                                  _type.c_void_p,  # user_data
                                  _type.c_uint],  # stack_size
                                 _type.c_void]
clang_getCompletionChunkKind: _Callable[[_type.CXCompletionString,  # completion_string
                                         _type.c_uint],  # chunk_number
                                        _enum.CXCompletionChunkKind]
clang_getCompletionChunkText: _Callable[[_type.CXCompletionString,  # completion_string
                                         _type.c_uint],  # chunk_number
                                        _struct.CXString]
clang_getCompletionChunkCompletionString: _Callable[[_type.CXCompletionString,  # completion_string
                                                     _type.c_uint],  # chunk_number
                                                    _type.CXCompletionString]
clang_getNumCompletionChunks: _Callable[[_type.CXCompletionString],  # completion_string
                                        _type.c_uint]
clang_getCompletionPriority: _Callable[[_type.CXCompletionString],  # completion_string
                                       _type.c_uint]
clang_getCompletionAvailability: _Callable[[_type.CXCompletionString],  # completion_string
                                           _enum.CXAvailabilityKind]
clang_getCompletionNumAnnotations: _Callable[[_type.CXCompletionString],  # completion_string
                                             _type.c_uint]
clang_getCompletionAnnotation: _Callable[[_type.CXCompletionString,  # completion_string
                                          _type.c_uint],  # annotation_number
                                         _struct.CXString]
clang_getCompletionParent: _Callable[[_type.CXCompletionString,  # completion_string
                                      _Pointer[_enum.CXCursorKind]],  # kind
                                     _struct.CXString]
clang_getCompletionBriefComment: _Callable[[_type.CXCompletionString],  # completion_string
                                           _struct.CXString]
clang_getCursorCompletionString: _Callable[[_struct.CXCursor],  # cursor
                                           _type.CXCompletionString]
clang_getCompletionNumFixIts: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # results
                                         _type.c_uint],  # completion_index
                                        _type.c_uint]
clang_getCompletionFixIt: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # results
                                     _type.c_uint,  # completion_index
                                     _type.c_uint,  # fixit_index
                                     _Pointer[_struct.CXSourceRange]],  # replacement_range
                                    _struct.CXString]
clang_defaultCodeCompleteOptions: _Callable[[],
                                            _type.c_uint]
clang_codeCompleteAt: _Callable[[_type.CXTranslationUnit,  # TU
                                 _type.c_char_p,  # complete_filename
                                 _type.c_uint,  # complete_line
                                 _type.c_uint,  # complete_column
                                 _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                 _type.c_uint,  # num_unsaved_files
                                 _type.c_uint],  # options
                                _Pointer[_struct.CXCodeCompleteResults]]
clang_sortCodeCompletionResults: _Callable[[_Pointer[_struct.CXCompletionResult],  # Results
                                            _type.c_uint],  # NumResults
                                           _type.c_void]
clang_disposeCodeCompleteResults: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                            _type.c_void]
clang_codeCompleteGetNumDiagnostics: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                               _type.c_uint]
clang_codeCompleteGetDiagnostic: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # Results
                                            _type.c_uint],  # Index
                                           _type.CXDiagnostic]
clang_codeCompleteGetContexts: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                         _type.c_ulonglong]
clang_codeCompleteGetContainerKind: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # Results
                                               _Pointer[_type.c_uint]],  # IsIncomplete
                                              _enum.CXCursorKind]
clang_codeCompleteGetContainerUSR: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                             _struct.CXString]
clang_codeCompleteGetObjCSelector: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                             _struct.CXString]
clang_getClangVersion: _Callable[[],
                                 _struct.CXString]
clang_toggleCrashRecovery: _Callable[[_type.c_uint],  # isEnabled
                                     _type.c_void]
clang_getInclusions: _Callable[[_type.CXTranslationUnit,  # tu
                                _type.CXInclusionVisitor,  # visitor
                                _type.CXClientData],  # client_data
                               _type.c_void]
clang_Cursor_Evaluate: _Callable[[_struct.CXCursor],  # C
                                 _type.CXEvalResult]
clang_EvalResult_getKind: _Callable[[_type.CXEvalResult],  # E
                                    _enum.CXEvalResultKind]
clang_EvalResult_getAsInt: _Callable[[_type.CXEvalResult],  # E
                                     _type.c_int]
clang_EvalResult_getAsLongLong: _Callable[[_type.CXEvalResult],  # E
                                          _type.c_longlong]
clang_EvalResult_isUnsignedInt: _Callable[[_type.CXEvalResult],  # E
                                          _type.c_uint]
clang_EvalResult_getAsUnsigned: _Callable[[_type.CXEvalResult],  # E
                                          _type.c_ulonglong]
clang_EvalResult_getAsDouble: _Callable[[_type.CXEvalResult],  # E
                                        _type.c_double]
clang_EvalResult_getAsStr: _Callable[[_type.CXEvalResult],  # E
                                     _type.c_char_p]
clang_EvalResult_dispose: _Callable[[_type.CXEvalResult],  # E
                                    _type.c_void]
clang_getRemappings: _Callable[[_type.c_char_p],  # path
                               _type.CXRemapping]
clang_getRemappingsFromFileList: _Callable[[_Pointer[_type.c_char_p],  # filePaths
                                            _type.c_uint],  # numFiles
                                           _type.CXRemapping]
clang_remap_getNumFiles: _Callable[[_type.CXRemapping],
                                   _type.c_uint]
clang_remap_getFilenames: _Callable[[_type.CXRemapping,
                                     _type.c_uint,  # index
                                     _Pointer[_struct.CXString],  # original
                                     _Pointer[_struct.CXString]],  # transformed
                                    _type.c_void]
clang_remap_dispose: _Callable[[_type.CXRemapping],
                               _type.c_void]
clang_findReferencesInFile: _Callable[[_struct.CXCursor,  # cursor
                                       _type.CXFile,  # file
                                       _struct.CXCursorAndRangeVisitor],  # visitor
                                      _enum.CXResult]
clang_findIncludesInFile: _Callable[[_type.CXTranslationUnit,  # TU
                                     _type.CXFile,  # file
                                     _struct.CXCursorAndRangeVisitor],  # visitor
                                    _enum.CXResult]
clang_index_isEntityObjCContainerKind: _Callable[[_enum.CXIdxEntityKind],
                                                 _type.c_int]
clang_index_getObjCContainerDeclInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                                _Pointer[_struct.CXIdxObjCContainerDeclInfo]]
clang_index_getObjCInterfaceDeclInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                                _Pointer[_struct.CXIdxObjCInterfaceDeclInfo]]
clang_index_getObjCCategoryDeclInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                               _Pointer[_struct.CXIdxObjCCategoryDeclInfo]]
clang_index_getObjCProtocolRefListInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                                  _Pointer[_struct.CXIdxObjCProtocolRefListInfo]]
clang_index_getObjCPropertyDeclInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                               _Pointer[_struct.CXIdxObjCPropertyDeclInfo]]
clang_index_getIBOutletCollectionAttrInfo: _Callable[[_Pointer[_struct.CXIdxAttrInfo]],
                                                     _Pointer[_struct.CXIdxIBOutletCollectionAttrInfo]]
clang_index_getCXXClassDeclInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                           _Pointer[_struct.CXIdxCXXClassDeclInfo]]
clang_index_getClientContainer: _Callable[[_Pointer[_struct.CXIdxContainerInfo]],
                                          _type.CXIdxClientContainer]
clang_index_setClientContainer: _Callable[[_Pointer[_struct.CXIdxContainerInfo],
                                           _type.CXIdxClientContainer],
                                          _type.c_void]
clang_index_getClientEntity: _Callable[[_Pointer[_struct.CXIdxEntityInfo]],
                                       _type.CXIdxClientEntity]
clang_index_setClientEntity: _Callable[[_Pointer[_struct.CXIdxEntityInfo],
                                        _type.CXIdxClientEntity],
                                       _type.c_void]
clang_IndexAction_create: _Callable[[_type.CXIndex],  # CIdx
                                    _type.CXIndexAction]
clang_IndexAction_dispose: _Callable[[_type.CXIndexAction],
                                     _type.c_void]
clang_indexLoc_getFileLocation: _Callable[[_struct.CXIdxLoc,  # loc
                                           _Pointer[_type.CXIdxClientFile],  # indexFile
                                           _Pointer[_type.CXFile],  # file
                                           _Pointer[_type.c_uint],  # line
                                           _Pointer[_type.c_uint],  # column
                                           _Pointer[_type.c_uint]],  # offset
                                          _type.c_void]
clang_indexLoc_getCXSourceLocation: _Callable[[_struct.CXIdxLoc],  # loc
                                              _struct.CXSourceLocation]
clang_Type_visitFields: _Callable[[_struct.CXType,  # T
                                   _type.CXFieldVisitor,  # visitor
                                   _type.CXClientData],  # client_data
                                  _type.c_uint]
# Rewrite
clang_CXRewriter_create: _Callable[[_type.CXTranslationUnit],  # TU
                                   _type.CXRewriter]
clang_CXRewriter_insertTextBefore: _Callable[[_type.CXRewriter,  # Rew
                                              _struct.CXSourceLocation,  # Loc
                                              _type.c_char_p],  # Insert
                                             _type.c_void]
clang_CXRewriter_replaceText: _Callable[[_type.CXRewriter,  # Rew
                                         _struct.CXSourceRange,  # ToBeReplaced
                                         _type.c_char_p],  # Replacement
                                        _type.c_void]
clang_CXRewriter_removeText: _Callable[[_type.CXRewriter,  # Rew
                                        _struct.CXSourceRange],  # ToBeRemoved
                                       _type.c_void]
clang_CXRewriter_overwriteChangedFiles: _Callable[[_type.CXRewriter],  # Rew
                                                  _type.c_int]
clang_CXRewriter_writeMainFileToStdOut: _Callable[[_type.CXRewriter],  # Rew
                                                  _type.c_void]
clang_CXRewriter_dispose: _Callable[[_type.CXRewriter],  # Rew
                                    _type.c_void]

_CLib(__name__)

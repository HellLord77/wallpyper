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
"""
Return the timestamp for use with Clang's -fbuild-session-timestamp= option.
"""
clang_VirtualFileOverlay_create: _Callable[[_type.c_uint],  # options
                                           _type.CXVirtualFileOverlay]
"""
Create a CXVirtualFileOverlay object. Must be disposed with
clang_VirtualFileOverlay_dispose().
"""
clang_VirtualFileOverlay_addFileMapping: _Callable[[_type.CXVirtualFileOverlay,
                                                    _type.c_char_p,  # virtualPath
                                                    _type.c_char_p],  # realPath
                                                   _enum.CXErrorCode]
"""
Map an absolute virtual file path to an absolute real one. The virtual path must
be canonicalized (not contain "."/"..").
"""
clang_VirtualFileOverlay_setCaseSensitivity: _Callable[[_type.CXVirtualFileOverlay,
                                                        _type.c_int],  # caseSensitive
                                                       _enum.CXErrorCode]
"""
Set the case sensitivity for the CXVirtualFileOverlay object. The
CXVirtualFileOverlay object is case-sensitive by default, this option can be
used to override the default.
"""
clang_VirtualFileOverlay_writeToBuffer: _Callable[[_type.CXVirtualFileOverlay,
                                                   _type.c_uint,  # options
                                                   _Pointer[_type.c_char_p],  # out_buffer_ptr
                                                   _Pointer[_type.c_uint]],  # out_buffer_size
                                                  _enum.CXErrorCode]
"""
Write out the CXVirtualFileOverlay object to a char buffer.
"""
clang_free: _Callable[[_type.c_void_p],  # buffer
                      _type.c_void]
"""
free memory allocated by libclang, such as the buffer returned by
CXVirtualFileOverlay() or clang_ModuleMapDescriptor_writeToBuffer().
"""
clang_VirtualFileOverlay_dispose: _Callable[[_type.CXVirtualFileOverlay],
                                            _type.c_void]
"""
Dispose a CXVirtualFileOverlay object.
"""
clang_ModuleMapDescriptor_create: _Callable[[_type.c_uint],  # options
                                            _type.CXModuleMapDescriptor]
"""
Create a CXModuleMapDescriptor object. Must be disposed with
clang_ModuleMapDescriptor_dispose().
"""
clang_ModuleMapDescriptor_setFrameworkModuleName: _Callable[[_type.CXModuleMapDescriptor,
                                                             _type.c_char_p],  # name
                                                            _enum.CXErrorCode]
"""
Sets the framework module name that the module.map describes.
"""
clang_ModuleMapDescriptor_setUmbrellaHeader: _Callable[[_type.CXModuleMapDescriptor,
                                                        _type.c_char_p],  # name
                                                       _enum.CXErrorCode]
"""
Sets the umbrella header name that the module.map describes.
"""
clang_ModuleMapDescriptor_writeToBuffer: _Callable[[_type.CXModuleMapDescriptor,
                                                    _type.c_uint,  # options
                                                    _Pointer[_type.c_char_p],  # out_buffer_ptr
                                                    _Pointer[_type.c_uint]],  # out_buffer_size
                                                   _enum.CXErrorCode]
"""
Write out the CXModuleMapDescriptor object to a char buffer.
"""
clang_ModuleMapDescriptor_dispose: _Callable[[_type.CXModuleMapDescriptor],
                                             _type.c_void]
"""
Dispose a CXModuleMapDescriptor object.
"""
# CXCompilationDatabase
clang_CompilationDatabase_fromDirectory: _Callable[[_type.c_char_p,  # BuildDir
                                                    _Pointer[_enum.CXCompilationDatabase_Error]],  # ErrorCode
                                                   _type.CXCompilationDatabase]
"""
Creates a compilation database from the database found in directory buildDir.
For example, CMake can output a compile_commands.json which can be used to build
the database.
"""
clang_CompilationDatabase_dispose: _Callable[[_type.CXCompilationDatabase],
                                             _type.c_void]
"""
Free the given compilation database
"""
clang_CompilationDatabase_getCompileCommands: _Callable[[_type.CXCompilationDatabase,
                                                         _type.c_char_p],  # CompleteFileName
                                                        _type.CXCompileCommands]
"""
Find the compile commands used for a file. The compile commands must be freed by
clang_CompileCommands_dispose.
"""
clang_CompilationDatabase_getAllCompileCommands: _Callable[[_type.CXCompilationDatabase],
                                                           _type.CXCompileCommands]
"""
Get all the compile commands in the given compilation database.
"""
clang_CompileCommands_dispose: _Callable[[_type.CXCompileCommands],
                                         _type.c_void]
"""
Free the given CompileCommands
"""
clang_CompileCommands_getSize: _Callable[[_type.CXCompileCommands],
                                         _type.c_uint]
"""
Get the number of CompileCommand we have for a file
"""
clang_CompileCommands_getCommand: _Callable[[_type.CXCompileCommands,
                                             _type.c_uint],  # I
                                            _type.CXCompileCommand]
"""
Get the I'th CompileCommand for a file
"""
clang_CompileCommand_getDirectory: _Callable[[_type.CXCompileCommand],
                                             _struct.CXString]
"""
Get the working directory where the CompileCommand was executed from
"""
clang_CompileCommand_getFilename: _Callable[[_type.CXCompileCommand],
                                            _struct.CXString]
"""
Get the filename associated with the CompileCommand.
"""
clang_CompileCommand_getNumArgs: _Callable[[_type.CXCompileCommand],
                                           _type.c_uint]
"""
Get the number of arguments in the compiler invocation.
"""
clang_CompileCommand_getArg: _Callable[[_type.CXCompileCommand,
                                        _type.c_uint],  # I
                                       _struct.CXString]
"""
Get the I'th argument value in the compiler invocations
"""
clang_CompileCommand_getNumMappedSources: _Callable[[_type.CXCompileCommand],
                                                    _type.c_uint]
"""
Get the number of source mappings for the compiler invocation.
"""
clang_CompileCommand_getMappedSourcePath: _Callable[[_type.CXCompileCommand,
                                                     _type.c_uint],  # I
                                                    _struct.CXString]
"""
Get the I'th mapped source path for the compiler invocation.
"""
clang_CompileCommand_getMappedSourceContent: _Callable[[_type.CXCompileCommand,
                                                        _type.c_uint],  # I
                                                       _struct.CXString]
"""
Get the I'th mapped source content for the compiler invocation.
"""
# CXString
clang_getCString: _Callable[[_struct.CXString],  # string
                            _type.c_char_p]
"""
Retrieve the character data associated with the given string.
"""
clang_disposeString: _Callable[[_struct.CXString],  # string
                               _type.c_void]
"""
Free the given string.
"""
clang_disposeStringSet: _Callable[[_Pointer[_struct.CXStringSet]],  # set
                                  _type.c_void]
"""
Free the given string set.
"""
# Documentation
clang_Cursor_getParsedComment: _Callable[[_struct.CXCursor],  # C
                                         _struct.CXComment]
"""
Given a cursor that represents a documentable entity (e.g., declaration), return
the associated parsed comment as a CXComment_FullComment AST node.
"""
clang_Comment_getKind: _Callable[[_struct.CXComment],  # Comment
                                 _enum.CXCommentKind]
"""
Returns the type of the AST node.
"""
clang_Comment_getNumChildren: _Callable[[_struct.CXComment],  # Comment
                                        _type.c_uint]
"""
Returns number of children of the AST node.
"""
clang_Comment_getChild: _Callable[[_struct.CXComment,  # Comment
                                   _type.c_uint],  # ChildIdx
                                  _struct.CXComment]
"""
Returns the specified child of the AST node.
"""
clang_Comment_isWhitespace: _Callable[[_struct.CXComment],  # Comment
                                      _type.c_uint]
"""
A CXComment_Paragraph node is considered whitespace if it contains only
CXComment_Text nodes that are empty or whitespace.
"""
clang_InlineContentComment_hasTrailingNewline: _Callable[[_struct.CXComment],  # Comment
                                                         _type.c_uint]
"""
Returns non-zero if Comment is inline content and has a newline immediately
following it in the comment text. Newlines between paragraphs do not count.
"""
clang_TextComment_getText: _Callable[[_struct.CXComment],  # Comment
                                     _struct.CXString]
"""
Returns text contained in the AST node.
"""
clang_InlineCommandComment_getCommandName: _Callable[[_struct.CXComment],  # Comment
                                                     _struct.CXString]
"""
Returns name of the inline command.
"""
clang_InlineCommandComment_getRenderKind: _Callable[[_struct.CXComment],  # Comment
                                                    _enum.CXCommentInlineCommandRenderKind]
"""
Returns the most appropriate rendering mode, chosen on command semantics in
Doxygen.
"""
clang_InlineCommandComment_getNumArgs: _Callable[[_struct.CXComment],  # Comment
                                                 _type.c_uint]
"""
Returns number of command arguments.
"""
clang_InlineCommandComment_getArgText: _Callable[[_struct.CXComment,  # Comment
                                                  _type.c_uint],  # ArgIdx
                                                 _struct.CXString]
"""
Returns text of the specified argument.
"""
clang_HTMLTagComment_getTagName: _Callable[[_struct.CXComment],  # Comment
                                           _struct.CXString]
"""
Returns HTML tag name.
"""
clang_HTMLStartTagComment_isSelfClosing: _Callable[[_struct.CXComment],  # Comment
                                                   _type.c_uint]
"""
Returns non-zero if tag is self-closing (for example, <br />).
"""
clang_HTMLStartTag_getNumAttrs: _Callable[[_struct.CXComment],  # Comment
                                          _type.c_uint]
"""
Returns number of attributes (name-value pairs) attached to the start tag.
"""
clang_HTMLStartTag_getAttrName: _Callable[[_struct.CXComment,  # Comment
                                           _type.c_uint],  # AttrIdx
                                          _struct.CXString]
"""
Returns name of the specified attribute.
"""
clang_HTMLStartTag_getAttrValue: _Callable[[_struct.CXComment,  # Comment
                                            _type.c_uint],  # AttrIdx
                                           _struct.CXString]
"""
Returns value of the specified attribute.
"""
clang_BlockCommandComment_getCommandName: _Callable[[_struct.CXComment],  # Comment
                                                    _struct.CXString]
"""
Returns name of the block command.
"""
clang_BlockCommandComment_getNumArgs: _Callable[[_struct.CXComment],  # Comment
                                                _type.c_uint]
"""
Returns number of word-like arguments.
"""
clang_BlockCommandComment_getArgText: _Callable[[_struct.CXComment,  # Comment
                                                 _type.c_uint],  # ArgIdx
                                                _struct.CXString]
"""
Returns text of the specified word-like argument.
"""
clang_BlockCommandComment_getParagraph: _Callable[[_struct.CXComment],  # Comment
                                                  _struct.CXComment]
"""
Returns paragraph argument of the block command.
"""
clang_ParamCommandComment_getParamName: _Callable[[_struct.CXComment],  # Comment
                                                  _struct.CXString]
"""
Returns parameter name.
"""
clang_ParamCommandComment_isParamIndexValid: _Callable[[_struct.CXComment],  # Comment
                                                       _type.c_uint]
"""
Returns non-zero if the parameter that this AST node represents was found in the
function prototype and clang_ParamCommandComment_getParamIndex function will
return a meaningful value.
"""
clang_ParamCommandComment_getParamIndex: _Callable[[_struct.CXComment],  # Comment
                                                   _type.c_uint]
"""
Returns zero-based parameter index in function prototype.
"""
clang_ParamCommandComment_isDirectionExplicit: _Callable[[_struct.CXComment],  # Comment
                                                         _type.c_uint]
"""
Returns non-zero if parameter passing direction was specified explicitly in the
comment.
"""
clang_ParamCommandComment_getDirection: _Callable[[_struct.CXComment],  # Comment
                                                  _enum.CXCommentParamPassDirection]
"""
Returns parameter passing direction.
"""
clang_TParamCommandComment_getParamName: _Callable[[_struct.CXComment],  # Comment
                                                   _struct.CXString]
"""
Returns template parameter name.
"""
clang_TParamCommandComment_isParamPositionValid: _Callable[[_struct.CXComment],  # Comment
                                                           _type.c_uint]
"""
Returns non-zero if the parameter that this AST node represents was found in the
template parameter list and clang_TParamCommandComment_getDepth and
clang_TParamCommandComment_getIndex functions will return a meaningful value.
"""
clang_TParamCommandComment_getDepth: _Callable[[_struct.CXComment],  # Comment
                                               _type.c_uint]
"""
Returns zero-based nesting depth of this parameter in the template parameter
list.
"""
clang_TParamCommandComment_getIndex: _Callable[[_struct.CXComment,  # Comment
                                                _type.c_uint],  # Depth
                                               _type.c_uint]
"""
Returns zero-based parameter index in the template parameter list at a given
nesting depth.
"""
clang_VerbatimBlockLineComment_getText: _Callable[[_struct.CXComment],  # Comment
                                                  _struct.CXString]
"""
Returns text contained in the AST node.
"""
clang_VerbatimLineComment_getText: _Callable[[_struct.CXComment],  # Comment
                                             _struct.CXString]
"""
Returns text contained in the AST node.
"""
clang_HTMLTagComment_getAsString: _Callable[[_struct.CXComment],  # Comment
                                            _struct.CXString]
"""
Convert an HTML tag AST node to string.
"""
clang_FullComment_getAsHTML: _Callable[[_struct.CXComment],  # Comment
                                       _struct.CXString]
"""
Convert a given full parsed comment to an HTML fragment.
"""
clang_FullComment_getAsXML: _Callable[[_struct.CXComment],  # Comment
                                      _struct.CXString]
"""
Convert a given full parsed comment to an XML document.
"""
# Index
clang_createIndex: _Callable[[_type.c_int,  # excludeDeclarationsFromPCH
                              _type.c_int],  # displayDiagnostics
                             _type.CXIndex]
"""
Provides a shared context for creating translation units.
"""
clang_disposeIndex: _Callable[[_type.CXIndex],  # index
                              _type.c_void]
"""
Destroy the given index.
"""
clang_CXIndex_setGlobalOptions: _Callable[[_type.CXIndex,
                                           _type.c_uint],  # options
                                          _type.c_void]
"""
Sets general options associated with a CXIndex.
"""
clang_CXIndex_getGlobalOptions: _Callable[[_type.CXIndex],
                                          _type.c_uint]
"""
Gets the general options associated with a CXIndex.
"""
clang_CXIndex_setInvocationEmissionPathOption: _Callable[[_type.CXIndex,
                                                          _type.c_char_p],  # Path
                                                         _type.c_void]
"""
Sets the invocation emission path option in a CXIndex.
"""
clang_getFileName: _Callable[[_type.CXFile],  # SFile
                             _struct.CXString]
"""
Retrieve the complete file and path name of the given file.
"""
clang_getFileTime: _Callable[[_type.CXFile],  # SFile
                             _type.time_t]
"""
Retrieve the last modification time of the given file.
"""
clang_getFileUniqueID: _Callable[[_type.CXFile,  # file
                                  _Pointer[_struct.CXFileUniqueID]],  # outID
                                 _type.c_int]
"""
Retrieve the unique ID for the given file.
"""
clang_isFileMultipleIncludeGuarded: _Callable[[_type.CXTranslationUnit,  # tu
                                               _type.CXFile],  # file
                                              _type.c_uint]
"""
Determine whether the given header is guarded against multiple inclusions,
either with the conventional #ifndef/#define/#endif macro guards or with #pragma
once.
"""
clang_getFile: _Callable[[_type.CXTranslationUnit,  # tu
                          _type.c_char_p],  # file_name
                         _type.CXFile]
"""
Retrieve a file handle within the given translation unit.
"""
clang_getFileContents: _Callable[[_type.CXTranslationUnit,  # tu
                                  _type.CXFile,  # file
                                  _Pointer[_type.c_size_t]],  # size
                                 _type.c_char_p]
"""
Retrieve the buffer associated with the given file.
"""
clang_File_isEqual: _Callable[[_type.CXFile,  # file1
                               _type.CXFile],  # file2
                              _type.c_int]
"""
Returns non-zero if the file1 and file2 point to the same file, or they are both
NULL.
"""
clang_File_tryGetRealPathName: _Callable[[_type.CXFile],  # file
                                         _struct.CXString]
"""
Returns the real path name of file.
"""
clang_getNullLocation: _Callable[[],
                                 _struct.CXSourceLocation]
"""
Retrieve a NULL (invalid) source location.
"""
clang_equalLocations: _Callable[[_struct.CXSourceLocation,  # loc1
                                 _struct.CXSourceLocation],  # loc2
                                _type.c_uint]
"""
Determine whether two source locations, which must refer into the same
translation unit, refer to exactly the same point in the source code.
"""
clang_getLocation: _Callable[[_type.CXTranslationUnit,  # tu
                              _type.CXFile,  # file
                              _type.c_uint,  # line
                              _type.c_uint],  # column
                             _struct.CXSourceLocation]
"""
Retrieves the source location associated with a given file/line/column in a
particular translation unit.
"""
clang_getLocationForOffset: _Callable[[_type.CXTranslationUnit,  # tu
                                       _type.CXFile,  # file
                                       _type.c_uint],  # offset
                                      _struct.CXSourceLocation]
"""
Retrieves the source location associated with a given character offset in a
particular translation unit.
"""
clang_Location_isInSystemHeader: _Callable[[_struct.CXSourceLocation],  # location
                                           _type.c_int]
"""
Returns non-zero if the given source location is in a system header.
"""
clang_Location_isFromMainFile: _Callable[[_struct.CXSourceLocation],  # location
                                         _type.c_int]
"""
Returns non-zero if the given source location is in the main file of the
corresponding translation unit.
"""
clang_getNullRange: _Callable[[],
                              _struct.CXSourceRange]
"""
Retrieve a NULL (invalid) source range.
"""
clang_getRange: _Callable[[_struct.CXSourceLocation,  # begin
                           _struct.CXSourceLocation],  # end
                          _struct.CXSourceRange]
"""
Retrieve a source range given the beginning and ending source locations.
"""
clang_equalRanges: _Callable[[_struct.CXSourceRange,  # range1
                              _struct.CXSourceRange],  # range2
                             _type.c_uint]
"""
Determine whether two ranges are equivalent.
"""
clang_Range_isNull: _Callable[[_struct.CXSourceRange],  # range
                              _type.c_int]
"""
Returns non-zero if range is null.
"""
clang_getExpansionLocation: _Callable[[_struct.CXSourceLocation,  # location
                                       _Pointer[_type.CXFile],  # file
                                       _Pointer[_type.c_uint],  # line
                                       _Pointer[_type.c_uint],  # column
                                       _Pointer[_type.c_uint]],  # offset
                                      _type.c_void]
"""
Retrieve the file, line, column, and offset represented by the given source
location.
"""
clang_getPresumedLocation: _Callable[[_struct.CXSourceLocation,  # location
                                      _Pointer[_struct.CXString],  # filename
                                      _Pointer[_type.c_uint],  # line
                                      _Pointer[_type.c_uint]],  # column
                                     _type.c_void]
"""
Retrieve the file, line and column represented by the given source location, as
specified in a # line directive.
"""
clang_getInstantiationLocation: _Callable[[_struct.CXSourceLocation,  # location
                                           _Pointer[_type.CXFile],  # file
                                           _Pointer[_type.c_uint],  # line
                                           _Pointer[_type.c_uint],  # column
                                           _Pointer[_type.c_uint]],  # offset
                                          _type.c_void]
"""
Legacy API to retrieve the file, line, column, and offset represented by the
given source location.
"""
clang_getSpellingLocation: _Callable[[_struct.CXSourceLocation,  # location
                                      _Pointer[_type.CXFile],  # file
                                      _Pointer[_type.c_uint],  # line
                                      _Pointer[_type.c_uint],  # column
                                      _Pointer[_type.c_uint]],  # offset
                                     _type.c_void]
"""
Retrieve the file, line, column, and offset represented by the given source
location.
"""
clang_getFileLocation: _Callable[[_struct.CXSourceLocation,  # location
                                  _Pointer[_type.CXFile],  # file
                                  _Pointer[_type.c_uint],  # line
                                  _Pointer[_type.c_uint],  # column
                                  _Pointer[_type.c_uint]],  # offset
                                 _type.c_void]
"""
Retrieve the file, line, column, and offset represented by the given source
location.
"""
clang_getRangeStart: _Callable[[_struct.CXSourceRange],  # range
                               _struct.CXSourceLocation]
"""
Retrieve a source location representing the first character within a source
range.
"""
clang_getRangeEnd: _Callable[[_struct.CXSourceRange],  # range
                             _struct.CXSourceLocation]
"""
Retrieve a source location representing the last character within a source
range.
"""
clang_getSkippedRanges: _Callable[[_type.CXTranslationUnit,  # tu
                                   _type.CXFile],  # file
                                  _Pointer[_struct.CXSourceRangeList]]
"""
Retrieve all ranges that were skipped by the preprocessor.
"""
clang_getAllSkippedRanges: _Callable[[_type.CXTranslationUnit],  # tu
                                     _Pointer[_struct.CXSourceRangeList]]
"""
Retrieve all ranges from all files that were skipped by the preprocessor.
"""
clang_disposeSourceRangeList: _Callable[[_Pointer[_struct.CXSourceRangeList]],  # ranges
                                        _type.c_void]
"""
Destroy the given CXSourceRangeList.
"""
clang_getNumDiagnosticsInSet: _Callable[[_type.CXDiagnosticSet],  # Diags
                                        _type.c_uint]
"""
Determine the number of diagnostics in a CXDiagnosticSet.
"""
clang_getDiagnosticInSet: _Callable[[_type.CXDiagnosticSet,  # Diags
                                     _type.c_uint],  # Index
                                    _type.CXDiagnostic]
"""
Retrieve a diagnostic associated with the given CXDiagnosticSet.
"""
clang_loadDiagnostics: _Callable[[_type.c_char_p,  # file
                                  _Pointer[_enum.CXLoadDiag_Error],  # error
                                  _Pointer[_struct.CXString]],  # errorString
                                 _type.CXDiagnosticSet]
"""
Deserialize a set of diagnostics from a Clang diagnostics bitcode file.
"""
clang_disposeDiagnosticSet: _Callable[[_type.CXDiagnosticSet],  # Diags
                                      _type.c_void]
"""
Release a CXDiagnosticSet and all of its contained diagnostics.
"""
clang_getChildDiagnostics: _Callable[[_type.CXDiagnostic],  # D
                                     _type.CXDiagnosticSet]
"""
Retrieve the child diagnostics of a CXDiagnostic.
"""
clang_getNumDiagnostics: _Callable[[_type.CXTranslationUnit],  # Unit
                                   _type.c_uint]
"""
Determine the number of diagnostics produced for the given translation unit.
"""
clang_getDiagnostic: _Callable[[_type.CXTranslationUnit,  # Unit
                                _type.c_uint],  # Index
                               _type.CXDiagnostic]
"""
Retrieve a diagnostic associated with the given translation unit.
"""
clang_getDiagnosticSetFromTU: _Callable[[_type.CXTranslationUnit],  # Unit
                                        _type.CXDiagnosticSet]
"""
Retrieve the complete set of diagnostics associated with a translation unit.
"""
clang_disposeDiagnostic: _Callable[[_type.CXDiagnostic],  # Diagnostic
                                   _type.c_void]
"""
Destroy a diagnostic.
"""
clang_formatDiagnostic: _Callable[[_type.CXDiagnostic,  # Diagnostic
                                   _type.c_uint],  # Options
                                  _struct.CXString]
"""
Format the given diagnostic in a manner that is suitable for display.
"""
clang_defaultDiagnosticDisplayOptions: _Callable[[],
                                                 _type.c_uint]
"""
Retrieve the set of display options most similar to the default behavior of the
clang compiler.
"""
clang_getDiagnosticSeverity: _Callable[[_type.CXDiagnostic],
                                       _enum.CXDiagnosticSeverity]
"""
Determine the severity of the given diagnostic.
"""
clang_getDiagnosticLocation: _Callable[[_type.CXDiagnostic],
                                       _struct.CXSourceLocation]
"""
Retrieve the source location of the given diagnostic.
"""
clang_getDiagnosticSpelling: _Callable[[_type.CXDiagnostic],
                                       _struct.CXString]
"""
Retrieve the text of the given diagnostic.
"""
clang_getDiagnosticOption: _Callable[[_type.CXDiagnostic,  # Diag
                                      _Pointer[_struct.CXString]],  # Disable
                                     _struct.CXString]
"""
Retrieve the name of the command-line option that enabled this diagnostic.
"""
clang_getDiagnosticCategory: _Callable[[_type.CXDiagnostic],
                                       _type.c_uint]
"""
Retrieve the category number for this diagnostic.
"""
clang_getDiagnosticCategoryName: _Callable[[_type.c_uint],  # Category
                                           _struct.CXString]
"""
Retrieve the name of a particular diagnostic category. This is now deprecated.
Use clang_getDiagnosticCategoryText() instead.
"""
clang_getDiagnosticCategoryText: _Callable[[_type.CXDiagnostic],
                                           _struct.CXString]
"""
Retrieve the diagnostic category text for a given diagnostic.
"""
clang_getDiagnosticNumRanges: _Callable[[_type.CXDiagnostic],
                                        _type.c_uint]
"""
Determine the number of source ranges associated with the given diagnostic.
"""
clang_getDiagnosticRange: _Callable[[_type.CXDiagnostic,  # Diagnostic
                                     _type.c_uint],  # Range
                                    _struct.CXSourceRange]
"""
Retrieve a source range associated with the diagnostic.
"""
clang_getDiagnosticNumFixIts: _Callable[[_type.CXDiagnostic],  # Diagnostic
                                        _type.c_uint]
"""
Determine the number of fix-it hints associated with the given diagnostic.
"""
clang_getDiagnosticFixIt: _Callable[[_type.CXDiagnostic,  # Diagnostic
                                     _type.c_uint,  # FixIt
                                     _Pointer[_struct.CXSourceRange]],  # ReplacementRange
                                    _struct.CXString]
"""
Retrieve the replacement information for a given fix-it.
"""
clang_getTranslationUnitSpelling: _Callable[[_type.CXTranslationUnit],  # CTUnit
                                            _struct.CXString]
"""
Get the original translation unit source file name.
"""
clang_createTranslationUnitFromSourceFile: _Callable[[_type.CXIndex,  # CIdx
                                                      _type.c_char_p,  # source_filename
                                                      _type.c_int,  # num_clang_command_line_args
                                                      _Pointer[_type.c_char_p],  # clang_command_line_args
                                                      _type.c_uint,  # num_unsaved_files
                                                      _Pointer[_struct.CXUnsavedFile]],  # unsaved_files
                                                     _type.CXTranslationUnit]
"""
Return the CXTranslationUnit for a given source file and the provided command
line arguments one would pass to the compiler.
"""
clang_createTranslationUnit: _Callable[[_type.CXIndex,  # CIdx
                                        _type.c_char_p],  # ast_filename
                                       _type.CXTranslationUnit]
"""
Same as clang_createTranslationUnit2, but returns the CXTranslationUnit instead
of an error code. In case of an error this routine returns a NULL
CXTranslationUnit, without further detailed error codes.
"""
clang_createTranslationUnit2: _Callable[[_type.CXIndex,  # CIdx
                                         _type.c_char_p,  # ast_filename
                                         _Pointer[_type.CXTranslationUnit]],  # out_TU
                                        _enum.CXErrorCode]
"""
Create a translation unit from an AST file ( -emit-ast).
"""
clang_defaultEditingTranslationUnitOptions: _Callable[[],
                                                      _type.c_uint]
"""
Returns the set of flags that is suitable for parsing a translation unit that is
being edited.
"""
clang_parseTranslationUnit: _Callable[[_type.CXIndex,  # CIdx
                                       _type.c_char_p,  # source_filename
                                       _Pointer[_type.c_char_p],  # command_line_args
                                       _type.c_int,  # num_command_line_args
                                       _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                       _type.c_uint,  # num_unsaved_files
                                       _type.c_uint],  # options
                                      _type.CXTranslationUnit]
"""
Same as clang_parseTranslationUnit2, but returns the CXTranslationUnit instead
of an error code. In case of an error this routine returns a NULL
CXTranslationUnit, without further detailed error codes.
"""
clang_parseTranslationUnit2: _Callable[[_type.CXIndex,  # CIdx
                                        _type.c_char_p,  # source_filename
                                        _Pointer[_type.c_char_p],  # command_line_args
                                        _type.c_int,  # num_command_line_args
                                        _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                        _type.c_uint,  # num_unsaved_files
                                        _type.c_uint,  # options
                                        _Pointer[_type.CXTranslationUnit]],  # out_TU
                                       _enum.CXErrorCode]
"""
Parse the given source file and the translation unit corresponding to that file.
"""
clang_parseTranslationUnit2FullArgv: _Callable[[_type.CXIndex,  # CIdx
                                                _type.c_char_p,  # source_filename
                                                _Pointer[_type.c_char_p],  # command_line_args
                                                _type.c_int,  # num_command_line_args
                                                _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                                _type.c_uint,  # num_unsaved_files
                                                _type.c_uint,  # options
                                                _Pointer[_type.CXTranslationUnit]],  # out_TU
                                               _enum.CXErrorCode]
"""
Same as clang_parseTranslationUnit2 but requires a full command line for
command_line_args including argv[0]. This is useful if the standard library
paths are relative to the binary.
"""
clang_defaultSaveOptions: _Callable[[_type.CXTranslationUnit],  # TU
                                    _type.c_uint]
"""
Returns the set of flags that is suitable for saving a translation unit.
"""
clang_saveTranslationUnit: _Callable[[_type.CXTranslationUnit,  # TU
                                      _type.c_char_p,  # FileName
                                      _type.c_uint],  # options
                                     _type.c_int]
"""
Saves a translation unit into a serialized representation of that translation
unit on disk.
"""
clang_suspendTranslationUnit: _Callable[[_type.CXTranslationUnit],
                                        _type.c_uint]
"""
Suspend a translation unit in order to free memory associated with it.
"""
clang_disposeTranslationUnit: _Callable[[_type.CXTranslationUnit],
                                        _type.c_void]
"""
Destroy the specified CXTranslationUnit object.
"""
clang_defaultReparseOptions: _Callable[[_type.CXTranslationUnit],  # TU
                                       _type.c_uint]
"""
Returns the set of flags that is suitable for reparsing a translation unit.
"""
clang_reparseTranslationUnit: _Callable[[_type.CXTranslationUnit,  # TU
                                         _type.c_uint,  # num_unsaved_files
                                         _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                         _type.c_uint],  # options
                                        _type.c_int]
"""
Reparse the source files that produced this translation unit.
"""
clang_getTUResourceUsageName: _Callable[[_enum.CXTUResourceUsageKind],  # kind
                                        _type.c_char_p]
"""
Returns the human-readable null-terminated C string that represents the name of
the memory category. This string should never be freed.
"""
clang_getCXTUResourceUsage: _Callable[[_type.CXTranslationUnit],  # TU
                                      _struct.CXTUResourceUsage]
"""
Return the memory usage of a translation unit. This object should be released
with clang_disposeCXTUResourceUsage().
"""
clang_disposeCXTUResourceUsage: _Callable[[_struct.CXTUResourceUsage],  # usage
                                          _type.c_void]
clang_getTranslationUnitTargetInfo: _Callable[[_type.CXTranslationUnit],  # CTUnit
                                              _type.CXTargetInfo]
"""
Get target information for this translation unit.
"""
clang_TargetInfo_dispose: _Callable[[_type.CXTargetInfo],  # Info
                                    _type.c_void]
"""
Destroy the CXTargetInfo object.
"""
clang_TargetInfo_getTriple: _Callable[[_type.CXTargetInfo],  # Info
                                      _struct.CXString]
"""
Get the normalized target triple as a string.
"""
clang_TargetInfo_getPointerWidth: _Callable[[_type.CXTargetInfo],  # Info
                                            _type.c_int]
"""
Get the pointer width of the target in bits.
"""
clang_getNullCursor: _Callable[[],
                               _struct.CXCursor]
"""
Retrieve the NULL cursor, which represents no entity.
"""
clang_getTranslationUnitCursor: _Callable[[_type.CXTranslationUnit],
                                          _struct.CXCursor]
"""
Retrieve the cursor that represents the given translation unit.
"""
clang_equalCursors: _Callable[[_struct.CXCursor,
                               _struct.CXCursor],
                              _type.c_uint]
"""
Determine whether two cursors are equivalent.
"""
clang_Cursor_isNull: _Callable[[_struct.CXCursor],  # cursor
                               _type.c_int]
"""
Returns non-zero if cursor is null.
"""
clang_hashCursor: _Callable[[_struct.CXCursor],
                            _type.c_uint]
"""
Compute a hash value for the given cursor.
"""
clang_getCursorKind: _Callable[[_struct.CXCursor],
                               _enum.CXCursorKind]
"""
Retrieve the kind of the given cursor.
"""
clang_isDeclaration: _Callable[[_enum.CXCursorKind],
                               _type.c_uint]
"""
Determine whether the given cursor kind represents a declaration.
"""
clang_isInvalidDeclaration: _Callable[[_struct.CXCursor],
                                      _type.c_uint]
"""
Determine whether the given declaration is invalid.
"""
clang_isReference: _Callable[[_enum.CXCursorKind],
                             _type.c_uint]
"""
Determine whether the given cursor kind represents a simple reference.
"""
clang_isExpression: _Callable[[_enum.CXCursorKind],
                              _type.c_uint]
"""
Determine whether the given cursor kind represents an expression.
"""
clang_isStatement: _Callable[[_enum.CXCursorKind],
                             _type.c_uint]
"""
Determine whether the given cursor kind represents a statement.
"""
clang_isAttribute: _Callable[[_enum.CXCursorKind],
                             _type.c_uint]
"""
Determine whether the given cursor kind represents an attribute.
"""
clang_Cursor_hasAttrs: _Callable[[_struct.CXCursor],  # C
                                 _type.c_uint]
"""
Determine whether the given cursor has any attributes.
"""
clang_isInvalid: _Callable[[_enum.CXCursorKind],
                           _type.c_uint]
"""
Determine whether the given cursor kind represents an invalid cursor.
"""
clang_isTranslationUnit: _Callable[[_enum.CXCursorKind],
                                   _type.c_uint]
"""
Determine whether the given cursor kind represents a translation unit.
"""
clang_isPreprocessing: _Callable[[_enum.CXCursorKind],
                                 _type.c_uint]
"""
* Determine whether the given cursor represents a preprocessing element, such as
a preprocessor directive or macro instantiation.
"""
clang_isUnexposed: _Callable[[_enum.CXCursorKind],
                             _type.c_uint]
"""
* Determine whether the given cursor represents a currently unexposed piece of
the AST (e.g., CXCursor_UnexposedStmt).
"""
clang_getCursorLinkage: _Callable[[_struct.CXCursor],  # cursor
                                  _enum.CXLinkageKind]
"""
Determine the linkage of the entity referred to by a given cursor.
"""
clang_getCursorVisibility: _Callable[[_struct.CXCursor],  # cursor
                                     _enum.CXVisibilityKind]
"""
Describe the visibility of the entity referred to by a cursor.
"""
clang_getCursorAvailability: _Callable[[_struct.CXCursor],  # cursor
                                       _enum.CXAvailabilityKind]
"""
Determine the availability of the entity that this cursor refers to, taking the
current target platform into account.
"""
clang_getCursorPlatformAvailability: _Callable[[_struct.CXCursor,  # cursor
                                                _Pointer[_type.c_int],  # always_deprecated
                                                _Pointer[_struct.CXString],  # deprecated_message
                                                _Pointer[_type.c_int],  # always_unavailable
                                                _Pointer[_struct.CXString],  # unavailable_message
                                                _Pointer[_struct.CXPlatformAvailability],  # availability
                                                _type.c_int],  # availability_size
                                               _type.c_int]
"""
Determine the availability of the entity that this cursor refers to on any
platforms for which availability information is known.
"""
clang_disposeCXPlatformAvailability: _Callable[[_Pointer[_struct.CXPlatformAvailability]],  # availability
                                               _type.c_void]
"""
Free the memory associated with a CXPlatformAvailability structure.
"""
clang_getCursorLanguage: _Callable[[_struct.CXCursor],  # cursor
                                   _enum.CXLanguageKind]
"""
Determine the "language" of the entity referred to by a given cursor.
"""
clang_getCursorTLSKind: _Callable[[_struct.CXCursor],  # cursor
                                  _enum.CXTLSKind]
"""
Determine the "thread-local storage (TLS) kind" of the declaration referred to
by a cursor.
"""
clang_Cursor_getTranslationUnit: _Callable[[_struct.CXCursor],
                                           _type.CXTranslationUnit]
"""
Returns the translation unit that a cursor originated from.
"""
clang_createCXCursorSet: _Callable[[],
                                   _type.CXCursorSet]
"""
Creates an empty CXCursorSet.
"""
clang_disposeCXCursorSet: _Callable[[_type.CXCursorSet],  # cset
                                    _type.c_void]
"""
Disposes a CXCursorSet and releases its associated memory.
"""
clang_CXCursorSet_contains: _Callable[[_type.CXCursorSet,  # cset
                                       _struct.CXCursor],  # cursor
                                      _type.c_uint]
"""
Queries a CXCursorSet to see if it contains a specific CXCursor.
"""
clang_CXCursorSet_insert: _Callable[[_type.CXCursorSet,  # cset
                                     _struct.CXCursor],  # cursor
                                    _type.c_uint]
"""
Inserts a CXCursor into a CXCursorSet.
"""
clang_getCursorSemanticParent: _Callable[[_struct.CXCursor],  # cursor
                                         _struct.CXCursor]
"""
Determine the semantic parent of the given cursor.
"""
clang_getCursorLexicalParent: _Callable[[_struct.CXCursor],  # cursor
                                        _struct.CXCursor]
"""
Determine the lexical parent of the given cursor.
"""
clang_getOverriddenCursors: _Callable[[_struct.CXCursor,  # cursor
                                       _Pointer[_Pointer[_struct.CXCursor]],  # overridden
                                       _Pointer[_type.c_uint]],  # num_overridden
                                      _type.c_void]
"""
Determine the set of methods that are overridden by the given method.
"""
clang_disposeOverriddenCursors: _Callable[[_Pointer[_struct.CXCursor]],  # overridden
                                          _type.c_void]
"""
Free the set of overridden cursors returned by clang_getOverriddenCursors().
"""
clang_getIncludedFile: _Callable[[_struct.CXCursor],  # cursor
                                 _type.CXFile]
"""
Retrieve the file that is included by the given inclusion directive cursor.
"""
clang_getCursor: _Callable[[_type.CXTranslationUnit,
                            _struct.CXSourceLocation],
                           _struct.CXCursor]
"""
Map a source location to the cursor that describes the entity at that location
in the source code.
"""
clang_getCursorLocation: _Callable[[_struct.CXCursor],
                                   _struct.CXSourceLocation]
"""
Retrieve the physical location of the source constructor referenced by the given
cursor.
"""
clang_getCursorExtent: _Callable[[_struct.CXCursor],
                                 _struct.CXSourceRange]
"""
Retrieve the physical extent of the source construct referenced by the given
cursor.
"""
clang_getCursorType: _Callable[[_struct.CXCursor],  # C
                               _struct.CXType]
"""
Retrieve the type of a CXCursor (if any).
"""
clang_getTypeSpelling: _Callable[[_struct.CXType],  # CT
                                 _struct.CXString]
"""
Pretty-print the underlying type using the rules of the language of the
translation unit from which it came.
"""
clang_getTypedefDeclUnderlyingType: _Callable[[_struct.CXCursor],  # C
                                              _struct.CXType]
"""
Retrieve the underlying type of a typedef declaration.
"""
clang_getEnumDeclIntegerType: _Callable[[_struct.CXCursor],  # C
                                        _struct.CXType]
"""
Retrieve the integer type of an enum declaration.
"""
clang_getEnumConstantDeclValue: _Callable[[_struct.CXCursor],  # C
                                          _type.c_longlong]
"""
Retrieve the integer value of an enum constant declaration as a signed long
long.
"""
clang_getEnumConstantDeclUnsignedValue: _Callable[[_struct.CXCursor],  # C
                                                  _type.c_ulonglong]
"""
Retrieve the integer value of an enum constant declaration as an unsigned long
long.
"""
clang_getFieldDeclBitWidth: _Callable[[_struct.CXCursor],  # C
                                      _type.c_int]
"""
Retrieve the bit width of a bit field declaration as an integer.
"""
clang_Cursor_getNumArguments: _Callable[[_struct.CXCursor],  # C
                                        _type.c_int]
"""
Retrieve the number of non-variadic arguments associated with a given cursor.
"""
clang_Cursor_getArgument: _Callable[[_struct.CXCursor,  # C
                                     _type.c_uint],  # i
                                    _struct.CXCursor]
"""
Retrieve the argument cursor of a function or method.
"""
clang_Cursor_getNumTemplateArguments: _Callable[[_struct.CXCursor],  # C
                                                _type.c_int]
"""
Returns the number of template args of a function decl representing a template
specialization.
"""
clang_Cursor_getTemplateArgumentKind: _Callable[[_struct.CXCursor,  # C
                                                 _type.c_uint],  # I
                                                _enum.CXTemplateArgumentKind]
"""
Retrieve the kind of the I'th template argument of the CXCursor C.
"""
clang_Cursor_getTemplateArgumentType: _Callable[[_struct.CXCursor,  # C
                                                 _type.c_uint],  # I
                                                _struct.CXType]
"""
Retrieve a CXType representing the type of a TemplateArgument of a function decl
representing a template specialization.
"""
clang_Cursor_getTemplateArgumentValue: _Callable[[_struct.CXCursor,  # C
                                                  _type.c_uint],  # I
                                                 _type.c_longlong]
"""
Retrieve the value of an Integral TemplateArgument (of a function decl
representing a template specialization) as a signed long long.
"""
clang_Cursor_getTemplateArgumentUnsignedValue: _Callable[[_struct.CXCursor,  # C
                                                          _type.c_uint],  # I
                                                         _type.c_ulonglong]
"""
Retrieve the value of an Integral TemplateArgument (of a function decl
representing a template specialization) as an unsigned long long.
"""
clang_equalTypes: _Callable[[_struct.CXType,  # A
                             _struct.CXType],  # B
                            _type.c_uint]
"""
Determine whether two CXTypes represent the same type.
"""
clang_getCanonicalType: _Callable[[_struct.CXType],  # T
                                  _struct.CXType]
"""
Return the canonical type for a CXType.
"""
clang_isConstQualifiedType: _Callable[[_struct.CXType],  # T
                                      _type.c_uint]
"""
Determine whether a CXType has the "const" qualifier set, without looking
through typedefs that may have added "const" at a different level.
"""
clang_Cursor_isMacroFunctionLike: _Callable[[_struct.CXCursor],  # C
                                            _type.c_uint]
"""
Determine whether a CXCursor that is a macro, is function like.
"""
clang_Cursor_isMacroBuiltin: _Callable[[_struct.CXCursor],  # C
                                       _type.c_uint]
"""
Determine whether a CXCursor that is a macro, is a builtin one.
"""
clang_Cursor_isFunctionInlined: _Callable[[_struct.CXCursor],  # C
                                          _type.c_uint]
"""
Determine whether a CXCursor that is a function declaration, is an inline
declaration.
"""
clang_isVolatileQualifiedType: _Callable[[_struct.CXType],  # T
                                         _type.c_uint]
"""
Determine whether a CXType has the "volatile" qualifier set, without looking
through typedefs that may have added "volatile" at a different level.
"""
clang_isRestrictQualifiedType: _Callable[[_struct.CXType],  # T
                                         _type.c_uint]
"""
Determine whether a CXType has the "restrict" qualifier set, without looking
through typedefs that may have added "restrict" at a different level.
"""
clang_getAddressSpace: _Callable[[_struct.CXType],  # T
                                 _type.c_uint]
"""
Returns the address space of the given type.
"""
clang_getTypedefName: _Callable[[_struct.CXType],  # CT
                                _struct.CXString]
"""
Returns the typedef name of the given type.
"""
clang_getPointeeType: _Callable[[_struct.CXType],  # T
                                _struct.CXType]
"""
For pointer types, returns the type of the pointee.
"""
clang_getTypeDeclaration: _Callable[[_struct.CXType],  # T
                                    _struct.CXCursor]
"""
Return the cursor for the declaration of the given type.
"""
clang_getDeclObjCTypeEncoding: _Callable[[_struct.CXCursor],  # C
                                         _struct.CXString]
"""
Returns the Objective-C type encoding for the specified declaration.
"""
clang_Type_getObjCEncoding: _Callable[[_struct.CXType],  # type
                                      _struct.CXString]
"""
Returns the Objective-C type encoding for the specified CXType.
"""
clang_getTypeKindSpelling: _Callable[[_enum.CXTypeKind],  # K
                                     _struct.CXString]
"""
Retrieve the spelling of a given CXTypeKind.
"""
clang_getFunctionTypeCallingConv: _Callable[[_struct.CXType],  # T
                                            _enum.CXCallingConv]
"""
Retrieve the calling convention associated with a function type.
"""
clang_getResultType: _Callable[[_struct.CXType],  # T
                               _struct.CXType]
"""
Retrieve the return type associated with a function type.
"""
clang_getExceptionSpecificationType: _Callable[[_struct.CXType],  # T
                                               _type.c_int]
"""
Retrieve the exception specification type associated with a function type. This
is a value of type CXCursor_ExceptionSpecificationKind.
"""
clang_getNumArgTypes: _Callable[[_struct.CXType],  # T
                                _type.c_int]
"""
Retrieve the number of non-variadic parameters associated with a function type.
"""
clang_getArgType: _Callable[[_struct.CXType,  # T
                             _type.c_uint],  # i
                            _struct.CXType]
"""
Retrieve the type of a parameter of a function type.
"""
clang_Type_getObjCObjectBaseType: _Callable[[_struct.CXType],  # T
                                            _struct.CXType]
"""
Retrieves the base type of the ObjCObjectType.
"""
clang_Type_getNumObjCProtocolRefs: _Callable[[_struct.CXType],  # T
                                             _type.c_uint]
"""
Retrieve the number of protocol references associated with an ObjC object/id.
"""
clang_Type_getObjCProtocolDecl: _Callable[[_struct.CXType,  # T
                                           _type.c_uint],  # i
                                          _struct.CXCursor]
"""
Retrieve the decl for a protocol reference for an ObjC object/id.
"""
clang_Type_getNumObjCTypeArgs: _Callable[[_struct.CXType],  # T
                                         _type.c_uint]
"""
Retrieve the number of type arguments associated with an ObjC object.
"""
clang_Type_getObjCTypeArg: _Callable[[_struct.CXType,  # T
                                      _type.c_uint],  # i
                                     _struct.CXType]
"""
Retrieve a type argument associated with an ObjC object.
"""
clang_isFunctionTypeVariadic: _Callable[[_struct.CXType],  # T
                                        _type.c_uint]
"""
Return 1 if the CXType is a variadic function type, and 0 otherwise.
"""
clang_getCursorResultType: _Callable[[_struct.CXCursor],  # C
                                     _struct.CXType]
"""
Retrieve the return type associated with a given cursor.
"""
clang_getCursorExceptionSpecificationType: _Callable[[_struct.CXCursor],  # C
                                                     _type.c_int]
"""
Retrieve the exception specification type associated with a given cursor. This
is a value of type CXCursor_ExceptionSpecificationKind.
"""
clang_isPODType: _Callable[[_struct.CXType],  # T
                           _type.c_uint]
"""
Return 1 if the CXType is a POD (plain old data) type, and 0 otherwise.
"""
clang_getElementType: _Callable[[_struct.CXType],  # T
                                _struct.CXType]
"""
Return the element type of an array, complex, or vector type.
"""
clang_getNumElements: _Callable[[_struct.CXType],  # T
                                _type.c_longlong]
"""
Return the number of elements of an array or vector type.
"""
clang_getArrayElementType: _Callable[[_struct.CXType],  # T
                                     _struct.CXType]
"""
Return the element type of an array type.
"""
clang_getArraySize: _Callable[[_struct.CXType],  # T
                              _type.c_longlong]
"""
Return the array size of a constant array.
"""
clang_Type_getNamedType: _Callable[[_struct.CXType],  # T
                                   _struct.CXType]
"""
Retrieve the type named by the qualified-id.
"""
clang_Type_isTransparentTagTypedef: _Callable[[_struct.CXType],  # T
                                              _type.c_uint]
"""
Determine if a typedef is 'transparent' tag.
"""
clang_Type_getNullability: _Callable[[_struct.CXType],  # T
                                     _enum.CXTypeNullabilityKind]
"""
Retrieve the nullability kind of a pointer type.
"""
clang_Type_getAlignOf: _Callable[[_struct.CXType],  # T
                                 _type.c_longlong]
"""
Return the alignment of a type in bytes as per C++[expr.alignof] standard.
"""
clang_Type_getClassType: _Callable[[_struct.CXType],  # T
                                   _struct.CXType]
"""
Return the class type of an member pointer type.
"""
clang_Type_getSizeOf: _Callable[[_struct.CXType],  # T
                                _type.c_longlong]
"""
Return the size of a type in bytes as per C++[expr.sizeof] standard.
"""
clang_Type_getOffsetOf: _Callable[[_struct.CXType,  # T
                                   _type.c_char_p],  # S
                                  _type.c_longlong]
"""
Return the offset of a field named S in a record of type T in bits as it would
be returned by __offsetof__ as per C++11[18.2p4]
"""
clang_Type_getModifiedType: _Callable[[_struct.CXType],  # T
                                      _struct.CXType]
"""
Return the type that was modified by this attributed type.
"""
clang_Type_getValueType: _Callable[[_struct.CXType],  # CT
                                   _struct.CXType]
"""
Gets the type contained by this atomic type.
"""
clang_Cursor_getOffsetOfField: _Callable[[_struct.CXCursor],  # C
                                         _type.c_longlong]
"""
Return the offset of the field represented by the Cursor.
"""
clang_Cursor_isAnonymous: _Callable[[_struct.CXCursor],  # C
                                    _type.c_uint]
"""
Determine whether the given cursor represents an anonymous tag or namespace
"""
clang_Cursor_isAnonymousRecordDecl: _Callable[[_struct.CXCursor],  # C
                                              _type.c_uint]
"""
Determine whether the given cursor represents an anonymous record declaration.
"""
clang_Cursor_isInlineNamespace: _Callable[[_struct.CXCursor],  # C
                                          _type.c_uint]
"""
Determine whether the given cursor represents an inline namespace declaration.
"""
clang_Type_getNumTemplateArguments: _Callable[[_struct.CXType],  # T
                                              _type.c_int]
"""
Returns the number of template arguments for given template specialization, or
-1 if type T is not a template specialization.
"""
clang_Type_getTemplateArgumentAsType: _Callable[[_struct.CXType,  # T
                                                 _type.c_uint],  # i
                                                _struct.CXType]
"""
Returns the type template argument of a template class specialization at given
index.
"""
clang_Type_getCXXRefQualifier: _Callable[[_struct.CXType],  # T
                                         _enum.CXRefQualifierKind]
"""
Retrieve the ref-qualifier kind of a function or method.
"""
clang_Cursor_isBitField: _Callable[[_struct.CXCursor],  # C
                                   _type.c_uint]
"""
Returns non-zero if the cursor specifies a Record member that is a bitfield.
"""
clang_isVirtualBase: _Callable[[_struct.CXCursor],
                               _type.c_uint]
"""
Returns 1 if the base class specified by the cursor with kind
CX_CXXBaseSpecifier is virtual.
"""
clang_getCXXAccessSpecifier: _Callable[[_struct.CXCursor],
                                       _enum.CX_CXXAccessSpecifier]
"""
Returns the access control level for the referenced object.
"""
clang_Cursor_getStorageClass: _Callable[[_struct.CXCursor],
                                        _enum.CX_StorageClass]
"""
Returns the storage class for a function or variable declaration.
"""
clang_getNumOverloadedDecls: _Callable[[_struct.CXCursor],  # cursor
                                       _type.c_uint]
"""
Determine the number of overloaded declarations referenced by a
CXCursor_OverloadedDeclRef cursor.
"""
clang_getOverloadedDecl: _Callable[[_struct.CXCursor,  # cursor
                                    _type.c_uint],  # index
                                   _struct.CXCursor]
"""
Retrieve a cursor for one of the overloaded declarations referenced by a
CXCursor_OverloadedDeclRef cursor.
"""
clang_getIBOutletCollectionType: _Callable[[_struct.CXCursor],
                                           _struct.CXType]
"""
For cursors representing an iboutletcollection attribute, this function returns
the collection element type.
"""
clang_visitChildren: _Callable[[_struct.CXCursor,  # parent
                                _type.CXCursorVisitor,  # visitor
                                _type.CXClientData],  # client_data
                               _type.c_uint]
"""
Visit the children of a particular cursor.
"""
clang_getCursorUSR: _Callable[[_struct.CXCursor],
                              _struct.CXString]
"""
Retrieve a Unified Symbol Resolution (USR) for the entity referenced by the
given cursor.
"""
clang_constructUSR_ObjCClass: _Callable[[_type.c_char_p],  # class_name
                                        _struct.CXString]
"""
Construct a USR for a specified Objective-C class.
"""
clang_constructUSR_ObjCCategory: _Callable[[_type.c_char_p,  # class_name
                                            _type.c_char_p],  # category_name
                                           _struct.CXString]
"""
Construct a USR for a specified Objective-C category.
"""
clang_constructUSR_ObjCProtocol: _Callable[[_type.c_char_p],  # protocol_name
                                           _struct.CXString]
"""
Construct a USR for a specified Objective-C protocol.
"""
clang_constructUSR_ObjCIvar: _Callable[[_type.c_char_p,  # name
                                        _struct.CXString],  # classUSR
                                       _struct.CXString]
"""
Construct a USR for a specified Objective-C instance variable and the USR for
its containing class.
"""
clang_constructUSR_ObjCMethod: _Callable[[_type.c_char_p,  # name
                                          _type.c_uint,  # isInstanceMethod
                                          _struct.CXString],  # classUSR
                                         _struct.CXString]
"""
Construct a USR for a specified Objective-C method and the USR for its
containing class.
"""
clang_constructUSR_ObjCProperty: _Callable[[_type.c_char_p,  # property
                                            _struct.CXString],  # classUSR
                                           _struct.CXString]
"""
Construct a USR for a specified Objective-C property and the USR for its
containing class.
"""
clang_getCursorSpelling: _Callable[[_struct.CXCursor],
                                   _struct.CXString]
"""
Retrieve a name for the entity referenced by this cursor.
"""
clang_Cursor_getSpellingNameRange: _Callable[[_struct.CXCursor,
                                              _type.c_uint,  # pieceIndex
                                              _type.c_uint],  # options
                                             _struct.CXSourceRange]
"""
Retrieve a range for a piece that forms the cursors spelling name. Most of the
times there is only one range for the complete spelling but for Objective-C
methods and Objective-C message expressions, there are multiple pieces for each
selector identifier.
"""
clang_PrintingPolicy_getProperty: _Callable[[_type.CXPrintingPolicy,  # Policy
                                             _enum.CXPrintingPolicyProperty],  # Property
                                            _type.c_uint]
"""
Get a property value for the given printing policy.
"""
clang_PrintingPolicy_setProperty: _Callable[[_type.CXPrintingPolicy,  # Policy
                                             _enum.CXPrintingPolicyProperty,  # Property
                                             _type.c_uint],  # Value
                                            _type.c_void]
"""
Set a property value for the given printing policy.
"""
clang_getCursorPrintingPolicy: _Callable[[_struct.CXCursor],
                                         _type.CXPrintingPolicy]
"""
Retrieve the default policy for the cursor.
"""
clang_PrintingPolicy_dispose: _Callable[[_type.CXPrintingPolicy],  # Policy
                                        _type.c_void]
"""
Release a printing policy.
"""
clang_getCursorPrettyPrinted: _Callable[[_struct.CXCursor,  # Cursor
                                         _type.CXPrintingPolicy],  # Policy
                                        _struct.CXString]
"""
Pretty print declarations.
"""
clang_getCursorDisplayName: _Callable[[_struct.CXCursor],
                                      _struct.CXString]
"""
Retrieve the display name for the entity referenced by this cursor.
"""
clang_getCursorReferenced: _Callable[[_struct.CXCursor],
                                     _struct.CXCursor]
"""
For a cursor that is a reference, retrieve a cursor representing the entity that
it references.
"""
clang_getCursorDefinition: _Callable[[_struct.CXCursor],
                                     _struct.CXCursor]
"""
For a cursor that is either a reference to or a declaration of some entity,
retrieve a cursor that describes the definition of that entity.
"""
clang_isCursorDefinition: _Callable[[_struct.CXCursor],
                                    _type.c_uint]
"""
Determine whether the declaration pointed to by this cursor is also a definition
of that entity.
"""
clang_getCanonicalCursor: _Callable[[_struct.CXCursor],
                                    _struct.CXCursor]
"""
Retrieve the canonical cursor corresponding to the given cursor.
"""
clang_Cursor_getObjCSelectorIndex: _Callable[[_struct.CXCursor],
                                             _type.c_int]
"""
If the cursor points to a selector identifier in an Objective-C method or
message expression, this returns the selector index.
"""
clang_Cursor_isDynamicCall: _Callable[[_struct.CXCursor],  # C
                                      _type.c_int]
"""
Given a cursor pointing to a C++ method call or an Objective-C message, returns
non-zero if the method/message is "dynamic", meaning:
"""
clang_Cursor_getReceiverType: _Callable[[_struct.CXCursor],  # C
                                        _struct.CXType]
"""
Given a cursor pointing to an Objective-C message or property reference, or C++
method call, returns the CXType of the receiver.
"""
clang_Cursor_getObjCPropertyAttributes: _Callable[[_struct.CXCursor,  # C
                                                   _type.c_uint],  # reserved
                                                  _type.c_uint]
"""
Given a cursor that represents a property declaration, return the associated
property attributes. The bits are formed from CXObjCPropertyAttrKind.
"""
clang_Cursor_getObjCPropertyGetterName: _Callable[[_struct.CXCursor],  # C
                                                  _struct.CXString]
"""
Given a cursor that represents a property declaration, return the name of the
method that implements the getter.
"""
clang_Cursor_getObjCPropertySetterName: _Callable[[_struct.CXCursor],  # C
                                                  _struct.CXString]
"""
Given a cursor that represents a property declaration, return the name of the
method that implements the setter, if any.
"""
clang_Cursor_getObjCDeclQualifiers: _Callable[[_struct.CXCursor],  # C
                                              _type.c_uint]
"""
Given a cursor that represents an Objective-C method or parameter declaration,
return the associated Objective-C qualifiers for the return type or the
parameter respectively. The bits are formed from CXObjCDeclQualifierKind.
"""
clang_Cursor_isObjCOptional: _Callable[[_struct.CXCursor],  # C
                                       _type.c_uint]
"""
Given a cursor that represents an Objective-C method or property declaration,
return non-zero if the declaration was affected by "@optional". Returns zero if
the cursor is not such a declaration or it is "@required".
"""
clang_Cursor_isVariadic: _Callable[[_struct.CXCursor],  # C
                                   _type.c_uint]
"""
Returns non-zero if the given cursor is a variadic function or method.
"""
clang_Cursor_isExternalSymbol: _Callable[[_struct.CXCursor,  # C
                                          _Pointer[_struct.CXString],  # language
                                          _Pointer[_struct.CXString],  # definedIn
                                          _Pointer[_type.c_uint]],  # isGenerated
                                         _type.c_uint]
"""
Returns non-zero if the given cursor points to a symbol marked with
external_source_symbol attribute.
"""
clang_Cursor_getCommentRange: _Callable[[_struct.CXCursor],  # C
                                        _struct.CXSourceRange]
"""
Given a cursor that represents a declaration, return the associated comment's
source range. The range may include multiple consecutive comments with
whitespace in between.
"""
clang_Cursor_getRawCommentText: _Callable[[_struct.CXCursor],  # C
                                          _struct.CXString]
"""
Given a cursor that represents a declaration, return the associated comment
text, including comment markers.
"""
clang_Cursor_getBriefCommentText: _Callable[[_struct.CXCursor],  # C
                                            _struct.CXString]
"""
Given a cursor that represents a documentable entity (e.g., declaration), return
the associated first paragraph.
"""
clang_Cursor_getMangling: _Callable[[_struct.CXCursor],
                                    _struct.CXString]
"""
Retrieve the CXString representing the mangled name of the cursor.
"""
clang_Cursor_getCXXManglings: _Callable[[_struct.CXCursor],
                                        _Pointer[_struct.CXStringSet]]
"""
Retrieve the CXStrings representing the mangled symbols of the C++ constructor
or destructor at the cursor.
"""
clang_Cursor_getObjCManglings: _Callable[[_struct.CXCursor],
                                         _Pointer[_struct.CXStringSet]]
"""
Retrieve the CXStrings representing the mangled symbols of the ObjC class
interface or implementation at the cursor.
"""
clang_Cursor_getModule: _Callable[[_struct.CXCursor],  # C
                                  _type.CXModule]
"""
Given a CXCursor_ModuleImportDecl cursor, return the associated module.
"""
clang_getModuleForFile: _Callable[[_type.CXTranslationUnit,
                                   _type.CXFile],
                                  _type.CXModule]
"""
Given a CXFile header file, return the module that contains it, if one exists.
"""
clang_Module_getASTFile: _Callable[[_type.CXModule],  # Module
                                   _type.CXFile]
"""
Returns the module file where the provided module object came from.
"""
clang_Module_getParent: _Callable[[_type.CXModule],  # Module
                                  _type.CXModule]
"""
Returns the parent of a sub-module or NULL if the given module is top-level,
e.g. for 'std.vector' it will return the 'std' module.
"""
clang_Module_getName: _Callable[[_type.CXModule],  # Module
                                _struct.CXString]
"""
Returns the name of the module, e.g. for the 'std.vector' sub-module it will
return "vector".
"""
clang_Module_getFullName: _Callable[[_type.CXModule],  # Module
                                    _struct.CXString]
"""
Returns the full name of the module, e.g. "std.vector".
"""
clang_Module_isSystem: _Callable[[_type.CXModule],  # Module
                                 _type.c_int]
"""
Returns non-zero if the module is a system one.
"""
clang_Module_getNumTopLevelHeaders: _Callable[[_type.CXTranslationUnit,
                                               _type.CXModule],  # Module
                                              _type.c_uint]
"""
Returns the number of top level headers associated with this module.
"""
clang_Module_getTopLevelHeader: _Callable[[_type.CXTranslationUnit,
                                           _type.CXModule,  # Module
                                           _type.c_uint],  # Index
                                          _type.CXFile]
"""
Returns the specified top level header associated with the module.
"""
clang_CXXConstructor_isConvertingConstructor: _Callable[[_struct.CXCursor],  # C
                                                        _type.c_uint]
"""
Determine if a C++ constructor is a converting constructor.
"""
clang_CXXConstructor_isCopyConstructor: _Callable[[_struct.CXCursor],  # C
                                                  _type.c_uint]
"""
Determine if a C++ constructor is a copy constructor.
"""
clang_CXXConstructor_isDefaultConstructor: _Callable[[_struct.CXCursor],  # C
                                                     _type.c_uint]
"""
Determine if a C++ constructor is the default constructor.
"""
clang_CXXConstructor_isMoveConstructor: _Callable[[_struct.CXCursor],  # C
                                                  _type.c_uint]
"""
Determine if a C++ constructor is a move constructor.
"""
clang_CXXField_isMutable: _Callable[[_struct.CXCursor],  # C
                                    _type.c_uint]
"""
Determine if a C++ field is declared 'mutable'.
"""
clang_CXXMethod_isDefaulted: _Callable[[_struct.CXCursor],  # C
                                       _type.c_uint]
"""
Determine if a C++ method is declared '= default'.
"""
clang_CXXMethod_isPureVirtual: _Callable[[_struct.CXCursor],  # C
                                         _type.c_uint]
"""
Determine if a C++ member function or member function template is pure virtual.
"""
clang_CXXMethod_isStatic: _Callable[[_struct.CXCursor],  # C
                                    _type.c_uint]
"""
Determine if a C++ member function or member function template is declared
'static'.
"""
clang_CXXMethod_isVirtual: _Callable[[_struct.CXCursor],  # C
                                     _type.c_uint]
"""
Determine if a C++ member function or member function template is explicitly
declared 'virtual' or if it overrides a virtual method from one of the base
classes.
"""
clang_CXXRecord_isAbstract: _Callable[[_struct.CXCursor],  # C
                                      _type.c_uint]
"""
Determine if a C++ record is abstract, i.e. whether a class or struct has a pure
virtual member function.
"""
clang_EnumDecl_isScoped: _Callable[[_struct.CXCursor],  # C
                                   _type.c_uint]
"""
Determine if an enum declaration refers to a scoped enum.
"""
clang_CXXMethod_isConst: _Callable[[_struct.CXCursor],  # C
                                   _type.c_uint]
"""
Determine if a C++ member function or member function template is declared
'const'.
"""
clang_getTemplateCursorKind: _Callable[[_struct.CXCursor],  # C
                                       _enum.CXCursorKind]
"""
Given a cursor that represents a template, determine the cursor kind of the
specializations would be generated by instantiating the template.
"""
clang_getSpecializedCursorTemplate: _Callable[[_struct.CXCursor],  # C
                                              _struct.CXCursor]
"""
Given a cursor that may represent a specialization or instantiation of a
template, retrieve the cursor that represents the template that it specializes
or from which it was instantiated.
"""
clang_getCursorReferenceNameRange: _Callable[[_struct.CXCursor,  # C
                                              _type.c_uint,  # NameFlags
                                              _type.c_uint],  # PieceIndex
                                             _struct.CXSourceRange]
"""
Given a cursor that references something else, return the source range covering
that reference.
"""
clang_getToken: _Callable[[_type.CXTranslationUnit,  # TU
                           _struct.CXSourceLocation],  # Location
                          _Pointer[_struct.CXToken]]
"""
Get the raw lexical token starting with the given location.
"""
clang_getTokenKind: _Callable[[_struct.CXToken],
                              _enum.CXTokenKind]
"""
Determine the kind of the given token.
"""
clang_getTokenSpelling: _Callable[[_type.CXTranslationUnit,
                                   _struct.CXToken],
                                  _struct.CXString]
"""
Determine the spelling of the given token.
"""
clang_getTokenLocation: _Callable[[_type.CXTranslationUnit,
                                   _struct.CXToken],
                                  _struct.CXSourceLocation]
"""
Retrieve the source location of the given token.
"""
clang_getTokenExtent: _Callable[[_type.CXTranslationUnit,
                                 _struct.CXToken],
                                _struct.CXSourceRange]
"""
Retrieve a source range that covers the given token.
"""
clang_tokenize: _Callable[[_type.CXTranslationUnit,  # TU
                           _struct.CXSourceRange,  # Range
                           _Pointer[_Pointer[_struct.CXToken]],  # Tokens
                           _Pointer[_type.c_uint]],  # NumTokens
                          _type.c_void]
"""
Tokenize the source code described by the given range into raw lexical tokens.
"""
clang_annotateTokens: _Callable[[_type.CXTranslationUnit,  # TU
                                 _Pointer[_struct.CXToken],  # Tokens
                                 _type.c_uint,  # NumTokens
                                 _Pointer[_struct.CXCursor]],  # Cursors
                                _type.c_void]
"""
Annotate the given set of tokens by providing cursors for each token that can be
mapped to a specific entity within the abstract syntax tree.
"""
clang_disposeTokens: _Callable[[_type.CXTranslationUnit,  # TU
                                _Pointer[_struct.CXToken],  # Tokens
                                _type.c_uint],  # NumTokens
                               _type.c_void]
"""
Free the given set of tokens.
"""
clang_getCursorKindSpelling: _Callable[[_enum.CXCursorKind],  # Kind
                                       _struct.CXString]
"""
for debug/testing
"""
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
"""
Determine the kind of a particular chunk within a completion string.
"""
clang_getCompletionChunkText: _Callable[[_type.CXCompletionString,  # completion_string
                                         _type.c_uint],  # chunk_number
                                        _struct.CXString]
"""
Retrieve the text associated with a particular chunk within a completion string.
"""
clang_getCompletionChunkCompletionString: _Callable[[_type.CXCompletionString,  # completion_string
                                                     _type.c_uint],  # chunk_number
                                                    _type.CXCompletionString]
"""
Retrieve the completion string associated with a particular chunk within a
completion string.
"""
clang_getNumCompletionChunks: _Callable[[_type.CXCompletionString],  # completion_string
                                        _type.c_uint]
"""
Retrieve the number of chunks in the given code-completion string.
"""
clang_getCompletionPriority: _Callable[[_type.CXCompletionString],  # completion_string
                                       _type.c_uint]
"""
Determine the priority of this code completion.
"""
clang_getCompletionAvailability: _Callable[[_type.CXCompletionString],  # completion_string
                                           _enum.CXAvailabilityKind]
"""
Determine the availability of the entity that this code-completion string refers
to.
"""
clang_getCompletionNumAnnotations: _Callable[[_type.CXCompletionString],  # completion_string
                                             _type.c_uint]
"""
Retrieve the number of annotations associated with the given completion string.
"""
clang_getCompletionAnnotation: _Callable[[_type.CXCompletionString,  # completion_string
                                          _type.c_uint],  # annotation_number
                                         _struct.CXString]
"""
Retrieve the annotation associated with the given completion string.
"""
clang_getCompletionParent: _Callable[[_type.CXCompletionString,  # completion_string
                                      _Pointer[_enum.CXCursorKind]],  # kind
                                     _struct.CXString]
"""
Retrieve the parent context of the given completion string.
"""
clang_getCompletionBriefComment: _Callable[[_type.CXCompletionString],  # completion_string
                                           _struct.CXString]
"""
Retrieve the brief documentation comment attached to the declaration that
corresponds to the given completion string.
"""
clang_getCursorCompletionString: _Callable[[_struct.CXCursor],  # cursor
                                           _type.CXCompletionString]
"""
Retrieve a completion string for an arbitrary declaration or macro definition
cursor.
"""
clang_getCompletionNumFixIts: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # results
                                         _type.c_uint],  # completion_index
                                        _type.c_uint]
"""
Retrieve the number of fix-its for the given completion index.
"""
clang_getCompletionFixIt: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # results
                                     _type.c_uint,  # completion_index
                                     _type.c_uint,  # fixit_index
                                     _Pointer[_struct.CXSourceRange]],  # replacement_range
                                    _struct.CXString]
"""
Fix-its that *must* be applied before inserting the text for the corresponding
completion.
"""
clang_defaultCodeCompleteOptions: _Callable[[],
                                            _type.c_uint]
"""
Returns a default set of code-completion options that can be passed to
clang_codeCompleteAt().
"""
clang_codeCompleteAt: _Callable[[_type.CXTranslationUnit,  # TU
                                 _type.c_char_p,  # complete_filename
                                 _type.c_uint,  # complete_line
                                 _type.c_uint,  # complete_column
                                 _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                 _type.c_uint,  # num_unsaved_files
                                 _type.c_uint],  # options
                                _Pointer[_struct.CXCodeCompleteResults]]
"""
Perform code completion at a given location in a translation unit.
"""
clang_sortCodeCompletionResults: _Callable[[_Pointer[_struct.CXCompletionResult],  # Results
                                            _type.c_uint],  # NumResults
                                           _type.c_void]
"""
Sort the code-completion results in case-insensitive alphabetical order.
"""
clang_disposeCodeCompleteResults: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                            _type.c_void]
"""
Free the given set of code-completion results.
"""
clang_codeCompleteGetNumDiagnostics: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                               _type.c_uint]
"""
Determine the number of diagnostics produced prior to the location where code
completion was performed.
"""
clang_codeCompleteGetDiagnostic: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # Results
                                            _type.c_uint],  # Index
                                           _type.CXDiagnostic]
"""
Retrieve a diagnostic associated with the given code completion.
"""
clang_codeCompleteGetContexts: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                         _type.c_ulonglong]
"""
Determines what completions are appropriate for the context the given code
completion.
"""
clang_codeCompleteGetContainerKind: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # Results
                                               _Pointer[_type.c_uint]],  # IsIncomplete
                                              _enum.CXCursorKind]
"""
Returns the cursor kind for the container for the current code completion
context. The container is only guaranteed to be set for contexts where a
container exists (i.e. member accesses or Objective-C message sends); if there
is not a container, this function will return CXCursor_InvalidCode.
"""
clang_codeCompleteGetContainerUSR: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                             _struct.CXString]
"""
Returns the USR for the container for the current code completion context. If
there is not a container for the current context, this function will return the
empty string.
"""
clang_codeCompleteGetObjCSelector: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                             _struct.CXString]
"""
Returns the currently-entered selector for an Objective-C message send,
formatted like "initWithFoo:bar:". Only guaranteed to return a non-empty string
for CXCompletionContext_ObjCInstanceMessage and
CXCompletionContext_ObjCClassMessage.
"""
clang_getClangVersion: _Callable[[],
                                 _struct.CXString]
"""
Return a version string, suitable for showing to a user, but not intended to be
parsed (the format is not guaranteed to be stable).
"""
clang_toggleCrashRecovery: _Callable[[_type.c_uint],  # isEnabled
                                     _type.c_void]
"""
Enable/disable crash recovery.
"""
clang_getInclusions: _Callable[[_type.CXTranslationUnit,  # tu
                                _type.CXInclusionVisitor,  # visitor
                                _type.CXClientData],  # client_data
                               _type.c_void]
"""
Visit the set of preprocessor inclusions in a translation unit. The visitor
function is called with the provided data for every included file. This does not
include headers included by the PCH file (unless one is inspecting the
inclusions in the PCH file itself).
"""
clang_Cursor_Evaluate: _Callable[[_struct.CXCursor],  # C
                                 _type.CXEvalResult]
"""
If cursor is a statement declaration tries to evaluate the statement and if its
variable, tries to evaluate its initializer, into its corresponding type. If
it's an expression, tries to evaluate the expression.
"""
clang_EvalResult_getKind: _Callable[[_type.CXEvalResult],  # E
                                    _enum.CXEvalResultKind]
"""
Returns the kind of the evaluated result.
"""
clang_EvalResult_getAsInt: _Callable[[_type.CXEvalResult],  # E
                                     _type.c_int]
"""
Returns the evaluation result as integer if the kind is Int.
"""
clang_EvalResult_getAsLongLong: _Callable[[_type.CXEvalResult],  # E
                                          _type.c_longlong]
"""
Returns the evaluation result as a long long integer if the kind is Int. This
prevents overflows that may happen if the result is returned with
clang_EvalResult_getAsInt.
"""
clang_EvalResult_isUnsignedInt: _Callable[[_type.CXEvalResult],  # E
                                          _type.c_uint]
"""
Returns a non-zero value if the kind is Int and the evaluation result resulted
in an unsigned integer.
"""
clang_EvalResult_getAsUnsigned: _Callable[[_type.CXEvalResult],  # E
                                          _type.c_ulonglong]
"""
Returns the evaluation result as an unsigned integer if the kind is Int and
clang_EvalResult_isUnsignedInt is non-zero.
"""
clang_EvalResult_getAsDouble: _Callable[[_type.CXEvalResult],  # E
                                        _type.c_double]
"""
Returns the evaluation result as double if the kind is double.
"""
clang_EvalResult_getAsStr: _Callable[[_type.CXEvalResult],  # E
                                     _type.c_char_p]
"""
Returns the evaluation result as a constant string if the kind is other than Int
or float. User must not free this pointer, instead call clang_EvalResult_dispose
on the CXEvalResult returned by clang_Cursor_Evaluate.
"""
clang_EvalResult_dispose: _Callable[[_type.CXEvalResult],  # E
                                    _type.c_void]
"""
Disposes the created Eval memory.
"""
clang_getRemappings: _Callable[[_type.c_char_p],  # path
                               _type.CXRemapping]
"""
Retrieve a remapping.
"""
clang_getRemappingsFromFileList: _Callable[[_Pointer[_type.c_char_p],  # filePaths
                                            _type.c_uint],  # numFiles
                                           _type.CXRemapping]
"""
Retrieve a remapping.
"""
clang_remap_getNumFiles: _Callable[[_type.CXRemapping],
                                   _type.c_uint]
"""
Determine the number of remappings.
"""
clang_remap_getFilenames: _Callable[[_type.CXRemapping,
                                     _type.c_uint,  # index
                                     _Pointer[_struct.CXString],  # original
                                     _Pointer[_struct.CXString]],  # transformed
                                    _type.c_void]
"""
Get the original and the associated filename from the remapping.
"""
clang_remap_dispose: _Callable[[_type.CXRemapping],
                               _type.c_void]
"""
Dispose the remapping.
"""
clang_findReferencesInFile: _Callable[[_struct.CXCursor,  # cursor
                                       _type.CXFile,  # file
                                       _struct.CXCursorAndRangeVisitor],  # visitor
                                      _enum.CXResult]
"""
Find references of a declaration in a specific file.
"""
clang_findIncludesInFile: _Callable[[_type.CXTranslationUnit,  # TU
                                     _type.CXFile,  # file
                                     _struct.CXCursorAndRangeVisitor],  # visitor
                                    _enum.CXResult]
"""
Find #import/#include directives in a specific file.
"""
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
"""
For retrieving a custom CXIdxClientContainer attached to a container.
"""
clang_index_setClientContainer: _Callable[[_Pointer[_struct.CXIdxContainerInfo],
                                           _type.CXIdxClientContainer],
                                          _type.c_void]
"""
For setting a custom CXIdxClientContainer attached to a container.
"""
clang_index_getClientEntity: _Callable[[_Pointer[_struct.CXIdxEntityInfo]],
                                       _type.CXIdxClientEntity]
"""
For retrieving a custom CXIdxClientEntity attached to an entity.
"""
clang_index_setClientEntity: _Callable[[_Pointer[_struct.CXIdxEntityInfo],
                                        _type.CXIdxClientEntity],
                                       _type.c_void]
"""
For setting a custom CXIdxClientEntity attached to an entity.
"""
clang_IndexAction_create: _Callable[[_type.CXIndex],  # CIdx
                                    _type.CXIndexAction]
"""
An indexing action/session, to be applied to one or multiple translation units.
"""
clang_IndexAction_dispose: _Callable[[_type.CXIndexAction],
                                     _type.c_void]
"""
Destroy the given index action.
"""
clang_indexSourceFile: _Callable[[_type.CXIndexAction,
                                  _type.CXClientData,  # client_data
                                  _Pointer[_struct.IndexerCallbacks],  # index_callbacks
                                  _type.c_uint,  # index_callbacks_size
                                  _type.c_uint,  # index_options
                                  _type.c_char_p,  # source_filename
                                  _Pointer[_type.c_char_p],  # command_line_args
                                  _type.c_int,  # num_command_line_args
                                  _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                  _type.c_uint,  # num_unsaved_files
                                  _Pointer[_type.CXTranslationUnit],  # out_TU
                                  _type.c_uint],  # TU_options
                                 _type.c_int]
"""
Index the given source file and the translation unit corresponding to that file
via callbacks implemented through #IndexerCallbacks.
"""
clang_indexSourceFileFullArgv: _Callable[[_type.CXIndexAction,
                                          _type.CXClientData,  # client_data
                                          _Pointer[_struct.IndexerCallbacks],  # index_callbacks
                                          _type.c_uint,  # index_callbacks_size
                                          _type.c_uint,  # index_options
                                          _type.c_char_p,  # source_filename
                                          _Pointer[_type.c_char_p],  # command_line_args
                                          _type.c_int,  # num_command_line_args
                                          _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                          _type.c_uint,  # num_unsaved_files
                                          _Pointer[_type.CXTranslationUnit],  # out_TU
                                          _type.c_uint],  # TU_options
                                         _type.c_int]
"""
Same as clang_indexSourceFile but requires a full command line for
command_line_args including argv[0]. This is useful if the standard library
paths are relative to the binary.
"""
clang_indexTranslationUnit: _Callable[[_type.CXIndexAction,
                                       _type.CXClientData,  # client_data
                                       _Pointer[_struct.IndexerCallbacks],  # index_callbacks
                                       _type.c_uint,  # index_callbacks_size
                                       _type.c_uint,  # index_options
                                       _type.CXTranslationUnit],
                                      _type.c_int]
"""
Index the given translation unit via callbacks implemented through
#IndexerCallbacks.
"""
clang_indexLoc_getFileLocation: _Callable[[_struct.CXIdxLoc,  # loc
                                           _Pointer[_type.CXIdxClientFile],  # indexFile
                                           _Pointer[_type.CXFile],  # file
                                           _Pointer[_type.c_uint],  # line
                                           _Pointer[_type.c_uint],  # column
                                           _Pointer[_type.c_uint]],  # offset
                                          _type.c_void]
"""
Retrieve the CXIdxFile, file, line, column, and offset represented by the given
CXIdxLoc.
"""
clang_indexLoc_getCXSourceLocation: _Callable[[_struct.CXIdxLoc],  # loc
                                              _struct.CXSourceLocation]
"""
Retrieve the CXSourceLocation represented by the given CXIdxLoc.
"""
clang_Type_visitFields: _Callable[[_struct.CXType,  # T
                                   _type.CXFieldVisitor,  # visitor
                                   _type.CXClientData],  # client_data
                                  _type.c_uint]
"""
Visit the fields of a particular type.
"""
# Rewrite
clang_CXRewriter_create: _Callable[[_type.CXTranslationUnit],  # TU
                                   _type.CXRewriter]
"""
Create CXRewriter.
"""
clang_CXRewriter_insertTextBefore: _Callable[[_type.CXRewriter,  # Rew
                                              _struct.CXSourceLocation,  # Loc
                                              _type.c_char_p],  # Insert
                                             _type.c_void]
"""
Insert the specified string at the specified location in the original buffer.
"""
clang_CXRewriter_replaceText: _Callable[[_type.CXRewriter,  # Rew
                                         _struct.CXSourceRange,  # ToBeReplaced
                                         _type.c_char_p],  # Replacement
                                        _type.c_void]
"""
Replace the specified range of characters in the input with the specified
replacement.
"""
clang_CXRewriter_removeText: _Callable[[_type.CXRewriter,  # Rew
                                        _struct.CXSourceRange],  # ToBeRemoved
                                       _type.c_void]
"""
Remove the specified range.
"""
clang_CXRewriter_overwriteChangedFiles: _Callable[[_type.CXRewriter],  # Rew
                                                  _type.c_int]
"""
Save all changed files to disk. Returns 1 if any files were not saved
successfully, returns 0 otherwise.
"""
clang_CXRewriter_writeMainFileToStdOut: _Callable[[_type.CXRewriter],  # Rew
                                                  _type.c_void]
"""
Write out rewritten version of the main file to stdout.
"""
clang_CXRewriter_dispose: _Callable[[_type.CXRewriter],  # Rew
                                    _type.c_void]
"""
Free the given CXRewriter.
"""

_CLib(__name__)

from . import _Enum


# CXCompilationDatabase
# noinspection PyPep8Naming
class CXCompilationDatabase_Error(_Enum):
    """
    Error codes for Compilation Database
    """
    NoError = 0
    """
    No error occurred
    """
    CanNotLoadDatabase = 1
    """
    Database can not be loaded
    """


# CXErrorCode
class CXErrorCode(_Enum):
    """
    Error codes returned by libclang routines.
    """
    Success = 0
    """
    No error.
    """
    Failure = 1
    """
    A generic error code, no further details are available.
    """
    Crashed = 2
    """
    libclang crashed while performing the requested operation.
    """
    InvalidArguments = 3
    """
    The function detected that the arguments violate the function contract.
    """
    ASTReadError = 4
    """
    An AST deserialization error has occurred.
    """


# Documentation
class CXCommentKind(_Enum):
    """
    Describes the type of the comment AST node ( CXComment). A comment node can be
    considered block content (e. g., paragraph), inline content (plain text) or
    neither (the root AST node).
    """
    Null = 0
    """
    Null comment. No AST node is constructed at the requested location because there
    is no text or a syntax error.
    """
    Text = 1
    """
    Plain text. Inline content.
    """
    InlineCommand = 2
    """
    A command with word-like arguments that is considered inline content.
    """
    HTMLStartTag = 3
    """
    HTML start tag with attributes (name-value pairs). Considered inline content.
    """
    HTMLEndTag = 4
    """
    HTML end tag. Considered inline content.
    """
    Paragraph = 5
    """
    A paragraph, contains inline comment. The paragraph itself is block content.
    """
    BlockCommand = 6
    """
    A command that has zero or more word-like arguments (number of word-like
    arguments depends on command name) and a paragraph as an argument. Block command
    is block content.
    """
    ParamCommand = 7
    """
    A param or arg command that describes the function parameter (name, passing
    direction, description).
    """
    TParamCommand = 8
    """
    A param command that describes a template parameter (name and description).
    """
    VerbatimBlockCommand = 9
    """
    A verbatim block command (e. g., preformatted code). Verbatim block has an
    opening and a closing command and contains multiple lines of text (
    VerbatimBlockLine child nodes).
    """
    VerbatimBlockLine = 10
    """
    A line of text that is contained within a VerbatimBlockCommand node.
    """
    VerbatimLine = 11
    """
    A verbatim line command. Verbatim line has an opening command, a single line of
    text (up to the newline after the opening command) and has no closing command.
    """
    FullComment = 12
    """
    A full comment attached to a declaration, contains block content.
    """


class CXCommentInlineCommandRenderKind(_Enum):
    """
    The most appropriate rendering mode for an inline command, chosen on command
    semantics in Doxygen.
    """
    Normal = 0
    """
    Command argument should be rendered in a normal font.
    """
    Bold = 1
    """
    Command argument should be rendered in a bold font.
    """
    Monospaced = 2
    """
    Command argument should be rendered in a monospaced font.
    """
    Emphasized = 3
    """
    Command argument should be rendered emphasized (typically italic font).
    """
    Anchor = 4
    """
    Command argument should not be rendered (since it only defines an anchor).
    """


class CXCommentParamPassDirection(_Enum):
    """
    Describes parameter passing direction for param or arg command.
    """
    In = 0
    """
    The parameter is an input parameter.
    """
    Out = 1
    """
    The parameter is an output parameter.
    """
    InOut = 2
    """
    The parameter is an input and output parameter.
    """


# Index
class CXAvailabilityKind(_Enum):
    """
    Describes the availability of a particular entity, which indicates whether the
    use of this entity will result in a warning or error due to it being deprecated
    or unavailable.
    """
    Available = 0
    """
    The entity is available.
    """
    Deprecated = 1
    """
    The entity is available, but has been deprecated (and its use is not
    recommended).
    """
    NotAvailable = 2
    """
    The entity is not available; any use of it will be an error.
    """
    NotAccessible = 3
    """
    The entity is available, but not accessible; any use of it will be an error.
    """


# noinspection PyPep8Naming
class CXCursor_ExceptionSpecificationKind(_Enum):
    """
    Describes the exception specification of a cursor.
    """
    None_ = 0
    """
    The cursor has no exception specification.
    """
    DynamicNone = 1
    """
    The cursor has exception specification throw()
    """
    Dynamic = 2
    """
    The cursor has exception specification throw(T1, T2)
    """
    MSAny = 3
    """
    The cursor has exception specification throw(...).
    """
    BasicNoexcept = 4
    """
    The cursor has exception specification basic noexcept.
    """
    ComputedNoexcept = 5
    """
    The cursor has exception specification computed noexcept.
    """
    Unevaluated = 6
    """
    The exception specification has not yet been evaluated.
    """
    Uninstantiated = 7
    """
    The exception specification has not yet been instantiated.
    """
    Unparsed = 8
    """
    The exception specification has not been parsed yet.
    """
    NoThrow = 9
    """
    The cursor has a __declspec(nothrow) exception specification.
    """


class CXGlobalOptFlags(_Enum):
    """
    Used to indicate that no special CXIndex options are needed.
    """
    None_ = 0
    """
    Used to indicate that no special CXIndex options are needed.
    """
    ThreadBackgroundPriorityForIndexing = 1
    """
    Used to indicate that threads that libclang creates for indexing purposes should
    use background priority.
    """
    ThreadBackgroundPriorityForEditing = 2
    """
    Used to indicate that threads that libclang creates for editing purposes should
    use background priority.
    """
    ThreadBackgroundPriorityForAll = 3
    """
    Used to indicate that all threads that libclang creates should use background
    priority.
    """


class CXDiagnosticSeverity(_Enum):
    """
    Describes the severity of a particular diagnostic.
    """
    Ignored = 0
    """
    A diagnostic that has been suppressed, e.g., by a command-line option.
    """
    Note = 1
    """
    This diagnostic is a note that should be attached to the previous (non-note)
    diagnostic.
    """
    Warning = 2
    """
    This diagnostic indicates suspicious code that may not be wrong.
    """
    Error = 3
    """
    This diagnostic indicates that the code is ill-formed.
    """
    Fatal = 4
    """
    This diagnostic indicates that the code is ill-formed such that future parser
    recovery is unlikely to produce useful results.
    """


# noinspection PyPep8Naming
class CXLoadDiag_Error(_Enum):
    """
    Describes the kind of error that occurred (if any) in a call to
    clang_loadDiagnostics.
    """
    None_ = 0
    """
    Indicates that no error occurred.
    """
    Unknown = 1
    """
    Indicates that an unknown error occurred while attempting to deserialize
    diagnostics.
    """
    CannotLoad = 2
    """
    Indicates that the file containing the serialized diagnostics could not be
    opened.
    """
    InvalidFile = 3
    """
    Indicates that the serialized diagnostics file is invalid or corrupt.
    """


class CXDiagnosticDisplayOptions(_Enum):
    """
    Options to control the display of diagnostics.
    """
    DisplaySourceLocation = 1
    """
    Display the source-location information where the diagnostic was located.
    """
    DisplayColumn = 2
    """
    If displaying the source-location information of the diagnostic, also include
    the column number.
    """
    DisplaySourceRanges = 4
    """
    If displaying the source-location information of the diagnostic, also include
    information about source ranges in a machine-parsable format.
    """
    DisplayOption = 8
    """
    Display the option name associated with this diagnostic, if any.
    """
    DisplayCategoryId = 16
    """
    Display the category number associated with this diagnostic, if any.
    """
    DisplayCategoryName = 32
    """
    Display the category name associated with this diagnostic, if any.
    """


# noinspection PyPep8Naming
class CXTranslationUnit_Flags(_Enum):
    """
    Flags that control the creation of translation units.
    """
    None_ = 0
    """
    Used to indicate that no special translation-unit options are needed.
    """
    DetailedPreprocessingRecord = 1
    """
    Used to indicate that the parser should construct a "detailed" preprocessing
    record, including all macro definitions and instantiations.
    """
    Incomplete = 2
    """
    Used to indicate that the translation unit is incomplete.
    """
    PrecompiledPreamble = 4
    """
    Used to indicate that the translation unit should be built with an implicit
    precompiled header for the preamble.
    """
    CacheCompletionResults = 8
    """
    Used to indicate that the translation unit should cache some code-completion
    results with each reparse of the source file.
    """
    ForSerialization = 16
    """
    Used to indicate that the translation unit will be serialized with
    clang_saveTranslationUnit.
    """
    CXXChainedPCH = 32
    """
    DEPRECATED: Enabled chained precompiled preambles in C++.
    """
    SkipFunctionBodies = 64
    """
    Used to indicate that function/method bodies should be skipped while parsing.
    """
    IncludeBriefCommentsInCodeCompletion = 128
    """
    Used to indicate that brief documentation comments should be included into the
    set of code completions returned from this translation unit.
    """
    CreatePreambleOnFirstParse = 256
    """
    Used to indicate that the precompiled preamble should be created on the first
    parse. Otherwise it will be created on the first reparse. This trades runtime on
    the first parse (serializing the preamble takes time) for reduced runtime on the
    second parse (can now reuse the preamble).
    """
    KeepGoing = 512
    """
    Do not stop processing when fatal errors are encountered.
    """
    SingleFileParse = 1024
    """
    Sets the preprocessor in a mode for parsing a single file only.
    """
    LimitSkipFunctionBodiesToPreamble = 2048
    """
    Used in combination with CXTranslationUnit_SkipFunctionBodies to constrain the
    skipping of function bodies to the preamble.
    """
    IncludeAttributedTypes = 4096
    """
    Used to indicate that attributed types should be included in CXType.
    """
    VisitImplicitAttributes = 8192
    """
    Used to indicate that implicit attributes should be visited.
    """
    IgnoreNonErrorsFromIncludedFiles = 16384
    """
    Used to indicate that non-errors from included files should be ignored.
    """
    RetainExcludedConditionalBlocks = 32768
    """
    Tells the preprocessor not to skip excluded conditional blocks.
    """


# noinspection PyPep8Naming
class CXSaveTranslationUnit_Flags(_Enum):
    """
    Flags that control how translation units are saved.
    """
    None_ = 0
    """
    Used to indicate that no special saving options are needed.
    """


class CXSaveError(_Enum):
    """
    Describes the kind of error that occurred (if any) in a call to
    clang_saveTranslationUnit().
    """
    None_ = 0
    """
    Indicates that no error occurred while saving a translation unit.
    """
    Unknown = 1
    """
    Indicates that an unknown error occurred while attempting to save the file.
    """
    TranslationErrors = 2
    """
    Indicates that errors during translation prevented this attempt to save the
    translation unit.
    """
    InvalidTU = 3
    """
    Indicates that the translation unit to be saved was somehow invalid (e.g.,
    NULL).
    """


# noinspection PyPep8Naming
class CXReparse_Flags(_Enum):
    """
    Flags that control the reparsing of translation units.
    """
    None_ = 0
    """
    Used to indicate that no special reparsing options are needed.
    """


class CXTUResourceUsageKind(_Enum):
    """
    Categorizes how memory is being used by a translation unit.
    """
    AST = 1
    Identifiers = 2
    Selectors = 3
    GlobalCompletionResults = 4
    SourceManagerContentCache = 5
    AST_SideTables = 6
    SourceManager_Membuffer_Malloc = 7
    SourceManager_Membuffer_MMap = 8
    ExternalASTSource_Membuffer_Malloc = 9
    ExternalASTSource_Membuffer_MMap = 10
    Preprocessor = 11
    PreprocessingRecord = 12
    SourceManager_DataStructures = 13
    Preprocessor_HeaderSearch = 14
    MEMORY_IN_BYTES_BEGIN = 1
    MEMORY_IN_BYTES_END = 14
    First = 1
    Last = 14


class CXCursorKind(_Enum):
    """
    Describes the kind of entity that a cursor refers to.
    """
    UnexposedDecl = 1
    """
    Declarations
    """
    StructDecl = 2
    """
    A C or C++ struct.
    """
    UnionDecl = 3
    """
    A C or C++ union.
    """
    ClassDecl = 4
    """
    A C++ class.
    """
    EnumDecl = 5
    """
    An enumeration.
    """
    FieldDecl = 6
    """
    A field (in C) or non-static data member (in C++) in a struct, union, or C++
    class.
    """
    EnumConstantDecl = 7
    """
    An enumerator constant.
    """
    FunctionDecl = 8
    """
    A function.
    """
    VarDecl = 9
    """
    A variable.
    """
    ParmDecl = 10
    """
    A function or method parameter.
    """
    ObjCInterfaceDecl = 11
    """
    An Objective-C @interface.
    """
    ObjCCategoryDecl = 12
    """
    An Objective-C @interface for a category.
    """
    ObjCProtocolDecl = 13
    """
    An Objective-C @protocol declaration.
    """
    ObjCPropertyDecl = 14
    """
    An Objective-C @property declaration.
    """
    ObjCIvarDecl = 15
    """
    An Objective-C instance variable.
    """
    ObjCInstanceMethodDecl = 16
    """
    An Objective-C instance method.
    """
    ObjCClassMethodDecl = 17
    """
    An Objective-C class method.
    """
    ObjCImplementationDecl = 18
    """
    An Objective-C @implementation.
    """
    ObjCCategoryImplDecl = 19
    """
    An Objective-C @implementation for a category.
    """
    TypedefDecl = 20
    """
    A typedef.
    """
    CXXMethod = 21
    """
    A C++ class method.
    """
    Namespace = 22
    """
    A C++ namespace.
    """
    LinkageSpec = 23
    """
    A linkage specification, e.g. 'extern "C"'.
    """
    Constructor = 24
    """
    A C++ constructor.
    """
    Destructor = 25
    """
    A C++ destructor.
    """
    ConversionFunction = 26
    """
    A C++ conversion function.
    """
    TemplateTypeParameter = 27
    """
    A C++ template type parameter.
    """
    NonTypeTemplateParameter = 28
    """
    A C++ non-type template parameter.
    """
    TemplateTemplateParameter = 29
    """
    A C++ template template parameter.
    """
    FunctionTemplate = 30
    """
    A C++ function template.
    """
    ClassTemplate = 31
    """
    A C++ class template.
    """
    ClassTemplatePartialSpecialization = 32
    """
    A C++ class template partial specialization.
    """
    NamespaceAlias = 33
    """
    A C++ namespace alias declaration.
    """
    UsingDirective = 34
    """
    A C++ using directive.
    """
    UsingDeclaration = 35
    """
    A C++ using declaration.
    """
    TypeAliasDecl = 36
    """
    A C++ alias declaration
    """
    ObjCSynthesizeDecl = 37
    """
    An Objective-C @synthesize definition.
    """
    ObjCDynamicDecl = 38
    """
    An Objective-C @dynamic definition.
    """
    CXXAccessSpecifier = 39
    """
    An access specifier.
    """
    FirstDecl = 1
    """
    An access specifier.
    """
    LastDecl = 39
    """
    An access specifier.
    """
    FirstRef = 40
    """
    Decl references
    """
    ObjCSuperClassRef = 40
    ObjCProtocolRef = 41
    ObjCClassRef = 42
    TypeRef = 43
    """
    A reference to a type declaration.
    """
    CXXBaseSpecifier = 44
    """
    A reference to a type declaration.
    """
    TemplateRef = 45
    """
    A reference to a class template, function template, template template parameter,
    or class template partial specialization.
    """
    NamespaceRef = 46
    """
    A reference to a namespace or namespace alias.
    """
    MemberRef = 47
    """
    A reference to a member of a struct, union, or class that occurs in some non-
    expression context, e.g., a designated initializer.
    """
    LabelRef = 48
    """
    A reference to a labeled statement.
    """
    OverloadedDeclRef = 49
    """
    A reference to a set of overloaded functions or function templates that has not
    yet been resolved to a specific function or function template.
    """
    VariableRef = 50
    """
    A reference to a variable that occurs in some non-expression context, e.g., a
    C++ lambda capture list.
    """
    LastRef = 50
    """
    A reference to a variable that occurs in some non-expression context, e.g., a
    C++ lambda capture list.
    """
    FirstInvalid = 70
    """
    Error conditions
    """
    InvalidFile = 70
    """
    Error conditions
    """
    NoDeclFound = 71
    """
    Error conditions
    """
    NotImplemented = 72
    """
    Error conditions
    """
    InvalidCode = 73
    """
    Error conditions
    """
    LastInvalid = 73
    """
    Error conditions
    """
    FirstExpr = 100
    """
    Expressions
    """
    UnexposedExpr = 100
    """
    An expression whose specific kind is not exposed via this interface.
    """
    DeclRefExpr = 101
    """
    An expression that refers to some value declaration, such as a function,
    variable, or enumerator.
    """
    MemberRefExpr = 102
    """
    An expression that refers to a member of a struct, union, class, Objective-C
    class, etc.
    """
    CallExpr = 103
    """
    An expression that calls a function.
    """
    ObjCMessageExpr = 104
    """
    An expression that sends a message to an Objective-C object or class.
    """
    BlockExpr = 105
    """
    An expression that represents a block literal.
    """
    IntegerLiteral = 106
    """
    An integer literal.
    """
    FloatingLiteral = 107
    """
    A floating point number literal.
    """
    ImaginaryLiteral = 108
    """
    An imaginary number literal.
    """
    StringLiteral = 109
    """
    A string literal.
    """
    CharacterLiteral = 110
    """
    A character literal.
    """
    ParenExpr = 111
    """
    A parenthesized expression, e.g. "(1)".
    """
    UnaryOperator = 112
    """
    This represents the unary-expression's (except sizeof and alignof).
    """
    ArraySubscriptExpr = 113
    """
    [C99 6.5.2.1] Array Subscripting.
    """
    BinaryOperator = 114
    """
    A builtin binary operation expression such as "x + y" or "x <= y".
    """
    CompoundAssignOperator = 115
    """
    Compound assignment such as "+=".
    """
    ConditionalOperator = 116
    """
    The ?: ternary operator.
    """
    CStyleCastExpr = 117
    """
    An explicit cast in C (C99 6.5.4) or a C-style cast in C++ (C++ [expr.cast]),
    which uses the syntax (Type)expr.
    """
    CompoundLiteralExpr = 118
    """
    [C99 6.5.2.5]
    """
    InitListExpr = 119
    """
    Describes an C or C++ initializer list.
    """
    AddrLabelExpr = 120
    """
    The GNU address of label extension, representing &&label.
    """
    StmtExpr = 121
    """
    This is the GNU Statement Expression extension: ({int X=4; X;})
    """
    GenericSelectionExpr = 122
    """
    Represents a C11 generic selection.
    """
    GNUNullExpr = 123
    """
    Implements the GNU __null extension, which is a name for a null pointer constant
    that has integral type (e.g., int or long) and is the same size and alignment as
    a pointer.
    """
    CXXStaticCastExpr = 124
    """
    C++'s static_cast<> expression.
    """
    CXXDynamicCastExpr = 125
    """
    C++'s dynamic_cast<> expression.
    """
    CXXReinterpretCastExpr = 126
    """
    C++'s reinterpret_cast<> expression.
    """
    CXXConstCastExpr = 127
    """
    C++'s const_cast<> expression.
    """
    CXXFunctionalCastExpr = 128
    """
    Represents an explicit C++ type conversion that uses "functional" notion (C++
    [expr.type.conv]).
    """
    CXXTypeidExpr = 129
    """
    A C++ typeid expression (C++ [expr.typeid]).
    """
    CXXBoolLiteralExpr = 130
    """
    [C++ 2.13.5] C++ Boolean Literal.
    """
    CXXNullPtrLiteralExpr = 131
    """
    [C++0x 2.14.7] C++ Pointer Literal.
    """
    CXXThisExpr = 132
    """
    Represents the "this" expression in C++
    """
    CXXThrowExpr = 133
    """
    [C++ 15] C++ Throw Expression.
    """
    CXXNewExpr = 134
    """
    A new expression for memory allocation and constructor calls, e.g: "new
    CXXNewExpr(foo)".
    """
    CXXDeleteExpr = 135
    """
    A delete expression for memory deallocation and destructor calls, e.g. "delete[]
    pArray".
    """
    UnaryExpr = 136
    """
    A unary expression. (noexcept, sizeof, or other traits)
    """
    ObjCStringLiteral = 137
    """
    An Objective-C string literal i.e. "foo".
    """
    ObjCEncodeExpr = 138
    """
    An Objective-C @encode expression.
    """
    ObjCSelectorExpr = 139
    """
    An Objective-C @selector expression.
    """
    ObjCProtocolExpr = 140
    """
    An Objective-C @protocol expression.
    """
    ObjCBridgedCastExpr = 141
    """
    An Objective-C "bridged" cast expression, which casts between Objective-C
    pointers and C pointers, transferring ownership in the process.
    """
    PackExpansionExpr = 142
    """
    Represents a C++0x pack expansion that produces a sequence of expressions.
    """
    SizeOfPackExpr = 143
    """
    Represents an expression that computes the length of a parameter pack.
    """
    LambdaExpr = 144
    """
    Represents a C++ lambda expression that produces a local function object.
    """
    ObjCBoolLiteralExpr = 145
    """
    Objective-c Boolean Literal.
    """
    ObjCSelfExpr = 146
    """
    Represents the "self" expression in an Objective-C method.
    """
    OMPArraySectionExpr = 147
    """
    OpenMP 5.0 [2.1.5, Array Section].
    """
    ObjCAvailabilityCheckExpr = 148
    """
    Represents an (...) check.
    """
    FixedPointLiteral = 149
    """
    Fixed point literal
    """
    OMPArrayShapingExpr = 150
    """
    OpenMP 5.0 [2.1.4, Array Shaping].
    """
    OMPIteratorExpr = 151
    """
    OpenMP 5.0 [2.1.6 Iterators]
    """
    CXXAddrspaceCastExpr = 152
    """
    OpenCL's addrspace_cast<> expression.
    """
    ConceptSpecializationExpr = 153
    """
    Expression that references a C++20 concept.
    """
    RequiresExpr = 154
    """
    Expression that references a C++20 concept.
    """
    LastExpr = 154
    """
    Expression that references a C++20 concept.
    """
    FirstStmt = 200
    """
    Statements
    """
    UnexposedStmt = 200
    """
    A statement whose specific kind is not exposed via this interface.
    """
    LabelStmt = 201
    """
    A labelled statement in a function.
    """
    CompoundStmt = 202
    """
    A group of statements like { stmt stmt }.
    """
    CaseStmt = 203
    """
    A case statement.
    """
    DefaultStmt = 204
    """
    A default statement.
    """
    IfStmt = 205
    """
    An if statement
    """
    SwitchStmt = 206
    """
    A switch statement.
    """
    WhileStmt = 207
    """
    A while statement.
    """
    DoStmt = 208
    """
    A do statement.
    """
    ForStmt = 209
    """
    A for statement.
    """
    GotoStmt = 210
    """
    A goto statement.
    """
    IndirectGotoStmt = 211
    """
    An indirect goto statement.
    """
    ContinueStmt = 212
    """
    A continue statement.
    """
    BreakStmt = 213
    """
    A break statement.
    """
    ReturnStmt = 214
    """
    A return statement.
    """
    GCCAsmStmt = 215
    """
    A GCC inline assembly statement extension.
    """
    AsmStmt = 215
    """
    A GCC inline assembly statement extension.
    """
    ObjCAtTryStmt = 216
    """
    Objective-C's overall @try-@catch-@finally statement.
    """
    ObjCAtCatchStmt = 217
    """
    Objective-C's @catch statement.
    """
    ObjCAtFinallyStmt = 218
    """
    Objective-C's @finally statement.
    """
    ObjCAtThrowStmt = 219
    """
    Objective-C's @throw statement.
    """
    ObjCAtSynchronizedStmt = 220
    """
    Objective-C's @synchronized statement.
    """
    ObjCAutoreleasePoolStmt = 221
    """
    Objective-C's autorelease pool statement.
    """
    ObjCForCollectionStmt = 222
    """
    Objective-C's collection statement.
    """
    CXXCatchStmt = 223
    """
    C++'s catch statement.
    """
    CXXTryStmt = 224
    """
    C++'s try statement.
    """
    CXXForRangeStmt = 225
    """
    C++'s for (* : *) statement.
    """
    SEHTryStmt = 226
    """
    Windows Structured Exception Handling's try statement.
    """
    SEHExceptStmt = 227
    """
    Windows Structured Exception Handling's except statement.
    """
    SEHFinallyStmt = 228
    """
    Windows Structured Exception Handling's finally statement.
    """
    MSAsmStmt = 229
    """
    A MS inline assembly statement extension.
    """
    NullStmt = 230
    """
    The null statement ";": C99 6.8.3p3.
    """
    DeclStmt = 231
    """
    Adaptor class for mixing declarations with statements and expressions.
    """
    OMPParallelDirective = 232
    """
    OpenMP parallel directive.
    """
    OMPSimdDirective = 233
    """
    OpenMP SIMD directive.
    """
    OMPForDirective = 234
    """
    OpenMP for directive.
    """
    OMPSectionsDirective = 235
    """
    OpenMP sections directive.
    """
    OMPSectionDirective = 236
    """
    OpenMP section directive.
    """
    OMPSingleDirective = 237
    """
    OpenMP single directive.
    """
    OMPParallelForDirective = 238
    """
    OpenMP parallel for directive.
    """
    OMPParallelSectionsDirective = 239
    """
    OpenMP parallel sections directive.
    """
    OMPTaskDirective = 240
    """
    OpenMP task directive.
    """
    OMPMasterDirective = 241
    """
    OpenMP master directive.
    """
    OMPCriticalDirective = 242
    """
    OpenMP critical directive.
    """
    OMPTaskyieldDirective = 243
    """
    OpenMP taskyield directive.
    """
    OMPBarrierDirective = 244
    """
    OpenMP barrier directive.
    """
    OMPTaskwaitDirective = 245
    """
    OpenMP taskwait directive.
    """
    OMPFlushDirective = 246
    """
    OpenMP flush directive.
    """
    SEHLeaveStmt = 247
    """
    Windows Structured Exception Handling's leave statement.
    """
    OMPOrderedDirective = 248
    """
    OpenMP ordered directive.
    """
    OMPAtomicDirective = 249
    """
    OpenMP atomic directive.
    """
    OMPForSimdDirective = 250
    """
    OpenMP for SIMD directive.
    """
    OMPParallelForSimdDirective = 251
    """
    OpenMP parallel for SIMD directive.
    """
    OMPTargetDirective = 252
    """
    OpenMP target directive.
    """
    OMPTeamsDirective = 253
    """
    OpenMP teams directive.
    """
    OMPTaskgroupDirective = 254
    """
    OpenMP taskgroup directive.
    """
    OMPCancellationPointDirective = 255
    """
    OpenMP cancellation point directive.
    """
    OMPCancelDirective = 256
    """
    OpenMP cancel directive.
    """
    OMPTargetDataDirective = 257
    """
    OpenMP target data directive.
    """
    OMPTaskLoopDirective = 258
    """
    OpenMP taskloop directive.
    """
    OMPTaskLoopSimdDirective = 259
    """
    OpenMP taskloop simd directive.
    """
    OMPDistributeDirective = 260
    """
    OpenMP distribute directive.
    """
    OMPTargetEnterDataDirective = 261
    """
    OpenMP target enter data directive.
    """
    OMPTargetExitDataDirective = 262
    """
    OpenMP target exit data directive.
    """
    OMPTargetParallelDirective = 263
    """
    OpenMP target parallel directive.
    """
    OMPTargetParallelForDirective = 264
    """
    OpenMP target parallel for directive.
    """
    OMPTargetUpdateDirective = 265
    """
    OpenMP target update directive.
    """
    OMPDistributeParallelForDirective = 266
    """
    OpenMP distribute parallel for directive.
    """
    OMPDistributeParallelForSimdDirective = 267
    """
    OpenMP distribute parallel for simd directive.
    """
    OMPDistributeSimdDirective = 268
    """
    OpenMP distribute simd directive.
    """
    OMPTargetParallelForSimdDirective = 269
    """
    OpenMP target parallel for simd directive.
    """
    OMPTargetSimdDirective = 270
    """
    OpenMP target simd directive.
    """
    OMPTeamsDistributeDirective = 271
    """
    OpenMP teams distribute directive.
    """
    OMPTeamsDistributeSimdDirective = 272
    """
    OpenMP teams distribute simd directive.
    """
    OMPTeamsDistributeParallelForSimdDirective = 273
    """
    OpenMP teams distribute parallel for simd directive.
    """
    OMPTeamsDistributeParallelForDirective = 274
    """
    OpenMP teams distribute parallel for directive.
    """
    OMPTargetTeamsDirective = 275
    """
    OpenMP target teams directive.
    """
    OMPTargetTeamsDistributeDirective = 276
    """
    OpenMP target teams distribute directive.
    """
    OMPTargetTeamsDistributeParallelForDirective = 277
    """
    OpenMP target teams distribute parallel for directive.
    """
    OMPTargetTeamsDistributeParallelForSimdDirective = 278
    """
    OpenMP target teams distribute parallel for simd directive.
    """
    OMPTargetTeamsDistributeSimdDirective = 279
    """
    OpenMP target teams distribute simd directive.
    """
    BuiltinBitCastExpr = 280
    """
    C++2a std::bit_cast expression.
    """
    OMPMasterTaskLoopDirective = 281
    """
    OpenMP master taskloop directive.
    """
    OMPParallelMasterTaskLoopDirective = 282
    """
    OpenMP parallel master taskloop directive.
    """
    OMPMasterTaskLoopSimdDirective = 283
    """
    OpenMP master taskloop simd directive.
    """
    OMPParallelMasterTaskLoopSimdDirective = 284
    """
    OpenMP parallel master taskloop simd directive.
    """
    OMPParallelMasterDirective = 285
    """
    OpenMP parallel master directive.
    """
    OMPDepobjDirective = 286
    """
    OpenMP depobj directive.
    """
    OMPScanDirective = 287
    """
    OpenMP scan directive.
    """
    OMPTileDirective = 288
    """
    OpenMP tile directive.
    """
    OMPCanonicalLoop = 289
    """
    OpenMP canonical loop.
    """
    OMPInteropDirective = 290
    """
    OpenMP interop directive.
    """
    OMPDispatchDirective = 291
    """
    OpenMP dispatch directive.
    """
    OMPMaskedDirective = 292
    """
    OpenMP masked directive.
    """
    OMPUnrollDirective = 293
    """
    OpenMP unroll directive.
    """
    OMPMetaDirective = 294
    """
    OpenMP metadirective directive.
    """
    OMPGenericLoopDirective = 295
    """
    OpenMP loop directive.
    """
    OMPTeamsGenericLoopDirective = 296
    """
    OpenMP teams loop directive.
    """
    OMPTargetTeamsGenericLoopDirective = 297
    """
    OpenMP target teams loop directive.
    """
    OMPParallelGenericLoopDirective = 298
    """
    OpenMP parallel loop directive.
    """
    OMPTargetParallelGenericLoopDirective = 299
    """
    OpenMP target parallel loop directive.
    """
    OMPParallelMaskedDirective = 300
    """
    OpenMP parallel masked directive.
    """
    OMPMaskedTaskLoopDirective = 301
    """
    OpenMP masked taskloop directive.
    """
    OMPMaskedTaskLoopSimdDirective = 302
    """
    OpenMP masked taskloop simd directive.
    """
    OMPParallelMaskedTaskLoopDirective = 303
    """
    OpenMP parallel masked taskloop directive.
    """
    OMPParallelMaskedTaskLoopSimdDirective = 304
    """
    OpenMP parallel masked taskloop simd directive.
    """
    LastStmt = 304
    """
    OpenMP parallel masked taskloop simd directive.
    """
    TranslationUnit = 350
    """
    Cursor that represents the translation unit itself.
    """
    FirstAttr = 400
    """
    Attributes
    """
    UnexposedAttr = 400
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    IBActionAttr = 401
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    IBOutletAttr = 402
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    IBOutletCollectionAttr = 403
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    CXXFinalAttr = 404
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    CXXOverrideAttr = 405
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    AnnotateAttr = 406
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    AsmLabelAttr = 407
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    PackedAttr = 408
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    PureAttr = 409
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ConstAttr = 410
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    NoDuplicateAttr = 411
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    CUDAConstantAttr = 412
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    CUDADeviceAttr = 413
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    CUDAGlobalAttr = 414
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    CUDAHostAttr = 415
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    CUDASharedAttr = 416
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    VisibilityAttr = 417
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    DLLExport = 418
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    DLLImport = 419
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    NSReturnsRetained = 420
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    NSReturnsNotRetained = 421
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    NSReturnsAutoreleased = 422
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    NSConsumesSelf = 423
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    NSConsumed = 424
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCException = 425
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCNSObject = 426
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCIndependentClass = 427
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCPreciseLifetime = 428
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCReturnsInnerPointer = 429
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCRequiresSuper = 430
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCRootClass = 431
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCSubclassingRestricted = 432
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCExplicitProtocolImpl = 433
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCDesignatedInitializer = 434
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCRuntimeVisible = 435
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ObjCBoxable = 436
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    FlagEnum = 437
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    ConvergentAttr = 438
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    WarnUnusedAttr = 439
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    WarnUnusedResultAttr = 440
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    AlignedAttr = 441
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    LastAttr = 441
    """
    An attribute whose specific kind is not exposed via this interface.
    """
    PreprocessingDirective = 500
    """
    Preprocessing
    """
    MacroDefinition = 501
    """
    Preprocessing
    """
    MacroExpansion = 502
    """
    Preprocessing
    """
    MacroInstantiation = 502
    """
    Preprocessing
    """
    InclusionDirective = 503
    """
    Preprocessing
    """
    FirstPreprocessing = 500
    """
    Preprocessing
    """
    LastPreprocessing = 503
    """
    Preprocessing
    """
    ModuleImportDecl = 600
    """
    Extra Declarations
    """
    TypeAliasTemplateDecl = 601
    """
    Extra Declarations
    """
    StaticAssert = 602
    """
    A static_assert or _Static_assert node
    """
    FriendDecl = 603
    """
    a friend declaration.
    """
    ConceptDecl = 604
    """
    a concept declaration.
    """
    FirstExtraDecl = 600
    """
    a concept declaration.
    """
    LastExtraDecl = 604
    """
    a concept declaration.
    """
    OverloadCandidate = 700
    """
    A code completion overload candidate.
    """


class CXLinkageKind(_Enum):
    """
    Describe the linkage of the entity referred to by a cursor.
    """
    Invalid = 0
    """
    This value indicates that no linkage information is available for a provided
    CXCursor.
    """
    NoLinkage = 1
    """
    This is the linkage for variables, parameters, and so on that have automatic
    storage. This covers normal (non-extern) local variables.
    """
    Internal = 2
    """
    This is the linkage for static variables and static functions.
    """
    UniqueExternal = 3
    """
    This is the linkage for entities with external linkage that live in C++
    anonymous namespaces.
    """
    External = 4
    """
    This is the linkage for entities with true, external linkage.
    """


class CXVisibilityKind(_Enum):
    Invalid = 0
    """
    This value indicates that no visibility information is available for a provided
    CXCursor.
    """
    Hidden = 1
    """
    Symbol not seen by the linker.
    """
    Protected = 2
    """
    Symbol seen by the linker but resolves to a symbol inside this object.
    """
    Default = 3
    """
    Symbol seen by the linker and acts like a normal symbol.
    """


class CXLanguageKind(_Enum):
    """
    Describe the "language" of the entity referred to by a cursor.
    """
    Invalid = 0
    C = 1
    ObjC = 2
    CPlusPlus = 3


class CXTLSKind(_Enum):
    """
    Describe the "thread-local storage (TLS) kind" of the declaration referred to by
    a cursor.
    """
    None_ = 0
    Dynamic = 1
    Static = 2


class CXTypeKind(_Enum):
    """
    Describes the kind of type
    """
    Invalid = 0
    """
    Represents an invalid type (e.g., where no type is available).
    """
    Unexposed = 1
    """
    A type whose specific kind is not exposed via this interface.
    """
    Void = 2
    """
    Builtin types
    """
    Bool = 3
    """
    Builtin types
    """
    Char_U = 4
    """
    Builtin types
    """
    UChar = 5
    """
    Builtin types
    """
    Char16 = 6
    """
    Builtin types
    """
    Char32 = 7
    """
    Builtin types
    """
    UShort = 8
    """
    Builtin types
    """
    UInt = 9
    """
    Builtin types
    """
    ULong = 10
    """
    Builtin types
    """
    ULongLong = 11
    """
    Builtin types
    """
    UInt128 = 12
    """
    Builtin types
    """
    Char_S = 13
    """
    Builtin types
    """
    SChar = 14
    """
    Builtin types
    """
    WChar = 15
    """
    Builtin types
    """
    Short = 16
    """
    Builtin types
    """
    Int = 17
    """
    Builtin types
    """
    Long = 18
    """
    Builtin types
    """
    LongLong = 19
    """
    Builtin types
    """
    Int128 = 20
    """
    Builtin types
    """
    Float = 21
    """
    Builtin types
    """
    Double = 22
    """
    Builtin types
    """
    LongDouble = 23
    """
    Builtin types
    """
    NullPtr = 24
    """
    Builtin types
    """
    Overload = 25
    """
    Builtin types
    """
    Dependent = 26
    """
    Builtin types
    """
    ObjCId = 27
    """
    Builtin types
    """
    ObjCClass = 28
    """
    Builtin types
    """
    ObjCSel = 29
    """
    Builtin types
    """
    Float128 = 30
    """
    Builtin types
    """
    Half = 31
    """
    Builtin types
    """
    Float16 = 32
    """
    Builtin types
    """
    ShortAccum = 33
    """
    Builtin types
    """
    Accum = 34
    """
    Builtin types
    """
    LongAccum = 35
    """
    Builtin types
    """
    UShortAccum = 36
    """
    Builtin types
    """
    UAccum = 37
    """
    Builtin types
    """
    ULongAccum = 38
    """
    Builtin types
    """
    BFloat16 = 39
    """
    Builtin types
    """
    Ibm128 = 40
    """
    Builtin types
    """
    FirstBuiltin = 2
    """
    Builtin types
    """
    LastBuiltin = 40
    """
    Builtin types
    """
    Complex = 100
    """
    Builtin types
    """
    Pointer = 101
    """
    Builtin types
    """
    BlockPointer = 102
    """
    Builtin types
    """
    LValueReference = 103
    """
    Builtin types
    """
    RValueReference = 104
    """
    Builtin types
    """
    Record = 105
    """
    Builtin types
    """
    Enum = 106
    """
    Builtin types
    """
    Typedef = 107
    """
    Builtin types
    """
    ObjCInterface = 108
    """
    Builtin types
    """
    ObjCObjectPointer = 109
    """
    Builtin types
    """
    FunctionNoProto = 110
    """
    Builtin types
    """
    FunctionProto = 111
    """
    Builtin types
    """
    ConstantArray = 112
    """
    Builtin types
    """
    Vector = 113
    """
    Builtin types
    """
    IncompleteArray = 114
    """
    Builtin types
    """
    VariableArray = 115
    """
    Builtin types
    """
    DependentSizedArray = 116
    """
    Builtin types
    """
    MemberPointer = 117
    """
    Builtin types
    """
    Auto = 118
    """
    Builtin types
    """
    Elaborated = 119
    """
    Represents a type that was referred to using an elaborated type keyword.
    """
    Pipe = 120
    """
    OpenCL PipeType.
    """
    OCLImage1dRO = 121
    """
    OpenCL builtin types.
    """
    OCLImage1dArrayRO = 122
    """
    OpenCL builtin types.
    """
    OCLImage1dBufferRO = 123
    """
    OpenCL builtin types.
    """
    OCLImage2dRO = 124
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayRO = 125
    """
    OpenCL builtin types.
    """
    OCLImage2dDepthRO = 126
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayDepthRO = 127
    """
    OpenCL builtin types.
    """
    OCLImage2dMSAARO = 128
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayMSAARO = 129
    """
    OpenCL builtin types.
    """
    OCLImage2dMSAADepthRO = 130
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayMSAADepthRO = 131
    """
    OpenCL builtin types.
    """
    OCLImage3dRO = 132
    """
    OpenCL builtin types.
    """
    OCLImage1dWO = 133
    """
    OpenCL builtin types.
    """
    OCLImage1dArrayWO = 134
    """
    OpenCL builtin types.
    """
    OCLImage1dBufferWO = 135
    """
    OpenCL builtin types.
    """
    OCLImage2dWO = 136
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayWO = 137
    """
    OpenCL builtin types.
    """
    OCLImage2dDepthWO = 138
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayDepthWO = 139
    """
    OpenCL builtin types.
    """
    OCLImage2dMSAAWO = 140
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayMSAAWO = 141
    """
    OpenCL builtin types.
    """
    OCLImage2dMSAADepthWO = 142
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayMSAADepthWO = 143
    """
    OpenCL builtin types.
    """
    OCLImage3dWO = 144
    """
    OpenCL builtin types.
    """
    OCLImage1dRW = 145
    """
    OpenCL builtin types.
    """
    OCLImage1dArrayRW = 146
    """
    OpenCL builtin types.
    """
    OCLImage1dBufferRW = 147
    """
    OpenCL builtin types.
    """
    OCLImage2dRW = 148
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayRW = 149
    """
    OpenCL builtin types.
    """
    OCLImage2dDepthRW = 150
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayDepthRW = 151
    """
    OpenCL builtin types.
    """
    OCLImage2dMSAARW = 152
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayMSAARW = 153
    """
    OpenCL builtin types.
    """
    OCLImage2dMSAADepthRW = 154
    """
    OpenCL builtin types.
    """
    OCLImage2dArrayMSAADepthRW = 155
    """
    OpenCL builtin types.
    """
    OCLImage3dRW = 156
    """
    OpenCL builtin types.
    """
    OCLSampler = 157
    """
    OpenCL builtin types.
    """
    OCLEvent = 158
    """
    OpenCL builtin types.
    """
    OCLQueue = 159
    """
    OpenCL builtin types.
    """
    OCLReserveID = 160
    """
    OpenCL builtin types.
    """
    ObjCObject = 161
    """
    OpenCL builtin types.
    """
    ObjCTypeParam = 162
    """
    OpenCL builtin types.
    """
    Attributed = 163
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCMcePayload = 164
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCImePayload = 165
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCRefPayload = 166
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCSicPayload = 167
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCMceResult = 168
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCImeResult = 169
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCRefResult = 170
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCSicResult = 171
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCImeResultSingleRefStreamout = 172
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCImeResultDualRefStreamout = 173
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCImeSingleRefStreamin = 174
    """
    OpenCL builtin types.
    """
    OCLIntelSubgroupAVCImeDualRefStreamin = 175
    """
    OpenCL builtin types.
    """
    ExtVector = 176
    """
    OpenCL builtin types.
    """
    Atomic = 177
    """
    OpenCL builtin types.
    """
    BTFTagAttributed = 178
    """
    OpenCL builtin types.
    """


class CXCallingConv(_Enum):
    """
    Describes the calling convention of a function type
    """
    Default = 0
    C = 1
    X86StdCall = 2
    X86FastCall = 3
    X86ThisCall = 4
    X86Pascal = 5
    AAPCS = 6
    AAPCS_VFP = 7
    X86RegCall = 8
    IntelOclBicc = 9
    Win64 = 10
    X86_64Win64 = 10
    """
    Alias for compatibility with older versions of API.
    """
    X86_64SysV = 11
    """
    Alias for compatibility with older versions of API.
    """
    X86VectorCall = 12
    """
    Alias for compatibility with older versions of API.
    """
    Swift = 13
    """
    Alias for compatibility with older versions of API.
    """
    PreserveMost = 14
    """
    Alias for compatibility with older versions of API.
    """
    PreserveAll = 15
    """
    Alias for compatibility with older versions of API.
    """
    AArch64VectorCall = 16
    """
    Alias for compatibility with older versions of API.
    """
    SwiftAsync = 17
    """
    Alias for compatibility with older versions of API.
    """
    AArch64SVEPCS = 18
    """
    Alias for compatibility with older versions of API.
    """
    Invalid = 100
    """
    Alias for compatibility with older versions of API.
    """
    Unexposed = 200
    """
    Alias for compatibility with older versions of API.
    """


class CXTemplateArgumentKind(_Enum):
    """
    Describes the kind of a template argument.
    """
    Null = 0
    Type = 1
    Declaration = 2
    NullPtr = 3
    Integral = 4
    Template = 5
    TemplateExpansion = 6
    Expression = 7
    Pack = 8
    Invalid = 9
    """
    Indicates an error case, preventing the kind from being deduced.
    """


class CXTypeNullabilityKind(_Enum):
    NonNull = 0
    """
    Values of this type can never be null.
    """
    Nullable = 1
    """
    Values of this type can be null.
    """
    Unspecified = 2
    """
    Whether values of this type can be null is (explicitly) unspecified. This
    captures a (fairly rare) case where we can't conclude anything about the
    nullability of the type even though it has been considered.
    """
    Invalid = 3
    """
    Nullability is not applicable to this type.
    """
    NullableResult = 4
    """
    Generally behaves like Nullable, except when used in a block parameter that was
    imported into a swift async method. There, swift will assume that the parameter
    can get null even if no error occurred. _Nullable parameters are assumed to only
    get null on error.
    """


class CXTypeLayoutError(_Enum):
    """
    List the possible error codes for clang_Type_getSizeOf, clang_Type_getAlignOf,
    clang_Type_getOffsetOf and clang_Cursor_getOffsetOf.
    """
    Invalid = -1
    """
    Type is of kind CXType_Invalid.
    """
    Incomplete = -2
    """
    The type is an incomplete Type.
    """
    Dependent = -3
    """
    The type is a dependent Type.
    """
    NotConstantSize = -4
    """
    The type is not a constant size type.
    """
    InvalidFieldName = -5
    """
    The Field name is not valid for this record.
    """
    Undeduced = -6
    """
    The type is undeduced.
    """


class CXRefQualifierKind(_Enum):
    None_ = 0
    """
    No ref-qualifier was provided.
    """
    LValue = 1
    """
    An lvalue ref-qualifier was provided ( &).
    """
    RValue = 2
    """
    An rvalue ref-qualifier was provided ( &&).
    """


# noinspection PyPep8Naming
class CX_CXXAccessSpecifier(_Enum):
    """
    Represents the C++ access control level to a base class for a cursor with kind
    CX_CXXBaseSpecifier.
    """
    InvalidAccessSpecifier = 0
    Public = 1
    Protected = 2
    Private = 3


# noinspection PyPep8Naming
class CX_StorageClass(_Enum):
    """
    Represents the storage classes as declared in the source. CX_SC_Invalid was
    added for the case that the passed cursor in not a declaration.
    """
    Invalid = 0
    None_ = 1
    Extern = 2
    Static = 3
    PrivateExtern = 4
    OpenCLWorkGroupLocal = 5
    Auto = 6
    Register = 7


class CXChildVisitResult(_Enum):
    """
    Describes how the traversal of the children of a particular cursor should
    proceed after visiting a particular child cursor.
    """
    Break = 0
    """
    Terminates the cursor traversal.
    """
    Continue = 1
    """
    Continues the cursor traversal with the next sibling of the cursor just visited,
    without visiting its children.
    """
    Recurse = 2
    """
    Recursively traverse the children of this cursor, using the same visitor and
    client data.
    """


class CXPrintingPolicyProperty(_Enum):
    """
    Properties for the printing policy.
    """
    Indentation = 0
    SuppressSpecifiers = 1
    SuppressTagKeyword = 2
    IncludeTagDefinition = 3
    SuppressScope = 4
    SuppressUnwrittenScope = 5
    SuppressInitializers = 6
    ConstantArraySizeAsWritten = 7
    AnonymousTagLocations = 8
    SuppressStrongLifetime = 9
    SuppressLifetimeQualifiers = 10
    SuppressTemplateArgsInCXXConstructors = 11
    Bool = 12
    Restrict = 13
    Alignof = 14
    UnderscoreAlignof = 15
    UseVoidForZeroParams = 16
    TerseOutput = 17
    PolishForDeclaration = 18
    Half = 19
    MSWChar = 20
    IncludeNewlines = 21
    MSVCFormatting = 22
    ConstantsAsWritten = 23
    SuppressImplicitBase = 24
    FullyQualifiedName = 25
    LastProperty = 25


class CXObjCPropertyAttrKind(_Enum):
    """
    Property attributes for a CXCursor_ObjCPropertyDecl.
    """
    noattr = 0
    readonly = 1
    getter = 2
    assign = 4
    readwrite = 8
    retain = 16
    copy = 32
    nonatomic = 64
    setter = 128
    atomic = 256
    weak = 512
    strong = 1024
    unsafe_unretained = 2048
    class_ = 4096


class CXObjCDeclQualifierKind(_Enum):
    """
    'Qualifiers' written next to the return and parameter types in Objective-C
    method declarations.
    """
    None_ = 0
    In = 1
    Inout = 2
    Out = 4
    Bycopy = 8
    Byref = 16
    Oneway = 32


class CXNameRefFlags(_Enum):
    WantQualifier = 1
    """
    Include the nested-name-specifier, e.g. Foo:: in x.Foo::y, in the range.
    """
    WantTemplateArgs = 2
    """
    Include the explicit template arguments, e.g. <int> in x.f<int>, in the range.
    """
    WantSinglePiece = 4
    """
    If the name is non-contiguous, return the full spanning range.
    """


class CXTokenKind(_Enum):
    """
    Describes a kind of token.
    """
    Punctuation = 0
    """
    A token that contains some kind of punctuation.
    """
    Keyword = 1
    """
    A language keyword.
    """
    Identifier = 2
    """
    An identifier (that is not a keyword).
    """
    Literal = 3
    """
    A numeric, string, or character literal.
    """
    Comment = 4
    """
    A comment.
    """


class CXCompletionChunkKind(_Enum):
    """
    Describes a single piece of text within a code-completion string.
    """
    Optional = 0
    """
    A code-completion string that describes "optional" text that could be a part of
    the template (but is not required).
    """
    TypedText = 1
    """
    Text that a user would be expected to type to get this code-completion result.
    """
    Text = 2
    """
    Text that should be inserted as part of a code-completion result.
    """
    Placeholder = 3
    """
    Placeholder text that should be replaced by the user.
    """
    Informative = 4
    """
    Informative text that should be displayed but never inserted as part of the
    template.
    """
    CurrentParameter = 5
    """
    Text that describes the current parameter when code-completion is referring to
    function call, message send, or template specialization.
    """
    LeftParen = 6
    """
    A left parenthesis ('('), used to initiate a function call or signal the
    beginning of a function parameter list.
    """
    RightParen = 7
    """
    A right parenthesis (')'), used to finish a function call or signal the end of a
    function parameter list.
    """
    LeftBracket = 8
    """
    A left bracket ('[').
    """
    RightBracket = 9
    """
    A right bracket (']').
    """
    LeftBrace = 10
    """
    A left brace ('{').
    """
    RightBrace = 11
    """
    A right brace ('}').
    """
    LeftAngle = 12
    """
    A left angle bracket ('<').
    """
    RightAngle = 13
    """
    A right angle bracket ('>').
    """
    Comma = 14
    """
    A comma separator (',').
    """
    ResultType = 15
    """
    Text that specifies the result type of a given result.
    """
    Colon = 16
    """
    A colon (':').
    """
    SemiColon = 17
    """
    A semicolon (';').
    """
    Equal = 18
    """
    An '=' sign.
    """
    HorizontalSpace = 19
    """
    Horizontal space (' ').
    """
    VerticalSpace = 20
    """
    Vertical space ('\n'), after which it is generally a good idea to perform
    indentation.
    """


# noinspection PyPep8Naming
class CXCodeComplete_Flags(_Enum):
    """
    Flags that can be passed to clang_codeCompleteAt() to modify its behavior.
    """
    IncludeMacros = 1
    """
    Whether to include macros within the set of code completions returned.
    """
    IncludeCodePatterns = 2
    """
    Whether to include code patterns for language constructs within the set of code
    completions, e.g., for loops.
    """
    IncludeBriefComments = 4
    """
    Whether to include brief documentation within the set of code completions
    returned.
    """
    SkipPreamble = 8
    """
    Whether to speed up completion by omitting top- or namespace-level entities
    defined in the preamble. There's no guarantee any particular entity is omitted.
    This may be useful if the headers are indexed externally.
    """
    IncludeCompletionsWithFixIts = 16
    """
    Whether to include completions with small fix-its, e.g. change '.' to '->' on
    member access, etc.
    """


class CXCompletionContext(_Enum):
    """
    Bits that represent the context under which completion is occurring.
    """
    Unexposed = 0
    """
    The context for completions is unexposed, as only Clang results should be
    included. (This is equivalent to having no context bits set.)
    """
    AnyType = 1
    """
    Completions for any possible type should be included in the results.
    """
    AnyValue = 2
    """
    Completions for any possible value (variables, function calls, etc.) should be
    included in the results.
    """
    ObjCObjectValue = 4
    """
    Completions for values that resolve to an Objective-C object should be included
    in the results.
    """
    ObjCSelectorValue = 8
    """
    Completions for values that resolve to an Objective-C selector should be
    included in the results.
    """
    CXXClassTypeValue = 16
    """
    Completions for values that resolve to a C++ class type should be included in
    the results.
    """
    DotMemberAccess = 32
    """
    Completions for fields of the member being accessed using the dot operator
    should be included in the results.
    """
    ArrowMemberAccess = 64
    """
    Completions for fields of the member being accessed using the arrow operator
    should be included in the results.
    """
    ObjCPropertyAccess = 128
    """
    Completions for properties of the Objective-C object being accessed using the
    dot operator should be included in the results.
    """
    EnumTag = 256
    """
    Completions for enum tags should be included in the results.
    """
    UnionTag = 512
    """
    Completions for union tags should be included in the results.
    """
    StructTag = 1024
    """
    Completions for struct tags should be included in the results.
    """
    ClassTag = 2048
    """
    Completions for C++ class names should be included in the results.
    """
    Namespace = 4096
    """
    Completions for C++ namespaces and namespace aliases should be included in the
    results.
    """
    NestedNameSpecifier = 8192
    """
    Completions for C++ nested name specifiers should be included in the results.
    """
    ObjCInterface = 16384
    """
    Completions for Objective-C interfaces (classes) should be included in the
    results.
    """
    ObjCProtocol = 32768
    """
    Completions for Objective-C protocols should be included in the results.
    """
    ObjCCategory = 65536
    """
    Completions for Objective-C categories should be included in the results.
    """
    ObjCInstanceMessage = 131072
    """
    Completions for Objective-C instance messages should be included in the results.
    """
    ObjCClassMessage = 262144
    """
    Completions for Objective-C class messages should be included in the results.
    """
    ObjCSelectorName = 524288
    """
    Completions for Objective-C selector names should be included in the results.
    """
    MacroName = 1048576
    """
    Completions for preprocessor macro names should be included in the results.
    """
    NaturalLanguage = 2097152
    """
    Natural language completions should be included in the results.
    """
    IncludedFile = 4194304
    """
    #include file completions should be included in the results.
    """
    Unknown = 8388607
    """
    The current context is unknown, so set all contexts.
    """


class CXEvalResultKind(_Enum):
    Int = 1
    Float = 2
    ObjCStrLiteral = 3
    StrLiteral = 4
    CFStr = 5
    Other = 6
    UnExposed = 0


class CXVisitorResult(_Enum):
    Break = 0
    Continue = 1


class CXResult(_Enum):
    """
    Function returned successfully.
    """
    CXResult_Success = 0
    """
    Function returned successfully.
    """
    CXResult_Invalid = 1
    """
    One of the parameters was invalid for the function.
    """
    CXResult_VisitBreak = 2
    """
    The function was terminated by a callback (e.g. it returned CXVisit_Break)
    """


class CXIdxEntityKind(_Enum):
    Unexposed = 0
    Typedef = 1
    Function = 2
    Variable = 3
    Field = 4
    EnumConstant = 5
    ObjCClass = 6
    ObjCProtocol = 7
    ObjCCategory = 8
    ObjCInstanceMethod = 9
    ObjCClassMethod = 10
    ObjCProperty = 11
    ObjCIvar = 12
    Enum = 13
    Struct = 14
    Union = 15
    CXXClass = 16
    CXXNamespace = 17
    CXXNamespaceAlias = 18
    CXXStaticVariable = 19
    CXXStaticMethod = 20
    CXXInstanceMethod = 21
    CXXConstructor = 22
    CXXDestructor = 23
    CXXConversionFunction = 24
    CXXTypeAlias = 25
    CXXInterface = 26
    CXXConcept = 27


class CXIdxEntityLanguage(_Enum):
    None_ = 0
    C = 1
    ObjC = 2
    CXX = 3
    Swift = 4


class CXIdxEntityCXXTemplateKind(_Enum):
    """
    Extra C++ template information for an entity. This can apply to:
    CXIdxEntity_Function CXIdxEntity_CXXClass CXIdxEntity_CXXStaticMethod
    CXIdxEntity_CXXInstanceMethod CXIdxEntity_CXXConstructor
    CXIdxEntity_CXXConversionFunction CXIdxEntity_CXXTypeAlias
    """
    CXIdxEntity_NonTemplate = 0
    CXIdxEntity_Template = 1
    CXIdxEntity_TemplatePartialSpecialization = 2
    CXIdxEntity_TemplateSpecialization = 3


class CXIdxAttrKind(_Enum):
    Unexposed = 0
    IBAction = 1
    IBOutlet = 2
    IBOutletCollection = 3


class CXIdxDeclInfoFlags(_Enum):
    Skipped = 1


class CXIdxObjCContainerKind(_Enum):
    ForwardRef = 0
    Interface = 1
    Implementation = 2


class CXIdxEntityRefKind(_Enum):
    """
    Data for IndexerCallbacks#indexEntityReference.
    """
    Direct = 1
    """
    The entity is referenced directly in user's code.
    """
    Implicit = 2
    """
    An implicit reference, e.g. a reference of an Objective-C method via the dot
    syntax.
    """


class CXSymbolRole(_Enum):
    """
    Roles that are attributed to symbol occurrences.
    """
    None_ = 0
    Declaration = 1
    Definition = 2
    Reference = 4
    Read = 8
    Write = 16
    Call = 32
    Dynamic = 64
    AddressOf = 128
    Implicit = 256


class CXIndexOptFlags(_Enum):
    """
    Used to indicate that no special indexing options are needed.
    """
    None_ = 0
    """
    Used to indicate that no special indexing options are needed.
    """
    SuppressRedundantRefs = 1
    """
    Used to indicate that IndexerCallbacks#indexEntityReference should be invoked
    for only one reference of an entity per source file that does not also include a
    declaration/definition of the entity.
    """
    IndexFunctionLocalSymbols = 2
    """
    Function-local symbols should be indexed. If this is not set function-local
    symbols will be ignored.
    """
    IndexImplicitTemplateInstantiations = 4
    """
    Implicit function/class template instantiations should be indexed. If this is
    not set, implicit instantiations will be ignored.
    """
    SuppressWarnings = 8
    """
    Suppress all compiler warnings when parsing for indexing.
    """
    SkipParsedBodiesInSession = 16
    """
    Skip a function/method body that was already parsed during an indexing session
    associated with a CXIndexAction object. Bodies in system headers are always
    skipped.
    """

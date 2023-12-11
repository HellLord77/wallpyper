from . import _Enum


# zstd
# noinspection PyPep8Naming
class ZSTD_strategy(_Enum):
    """
    Compression strategies, listed from fastest to strongest
    """
    fast = 1
    dfast = 2
    greedy = 3
    lazy = 4
    lazy2 = 5
    btlazy2 = 6
    btopt = 7
    btultra = 8
    btultra2 = 9


# noinspection PyPep8Naming
class ZSTD_cParameter(_Enum):
    """
    compression parameters Note: When compressing with a ZSTD_CDict these parameters
    are superseded by the parameters used to construct the ZSTD_CDict. See
    ZSTD_CCtx_refCDict() for more info (superseded-by-cdict).
    """
    compressionLevel = 100
    """
    Set compression parameters according to pre-defined cLevel table. Note that
    exact compression parameters are dynamically determined, depending on both
    compression level and srcSize (when known). Default level is
    ZSTD_CLEVEL_DEFAULT==3. Special: value 0 means default, which is controlled by
    ZSTD_CLEVEL_DEFAULT. Note 1 : it's possible to pass a negative compression
    level. Note 2 : setting a level does not automatically set all other compression
    parameters to default. Setting this will however eventually dynamically impact
    the compression parameters which have not been manually set. The manually set
    ones will 'stick'.
    """
    windowLog = 101
    """
    Maximum allowed back-reference distance, expressed as power of 2. This will set
    a memory budget for streaming decompression, with larger values requiring more
    memory and typically compressing more. Must be clamped between
    ZSTD_WINDOWLOG_MIN and ZSTD_WINDOWLOG_MAX. Special: value 0 means "use default
    windowLog". Note: Using a windowLog greater than ZSTD_WINDOWLOG_LIMIT_DEFAULT
    requires explicitly allowing such size at streaming decompression stage.
    """
    hashLog = 102
    """
    Size of the initial probe table, as a power of 2. Resulting memory usage is (1
    << (hashLog+2)). Must be clamped between ZSTD_HASHLOG_MIN and ZSTD_HASHLOG_MAX.
    Larger tables improve compression ratio of strategies <= dFast, and improve
    speed of strategies > dFast. Special: value 0 means "use default hashLog".
    """
    chainLog = 103
    """
    Size of the multi-probe search table, as a power of 2. Resulting memory usage is
    (1 << (chainLog+2)). Must be clamped between ZSTD_CHAINLOG_MIN and
    ZSTD_CHAINLOG_MAX. Larger tables result in better and slower compression. This
    parameter is useless for "fast" strategy. It's still useful when using "dfast"
    strategy, in which case it defines a secondary probe table. Special: value 0
    means "use default chainLog".
    """
    searchLog = 104
    """
    Number of search attempts, as a power of 2. More attempts result in better and
    slower compression. This parameter is useless for "fast" and "dFast" strategies.
    Special: value 0 means "use default searchLog".
    """
    minMatch = 105
    """
    Minimum size of searched matches. Note that Zstandard can still find matches of
    smaller size, it just tweaks its search algorithm to look for this size and
    larger. Larger values increase compression and decompression speed, but decrease
    ratio. Must be clamped between ZSTD_MINMATCH_MIN and ZSTD_MINMATCH_MAX. Note
    that currently, for all strategies < btopt, effective minimum is 4. , for all
    strategies > fast, effective maximum is 6. Special: value 0 means "use default
    minMatchLength".
    """
    targetLength = 106
    """
    Impact of this field depends on strategy. For strategies btopt, btultra &
    btultra2: Length of Match considered "good enough" to stop search. Larger values
    make compression stronger, and slower. For strategy fast: Distance between match
    sampling. Larger values make compression faster, and weaker. Special: value 0
    means "use default targetLength".
    """
    strategy = 107
    """
    See ZSTD_strategy enum definition. The higher the value of selected strategy,
    the more complex it is, resulting in stronger and slower compression. Special:
    value 0 means "use default strategy".
    """
    enableLongDistanceMatching = 160
    """
    Enable long distance matching. This parameter is designed to improve compression
    ratio for large inputs, by finding large matches at long distance. It increases
    memory usage and window size. Note: enabling this parameter increases default
    ZSTD_c_windowLog to 128 MB except when expressly set to a different value. Note:
    will be enabled by default if ZSTD_c_windowLog >= 128 MB and compression
    strategy >= ZSTD_btopt (== compression level 16+)
    """
    ldmHashLog = 161
    """
    Size of the table for long distance matching, as a power of 2. Larger values
    increase memory usage and compression ratio, but decrease compression speed.
    Must be clamped between ZSTD_HASHLOG_MIN and ZSTD_HASHLOG_MAX default: windowlog
    - 7. Special: value 0 means "automatically determine hashlog".
    """
    ldmMinMatch = 162
    """
    Minimum match size for long distance matcher. Larger/too small values usually
    decrease compression ratio. Must be clamped between ZSTD_LDM_MINMATCH_MIN and
    ZSTD_LDM_MINMATCH_MAX. Special: value 0 means "use default value" (default: 64).
    """
    ldmBucketSizeLog = 163
    """
    Log size of each bucket in the LDM hash table for collision resolution. Larger
    values improve collision resolution but decrease compression speed. The maximum
    value is ZSTD_LDM_BUCKETSIZELOG_MAX. Special: value 0 means "use default value"
    (default: 3).
    """
    ldmHashRateLog = 164
    """
    Frequency of inserting/looking up entries into the LDM hash table. Must be
    clamped between 0 and (ZSTD_WINDOWLOG_MAX - ZSTD_HASHLOG_MIN). Default is MAX(0,
    (windowLog - ldmHashLog)), optimizing hash table usage. Larger values improve
    compression speed. Deviating far from default value will likely result in a
    compression ratio decrease. Special: value 0 means "automatically determine
    hashRateLog".
    """
    contentSizeFlag = 200
    """
    Content size will be written into frame header _whenever known_ (default:1)
    Content size must be known at the beginning of compression. This is
    automatically the case when using ZSTD_compress2(), For streaming scenarios,
    content size must be provided with ZSTD_CCtx_setPledgedSrcSize()
    """
    checksumFlag = 201
    """
    A 32-bits checksum of content is written at end of frame (default:0)
    """
    dictIDFlag = 202
    """
    When applicable, dictionary's ID is written into frame header (default:1)
    """
    nbWorkers = 400
    """
    Select how many threads will be spawned to compress in parallel. When nbWorkers
    >= 1, triggers asynchronous mode when invoking ZSTD_compressStream*() :
    ZSTD_compressStream*() consumes input and flush output if possible, but
    immediately gives back control to caller, while compression is performed in
    parallel, within worker thread(s). (note : a strong exception to this rule is
    when first invocation of ZSTD_compressStream2() sets ZSTD_e_end : in which case,
    ZSTD_compressStream2() delegates to ZSTD_compress2(), which is always a blocking
    call). More workers improve speed, but also increase memory usage. Default value
    is `0`, aka "single-threaded mode" : no worker is spawned, compression is
    performed inside Caller's thread, and all invocations are blocking
    """
    jobSize = 401
    """
    Size of a compression job. This value is enforced only when nbWorkers >= 1. Each
    compression job is completed in parallel, so this value can indirectly impact
    the nb of active threads. 0 means default, which is dynamically determined based
    on compression parameters. Job size must be a minimum of overlap size, or
    ZSTDMT_JOBSIZE_MIN (= 512 KB), whichever is largest. The minimum size is
    automatically and transparently enforced.
    """
    overlapLog = 402
    """
    Control the overlap size, as a fraction of window size. The overlap size is an
    amount of data reloaded from previous job at the beginning of a new job. It
    helps preserve compression ratio, while each job is compressed in parallel. This
    value is enforced only when nbWorkers >= 1. Larger values increase compression
    ratio, but decrease speed. Possible values range from 0 to 9 : - 0 means
    "default" : value will be determined by the library, depending on strategy - 1
    means "no overlap" - 9 means "full overlap", using a full window size. Each
    intermediate rank increases/decreases load size by a factor 2 : 9: full window;
    8: w/2; 7: w/4; 6: w/8; 5:w/16; 4: w/32; 3:w/64; 2:w/128; 1:no overlap;
    0:default default value varies between 6 and 9, depending on strategy
    """
    rsyncable = 500
    """
    Enables rsyncable mode, which makes compressed files more rsync friendly by
    adding periodic synchronization points to the compressed data. The target
    average block size is ZSTD_c_jobSize / 2. It's possible to modify the job size
    to increase or decrease the granularity of the synchronization point. Once the
    jobSize is smaller than the window size, it will result in compression ratio
    degradation. NOTE 1: rsyncable mode only works when multithreading is enabled.
    NOTE 2: rsyncable performs poorly in combination with long range mode, since it
    will decrease the effectiveness of synchronization points, though mileage may
    vary. NOTE 3: Rsyncable mode limits maximum compression speed to ~400 MB/s. If
    the selected compression level is already running significantly slower, the
    overall speed won't be significantly impacted.
    """
    format = 10
    """
    Select a compression format. The value must be of type ZSTD_format_e. See
    ZSTD_format_e enum definition for details
    """
    forceMaxWindow = 1000
    """
    Force back-reference distances to remain < windowSize, even when referencing
    into Dictionary content (default:0)
    """
    forceAttachDict = 1001
    """
    Controls whether the contents of a CDict are used in place, or copied into the
    working context. Accepts values from the ZSTD_dictAttachPref_e enum. See the
    comments on that enum for an explanation of the feature.
    """
    literalCompressionMode = 1002
    """
    Controlled with ZSTD_paramSwitch_e enum. Default is ZSTD_ps_auto. Set to
    ZSTD_ps_disable to never compress literals. Set to ZSTD_ps_enable to always
    compress literals. (Note: uncompressed literals may still be emitted if huffman
    is not beneficial to use.)
    """
    targetCBlockSize = 1003
    """
    Tries to fit compressed block size to be around targetCBlockSize. No target when
    targetCBlockSize == 0. There is no guarantee on compressed block size
    (default:0)
    """
    srcSizeHint = 1004
    """
    User's best guess of source size. Hint is not valid when srcSizeHint == 0. There
    is no guarantee that hint is close to actual source size, but compression ratio
    may regress significantly if guess considerably underestimates
    """
    enableDedicatedDictSearch = 1005
    """
    Controls whether the new and experimental "dedicated dictionary search
    structure" can be used. This feature is still rough around the edges, be
    prepared for surprising behavior!
    """
    stableInBuffer = 1006
    """
    Default is 0 == disabled. Set to 1 to enable.
    """
    stableOutBuffer = 1007
    """
    Default is 0 == disabled. Set to 1 to enable.
    """
    blockDelimiters = 1008
    """
    Default is 0 == ZSTD_sf_noBlockDelimiters.
    """
    validateSequences = 1009
    """
    Default is 0 == disabled. Set to 1 to enable sequence validation.
    """
    useBlockSplitter = 1010
    """
    Controlled with ZSTD_paramSwitch_e enum. Default is ZSTD_ps_auto. Set to
    ZSTD_ps_disable to never use block splitter. Set to ZSTD_ps_enable to always use
    block splitter.
    """
    useRowMatchFinder = 1011
    """
    Controlled with ZSTD_paramSwitch_e enum. Default is ZSTD_ps_auto. Set to
    ZSTD_ps_disable to never use row-based matchfinder. Set to ZSTD_ps_enable to
    force usage of row-based matchfinder.
    """
    deterministicRefPrefix = 1012
    """
    Default is 0 == disabled. Set to 1 to enable.
    """
    prefetchCDictTables = 1013
    """
    Controlled with ZSTD_paramSwitch_e enum. Default is ZSTD_ps_auto.
    """
    enableSeqProducerFallback = 1014
    """
    Allowed values are 0 (disable) and 1 (enable). The default setting is 0.
    """
    maxBlockSize = 1015
    """
    Allowed values are between 1KB and ZSTD_BLOCKSIZE_MAX (128KB). The default is
    ZSTD_BLOCKSIZE_MAX, and setting to 0 will set to the default.
    """
    searchForExternalRepcodes = 1016
    """
    This parameter affects how zstd parses external sequences, such as sequences
    provided through the compressSequences() API or from an external block-level
    sequence producer.
    """


# noinspection PyPep8Naming
class ZSTD_ResetDirective(_Enum):
    session_only = 1
    parameters = 2
    session_and_parameters = 3


# noinspection PyPep8Naming
class ZSTD_dParameter(_Enum):
    """
    The advanced API pushes parameters one by one into an existing DCtx context.
    Parameters are sticky, and remain valid for all following frames using the same
    DCtx context. It's possible to reset parameters to default values using
    ZSTD_DCtx_reset(). Note : This API is compatible with existing
    ZSTD_decompressDCtx() and ZSTD_decompressStream(). Therefore, no new
    decompression function is necessary.
    """
    windowLogMax = 100
    """
    Select a size limit (in power of 2) beyond which the streaming API will refuse
    to allocate memory buffer in order to protect the host from unreasonable memory
    requirements. This parameter is only useful in streaming mode, since no internal
    buffer is allocated in single-pass mode. By default, a decompression context
    accepts window sizes <= (1 << ZSTD_WINDOWLOG_LIMIT_DEFAULT). Special: value 0
    means "use default maximum windowLog".
    """
    format = 1000
    """
    allowing selection between ZSTD_format_e input compression formats
    """
    stableOutBuffer = 1001
    """
    Default is 0 == disabled. Set to 1 to enable.
    """
    forceIgnoreChecksum = 1002
    """
    Default is 0 == disabled. Set to 1 to enable
    """
    refMultipleDDicts = 1003
    """
    Default is 0 == disabled. Set to 1 to enable
    """
    disableHuffmanAssembly = 1004
    """
    Set to 1 to disable the Huffman assembly implementation. The default value is 0,
    which allows zstd to use the Huffman assembly implementation if available.
    """
    maxBlockSize = 1005
    """
    Allowed values are between 1KB and ZSTD_BLOCKSIZE_MAX (128KB). The default is
    ZSTD_BLOCKSIZE_MAX, and setting to 0 will set to the default.
    """


# noinspection PyPep8Naming
class ZSTD_EndDirective(_Enum):
    """
    ===== Streaming compression functions =====
    """
    continue_ = 0
    """
    collect more data, encoder decides when to output compressed result, for optimal
    compression ratio
    """
    flush = 1
    """
    flush any data provided so far, it creates (at least) one new block, that can be
    decoded immediately on reception; frame will continue: any future data can still
    reference previously compressed data, improving compression. note :
    multithreaded compression will block to flush as much output as possible.
    """
    end = 2
    """
    flush any remaining data _and_ close current frame. note that frame is only
    closed after compressed data is fully flushed (return value == 0). After that
    point, any additional data starts a new frame. note : each frame is independent
    (does not reference any content from previous frame). : note : multithreaded
    compression will block to flush as much output as possible.
    """


# noinspection PyPep8Naming
class ZSTD_dictContentType_e(_Enum):
    auto = 0
    """
    dictionary is "full" when starting with ZSTD_MAGIC_DICTIONARY, otherwise it is
    "rawContent"
    """
    rawContent = 1
    """
    ensures dictionary is always loaded as rawContent, even if it starts with
    ZSTD_MAGIC_DICTIONARY
    """
    fullDict = 2
    """
    refuses to load a dictionary if it does not respect Zstandard's specification,
    starting with ZSTD_MAGIC_DICTIONARY
    """


# noinspection PyPep8Naming
class ZSTD_dictLoadMethod_e(_Enum):
    byCopy = 0
    """
    Copy dictionary content internally
    """
    byRef = 1
    """
    Reference dictionary content -- the dictionary buffer must outlive its users.
    """


# noinspection PyPep8Naming
class ZSTD_format_e(_Enum):
    zstd1 = 0
    """
    zstd frame format, specified in zstd_compression_format.md (default)
    """
    zstd1_magicless = 1
    """
    Variant of zstd frame format, without initial 4-bytes magic number. Useful to
    save 4 bytes per generated frame. Decoder cannot recognise automatically this
    format, requiring this instruction.
    """


# noinspection PyPep8Naming
class ZSTD_forceIgnoreChecksum_e(_Enum):
    """
    Note: this enum controls ZSTD_d_forceIgnoreChecksum
    """
    validateChecksum = 0
    """
    Note: this enum controls ZSTD_d_forceIgnoreChecksum
    """
    ignoreChecksum = 1
    """
    Note: this enum controls ZSTD_d_forceIgnoreChecksum
    """


# noinspection PyPep8Naming
class ZSTD_refMultipleDDicts_e(_Enum):
    """
    Note: this enum controls ZSTD_d_refMultipleDDicts
    """
    refSingleDDict = 0
    """
    Note: this enum controls ZSTD_d_refMultipleDDicts
    """
    refMultipleDDicts = 1
    """
    Note: this enum controls ZSTD_d_refMultipleDDicts
    """


# noinspection PyPep8Naming
class ZSTD_dictAttachPref_e(_Enum):
    """
    Note: this enum and the behavior it controls are effectively internal
    implementation details of the compressor. They are expected to continue to
    evolve and should be considered only in the context of extremely advanced
    performance tuning.
    """
    dictDefaultAttach = 0
    """
    Use the default heuristic.
    """
    dictForceAttach = 1
    """
    Never copy the dictionary.
    """
    dictForceCopy = 2
    """
    Always copy the dictionary.
    """
    dictForceLoad = 3
    """
    Always reload the dictionary
    """


# noinspection PyPep8Naming
class ZSTD_literalCompressionMode_e(_Enum):
    auto = 0
    """
    Automatically determine the compression mode based on the compression level.
    Negative compression levels will be uncompressed, and positive compression
    levels will be compressed.
    """
    huffman = 1
    """
    Always attempt Huffman compression. Uncompressed literals will still be emitted
    if Huffman compression is not profitable.
    """
    uncompressed = 2
    """
    Always emit uncompressed literals.
    """


# noinspection PyPep8Naming
class ZSTD_paramSwitch_e(_Enum):
    """
    Note: This enum controls features which are conditionally beneficial. Zstd
    typically will make a final decision on whether or not to enable the feature
    (ZSTD_ps_auto), but setting the switch to ZSTD_ps_enable or ZSTD_ps_disable
    allow for a force enable/disable the feature.
    """
    auto = 0
    """
    Let the library automatically determine whether the feature shall be enabled
    """
    enable = 1
    """
    Force-enable the feature
    """
    disable = 2
    """
    Do not use the feature
    """


# noinspection PyPep8Naming
class ZSTD_frameType_e(_Enum):
    frame = 0
    skippableFrame = 1


# noinspection PyPep8Naming
class ZSTD_sequenceFormat_e(_Enum):
    noBlockDelimiters = 0
    """
    Representation of ZSTD_Sequence has no block delimiters, sequences only
    """
    explicitBlockDelimiters = 1
    """
    Representation of ZSTD_Sequence contains explicit block delimiters
    """


# noinspection PyPep8Naming
class ZSTD_nextInputType_e(_Enum):
    frameHeader = 0
    blockHeader = 1
    block = 2
    lastBlock = 3
    checksum = 4
    skippableFrame = 5

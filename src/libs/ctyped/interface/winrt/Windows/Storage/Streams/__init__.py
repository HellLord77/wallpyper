from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IBuffer(_inspectable.IInspectable):
    get_Capacity: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    put_Length: _Callable[[_type.UINT32],  # value
                          _type.HRESULT]


class IBufferFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # capacity
                       _Pointer[IBuffer]],  # value
                      _type.HRESULT]

    _factory = True


class IBufferStatics(_inspectable.IInspectable):
    CreateCopyFromMemoryBuffer: _Callable[[_Windows_Foundation.IMemoryBuffer,  # input
                                           _Pointer[IBuffer]],  # value
                                          _type.HRESULT]
    CreateMemoryBufferOverIBuffer: _Callable[[IBuffer,  # input
                                              _Pointer[_Windows_Foundation.IMemoryBuffer]],  # value
                                             _type.HRESULT]

    _factory = True


class IContentTypeProvider(_inspectable.IInspectable):
    get_ContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IDataReader(_inspectable.IInspectable):
    get_UnconsumedBufferLength: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    get_UnicodeEncoding: _Callable[[_Pointer[_enum.Windows.Storage.Streams.UnicodeEncoding]],  # value
                                   _type.HRESULT]
    put_UnicodeEncoding: _Callable[[_enum.Windows.Storage.Streams.UnicodeEncoding],  # value
                                   _type.HRESULT]
    get_ByteOrder: _Callable[[_Pointer[_enum.Windows.Storage.Streams.ByteOrder]],  # value
                             _type.HRESULT]
    put_ByteOrder: _Callable[[_enum.Windows.Storage.Streams.ByteOrder],  # value
                             _type.HRESULT]
    get_InputStreamOptions: _Callable[[_Pointer[_enum.Windows.Storage.Streams.InputStreamOptions]],  # value
                                      _type.HRESULT]
    put_InputStreamOptions: _Callable[[_enum.Windows.Storage.Streams.InputStreamOptions],  # value
                                      _type.HRESULT]
    ReadByte: _Callable[[_Pointer[_type.BYTE]],  # value
                        _type.HRESULT]
    ReadBytes: _Callable[[_type.UINT32,  # __valueSize
                          _Pointer[_type.BYTE]],  # value
                         _type.HRESULT]
    ReadBuffer: _Callable[[_type.UINT32,  # length
                           _Pointer[IBuffer]],  # buffer
                          _type.HRESULT]
    ReadBoolean: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    ReadGuid: _Callable[[_Pointer[_struct.GUID]],  # value
                        _type.HRESULT]
    ReadInt16: _Callable[[_Pointer[_type.INT16]],  # value
                         _type.HRESULT]
    ReadInt32: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    ReadInt64: _Callable[[_Pointer[_type.INT64]],  # value
                         _type.HRESULT]
    ReadUInt16: _Callable[[_Pointer[_type.UINT16]],  # value
                          _type.HRESULT]
    ReadUInt32: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    ReadUInt64: _Callable[[_Pointer[_type.UINT64]],  # value
                          _type.HRESULT]
    ReadSingle: _Callable[[_Pointer[_type.FLOAT]],  # value
                          _type.HRESULT]
    ReadDouble: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    ReadString: _Callable[[_type.UINT32,  # codeUnitCount
                           _Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    ReadDateTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    ReadTimeSpan: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    LoadAsync: _Callable[[_type.UINT32,  # count
                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                         _type.HRESULT]
    DetachBuffer: _Callable[[_Pointer[IBuffer]],  # buffer
                            _type.HRESULT]
    DetachStream: _Callable[[_Pointer[IInputStream]],  # stream
                            _type.HRESULT]


class IDataReaderFactory(_inspectable.IInspectable):
    CreateDataReader: _Callable[[IInputStream,  # inputStream
                                 _Pointer[IDataReader]],  # dataReader
                                _type.HRESULT]

    _factory = True


class IDataReaderStatics(_inspectable.IInspectable):
    FromBuffer: _Callable[[IBuffer,  # buffer
                           _Pointer[IDataReader]],  # dataReader
                          _type.HRESULT]

    _factory = True


class IDataWriter(_inspectable.IInspectable):
    get_UnstoredBufferLength: _Callable[[_Pointer[_type.UINT32]],  # value
                                        _type.HRESULT]
    get_UnicodeEncoding: _Callable[[_Pointer[_enum.Windows.Storage.Streams.UnicodeEncoding]],  # value
                                   _type.HRESULT]
    put_UnicodeEncoding: _Callable[[_enum.Windows.Storage.Streams.UnicodeEncoding],  # value
                                   _type.HRESULT]
    get_ByteOrder: _Callable[[_Pointer[_enum.Windows.Storage.Streams.ByteOrder]],  # value
                             _type.HRESULT]
    put_ByteOrder: _Callable[[_enum.Windows.Storage.Streams.ByteOrder],  # value
                             _type.HRESULT]
    WriteByte: _Callable[[_type.BYTE],  # value
                         _type.HRESULT]
    WriteBytes: _Callable[[_type.UINT32,  # __valueSize
                           _Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    WriteBuffer: _Callable[[IBuffer],  # buffer
                           _type.HRESULT]
    WriteBufferRange: _Callable[[IBuffer,  # buffer
                                 _type.UINT32,  # start
                                 _type.UINT32],  # count
                                _type.HRESULT]
    WriteBoolean: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    WriteGuid: _Callable[[_struct.GUID],  # value
                         _type.HRESULT]
    WriteInt16: _Callable[[_type.INT16],  # value
                          _type.HRESULT]
    WriteInt32: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    WriteInt64: _Callable[[_type.INT64],  # value
                          _type.HRESULT]
    WriteUInt16: _Callable[[_type.UINT16],  # value
                           _type.HRESULT]
    WriteUInt32: _Callable[[_type.UINT32],  # value
                           _type.HRESULT]
    WriteUInt64: _Callable[[_type.UINT64],  # value
                           _type.HRESULT]
    WriteSingle: _Callable[[_type.FLOAT],  # value
                           _type.HRESULT]
    WriteDouble: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    WriteDateTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                             _type.HRESULT]
    WriteTimeSpan: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                             _type.HRESULT]
    WriteString: _Callable[[_type.HSTRING,  # value
                            _Pointer[_type.UINT32]],  # codeUnitCount
                           _type.HRESULT]
    MeasureString: _Callable[[_type.HSTRING,  # value
                              _Pointer[_type.UINT32]],  # codeUnitCount
                             _type.HRESULT]
    StoreAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                          _type.HRESULT]
    FlushAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                          _type.HRESULT]
    DetachBuffer: _Callable[[_Pointer[IBuffer]],  # buffer
                            _type.HRESULT]
    DetachStream: _Callable[[_Pointer[IOutputStream]],  # outputStream
                            _type.HRESULT]


class IDataWriterFactory(_inspectable.IInspectable):
    CreateDataWriter: _Callable[[IOutputStream,  # outputStream
                                 _Pointer[IDataWriter]],  # dataWriter
                                _type.HRESULT]

    _factory = True


class IFileRandomAccessStreamStatics(_inspectable.IInspectable):
    OpenAsync: _Callable[[_type.HSTRING,  # filePath
                          _enum.Windows.Storage.FileAccessMode,  # accessMode
                          _Pointer[_Windows_Foundation.IAsyncOperation[IRandomAccessStream]]],  # operation
                         _type.HRESULT]
    OpenWithOptionsAsync: _Callable[[_type.HSTRING,  # filePath
                                     _enum.Windows.Storage.FileAccessMode,  # accessMode
                                     _enum.Windows.Storage.StorageOpenOptions,  # sharingOptions
                                     _enum.Windows.Storage.Streams.FileOpenDisposition,  # openDisposition
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IRandomAccessStream]]],  # operation
                                    _type.HRESULT]
    OpenTransactedWriteAsync: _Callable[[_type.HSTRING,  # filePath
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageStreamTransaction]]],  # operation
                                        _type.HRESULT]
    OpenTransactedWriteWithOptionsAsync: _Callable[[_type.HSTRING,  # filePath
                                                    _enum.Windows.Storage.StorageOpenOptions,  # openOptions
                                                    _enum.Windows.Storage.Streams.FileOpenDisposition,  # openDisposition
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageStreamTransaction]]],  # operation
                                                   _type.HRESULT]
    OpenForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                 _type.HSTRING,  # filePath
                                 _enum.Windows.Storage.FileAccessMode,  # accessMode
                                 _Pointer[_Windows_Foundation.IAsyncOperation[IRandomAccessStream]]],  # operation
                                _type.HRESULT]
    OpenForUserWithOptionsAsync: _Callable[[_Windows_System.IUser,  # user
                                            _type.HSTRING,  # filePath
                                            _enum.Windows.Storage.FileAccessMode,  # accessMode
                                            _enum.Windows.Storage.StorageOpenOptions,  # sharingOptions
                                            _enum.Windows.Storage.Streams.FileOpenDisposition,  # openDisposition
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IRandomAccessStream]]],  # operation
                                           _type.HRESULT]
    OpenTransactedWriteForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                _type.HSTRING,  # filePath
                                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageStreamTransaction]]],  # operation
                                               _type.HRESULT]
    OpenTransactedWriteForUserWithOptionsAsync: _Callable[[_Windows_System.IUser,  # user
                                                           _type.HSTRING,  # filePath
                                                           _enum.Windows.Storage.StorageOpenOptions,  # openOptions
                                                           _enum.Windows.Storage.Streams.FileOpenDisposition,  # openDisposition
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageStreamTransaction]]],  # operation
                                                          _type.HRESULT]

    _factory = True


class IInputStream(_inspectable.IInspectable):
    ReadAsync: _Callable[[IBuffer,  # buffer
                          _type.UINT32,  # count
                          _enum.Windows.Storage.Streams.InputStreamOptions,  # options
                          _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IBuffer, _type.UINT32]]],  # operation
                         _type.HRESULT]


class IInputStreamReference(_inspectable.IInspectable):
    OpenSequentialReadAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IInputStream]]],  # operation
                                       _type.HRESULT]


class IOutputStream(_inspectable.IInspectable):
    WriteAsync: _Callable[[IBuffer,  # buffer
                           _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.UINT32, _type.UINT32]]],  # operation
                          _type.HRESULT]
    FlushAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                          _type.HRESULT]


class IPropertySetSerializer(_inspectable.IInspectable):
    Serialize: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # propertySet
                          _Pointer[IBuffer]],  # result
                         _type.HRESULT]
    Deserialize: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # propertySet
                            IBuffer],  # buffer
                           _type.HRESULT]


class IRandomAccessStream(_inspectable.IInspectable):
    get_Size: _Callable[[_Pointer[_type.UINT64]],  # value
                        _type.HRESULT]
    put_Size: _Callable[[_type.UINT64],  # value
                        _type.HRESULT]
    GetInputStreamAt: _Callable[[_type.UINT64,  # position
                                 _Pointer[IInputStream]],  # stream
                                _type.HRESULT]
    GetOutputStreamAt: _Callable[[_type.UINT64,  # position
                                  _Pointer[IOutputStream]],  # stream
                                 _type.HRESULT]
    get_Position: _Callable[[_Pointer[_type.UINT64]],  # value
                            _type.HRESULT]
    Seek: _Callable[[_type.UINT64],  # position
                    _type.HRESULT]
    CloneStream: _Callable[[_Pointer[IRandomAccessStream]],  # stream
                           _type.HRESULT]
    get_CanRead: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_CanWrite: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]


class IRandomAccessStreamReference(_inspectable.IInspectable):
    OpenReadAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IRandomAccessStreamWithContentType]]],  # operation
                             _type.HRESULT]


class IRandomAccessStreamReferenceStatics(_inspectable.IInspectable):
    CreateFromFile: _Callable[[_Windows_Storage.IStorageFile,  # file
                               _Pointer[IRandomAccessStreamReference]],  # streamReference
                              _type.HRESULT]
    CreateFromUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                              _Pointer[IRandomAccessStreamReference]],  # streamReference
                             _type.HRESULT]
    CreateFromStream: _Callable[[IRandomAccessStream,  # stream
                                 _Pointer[IRandomAccessStreamReference]],  # streamReference
                                _type.HRESULT]

    _factory = True


class IRandomAccessStreamStatics(_inspectable.IInspectable):
    CopyAsync: _Callable[[IInputStream,  # source
                          IOutputStream,  # destination
                          _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.UINT64, _type.UINT64]]],  # operation
                         _type.HRESULT]
    CopySizeAsync: _Callable[[IInputStream,  # source
                              IOutputStream,  # destination
                              _type.UINT64,  # bytesToCopy
                              _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.UINT64, _type.UINT64]]],  # operation
                             _type.HRESULT]
    CopyAndCloseAsync: _Callable[[IInputStream,  # source
                                  IOutputStream,  # destination
                                  _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.UINT64, _type.UINT64]]],  # operation
                                 _type.HRESULT]

    _factory = True


class IRandomAccessStreamWithContentType(_inspectable.IInspectable):
    pass

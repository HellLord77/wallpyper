from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IDirectDraw(_Unknwnbase.IUnknown):
    Compact: _Callable[[],
                       _type.HRESULT]
    CreateClipper: _Callable[[_type.DWORD,
                              _Pointer[IDirectDrawClipper],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    CreatePalette: _Callable[[_type.DWORD,
                              _Pointer[_struct.PALETTEENTRY],
                              _Pointer[IDirectDrawPalette],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    CreateSurface: _Callable[[_Pointer[_struct.DDSURFACEDESC],
                              _Pointer[IDirectDrawSurface],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    DuplicateSurface: _Callable[[IDirectDrawSurface,
                                 _Pointer[IDirectDrawSurface]],
                                _type.HRESULT]
    EnumDisplayModes: _Callable
    EnumSurfaces: _Callable
    FlipToGDISurface: _Callable[[],
                                _type.HRESULT]
    GetCaps: _Callable
    GetDisplayMode: _Callable[[_Pointer[_struct.DDSURFACEDESC]],
                              _type.HRESULT]
    GetFourCCCodes: _Callable[[_Pointer[_type.DWORD],
                               _Pointer[_type.DWORD]],
                              _type.HRESULT]
    GetGDISurface: _Callable[[_Pointer[IDirectDrawSurface]],
                             _type.HRESULT]
    GetMonitorFrequency: _Callable[[_Pointer[_type.DWORD]],
                                   _type.HRESULT]
    GetScanLine: _Callable[[_Pointer[_type.DWORD]],
                           _type.HRESULT]
    GetVerticalBlankStatus: _Callable[[_Pointer[_type.BOOL]],
                                      _type.HRESULT]
    Initialize: _Callable[[_Pointer[_struct.GUID]],
                          _type.HRESULT]
    RestoreDisplayMode: _Callable[[],
                                  _type.HRESULT]
    SetCooperativeLevel: _Callable[[_type.HWND,
                                    _type.DWORD],
                                   _type.HRESULT]
    SetDisplayMode: _Callable[[_type.DWORD,
                               _type.DWORD,
                               _type.DWORD],
                              _type.HRESULT]
    WaitForVerticalBlank: _Callable[[_type.DWORD,
                                     _type.HANDLE],
                                    _type.HRESULT]


class IDirectDraw2(_Unknwnbase.IUnknown):
    Compact: _Callable[[],
                       _type.HRESULT]
    CreateClipper: _Callable[[_type.DWORD,
                              _Pointer[IDirectDrawClipper],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    CreatePalette: _Callable[[_type.DWORD,
                              _Pointer[_struct.PALETTEENTRY],
                              _Pointer[IDirectDrawPalette],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    CreateSurface: _Callable[[_Pointer[_struct.DDSURFACEDESC],
                              _Pointer[IDirectDrawSurface],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    DuplicateSurface: _Callable[[IDirectDrawSurface,
                                 _Pointer[IDirectDrawSurface]],
                                _type.HRESULT]
    EnumDisplayModes: _Callable
    EnumSurfaces: _Callable
    FlipToGDISurface: _Callable[[],
                                _type.HRESULT]
    GetCaps: _Callable
    GetDisplayMode: _Callable[[_Pointer[_struct.DDSURFACEDESC]],
                              _type.HRESULT]
    GetFourCCCodes: _Callable[[_Pointer[_type.DWORD],
                               _Pointer[_type.DWORD]],
                              _type.HRESULT]
    GetGDISurface: _Callable[[_Pointer[IDirectDrawSurface]],
                             _type.HRESULT]
    GetMonitorFrequency: _Callable[[_Pointer[_type.DWORD]],
                                   _type.HRESULT]
    GetScanLine: _Callable[[_Pointer[_type.DWORD]],
                           _type.HRESULT]
    GetVerticalBlankStatus: _Callable[[_Pointer[_type.BOOL]],
                                      _type.HRESULT]
    Initialize: _Callable[[_Pointer[_struct.GUID]],
                          _type.HRESULT]
    RestoreDisplayMode: _Callable[[],
                                  _type.HRESULT]
    SetCooperativeLevel: _Callable[[_type.HWND,
                                    _type.DWORD],
                                   _type.HRESULT]
    SetDisplayMode: _Callable[[_type.DWORD,
                               _type.DWORD,
                               _type.DWORD,
                               _type.DWORD,
                               _type.DWORD],
                              _type.HRESULT]
    WaitForVerticalBlank: _Callable[[_type.DWORD,
                                     _type.HANDLE],
                                    _type.HRESULT]
    GetAvailableVidMem: _Callable[[_Pointer[_struct.DDSCAPS],
                                   _Pointer[_type.DWORD],
                                   _Pointer[_type.DWORD]],
                                  _type.HRESULT]


class IDirectDraw4(_Unknwnbase.IUnknown):
    Compact: _Callable[[],
                       _type.HRESULT]
    CreateClipper: _Callable[[_type.DWORD,
                              _Pointer[IDirectDrawClipper],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    CreatePalette: _Callable[[_type.DWORD,
                              _Pointer[_struct.PALETTEENTRY],
                              _Pointer[IDirectDrawPalette],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    CreateSurface: _Callable[[_Pointer[_struct.DDSURFACEDESC2],
                              _Pointer[IDirectDrawSurface4],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    DuplicateSurface: _Callable[[IDirectDrawSurface4,
                                 _Pointer[IDirectDrawSurface4]],
                                _type.HRESULT]
    EnumDisplayModes: _Callable
    EnumSurfaces: _Callable
    FlipToGDISurface: _Callable[[],
                                _type.HRESULT]
    GetCaps: _Callable
    GetDisplayMode: _Callable[[_Pointer[_struct.DDSURFACEDESC2]],
                              _type.HRESULT]
    GetFourCCCodes: _Callable[[_Pointer[_type.DWORD],
                               _Pointer[_type.DWORD]],
                              _type.HRESULT]
    GetGDISurface: _Callable[[_Pointer[IDirectDrawSurface4]],
                             _type.HRESULT]
    GetMonitorFrequency: _Callable[[_Pointer[_type.DWORD]],
                                   _type.HRESULT]
    GetScanLine: _Callable[[_Pointer[_type.DWORD]],
                           _type.HRESULT]
    GetVerticalBlankStatus: _Callable[[_Pointer[_type.BOOL]],
                                      _type.HRESULT]
    Initialize: _Callable[[_Pointer[_struct.GUID]],
                          _type.HRESULT]
    RestoreDisplayMode: _Callable[[],
                                  _type.HRESULT]
    SetCooperativeLevel: _Callable[[_type.HWND,
                                    _type.DWORD],
                                   _type.HRESULT]
    SetDisplayMode: _Callable[[_type.DWORD,
                               _type.DWORD,
                               _type.DWORD,
                               _type.DWORD,
                               _type.DWORD],
                              _type.HRESULT]
    WaitForVerticalBlank: _Callable[[_type.DWORD,
                                     _type.HANDLE],
                                    _type.HRESULT]
    GetAvailableVidMem: _Callable[[_Pointer[_struct.DDSCAPS],
                                   _Pointer[_type.DWORD],
                                   _Pointer[_type.DWORD]],
                                  _type.HRESULT]
    GetSurfaceFromDC: _Callable[[_type.HDC,
                                 _Pointer[IDirectDrawSurface4]],
                                _type.HRESULT]
    RestoreAllSurfaces: _Callable[[],
                                  _type.HRESULT]
    TestCooperativeLevel: _Callable[[],
                                    _type.HRESULT]
    GetDeviceIdentifier: _Callable[[_Pointer[_struct.DDDEVICEIDENTIFIER],
                                    _type.DWORD],
                                   _type.HRESULT]


class IDirectDraw7(_Unknwnbase.IUnknown):
    Compact: _Callable[[],
                       _type.HRESULT]
    CreateClipper: _Callable[[_type.DWORD,
                              _Pointer[IDirectDrawClipper],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    CreatePalette: _Callable[[_type.DWORD,
                              _Pointer[_struct.PALETTEENTRY],
                              _Pointer[IDirectDrawPalette],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    CreateSurface: _Callable[[_Pointer[_struct.DDSURFACEDESC2],
                              _Pointer[IDirectDrawSurface7],
                              _Unknwnbase.IUnknown],
                             _type.HRESULT]
    DuplicateSurface: _Callable[[IDirectDrawSurface7,
                                 _Pointer[IDirectDrawSurface7]],
                                _type.HRESULT]
    EnumDisplayModes: _Callable
    EnumSurfaces: _Callable
    FlipToGDISurface: _Callable[[],
                                _type.HRESULT]
    GetCaps: _Callable
    GetDisplayMode: _Callable[[_Pointer[_struct.DDSURFACEDESC2]],
                              _type.HRESULT]
    GetFourCCCodes: _Callable[[_Pointer[_type.DWORD],
                               _Pointer[_type.DWORD]],
                              _type.HRESULT]
    GetGDISurface: _Callable[[_Pointer[IDirectDrawSurface7]],
                             _type.HRESULT]
    GetMonitorFrequency: _Callable[[_Pointer[_type.DWORD]],
                                   _type.HRESULT]
    GetScanLine: _Callable[[_Pointer[_type.DWORD]],
                           _type.HRESULT]
    GetVerticalBlankStatus: _Callable[[_Pointer[_type.BOOL]],
                                      _type.HRESULT]
    Initialize: _Callable[[_Pointer[_struct.GUID]],
                          _type.HRESULT]
    RestoreDisplayMode: _Callable[[],
                                  _type.HRESULT]
    SetCooperativeLevel: _Callable[[_type.HWND,
                                    _type.DWORD],
                                   _type.HRESULT]
    SetDisplayMode: _Callable[[_type.DWORD,
                               _type.DWORD,
                               _type.DWORD,
                               _type.DWORD,
                               _type.DWORD],
                              _type.HRESULT]
    WaitForVerticalBlank: _Callable[[_type.DWORD,
                                     _type.HANDLE],
                                    _type.HRESULT]
    GetAvailableVidMem: _Callable[[_Pointer[_struct.DDSCAPS],
                                   _Pointer[_type.DWORD],
                                   _Pointer[_type.DWORD]],
                                  _type.HRESULT]
    GetSurfaceFromDC: _Callable[[_type.HDC,
                                 _Pointer[IDirectDrawSurface7]],
                                _type.HRESULT]
    RestoreAllSurfaces: _Callable[[],
                                  _type.HRESULT]
    TestCooperativeLevel: _Callable[[],
                                    _type.HRESULT]
    GetDeviceIdentifier: _Callable[[_Pointer[_struct.DDDEVICEIDENTIFIER],
                                    _type.DWORD],
                                   _type.HRESULT]
    StartModeTest: _Callable[[_Pointer[_struct.SIZE],
                              _type.DWORD,
                              _type.DWORD],
                             _type.HRESULT]
    EvaluateMode: _Callable[[_type.DWORD,
                             _Pointer[_type.DWORD]],
                            _type.HRESULT]


class IDirectDrawPalette(_Unknwnbase.IUnknown):
    GetCaps: _Callable[[_Pointer[_type.DWORD]],
                       _type.HRESULT]
    GetEntries: _Callable[[_type.DWORD,
                           _type.DWORD,
                           _type.DWORD,
                           _Pointer[_struct.PALETTEENTRY]],
                          _type.HRESULT]
    Initialize: _Callable[[IDirectDraw,
                           _type.DWORD,
                           _Pointer[_struct.PALETTEENTRY]],
                          _type.HRESULT]
    SetEntries: _Callable[[_type.DWORD,
                           _type.DWORD,
                           _type.DWORD,
                           _Pointer[_struct.PALETTEENTRY]],
                          _type.HRESULT]


class IDirectDrawClipper(_Unknwnbase.IUnknown):
    GetClipList: _Callable[[_Pointer[_struct.RECT],
                            _Pointer[_struct.RGNDATA],
                            _Pointer[_type.DWORD]],
                           _type.HRESULT]
    GetHWnd: _Callable[[_Pointer[_type.HWND]],
                       _type.HRESULT]
    Initialize: _Callable[[IDirectDraw,
                           _type.DWORD],
                          _type.HRESULT]
    IsClipListChanged: _Callable[[_Pointer[_type.BOOL]],
                                 _type.HRESULT]
    SetClipList: _Callable[[_Pointer[_struct.RGNDATA],
                            _type.DWORD],
                           _type.HRESULT]
    SetHWnd: _Callable[[_type.DWORD,
                        _type.HWND],
                       _type.HRESULT]


class IDirectDrawSurface(_Unknwnbase.IUnknown):
    AddAttachedSurface: _Callable[[IDirectDrawSurface],
                                  _type.HRESULT]
    AddOverlayDirtyRect: _Callable[[_Pointer[_struct.RECT]],
                                   _type.HRESULT]
    Blt: _Callable[[_Pointer[_struct.RECT],
                    IDirectDrawSurface,
                    _Pointer[_struct.RECT],
                    _type.DWORD,
                    _Pointer[_struct.DDBLTFX]],
                   _type.HRESULT]
    BltBatch: _Callable[[_Pointer[_struct.DDBLTBATCH],
                         _type.DWORD,
                         _type.DWORD],
                        _type.HRESULT]
    BltFast: _Callable[[_type.DWORD,
                        _type.DWORD,
                        IDirectDrawSurface,
                        _Pointer[_struct.RECT],
                        _type.DWORD],
                       _type.HRESULT]
    DeleteAttachedSurface: _Callable[[_type.DWORD,
                                      IDirectDrawSurface],
                                     _type.HRESULT]
    EnumAttachedSurfaces: _Callable
    EnumOverlayZOrders: _Callable
    Flip: _Callable[[IDirectDrawSurface,
                     _type.DWORD],
                    _type.HRESULT]
    GetAttachedSurface: _Callable[[_Pointer[_struct.DDSCAPS],
                                   _Pointer[IDirectDrawSurface]],
                                  _type.HRESULT]
    GetBltStatus: _Callable[[_type.DWORD],
                            _type.HRESULT]
    GetCaps: _Callable[[_Pointer[_struct.DDSCAPS]],
                       _type.HRESULT]
    GetClipper: _Callable[[_Pointer[IDirectDrawClipper]],
                          _type.HRESULT]
    GetColorKey: _Callable[[_type.DWORD,
                            _Pointer[_struct.DDCOLORKEY]],
                           _type.HRESULT]
    GetDC: _Callable[[_Pointer[_type.HDC]],
                     _type.HRESULT]
    GetFlipStatus: _Callable[[_type.DWORD],
                             _type.HRESULT]
    GetOverlayPosition: _Callable[[_Pointer[_type.c_long],
                                   _Pointer[_type.c_long]],
                                  _type.HRESULT]
    GetPalette: _Callable[[_Pointer[IDirectDrawPalette]],
                          _type.HRESULT]
    GetPixelFormat: _Callable[[_Pointer[_struct.DDPIXELFORMAT]],
                              _type.HRESULT]
    GetSurfaceDesc: _Callable[[_Pointer[_struct.DDSURFACEDESC]],
                              _type.HRESULT]
    Initialize: _Callable[[IDirectDraw,
                           _Pointer[_struct.DDSURFACEDESC]],
                          _type.HRESULT]
    IsLost: _Callable[[],
                      _type.HRESULT]
    Lock: _Callable[[_Pointer[_struct.RECT],
                     _Pointer[_struct.DDSURFACEDESC],
                     _type.DWORD,
                     _type.HANDLE],
                    _type.HRESULT]
    ReleaseDC: _Callable[[_type.HDC],
                         _type.HRESULT]
    Restore: _Callable[[],
                       _type.HRESULT]
    SetClipper: _Callable[[IDirectDrawClipper],
                          _type.HRESULT]
    SetColorKey: _Callable[[_type.DWORD,
                            _Pointer[_struct.DDCOLORKEY]],
                           _type.HRESULT]
    SetOverlayPosition: _Callable[[_type.LONG,
                                   _type.LONG],
                                  _type.HRESULT]
    SetPalette: _Callable[[IDirectDrawPalette],
                          _type.HRESULT]
    Unlock: _Callable[[_type.LPVOID],
                      _type.HRESULT]
    UpdateOverlay: _Callable[[_Pointer[_struct.RECT],
                              IDirectDrawSurface,
                              _Pointer[_struct.RECT],
                              _type.DWORD,
                              _Pointer[_struct.DDOVERLAYFX]],
                             _type.HRESULT]
    UpdateOverlayDisplay: _Callable[[_type.DWORD],
                                    _type.HRESULT]
    UpdateOverlayZOrder: _Callable[[_type.DWORD,
                                    IDirectDrawSurface],
                                   _type.HRESULT]


class IDirectDrawSurface2(_Unknwnbase.IUnknown):
    AddAttachedSurface: _Callable[[IDirectDrawSurface2],
                                  _type.HRESULT]
    AddOverlayDirtyRect: _Callable[[_Pointer[_struct.RECT]],
                                   _type.HRESULT]
    Blt: _Callable[[_Pointer[_struct.RECT],
                    IDirectDrawSurface2,
                    _Pointer[_struct.RECT],
                    _type.DWORD,
                    _Pointer[_struct.DDBLTFX]],
                   _type.HRESULT]
    BltBatch: _Callable[[_Pointer[_struct.DDBLTBATCH],
                         _type.DWORD,
                         _type.DWORD],
                        _type.HRESULT]
    BltFast: _Callable[[_type.DWORD,
                        _type.DWORD,
                        IDirectDrawSurface2,
                        _Pointer[_struct.RECT],
                        _type.DWORD],
                       _type.HRESULT]
    DeleteAttachedSurface: _Callable[[_type.DWORD,
                                      IDirectDrawSurface2],
                                     _type.HRESULT]
    EnumAttachedSurfaces: _Callable
    EnumOverlayZOrders: _Callable
    Flip: _Callable[[IDirectDrawSurface2,
                     _type.DWORD],
                    _type.HRESULT]
    GetAttachedSurface: _Callable[[_Pointer[_struct.DDSCAPS],
                                   _Pointer[IDirectDrawSurface2]],
                                  _type.HRESULT]
    GetBltStatus: _Callable[[_type.DWORD],
                            _type.HRESULT]
    GetCaps: _Callable[[_Pointer[_struct.DDSCAPS]],
                       _type.HRESULT]
    GetClipper: _Callable[[_Pointer[IDirectDrawClipper]],
                          _type.HRESULT]
    GetColorKey: _Callable[[_type.DWORD,
                            _Pointer[_struct.DDCOLORKEY]],
                           _type.HRESULT]
    GetDC: _Callable[[_Pointer[_type.HDC]],
                     _type.HRESULT]
    GetFlipStatus: _Callable[[_type.DWORD],
                             _type.HRESULT]
    GetOverlayPosition: _Callable[[_Pointer[_type.c_long],
                                   _Pointer[_type.c_long]],
                                  _type.HRESULT]
    GetPalette: _Callable[[_Pointer[IDirectDrawPalette]],
                          _type.HRESULT]
    GetPixelFormat: _Callable[[_Pointer[_struct.DDPIXELFORMAT]],
                              _type.HRESULT]
    GetSurfaceDesc: _Callable[[_Pointer[_struct.DDSURFACEDESC]],
                              _type.HRESULT]
    Initialize: _Callable[[IDirectDraw,
                           _Pointer[_struct.DDSURFACEDESC]],
                          _type.HRESULT]
    IsLost: _Callable[[],
                      _type.HRESULT]
    Lock: _Callable[[_Pointer[_struct.RECT],
                     _Pointer[_struct.DDSURFACEDESC],
                     _type.DWORD,
                     _type.HANDLE],
                    _type.HRESULT]
    ReleaseDC: _Callable[[_type.HDC],
                         _type.HRESULT]
    Restore: _Callable[[],
                       _type.HRESULT]
    SetClipper: _Callable[[IDirectDrawClipper],
                          _type.HRESULT]
    SetColorKey: _Callable[[_type.DWORD,
                            _Pointer[_struct.DDCOLORKEY]],
                           _type.HRESULT]
    SetOverlayPosition: _Callable[[_type.LONG,
                                   _type.LONG],
                                  _type.HRESULT]
    SetPalette: _Callable[[IDirectDrawPalette],
                          _type.HRESULT]
    Unlock: _Callable[[_type.LPVOID],
                      _type.HRESULT]
    UpdateOverlay: _Callable[[_Pointer[_struct.RECT],
                              IDirectDrawSurface2,
                              _Pointer[_struct.RECT],
                              _type.DWORD,
                              _Pointer[_struct.DDOVERLAYFX]],
                             _type.HRESULT]
    UpdateOverlayDisplay: _Callable[[_type.DWORD],
                                    _type.HRESULT]
    UpdateOverlayZOrder: _Callable[[_type.DWORD,
                                    IDirectDrawSurface2],
                                   _type.HRESULT]
    GetDDInterface: _Callable[[_Pointer[_type.LPVOID]],
                              _type.HRESULT]
    PageLock: _Callable[[_type.DWORD],
                        _type.HRESULT]
    PageUnlock: _Callable[[_type.DWORD],
                          _type.HRESULT]


class IDirectDrawSurface3(_Unknwnbase.IUnknown):
    AddAttachedSurface: _Callable[[IDirectDrawSurface3],
                                  _type.HRESULT]
    AddOverlayDirtyRect: _Callable[[_Pointer[_struct.RECT]],
                                   _type.HRESULT]
    Blt: _Callable[[_Pointer[_struct.RECT],
                    IDirectDrawSurface3,
                    _Pointer[_struct.RECT],
                    _type.DWORD,
                    _Pointer[_struct.DDBLTFX]],
                   _type.HRESULT]
    BltBatch: _Callable[[_Pointer[_struct.DDBLTBATCH],
                         _type.DWORD,
                         _type.DWORD],
                        _type.HRESULT]
    BltFast: _Callable[[_type.DWORD,
                        _type.DWORD,
                        IDirectDrawSurface3,
                        _Pointer[_struct.RECT],
                        _type.DWORD],
                       _type.HRESULT]
    DeleteAttachedSurface: _Callable[[_type.DWORD,
                                      IDirectDrawSurface3],
                                     _type.HRESULT]
    EnumAttachedSurfaces: _Callable
    EnumOverlayZOrders: _Callable
    Flip: _Callable[[IDirectDrawSurface3,
                     _type.DWORD],
                    _type.HRESULT]
    GetAttachedSurface: _Callable[[_Pointer[_struct.DDSCAPS],
                                   _Pointer[IDirectDrawSurface3]],
                                  _type.HRESULT]
    GetBltStatus: _Callable[[_type.DWORD],
                            _type.HRESULT]
    GetCaps: _Callable[[_Pointer[_struct.DDSCAPS]],
                       _type.HRESULT]
    GetClipper: _Callable[[_Pointer[IDirectDrawClipper]],
                          _type.HRESULT]
    GetColorKey: _Callable[[_type.DWORD,
                            _Pointer[_struct.DDCOLORKEY]],
                           _type.HRESULT]
    GetDC: _Callable[[_Pointer[_type.HDC]],
                     _type.HRESULT]
    GetFlipStatus: _Callable[[_type.DWORD],
                             _type.HRESULT]
    GetOverlayPosition: _Callable[[_Pointer[_type.c_long],
                                   _Pointer[_type.c_long]],
                                  _type.HRESULT]
    GetPalette: _Callable[[_Pointer[IDirectDrawPalette]],
                          _type.HRESULT]
    GetPixelFormat: _Callable[[_Pointer[_struct.DDPIXELFORMAT]],
                              _type.HRESULT]
    GetSurfaceDesc: _Callable[[_Pointer[_struct.DDSURFACEDESC]],
                              _type.HRESULT]
    Initialize: _Callable[[IDirectDraw,
                           _Pointer[_struct.DDSURFACEDESC]],
                          _type.HRESULT]
    IsLost: _Callable[[],
                      _type.HRESULT]
    Lock: _Callable[[_Pointer[_struct.RECT],
                     _Pointer[_struct.DDSURFACEDESC],
                     _type.DWORD,
                     _type.HANDLE],
                    _type.HRESULT]
    ReleaseDC: _Callable[[_type.HDC],
                         _type.HRESULT]
    Restore: _Callable[[],
                       _type.HRESULT]
    SetClipper: _Callable[[IDirectDrawClipper],
                          _type.HRESULT]
    SetColorKey: _Callable[[_type.DWORD,
                            _Pointer[_struct.DDCOLORKEY]],
                           _type.HRESULT]
    SetOverlayPosition: _Callable[[_type.LONG,
                                   _type.LONG],
                                  _type.HRESULT]
    SetPalette: _Callable[[IDirectDrawPalette],
                          _type.HRESULT]
    Unlock: _Callable[[_type.LPVOID],
                      _type.HRESULT]
    UpdateOverlay: _Callable[[_Pointer[_struct.RECT],
                              IDirectDrawSurface3,
                              _Pointer[_struct.RECT],
                              _type.DWORD,
                              _Pointer[_struct.DDOVERLAYFX]],
                             _type.HRESULT]
    UpdateOverlayDisplay: _Callable[[_type.DWORD],
                                    _type.HRESULT]
    UpdateOverlayZOrder: _Callable[[_type.DWORD,
                                    IDirectDrawSurface3],
                                   _type.HRESULT]
    GetDDInterface: _Callable[[_Pointer[_type.LPVOID]],
                              _type.HRESULT]
    PageLock: _Callable[[_type.DWORD],
                        _type.HRESULT]
    PageUnlock: _Callable[[_type.DWORD],
                          _type.HRESULT]
    SetSurfaceDesc: _Callable[[_Pointer[_struct.DDSURFACEDESC],
                               _type.DWORD],
                              _type.HRESULT]


class IDirectDrawSurface4(_Unknwnbase.IUnknown):
    AddAttachedSurface: _Callable[[IDirectDrawSurface4],
                                  _type.HRESULT]
    AddOverlayDirtyRect: _Callable[[_Pointer[_struct.RECT]],
                                   _type.HRESULT]
    Blt: _Callable[[_Pointer[_struct.RECT],
                    IDirectDrawSurface4,
                    _Pointer[_struct.RECT],
                    _type.DWORD,
                    _Pointer[_struct.DDBLTFX]],
                   _type.HRESULT]
    BltBatch: _Callable[[_Pointer[_struct.DDBLTBATCH],
                         _type.DWORD,
                         _type.DWORD],
                        _type.HRESULT]
    BltFast: _Callable[[_type.DWORD,
                        _type.DWORD,
                        IDirectDrawSurface4,
                        _Pointer[_struct.RECT],
                        _type.DWORD],
                       _type.HRESULT]
    DeleteAttachedSurface: _Callable[[_type.DWORD,
                                      IDirectDrawSurface4],
                                     _type.HRESULT]
    EnumAttachedSurfaces: _Callable
    EnumOverlayZOrders: _Callable
    Flip: _Callable[[IDirectDrawSurface4,
                     _type.DWORD],
                    _type.HRESULT]
    GetAttachedSurface: _Callable[[_Pointer[_struct.DDSCAPS],
                                   _Pointer[IDirectDrawSurface4]],
                                  _type.HRESULT]
    GetBltStatus: _Callable[[_type.DWORD],
                            _type.HRESULT]
    GetCaps: _Callable[[_Pointer[_struct.DDSCAPS]],
                       _type.HRESULT]
    GetClipper: _Callable[[_Pointer[IDirectDrawClipper]],
                          _type.HRESULT]
    GetColorKey: _Callable[[_type.DWORD,
                            _Pointer[_struct.DDCOLORKEY]],
                           _type.HRESULT]
    GetDC: _Callable[[_Pointer[_type.HDC]],
                     _type.HRESULT]
    GetFlipStatus: _Callable[[_type.DWORD],
                             _type.HRESULT]
    GetOverlayPosition: _Callable[[_Pointer[_type.c_long],
                                   _Pointer[_type.c_long]],
                                  _type.HRESULT]
    GetPalette: _Callable[[_Pointer[IDirectDrawPalette]],
                          _type.HRESULT]
    GetPixelFormat: _Callable[[_Pointer[_struct.DDPIXELFORMAT]],
                              _type.HRESULT]
    GetSurfaceDesc: _Callable[[_Pointer[_struct.DDSURFACEDESC2]],
                              _type.HRESULT]
    Initialize: _Callable[[IDirectDraw,
                           _Pointer[_struct.DDSURFACEDESC2]],
                          _type.HRESULT]
    IsLost: _Callable[[],
                      _type.HRESULT]
    Lock: _Callable[[_Pointer[_struct.RECT],
                     _Pointer[_struct.DDSURFACEDESC2],
                     _type.DWORD,
                     _type.HANDLE],
                    _type.HRESULT]
    ReleaseDC: _Callable[[_type.HDC],
                         _type.HRESULT]
    Restore: _Callable[[],
                       _type.HRESULT]
    SetClipper: _Callable[[IDirectDrawClipper],
                          _type.HRESULT]
    SetColorKey: _Callable[[_type.DWORD,
                            _Pointer[_struct.DDCOLORKEY]],
                           _type.HRESULT]
    SetOverlayPosition: _Callable[[_type.LONG,
                                   _type.LONG],
                                  _type.HRESULT]
    SetPalette: _Callable[[IDirectDrawPalette],
                          _type.HRESULT]
    Unlock: _Callable[[_Pointer[_struct.RECT]],
                      _type.HRESULT]
    UpdateOverlay: _Callable[[_Pointer[_struct.RECT],
                              IDirectDrawSurface4,
                              _Pointer[_struct.RECT],
                              _type.DWORD,
                              _Pointer[_struct.DDOVERLAYFX]],
                             _type.HRESULT]
    UpdateOverlayDisplay: _Callable[[_type.DWORD],
                                    _type.HRESULT]
    UpdateOverlayZOrder: _Callable[[_type.DWORD,
                                    IDirectDrawSurface4],
                                   _type.HRESULT]
    GetDDInterface: _Callable[[_Pointer[_type.LPVOID]],
                              _type.HRESULT]
    PageLock: _Callable[[_type.DWORD],
                        _type.HRESULT]
    PageUnlock: _Callable[[_type.DWORD],
                          _type.HRESULT]
    SetSurfaceDesc: _Callable[[_Pointer[_struct.DDSURFACEDESC2],
                               _type.DWORD],
                              _type.HRESULT]
    SetPrivateData: _Callable[[_Pointer[_struct.GUID],
                               _type.LPVOID,
                               _type.DWORD,
                               _type.DWORD],
                              _type.HRESULT]
    GetPrivateData: _Callable[[_Pointer[_struct.GUID],
                               _type.LPVOID,
                               _Pointer[_type.DWORD]],
                              _type.HRESULT]
    FreePrivateData: _Callable[[_Pointer[_struct.GUID]],
                               _type.HRESULT]
    GetUniquenessValue: _Callable[[_Pointer[_type.DWORD]],
                                  _type.HRESULT]
    ChangeUniquenessValue: _Callable[[],
                                     _type.HRESULT]


class IDirectDrawSurface7(_Unknwnbase.IUnknown):
    AddAttachedSurface: _Callable[[IDirectDrawSurface7],
                                  _type.HRESULT]
    AddOverlayDirtyRect: _Callable[[_Pointer[_struct.RECT]],
                                   _type.HRESULT]
    Blt: _Callable[[_Pointer[_struct.RECT],
                    IDirectDrawSurface7,
                    _Pointer[_struct.RECT],
                    _type.DWORD,
                    _Pointer[_struct.DDBLTFX]],
                   _type.HRESULT]
    BltBatch: _Callable[[_Pointer[_struct.DDBLTBATCH],
                         _type.DWORD,
                         _type.DWORD],
                        _type.HRESULT]
    BltFast: _Callable[[_type.DWORD,
                        _type.DWORD,
                        IDirectDrawSurface7,
                        _Pointer[_struct.RECT],
                        _type.DWORD],
                       _type.HRESULT]
    DeleteAttachedSurface: _Callable[[_type.DWORD,
                                      IDirectDrawSurface7],
                                     _type.HRESULT]
    EnumAttachedSurfaces: _Callable
    EnumOverlayZOrders: _Callable
    Flip: _Callable[[IDirectDrawSurface7,
                     _type.DWORD],
                    _type.HRESULT]
    GetAttachedSurface: _Callable[[_Pointer[_struct.DDSCAPS],
                                   _Pointer[IDirectDrawSurface7]],
                                  _type.HRESULT]
    GetBltStatus: _Callable[[_type.DWORD],
                            _type.HRESULT]
    GetCaps: _Callable[[_Pointer[_struct.DDSCAPS]],
                       _type.HRESULT]
    GetClipper: _Callable[[_Pointer[IDirectDrawClipper]],
                          _type.HRESULT]
    GetColorKey: _Callable[[_type.DWORD,
                            _Pointer[_struct.DDCOLORKEY]],
                           _type.HRESULT]
    GetDC: _Callable[[_Pointer[_type.HDC]],
                     _type.HRESULT]
    GetFlipStatus: _Callable[[_type.DWORD],
                             _type.HRESULT]
    GetOverlayPosition: _Callable[[_Pointer[_type.c_long],
                                   _Pointer[_type.c_long]],
                                  _type.HRESULT]
    GetPalette: _Callable[[_Pointer[IDirectDrawPalette]],
                          _type.HRESULT]
    GetPixelFormat: _Callable[[_Pointer[_struct.DDPIXELFORMAT]],
                              _type.HRESULT]
    GetSurfaceDesc: _Callable[[_Pointer[_struct.DDSURFACEDESC2]],
                              _type.HRESULT]
    Initialize: _Callable[[IDirectDraw,
                           _Pointer[_struct.DDSURFACEDESC2]],
                          _type.HRESULT]
    IsLost: _Callable[[],
                      _type.HRESULT]
    Lock: _Callable[[_Pointer[_struct.RECT],
                     _Pointer[_struct.DDSURFACEDESC2],
                     _type.DWORD,
                     _type.HANDLE],
                    _type.HRESULT]
    ReleaseDC: _Callable[[_type.HDC],
                         _type.HRESULT]
    Restore: _Callable[[],
                       _type.HRESULT]
    SetClipper: _Callable[[IDirectDrawClipper],
                          _type.HRESULT]
    SetColorKey: _Callable[[_type.DWORD,
                            _Pointer[_struct.DDCOLORKEY]],
                           _type.HRESULT]
    SetOverlayPosition: _Callable[[_type.LONG,
                                   _type.LONG],
                                  _type.HRESULT]
    SetPalette: _Callable[[IDirectDrawPalette],
                          _type.HRESULT]
    Unlock: _Callable[[_Pointer[_struct.RECT]],
                      _type.HRESULT]
    UpdateOverlay: _Callable[[_Pointer[_struct.RECT],
                              IDirectDrawSurface7,
                              _Pointer[_struct.RECT],
                              _type.DWORD,
                              _Pointer[_struct.DDOVERLAYFX]],
                             _type.HRESULT]
    UpdateOverlayDisplay: _Callable[[_type.DWORD],
                                    _type.HRESULT]
    UpdateOverlayZOrder: _Callable[[_type.DWORD,
                                    IDirectDrawSurface7],
                                   _type.HRESULT]
    GetDDInterface: _Callable[[_Pointer[_type.LPVOID]],
                              _type.HRESULT]
    PageLock: _Callable[[_type.DWORD],
                        _type.HRESULT]
    PageUnlock: _Callable[[_type.DWORD],
                          _type.HRESULT]
    SetSurfaceDesc: _Callable[[_Pointer[_struct.DDSURFACEDESC2],
                               _type.DWORD],
                              _type.HRESULT]
    SetPrivateData: _Callable[[_Pointer[_struct.GUID],
                               _type.LPVOID,
                               _type.DWORD,
                               _type.DWORD],
                              _type.HRESULT]
    GetPrivateData: _Callable[[_Pointer[_struct.GUID],
                               _type.LPVOID,
                               _Pointer[_type.DWORD]],
                              _type.HRESULT]
    FreePrivateData: _Callable[[_Pointer[_struct.GUID]],
                               _type.HRESULT]
    GetUniquenessValue: _Callable[[_Pointer[_type.DWORD]],
                                  _type.HRESULT]
    ChangeUniquenessValue: _Callable[[],
                                     _type.HRESULT]
    SetPriority: _Callable[[_type.DWORD],
                           _type.HRESULT]
    GetPriority: _Callable[[_Pointer[_type.DWORD]],
                           _type.HRESULT]
    SetLOD: _Callable[[_type.DWORD],
                      _type.HRESULT]
    GetLOD: _Callable[[_Pointer[_type.DWORD]],
                      _type.HRESULT]


class IDirectDrawColorControl(_Unknwnbase.IUnknown):
    GetColorControls: _Callable[[_Pointer[_struct.DDCOLORCONTROL]],
                                _type.HRESULT]
    SetColorControls: _Callable[[_Pointer[_struct.DDCOLORCONTROL]],
                                _type.HRESULT]


class IDirectDrawGammaControl(_Unknwnbase.IUnknown):
    GetGammaRamp: _Callable[[_type.DWORD,
                             _Pointer[_struct.DDGAMMARAMP]],
                            _type.HRESULT]
    SetGammaRamp: _Callable[[_type.DWORD,
                             _Pointer[_struct.DDGAMMARAMP]],
                            _type.HRESULT]

from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

PluginAddColor: _Callable[[_type.c_int,  # color1
                           _type.c_int],  # color2
                          _type.c_int]
"""
Return the sum of colors
"""
PluginAddFrame: _Callable[[_type.c_int,  # animationId
                           _type.c_float,  # duration
                           _Pointer[_type.c_int],  # colors
                           _type.c_int],  # length
                          _type.c_int]
"""
Adds a frame to the `Chroma` animation and sets the `duration` (in seconds). The
`color` is expected to be an array of the dimensions for the
`deviceType/device`. The `length` parameter is the size of the `color` array.
For `EChromaSDKDevice1DEnum` the array size should be `MAX LEDS`. For
`EChromaSDKDevice2DEnum` the array size should be `MAX ROW` times `MAX COLUMN`.
Returns the animation id upon success. Returns negative one upon failure.
"""
PluginAddNonZeroAllKeys: _Callable[[_type.c_int,  # sourceAnimationId
                                    _type.c_int,  # targetAnimationId
                                    _type.c_int],  # frameId
                                   _type.c_void]
"""
Add source color to target where color is not black for frame id, reference
source and target by id.
"""
PluginAddNonZeroAllKeysAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                             _type.c_int],  # targetAnimationId
                                            _type.c_void]
"""
Add source color to target where color is not black for all frames, reference
source and target by id.
"""
PluginAddNonZeroAllKeysAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                 _type.c_char_p],  # targetAnimation
                                                _type.c_void]
"""
Add source color to target where color is not black for all frames, reference
source and target by name.
"""
PluginAddNonZeroAllKeysAllFramesNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                  _type.c_char_p],  # targetAnimation
                                                 _type.c_double]
"""
D suffix for limited data types.
"""
PluginAddNonZeroAllKeysAllFramesOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                                   _type.c_int,  # targetAnimationId
                                                   _type.c_int],  # offset
                                                  _type.c_void]
"""
Add source color to target where color is not black for all frames starting at
offset for the length of the source, reference source and target by id.
"""
PluginAddNonZeroAllKeysAllFramesOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                       _type.c_char_p,  # targetAnimation
                                                       _type.c_int],  # offset
                                                      _type.c_void]
"""
Add source color to target where color is not black for all frames starting at
offset for the length of the source, reference source and target by name.
"""
PluginAddNonZeroAllKeysAllFramesOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                        _type.c_char_p,  # targetAnimation
                                                        _type.c_double],  # offset
                                                       _type.c_double]
"""
D suffix for limited data types.
"""
PluginAddNonZeroAllKeysName: _Callable[[_type.c_char_p,  # sourceAnimation
                                        _type.c_char_p,  # targetAnimation
                                        _type.c_int],  # frameId
                                       _type.c_void]
"""
Add source color to target where color is not black for frame id, reference
source and target by name.
"""
PluginAddNonZeroAllKeysOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                          _type.c_int,  # targetAnimationId
                                          _type.c_int,  # frameId
                                          _type.c_int],  # offset
                                         _type.c_void]
"""
Add source color to target where color is not black for the source frame and
target offset frame, reference source and target by id.
"""
PluginAddNonZeroAllKeysOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                              _type.c_char_p,  # targetAnimation
                                              _type.c_int,  # frameId
                                              _type.c_int],  # offset
                                             _type.c_void]
"""
Add source color to target where color is not black for the source frame and
target offset frame, reference source and target by name.
"""
PluginAddNonZeroAllKeysOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                               _type.c_char_p,  # targetAnimation
                                               _type.c_double,  # frameId
                                               _type.c_double],  # offset
                                              _type.c_double]
"""
D suffix for limited data types.
"""
PluginAddNonZeroTargetAllKeysAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                                   _type.c_int],  # targetAnimationId
                                                  _type.c_void]
"""
Add source color to target where the target color is not black for all frames,
reference source and target by id.
"""
PluginAddNonZeroTargetAllKeysAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                       _type.c_char_p],  # targetAnimation
                                                      _type.c_void]
"""
Add source color to target where the target color is not black for all frames,
reference source and target by name.
"""
PluginAddNonZeroTargetAllKeysAllFramesNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                        _type.c_char_p],  # targetAnimation
                                                       _type.c_double]
"""
D suffix for limited data types.
"""
PluginAddNonZeroTargetAllKeysAllFramesOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                                         _type.c_int,  # targetAnimationId
                                                         _type.c_int],  # offset
                                                        _type.c_void]
"""
Add source color to target where the target color is not black for all frames
starting at offset for the length of the source, reference source and target by
id.
"""
PluginAddNonZeroTargetAllKeysAllFramesOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                             _type.c_char_p,  # targetAnimation
                                                             _type.c_int],  # offset
                                                            _type.c_void]
"""
Add source color to target where the target color is not black for all frames
starting at offset for the length of the source, reference source and target by
name.
"""
PluginAddNonZeroTargetAllKeysAllFramesOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                              _type.c_char_p,  # targetAnimation
                                                              _type.c_double],  # offset
                                                             _type.c_double]
"""
D suffix for limited data types.
"""
PluginAddNonZeroTargetAllKeysOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                                _type.c_int,  # targetAnimationId
                                                _type.c_int,  # frameId
                                                _type.c_int],  # offset
                                               _type.c_void]
"""
Add source color to target where target color is not blank from the source frame
to the target offset frame, reference source and target by id.
"""
PluginAddNonZeroTargetAllKeysOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                    _type.c_char_p,  # targetAnimation
                                                    _type.c_int,  # frameId
                                                    _type.c_int],  # offset
                                                   _type.c_void]
"""
Add source color to target where target color is not blank from the source frame
to the target offset frame, reference source and target by name.
"""
PluginAddNonZeroTargetAllKeysOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                     _type.c_char_p,  # targetAnimation
                                                     _type.c_double,  # frameId
                                                     _type.c_double],  # offset
                                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginAppendAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                  _type.c_int],  # targetAnimationId
                                 _type.c_void]
"""
Append all source frames to the target animation, reference source and target by
id.
"""
PluginAppendAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                      _type.c_char_p],  # targetAnimation
                                     _type.c_void]
"""
Append all source frames to the target animation, reference source and target by
name.
"""
PluginAppendAllFramesNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                       _type.c_char_p],  # targetAnimation
                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginClearAll: _Callable[[],
                          _type.c_void]
"""
`PluginClearAll` will issue a `CLEAR` effect for all devices.
"""
PluginClearAnimationType: _Callable[[_type.c_int,  # deviceType
                                     _type.c_int],  # device
                                    _type.c_void]
"""
`PluginClearAnimationType` will issue a `CLEAR` effect for the given device.
"""
PluginCloseAll: _Callable[[],
                          _type.c_void]
"""
`PluginCloseAll` closes all open animations so they can be reloaded from disk.
The set of animations will be stopped if playing.
"""
PluginCloseAnimation: _Callable[[_type.c_int],  # animationId
                                _type.c_int]
"""
Closes the `Chroma` animation to free up resources referenced by id. Returns the
animation id upon success. Returns negative one upon failure. This might be used
while authoring effects if there was a change necessitating re-opening the
animation. The animation id can no longer be used once closed.
"""
PluginCloseAnimationD: _Callable[[_type.c_double],  # animationId
                                 _type.c_double]
"""
D suffix for limited data types.
"""
PluginCloseAnimationName: _Callable[[_type.c_char_p],  # path
                                    _type.c_void]
"""
Closes the `Chroma` animation referenced by name so that the animation can be
reloaded from disk.
"""
PluginCloseAnimationNameD: _Callable[[_type.c_char_p],  # path
                                     _type.c_double]
"""
D suffix for limited data types.
"""
PluginCloseComposite: _Callable[[_type.c_char_p],  # name
                                _type.c_void]
"""
`PluginCloseComposite` closes a set of animations so they can be reloaded from
disk. The set of animations will be stopped if playing.
"""
PluginCloseCompositeD: _Callable[[_type.c_char_p],  # name
                                 _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyAllKeys: _Callable[[_type.c_int,  # sourceAnimationId
                              _type.c_int,  # targetAnimationId
                              _type.c_int],  # frameId
                             _type.c_void]
"""
Copy source animation to target animation for the given frame. Source and target
are referenced by id.
"""
PluginCopyAllKeysName: _Callable[[_type.c_char_p,  # sourceAnimation
                                  _type.c_char_p,  # targetAnimation
                                  _type.c_int],  # frameId
                                 _type.c_void]
"""
Copy source animation to target animation for the given frame. Source and target
are referenced by id.
"""
PluginCopyAnimation: _Callable[[_type.c_int,  # sourceAnimationId
                                _type.c_char_p],  # targetAnimation
                               _type.c_int]
"""
Copy animation to named target animation in memory. If target animation exists,
close first. Source is referenced by id.
"""
PluginCopyAnimationName: _Callable[[_type.c_char_p,  # sourceAnimation
                                    _type.c_char_p],  # targetAnimation
                                   _type.c_void]
"""
Copy animation to named target animation in memory. If target animation exists,
close first. Source is referenced by name.
"""
PluginCopyAnimationNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                     _type.c_char_p],  # targetAnimation
                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyBlueChannelAllFrames: _Callable[[_type.c_int,  # animationId
                                           _type.c_float,  # redIntensity
                                           _type.c_float],  # greenIntensity
                                          _type.c_void]
"""
Copy blue channel to other channels for all frames. Intensity range is 0.0 to
1.0. Reference the animation by id.
"""
PluginCopyBlueChannelAllFramesName: _Callable[[_type.c_char_p,  # path
                                               _type.c_float,  # redIntensity
                                               _type.c_float],  # greenIntensity
                                              _type.c_void]
"""
Copy blue channel to other channels for all frames. Intensity range is 0.0 to
1.0. Reference the animation by name.
"""
PluginCopyBlueChannelAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                                _type.c_double,  # redIntensity
                                                _type.c_double],  # greenIntensity
                                               _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyGreenChannelAllFrames: _Callable[[_type.c_int,  # animationId
                                            _type.c_float,  # redIntensity
                                            _type.c_float],  # blueIntensity
                                           _type.c_void]
"""
Copy green channel to other channels for all frames. Intensity range is 0.0 to
1.0. Reference the animation by id.
"""
PluginCopyGreenChannelAllFramesName: _Callable[[_type.c_char_p,  # path
                                                _type.c_float,  # redIntensity
                                                _type.c_float],  # blueIntensity
                                               _type.c_void]
"""
Copy green channel to other channels for all frames. Intensity range is 0.0 to
1.0. Reference the animation by name.
"""
PluginCopyGreenChannelAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                                 _type.c_double,  # redIntensity
                                                 _type.c_double],  # blueIntensity
                                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyKeyColor: _Callable[[_type.c_int,  # sourceAnimationId
                               _type.c_int,  # targetAnimationId
                               _type.c_int,  # frameId
                               _type.c_int],  # rzkey
                              _type.c_void]
"""
Copy animation key color from the source animation to the target animation for
the given frame. Reference the source and target by id.
"""
PluginCopyKeyColorAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                        _type.c_int,  # targetAnimationId
                                        _type.c_int],  # rzkey
                                       _type.c_void]
"""
Copy animation key color from the source animation to the target animation for
all frames. Reference the source and target by id.
"""
PluginCopyKeyColorAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                            _type.c_char_p,  # targetAnimation
                                            _type.c_int],  # rzkey
                                           _type.c_void]
"""
Copy animation key color from the source animation to the target animation for
all frames. Reference the source and target by name.
"""
PluginCopyKeyColorAllFramesNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                             _type.c_char_p,  # targetAnimation
                                             _type.c_double],  # rzkey
                                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyKeyColorAllFramesOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                              _type.c_int,  # targetAnimationId
                                              _type.c_int,  # rzkey
                                              _type.c_int],  # offset
                                             _type.c_void]
"""
Copy animation key color from the source animation to the target animation for
all frames, starting at the offset for the length of the source animation.
Source and target are referenced by id.
"""
PluginCopyKeyColorAllFramesOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                  _type.c_char_p,  # targetAnimation
                                                  _type.c_int,  # rzkey
                                                  _type.c_int],  # offset
                                                 _type.c_void]
"""
Copy animation key color from the source animation to the target animation for
all frames, starting at the offset for the length of the source animation.
Source and target are referenced by name.
"""
PluginCopyKeyColorAllFramesOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                   _type.c_char_p,  # targetAnimation
                                                   _type.c_double,  # rzkey
                                                   _type.c_double],  # offset
                                                  _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyKeyColorName: _Callable[[_type.c_char_p,  # sourceAnimation
                                   _type.c_char_p,  # targetAnimation
                                   _type.c_int,  # frameId
                                   _type.c_int],  # rzkey
                                  _type.c_void]
"""
Copy animation key color from the source animation to the target animation for
the given frame.
"""
PluginCopyKeyColorNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                    _type.c_char_p,  # targetAnimation
                                    _type.c_double,  # frameId
                                    _type.c_double],  # rzkey
                                   _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyKeysColor: _Callable[[_type.c_int,  # sourceAnimationId
                                _type.c_int,  # targetAnimationId
                                _type.c_int,  # frameId
                                _Pointer[_type.c_int],  # keys
                                _type.c_int],  # size
                               _type.c_void]
"""
Copy animation color for a set of keys from the source animation to the target
animation for the given frame. Reference the source and target by id.
"""
PluginCopyKeysColorAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                         _type.c_int,  # targetAnimationId
                                         _Pointer[_type.c_int],  # keys
                                         _type.c_int],  # size
                                        _type.c_void]
"""
Copy animation color for a set of keys from the source animation to the target
animation for all frames. Reference the source and target by id.
"""
PluginCopyKeysColorAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                             _type.c_char_p,  # targetAnimation
                                             _Pointer[_type.c_int],  # keys
                                             _type.c_int],  # size
                                            _type.c_void]
"""
Copy animation color for a set of keys from the source animation to the target
animation for all frames. Reference the source and target by name.
"""
PluginCopyKeysColorName: _Callable[[_type.c_char_p,  # sourceAnimation
                                    _type.c_char_p,  # targetAnimation
                                    _type.c_int,  # frameId
                                    _Pointer[_type.c_int],  # keys
                                    _type.c_int],  # size
                                   _type.c_void]
"""
Copy animation color for a set of keys from the source animation to the target
animation for the given frame. Reference the source and target by name.
"""
PluginCopyKeysColorOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                      _type.c_int,  # targetAnimationId
                                      _type.c_int,  # sourceFrameId
                                      _type.c_int,  # targetFrameId
                                      _Pointer[_type.c_int],  # keys
                                      _type.c_int],  # size
                                     _type.c_void]
"""
Copy animation color for a set of keys from the source animation to the target
animation from the source frame to the target frame. Reference the source and
target by id.
"""
PluginCopyKeysColorOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                          _type.c_char_p,  # targetAnimation
                                          _type.c_int,  # sourceFrameId
                                          _type.c_int,  # targetFrameId
                                          _Pointer[_type.c_int],  # keys
                                          _type.c_int],  # size
                                         _type.c_void]
"""
Copy animation color for a set of keys from the source animation to the target
animation from the source frame to the target frame. Reference the source and
target by name.
"""
PluginCopyNonZeroAllKeys: _Callable[[_type.c_int,  # sourceAnimationId
                                     _type.c_int,  # targetAnimationId
                                     _type.c_int],  # frameId
                                    _type.c_void]
"""
Copy source animation to target animation for the given frame. Source and target
are referenced by id.
"""
PluginCopyNonZeroAllKeysAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                              _type.c_int],  # targetAnimationId
                                             _type.c_void]
"""
Copy nonzero colors from a source animation to a target animation for all
frames. Reference source and target by id.
"""
PluginCopyNonZeroAllKeysAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                  _type.c_char_p],  # targetAnimation
                                                 _type.c_void]
"""
Copy nonzero colors from a source animation to a target animation for all
frames. Reference source and target by name.
"""
PluginCopyNonZeroAllKeysAllFramesNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                   _type.c_char_p],  # targetAnimation
                                                  _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyNonZeroAllKeysAllFramesOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                                    _type.c_int,  # targetAnimationId
                                                    _type.c_int],  # offset
                                                   _type.c_void]
"""
Copy nonzero colors from a source animation to a target animation for all frames
starting at the offset for the length of the source animation. The source and
target are referenced by id.
"""
PluginCopyNonZeroAllKeysAllFramesOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                        _type.c_char_p,  # targetAnimation
                                                        _type.c_int],  # offset
                                                       _type.c_void]
"""
Copy nonzero colors from a source animation to a target animation for all frames
starting at the offset for the length of the source animation. The source and
target are referenced by name.
"""
PluginCopyNonZeroAllKeysAllFramesOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                         _type.c_char_p,  # targetAnimation
                                                         _type.c_double],  # offset
                                                        _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyNonZeroAllKeysName: _Callable[[_type.c_char_p,  # sourceAnimation
                                         _type.c_char_p,  # targetAnimation
                                         _type.c_int],  # frameId
                                        _type.c_void]
"""
Copy nonzero colors from source animation to target animation for the specified
frame. Source and target are referenced by id.
"""
PluginCopyNonZeroAllKeysNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                          _type.c_char_p,  # targetAnimation
                                          _type.c_double],  # frameId
                                         _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyNonZeroAllKeysOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                           _type.c_int,  # targetAnimationId
                                           _type.c_int,  # frameId
                                           _type.c_int],  # offset
                                          _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation from the
source frame to the target offset frame. Source and target are referenced by id.
"""
PluginCopyNonZeroAllKeysOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                               _type.c_char_p,  # targetAnimation
                                               _type.c_int,  # frameId
                                               _type.c_int],  # offset
                                              _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation from the
source frame to the target offset frame. Source and target are referenced by
name.
"""
PluginCopyNonZeroAllKeysOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                _type.c_char_p,  # targetAnimation
                                                _type.c_double,  # frameId
                                                _type.c_double],  # offset
                                               _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyNonZeroKeyColor: _Callable[[_type.c_int,  # sourceAnimationId
                                      _type.c_int,  # targetAnimationId
                                      _type.c_int,  # frameId
                                      _type.c_int],  # rzkey
                                     _type.c_void]
"""
Copy animation key color from the source animation to the target animation for
the given frame where color is not zero.
"""
PluginCopyNonZeroKeyColorName: _Callable[[_type.c_char_p,  # sourceAnimation
                                          _type.c_char_p,  # targetAnimation
                                          _type.c_int,  # frameId
                                          _type.c_int],  # rzkey
                                         _type.c_void]
"""
Copy animation key color from the source animation to the target animation for
the given frame where color is not zero.
"""
PluginCopyNonZeroKeyColorNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                           _type.c_char_p,  # targetAnimation
                                           _type.c_double,  # frameId
                                           _type.c_double],  # rzkey
                                          _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyNonZeroTargetAllKeys: _Callable[[_type.c_int,  # sourceAnimationId
                                           _type.c_int,  # targetAnimationId
                                           _type.c_int],  # frameId
                                          _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation where the
target color is nonzero for the specified frame. Source and target are
referenced by id.
"""
PluginCopyNonZeroTargetAllKeysAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                                    _type.c_int],  # targetAnimationId
                                                   _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation where the
target color is nonzero for all frames. Source and target are referenced by id.
"""
PluginCopyNonZeroTargetAllKeysAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                        _type.c_char_p],  # targetAnimation
                                                       _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation where the
target color is nonzero for all frames. Source and target are referenced by
name.
"""
PluginCopyNonZeroTargetAllKeysAllFramesNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                         _type.c_char_p],  # targetAnimation
                                                        _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyNonZeroTargetAllKeysAllFramesOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                                          _type.c_int,  # targetAnimationId
                                                          _type.c_int],  # offset
                                                         _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation where the
target color is nonzero for all frames. Source and target are referenced by
name.
"""
PluginCopyNonZeroTargetAllKeysAllFramesOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                              _type.c_char_p,  # targetAnimation
                                                              _type.c_int],  # offset
                                                             _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation where the
target color is nonzero for all frames starting at the target offset for the
length of the source animation. Source and target animations are referenced by
name.
"""
PluginCopyNonZeroTargetAllKeysAllFramesOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                               _type.c_char_p,  # targetAnimation
                                                               _type.c_double],  # offset
                                                              _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyNonZeroTargetAllKeysName: _Callable[[_type.c_char_p,  # sourceAnimation
                                               _type.c_char_p,  # targetAnimation
                                               _type.c_int],  # frameId
                                              _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation where the
target color is nonzero for the specified frame. The source and target are
referenced by name.
"""
PluginCopyNonZeroTargetAllKeysNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                _type.c_char_p,  # targetAnimation
                                                _type.c_double],  # frameId
                                               _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyNonZeroTargetAllKeysOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                                 _type.c_int,  # targetAnimationId
                                                 _type.c_int,  # frameId
                                                 _type.c_int],  # offset
                                                _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation where the
target color is nonzero for the specified source frame and target offset frame.
The source and target are referenced by id.
"""
PluginCopyNonZeroTargetAllKeysOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                     _type.c_char_p,  # targetAnimation
                                                     _type.c_int,  # frameId
                                                     _type.c_int],  # offset
                                                    _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation where the
target color is nonzero for the specified source frame and target offset frame.
The source and target are referenced by name.
"""
PluginCopyNonZeroTargetAllKeysOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                      _type.c_char_p,  # targetAnimation
                                                      _type.c_double,  # frameId
                                                      _type.c_double],  # offset
                                                     _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyNonZeroTargetZeroAllKeysAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                                        _type.c_int],  # targetAnimationId
                                                       _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation where the
target color is zero for all frames. Source and target are referenced by id.
"""
PluginCopyNonZeroTargetZeroAllKeysAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                            _type.c_char_p],  # targetAnimation
                                                           _type.c_void]
"""
Copy nonzero colors from the source animation to the target animation where the
target color is zero for all frames. Source and target are referenced by name.
"""
PluginCopyNonZeroTargetZeroAllKeysAllFramesNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                             _type.c_char_p],  # targetAnimation
                                                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyRedChannelAllFrames: _Callable[[_type.c_int,  # animationId
                                          _type.c_float,  # greenIntensity
                                          _type.c_float],  # blueIntensity
                                         _type.c_void]
"""
Copy red channel to other channels for all frames. Intensity range is 0.0 to
1.0. Reference the animation by id.
"""
PluginCopyRedChannelAllFramesName: _Callable[[_type.c_char_p,  # path
                                              _type.c_float,  # greenIntensity
                                              _type.c_float],  # blueIntensity
                                             _type.c_void]
"""
Copy green channel to other channels for all frames. Intensity range is 0.0 to
1.0. Reference the animation by name.
"""
PluginCopyRedChannelAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                               _type.c_double,  # greenIntensity
                                               _type.c_double],  # blueIntensity
                                              _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyZeroAllKeys: _Callable[[_type.c_int,  # sourceAnimationId
                                  _type.c_int,  # targetAnimationId
                                  _type.c_int],  # frameId
                                 _type.c_void]
"""
Copy zero colors from source animation to target animation for the frame. Source
and target are referenced by id.
"""
PluginCopyZeroAllKeysAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                           _type.c_int],  # targetAnimationId
                                          _type.c_void]
"""
Copy zero colors from source animation to target animation for all frames.
Source and target are referenced by id.
"""
PluginCopyZeroAllKeysAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                               _type.c_char_p],  # targetAnimation
                                              _type.c_void]
"""
Copy zero colors from source animation to target animation for all frames.
Source and target are referenced by name.
"""
PluginCopyZeroAllKeysAllFramesNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                _type.c_char_p],  # targetAnimation
                                               _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyZeroAllKeysAllFramesOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                                 _type.c_int,  # targetAnimationId
                                                 _type.c_int],  # offset
                                                _type.c_void]
"""
Copy zero colors from source animation to target animation for all frames
starting at the target offset for the length of the source animation. Source and
target are referenced by id.
"""
PluginCopyZeroAllKeysAllFramesOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                     _type.c_char_p,  # targetAnimation
                                                     _type.c_int],  # offset
                                                    _type.c_void]
"""
Copy zero colors from source animation to target animation for all frames
starting at the target offset for the length of the source animation. Source and
target are referenced by name.
"""
PluginCopyZeroAllKeysAllFramesOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                      _type.c_char_p,  # targetAnimation
                                                      _type.c_double],  # offset
                                                     _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyZeroAllKeysName: _Callable[[_type.c_char_p,  # sourceAnimation
                                      _type.c_char_p,  # targetAnimation
                                      _type.c_int],  # frameId
                                     _type.c_void]
"""
Copy zero colors from source animation to target animation for the frame. Source
and target are referenced by name.
"""
PluginCopyZeroAllKeysOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                        _type.c_int,  # targetAnimationId
                                        _type.c_int,  # frameId
                                        _type.c_int],  # offset
                                       _type.c_void]
"""
Copy zero colors from source animation to target animation for the frame id
starting at the target offset for the length of the source animation. Source and
target are referenced by id.
"""
PluginCopyZeroAllKeysOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                            _type.c_char_p,  # targetAnimation
                                            _type.c_int,  # frameId
                                            _type.c_int],  # offset
                                           _type.c_void]
"""
Copy zero colors from source animation to target animation for the frame id
starting at the target offset for the length of the source animation. Source and
target are referenced by name.
"""
PluginCopyZeroKeyColor: _Callable[[_type.c_int,  # sourceAnimationId
                                   _type.c_int,  # targetAnimationId
                                   _type.c_int,  # frameId
                                   _type.c_int],  # rzkey
                                  _type.c_void]
"""
Copy zero key color from source animation to target animation for the specified
frame. Source and target are referenced by id.
"""
PluginCopyZeroKeyColorName: _Callable[[_type.c_char_p,  # sourceAnimation
                                       _type.c_char_p,  # targetAnimation
                                       _type.c_int,  # frameId
                                       _type.c_int],  # rzkey
                                      _type.c_void]
"""
Copy zero key color from source animation to target animation for the specified
frame. Source and target are referenced by name.
"""
PluginCopyZeroKeyColorNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                        _type.c_char_p,  # targetAnimation
                                        _type.c_double,  # frameId
                                        _type.c_double],  # rzkey
                                       _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyZeroTargetAllKeys: _Callable[[_type.c_int,  # sourceAnimationId
                                        _type.c_int,  # targetAnimationId
                                        _type.c_int],  # frameId
                                       _type.c_void]
"""
Copy nonzero color from source animation to target animation where target is
zero for the frame. Source and target are referenced by id.
"""
PluginCopyZeroTargetAllKeysAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                                 _type.c_int],  # targetAnimationId
                                                _type.c_void]
"""
Copy nonzero color from source animation to target animation where target is
zero for all frames. Source and target are referenced by id.
"""
PluginCopyZeroTargetAllKeysAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                     _type.c_char_p],  # targetAnimation
                                                    _type.c_void]
"""
Copy nonzero color from source animation to target animation where target is
zero for all frames. Source and target are referenced by name.
"""
PluginCopyZeroTargetAllKeysAllFramesNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                      _type.c_char_p],  # targetAnimation
                                                     _type.c_double]
"""
D suffix for limited data types.
"""
PluginCopyZeroTargetAllKeysName: _Callable[[_type.c_char_p,  # sourceAnimation
                                            _type.c_char_p,  # targetAnimation
                                            _type.c_int],  # frameId
                                           _type.c_void]
"""
Copy nonzero color from source animation to target animation where target is
zero for the frame. Source and target are referenced by name.
"""
PluginCoreCreateChromaLinkEffect: _Callable[[_enum.ChromaSDK.ChromaLink.EFFECT_TYPE,  # Effect
                                             _type.PRZPARAM,  # pParam
                                             _Pointer[_struct.RZEFFECTID]],  # pEffectId
                                            _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreCreateEffect: _Callable[[_struct.RZDEVICEID,  # DeviceId
                                   _enum.ChromaSDK.EFFECT_TYPE,  # Effect
                                   _type.PRZPARAM,  # pParam
                                   _Pointer[_struct.RZEFFECTID]],  # pEffectId
                                  _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreCreateHeadsetEffect: _Callable[[_enum.ChromaSDK.Headset.EFFECT_TYPE,  # Effect
                                          _type.PRZPARAM,  # pParam
                                          _Pointer[_struct.RZEFFECTID]],  # pEffectId
                                         _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreCreateKeyboardEffect: _Callable[[_enum.ChromaSDK.Keyboard.EFFECT_TYPE,  # Effect
                                           _type.PRZPARAM,  # pParam
                                           _Pointer[_struct.RZEFFECTID]],  # pEffectId
                                          _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreCreateKeypadEffect: _Callable[[_enum.ChromaSDK.Keypad.EFFECT_TYPE,  # Effect
                                         _type.PRZPARAM,  # pParam
                                         _Pointer[_struct.RZEFFECTID]],  # pEffectId
                                        _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreCreateMouseEffect: _Callable[[_enum.ChromaSDK.Mouse.EFFECT_TYPE,  # Effect
                                        _type.PRZPARAM,  # pParam
                                        _Pointer[_struct.RZEFFECTID]],  # pEffectId
                                       _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreCreateMousepadEffect: _Callable[[_enum.ChromaSDK.Mousepad.EFFECT_TYPE,  # Effect
                                           _type.PRZPARAM,  # pParam
                                           _Pointer[_struct.RZEFFECTID]],  # pEffectId
                                          _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreDeleteEffect: _Callable[[_struct.RZEFFECTID],  # EffectId
                                  _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreInit: _Callable[[],
                          _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreInitSDK: _Callable[[_Pointer[_struct.ChromaSDK.APPINFOTYPE]],  # AppInfo
                             _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreQueryDevice: _Callable[[_struct.RZDEVICEID,  # DeviceId
                                  _Pointer[_struct.ChromaSDK.DEVICE_INFO_TYPE]],  # DeviceInfo
                                 _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreSetEffect: _Callable[[_struct.RZEFFECTID],  # EffectId
                               _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCoreStreamBroadcast: _Callable[[_type.c_char_p,  # streamId
                                      _type.c_char_p],  # streamKey
                                     _type.c_bool]
"""
Begin broadcasting Chroma RGB data using the stored stream key as the endpoint.
Intended for Cloud Gaming Platforms, restore the streaming key when the game
instance is launched to continue streaming. streamId is a null terminated string
streamKey is a null terminated string StreamGetStatus() should return the READY
status to use this method.
"""
PluginCoreStreamBroadcastEnd: _Callable[[],
                                        _type.c_bool]
"""
End broadcasting Chroma RGB data. StreamGetStatus() should return the
BROADCASTING status to use this method.
"""
PluginCoreStreamGetAuthShortcode: _Callable[[_type.c_char_p,  # shortcode
                                             _Pointer[_type.c_uchar],  # length
                                             _Pointer[_type.c_wchar_t],  # platform
                                             _Pointer[_type.c_wchar_t]],  # title
                                            _type.c_void]
"""
shortcode: Pass the address of a preallocated character buffer to get the
streaming auth code. The buffer should have a minimum length of 6. length:
Length will return as zero if the streaming auth code could not be obtained. If
length is greater than zero, it will be the length of the returned streaming
auth code. Once you have the shortcode, it should be shown to the user so they
can associate the stream with their Razer ID StreamGetStatus() should return the
READY status before invoking this method. platform: is the null terminated
string that identifies the source of the stream: { GEFORCE_NOW, LUNA, STADIA,
GAME_PASS } title: is the null terminated string that identifies the application
or game.
"""
PluginCoreStreamGetFocus: _Callable[[_type.c_char_p,  # focus
                                     _Pointer[_type.c_uchar]],  # length
                                    _type.c_bool]
"""
focus: Pass the address of a preallocated character buffer to get the stream
focus. The buffer should have a length of 48 length: Length will return as zero
if the stream focus could not be obtained. If length is greater than zero, it
will be the length of the returned stream focus.
"""
PluginCoreStreamGetId: _Callable[[_type.c_char_p,  # shortcode
                                  _type.c_char_p,  # streamId
                                  _Pointer[_type.c_uchar]],  # length
                                 _type.c_void]
"""
Intended for Cloud Gaming Platforms, store the stream id to persist in user
preferences to continue streaming if the game is suspended or closed. shortcode:
The shortcode is a null terminated string. Use the shortcode that authorized the
stream to obtain the stream id. streamId should be a preallocated buffer to get
the stream key. The buffer should have a length of 48. length: Length will
return zero if the key could not be obtained. If the length is greater than
zero, it will be the length of the returned streaming id. Retrieve the stream id
after authorizing the shortcode. The authorization window will expire in 5
minutes. Be sure to save the stream key before the window expires.
StreamGetStatus() should return the READY status to use this method.
"""
PluginCoreStreamGetKey: _Callable[[_type.c_char_p,  # shortcode
                                   _type.c_char_p,  # streamKey
                                   _Pointer[_type.c_uchar]],  # length
                                  _type.c_void]
"""
Intended for Cloud Gaming Platforms, store the streaming key to persist in user
preferences to continue streaming if the game is suspended or closed. shortcode:
The shortcode is a null terminated string. Use the shortcode that authorized the
stream to obtain the stream key. If the status is in the BROADCASTING or
WATCHING state, passing a NULL shortcode will return the active streamId.
streamKey should be a preallocated buffer to get the stream key. The buffer
should have a length of 48. length: Length will return zero if the key could not
be obtained. If the length is greater than zero, it will be the length of the
returned streaming key. Retrieve the stream key after authorizing the shortcode.
The authorization window will expire in 5 minutes. Be sure to save the stream
key before the window expires. StreamGetStatus() should return the READY status
to use this method.
"""
PluginCoreStreamGetStatus: _Callable[[],
                                     _enum.ChromaSDK.Stream.StreamStatusType]
"""
Returns StreamStatus, the current status of the service
"""
PluginCoreStreamGetStatusString: _Callable[[_enum.ChromaSDK.Stream.StreamStatusType],  # status
                                           _type.c_char_p]
"""
Convert StreamStatusType to a printable string
"""
PluginCoreStreamReleaseShortcode: _Callable[[_type.c_char_p],  # shortcode
                                            _type.c_bool]
"""
This prevents the stream id and stream key from being obtained through the
shortcode. This closes the auth window. shortcode is a null terminated string.
StreamGetStatus() should return the READY status to use this method. returns
success when shortcode has been released
"""
PluginCoreStreamSetFocus: _Callable[[_type.c_char_p],  # focus
                                    _type.c_bool]
"""
The focus is a null terminated string. Set the focus identifer for the
application designated to automatically change the streaming state. Returns true
on success.
"""
PluginCoreStreamSupportsStreaming: _Callable[[],
                                             _type.c_bool]
"""
Returns true if the Chroma streaming is supported. If false is returned, avoid
calling stream methods.
"""
PluginCoreStreamWatch: _Callable[[_type.c_char_p,  # streamId
                                  _type.c_ulonglong],  # timestamp
                                 _type.c_bool]
"""
Begin watching the Chroma RGB data using streamID parameter. streamId is a null
terminated string. StreamGetStatus() should return the READY status to use this
method.
"""
PluginCoreStreamWatchEnd: _Callable[[],
                                    _type.c_bool]
"""
End watching Chroma RGB data stream. StreamGetStatus() should return the
WATCHING status to use this method.
"""
PluginCoreUnInit: _Callable[[],
                            _type.RZRESULT]
"""
Direct access to low level API.
"""
PluginCreateAnimation: _Callable[[_type.c_char_p,  # path
                                  _type.c_int,  # deviceType
                                  _type.c_int],  # device
                                 _type.c_int]
"""
Creates a `Chroma` animation at the given path. The `deviceType` parameter uses
`EChromaSDKDeviceTypeEnum` as an integer. The `device` parameter uses
`EChromaSDKDevice1DEnum` or `EChromaSDKDevice2DEnum` as an integer, respective
to the `deviceType`. Returns the animation id upon success. Returns negative one
upon failure. Saves a `Chroma` animation file with the `.chroma` extension at
the given path. Returns the animation id upon success. Returns negative one upon
failure.
"""
PluginCreateAnimationInMemory: _Callable[[_type.c_int,  # deviceType
                                          _type.c_int],  # device
                                         _type.c_int]
"""
Creates a `Chroma` animation in memory without creating a file. The `deviceType`
parameter uses `EChromaSDKDeviceTypeEnum` as an integer. The `device` parameter
uses `EChromaSDKDevice1DEnum` or `EChromaSDKDevice2DEnum` as an integer,
respective to the `deviceType`. Returns the animation id upon success. Returns
negative one upon failure. Returns the animation id upon success. Returns
negative one upon failure.
"""
PluginCreateEffect: _Callable[[_struct.RZDEVICEID,  # deviceId
                               _enum.ChromaSDK.EFFECT_TYPE,  # effect
                               _Pointer[_type.c_int],  # colors
                               _type.c_int,  # size
                               _Pointer[_struct.ChromaSDK.FChromaSDKGuid]],  # effectId
                              _type.RZRESULT]
"""
Create a device specific effect.
"""
PluginDeleteEffect: _Callable[[_Pointer[_struct.ChromaSDK.FChromaSDKGuid]],  # effectId
                              _type.RZRESULT]
"""
Delete an effect given the effect id.
"""
PluginDuplicateFirstFrame: _Callable[[_type.c_int,  # animationId
                                      _type.c_int],  # frameCount
                                     _type.c_void]
"""
Duplicate the first animation frame so that the animation length matches the
frame count. Animation is referenced by id.
"""
PluginDuplicateFirstFrameName: _Callable[[_type.c_char_p,  # path
                                          _type.c_int],  # frameCount
                                         _type.c_void]
"""
Duplicate the first animation frame so that the animation length matches the
frame count. Animation is referenced by name.
"""
PluginDuplicateFirstFrameNameD: _Callable[[_type.c_char_p,  # path
                                           _type.c_double],  # frameCount
                                          _type.c_double]
"""
D suffix for limited data types.
"""
PluginDuplicateFrames: _Callable[[_type.c_int],  # animationId
                                 _type.c_void]
"""
Duplicate all the frames of the animation to double the animation length. Frame
1 becomes frame 1 and 2. Frame 2 becomes frame 3 and 4. And so on. The animation
is referenced by id.
"""
PluginDuplicateFramesName: _Callable[[_type.c_char_p],  # path
                                     _type.c_void]
"""
Duplicate all the frames of the animation to double the animation length. Frame
1 becomes frame 1 and 2. Frame 2 becomes frame 3 and 4. And so on. The animation
is referenced by name.
"""
PluginDuplicateFramesNameD: _Callable[[_type.c_char_p],  # path
                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginDuplicateMirrorFrames: _Callable[[_type.c_int],  # animationId
                                       _type.c_void]
"""
Duplicate all the animation frames in reverse so that the animation plays
forwards and backwards. Animation is referenced by id.
"""
PluginDuplicateMirrorFramesName: _Callable[[_type.c_char_p],  # path
                                           _type.c_void]
"""
Duplicate all the animation frames in reverse so that the animation plays
forwards and backwards. Animation is referenced by name.
"""
PluginDuplicateMirrorFramesNameD: _Callable[[_type.c_char_p],  # path
                                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginFadeEndFrames: _Callable[[_type.c_int,  # animationId
                                _type.c_int],  # fade
                               _type.c_void]
"""
Fade the animation to black starting at the fade frame index to the end of the
animation. Animation is referenced by id.
"""
PluginFadeEndFramesName: _Callable[[_type.c_char_p,  # path
                                    _type.c_int],  # fade
                                   _type.c_void]
"""
Fade the animation to black starting at the fade frame index to the end of the
animation. Animation is referenced by name.
"""
PluginFadeEndFramesNameD: _Callable[[_type.c_char_p,  # path
                                     _type.c_double],  # fade
                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginFadeStartFrames: _Callable[[_type.c_int,  # animationId
                                  _type.c_int],  # fade
                                 _type.c_void]
"""
Fade the animation from black to full color starting at 0 to the fade frame
index. Animation is referenced by id.
"""
PluginFadeStartFramesName: _Callable[[_type.c_char_p,  # path
                                      _type.c_int],  # fade
                                     _type.c_void]
"""
Fade the animation from black to full color starting at 0 to the fade frame
index. Animation is referenced by name.
"""
PluginFadeStartFramesNameD: _Callable[[_type.c_char_p,  # path
                                       _type.c_double],  # fade
                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillColor: _Callable[[_type.c_int,  # animationId
                            _type.c_int,  # frameId
                            _type.c_int],  # color
                           _type.c_void]
"""
Set the RGB value for all colors in the specified frame. Animation is referenced
by id.
"""
PluginFillColorAllFrames: _Callable[[_type.c_int,  # animationId
                                     _type.c_int],  # color
                                    _type.c_void]
"""
Set the RGB value for all colors for all frames. Animation is referenced by id.
"""
PluginFillColorAllFramesName: _Callable[[_type.c_char_p,  # path
                                         _type.c_int],  # color
                                        _type.c_void]
"""
Set the RGB value for all colors for all frames. Animation is referenced by
name.
"""
PluginFillColorAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                          _type.c_double],  # color
                                         _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillColorAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                        _type.c_int,  # red
                                        _type.c_int,  # green
                                        _type.c_int],  # blue
                                       _type.c_void]
"""
Set the RGB value for all colors for all frames. Use the range of 0 to 255 for
red, green, and blue parameters. Animation is referenced by id.
"""
PluginFillColorAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                            _type.c_int,  # red
                                            _type.c_int,  # green
                                            _type.c_int],  # blue
                                           _type.c_void]
"""
Set the RGB value for all colors for all frames. Use the range of 0 to 255 for
red, green, and blue parameters. Animation is referenced by name.
"""
PluginFillColorAllFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                             _type.c_double,  # red
                                             _type.c_double,  # green
                                             _type.c_double],  # blue
                                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillColorName: _Callable[[_type.c_char_p,  # path
                                _type.c_int,  # frameId
                                _type.c_int],  # color
                               _type.c_void]
"""
Set the RGB value for all colors in the specified frame. Animation is referenced
by name.
"""
PluginFillColorNameD: _Callable[[_type.c_char_p,  # path
                                 _type.c_double,  # frameId
                                 _type.c_double],  # color
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillColorRGB: _Callable[[_type.c_int,  # animationId
                               _type.c_int,  # frameId
                               _type.c_int,  # red
                               _type.c_int,  # green
                               _type.c_int],  # blue
                              _type.c_void]
"""
Set the RGB value for all colors in the specified frame. Animation is referenced
by id.
"""
PluginFillColorRGBName: _Callable[[_type.c_char_p,  # path
                                   _type.c_int,  # frameId
                                   _type.c_int,  # red
                                   _type.c_int,  # green
                                   _type.c_int],  # blue
                                  _type.c_void]
"""
Set the RGB value for all colors in the specified frame. Animation is referenced
by name.
"""
PluginFillColorRGBNameD: _Callable[[_type.c_char_p,  # path
                                    _type.c_double,  # frameId
                                    _type.c_double,  # red
                                    _type.c_double,  # green
                                    _type.c_double],  # blue
                                   _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillNonZeroColor: _Callable[[_type.c_int,  # animationId
                                   _type.c_int,  # frameId
                                   _type.c_int],  # color
                                  _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Set the RGB value for a subset of colors in the specified frame.
Animation is referenced by id.
"""
PluginFillNonZeroColorAllFrames: _Callable[[_type.c_int,  # animationId
                                            _type.c_int],  # color
                                           _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Set the RGB value for a subset of colors for all frames. Animation is
referenced by id.
"""
PluginFillNonZeroColorAllFramesName: _Callable[[_type.c_char_p,  # path
                                                _type.c_int],  # color
                                               _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Set the RGB value for a subset of colors for all frames. Animation is
referenced by name.
"""
PluginFillNonZeroColorAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                                 _type.c_double],  # color
                                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillNonZeroColorAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                               _type.c_int,  # red
                                               _type.c_int,  # green
                                               _type.c_int],  # blue
                                              _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Set the RGB value for a subset of colors for all frames. Use the range of
0 to 255 for red, green, and blue parameters. Animation is referenced by id.
"""
PluginFillNonZeroColorAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                                   _type.c_int,  # red
                                                   _type.c_int,  # green
                                                   _type.c_int],  # blue
                                                  _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Set the RGB value for a subset of colors for all frames. Use the range of
0 to 255 for red, green, and blue parameters. Animation is referenced by name.
"""
PluginFillNonZeroColorAllFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                                    _type.c_double,  # red
                                                    _type.c_double,  # green
                                                    _type.c_double],  # blue
                                                   _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillNonZeroColorName: _Callable[[_type.c_char_p,  # path
                                       _type.c_int,  # frameId
                                       _type.c_int],  # color
                                      _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Set the RGB value for a subset of colors in the specified frame.
Animation is referenced by name.
"""
PluginFillNonZeroColorNameD: _Callable[[_type.c_char_p,  # path
                                        _type.c_double,  # frameId
                                        _type.c_double],  # color
                                       _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillNonZeroColorRGB: _Callable[[_type.c_int,  # animationId
                                      _type.c_int,  # frameId
                                      _type.c_int,  # red
                                      _type.c_int,  # green
                                      _type.c_int],  # blue
                                     _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Set the RGB value for a subset of colors in the specified frame. Use the
range of 0 to 255 for red, green, and blue parameters. Animation is referenced
by id.
"""
PluginFillNonZeroColorRGBName: _Callable[[_type.c_char_p,  # path
                                          _type.c_int,  # frameId
                                          _type.c_int,  # red
                                          _type.c_int,  # green
                                          _type.c_int],  # blue
                                         _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Set the RGB value for a subset of colors in the specified frame. Use the
range of 0 to 255 for red, green, and blue parameters. Animation is referenced
by name.
"""
PluginFillNonZeroColorRGBNameD: _Callable[[_type.c_char_p,  # path
                                           _type.c_double,  # frameId
                                           _type.c_double,  # red
                                           _type.c_double,  # green
                                           _type.c_double],  # blue
                                          _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillRandomColors: _Callable[[_type.c_int,  # animationId
                                   _type.c_int],  # frameId
                                  _type.c_void]
"""
Fill the frame with random RGB values for the given frame. Animation is
referenced by id.
"""
PluginFillRandomColorsAllFrames: _Callable[[_type.c_int],  # animationId
                                           _type.c_void]
"""
Fill the frame with random RGB values for all frames. Animation is referenced by
id.
"""
PluginFillRandomColorsAllFramesName: _Callable[[_type.c_char_p],  # path
                                               _type.c_void]
"""
Fill the frame with random RGB values for all frames. Animation is referenced by
name.
"""
PluginFillRandomColorsAllFramesNameD: _Callable[[_type.c_char_p],  # path
                                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillRandomColorsBlackAndWhite: _Callable[[_type.c_int,  # animationId
                                                _type.c_int],  # frameId
                                               _type.c_void]
"""
Fill the frame with random black and white values for the specified frame.
Animation is referenced by id.
"""
PluginFillRandomColorsBlackAndWhiteAllFrames: _Callable[[_type.c_int],  # animationId
                                                        _type.c_void]
"""
Fill the frame with random black and white values for all frames. Animation is
referenced by id.
"""
PluginFillRandomColorsBlackAndWhiteAllFramesName: _Callable[[_type.c_char_p],  # path
                                                            _type.c_void]
"""
Fill the frame with random black and white values for all frames. Animation is
referenced by name.
"""
PluginFillRandomColorsBlackAndWhiteAllFramesNameD: _Callable[[_type.c_char_p],  # path
                                                             _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillRandomColorsBlackAndWhiteName: _Callable[[_type.c_char_p,  # path
                                                    _type.c_int],  # frameId
                                                   _type.c_void]
"""
Fill the frame with random black and white values for the specified frame.
Animation is referenced by name.
"""
PluginFillRandomColorsBlackAndWhiteNameD: _Callable[[_type.c_char_p,  # path
                                                     _type.c_double],  # frameId
                                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillRandomColorsName: _Callable[[_type.c_char_p,  # path
                                       _type.c_int],  # frameId
                                      _type.c_void]
"""
Fill the frame with random RGB values for the given frame. Animation is
referenced by name.
"""
PluginFillRandomColorsNameD: _Callable[[_type.c_char_p,  # path
                                        _type.c_double],  # frameId
                                       _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillThresholdColors: _Callable[[_type.c_int,  # animationId
                                      _type.c_int,  # frameId
                                      _type.c_int,  # threshold
                                      _type.c_int],  # color
                                     _type.c_void]
"""
Fill the specified frame with RGB color where the animation color is less than
the RGB threshold. Animation is referenced by id.
"""
PluginFillThresholdColorsAllFrames: _Callable[[_type.c_int,  # animationId
                                               _type.c_int,  # threshold
                                               _type.c_int],  # color
                                              _type.c_void]
"""
Fill all frames with RGB color where the animation color is less than the RGB
threshold. Animation is referenced by id.
"""
PluginFillThresholdColorsAllFramesName: _Callable[[_type.c_char_p,  # path
                                                   _type.c_int,  # threshold
                                                   _type.c_int],  # color
                                                  _type.c_void]
"""
Fill all frames with RGB color where the animation color is less than the RGB
threshold. Animation is referenced by name.
"""
PluginFillThresholdColorsAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                                    _type.c_double,  # threshold
                                                    _type.c_double],  # color
                                                   _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillThresholdColorsAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                                  _type.c_int,  # threshold
                                                  _type.c_int,  # red
                                                  _type.c_int,  # green
                                                  _type.c_int],  # blue
                                                 _type.c_void]
"""
Fill all frames with RGB color where the animation color is less than the
threshold. Animation is referenced by id.
"""
PluginFillThresholdColorsAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                                      _type.c_int,  # threshold
                                                      _type.c_int,  # red
                                                      _type.c_int,  # green
                                                      _type.c_int],  # blue
                                                     _type.c_void]
"""
Fill all frames with RGB color where the animation color is less than the
threshold. Animation is referenced by name.
"""
PluginFillThresholdColorsAllFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                                       _type.c_double,  # threshold
                                                       _type.c_double,  # red
                                                       _type.c_double,  # green
                                                       _type.c_double],  # blue
                                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillThresholdColorsMinMaxAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                                        _type.c_int,  # minThreshold
                                                        _type.c_int,  # minRed
                                                        _type.c_int,  # minGreen
                                                        _type.c_int,  # minBlue
                                                        _type.c_int,  # maxThreshold
                                                        _type.c_int,  # maxRed
                                                        _type.c_int,  # maxGreen
                                                        _type.c_int],  # maxBlue
                                                       _type.c_void]
"""
Fill all frames with the min RGB color where the animation color is less than
the min threshold AND with the max RGB color where the animation is more than
the max threshold. Animation is referenced by id.
"""
PluginFillThresholdColorsMinMaxAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                                            _type.c_int,  # minThreshold
                                                            _type.c_int,  # minRed
                                                            _type.c_int,  # minGreen
                                                            _type.c_int,  # minBlue
                                                            _type.c_int,  # maxThreshold
                                                            _type.c_int,  # maxRed
                                                            _type.c_int,  # maxGreen
                                                            _type.c_int],  # maxBlue
                                                           _type.c_void]
"""
Fill all frames with the min RGB color where the animation color is less than
the min threshold AND with the max RGB color where the animation is more than
the max threshold. Animation is referenced by name.
"""
PluginFillThresholdColorsMinMaxAllFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                                             _type.c_double,  # minThreshold
                                                             _type.c_double,  # minRed
                                                             _type.c_double,  # minGreen
                                                             _type.c_double,  # minBlue
                                                             _type.c_double,  # maxThreshold
                                                             _type.c_double,  # maxRed
                                                             _type.c_double,  # maxGreen
                                                             _type.c_double],  # maxBlue
                                                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillThresholdColorsMinMaxRGB: _Callable[[_type.c_int,  # animationId
                                               _type.c_int,  # frameId
                                               _type.c_int,  # minThreshold
                                               _type.c_int,  # minRed
                                               _type.c_int,  # minGreen
                                               _type.c_int,  # minBlue
                                               _type.c_int,  # maxThreshold
                                               _type.c_int,  # maxRed
                                               _type.c_int,  # maxGreen
                                               _type.c_int],  # maxBlue
                                              _type.c_void]
"""
Fill the specified frame with the min RGB color where the animation color is
less than the min threshold AND with the max RGB color where the animation is
more than the max threshold. Animation is referenced by id.
"""
PluginFillThresholdColorsMinMaxRGBName: _Callable[[_type.c_char_p,  # path
                                                   _type.c_int,  # frameId
                                                   _type.c_int,  # minThreshold
                                                   _type.c_int,  # minRed
                                                   _type.c_int,  # minGreen
                                                   _type.c_int,  # minBlue
                                                   _type.c_int,  # maxThreshold
                                                   _type.c_int,  # maxRed
                                                   _type.c_int,  # maxGreen
                                                   _type.c_int],  # maxBlue
                                                  _type.c_void]
"""
Fill the specified frame with the min RGB color where the animation color is
less than the min threshold AND with the max RGB color where the animation is
more than the max threshold. Animation is referenced by name.
"""
PluginFillThresholdColorsMinMaxRGBNameD: _Callable[[_type.c_char_p,  # path
                                                    _type.c_double,  # frameId
                                                    _type.c_double,  # minThreshold
                                                    _type.c_double,  # minRed
                                                    _type.c_double,  # minGreen
                                                    _type.c_double,  # minBlue
                                                    _type.c_double,  # maxThreshold
                                                    _type.c_double,  # maxRed
                                                    _type.c_double,  # maxGreen
                                                    _type.c_double],  # maxBlue
                                                   _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillThresholdColorsName: _Callable[[_type.c_char_p,  # path
                                          _type.c_int,  # frameId
                                          _type.c_int,  # threshold
                                          _type.c_int],  # color
                                         _type.c_void]
"""
Fill the specified frame with RGB color where the animation color is less than
the RGB threshold. Animation is referenced by name.
"""
PluginFillThresholdColorsNameD: _Callable[[_type.c_char_p,  # path
                                           _type.c_double,  # frameId
                                           _type.c_double,  # threshold
                                           _type.c_double],  # color
                                          _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillThresholdColorsRGB: _Callable[[_type.c_int,  # animationId
                                         _type.c_int,  # frameId
                                         _type.c_int,  # threshold
                                         _type.c_int,  # red
                                         _type.c_int,  # green
                                         _type.c_int],  # blue
                                        _type.c_void]
"""
Fill the specified frame with RGB color where the animation color is less than
the RGB threshold. Animation is referenced by id.
"""
PluginFillThresholdColorsRGBName: _Callable[[_type.c_char_p,  # path
                                             _type.c_int,  # frameId
                                             _type.c_int,  # threshold
                                             _type.c_int,  # red
                                             _type.c_int,  # green
                                             _type.c_int],  # blue
                                            _type.c_void]
"""
Fill the specified frame with RGB color where the animation color is less than
the RGB threshold. Animation is referenced by name.
"""
PluginFillThresholdColorsRGBNameD: _Callable[[_type.c_char_p,  # path
                                              _type.c_double,  # frameId
                                              _type.c_double,  # threshold
                                              _type.c_double,  # red
                                              _type.c_double,  # green
                                              _type.c_double],  # blue
                                             _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillThresholdRGBColorsAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                                     _type.c_int,  # redThreshold
                                                     _type.c_int,  # greenThreshold
                                                     _type.c_int,  # blueThreshold
                                                     _type.c_int,  # red
                                                     _type.c_int,  # green
                                                     _type.c_int],  # blue
                                                    _type.c_void]
"""
Fill all frames with RGB color where the animation color is less than the RGB
threshold. Animation is referenced by id.
"""
PluginFillThresholdRGBColorsAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                                         _type.c_int,  # redThreshold
                                                         _type.c_int,  # greenThreshold
                                                         _type.c_int,  # blueThreshold
                                                         _type.c_int,  # red
                                                         _type.c_int,  # green
                                                         _type.c_int],  # blue
                                                        _type.c_void]
"""
Fill all frames with RGB color where the animation color is less than the RGB
threshold. Animation is referenced by name.
"""
PluginFillThresholdRGBColorsAllFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                                          _type.c_double,  # redThreshold
                                                          _type.c_double,  # greenThreshold
                                                          _type.c_double,  # blueThreshold
                                                          _type.c_double,  # red
                                                          _type.c_double,  # green
                                                          _type.c_double],  # blue
                                                         _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillThresholdRGBColorsRGB: _Callable[[_type.c_int,  # animationId
                                            _type.c_int,  # frameId
                                            _type.c_int,  # redThreshold
                                            _type.c_int,  # greenThreshold
                                            _type.c_int,  # blueThreshold
                                            _type.c_int,  # red
                                            _type.c_int,  # green
                                            _type.c_int],  # blue
                                           _type.c_void]
"""
Fill the specified frame with RGB color where the animation color is less than
the RGB threshold. Animation is referenced by id.
"""
PluginFillThresholdRGBColorsRGBName: _Callable[[_type.c_char_p,  # path
                                                _type.c_int,  # frameId
                                                _type.c_int,  # redThreshold
                                                _type.c_int,  # greenThreshold
                                                _type.c_int,  # blueThreshold
                                                _type.c_int,  # red
                                                _type.c_int,  # green
                                                _type.c_int],  # blue
                                               _type.c_void]
"""
Fill the specified frame with RGB color where the animation color is less than
the RGB threshold. Animation is referenced by name.
"""
PluginFillThresholdRGBColorsRGBNameD: _Callable[[_type.c_char_p,  # path
                                                 _type.c_double,  # frameId
                                                 _type.c_double,  # redThreshold
                                                 _type.c_double,  # greenThreshold
                                                 _type.c_double,  # blueThreshold
                                                 _type.c_double,  # red
                                                 _type.c_double,  # green
                                                 _type.c_double],  # blue
                                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillZeroColor: _Callable[[_type.c_int,  # animationId
                                _type.c_int,  # frameId
                                _type.c_int],  # color
                               _type.c_void]
"""
Fill the specified frame with RGB color where the animation color is zero.
Animation is referenced by id.
"""
PluginFillZeroColorAllFrames: _Callable[[_type.c_int,  # animationId
                                         _type.c_int],  # color
                                        _type.c_void]
"""
Fill all frames with RGB color where the animation color is zero. Animation is
referenced by id.
"""
PluginFillZeroColorAllFramesName: _Callable[[_type.c_char_p,  # path
                                             _type.c_int],  # color
                                            _type.c_void]
"""
Fill all frames with RGB color where the animation color is zero. Animation is
referenced by name.
"""
PluginFillZeroColorAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                              _type.c_double],  # color
                                             _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillZeroColorAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                            _type.c_int,  # red
                                            _type.c_int,  # green
                                            _type.c_int],  # blue
                                           _type.c_void]
"""
Fill all frames with RGB color where the animation color is zero. Animation is
referenced by id.
"""
PluginFillZeroColorAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                                _type.c_int,  # red
                                                _type.c_int,  # green
                                                _type.c_int],  # blue
                                               _type.c_void]
"""
Fill all frames with RGB color where the animation color is zero. Animation is
referenced by name.
"""
PluginFillZeroColorAllFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                                 _type.c_double,  # red
                                                 _type.c_double,  # green
                                                 _type.c_double],  # blue
                                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillZeroColorName: _Callable[[_type.c_char_p,  # path
                                    _type.c_int,  # frameId
                                    _type.c_int],  # color
                                   _type.c_void]
"""
Fill the specified frame with RGB color where the animation color is zero.
Animation is referenced by name.
"""
PluginFillZeroColorNameD: _Callable[[_type.c_char_p,  # path
                                     _type.c_double,  # frameId
                                     _type.c_double],  # color
                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginFillZeroColorRGB: _Callable[[_type.c_int,  # animationId
                                   _type.c_int,  # frameId
                                   _type.c_int,  # red
                                   _type.c_int,  # green
                                   _type.c_int],  # blue
                                  _type.c_void]
"""
Fill the specified frame with RGB color where the animation color is zero.
Animation is referenced by id.
"""
PluginFillZeroColorRGBName: _Callable[[_type.c_char_p,  # path
                                       _type.c_int,  # frameId
                                       _type.c_int,  # red
                                       _type.c_int,  # green
                                       _type.c_int],  # blue
                                      _type.c_void]
"""
Fill the specified frame with RGB color where the animation color is zero.
Animation is referenced by name.
"""
PluginFillZeroColorRGBNameD: _Callable[[_type.c_char_p,  # path
                                        _type.c_double,  # frameId
                                        _type.c_double,  # red
                                        _type.c_double,  # green
                                        _type.c_double],  # blue
                                       _type.c_double]
"""
D suffix for limited data types.
"""
PluginGet1DColor: _Callable[[_type.c_int,  # animationId
                             _type.c_int,  # frameId
                             _type.c_int],  # led
                            _type.c_int]
"""
Get the animation color for a frame given the `1D` `led`. The `led` should be
greater than or equal to 0 and less than the `MaxLeds`. Animation is referenced
by id.
"""
PluginGet1DColorName: _Callable[[_type.c_char_p,  # path
                                 _type.c_int,  # frameId
                                 _type.c_int],  # led
                                _type.c_int]
"""
Get the animation color for a frame given the `1D` `led`. The `led` should be
greater than or equal to 0 and less than the `MaxLeds`. Animation is referenced
by name.
"""
PluginGet1DColorNameD: _Callable[[_type.c_char_p,  # path
                                  _type.c_double,  # frameId
                                  _type.c_double],  # led
                                 _type.c_double]
"""
D suffix for limited data types.
"""
PluginGet2DColor: _Callable[[_type.c_int,  # animationId
                             _type.c_int,  # frameId
                             _type.c_int,  # row
                             _type.c_int],  # column
                            _type.c_int]
"""
Get the animation color for a frame given the `2D` `row` and `column`. The `row`
should be greater than or equal to 0 and less than the `MaxRow`. The `column`
should be greater than or equal to 0 and less than the `MaxColumn`. Animation is
referenced by id.
"""
PluginGet2DColorName: _Callable[[_type.c_char_p,  # path
                                 _type.c_int,  # frameId
                                 _type.c_int,  # row
                                 _type.c_int],  # column
                                _type.c_int]
"""
Get the animation color for a frame given the `2D` `row` and `column`. The `row`
should be greater than or equal to 0 and less than the `MaxRow`. The `column`
should be greater than or equal to 0 and less than the `MaxColumn`. Animation is
referenced by name.
"""
PluginGet2DColorNameD: _Callable[[_type.c_char_p,  # path
                                  _type.c_double,  # frameId
                                  _type.c_double,  # row
                                  _type.c_double],  # column
                                 _type.c_double]
"""
D suffix for limited data types.
"""
PluginGetAnimation: _Callable[[_type.c_char_p],  # name
                              _type.c_int]
"""
Get the animation id for the named animation.
"""
PluginGetAnimationCount: _Callable[[],
                                   _type.c_int]
"""
`PluginGetAnimationCount` will return the number of loaded animations.
"""
PluginGetAnimationD: _Callable[[_type.c_char_p],  # name
                               _type.c_double]
"""
D suffix for limited data types.
"""
PluginGetAnimationId: _Callable[[_type.c_int],  # index
                                _type.c_int]
"""
`PluginGetAnimationId` will return the `animationId` given the `index` of the
loaded animation. The `index` is zero-based and less than the number returned by
`PluginGetAnimationCount`. Use `PluginGetAnimationName` to get the name of the
animation.
"""
PluginGetAnimationName: _Callable[[_type.c_int],  # animationId
                                  _type.c_char_p]
"""
`PluginGetAnimationName` takes an `animationId` and returns the name of the
animation of the `.chroma` animation file. If a name is not available then an
empty string will be returned.
"""
PluginGetCurrentFrame: _Callable[[_type.c_int],  # animationId
                                 _type.c_int]
"""
Get the current frame of the animation referenced by id.
"""
PluginGetCurrentFrameName: _Callable[[_type.c_char_p],  # path
                                     _type.c_int]
"""
Get the current frame of the animation referenced by name.
"""
PluginGetCurrentFrameNameD: _Callable[[_type.c_char_p],  # path
                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginGetDevice: _Callable[[_type.c_int],  # animationId
                           _type.c_int]
"""
Returns the `EChromaSDKDevice1DEnum` or `EChromaSDKDevice2DEnum` of a `Chroma`
animation respective to the `deviceType`, as an integer upon success. Returns
negative one upon failure.
"""
PluginGetDeviceName: _Callable[[_type.c_char_p],  # path
                               _type.c_int]
"""
Returns the `EChromaSDKDevice1DEnum` or `EChromaSDKDevice2DEnum` of a `Chroma`
animation respective to the `deviceType`, as an integer upon success. Returns
negative one upon failure.
"""
PluginGetDeviceNameD: _Callable[[_type.c_char_p],  # path
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginGetDeviceType: _Callable[[_type.c_int],  # animationId
                               _type.c_int]
"""
Returns the `EChromaSDKDeviceTypeEnum` of a `Chroma` animation as an integer
upon success. Returns negative one upon failure.
"""
PluginGetDeviceTypeName: _Callable[[_type.c_char_p],  # path
                                   _type.c_int]
"""
Returns the `EChromaSDKDeviceTypeEnum` of a `Chroma` animation as an integer
upon success. Returns negative one upon failure.
"""
PluginGetDeviceTypeNameD: _Callable[[_type.c_char_p],  # path
                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginGetFrame: _Callable[[_type.c_int,  # animationId
                           _type.c_int,  # frameIndex
                           _Pointer[_type.c_float],  # duration
                           _Pointer[_type.c_int],  # colors
                           _type.c_int,  # length
                           _Pointer[_type.c_int],  # keys
                           _type.c_int],  # keysLength
                          _type.c_int]
"""
Get the frame colors and duration (in seconds) for a `Chroma` animation
referenced by id. The `color` is expected to be an array of the expected
dimensions for the `deviceType/device`. The `length` parameter is the size of
the `color` array. For `EChromaSDKDevice1DEnum` the array size should be `MAX
LEDS`. For `EChromaSDKDevice2DEnum` the array size should be `MAX ROW` times
`MAX COLUMN`. Keys are populated only for EChromaSDKDevice2DEnum.DE_Keyboard
and EChromaSDKDevice2DEnum.DE_KeyboardExtended. Keys will only use the
EChromaSDKDevice2DEnum.DE_Keyboard `MAX_ROW` times `MAX_COLUMN` keysLength.
Returns the animation id upon success. Returns negative one upon failure.
"""
PluginGetFrameCount: _Callable[[_type.c_int],  # animationId
                               _type.c_int]
"""
Returns the frame count of a `Chroma` animation upon success. Returns negative
one upon failure.
"""
PluginGetFrameCountName: _Callable[[_type.c_char_p],  # path
                                   _type.c_int]
"""
Returns the frame count of a `Chroma` animation upon success. Returns negative
one upon failure.
"""
PluginGetFrameCountNameD: _Callable[[_type.c_char_p],  # path
                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginGetFrameName: _Callable[[_type.c_char_p,  # path
                               _type.c_int,  # frameIndex
                               _Pointer[_type.c_float],  # duration
                               _Pointer[_type.c_int],  # colors
                               _type.c_int,  # length
                               _Pointer[_type.c_int],  # keys
                               _type.c_int],  # keysLength
                              _type.c_int]
"""
Get the frame colors and duration (in seconds) for a `Chroma` animation
referenced by name. The `color` is expected to be an array of the expected
dimensions for the `deviceType/device`. The `length` parameter is the size of
the `color` array. For `EChromaSDKDevice1DEnum` the array size should be `MAX
LEDS`. For `EChromaSDKDevice2DEnum` the array size should be `MAX ROW` times
`MAX COLUMN`. Keys are populated only for EChromaSDKDevice2DEnum.DE_Keyboard
and EChromaSDKDevice2DEnum.DE_KeyboardExtended. Keys will only use the
EChromaSDKDevice2DEnum.DE_Keyboard `MAX_ROW` times `MAX_COLUMN` keysLength.
Returns the animation id upon success. Returns negative one upon failure.
"""
PluginGetKeyColor: _Callable[[_type.c_int,  # animationId
                              _type.c_int,  # frameId
                              _type.c_int],  # rzkey
                             _type.c_int]
"""
Get the color of an animation key for the given frame referenced by id.
"""
PluginGetKeyColorD: _Callable[[_type.c_char_p,  # path
                               _type.c_double,  # frameId
                               _type.c_double],  # rzkey
                              _type.c_double]
"""
D suffix for limited data types.
"""
PluginGetKeyColorName: _Callable[[_type.c_char_p,  # path
                                  _type.c_int,  # frameId
                                  _type.c_int],  # rzkey
                                 _type.c_int]
"""
Get the color of an animation key for the given frame referenced by name.
"""
PluginGetLibraryLoadedState: _Callable[[],
                                       _type.RZRESULT]
"""
Returns `RZRESULT_SUCCESS` if the plugin has been initialized successfully.
Returns `RZRESULT_DLL_NOT_FOUND` if core Chroma library is not found. Returns
`RZRESULT_DLL_INVALID_SIGNATURE` if core Chroma library has an invalid
signature.
"""
PluginGetLibraryLoadedStateD: _Callable[[],
                                        _type.c_double]
"""
D suffix for limited data types.
"""
PluginGetMaxColumn: _Callable[[_type.c_int],  # device
                              _type.c_int]
"""
Returns the `MAX COLUMN` given the `EChromaSDKDevice2DEnum` device as an integer
upon success. Returns negative one upon failure.
"""
PluginGetMaxColumnD: _Callable[[_type.c_double],  # device
                               _type.c_double]
"""
D suffix for limited data types.
"""
PluginGetMaxLeds: _Callable[[_type.c_int],  # device
                            _type.c_int]
"""
Returns the MAX LEDS given the `EChromaSDKDevice1DEnum` device as an integer
upon success. Returns negative one upon failure.
"""
PluginGetMaxLedsD: _Callable[[_type.c_double],  # device
                             _type.c_double]
"""
D suffix for limited data types.
"""
PluginGetMaxRow: _Callable[[_type.c_int],  # device
                           _type.c_int]
"""
Returns the `MAX ROW` given the `EChromaSDKDevice2DEnum` device as an integer
upon success. Returns negative one upon failure.
"""
PluginGetMaxRowD: _Callable[[_type.c_double],  # device
                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginGetPlayingAnimationCount: _Callable[[],
                                          _type.c_int]
"""
`PluginGetPlayingAnimationCount` will return the number of playing animations.
"""
PluginGetPlayingAnimationId: _Callable[[_type.c_int],  # index
                                       _type.c_int]
"""
`PluginGetPlayingAnimationId` will return the `animationId` given the `index` of
the playing animation. The `index` is zero-based and less than the number
returned by `PluginGetPlayingAnimationCount`. Use `PluginGetAnimationName` to
get the name of the animation.
"""
PluginGetRGB: _Callable[[_type.c_int,  # red
                         _type.c_int,  # green
                         _type.c_int],  # blue
                        _type.c_int]
"""
Get the RGB color given red, green, and blue.
"""
PluginGetRGBD: _Callable[[_type.c_double,  # red
                          _type.c_double,  # green
                          _type.c_double],  # blue
                         _type.c_double]
"""
D suffix for limited data types.
"""
PluginHasAnimationLoop: _Callable[[_type.c_int],  # animationId
                                  _type.c_bool]
"""
Check if the animation has loop enabled referenced by id.
"""
PluginHasAnimationLoopName: _Callable[[_type.c_char_p],  # path
                                      _type.c_bool]
"""
Check if the animation has loop enabled referenced by name.
"""
PluginHasAnimationLoopNameD: _Callable[[_type.c_char_p],  # path
                                       _type.c_double]
"""
D suffix for limited data types.
"""
PluginInit: _Callable[[],
                      _type.RZRESULT]
"""
Initialize the ChromaSDK. Zero indicates success, otherwise failure. Many API
methods auto initialize the ChromaSDK if not already initialized.
"""
PluginInitD: _Callable[[],
                       _type.c_double]
"""
D suffix for limited data types.
"""
PluginInitSDK: _Callable[[_Pointer[_struct.ChromaSDK.APPINFOTYPE]],  # AppInfo
                         _type.RZRESULT]
"""
Initialize the ChromaSDK. AppInfo populates the details in Synapse. Zero
indicates success, otherwise failure. Many API methods auto initialize the
ChromaSDK if not already initialized.
"""
PluginInsertDelay: _Callable[[_type.c_int,  # animationId
                              _type.c_int,  # frameId
                              _type.c_int],  # delay
                             _type.c_void]
"""
Insert an animation delay by duplicating the frame by the delay number of times.
Animation is referenced by id.
"""
PluginInsertDelayName: _Callable[[_type.c_char_p,  # path
                                  _type.c_int,  # frameId
                                  _type.c_int],  # delay
                                 _type.c_void]
"""
Insert an animation delay by duplicating the frame by the delay number of times.
Animation is referenced by name.
"""
PluginInsertDelayNameD: _Callable[[_type.c_char_p,  # path
                                   _type.c_double,  # frameId
                                   _type.c_double],  # delay
                                  _type.c_double]
"""
D suffix for limited data types.
"""
PluginInsertFrame: _Callable[[_type.c_int,  # animationId
                              _type.c_int,  # sourceFrame
                              _type.c_int],  # targetFrame
                             _type.c_void]
"""
Duplicate the source frame index at the target frame index. Animation is
referenced by id.
"""
PluginInsertFrameName: _Callable[[_type.c_char_p,  # path
                                  _type.c_int,  # sourceFrame
                                  _type.c_int],  # targetFrame
                                 _type.c_void]
"""
Duplicate the source frame index at the target frame index. Animation is
referenced by name.
"""
PluginInsertFrameNameD: _Callable[[_type.c_char_p,  # path
                                   _type.c_double,  # sourceFrame
                                   _type.c_double],  # targetFrame
                                  _type.c_double]
"""
D suffix for limited data types.
"""
PluginInvertColors: _Callable[[_type.c_int,  # animationId
                               _type.c_int],  # frameId
                              _type.c_void]
"""
Invert all the colors at the specified frame. Animation is referenced by id.
"""
PluginInvertColorsAllFrames: _Callable[[_type.c_int],  # animationId
                                       _type.c_void]
"""
Invert all the colors for all frames. Animation is referenced by id.
"""
PluginInvertColorsAllFramesName: _Callable[[_type.c_char_p],  # path
                                           _type.c_void]
"""
Invert all the colors for all frames. Animation is referenced by name.
"""
PluginInvertColorsAllFramesNameD: _Callable[[_type.c_char_p],  # path
                                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginInvertColorsName: _Callable[[_type.c_char_p,  # path
                                   _type.c_int],  # frameId
                                  _type.c_void]
"""
Invert all the colors at the specified frame. Animation is referenced by name.
"""
PluginInvertColorsNameD: _Callable[[_type.c_char_p,  # path
                                    _type.c_double],  # frameId
                                   _type.c_double]
"""
D suffix for limited data types.
"""
PluginIsAnimationPaused: _Callable[[_type.c_int],  # animationId
                                   _type.c_bool]
"""
Check if the animation is paused referenced by id.
"""
PluginIsAnimationPausedName: _Callable[[_type.c_char_p],  # path
                                       _type.c_bool]
"""
Check if the animation is paused referenced by name.
"""
PluginIsAnimationPausedNameD: _Callable[[_type.c_char_p],  # path
                                        _type.c_double]
"""
D suffix for limited data types.
"""
PluginIsDialogOpen: _Callable[[],
                              _type.c_bool]
"""
The editor dialog is a non-blocking modal window, this method returns true if
the modal window is open, otherwise false.
"""
PluginIsDialogOpenD: _Callable[[],
                               _type.c_double]
"""
D suffix for limited data types.
"""
PluginIsInitialized: _Callable[[],
                               _type.c_bool]
"""
Returns true if the plugin has been initialized. Returns false if the plugin is
uninitialized.
"""
PluginIsInitializedD: _Callable[[],
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginIsPlatformSupported: _Callable[[],
                                     _type.c_bool]
"""
If the method can be invoked the method returns true.
"""
PluginIsPlatformSupportedD: _Callable[[],
                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginIsPlaying: _Callable[[_type.c_int],  # animationId
                           _type.c_bool]
"""
`PluginIsPlayingName` automatically handles initializing the `ChromaSDK`. The
named `.chroma` animation file will be automatically opened. The method will
return whether the animation is playing or not. Animation is referenced by id.
"""
PluginIsPlayingD: _Callable[[_type.c_double],  # animationId
                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginIsPlayingName: _Callable[[_type.c_char_p],  # path
                               _type.c_bool]
"""
`PluginIsPlayingName` automatically handles initializing the `ChromaSDK`. The
named `.chroma` animation file will be automatically opened. The method will
return whether the animation is playing or not. Animation is referenced by name.
"""
PluginIsPlayingNameD: _Callable[[_type.c_char_p],  # path
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginIsPlayingType: _Callable[[_type.c_int,  # deviceType
                                _type.c_int],  # device
                               _type.c_bool]
"""
`PluginIsPlayingType` automatically handles initializing the `ChromaSDK`. If any
animation is playing for the `deviceType` and `device` combination, the method
will return true, otherwise false.
"""
PluginIsPlayingTypeD: _Callable[[_type.c_double,  # deviceType
                                 _type.c_double],  # device
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginLerp: _Callable[[_type.c_float,  # start
                       _type.c_float,  # end
                       _type.c_float],  # amt
                      _type.c_float]
"""
Do a lerp math operation on a float.
"""
PluginLerpColor: _Callable[[_type.c_int,  # from
                            _type.c_int,  # to
                            _type.c_float],  # t
                           _type.c_int]
"""
Lerp from one color to another given t in the range 0.0 to 1.0.
"""
PluginLoadAnimation: _Callable[[_type.c_int],  # animationId
                               _type.c_int]
"""
Loads `Chroma` effects so that the animation can be played immediately. Returns
the animation id upon success. Returns negative one upon failure.
"""
PluginLoadAnimationD: _Callable[[_type.c_double],  # animationId
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginLoadAnimationName: _Callable[[_type.c_char_p],  # path
                                   _type.c_void]
"""
Load the named animation.
"""
PluginLoadComposite: _Callable[[_type.c_char_p],  # name
                               _type.c_void]
"""
Load a composite set of animations.
"""
PluginMakeBlankFrames: _Callable[[_type.c_int,  # animationId
                                  _type.c_int,  # frameCount
                                  _type.c_float,  # duration
                                  _type.c_int],  # color
                                 _type.c_void]
"""
Make a blank animation for the length of the frame count. Frame duration
defaults to the duration. The frame color defaults to color. Animation is
referenced by id.
"""
PluginMakeBlankFramesName: _Callable[[_type.c_char_p,  # path
                                      _type.c_int,  # frameCount
                                      _type.c_float,  # duration
                                      _type.c_int],  # color
                                     _type.c_void]
"""
Make a blank animation for the length of the frame count. Frame duration
defaults to the duration. The frame color defaults to color. Animation is
referenced by name.
"""
PluginMakeBlankFramesNameD: _Callable[[_type.c_char_p,  # path
                                       _type.c_double,  # frameCount
                                       _type.c_double,  # duration
                                       _type.c_double],  # color
                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginMakeBlankFramesRandom: _Callable[[_type.c_int,  # animationId
                                        _type.c_int,  # frameCount
                                        _type.c_float],  # duration
                                       _type.c_void]
"""
Make a blank animation for the length of the frame count. Frame duration
defaults to the duration. The frame color is random. Animation is referenced by
id.
"""
PluginMakeBlankFramesRandomBlackAndWhite: _Callable[[_type.c_int,  # animationId
                                                     _type.c_int,  # frameCount
                                                     _type.c_float],  # duration
                                                    _type.c_void]
"""
Make a blank animation for the length of the frame count. Frame duration
defaults to the duration. The frame color is random black and white. Animation
is referenced by id.
"""
PluginMakeBlankFramesRandomBlackAndWhiteName: _Callable[[_type.c_char_p,  # path
                                                         _type.c_int,  # frameCount
                                                         _type.c_float],  # duration
                                                        _type.c_void]
"""
Make a blank animation for the length of the frame count. Frame duration
defaults to the duration. The frame color is random black and white. Animation
is referenced by name.
"""
PluginMakeBlankFramesRandomBlackAndWhiteNameD: _Callable[[_type.c_char_p,  # path
                                                          _type.c_double,  # frameCount
                                                          _type.c_double],  # duration
                                                         _type.c_double]
"""
D suffix for limited data types.
"""
PluginMakeBlankFramesRandomName: _Callable[[_type.c_char_p,  # path
                                            _type.c_int,  # frameCount
                                            _type.c_float],  # duration
                                           _type.c_void]
"""
Make a blank animation for the length of the frame count. Frame duration
defaults to the duration. The frame color is random. Animation is referenced by
name.
"""
PluginMakeBlankFramesRandomNameD: _Callable[[_type.c_char_p,  # path
                                             _type.c_double,  # frameCount
                                             _type.c_double],  # duration
                                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginMakeBlankFramesRGB: _Callable[[_type.c_int,  # animationId
                                     _type.c_int,  # frameCount
                                     _type.c_float,  # duration
                                     _type.c_int,  # red
                                     _type.c_int,  # green
                                     _type.c_int],  # blue
                                    _type.c_void]
"""
Make a blank animation for the length of the frame count. Frame duration
defaults to the duration. The frame color defaults to color. Animation is
referenced by id.
"""
PluginMakeBlankFramesRGBName: _Callable[[_type.c_char_p,  # path
                                         _type.c_int,  # frameCount
                                         _type.c_float,  # duration
                                         _type.c_int,  # red
                                         _type.c_int,  # green
                                         _type.c_int],  # blue
                                        _type.c_void]
"""
Make a blank animation for the length of the frame count. Frame duration
defaults to the duration. The frame color defaults to color. Animation is
referenced by name.
"""
PluginMakeBlankFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                          _type.c_double,  # frameCount
                                          _type.c_double,  # duration
                                          _type.c_double,  # red
                                          _type.c_double,  # green
                                          _type.c_double],  # blue
                                         _type.c_double]
"""
D suffix for limited data types.
"""
PluginMirrorHorizontally: _Callable[[_type.c_int],  # animationId
                                    _type.c_int]
"""
Flips the color grid horizontally for all `Chroma` animation frames. Returns the
animation id upon success. Returns negative one upon failure.
"""
PluginMirrorVertically: _Callable[[_type.c_int],  # animationId
                                  _type.c_int]
"""
Flips the color grid vertically for all `Chroma` animation frames. This method
has no effect for `EChromaSDKDevice1DEnum` devices. Returns the animation id
upon success. Returns negative one upon failure.
"""
PluginMultiplyColorLerpAllFrames: _Callable[[_type.c_int,  # animationId
                                             _type.c_int,  # color1
                                             _type.c_int],  # color2
                                            _type.c_void]
"""
Multiply the color intensity with the lerp result from color 1 to color 2 using
the frame index divided by the frame count for the `t` parameter. Animation is
referenced in id.
"""
PluginMultiplyColorLerpAllFramesName: _Callable[[_type.c_char_p,  # path
                                                 _type.c_int,  # color1
                                                 _type.c_int],  # color2
                                                _type.c_void]
"""
Multiply the color intensity with the lerp result from color 1 to color 2 using
the frame index divided by the frame count for the `t` parameter. Animation is
referenced in name.
"""
PluginMultiplyColorLerpAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                                  _type.c_double,  # color1
                                                  _type.c_double],  # color2
                                                 _type.c_double]
"""
D suffix for limited data types.
"""
PluginMultiplyIntensity: _Callable[[_type.c_int,  # animationId
                                    _type.c_int,  # frameId
                                    _type.c_float],  # intensity
                                   _type.c_void]
"""
Multiply all the colors in the frame by the intensity value. The valid the
intensity range is from 0.0 to 255.0. RGB components are multiplied equally. An
intensity of 0.5 would half the color value. Black colors in the frame will not
be affected by this method.
"""
PluginMultiplyIntensityAllFrames: _Callable[[_type.c_int,  # animationId
                                             _type.c_float],  # intensity
                                            _type.c_void]
"""
Multiply all the colors for all frames by the intensity value. The valid the
intensity range is from 0.0 to 255.0. RGB components are multiplied equally. An
intensity of 0.5 would half the color value. Black colors in the frame will not
be affected by this method.
"""
PluginMultiplyIntensityAllFramesName: _Callable[[_type.c_char_p,  # path
                                                 _type.c_float],  # intensity
                                                _type.c_void]
"""
Multiply all the colors for all frames by the intensity value. The valid the
intensity range is from 0.0 to 255.0. RGB components are multiplied equally. An
intensity of 0.5 would half the color value. Black colors in the frame will not
be affected by this method.
"""
PluginMultiplyIntensityAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                                  _type.c_double],  # intensity
                                                 _type.c_double]
"""
D suffix for limited data types.
"""
PluginMultiplyIntensityAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                                _type.c_int,  # red
                                                _type.c_int,  # green
                                                _type.c_int],  # blue
                                               _type.c_void]
"""
Multiply all frames by the RBG color intensity. Animation is referenced by id.
"""
PluginMultiplyIntensityAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                                    _type.c_int,  # red
                                                    _type.c_int,  # green
                                                    _type.c_int],  # blue
                                                   _type.c_void]
"""
Multiply all frames by the RBG color intensity. Animation is referenced by name.
"""
PluginMultiplyIntensityAllFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                                     _type.c_double,  # red
                                                     _type.c_double,  # green
                                                     _type.c_double],  # blue
                                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginMultiplyIntensityColor: _Callable[[_type.c_int,  # animationId
                                         _type.c_int,  # frameId
                                         _type.c_int],  # color
                                        _type.c_void]
"""
Multiply the specific frame by the RBG color intensity. Animation is referenced
by id.
"""
PluginMultiplyIntensityColorAllFrames: _Callable[[_type.c_int,  # animationId
                                                  _type.c_int],  # color
                                                 _type.c_void]
"""
Multiply all frames by the RBG color intensity. Animation is referenced by id.
"""
PluginMultiplyIntensityColorAllFramesName: _Callable[[_type.c_char_p,  # path
                                                      _type.c_int],  # color
                                                     _type.c_void]
"""
Multiply all frames by the RBG color intensity. Animation is referenced by name.
"""
PluginMultiplyIntensityColorAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                                       _type.c_double],  # color
                                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginMultiplyIntensityColorName: _Callable[[_type.c_char_p,  # path
                                             _type.c_int,  # frameId
                                             _type.c_int],  # color
                                            _type.c_void]
"""
Multiply the specific frame by the RBG color intensity. Animation is referenced
by name.
"""
PluginMultiplyIntensityColorNameD: _Callable[[_type.c_char_p,  # path
                                              _type.c_double,  # frameId
                                              _type.c_double],  # color
                                             _type.c_double]
"""
D suffix for limited data types.
"""
PluginMultiplyIntensityName: _Callable[[_type.c_char_p,  # path
                                        _type.c_int,  # frameId
                                        _type.c_float],  # intensity
                                       _type.c_void]
"""
Multiply all the colors in the frame by the intensity value. The valid the
intensity range is from 0.0 to 255.0. RGB components are multiplied equally. An
intensity of 0.5 would half the color value. Black colors in the frame will not
be affected by this method.
"""
PluginMultiplyIntensityNameD: _Callable[[_type.c_char_p,  # path
                                         _type.c_double,  # frameId
                                         _type.c_double],  # intensity
                                        _type.c_double]
"""
D suffix for limited data types.
"""
PluginMultiplyIntensityRGB: _Callable[[_type.c_int,  # animationId
                                       _type.c_int,  # frameId
                                       _type.c_int,  # red
                                       _type.c_int,  # green
                                       _type.c_int],  # blue
                                      _type.c_void]
"""
Multiply the specific frame by the RBG color intensity. Animation is referenced
by id.
"""
PluginMultiplyIntensityRGBName: _Callable[[_type.c_char_p,  # path
                                           _type.c_int,  # frameId
                                           _type.c_int,  # red
                                           _type.c_int,  # green
                                           _type.c_int],  # blue
                                          _type.c_void]
"""
Multiply the specific frame by the RBG color intensity. Animation is referenced
by name.
"""
PluginMultiplyIntensityRGBNameD: _Callable[[_type.c_char_p,  # path
                                            _type.c_double,  # frameId
                                            _type.c_double,  # red
                                            _type.c_double,  # green
                                            _type.c_double],  # blue
                                           _type.c_double]
"""
D suffix for limited data types.
"""
PluginMultiplyNonZeroTargetColorLerp: _Callable[[_type.c_int,  # animationId
                                                 _type.c_int,  # frameId
                                                 _type.c_int,  # color1
                                                 _type.c_int],  # color2
                                                _type.c_void]
"""
Multiply the specific frame by the color lerp result between color 1 and 2 using
the frame color value as the `t` value. Animation is referenced by id.
"""
PluginMultiplyNonZeroTargetColorLerpAllFrames: _Callable[[_type.c_int,  # animationId
                                                          _type.c_int,  # color1
                                                          _type.c_int],  # color2
                                                         _type.c_void]
"""
Multiply all frames by the color lerp result between color 1 and 2 using the
frame color value as the `t` value. Animation is referenced by id.
"""
PluginMultiplyNonZeroTargetColorLerpAllFramesName: _Callable[[_type.c_char_p,  # path
                                                              _type.c_int,  # color1
                                                              _type.c_int],  # color2
                                                             _type.c_void]
"""
Multiply all frames by the color lerp result between color 1 and 2 using the
frame color value as the `t` value. Animation is referenced by name.
"""
PluginMultiplyNonZeroTargetColorLerpAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                                               _type.c_double,  # color1
                                                               _type.c_double],  # color2
                                                              _type.c_double]
"""
D suffix for limited data types.
"""
PluginMultiplyNonZeroTargetColorLerpAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                                             _type.c_int,  # red1
                                                             _type.c_int,  # green1
                                                             _type.c_int,  # blue1
                                                             _type.c_int,  # red2
                                                             _type.c_int,  # green2
                                                             _type.c_int],  # blue2
                                                            _type.c_void]
"""
Multiply the specific frame by the color lerp result between RGB 1 and 2 using
the frame color value as the `t` value. Animation is referenced by id.
"""
PluginMultiplyNonZeroTargetColorLerpAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                                                 _type.c_int,  # red1
                                                                 _type.c_int,  # green1
                                                                 _type.c_int,  # blue1
                                                                 _type.c_int,  # red2
                                                                 _type.c_int,  # green2
                                                                 _type.c_int],  # blue2
                                                                _type.c_void]
"""
Multiply the specific frame by the color lerp result between RGB 1 and 2 using
the frame color value as the `t` value. Animation is referenced by name.
"""
PluginMultiplyNonZeroTargetColorLerpAllFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                                                  _type.c_double,  # red1
                                                                  _type.c_double,  # green1
                                                                  _type.c_double,  # blue1
                                                                  _type.c_double,  # red2
                                                                  _type.c_double,  # green2
                                                                  _type.c_double],  # blue2
                                                                 _type.c_double]
"""
D suffix for limited data types.
"""
PluginMultiplyTargetColorLerp: _Callable[[_type.c_int,  # animationId
                                          _type.c_int,  # frameId
                                          _type.c_int,  # color1
                                          _type.c_int],  # color2
                                         _type.c_void]
"""
Multiply the specific frame by the color lerp result between color 1 and 2 using
the frame color value as the `t` value. Animation is referenced by id.
"""
PluginMultiplyTargetColorLerpAllFrames: _Callable[[_type.c_int,  # animationId
                                                   _type.c_int,  # color1
                                                   _type.c_int],  # color2
                                                  _type.c_void]
"""
Multiply all frames by the color lerp result between color 1 and 2 using the
frame color value as the `t` value. Animation is referenced by id.
"""
PluginMultiplyTargetColorLerpAllFramesName: _Callable[[_type.c_char_p,  # path
                                                       _type.c_int,  # color1
                                                       _type.c_int],  # color2
                                                      _type.c_void]
"""
Multiply all frames by the color lerp result between color 1 and 2 using the
frame color value as the `t` value. Animation is referenced by name.
"""
PluginMultiplyTargetColorLerpAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                                        _type.c_double,  # color1
                                                        _type.c_double],  # color2
                                                       _type.c_double]
"""
D suffix for limited data types.
"""
PluginMultiplyTargetColorLerpAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                                      _type.c_int,  # red1
                                                      _type.c_int,  # green1
                                                      _type.c_int,  # blue1
                                                      _type.c_int,  # red2
                                                      _type.c_int,  # green2
                                                      _type.c_int],  # blue2
                                                     _type.c_void]
"""
Multiply all frames by the color lerp result between RGB 1 and 2 using the frame
color value as the `t` value. Animation is referenced by id.
"""
PluginMultiplyTargetColorLerpAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                                          _type.c_int,  # red1
                                                          _type.c_int,  # green1
                                                          _type.c_int,  # blue1
                                                          _type.c_int,  # red2
                                                          _type.c_int,  # green2
                                                          _type.c_int],  # blue2
                                                         _type.c_void]
"""
Multiply all frames by the color lerp result between RGB 1 and 2 using the frame
color value as the `t` value. Animation is referenced by name.
"""
PluginMultiplyTargetColorLerpAllFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                                           _type.c_double,  # red1
                                                           _type.c_double,  # green1
                                                           _type.c_double,  # blue1
                                                           _type.c_double,  # red2
                                                           _type.c_double,  # green2
                                                           _type.c_double],  # blue2
                                                          _type.c_double]
"""
D suffix for limited data types.
"""
PluginMultiplyTargetColorLerpName: _Callable[[_type.c_char_p,  # path
                                              _type.c_int,  # frameId
                                              _type.c_int,  # color1
                                              _type.c_int],  # color2
                                             _type.c_void]
"""
Multiply the specific frame by the color lerp result between color 1 and 2 using
the frame color value as the `t` value. Animation is referenced by name.
"""
PluginOffsetColors: _Callable[[_type.c_int,  # animationId
                               _type.c_int,  # frameId
                               _type.c_int,  # red
                               _type.c_int,  # green
                               _type.c_int],  # blue
                              _type.c_void]
"""
Offset all colors in the frame using the RGB offset. Use the range of -255 to
255 for red, green, and blue parameters. Negative values remove color. Positive
values add color.
"""
PluginOffsetColorsAllFrames: _Callable[[_type.c_int,  # animationId
                                        _type.c_int,  # red
                                        _type.c_int,  # green
                                        _type.c_int],  # blue
                                       _type.c_void]
"""
Offset all colors for all frames using the RGB offset. Use the range of -255 to
255 for red, green, and blue parameters. Negative values remove color. Positive
values add color.
"""
PluginOffsetColorsAllFramesName: _Callable[[_type.c_char_p,  # path
                                            _type.c_int,  # red
                                            _type.c_int,  # green
                                            _type.c_int],  # blue
                                           _type.c_void]
"""
Offset all colors for all frames using the RGB offset. Use the range of -255 to
255 for red, green, and blue parameters. Negative values remove color. Positive
values add color.
"""
PluginOffsetColorsAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                             _type.c_double,  # red
                                             _type.c_double,  # green
                                             _type.c_double],  # blue
                                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginOffsetColorsName: _Callable[[_type.c_char_p,  # path
                                   _type.c_int,  # frameId
                                   _type.c_int,  # red
                                   _type.c_int,  # green
                                   _type.c_int],  # blue
                                  _type.c_void]
"""
Offset all colors in the frame using the RGB offset. Use the range of -255 to
255 for red, green, and blue parameters. Negative values remove color. Positive
values add color.
"""
PluginOffsetColorsNameD: _Callable[[_type.c_char_p,  # path
                                    _type.c_double,  # frameId
                                    _type.c_double,  # red
                                    _type.c_double,  # green
                                    _type.c_double],  # blue
                                   _type.c_double]
"""
D suffix for limited data types.
"""
PluginOffsetNonZeroColors: _Callable[[_type.c_int,  # animationId
                                      _type.c_int,  # frameId
                                      _type.c_int,  # red
                                      _type.c_int,  # green
                                      _type.c_int],  # blue
                                     _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Offset a subset of colors in the frame using the RGB offset. Use the
range of -255 to 255 for red, green, and blue parameters. Negative values remove
color. Positive values add color.
"""
PluginOffsetNonZeroColorsAllFrames: _Callable[[_type.c_int,  # animationId
                                               _type.c_int,  # red
                                               _type.c_int,  # green
                                               _type.c_int],  # blue
                                              _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Offset a subset of colors for all frames using the RGB offset. Use the
range of -255 to 255 for red, green, and blue parameters. Negative values remove
color. Positive values add color.
"""
PluginOffsetNonZeroColorsAllFramesName: _Callable[[_type.c_char_p,  # path
                                                   _type.c_int,  # red
                                                   _type.c_int,  # green
                                                   _type.c_int],  # blue
                                                  _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Offset a subset of colors for all frames using the RGB offset. Use the
range of -255 to 255 for red, green, and blue parameters. Negative values remove
color. Positive values add color.
"""
PluginOffsetNonZeroColorsAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                                    _type.c_double,  # red
                                                    _type.c_double,  # green
                                                    _type.c_double],  # blue
                                                   _type.c_double]
"""
D suffix for limited data types.
"""
PluginOffsetNonZeroColorsName: _Callable[[_type.c_char_p,  # path
                                          _type.c_int,  # frameId
                                          _type.c_int,  # red
                                          _type.c_int,  # green
                                          _type.c_int],  # blue
                                         _type.c_void]
"""
This method will only update colors in the animation that are not already set to
black. Offset a subset of colors in the frame using the RGB offset. Use the
range of -255 to 255 for red, green, and blue parameters. Negative values remove
color. Positive values add color.
"""
PluginOffsetNonZeroColorsNameD: _Callable[[_type.c_char_p,  # path
                                           _type.c_double,  # frameId
                                           _type.c_double,  # red
                                           _type.c_double,  # green
                                           _type.c_double],  # blue
                                          _type.c_double]
"""
D suffix for limited data types.
"""
PluginOpenAnimation: _Callable[[_type.c_char_p],  # path
                               _type.c_int]
"""
Opens a `Chroma` animation file so that it can be played. Returns an animation
id >= 0 upon success. Returns negative one if there was a failure. The animation
id is used in most of the API methods.
"""
PluginOpenAnimationD: _Callable[[_type.c_char_p],  # path
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginOpenAnimationFromMemory: _Callable[[_Pointer[_type.BYTE],  # data
                                          _type.c_char_p],  # name
                                         _type.c_int]
"""
Opens a `Chroma` animation data from memory so that it can be played. `Data` is
a pointer to BYTE array of the loaded animation in memory. `Name` will be
assigned to the animation when loaded. Returns an animation id >= 0 upon
success. Returns negative one if there was a failure. The animation id is used
in most of the API methods.
"""
PluginOpenEditorDialog: _Callable[[_type.c_char_p],  # path
                                  _type.c_int]
"""
Opens a `Chroma` animation file with the `.chroma` extension. Returns zero upon
success. Returns negative one if there was a failure.
"""
PluginOpenEditorDialogAndPlay: _Callable[[_type.c_char_p],  # path
                                         _type.c_int]
"""
Open the named animation in the editor dialog and play the animation at start.
"""
PluginOpenEditorDialogAndPlayD: _Callable[[_type.c_char_p],  # path
                                          _type.c_double]
"""
D suffix for limited data types.
"""
PluginOpenEditorDialogD: _Callable[[_type.c_char_p],  # path
                                   _type.c_double]
"""
D suffix for limited data types.
"""
PluginOverrideFrameDuration: _Callable[[_type.c_int,  # animationId
                                        _type.c_float],  # duration
                                       _type.c_int]
"""
Sets the `duration` for all grames in the `Chroma` animation to the `duration`
parameter. Returns the animation id upon success. Returns negative one upon
failure.
"""
PluginOverrideFrameDurationD: _Callable[[_type.c_double,  # animationId
                                         _type.c_double],  # duration
                                        _type.c_double]
"""
D suffix for limited data types.
"""
PluginOverrideFrameDurationName: _Callable[[_type.c_char_p,  # path
                                            _type.c_float],  # duration
                                           _type.c_void]
"""
Override the duration of all frames with the `duration` value. Animation is
referenced by name.
"""
PluginPauseAnimation: _Callable[[_type.c_int],  # animationId
                                _type.c_void]
"""
Pause the current animation referenced by id.
"""
PluginPauseAnimationName: _Callable[[_type.c_char_p],  # path
                                    _type.c_void]
"""
Pause the current animation referenced by name.
"""
PluginPauseAnimationNameD: _Callable[[_type.c_char_p],  # path
                                     _type.c_double]
"""
D suffix for limited data types.
"""
PluginPlayAnimation: _Callable[[_type.c_int],  # animationId
                               _type.c_int]
"""
Plays the `Chroma` animation. This will load the animation, if not loaded
previously. Returns the animation id upon success. Returns negative one upon
failure.
"""
PluginPlayAnimationD: _Callable[[_type.c_double],  # animationId
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginPlayAnimationFrame: _Callable[[_type.c_int,  # animationId
                                     _type.c_int,  # frameId
                                     _type.c_bool],  # loop
                                    _type.c_void]
"""
`PluginPlayAnimationFrame` automatically handles initializing the `ChromaSDK`.
The method will play the animation given the `animationId` with looping `on` or
`off` starting at the `frameId`.
"""
PluginPlayAnimationFrameName: _Callable[[_type.c_char_p,  # path
                                         _type.c_int,  # frameId
                                         _type.c_bool],  # loop
                                        _type.c_void]
"""
`PluginPlayAnimationFrameName` automatically handles initializing the
`ChromaSDK`. The named `.chroma` animation file will be automatically opened.
The animation will play with looping `on` or `off` starting at the `frameId`.
"""
PluginPlayAnimationFrameNameD: _Callable[[_type.c_char_p,  # path
                                          _type.c_double,  # frameId
                                          _type.c_double],  # loop
                                         _type.c_double]
"""
D suffix for limited data types.
"""
PluginPlayAnimationLoop: _Callable[[_type.c_int,  # animationId
                                    _type.c_bool],  # loop
                                   _type.c_void]
"""
`PluginPlayAnimationLoop` automatically handles initializing the `ChromaSDK`.
The method will play the animation given the `animationId` with looping `on` or
`off`.
"""
PluginPlayAnimationName: _Callable[[_type.c_char_p,  # path
                                    _type.c_bool],  # loop
                                   _type.c_void]
"""
`PluginPlayAnimationName` automatically handles initializing the `ChromaSDK`.
The named `.chroma` animation file will be automatically opened. The animation
will play with looping `on` or `off`.
"""
PluginPlayAnimationNameD: _Callable[[_type.c_char_p,  # path
                                     _type.c_double],  # loop
                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginPlayComposite: _Callable[[_type.c_char_p,  # name
                                _type.c_bool],  # loop
                               _type.c_void]
"""
`PluginPlayComposite` automatically handles initializing the `ChromaSDK`. The
named animation files for the `.chroma` set will be automatically opened. The
set of animations will play with looping `on` or `off`.
"""
PluginPlayCompositeD: _Callable[[_type.c_char_p,  # name
                                 _type.c_double],  # loop
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginPreviewFrame: _Callable[[_type.c_int,  # animationId
                               _type.c_int],  # frameIndex
                              _type.c_int]
"""
Displays the `Chroma` animation frame on `Chroma` hardware given the
`frameIndex`. Returns the animation id upon success. Returns negative one upon
failure.
"""
PluginPreviewFrameD: _Callable[[_type.c_double,  # animationId
                                _type.c_double],  # frameIndex
                               _type.c_double]
"""
D suffix for limited data types.
"""
PluginPreviewFrameName: _Callable[[_type.c_char_p,  # path
                                   _type.c_int],  # frameIndex
                                  _type.c_void]
"""
Displays the `Chroma` animation frame on `Chroma` hardware given the
`frameIndex`. Animaton is referenced by name.
"""
PluginReduceFrames: _Callable[[_type.c_int,  # animationId
                               _type.c_int],  # n
                              _type.c_void]
"""
Reduce the frames of the animation by removing every nth element. Animation is
referenced by id.
"""
PluginReduceFramesName: _Callable[[_type.c_char_p,  # path
                                   _type.c_int],  # n
                                  _type.c_void]
"""
Reduce the frames of the animation by removing every nth element. Animation is
referenced by name.
"""
PluginReduceFramesNameD: _Callable[[_type.c_char_p,  # path
                                    _type.c_double],  # n
                                   _type.c_double]
"""
D suffix for limited data types.
"""
PluginResetAnimation: _Callable[[_type.c_int],  # animationId
                                _type.c_int]
"""
Resets the `Chroma` animation to 1 blank frame. Returns the animation id upon
success. Returns negative one upon failure.
"""
PluginResumeAnimation: _Callable[[_type.c_int,  # animationId
                                  _type.c_bool],  # loop
                                 _type.c_void]
"""
Resume the animation with loop `ON` or `OFF` referenced by id.
"""
PluginResumeAnimationName: _Callable[[_type.c_char_p,  # path
                                      _type.c_bool],  # loop
                                     _type.c_void]
"""
Resume the animation with loop `ON` or `OFF` referenced by name.
"""
PluginResumeAnimationNameD: _Callable[[_type.c_char_p,  # path
                                       _type.c_double],  # loop
                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginReverse: _Callable[[_type.c_int],  # animationId
                         _type.c_int]
"""
Reverse the animation frame order of the `Chroma` animation. Returns the
animation id upon success. Returns negative one upon failure. Animation is
referenced by id.
"""
PluginReverseAllFrames: _Callable[[_type.c_int],  # animationId
                                  _type.c_void]
"""
Reverse the animation frame order of the `Chroma` animation. Animation is
referenced by id.
"""
PluginReverseAllFramesName: _Callable[[_type.c_char_p],  # path
                                      _type.c_void]
"""
Reverse the animation frame order of the `Chroma` animation. Animation is
referenced by name.
"""
PluginReverseAllFramesNameD: _Callable[[_type.c_char_p],  # path
                                       _type.c_double]
"""
D suffix for limited data types.
"""
PluginSaveAnimation: _Callable[[_type.c_int,  # animationId
                                _type.c_char_p],  # path
                               _type.c_int]
"""
Save the animation referenced by id to the path specified.
"""
PluginSaveAnimationName: _Callable[[_type.c_char_p,  # sourceAnimation
                                    _type.c_char_p],  # targetAnimation
                                   _type.c_int]
"""
Save the named animation to the target path specified.
"""
PluginSet1DColor: _Callable[[_type.c_int,  # animationId
                             _type.c_int,  # frameId
                             _type.c_int,  # led
                             _type.c_int],  # color
                            _type.c_void]
"""
Set the animation color for a frame given the `1D` `led`. The `led` should be
greater than or equal to 0 and less than the `MaxLeds`. The animation is
referenced by id.
"""
PluginSet1DColorName: _Callable[[_type.c_char_p,  # path
                                 _type.c_int,  # frameId
                                 _type.c_int,  # led
                                 _type.c_int],  # color
                                _type.c_void]
"""
Set the animation color for a frame given the `1D` `led`. The `led` should be
greater than or equal to 0 and less than the `MaxLeds`. The animation is
referenced by name.
"""
PluginSet1DColorNameD: _Callable[[_type.c_char_p,  # path
                                  _type.c_double,  # frameId
                                  _type.c_double,  # led
                                  _type.c_double],  # color
                                 _type.c_double]
"""
D suffix for limited data types.
"""
PluginSet2DColor: _Callable[[_type.c_int,  # animationId
                             _type.c_int,  # frameId
                             _type.c_int,  # row
                             _type.c_int,  # column
                             _type.c_int],  # color
                            _type.c_void]
"""
Set the animation color for a frame given the `2D` `row` and `column`. The `row`
should be greater than or equal to 0 and less than the `MaxRow`. The `column`
should be greater than or equal to 0 and less than the `MaxColumn`. The
animation is referenced by id.
"""
PluginSet2DColorName: _Callable[[_type.c_char_p,  # path
                                 _type.c_int,  # frameId
                                 _type.c_int,  # row
                                 _type.c_int,  # column
                                 _type.c_int],  # color
                                _type.c_void]
"""
Set the animation color for a frame given the `2D` `row` and `column`. The `row`
should be greater than or equal to 0 and less than the `MaxRow`. The `column`
should be greater than or equal to 0 and less than the `MaxColumn`. The
animation is referenced by name.
"""
PluginSet2DColorNameD: _Callable[[_type.c_char_p,  # path
                                  _type.c_double,  # frameId
                                  _type.c_double,  # rowColumnIndex
                                  _type.c_double],  # color
                                 _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetChromaCustomColorAllFrames: _Callable[[_type.c_int],  # animationId
                                               _type.c_void]
"""
When custom color is set, the custom key mode will be used. The animation is
referenced by id.
"""
PluginSetChromaCustomColorAllFramesName: _Callable[[_type.c_char_p],  # path
                                                   _type.c_void]
"""
When custom color is set, the custom key mode will be used. The animation is
referenced by name.
"""
PluginSetChromaCustomColorAllFramesNameD: _Callable[[_type.c_char_p],  # path
                                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetChromaCustomFlag: _Callable[[_type.c_int,  # animationId
                                      _type.c_bool],  # flag
                                     _type.c_void]
"""
Set the Chroma custom key color flag on all frames. `True` changes the layout
from grid to key. `True` changes the layout from key to grid. Animation is
referenced by id.
"""
PluginSetChromaCustomFlagName: _Callable[[_type.c_char_p,  # path
                                          _type.c_bool],  # flag
                                         _type.c_void]
"""
Set the Chroma custom key color flag on all frames. `True` changes the layout
from grid to key. `True` changes the layout from key to grid. Animation is
referenced by name.
"""
PluginSetChromaCustomFlagNameD: _Callable[[_type.c_char_p,  # path
                                           _type.c_double],  # flag
                                          _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetCurrentFrame: _Callable[[_type.c_int,  # animationId
                                  _type.c_int],  # frameId
                                 _type.c_void]
"""
Set the current frame of the animation referenced by id.
"""
PluginSetCurrentFrameName: _Callable[[_type.c_char_p,  # path
                                      _type.c_int],  # frameId
                                     _type.c_void]
"""
Set the current frame of the animation referenced by name.
"""
PluginSetCurrentFrameNameD: _Callable[[_type.c_char_p,  # path
                                       _type.c_double],  # frameId
                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetCustomColorFlag2D: _Callable[[_type.c_int,  # device
                                       _Pointer[_type.c_int]],  # colors
                                      _type.RZRESULT]
"""
Set the custom alpha flag on the color array
"""
PluginSetDevice: _Callable[[_type.c_int,  # animationId
                            _type.c_int,  # deviceType
                            _type.c_int],  # device
                           _type.c_int]
"""
Changes the `deviceType` and `device` of a `Chroma` animation. If the device is
changed, the `Chroma` animation will be reset with 1 blank frame. Returns the
animation id upon success. Returns negative one upon failure.
"""
PluginSetEffect: _Callable[[_Pointer[_struct.ChromaSDK.FChromaSDKGuid]],  # effectId
                           _type.RZRESULT]
"""
SetEffect will display the referenced effect id.
"""
PluginSetEffectCustom1D: _Callable[[_type.c_int,  # device
                                    _Pointer[_type.c_int]],  # colors
                                   _type.RZRESULT]
"""
SetEffectCustom1D will display the referenced colors immediately
"""
PluginSetEffectCustom2D: _Callable[[_type.c_int,  # device
                                    _Pointer[_type.c_int]],  # colors
                                   _type.RZRESULT]
"""
SetEffectCustom2D will display the referenced colors immediately.
"""
PluginSetEffectKeyboardCustom2D: _Callable[[_type.c_int,  # device
                                            _Pointer[_type.c_int],  # colors
                                            _Pointer[_type.c_int]],  # keys
                                           _type.RZRESULT]
"""
SetEffectKeyboardCustom2D will display the referenced custom keyboard colors
immediately. Colors represent a visual grid layout. Keys represent the hotkeys
for any layout.
"""
PluginSetIdleAnimation: _Callable[[_type.c_int],  # animationId
                                  _type.c_void]
"""
When the idle animation is used, the named animation will play when no other
animations are playing. Reference the animation by id.
"""
PluginSetIdleAnimationName: _Callable[[_type.c_char_p],  # path
                                      _type.c_void]
"""
When the idle animation is used, the named animation will play when no other
animations are playing. Reference the animation by name.
"""
PluginSetKeyColor: _Callable[[_type.c_int,  # animationId
                              _type.c_int,  # frameId
                              _type.c_int,  # rzkey
                              _type.c_int],  # color
                             _type.c_void]
"""
Set animation key to a static color for the given frame.
"""
PluginSetKeyColorAllFrames: _Callable[[_type.c_int,  # animationId
                                       _type.c_int,  # rzkey
                                       _type.c_int],  # color
                                      _type.c_void]
"""
Set the key to the specified key color for all frames. Animation is referenced
by id.
"""
PluginSetKeyColorAllFramesName: _Callable[[_type.c_char_p,  # path
                                           _type.c_int,  # rzkey
                                           _type.c_int],  # color
                                          _type.c_void]
"""
Set the key to the specified key color for all frames. Animation is referenced
by name.
"""
PluginSetKeyColorAllFramesNameD: _Callable[[_type.c_char_p,  # path
                                            _type.c_double,  # rzkey
                                            _type.c_double],  # color
                                           _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetKeyColorAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                          _type.c_int,  # rzkey
                                          _type.c_int,  # red
                                          _type.c_int,  # green
                                          _type.c_int],  # blue
                                         _type.c_void]
"""
Set the key to the specified key color for all frames. Animation is referenced
by id.
"""
PluginSetKeyColorAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                              _type.c_int,  # rzkey
                                              _type.c_int,  # red
                                              _type.c_int,  # green
                                              _type.c_int],  # blue
                                             _type.c_void]
"""
Set the key to the specified key color for all frames. Animation is referenced
by name.
"""
PluginSetKeyColorAllFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                               _type.c_double,  # rzkey
                                               _type.c_double,  # red
                                               _type.c_double,  # green
                                               _type.c_double],  # blue
                                              _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetKeyColorName: _Callable[[_type.c_char_p,  # path
                                  _type.c_int,  # frameId
                                  _type.c_int,  # rzkey
                                  _type.c_int],  # color
                                 _type.c_void]
"""
Set animation key to a static color for the given frame.
"""
PluginSetKeyColorNameD: _Callable[[_type.c_char_p,  # path
                                   _type.c_double,  # frameId
                                   _type.c_double,  # rzkey
                                   _type.c_double],  # color
                                  _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetKeyColorRGB: _Callable[[_type.c_int,  # animationId
                                 _type.c_int,  # frameId
                                 _type.c_int,  # rzkey
                                 _type.c_int,  # red
                                 _type.c_int,  # green
                                 _type.c_int],  # blue
                                _type.c_void]
"""
Set the key to the specified key color for the specified frame. Animation is
referenced by id.
"""
PluginSetKeyColorRGBName: _Callable[[_type.c_char_p,  # path
                                     _type.c_int,  # frameId
                                     _type.c_int,  # rzkey
                                     _type.c_int,  # red
                                     _type.c_int,  # green
                                     _type.c_int],  # blue
                                    _type.c_void]
"""
Set the key to the specified key color for the specified frame. Animation is
referenced by name.
"""
PluginSetKeyColorRGBNameD: _Callable[[_type.c_char_p,  # path
                                      _type.c_double,  # frameId
                                      _type.c_double,  # rzkey
                                      _type.c_double,  # red
                                      _type.c_double,  # green
                                      _type.c_double],  # blue
                                     _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetKeyNonZeroColor: _Callable[[_type.c_int,  # animationId
                                     _type.c_int,  # frameId
                                     _type.c_int,  # rzkey
                                     _type.c_int],  # color
                                    _type.c_void]
"""
Set animation key to a static color for the given frame if the existing color is
not already black.
"""
PluginSetKeyNonZeroColorName: _Callable[[_type.c_char_p,  # path
                                         _type.c_int,  # frameId
                                         _type.c_int,  # rzkey
                                         _type.c_int],  # color
                                        _type.c_void]
"""
Set animation key to a static color for the given frame if the existing color is
not already black.
"""
PluginSetKeyNonZeroColorNameD: _Callable[[_type.c_char_p,  # path
                                          _type.c_double,  # frameId
                                          _type.c_double,  # rzkey
                                          _type.c_double],  # color
                                         _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetKeyNonZeroColorRGB: _Callable[[_type.c_int,  # animationId
                                        _type.c_int,  # frameId
                                        _type.c_int,  # rzkey
                                        _type.c_int,  # red
                                        _type.c_int,  # green
                                        _type.c_int],  # blue
                                       _type.c_void]
"""
Set the key to the specified key color for the specified frame where color is
not black. Animation is referenced by id.
"""
PluginSetKeyNonZeroColorRGBName: _Callable[[_type.c_char_p,  # path
                                            _type.c_int,  # frameId
                                            _type.c_int,  # rzkey
                                            _type.c_int,  # red
                                            _type.c_int,  # green
                                            _type.c_int],  # blue
                                           _type.c_void]
"""
Set the key to the specified key color for the specified frame where color is
not black. Animation is referenced by name.
"""
PluginSetKeyNonZeroColorRGBNameD: _Callable[[_type.c_char_p,  # path
                                             _type.c_double,  # frameId
                                             _type.c_double,  # rzkey
                                             _type.c_double,  # red
                                             _type.c_double,  # green
                                             _type.c_double],  # blue
                                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetKeyRowColumnColorName: _Callable[[_type.c_char_p,  # path
                                           _type.c_int,  # frameId
                                           _type.c_int,  # row
                                           _type.c_int,  # column
                                           _type.c_int],  # color
                                          _type.c_void]
"""
Set animation key by row and column to a static color for the given frame.
"""
PluginSetKeysColor: _Callable[[_type.c_int,  # animationId
                               _type.c_int,  # frameId
                               _Pointer[_type.c_int],  # rzkeys
                               _type.c_int,  # keyCount
                               _type.c_int],  # color
                              _type.c_void]
"""
Set an array of animation keys to a static color for the given frame. Animation
is referenced by id.
"""
PluginSetKeysColorAllFrames: _Callable[[_type.c_int,  # animationId
                                        _Pointer[_type.c_int],  # rzkeys
                                        _type.c_int,  # keyCount
                                        _type.c_int],  # color
                                       _type.c_void]
"""
Set an array of animation keys to a static color for all frames. Animation is
referenced by id.
"""
PluginSetKeysColorAllFramesName: _Callable[[_type.c_char_p,  # path
                                            _Pointer[_type.c_int],  # rzkeys
                                            _type.c_int,  # keyCount
                                            _type.c_int],  # color
                                           _type.c_void]
"""
Set an array of animation keys to a static color for all frames. Animation is
referenced by name.
"""
PluginSetKeysColorAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                           _Pointer[_type.c_int],  # rzkeys
                                           _type.c_int,  # keyCount
                                           _type.c_int,  # red
                                           _type.c_int,  # green
                                           _type.c_int],  # blue
                                          _type.c_void]
"""
Set an array of animation keys to a static color for all frames. Animation is
referenced by id.
"""
PluginSetKeysColorAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                               _Pointer[_type.c_int],  # rzkeys
                                               _type.c_int,  # keyCount
                                               _type.c_int,  # red
                                               _type.c_int,  # green
                                               _type.c_int],  # blue
                                              _type.c_void]
"""
Set an array of animation keys to a static color for all frames. Animation is
referenced by name.
"""
PluginSetKeysColorName: _Callable[[_type.c_char_p,  # path
                                   _type.c_int,  # frameId
                                   _Pointer[_type.c_int],  # rzkeys
                                   _type.c_int,  # keyCount
                                   _type.c_int],  # color
                                  _type.c_void]
"""
Set an array of animation keys to a static color for the given frame.
"""
PluginSetKeysColorRGB: _Callable[[_type.c_int,  # animationId
                                  _type.c_int,  # frameId
                                  _Pointer[_type.c_int],  # rzkeys
                                  _type.c_int,  # keyCount
                                  _type.c_int,  # red
                                  _type.c_int,  # green
                                  _type.c_int],  # blue
                                 _type.c_void]
"""
Set an array of animation keys to a static color for the given frame. Animation
is referenced by id.
"""
PluginSetKeysColorRGBName: _Callable[[_type.c_char_p,  # path
                                      _type.c_int,  # frameId
                                      _Pointer[_type.c_int],  # rzkeys
                                      _type.c_int,  # keyCount
                                      _type.c_int,  # red
                                      _type.c_int,  # green
                                      _type.c_int],  # blue
                                     _type.c_void]
"""
Set an array of animation keys to a static color for the given frame. Animation
is referenced by name.
"""
PluginSetKeysNonZeroColor: _Callable[[_type.c_int,  # animationId
                                      _type.c_int,  # frameId
                                      _Pointer[_type.c_int],  # rzkeys
                                      _type.c_int,  # keyCount
                                      _type.c_int],  # color
                                     _type.c_void]
"""
Set an array of animation keys to a static color for the given frame if the
existing color is not already black.
"""
PluginSetKeysNonZeroColorAllFrames: _Callable[[_type.c_int,  # animationId
                                               _Pointer[_type.c_int],  # rzkeys
                                               _type.c_int,  # keyCount
                                               _type.c_int],  # color
                                              _type.c_void]
"""
Set an array of animation keys to a static color for the given frame where the
color is not black. Animation is referenced by id.
"""
PluginSetKeysNonZeroColorAllFramesName: _Callable[[_type.c_char_p,  # path
                                                   _Pointer[_type.c_int],  # rzkeys
                                                   _type.c_int,  # keyCount
                                                   _type.c_int],  # color
                                                  _type.c_void]
"""
Set an array of animation keys to a static color for all frames if the existing
color is not already black. Reference animation by name.
"""
PluginSetKeysNonZeroColorName: _Callable[[_type.c_char_p,  # path
                                          _type.c_int,  # frameId
                                          _Pointer[_type.c_int],  # rzkeys
                                          _type.c_int,  # keyCount
                                          _type.c_int],  # color
                                         _type.c_void]
"""
Set an array of animation keys to a static color for the given frame if the
existing color is not already black. Reference animation by name.
"""
PluginSetKeysNonZeroColorRGB: _Callable[[_type.c_int,  # animationId
                                         _type.c_int,  # frameId
                                         _Pointer[_type.c_int],  # rzkeys
                                         _type.c_int,  # keyCount
                                         _type.c_int,  # red
                                         _type.c_int,  # green
                                         _type.c_int],  # blue
                                        _type.c_void]
"""
Set an array of animation keys to a static color for the given frame where the
color is not black. Animation is referenced by id.
"""
PluginSetKeysNonZeroColorRGBName: _Callable[[_type.c_char_p,  # path
                                             _type.c_int,  # frameId
                                             _Pointer[_type.c_int],  # rzkeys
                                             _type.c_int,  # keyCount
                                             _type.c_int,  # red
                                             _type.c_int,  # green
                                             _type.c_int],  # blue
                                            _type.c_void]
"""
Set an array of animation keys to a static color for the given frame where the
color is not black. Animation is referenced by name.
"""
PluginSetKeysZeroColor: _Callable[[_type.c_int,  # animationId
                                   _type.c_int,  # frameId
                                   _Pointer[_type.c_int],  # rzkeys
                                   _type.c_int,  # keyCount
                                   _type.c_int],  # color
                                  _type.c_void]
"""
Set an array of animation keys to a static color for the given frame where the
color is black. Animation is referenced by id.
"""
PluginSetKeysZeroColorAllFrames: _Callable[[_type.c_int,  # animationId
                                            _Pointer[_type.c_int],  # rzkeys
                                            _type.c_int,  # keyCount
                                            _type.c_int],  # color
                                           _type.c_void]
"""
Set an array of animation keys to a static color for all frames where the color
is black. Animation is referenced by id.
"""
PluginSetKeysZeroColorAllFramesName: _Callable[[_type.c_char_p,  # path
                                                _Pointer[_type.c_int],  # rzkeys
                                                _type.c_int,  # keyCount
                                                _type.c_int],  # color
                                               _type.c_void]
"""
Set an array of animation keys to a static color for all frames where the color
is black. Animation is referenced by name.
"""
PluginSetKeysZeroColorAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                               _Pointer[_type.c_int],  # rzkeys
                                               _type.c_int,  # keyCount
                                               _type.c_int,  # red
                                               _type.c_int,  # green
                                               _type.c_int],  # blue
                                              _type.c_void]
"""
Set an array of animation keys to a static color for all frames where the color
is black. Animation is referenced by id.
"""
PluginSetKeysZeroColorAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                                   _Pointer[_type.c_int],  # rzkeys
                                                   _type.c_int,  # keyCount
                                                   _type.c_int,  # red
                                                   _type.c_int,  # green
                                                   _type.c_int],  # blue
                                                  _type.c_void]
"""
Set an array of animation keys to a static color for all frames where the color
is black. Animation is referenced by name.
"""
PluginSetKeysZeroColorName: _Callable[[_type.c_char_p,  # path
                                       _type.c_int,  # frameId
                                       _Pointer[_type.c_int],  # rzkeys
                                       _type.c_int,  # keyCount
                                       _type.c_int],  # color
                                      _type.c_void]
"""
Set an array of animation keys to a static color for the given frame where the
color is black. Animation is referenced by name.
"""
PluginSetKeysZeroColorRGB: _Callable[[_type.c_int,  # animationId
                                      _type.c_int,  # frameId
                                      _Pointer[_type.c_int],  # rzkeys
                                      _type.c_int,  # keyCount
                                      _type.c_int,  # red
                                      _type.c_int,  # green
                                      _type.c_int],  # blue
                                     _type.c_void]
"""
Set an array of animation keys to a static color for the given frame where the
color is black. Animation is referenced by id.
"""
PluginSetKeysZeroColorRGBName: _Callable[[_type.c_char_p,  # path
                                          _type.c_int,  # frameId
                                          _Pointer[_type.c_int],  # rzkeys
                                          _type.c_int,  # keyCount
                                          _type.c_int,  # red
                                          _type.c_int,  # green
                                          _type.c_int],  # blue
                                         _type.c_void]
"""
Set an array of animation keys to a static color for the given frame where the
color is black. Animation is referenced by name.
"""
PluginSetKeyZeroColor: _Callable[[_type.c_int,  # animationId
                                  _type.c_int,  # frameId
                                  _type.c_int,  # rzkey
                                  _type.c_int],  # color
                                 _type.c_void]
"""
Set animation key to a static color for the given frame where the color is
black. Animation is referenced by id.
"""
PluginSetKeyZeroColorName: _Callable[[_type.c_char_p,  # path
                                      _type.c_int,  # frameId
                                      _type.c_int,  # rzkey
                                      _type.c_int],  # color
                                     _type.c_void]
"""
Set animation key to a static color for the given frame where the color is
black. Animation is referenced by name.
"""
PluginSetKeyZeroColorNameD: _Callable[[_type.c_char_p,  # path
                                       _type.c_double,  # frameId
                                       _type.c_double,  # rzkey
                                       _type.c_double],  # color
                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetKeyZeroColorRGB: _Callable[[_type.c_int,  # animationId
                                     _type.c_int,  # frameId
                                     _type.c_int,  # rzkey
                                     _type.c_int,  # red
                                     _type.c_int,  # green
                                     _type.c_int],  # blue
                                    _type.c_void]
"""
Set animation key to a static color for the given frame where the color is
black. Animation is referenced by id.
"""
PluginSetKeyZeroColorRGBName: _Callable[[_type.c_char_p,  # path
                                         _type.c_int,  # frameId
                                         _type.c_int,  # rzkey
                                         _type.c_int,  # red
                                         _type.c_int,  # green
                                         _type.c_int],  # blue
                                        _type.c_void]
"""
Set animation key to a static color for the given frame where the color is
black. Animation is referenced by name.
"""
PluginSetKeyZeroColorRGBNameD: _Callable[[_type.c_char_p,  # path
                                          _type.c_double,  # frameId
                                          _type.c_double,  # rzkey
                                          _type.c_double,  # red
                                          _type.c_double,  # green
                                          _type.c_double],  # blue
                                         _type.c_double]
"""
D suffix for limited data types.
"""
PluginSetLogDelegate: _Callable[[_type.DebugLogPtr],  # fp
                                _type.c_void]
"""
Invokes the setup for a debug logging callback so that `stdout` is redirected to
the callback. This is used by `Unity` so that debug messages can appear in the
console window.
"""
PluginSetStaticColor: _Callable[[_type.c_int,  # deviceType
                                 _type.c_int,  # device
                                 _type.c_int],  # color
                                _type.c_void]
"""
Sets the target device to the static color.
"""
PluginSetStaticColorAll: _Callable[[_type.c_int],  # color
                                   _type.c_void]
"""
Sets all devices to the static color.
"""
PluginStaticColor: _Callable[[_type.c_int,  # deviceType
                              _type.c_int,  # device
                              _type.c_int],  # color
                             _type.c_void]
"""
Sets the target device to the static color.
"""
PluginStaticColorAll: _Callable[[_type.c_int],  # color
                                _type.c_void]
"""
Sets all devices to the static color.
"""
PluginStaticColorD: _Callable[[_type.c_double,  # deviceType
                               _type.c_double,  # device
                               _type.c_double],  # color
                              _type.c_double]
"""
D suffix for limited data types.
"""
PluginStopAll: _Callable[[],
                         _type.c_void]
"""
`PluginStopAll` will automatically stop all animations that are playing.
"""
PluginStopAnimation: _Callable[[_type.c_int],  # animationId
                               _type.c_int]
"""
Stops animation playback if in progress. Returns the animation id upon success.
Returns negative one upon failure.
"""
PluginStopAnimationD: _Callable[[_type.c_double],  # animationId
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginStopAnimationName: _Callable[[_type.c_char_p],  # path
                                   _type.c_void]
"""
`PluginStopAnimationName` automatically handles initializing the `ChromaSDK`.
The named `.chroma` animation file will be automatically opened. The animation
will stop if playing.
"""
PluginStopAnimationNameD: _Callable[[_type.c_char_p],  # path
                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginStopAnimationType: _Callable[[_type.c_int,  # deviceType
                                    _type.c_int],  # device
                                   _type.c_void]
"""
`PluginStopAnimationType` automatically handles initializing the `ChromaSDK`. If
any animation is playing for the `deviceType` and `device` combination, it will
be stopped.
"""
PluginStopAnimationTypeD: _Callable[[_type.c_double,  # deviceType
                                     _type.c_double],  # device
                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginStopComposite: _Callable[[_type.c_char_p],  # name
                               _type.c_void]
"""
`PluginStopComposite` automatically handles initializing the `ChromaSDK`. The
named animation files for the `.chroma` set will be automatically opened. The
set of animations will be stopped if playing.
"""
PluginStopCompositeD: _Callable[[_type.c_char_p],  # name
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginSubtractColor: _Callable[[_type.c_int,  # color1
                                _type.c_int],  # color2
                               _type.c_int]
"""
Return color1 - color2
"""
PluginSubtractNonZeroAllKeys: _Callable[[_type.c_int,  # sourceAnimationId
                                         _type.c_int,  # targetAnimationId
                                         _type.c_int],  # frameId
                                        _type.c_void]
"""
Subtract the source color from the target color for the frame where the target
color is not black. Source and target are referenced by id.
"""
PluginSubtractNonZeroAllKeysAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                                  _type.c_int],  # targetAnimationId
                                                 _type.c_void]
"""
Subtract the source color from the target color for all frames where the target
color is not black. Source and target are referenced by id.
"""
PluginSubtractNonZeroAllKeysAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                      _type.c_char_p],  # targetAnimation
                                                     _type.c_void]
"""
Subtract the source color from the target color for all frames where the target
color is not black. Source and target are referenced by name.
"""
PluginSubtractNonZeroAllKeysAllFramesNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                       _type.c_char_p],  # targetAnimation
                                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginSubtractNonZeroAllKeysAllFramesOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                                        _type.c_int,  # targetAnimationId
                                                        _type.c_int],  # offset
                                                       _type.c_void]
"""
Subtract the source color from the target color for all frames where the target
color is not black starting at offset for the length of the source. Source and
target are referenced by id.
"""
PluginSubtractNonZeroAllKeysAllFramesOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                            _type.c_char_p,  # targetAnimation
                                                            _type.c_int],  # offset
                                                           _type.c_void]
"""
Subtract the source color from the target color for all frames where the target
color is not black starting at offset for the length of the source. Source and
target are referenced by name.
"""
PluginSubtractNonZeroAllKeysAllFramesOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                             _type.c_char_p,  # targetAnimation
                                                             _type.c_double],  # offset
                                                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginSubtractNonZeroAllKeysName: _Callable[[_type.c_char_p,  # sourceAnimation
                                             _type.c_char_p,  # targetAnimation
                                             _type.c_int],  # frameId
                                            _type.c_void]
"""
Subtract the source color from the target color for the frame where the target
color is not black. Source and target are referenced by name.
"""
PluginSubtractNonZeroAllKeysOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                               _type.c_int,  # targetAnimationId
                                               _type.c_int,  # frameId
                                               _type.c_int],  # offset
                                              _type.c_void]
"""
Subtract the source color from the target where color is not black for the
source frame and target offset frame, reference source and target by id.
"""
PluginSubtractNonZeroAllKeysOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                   _type.c_char_p,  # targetAnimation
                                                   _type.c_int,  # frameId
                                                   _type.c_int],  # offset
                                                  _type.c_void]
"""
Subtract the source color from the target where color is not black for the
source frame and target offset frame, reference source and target by name.
"""
PluginSubtractNonZeroAllKeysOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                    _type.c_char_p,  # targetAnimation
                                                    _type.c_double,  # frameId
                                                    _type.c_double],  # offset
                                                   _type.c_double]
"""
D suffix for limited data types.
"""
PluginSubtractNonZeroTargetAllKeysAllFrames: _Callable[[_type.c_int,  # sourceAnimationId
                                                        _type.c_int],  # targetAnimationId
                                                       _type.c_void]
"""
Subtract the source color from the target color where the target color is not
black for all frames. Reference source and target by id.
"""
PluginSubtractNonZeroTargetAllKeysAllFramesName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                            _type.c_char_p],  # targetAnimation
                                                           _type.c_void]
"""
Subtract the source color from the target color where the target color is not
black for all frames. Reference source and target by name.
"""
PluginSubtractNonZeroTargetAllKeysAllFramesNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                             _type.c_char_p],  # targetAnimation
                                                            _type.c_double]
"""
D suffix for limited data types.
"""
PluginSubtractNonZeroTargetAllKeysAllFramesOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                                              _type.c_int,  # targetAnimationId
                                                              _type.c_int],  # offset
                                                             _type.c_void]
"""
Subtract the source color from the target color where the target color is not
black for all frames starting at the target offset for the length of the source.
Reference source and target by id.
"""
PluginSubtractNonZeroTargetAllKeysAllFramesOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                                  _type.c_char_p,  # targetAnimation
                                                                  _type.c_int],  # offset
                                                                 _type.c_void]
"""
Subtract the source color from the target color where the target color is not
black for all frames starting at the target offset for the length of the source.
Reference source and target by name.
"""
PluginSubtractNonZeroTargetAllKeysAllFramesOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                                   _type.c_char_p,  # targetAnimation
                                                                   _type.c_double],  # offset
                                                                  _type.c_double]
"""
D suffix for limited data types.
"""
PluginSubtractNonZeroTargetAllKeysOffset: _Callable[[_type.c_int,  # sourceAnimationId
                                                     _type.c_int,  # targetAnimationId
                                                     _type.c_int,  # frameId
                                                     _type.c_int],  # offset
                                                    _type.c_void]
"""
Subtract the source color from the target color where the target color is not
black from the source frame to the target offset frame. Reference source and
target by id.
"""
PluginSubtractNonZeroTargetAllKeysOffsetName: _Callable[[_type.c_char_p,  # sourceAnimation
                                                         _type.c_char_p,  # targetAnimation
                                                         _type.c_int,  # frameId
                                                         _type.c_int],  # offset
                                                        _type.c_void]
"""
Subtract the source color from the target color where the target color is not
black from the source frame to the target offset frame. Reference source and
target by name.
"""
PluginSubtractNonZeroTargetAllKeysOffsetNameD: _Callable[[_type.c_char_p,  # sourceAnimation
                                                          _type.c_char_p,  # targetAnimation
                                                          _type.c_double,  # frameId
                                                          _type.c_double],  # offset
                                                         _type.c_double]
"""
D suffix for limited data types.
"""
PluginSubtractThresholdColorsMinMaxAllFramesRGB: _Callable[[_type.c_int,  # animationId
                                                            _type.c_int,  # minThreshold
                                                            _type.c_int,  # minRed
                                                            _type.c_int,  # minGreen
                                                            _type.c_int,  # minBlue
                                                            _type.c_int,  # maxThreshold
                                                            _type.c_int,  # maxRed
                                                            _type.c_int,  # maxGreen
                                                            _type.c_int],  # maxBlue
                                                           _type.c_void]
"""
Subtract all frames with the min RGB color where the animation color is less
than the min threshold AND with the max RGB color where the animation is more
than the max threshold. Animation is referenced by id.
"""
PluginSubtractThresholdColorsMinMaxAllFramesRGBName: _Callable[[_type.c_char_p,  # path
                                                                _type.c_int,  # minThreshold
                                                                _type.c_int,  # minRed
                                                                _type.c_int,  # minGreen
                                                                _type.c_int,  # minBlue
                                                                _type.c_int,  # maxThreshold
                                                                _type.c_int,  # maxRed
                                                                _type.c_int,  # maxGreen
                                                                _type.c_int],  # maxBlue
                                                               _type.c_void]
"""
Subtract all frames with the min RGB color where the animation color is less
than the min threshold AND with the max RGB color where the animation is more
than the max threshold. Animation is referenced by name.
"""
PluginSubtractThresholdColorsMinMaxAllFramesRGBNameD: _Callable[[_type.c_char_p,  # path
                                                                 _type.c_double,  # minThreshold
                                                                 _type.c_double,  # minRed
                                                                 _type.c_double,  # minGreen
                                                                 _type.c_double,  # minBlue
                                                                 _type.c_double,  # maxThreshold
                                                                 _type.c_double,  # maxRed
                                                                 _type.c_double,  # maxGreen
                                                                 _type.c_double],  # maxBlue
                                                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginSubtractThresholdColorsMinMaxRGB: _Callable[[_type.c_int,  # animationId
                                                   _type.c_int,  # frameId
                                                   _type.c_int,  # minThreshold
                                                   _type.c_int,  # minRed
                                                   _type.c_int,  # minGreen
                                                   _type.c_int,  # minBlue
                                                   _type.c_int,  # maxThreshold
                                                   _type.c_int,  # maxRed
                                                   _type.c_int,  # maxGreen
                                                   _type.c_int],  # maxBlue
                                                  _type.c_void]
"""
Subtract the specified frame with the min RGB color where the animation color is
less than the min threshold AND with the max RGB color where the animation is
more than the max threshold. Animation is referenced by id.
"""
PluginSubtractThresholdColorsMinMaxRGBName: _Callable[[_type.c_char_p,  # path
                                                       _type.c_int,  # frameId
                                                       _type.c_int,  # minThreshold
                                                       _type.c_int,  # minRed
                                                       _type.c_int,  # minGreen
                                                       _type.c_int,  # minBlue
                                                       _type.c_int,  # maxThreshold
                                                       _type.c_int,  # maxRed
                                                       _type.c_int,  # maxGreen
                                                       _type.c_int],  # maxBlue
                                                      _type.c_void]
"""
Subtract the specified frame with the min RGB color where the animation color is
less than the min threshold AND with the max RGB color where the animation is
more than the max threshold. Animation is referenced by name.
"""
PluginSubtractThresholdColorsMinMaxRGBNameD: _Callable[[_type.c_char_p,  # path
                                                        _type.c_int,  # frameId
                                                        _type.c_int,  # minThreshold
                                                        _type.c_int,  # minRed
                                                        _type.c_int,  # minGreen
                                                        _type.c_int,  # minBlue
                                                        _type.c_int,  # maxThreshold
                                                        _type.c_int,  # maxRed
                                                        _type.c_int,  # maxGreen
                                                        _type.c_int],  # maxBlue
                                                       _type.c_double]
"""
D suffix for limited data types.
"""
PluginTrimEndFrames: _Callable[[_type.c_int,  # animationId
                                _type.c_int],  # lastFrameId
                               _type.c_void]
"""
Trim the end of the animation. The length of the animation will be the
lastFrameId plus one. Reference the animation by id.
"""
PluginTrimEndFramesName: _Callable[[_type.c_char_p,  # path
                                    _type.c_int],  # lastFrameId
                                   _type.c_void]
"""
Trim the end of the animation. The length of the animation will be the
lastFrameId plus one. Reference the animation by name.
"""
PluginTrimEndFramesNameD: _Callable[[_type.c_char_p,  # path
                                     _type.c_double],  # lastFrameId
                                    _type.c_double]
"""
D suffix for limited data types.
"""
PluginTrimFrame: _Callable[[_type.c_int,  # animationId
                            _type.c_int],  # frameId
                           _type.c_void]
"""
Remove the frame from the animation. Reference animation by id.
"""
PluginTrimFrameName: _Callable[[_type.c_char_p,  # path
                                _type.c_int],  # frameId
                               _type.c_void]
"""
Remove the frame from the animation. Reference animation by name.
"""
PluginTrimFrameNameD: _Callable[[_type.c_char_p,  # path
                                 _type.c_double],  # frameId
                                _type.c_double]
"""
D suffix for limited data types.
"""
PluginTrimStartFrames: _Callable[[_type.c_int,  # animationId
                                  _type.c_int],  # numberOfFrames
                                 _type.c_void]
"""
Trim the start of the animation starting at frame 0 for the number of frames.
Reference the animation by id.
"""
PluginTrimStartFramesName: _Callable[[_type.c_char_p,  # path
                                      _type.c_int],  # numberOfFrames
                                     _type.c_void]
"""
Trim the start of the animation starting at frame 0 for the number of frames.
Reference the animation by name.
"""
PluginTrimStartFramesNameD: _Callable[[_type.c_char_p,  # path
                                       _type.c_double],  # numberOfFrames
                                      _type.c_double]
"""
D suffix for limited data types.
"""
PluginUninit: _Callable[[],
                        _type.RZRESULT]
"""
Uninitializes the `ChromaSDK`. Returns 0 upon success. Returns negative one upon
failure.
"""
PluginUninitD: _Callable[[],
                         _type.c_double]
"""
D suffix for limited data types.
"""
PluginUnloadAnimation: _Callable[[_type.c_int],  # animationId
                                 _type.c_int]
"""
Unloads `Chroma` effects to free up resources. Returns the animation id upon
success. Returns negative one upon failure. Reference the animation by id.
"""
PluginUnloadAnimationD: _Callable[[_type.c_double],  # animationId
                                  _type.c_double]
"""
D suffix for limited data types.
"""
PluginUnloadAnimationName: _Callable[[_type.c_char_p],  # path
                                     _type.c_void]
"""
Unload the animation effects. Reference the animation by name.
"""
PluginUnloadComposite: _Callable[[_type.c_char_p],  # name
                                 _type.c_void]
"""
Unload the the composite set of animation effects. Reference the animation by
name.
"""
PluginUnloadLibrarySDK: _Callable[[],
                                  _type.c_void]
"""
Unload the Razer Chroma SDK Library before exiting the application.
"""
PluginUnloadLibraryStreamingPlugin: _Callable[[],
                                              _type.c_void]
"""
Unload the Razer Chroma Streaming Plugin Library before exiting the application.
"""
PluginUpdateFrame: _Callable[[_type.c_int,  # animationId
                              _type.c_int,  # frameIndex
                              _type.c_float,  # duration
                              _Pointer[_type.c_int],  # colors
                              _type.c_int,  # length
                              _Pointer[_type.c_int],  # keys
                              _type.c_int],  # keysLength
                             _type.c_int]
"""
Updates the `frameIndex` of the `Chroma` animation referenced by id and sets the
`duration` (in seconds). The `color` is expected to be an array of the
dimensions for the `deviceType/device`. The `length` parameter is the size of
the `color` array. For `EChromaSDKDevice1DEnum` the array size should be `MAX
LEDS`. For `EChromaSDKDevice2DEnum` the array size should be `MAX ROW` times
`MAX COLUMN`. Keys are populated only for EChromaSDKDevice2DEnum.DE_Keyboard
and EChromaSDKDevice2DEnum.DE_KeyboardExtended. Keys will only use the
EChromaSDKDevice2DEnum.DE_Keyboard `MAX_ROW` times `MAX_COLUMN` keysLength.
"""
PluginUpdateFrameName: _Callable[[_type.c_char_p,  # path
                                  _type.c_int,  # frameIndex
                                  _type.c_float,  # duration
                                  _Pointer[_type.c_int],  # colors
                                  _type.c_int,  # length
                                  _Pointer[_type.c_int],  # keys
                                  _type.c_int],  # keysLength
                                 _type.c_int]
"""
Update the `frameIndex` of the `Chroma` animation referenced by name and sets
the `duration` (in seconds). The `color` is expected to be an array of the
dimensions for the `deviceType/device`. The `length` parameter is the size of
the `color` array. For `EChromaSDKDevice1DEnum` the array size should be `MAX
LEDS`. For `EChromaSDKDevice2DEnum` the array size should be `MAX ROW` times
`MAX COLUMN`. Keys are populated only for EChromaSDKDevice2DEnum.DE_Keyboard
and EChromaSDKDevice2DEnum.DE_KeyboardExtended. Keys will only use the
EChromaSDKDevice2DEnum.DE_Keyboard `MAX_ROW` times `MAX_COLUMN` keysLength.
Returns the animation id upon success. Returns negative one upon failure.
"""
PluginUseIdleAnimation: _Callable[[_type.c_int,  # device
                                   _type.c_bool],  # flag
                                  _type.c_void]
"""
When the idle animation flag is true, when no other animations are playing, the
idle animation will be used. The idle animation will not be affected by the API
calls to PluginIsPlaying, PluginStopAnimationType, PluginGetPlayingAnimationId,
and PluginGetPlayingAnimationCount. Then the idle animation flag is false, the
idle animation is disabled. `Device` uses `EChromaSDKDeviceEnum` enums.
"""
PluginUseIdleAnimations: _Callable[[_type.c_bool],  # flag
                                   _type.c_void]
"""
Set idle animation flag for all devices.
"""
PluginUsePreloading: _Callable[[_type.c_int,  # animationId
                                _type.c_bool],  # flag
                               _type.c_void]
"""
Set preloading animation flag, which is set to true by default. Reference
animation by id.
"""
PluginUsePreloadingName: _Callable[[_type.c_char_p,  # path
                                    _type.c_bool],  # flag
                                   _type.c_void]
"""
Set preloading animation flag, which is set to true by default. Reference
animation by name.
"""

_WinLib(__name__)

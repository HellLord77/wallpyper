from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import type as _type
from .._utils import _Pointer

# GL
glAccum: _Callable[[_type.GLenum,  # op
                    _type.GLfloat],  # value
                   _type.c_int]
glAlphaFunc: _Callable[[_type.GLenum,  # func
                        _type.GLclampf],  # ref
                       _type.c_int]
glArrayElement: _Callable[[_type.GLint],  # i
                          _type.c_int]
glBegin: _Callable[[_type.GLenum],  # mode
                   _type.c_int]
glBindTexture: _Callable[[_type.GLenum,  # target
                          _type.GLuint],  # texture
                         _type.c_int]
glBitmap: _Callable[[_type.GLsizei,  # width
                     _type.GLsizei,  # height
                     _type.GLfloat,  # xorig
                     _type.GLfloat,  # yorig
                     _type.GLfloat,  # xmove
                     _type.GLfloat,  # ymove
                     _Pointer[_type.GLubyte]],  # bitmap
                    _type.c_int]
glBlendFunc: _Callable[[_type.GLenum,  # sfactor
                        _type.GLenum],  # dfactor
                       _type.c_int]
glCallList: _Callable[[_type.GLuint],  # list
                      _type.c_int]
glCallLists: _Callable[[_type.GLsizei,  # n
                        _type.GLenum,  # type
                        _Pointer[_type.GLvoid]],  # lists
                       _type.c_int]
glClear: _Callable[[_type.GLbitfield],  # mask
                   _type.c_int]
glClearAccum: _Callable[[_type.GLfloat,  # red
                         _type.GLfloat,  # green
                         _type.GLfloat,  # blue
                         _type.GLfloat],  # alpha
                        _type.c_int]
glClearColor: _Callable[[_type.GLclampf,  # red
                         _type.GLclampf,  # green
                         _type.GLclampf,  # blue
                         _type.GLclampf],  # alpha
                        _type.c_int]
glClearDepth: _Callable[[_type.GLclampd],  # depth
                        _type.c_int]
glClearIndex: _Callable[[_type.GLfloat],  # c
                        _type.c_int]
glClearStencil: _Callable[[_type.GLint],  # s
                          _type.c_int]
glClipPlane: _Callable[[_type.GLenum,  # plane
                        _Pointer[_type.GLdouble]],  # equation
                       _type.c_int]
glColor3b: _Callable[[_type.GLbyte,  # red
                      _type.GLbyte,  # green
                      _type.GLbyte],  # blue
                     _type.c_int]
glColor3bv: _Callable[[_Pointer[_type.GLbyte]],  # v
                      _type.c_int]
glColor3d: _Callable[[_type.GLdouble,  # red
                      _type.GLdouble,  # green
                      _type.GLdouble],  # blue
                     _type.c_int]
glColor3dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                      _type.c_int]
glColor3f: _Callable[[_type.GLfloat,  # red
                      _type.GLfloat,  # green
                      _type.GLfloat],  # blue
                     _type.c_int]
glColor3fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                      _type.c_int]
glColor3i: _Callable[[_type.GLint,  # red
                      _type.GLint,  # green
                      _type.GLint],  # blue
                     _type.c_int]
glColor3iv: _Callable[[_Pointer[_type.GLint]],  # v
                      _type.c_int]
glColor3s: _Callable[[_type.GLshort,  # red
                      _type.GLshort,  # green
                      _type.GLshort],  # blue
                     _type.c_int]
glColor3sv: _Callable[[_Pointer[_type.GLshort]],  # v
                      _type.c_int]
glColor3ub: _Callable[[_type.GLubyte,  # red
                       _type.GLubyte,  # green
                       _type.GLubyte],  # blue
                      _type.c_int]
glColor3ubv: _Callable[[_Pointer[_type.GLubyte]],  # v
                       _type.c_int]
glColor3ui: _Callable[[_type.GLuint,  # red
                       _type.GLuint,  # green
                       _type.GLuint],  # blue
                      _type.c_int]
glColor3uiv: _Callable[[_Pointer[_type.GLuint]],  # v
                       _type.c_int]
glColor3us: _Callable[[_type.GLushort,  # red
                       _type.GLushort,  # green
                       _type.GLushort],  # blue
                      _type.c_int]
glColor3usv: _Callable[[_Pointer[_type.GLushort]],  # v
                       _type.c_int]
glColor4b: _Callable[[_type.GLbyte,  # red
                      _type.GLbyte,  # green
                      _type.GLbyte,  # blue
                      _type.GLbyte],  # alpha
                     _type.c_int]
glColor4bv: _Callable[[_Pointer[_type.GLbyte]],  # v
                      _type.c_int]
glColor4d: _Callable[[_type.GLdouble,  # red
                      _type.GLdouble,  # green
                      _type.GLdouble,  # blue
                      _type.GLdouble],  # alpha
                     _type.c_int]
glColor4dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                      _type.c_int]
glColor4f: _Callable[[_type.GLfloat,  # red
                      _type.GLfloat,  # green
                      _type.GLfloat,  # blue
                      _type.GLfloat],  # alpha
                     _type.c_int]
glColor4fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                      _type.c_int]
glColor4i: _Callable[[_type.GLint,  # red
                      _type.GLint,  # green
                      _type.GLint,  # blue
                      _type.GLint],  # alpha
                     _type.c_int]
glColor4iv: _Callable[[_Pointer[_type.GLint]],  # v
                      _type.c_int]
glColor4s: _Callable[[_type.GLshort,  # red
                      _type.GLshort,  # green
                      _type.GLshort,  # blue
                      _type.GLshort],  # alpha
                     _type.c_int]
glColor4sv: _Callable[[_Pointer[_type.GLshort]],  # v
                      _type.c_int]
glColor4ub: _Callable[[_type.GLubyte,  # red
                       _type.GLubyte,  # green
                       _type.GLubyte,  # blue
                       _type.GLubyte],  # alpha
                      _type.c_int]
glColor4ubv: _Callable[[_Pointer[_type.GLubyte]],  # v
                       _type.c_int]
glColor4ui: _Callable[[_type.GLuint,  # red
                       _type.GLuint,  # green
                       _type.GLuint,  # blue
                       _type.GLuint],  # alpha
                      _type.c_int]
glColor4uiv: _Callable[[_Pointer[_type.GLuint]],  # v
                       _type.c_int]
glColor4us: _Callable[[_type.GLushort,  # red
                       _type.GLushort,  # green
                       _type.GLushort,  # blue
                       _type.GLushort],  # alpha
                      _type.c_int]
glColor4usv: _Callable[[_Pointer[_type.GLushort]],  # v
                       _type.c_int]
glColorMask: _Callable[[_type.GLboolean,  # red
                        _type.GLboolean,  # green
                        _type.GLboolean,  # blue
                        _type.GLboolean],  # alpha
                       _type.c_int]
glColorMaterial: _Callable[[_type.GLenum,  # face
                            _type.GLenum],  # mode
                           _type.c_int]
glColorPointer: _Callable[[_type.GLint,  # size
                           _type.GLenum,  # type
                           _type.GLsizei,  # stride
                           _Pointer[_type.GLvoid]],  # pointer
                          _type.c_int]
glCopyPixels: _Callable[[_type.GLint,  # x
                         _type.GLint,  # y
                         _type.GLsizei,  # width
                         _type.GLsizei,  # height
                         _type.GLenum],  # type
                        _type.c_int]
glCopyTexImage1D: _Callable[[_type.GLenum,  # target
                             _type.GLint,  # level
                             _type.GLenum,  # internalFormat
                             _type.GLint,  # x
                             _type.GLint,  # y
                             _type.GLsizei,  # width
                             _type.GLint],  # border
                            _type.c_int]
glCopyTexImage2D: _Callable[[_type.GLenum,  # target
                             _type.GLint,  # level
                             _type.GLenum,  # internalFormat
                             _type.GLint,  # x
                             _type.GLint,  # y
                             _type.GLsizei,  # width
                             _type.GLsizei,  # height
                             _type.GLint],  # border
                            _type.c_int]
glCopyTexSubImage1D: _Callable[[_type.GLenum,  # target
                                _type.GLint,  # level
                                _type.GLint,  # xoffset
                                _type.GLint,  # x
                                _type.GLint,  # y
                                _type.GLsizei],  # width
                               _type.c_int]
glCopyTexSubImage2D: _Callable[[_type.GLenum,  # target
                                _type.GLint,  # level
                                _type.GLint,  # xoffset
                                _type.GLint,  # yoffset
                                _type.GLint,  # x
                                _type.GLint,  # y
                                _type.GLsizei,  # width
                                _type.GLsizei],  # height
                               _type.c_int]
glCullFace: _Callable[[_type.GLenum],  # mode
                      _type.c_int]
glDeleteLists: _Callable[[_type.GLuint,  # list
                          _type.GLsizei],  # range
                         _type.c_int]
glDeleteTextures: _Callable[[_type.GLsizei,  # n
                             _Pointer[_type.GLuint]],  # textures
                            _type.c_int]
glDepthFunc: _Callable[[_type.GLenum],  # func
                       _type.c_int]
glDepthMask: _Callable[[_type.GLboolean],  # flag
                       _type.c_int]
glDepthRange: _Callable[[_type.GLclampd,  # zNear
                         _type.GLclampd],  # zFar
                        _type.c_int]
glDisable: _Callable[[_type.GLenum],  # cap
                     _type.c_int]
glDisableClientState: _Callable[[_type.GLenum],  # array
                                _type.c_int]
glDrawArrays: _Callable[[_type.GLenum,  # mode
                         _type.GLint,  # first
                         _type.GLsizei],  # count
                        _type.c_int]
glDrawBuffer: _Callable[[_type.GLenum],  # mode
                        _type.c_int]
glDrawElements: _Callable[[_type.GLenum,  # mode
                           _type.GLsizei,  # count
                           _type.GLenum,  # type
                           _Pointer[_type.GLvoid]],  # indices
                          _type.c_int]
glDrawPixels: _Callable[[_type.GLsizei,  # width
                         _type.GLsizei,  # height
                         _type.GLenum,  # format
                         _type.GLenum,  # type
                         _Pointer[_type.GLvoid]],  # pixels
                        _type.c_int]
glEdgeFlag: _Callable[[_type.GLboolean],  # flag
                      _type.c_int]
glEdgeFlagPointer: _Callable[[_type.GLsizei,  # stride
                              _Pointer[_type.GLvoid]],  # pointer
                             _type.c_int]
glEdgeFlagv: _Callable[[_Pointer[_type.GLboolean]],  # flag
                       _type.c_int]
glEnable: _Callable[[_type.GLenum],  # cap
                    _type.c_int]
glEnableClientState: _Callable[[_type.GLenum],  # array
                               _type.c_int]
glEnd: _Callable[[],
                 _type.c_int]
glEndList: _Callable[[],
                     _type.c_int]
glEvalCoord1d: _Callable[[_type.GLdouble],  # u
                         _type.c_int]
glEvalCoord1dv: _Callable[[_Pointer[_type.GLdouble]],  # u
                          _type.c_int]
glEvalCoord1f: _Callable[[_type.GLfloat],  # u
                         _type.c_int]
glEvalCoord1fv: _Callable[[_Pointer[_type.GLfloat]],  # u
                          _type.c_int]
glEvalCoord2d: _Callable[[_type.GLdouble,  # u
                          _type.GLdouble],  # v
                         _type.c_int]
glEvalCoord2dv: _Callable[[_Pointer[_type.GLdouble]],  # u
                          _type.c_int]
glEvalCoord2f: _Callable[[_type.GLfloat,  # u
                          _type.GLfloat],  # v
                         _type.c_int]
glEvalCoord2fv: _Callable[[_Pointer[_type.GLfloat]],  # u
                          _type.c_int]
glEvalMesh1: _Callable[[_type.GLenum,  # mode
                        _type.GLint,  # i1
                        _type.GLint],  # i2
                       _type.c_int]
glEvalMesh2: _Callable[[_type.GLenum,  # mode
                        _type.GLint,  # i1
                        _type.GLint,  # i2
                        _type.GLint,  # j1
                        _type.GLint],  # j2
                       _type.c_int]
glEvalPoint1: _Callable[[_type.GLint],  # i
                        _type.c_int]
glEvalPoint2: _Callable[[_type.GLint,  # i
                         _type.GLint],  # j
                        _type.c_int]
glFeedbackBuffer: _Callable[[_type.GLsizei,  # size
                             _type.GLenum,  # type
                             _Pointer[_type.GLfloat]],  # buffer
                            _type.c_int]
glFinish: _Callable[[],
                    _type.c_int]
glFlush: _Callable[[],
                   _type.c_int]
glFogf: _Callable[[_type.GLenum,  # pname
                   _type.GLfloat],  # param
                  _type.c_int]
glFogfv: _Callable[[_type.GLenum,  # pname
                    _Pointer[_type.GLfloat]],  # params
                   _type.c_int]
glFogi: _Callable[[_type.GLenum,  # pname
                   _type.GLint],  # param
                  _type.c_int]
glFogiv: _Callable[[_type.GLenum,  # pname
                    _Pointer[_type.GLint]],  # params
                   _type.c_int]
glFrontFace: _Callable[[_type.GLenum],  # mode
                       _type.c_int]
glFrustum: _Callable[[_type.GLdouble,  # left
                      _type.GLdouble,  # right
                      _type.GLdouble,  # bottom
                      _type.GLdouble,  # top
                      _type.GLdouble,  # zNear
                      _type.GLdouble],  # zFar
                     _type.c_int]
glGenTextures: _Callable[[_type.GLsizei,  # n
                          _Pointer[_type.GLuint]],  # textures
                         _type.c_int]
glGetBooleanv: _Callable[[_type.GLenum,  # pname
                          _Pointer[_type.GLboolean]],  # params
                         _type.c_int]
glGetClipPlane: _Callable[[_type.GLenum,  # plane
                           _Pointer[_type.GLdouble]],  # equation
                          _type.c_int]
glGetDoublev: _Callable[[_type.GLenum,  # pname
                         _Pointer[_type.GLdouble]],  # params
                        _type.c_int]
glGetFloatv: _Callable[[_type.GLenum,  # pname
                        _Pointer[_type.GLfloat]],  # params
                       _type.c_int]
glGetIntegerv: _Callable[[_type.GLenum,  # pname
                          _Pointer[_type.GLint]],  # params
                         _type.c_int]
glGetLightfv: _Callable[[_type.GLenum,  # light
                         _type.GLenum,  # pname
                         _Pointer[_type.GLfloat]],  # params
                        _type.c_int]
glGetLightiv: _Callable[[_type.GLenum,  # light
                         _type.GLenum,  # pname
                         _Pointer[_type.GLint]],  # params
                        _type.c_int]
glGetMapdv: _Callable[[_type.GLenum,  # target
                       _type.GLenum,  # query
                       _Pointer[_type.GLdouble]],  # v
                      _type.c_int]
glGetMapfv: _Callable[[_type.GLenum,  # target
                       _type.GLenum,  # query
                       _Pointer[_type.GLfloat]],  # v
                      _type.c_int]
glGetMapiv: _Callable[[_type.GLenum,  # target
                       _type.GLenum,  # query
                       _Pointer[_type.GLint]],  # v
                      _type.c_int]
glGetMaterialfv: _Callable[[_type.GLenum,  # face
                            _type.GLenum,  # pname
                            _Pointer[_type.GLfloat]],  # params
                           _type.c_int]
glGetMaterialiv: _Callable[[_type.GLenum,  # face
                            _type.GLenum,  # pname
                            _Pointer[_type.GLint]],  # params
                           _type.c_int]
glGetPixelMapfv: _Callable[[_type.GLenum,  # map
                            _Pointer[_type.GLfloat]],  # values
                           _type.c_int]
glGetPixelMapuiv: _Callable[[_type.GLenum,  # map
                             _Pointer[_type.GLuint]],  # values
                            _type.c_int]
glGetPixelMapusv: _Callable[[_type.GLenum,  # map
                             _Pointer[_type.GLushort]],  # values
                            _type.c_int]
glGetPointerv: _Callable[[_type.GLenum,  # pname
                          _Pointer[_Pointer[_type.GLvoid]]],  # params
                         _type.c_int]
glGetPolygonStipple: _Callable[[_Pointer[_type.GLubyte]],  # mask
                               _type.c_int]
glGetTexEnvfv: _Callable[[_type.GLenum,  # target
                          _type.GLenum,  # pname
                          _Pointer[_type.GLfloat]],  # params
                         _type.c_int]
glGetTexEnviv: _Callable[[_type.GLenum,  # target
                          _type.GLenum,  # pname
                          _Pointer[_type.GLint]],  # params
                         _type.c_int]
glGetTexGendv: _Callable[[_type.GLenum,  # coord
                          _type.GLenum,  # pname
                          _Pointer[_type.GLdouble]],  # params
                         _type.c_int]
glGetTexGenfv: _Callable[[_type.GLenum,  # coord
                          _type.GLenum,  # pname
                          _Pointer[_type.GLfloat]],  # params
                         _type.c_int]
glGetTexGeniv: _Callable[[_type.GLenum,  # coord
                          _type.GLenum,  # pname
                          _Pointer[_type.GLint]],  # params
                         _type.c_int]
glGetTexImage: _Callable[[_type.GLenum,  # target
                          _type.GLint,  # level
                          _type.GLenum,  # format
                          _type.GLenum,  # type
                          _Pointer[_type.GLvoid]],  # pixels
                         _type.c_int]
glGetTexLevelParameterfv: _Callable[[_type.GLenum,  # target
                                     _type.GLint,  # level
                                     _type.GLenum,  # pname
                                     _Pointer[_type.GLfloat]],  # params
                                    _type.c_int]
glGetTexLevelParameteriv: _Callable[[_type.GLenum,  # target
                                     _type.GLint,  # level
                                     _type.GLenum,  # pname
                                     _Pointer[_type.GLint]],  # params
                                    _type.c_int]
glGetTexParameterfv: _Callable[[_type.GLenum,  # target
                                _type.GLenum,  # pname
                                _Pointer[_type.GLfloat]],  # params
                               _type.c_int]
glGetTexParameteriv: _Callable[[_type.GLenum,  # target
                                _type.GLenum,  # pname
                                _Pointer[_type.GLint]],  # params
                               _type.c_int]
glHint: _Callable[[_type.GLenum,  # target
                   _type.GLenum],  # mode
                  _type.c_int]
glIndexMask: _Callable[[_type.GLuint],  # mask
                       _type.c_int]
glIndexPointer: _Callable[[_type.GLenum,  # type
                           _type.GLsizei,  # stride
                           _Pointer[_type.GLvoid]],  # pointer
                          _type.c_int]
glIndexd: _Callable[[_type.GLdouble],  # c
                    _type.c_int]
glIndexdv: _Callable[[_Pointer[_type.GLdouble]],  # c
                     _type.c_int]
glIndexf: _Callable[[_type.GLfloat],  # c
                    _type.c_int]
glIndexfv: _Callable[[_Pointer[_type.GLfloat]],  # c
                     _type.c_int]
glIndexi: _Callable[[_type.GLint],  # c
                    _type.c_int]
glIndexiv: _Callable[[_Pointer[_type.GLint]],  # c
                     _type.c_int]
glIndexs: _Callable[[_type.GLshort],  # c
                    _type.c_int]
glIndexsv: _Callable[[_Pointer[_type.GLshort]],  # c
                     _type.c_int]
glIndexub: _Callable[[_type.GLubyte],  # c
                     _type.c_int]
glIndexubv: _Callable[[_Pointer[_type.GLubyte]],  # c
                      _type.c_int]
glInitNames: _Callable[[],
                       _type.c_int]
glInterleavedArrays: _Callable[[_type.GLenum,  # format
                                _type.GLsizei,  # stride
                                _Pointer[_type.GLvoid]],  # pointer
                               _type.c_int]
glLightModelf: _Callable[[_type.GLenum,  # pname
                          _type.GLfloat],  # param
                         _type.c_int]
glLightModelfv: _Callable[[_type.GLenum,  # pname
                           _Pointer[_type.GLfloat]],  # params
                          _type.c_int]
glLightModeli: _Callable[[_type.GLenum,  # pname
                          _type.GLint],  # param
                         _type.c_int]
glLightModeliv: _Callable[[_type.GLenum,  # pname
                           _Pointer[_type.GLint]],  # params
                          _type.c_int]
glLightf: _Callable[[_type.GLenum,  # light
                     _type.GLenum,  # pname
                     _type.GLfloat],  # param
                    _type.c_int]
glLightfv: _Callable[[_type.GLenum,  # light
                      _type.GLenum,  # pname
                      _Pointer[_type.GLfloat]],  # params
                     _type.c_int]
glLighti: _Callable[[_type.GLenum,  # light
                     _type.GLenum,  # pname
                     _type.GLint],  # param
                    _type.c_int]
glLightiv: _Callable[[_type.GLenum,  # light
                      _type.GLenum,  # pname
                      _Pointer[_type.GLint]],  # params
                     _type.c_int]
glLineStipple: _Callable[[_type.GLint,  # factor
                          _type.GLushort],  # pattern
                         _type.c_int]
glLineWidth: _Callable[[_type.GLfloat],  # width
                       _type.c_int]
glListBase: _Callable[[_type.GLuint],  # base
                      _type.c_int]
glLoadIdentity: _Callable[[],
                          _type.c_int]
glLoadMatrixd: _Callable[[_Pointer[_type.GLdouble]],  # m
                         _type.c_int]
glLoadMatrixf: _Callable[[_Pointer[_type.GLfloat]],  # m
                         _type.c_int]
glLoadName: _Callable[[_type.GLuint],  # name
                      _type.c_int]
glLogicOp: _Callable[[_type.GLenum],  # opcode
                     _type.c_int]
glMap1d: _Callable[[_type.GLenum,  # target
                    _type.GLdouble,  # u1
                    _type.GLdouble,  # u2
                    _type.GLint,  # stride
                    _type.GLint,  # order
                    _Pointer[_type.GLdouble]],  # points
                   _type.c_int]
glMap1f: _Callable[[_type.GLenum,  # target
                    _type.GLfloat,  # u1
                    _type.GLfloat,  # u2
                    _type.GLint,  # stride
                    _type.GLint,  # order
                    _Pointer[_type.GLfloat]],  # points
                   _type.c_int]
glMap2d: _Callable[[_type.GLenum,  # target
                    _type.GLdouble,  # u1
                    _type.GLdouble,  # u2
                    _type.GLint,  # ustride
                    _type.GLint,  # uorder
                    _type.GLdouble,  # v1
                    _type.GLdouble,  # v2
                    _type.GLint,  # vstride
                    _type.GLint,  # vorder
                    _Pointer[_type.GLdouble]],  # points
                   _type.c_int]
glMap2f: _Callable[[_type.GLenum,  # target
                    _type.GLfloat,  # u1
                    _type.GLfloat,  # u2
                    _type.GLint,  # ustride
                    _type.GLint,  # uorder
                    _type.GLfloat,  # v1
                    _type.GLfloat,  # v2
                    _type.GLint,  # vstride
                    _type.GLint,  # vorder
                    _Pointer[_type.GLfloat]],  # points
                   _type.c_int]
glMapGrid1d: _Callable[[_type.GLint,  # un
                        _type.GLdouble,  # u1
                        _type.GLdouble],  # u2
                       _type.c_int]
glMapGrid1f: _Callable[[_type.GLint,  # un
                        _type.GLfloat,  # u1
                        _type.GLfloat],  # u2
                       _type.c_int]
glMapGrid2d: _Callable[[_type.GLint,  # un
                        _type.GLdouble,  # u1
                        _type.GLdouble,  # u2
                        _type.GLint,  # vn
                        _type.GLdouble,  # v1
                        _type.GLdouble],  # v2
                       _type.c_int]
glMapGrid2f: _Callable[[_type.GLint,  # un
                        _type.GLfloat,  # u1
                        _type.GLfloat,  # u2
                        _type.GLint,  # vn
                        _type.GLfloat,  # v1
                        _type.GLfloat],  # v2
                       _type.c_int]
glMaterialf: _Callable[[_type.GLenum,  # face
                        _type.GLenum,  # pname
                        _type.GLfloat],  # param
                       _type.c_int]
glMaterialfv: _Callable[[_type.GLenum,  # face
                         _type.GLenum,  # pname
                         _Pointer[_type.GLfloat]],  # params
                        _type.c_int]
glMateriali: _Callable[[_type.GLenum,  # face
                        _type.GLenum,  # pname
                        _type.GLint],  # param
                       _type.c_int]
glMaterialiv: _Callable[[_type.GLenum,  # face
                         _type.GLenum,  # pname
                         _Pointer[_type.GLint]],  # params
                        _type.c_int]
glMatrixMode: _Callable[[_type.GLenum],  # mode
                        _type.c_int]
glMultMatrixd: _Callable[[_Pointer[_type.GLdouble]],  # m
                         _type.c_int]
glMultMatrixf: _Callable[[_Pointer[_type.GLfloat]],  # m
                         _type.c_int]
glNewList: _Callable[[_type.GLuint,  # list
                      _type.GLenum],  # mode
                     _type.c_int]
glNormal3b: _Callable[[_type.GLbyte,  # nx
                       _type.GLbyte,  # ny
                       _type.GLbyte],  # nz
                      _type.c_int]
glNormal3bv: _Callable[[_Pointer[_type.GLbyte]],  # v
                       _type.c_int]
glNormal3d: _Callable[[_type.GLdouble,  # nx
                       _type.GLdouble,  # ny
                       _type.GLdouble],  # nz
                      _type.c_int]
glNormal3dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                       _type.c_int]
glNormal3f: _Callable[[_type.GLfloat,  # nx
                       _type.GLfloat,  # ny
                       _type.GLfloat],  # nz
                      _type.c_int]
glNormal3fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                       _type.c_int]
glNormal3i: _Callable[[_type.GLint,  # nx
                       _type.GLint,  # ny
                       _type.GLint],  # nz
                      _type.c_int]
glNormal3iv: _Callable[[_Pointer[_type.GLint]],  # v
                       _type.c_int]
glNormal3s: _Callable[[_type.GLshort,  # nx
                       _type.GLshort,  # ny
                       _type.GLshort],  # nz
                      _type.c_int]
glNormal3sv: _Callable[[_Pointer[_type.GLshort]],  # v
                       _type.c_int]
glNormalPointer: _Callable[[_type.GLenum,  # type
                            _type.GLsizei,  # stride
                            _Pointer[_type.GLvoid]],  # pointer
                           _type.c_int]
glOrtho: _Callable[[_type.GLdouble,  # left
                    _type.GLdouble,  # right
                    _type.GLdouble,  # bottom
                    _type.GLdouble,  # top
                    _type.GLdouble,  # zNear
                    _type.GLdouble],  # zFar
                   _type.c_int]
glPassThrough: _Callable[[_type.GLfloat],  # token
                         _type.c_int]
glPixelMapfv: _Callable[[_type.GLenum,  # map
                         _type.GLsizei,  # mapsize
                         _Pointer[_type.GLfloat]],  # values
                        _type.c_int]
glPixelMapuiv: _Callable[[_type.GLenum,  # map
                          _type.GLsizei,  # mapsize
                          _Pointer[_type.GLuint]],  # values
                         _type.c_int]
glPixelMapusv: _Callable[[_type.GLenum,  # map
                          _type.GLsizei,  # mapsize
                          _Pointer[_type.GLushort]],  # values
                         _type.c_int]
glPixelStoref: _Callable[[_type.GLenum,  # pname
                          _type.GLfloat],  # param
                         _type.c_int]
glPixelStorei: _Callable[[_type.GLenum,  # pname
                          _type.GLint],  # param
                         _type.c_int]
glPixelTransferf: _Callable[[_type.GLenum,  # pname
                             _type.GLfloat],  # param
                            _type.c_int]
glPixelTransferi: _Callable[[_type.GLenum,  # pname
                             _type.GLint],  # param
                            _type.c_int]
glPixelZoom: _Callable[[_type.GLfloat,  # xfactor
                        _type.GLfloat],  # yfactor
                       _type.c_int]
glPointSize: _Callable[[_type.GLfloat],  # size
                       _type.c_int]
glPolygonMode: _Callable[[_type.GLenum,  # face
                          _type.GLenum],  # mode
                         _type.c_int]
glPolygonOffset: _Callable[[_type.GLfloat,  # factor
                            _type.GLfloat],  # units
                           _type.c_int]
glPolygonStipple: _Callable[[_Pointer[_type.GLubyte]],  # mask
                            _type.c_int]
glPopAttrib: _Callable[[],
                       _type.c_int]
glPopClientAttrib: _Callable[[],
                             _type.c_int]
glPopMatrix: _Callable[[],
                       _type.c_int]
glPopName: _Callable[[],
                     _type.c_int]
glPrioritizeTextures: _Callable[[_type.GLsizei,  # n
                                 _Pointer[_type.GLuint],  # textures
                                 _Pointer[_type.GLclampf]],  # priorities
                                _type.c_int]
glPushAttrib: _Callable[[_type.GLbitfield],  # mask
                        _type.c_int]
glPushClientAttrib: _Callable[[_type.GLbitfield],  # mask
                              _type.c_int]
glPushMatrix: _Callable[[],
                        _type.c_int]
glPushName: _Callable[[_type.GLuint],  # name
                      _type.c_int]
glRasterPos2d: _Callable[[_type.GLdouble,  # x
                          _type.GLdouble],  # y
                         _type.c_int]
glRasterPos2dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                          _type.c_int]
glRasterPos2f: _Callable[[_type.GLfloat,  # x
                          _type.GLfloat],  # y
                         _type.c_int]
glRasterPos2fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                          _type.c_int]
glRasterPos2i: _Callable[[_type.GLint,  # x
                          _type.GLint],  # y
                         _type.c_int]
glRasterPos2iv: _Callable[[_Pointer[_type.GLint]],  # v
                          _type.c_int]
glRasterPos2s: _Callable[[_type.GLshort,  # x
                          _type.GLshort],  # y
                         _type.c_int]
glRasterPos2sv: _Callable[[_Pointer[_type.GLshort]],  # v
                          _type.c_int]
glRasterPos3d: _Callable[[_type.GLdouble,  # x
                          _type.GLdouble,  # y
                          _type.GLdouble],  # z
                         _type.c_int]
glRasterPos3dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                          _type.c_int]
glRasterPos3f: _Callable[[_type.GLfloat,  # x
                          _type.GLfloat,  # y
                          _type.GLfloat],  # z
                         _type.c_int]
glRasterPos3fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                          _type.c_int]
glRasterPos3i: _Callable[[_type.GLint,  # x
                          _type.GLint,  # y
                          _type.GLint],  # z
                         _type.c_int]
glRasterPos3iv: _Callable[[_Pointer[_type.GLint]],  # v
                          _type.c_int]
glRasterPos3s: _Callable[[_type.GLshort,  # x
                          _type.GLshort,  # y
                          _type.GLshort],  # z
                         _type.c_int]
glRasterPos3sv: _Callable[[_Pointer[_type.GLshort]],  # v
                          _type.c_int]
glRasterPos4d: _Callable[[_type.GLdouble,  # x
                          _type.GLdouble,  # y
                          _type.GLdouble,  # z
                          _type.GLdouble],  # w
                         _type.c_int]
glRasterPos4dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                          _type.c_int]
glRasterPos4f: _Callable[[_type.GLfloat,  # x
                          _type.GLfloat,  # y
                          _type.GLfloat,  # z
                          _type.GLfloat],  # w
                         _type.c_int]
glRasterPos4fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                          _type.c_int]
glRasterPos4i: _Callable[[_type.GLint,  # x
                          _type.GLint,  # y
                          _type.GLint,  # z
                          _type.GLint],  # w
                         _type.c_int]
glRasterPos4iv: _Callable[[_Pointer[_type.GLint]],  # v
                          _type.c_int]
glRasterPos4s: _Callable[[_type.GLshort,  # x
                          _type.GLshort,  # y
                          _type.GLshort,  # z
                          _type.GLshort],  # w
                         _type.c_int]
glRasterPos4sv: _Callable[[_Pointer[_type.GLshort]],  # v
                          _type.c_int]
glReadBuffer: _Callable[[_type.GLenum],  # mode
                        _type.c_int]
glReadPixels: _Callable[[_type.GLint,  # x
                         _type.GLint,  # y
                         _type.GLsizei,  # width
                         _type.GLsizei,  # height
                         _type.GLenum,  # format
                         _type.GLenum,  # type
                         _Pointer[_type.GLvoid]],  # pixels
                        _type.c_int]
glRectd: _Callable[[_type.GLdouble,  # x1
                    _type.GLdouble,  # y1
                    _type.GLdouble,  # x2
                    _type.GLdouble],  # y2
                   _type.c_int]
glRectdv: _Callable[[_Pointer[_type.GLdouble],  # v1
                     _Pointer[_type.GLdouble]],  # v2
                    _type.c_int]
glRectf: _Callable[[_type.GLfloat,  # x1
                    _type.GLfloat,  # y1
                    _type.GLfloat,  # x2
                    _type.GLfloat],  # y2
                   _type.c_int]
glRectfv: _Callable[[_Pointer[_type.GLfloat],  # v1
                     _Pointer[_type.GLfloat]],  # v2
                    _type.c_int]
glRecti: _Callable[[_type.GLint,  # x1
                    _type.GLint,  # y1
                    _type.GLint,  # x2
                    _type.GLint],  # y2
                   _type.c_int]
glRectiv: _Callable[[_Pointer[_type.GLint],  # v1
                     _Pointer[_type.GLint]],  # v2
                    _type.c_int]
glRects: _Callable[[_type.GLshort,  # x1
                    _type.GLshort,  # y1
                    _type.GLshort,  # x2
                    _type.GLshort],  # y2
                   _type.c_int]
glRectsv: _Callable[[_Pointer[_type.GLshort],  # v1
                     _Pointer[_type.GLshort]],  # v2
                    _type.c_int]
glRotated: _Callable[[_type.GLdouble,  # angle
                      _type.GLdouble,  # x
                      _type.GLdouble,  # y
                      _type.GLdouble],  # z
                     _type.c_int]
glRotatef: _Callable[[_type.GLfloat,  # angle
                      _type.GLfloat,  # x
                      _type.GLfloat,  # y
                      _type.GLfloat],  # z
                     _type.c_int]
glScaled: _Callable[[_type.GLdouble,  # x
                     _type.GLdouble,  # y
                     _type.GLdouble],  # z
                    _type.c_int]
glScalef: _Callable[[_type.GLfloat,  # x
                     _type.GLfloat,  # y
                     _type.GLfloat],  # z
                    _type.c_int]
glScissor: _Callable[[_type.GLint,  # x
                      _type.GLint,  # y
                      _type.GLsizei,  # width
                      _type.GLsizei],  # height
                     _type.c_int]
glSelectBuffer: _Callable[[_type.GLsizei,  # size
                           _Pointer[_type.GLuint]],  # buffer
                          _type.c_int]
glShadeModel: _Callable[[_type.GLenum],  # mode
                        _type.c_int]
glStencilFunc: _Callable[[_type.GLenum,  # func
                          _type.GLint,  # ref
                          _type.GLuint],  # mask
                         _type.c_int]
glStencilMask: _Callable[[_type.GLuint],  # mask
                         _type.c_int]
glStencilOp: _Callable[[_type.GLenum,  # fail
                        _type.GLenum,  # zfail
                        _type.GLenum],  # zpass
                       _type.c_int]
glTexCoord1d: _Callable[[_type.GLdouble],  # s
                        _type.c_int]
glTexCoord1dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                         _type.c_int]
glTexCoord1f: _Callable[[_type.GLfloat],  # s
                        _type.c_int]
glTexCoord1fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                         _type.c_int]
glTexCoord1i: _Callable[[_type.GLint],  # s
                        _type.c_int]
glTexCoord1iv: _Callable[[_Pointer[_type.GLint]],  # v
                         _type.c_int]
glTexCoord1s: _Callable[[_type.GLshort],  # s
                        _type.c_int]
glTexCoord1sv: _Callable[[_Pointer[_type.GLshort]],  # v
                         _type.c_int]
glTexCoord2d: _Callable[[_type.GLdouble,  # s
                         _type.GLdouble],  # t
                        _type.c_int]
glTexCoord2dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                         _type.c_int]
glTexCoord2f: _Callable[[_type.GLfloat,  # s
                         _type.GLfloat],  # t
                        _type.c_int]
glTexCoord2fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                         _type.c_int]
glTexCoord2i: _Callable[[_type.GLint,  # s
                         _type.GLint],  # t
                        _type.c_int]
glTexCoord2iv: _Callable[[_Pointer[_type.GLint]],  # v
                         _type.c_int]
glTexCoord2s: _Callable[[_type.GLshort,  # s
                         _type.GLshort],  # t
                        _type.c_int]
glTexCoord2sv: _Callable[[_Pointer[_type.GLshort]],  # v
                         _type.c_int]
glTexCoord3d: _Callable[[_type.GLdouble,  # s
                         _type.GLdouble,  # t
                         _type.GLdouble],  # r
                        _type.c_int]
glTexCoord3dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                         _type.c_int]
glTexCoord3f: _Callable[[_type.GLfloat,  # s
                         _type.GLfloat,  # t
                         _type.GLfloat],  # r
                        _type.c_int]
glTexCoord3fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                         _type.c_int]
glTexCoord3i: _Callable[[_type.GLint,  # s
                         _type.GLint,  # t
                         _type.GLint],  # r
                        _type.c_int]
glTexCoord3iv: _Callable[[_Pointer[_type.GLint]],  # v
                         _type.c_int]
glTexCoord3s: _Callable[[_type.GLshort,  # s
                         _type.GLshort,  # t
                         _type.GLshort],  # r
                        _type.c_int]
glTexCoord3sv: _Callable[[_Pointer[_type.GLshort]],  # v
                         _type.c_int]
glTexCoord4d: _Callable[[_type.GLdouble,  # s
                         _type.GLdouble,  # t
                         _type.GLdouble,  # r
                         _type.GLdouble],  # q
                        _type.c_int]
glTexCoord4dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                         _type.c_int]
glTexCoord4f: _Callable[[_type.GLfloat,  # s
                         _type.GLfloat,  # t
                         _type.GLfloat,  # r
                         _type.GLfloat],  # q
                        _type.c_int]
glTexCoord4fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                         _type.c_int]
glTexCoord4i: _Callable[[_type.GLint,  # s
                         _type.GLint,  # t
                         _type.GLint,  # r
                         _type.GLint],  # q
                        _type.c_int]
glTexCoord4iv: _Callable[[_Pointer[_type.GLint]],  # v
                         _type.c_int]
glTexCoord4s: _Callable[[_type.GLshort,  # s
                         _type.GLshort,  # t
                         _type.GLshort,  # r
                         _type.GLshort],  # q
                        _type.c_int]
glTexCoord4sv: _Callable[[_Pointer[_type.GLshort]],  # v
                         _type.c_int]
glTexCoordPointer: _Callable[[_type.GLint,  # size
                              _type.GLenum,  # type
                              _type.GLsizei,  # stride
                              _Pointer[_type.GLvoid]],  # pointer
                             _type.c_int]
glTexEnvf: _Callable[[_type.GLenum,  # target
                      _type.GLenum,  # pname
                      _type.GLfloat],  # param
                     _type.c_int]
glTexEnvfv: _Callable[[_type.GLenum,  # target
                       _type.GLenum,  # pname
                       _Pointer[_type.GLfloat]],  # params
                      _type.c_int]
glTexEnvi: _Callable[[_type.GLenum,  # target
                      _type.GLenum,  # pname
                      _type.GLint],  # param
                     _type.c_int]
glTexEnviv: _Callable[[_type.GLenum,  # target
                       _type.GLenum,  # pname
                       _Pointer[_type.GLint]],  # params
                      _type.c_int]
glTexGend: _Callable[[_type.GLenum,  # coord
                      _type.GLenum,  # pname
                      _type.GLdouble],  # param
                     _type.c_int]
glTexGendv: _Callable[[_type.GLenum,  # coord
                       _type.GLenum,  # pname
                       _Pointer[_type.GLdouble]],  # params
                      _type.c_int]
glTexGenf: _Callable[[_type.GLenum,  # coord
                      _type.GLenum,  # pname
                      _type.GLfloat],  # param
                     _type.c_int]
glTexGenfv: _Callable[[_type.GLenum,  # coord
                       _type.GLenum,  # pname
                       _Pointer[_type.GLfloat]],  # params
                      _type.c_int]
glTexGeni: _Callable[[_type.GLenum,  # coord
                      _type.GLenum,  # pname
                      _type.GLint],  # param
                     _type.c_int]
glTexGeniv: _Callable[[_type.GLenum,  # coord
                       _type.GLenum,  # pname
                       _Pointer[_type.GLint]],  # params
                      _type.c_int]
glTexImage1D: _Callable[[_type.GLenum,  # target
                         _type.GLint,  # level
                         _type.GLint,  # internalformat
                         _type.GLsizei,  # width
                         _type.GLint,  # border
                         _type.GLenum,  # format
                         _type.GLenum,  # type
                         _Pointer[_type.GLvoid]],  # pixels
                        _type.c_int]
glTexImage2D: _Callable[[_type.GLenum,  # target
                         _type.GLint,  # level
                         _type.GLint,  # internalformat
                         _type.GLsizei,  # width
                         _type.GLsizei,  # height
                         _type.GLint,  # border
                         _type.GLenum,  # format
                         _type.GLenum,  # type
                         _Pointer[_type.GLvoid]],  # pixels
                        _type.c_int]
glTexParameterf: _Callable[[_type.GLenum,  # target
                            _type.GLenum,  # pname
                            _type.GLfloat],  # param
                           _type.c_int]
glTexParameterfv: _Callable[[_type.GLenum,  # target
                             _type.GLenum,  # pname
                             _Pointer[_type.GLfloat]],  # params
                            _type.c_int]
glTexParameteri: _Callable[[_type.GLenum,  # target
                            _type.GLenum,  # pname
                            _type.GLint],  # param
                           _type.c_int]
glTexParameteriv: _Callable[[_type.GLenum,  # target
                             _type.GLenum,  # pname
                             _Pointer[_type.GLint]],  # params
                            _type.c_int]
glTexSubImage1D: _Callable[[_type.GLenum,  # target
                            _type.GLint,  # level
                            _type.GLint,  # xoffset
                            _type.GLsizei,  # width
                            _type.GLenum,  # format
                            _type.GLenum,  # type
                            _Pointer[_type.GLvoid]],  # pixels
                           _type.c_int]
glTexSubImage2D: _Callable[[_type.GLenum,  # target
                            _type.GLint,  # level
                            _type.GLint,  # xoffset
                            _type.GLint,  # yoffset
                            _type.GLsizei,  # width
                            _type.GLsizei,  # height
                            _type.GLenum,  # format
                            _type.GLenum,  # type
                            _Pointer[_type.GLvoid]],  # pixels
                           _type.c_int]
glTranslated: _Callable[[_type.GLdouble,  # x
                         _type.GLdouble,  # y
                         _type.GLdouble],  # z
                        _type.c_int]
glTranslatef: _Callable[[_type.GLfloat,  # x
                         _type.GLfloat,  # y
                         _type.GLfloat],  # z
                        _type.c_int]
glVertex2d: _Callable[[_type.GLdouble,  # x
                       _type.GLdouble],  # y
                      _type.c_int]
glVertex2dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                       _type.c_int]
glVertex2f: _Callable[[_type.GLfloat,  # x
                       _type.GLfloat],  # y
                      _type.c_int]
glVertex2fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                       _type.c_int]
glVertex2i: _Callable[[_type.GLint,  # x
                       _type.GLint],  # y
                      _type.c_int]
glVertex2iv: _Callable[[_Pointer[_type.GLint]],  # v
                       _type.c_int]
glVertex2s: _Callable[[_type.GLshort,  # x
                       _type.GLshort],  # y
                      _type.c_int]
glVertex2sv: _Callable[[_Pointer[_type.GLshort]],  # v
                       _type.c_int]
glVertex3d: _Callable[[_type.GLdouble,  # x
                       _type.GLdouble,  # y
                       _type.GLdouble],  # z
                      _type.c_int]
glVertex3dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                       _type.c_int]
glVertex3f: _Callable[[_type.GLfloat,  # x
                       _type.GLfloat,  # y
                       _type.GLfloat],  # z
                      _type.c_int]
glVertex3fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                       _type.c_int]
glVertex3i: _Callable[[_type.GLint,  # x
                       _type.GLint,  # y
                       _type.GLint],  # z
                      _type.c_int]
glVertex3iv: _Callable[[_Pointer[_type.GLint]],  # v
                       _type.c_int]
glVertex3s: _Callable[[_type.GLshort,  # x
                       _type.GLshort,  # y
                       _type.GLshort],  # z
                      _type.c_int]
glVertex3sv: _Callable[[_Pointer[_type.GLshort]],  # v
                       _type.c_int]
glVertex4d: _Callable[[_type.GLdouble,  # x
                       _type.GLdouble,  # y
                       _type.GLdouble,  # z
                       _type.GLdouble],  # w
                      _type.c_int]
glVertex4dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                       _type.c_int]
glVertex4f: _Callable[[_type.GLfloat,  # x
                       _type.GLfloat,  # y
                       _type.GLfloat,  # z
                       _type.GLfloat],  # w
                      _type.c_int]
glVertex4fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                       _type.c_int]
glVertex4i: _Callable[[_type.GLint,  # x
                       _type.GLint,  # y
                       _type.GLint,  # z
                       _type.GLint],  # w
                      _type.c_int]
glVertex4iv: _Callable[[_Pointer[_type.GLint]],  # v
                       _type.c_int]
glVertex4s: _Callable[[_type.GLshort,  # x
                       _type.GLshort,  # y
                       _type.GLshort,  # z
                       _type.GLshort],  # w
                      _type.c_int]
glVertex4sv: _Callable[[_Pointer[_type.GLshort]],  # v
                       _type.c_int]
glVertexPointer: _Callable[[_type.GLint,  # size
                            _type.GLenum,  # type
                            _type.GLsizei,  # stride
                            _Pointer[_type.GLvoid]],  # pointer
                           _type.c_int]
glViewport: _Callable[[_type.GLint,  # x
                       _type.GLint,  # y
                       _type.GLsizei,  # width
                       _type.GLsizei],  # height
                      _type.c_int]

_WinLib(__name__)

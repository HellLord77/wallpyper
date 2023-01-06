from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import type as _type
from .._utils import _Pointer

# GLU
gluErrorString: _Callable[[_type.GLenum],  # errCode
                          _Pointer[_type.GLubyte]]
gluErrorUnicodeStringEXT: _Callable[[_type.GLenum],  # errCode
                                    _Pointer[_type.c_wchar_t]]
gluGetString: _Callable[[_type.GLenum],  # name
                        _Pointer[_type.GLubyte]]
gluOrtho2D: _Callable[[_type.GLdouble,  # left
                       _type.GLdouble,  # right
                       _type.GLdouble,  # bottom
                       _type.GLdouble],  # top
                      _type.c_void]
gluPerspective: _Callable[[_type.GLdouble,  # fovy
                           _type.GLdouble,  # aspect
                           _type.GLdouble,  # zNear
                           _type.GLdouble],  # zFar
                          _type.c_void]
gluPickMatrix: _Callable[[_type.GLdouble,  # x
                          _type.GLdouble,  # y
                          _type.GLdouble,  # width
                          _type.GLdouble,  # height
                          _type.GLint * 4],  # viewport
                         _type.c_void]
gluLookAt: _Callable[[_type.GLdouble,  # eyex
                      _type.GLdouble,  # eyey
                      _type.GLdouble,  # eyez
                      _type.GLdouble,  # centerx
                      _type.GLdouble,  # centery
                      _type.GLdouble,  # centerz
                      _type.GLdouble,  # upx
                      _type.GLdouble,  # upy
                      _type.GLdouble],  # upz
                     _type.c_void]
gluProject: _Callable[[_type.GLdouble,  # objx
                       _type.GLdouble,  # objy
                       _type.GLdouble,  # objz
                       _type.GLdouble * 16,  # modelMatrix
                       _type.GLdouble * 16,  # projMatrix
                       _type.GLint * 4,  # viewport
                       _Pointer[_type.GLdouble],  # winx
                       _Pointer[_type.GLdouble],  # winy
                       _Pointer[_type.GLdouble]],  # winz
                      _type.c_int]
gluUnProject: _Callable[[_type.GLdouble,  # winx
                         _type.GLdouble,  # winy
                         _type.GLdouble,  # winz
                         _type.GLdouble * 16,  # modelMatrix
                         _type.GLdouble * 16,  # projMatrix
                         _type.GLint * 4,  # viewport
                         _Pointer[_type.GLdouble],  # objx
                         _Pointer[_type.GLdouble],  # objy
                         _Pointer[_type.GLdouble]],  # objz
                        _type.c_int]
gluScaleImage: _Callable[[_type.GLenum,  # format
                          _type.GLint,  # widthin
                          _type.GLint,  # heightin
                          _type.GLenum,  # typein
                          _type.c_void_p,  # datain
                          _type.GLint,  # widthout
                          _type.GLint,  # heightout
                          _type.GLenum,  # typeout
                          _type.c_void_p],  # dataout
                         _type.c_int]
gluBuild1DMipmaps: _Callable[[_type.GLenum,  # target
                              _type.GLint,  # components
                              _type.GLint,  # width
                              _type.GLenum,  # format
                              _type.GLenum,  # type
                              _type.c_void_p],  # data
                             _type.c_int]
gluBuild2DMipmaps: _Callable[[_type.GLenum,  # target
                              _type.GLint,  # components
                              _type.GLint,  # width
                              _type.GLint,  # height
                              _type.GLenum,  # format
                              _type.GLenum,  # type
                              _type.c_void_p],  # data
                             _type.c_int]
gluNewQuadric: _Callable[[],
                         _Pointer[_type.GLUquadric]]
gluDeleteQuadric: _Callable[[_Pointer[_type.GLUquadric]],  # state
                            _type.c_void]
gluQuadricNormals: _Callable[[_Pointer[_type.GLUquadric],  # quadObject
                              _type.GLenum],  # normals
                             _type.c_void]
gluQuadricTexture: _Callable[[_Pointer[_type.GLUquadric],  # quadObject
                              _type.GLboolean],  # textureCoords
                             _type.c_void]
gluQuadricOrientation: _Callable[[_Pointer[_type.GLUquadric],  # quadObject
                                  _type.GLenum],  # orientation
                                 _type.c_void]
gluQuadricDrawStyle: _Callable[[_Pointer[_type.GLUquadric],  # quadObject
                                _type.GLenum],  # drawStyle
                               _type.c_void]
gluCylinder: _Callable[[_Pointer[_type.GLUquadric],  # qobj
                        _type.GLdouble,  # baseRadius
                        _type.GLdouble,  # topRadius
                        _type.GLdouble,  # height
                        _type.GLint,  # slices
                        _type.GLint],  # stacks
                       _type.c_void]
gluDisk: _Callable[[_Pointer[_type.GLUquadric],  # qobj
                    _type.GLdouble,  # innerRadius
                    _type.GLdouble,  # outerRadius
                    _type.GLint,  # slices
                    _type.GLint],  # loops
                   _type.c_void]
gluPartialDisk: _Callable[[_Pointer[_type.GLUquadric],  # qobj
                           _type.GLdouble,  # innerRadius
                           _type.GLdouble,  # outerRadius
                           _type.GLint,  # slices
                           _type.GLint,  # loops
                           _type.GLdouble,  # startAngle
                           _type.GLdouble],  # sweepAngle
                          _type.c_void]
gluSphere: _Callable[[_Pointer[_type.GLUquadric],  # qobj
                      _type.GLdouble,  # radius
                      _type.GLint,  # slices
                      _type.GLint],  # stacks
                     _type.c_void]
gluNewTess: _Callable[[],
                      _Pointer[_type.GLUtesselator]]
gluDeleteTess: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                         _type.c_void]
gluTessBeginPolygon: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                                _type.c_void_p],  # polygon_data
                               _type.c_void]
gluTessBeginContour: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                               _type.c_void]
gluTessVertex: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                          _type.GLdouble * 3,  # coords
                          _type.c_void_p],  # data
                         _type.c_void]
gluTessEndContour: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                             _type.c_void]
gluTessEndPolygon: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                             _type.c_void]
gluTessProperty: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                            _type.GLenum,  # which
                            _type.GLdouble],  # value
                           _type.c_void]
gluTessNormal: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                          _type.GLdouble,  # x
                          _type.GLdouble,  # y
                          _type.GLdouble],  # z
                         _type.c_void]
gluGetTessProperty: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                               _type.GLenum,  # which
                               _Pointer[_type.GLdouble]],  # value
                              _type.c_void]
gluNewNurbsRenderer: _Callable[[],
                               _Pointer[_type.GLUnurbs]]
gluDeleteNurbsRenderer: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                                  _type.c_void]
gluBeginSurface: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                           _type.c_void]
gluBeginCurve: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                         _type.c_void]
gluEndCurve: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                       _type.c_void]
gluEndSurface: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                         _type.c_void]
gluBeginTrim: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                        _type.c_void]
gluEndTrim: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                      _type.c_void]
gluPwlCurve: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                        _type.GLint,  # count
                        _Pointer[_type.GLfloat],  # array
                        _type.GLint,  # stride
                        _type.GLenum],  # type
                       _type.c_void]
gluNurbsCurve: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                          _type.GLint,  # nknots
                          _Pointer[_type.GLfloat],  # knot
                          _type.GLint,  # stride
                          _Pointer[_type.GLfloat],  # ctlarray
                          _type.GLint,  # order
                          _type.GLenum],  # type
                         _type.c_void]
gluNurbsSurface: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                            _type.GLint,  # sknot_count
                            _Pointer[_type.c_float],  # sknot
                            _type.GLint,  # tknot_count
                            _Pointer[_type.GLfloat],  # tknot
                            _type.GLint,  # s_stride
                            _type.GLint,  # t_stride
                            _Pointer[_type.GLfloat],  # ctlarray
                            _type.GLint,  # sorder
                            _type.GLint,  # torder
                            _type.GLenum],  # type
                           _type.c_void]
gluLoadSamplingMatrices: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                                    _type.GLfloat * 16,  # modelMatrix
                                    _type.GLfloat * 16,  # projMatrix
                                    _type.GLint * 4],  # viewport
                                   _type.c_void]
gluNurbsProperty: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                             _type.GLenum,  # property
                             _type.GLfloat],  # value
                            _type.c_void]
gluGetNurbsProperty: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                                _type.GLenum,  # property
                                _Pointer[_type.GLfloat]],  # value
                               _type.c_void]
gluBeginPolygon: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                           _type.c_void]
gluNextContour: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                           _type.GLenum],  # type
                          _type.c_void]
gluEndPolygon: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                         _type.c_void]

_WinLib(__name__)

from __future__ import annotations as _

import math
import ntpath
import random
from typing import Optional

from libs import ctyped
from libs.ctyped.const import ChromaSDK as const_ChromaSDK
from libs.ctyped.enum import CChromaEditor as enum_CCChromaEditor
from libs.ctyped.lib import CChromaEditorLibrary


def init(info: Optional[ctyped.struct.ChromaSDK.APPINFOTYPE] = None) -> bool:
    return (CChromaEditorLibrary.PluginInit() if info is None else
            CChromaEditorLibrary.PluginInitSDK(ctyped.byref(info))) == const_ChromaSDK.RZRESULT_SUCCESS


def cleanup() -> bool:
    CChromaEditorLibrary.PluginStopAll()
    CChromaEditorLibrary.PluginCloseAll()
    return CChromaEditorLibrary.PluginUninit() == const_ChromaSDK.RZRESULT_SUCCESS


def _get_base_layer(layer: str, get: bool = True) -> ctyped.type.c_char_p:
    name = ctyped.type.c_char_p(ntpath.join(ntpath.dirname(
        __file__), 'Animations', f'{layer}.chroma').encode())
    CChromaEditorLibrary.PluginCloseAnimationName(name)
    if get:
        CChromaEditorLibrary.PluginGetAnimation(name)
    return name


class _AnimationMeta(type):
    def __enter__(self) -> bool:
        return init() and self()

    def __exit__(self, _, __, ___):
        cleanup()

    def __call__(cls: type[_Animation], keyboard: bool = True, chroma_link: bool = True,
                 headset: bool = True, keypad: bool = True, mousepad: bool = True, mouse: bool = True):
        if keyboard:
            cls.keyboard()
        if chroma_link:
            cls.chroma_link()
        if headset:
            cls.headset()
        if keypad:
            cls.keypad()
        if mousepad:
            cls.mousepad()
        if mouse:
            cls.mouse()


class _Animation(metaclass=_AnimationMeta):
    @staticmethod
    def _device(name: str):
        raise NotImplementedError

    @classmethod
    def keyboard(cls):
        cls._device('Keyboard')

    @classmethod
    def chroma_link(cls):
        cls._device('ChromaLink')

    @classmethod
    def headset(cls):
        cls._device('Headset')

    @classmethod
    def mousepad(cls):
        cls._device('Mousepad')

    @classmethod
    def mouse(cls):
        cls._device('Mouse')

    @classmethod
    def keypad(cls):
        cls._device('Keypad')


class Animation1(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Sprite1_{name}')
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)

    @classmethod
    def keyboard(cls):
        CChromaEditorLibrary.PluginUseIdleAnimation(enum_CCChromaEditor.ChromaSDK.EChromaSDKDeviceEnum.Keyboard, False)
        super().keyboard()


class Animation2(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Trails_{name}')
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation3(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Trails_{name}')
        CChromaEditorLibrary.PluginMultiplyIntensityAllFramesRGBName(base_layer, 0, 255, 0)
        min_threshold = 50
        max_threshold = 150
        CChromaEditorLibrary.PluginFillThresholdColorsMinMaxAllFramesRGBName(base_layer, min_threshold, 255, 0, 0, max_threshold, 0, 0, 255)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)

    @classmethod
    def keypad(cls):
        base_layer = _get_base_layer('Blank_Keypad')
        CChromaEditorLibrary.PluginFillZeroColorAllFramesRGBName(base_layer, 255, 0, 0)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation4(_Animation):
    @classmethod
    def _device(cls, name: str):
        base_layer = _get_base_layer(f'ParticlesOut_{name}')
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation5(_Animation):
    @classmethod
    def _device(cls, name: str):
        base_layer = _get_base_layer(f'ParticlesOut_{name}')
        CChromaEditorLibrary.PluginMultiplyIntensityAllFramesRGBName(base_layer, 0, 127, 255)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation6(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        frame_count = 50
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.033, 255, 255, 255)
        CChromaEditorLibrary.PluginFadeStartFramesName(base_layer, 40)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation7(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        frame_count = 50
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.033, 255, 255, 255)
        CChromaEditorLibrary.PluginFadeEndFramesName(base_layer, 40)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation8(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        frame_count = 50
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.033, 255, 255, 255)
        CChromaEditorLibrary.PluginFadeStartFramesName(base_layer, 40)
        CChromaEditorLibrary.PluginFadeEndFramesName(base_layer, 40)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation9(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        frame_count = 50
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.033, 255, 255, 255)
        speed = 2
        for frame_id in range(frame_count):
            t = 1 - abs(math.cos(speed * math.pi * (frame_id + 1) / frame_count))
            CChromaEditorLibrary.PluginMultiplyIntensityName(base_layer, frame_id, t)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation10(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Particles2_{name}')
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation11(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Particles2_{name}')
        CChromaEditorLibrary.PluginMultiplyIntensityAllFramesName(base_layer, 0.25)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation12(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'BlackAndWhiteRainbow_{name}')
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation13(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'BlackAndWhiteRainbow_{name}')
        frame_count = CChromaEditorLibrary.PluginGetFrameCountName(base_layer)
        for frame_id in range(frame_count):
            CChromaEditorLibrary.PluginMultiplyIntensityRGBName(base_layer, frame_id, 255, 255, 0)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation14(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'BlackAndWhiteRainbow_{name}')
        CChromaEditorLibrary.PluginMultiplyIntensityAllFramesRGBName(base_layer, 0, 255, 255)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation15(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'BlackAndWhiteRainbow_{name}')
        frame_count = CChromaEditorLibrary.PluginGetFrameCountName(base_layer)
        color1 = CChromaEditorLibrary.PluginGetRGB(255, 0, 0)
        color2 = CChromaEditorLibrary.PluginGetRGB(0, 255, 0)
        speed = 2
        for frame_id in range(frame_count):
            t = abs(math.cos(speed * math.pi * (frame_id + 1) / frame_count))
            color = CChromaEditorLibrary.PluginLerpColor(color1, color2, t)
            CChromaEditorLibrary.PluginMultiplyIntensityColorName(base_layer, frame_id, color)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation16(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Trails_{name}')
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation17(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Trails_{name}')
        frame_count = CChromaEditorLibrary.PluginGetFrameCountName(base_layer)
        for frame_id in range(frame_count):
            threshold = 100
            CChromaEditorLibrary.PluginFillThresholdColorsRGBName(base_layer, frame_id, threshold, 255, 0, 0)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation18(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Trails_{name}')
        threshold = 50
        CChromaEditorLibrary.PluginFillThresholdColorsAllFramesRGBName(base_layer, threshold, 0, 64, 0)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation19(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Trails_{name}')
        min_threshold = 50
        max_threshold = 150
        CChromaEditorLibrary.PluginFillThresholdColorsMinMaxAllFramesRGBName(base_layer, min_threshold, 0, 63, 63, max_threshold, 127, 0, 127)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation20(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Arc3_{name}')
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation21(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        layer2 = _get_base_layer(f'Arc3_{name}')
        background = CChromaEditorLibrary.PluginGetRGB(127, 0, 0)
        frame_count = CChromaEditorLibrary.PluginGetFrameCountName(layer2)
        CChromaEditorLibrary.PluginMakeBlankFramesName(base_layer, frame_count, 0.033, background)
        CChromaEditorLibrary.PluginCopyNonZeroAllKeysAllFramesName(layer2, base_layer)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation22(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        layer2 = _get_base_layer(f'Arc3_{name}')
        frame_count = CChromaEditorLibrary.PluginGetFrameCountName(layer2)
        background = CChromaEditorLibrary.PluginGetRGB(127, 0, 0)
        CChromaEditorLibrary.PluginMakeBlankFramesName(base_layer, frame_count, 0.033, background)
        CChromaEditorLibrary.PluginFillThresholdColorsAllFramesName(layer2, 64, background)
        CChromaEditorLibrary.PluginCopyNonZeroAllKeysAllFramesName(layer2, base_layer)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation23(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        layer2 = _get_base_layer(f'Arc3_{name}')
        frame_count = CChromaEditorLibrary.PluginGetFrameCountName(layer2)
        background = CChromaEditorLibrary.PluginGetRGB(127, 0, 0)
        CChromaEditorLibrary.PluginMakeBlankFramesName(base_layer, frame_count, 0.033, background)
        CChromaEditorLibrary.PluginAddNonZeroAllKeysAllFramesName(layer2, base_layer)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation24(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        layer2 = _get_base_layer(f'Arc3_{name}')
        frame_count = CChromaEditorLibrary.PluginGetFrameCountName(layer2)
        background = CChromaEditorLibrary.PluginGetRGB(127, 0, 0)
        CChromaEditorLibrary.PluginMakeBlankFramesName(base_layer, frame_count, 0.033, background)
        CChromaEditorLibrary.PluginSubtractNonZeroAllKeysAllFramesName(layer2, base_layer)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation25(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Rainbow_{name}')
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation26(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Movement_{name}')
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation27(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Movement_{name}')
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation28(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Movement_{name}')
        CChromaEditorLibrary.PluginReverseAllFramesName(base_layer)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation29(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Movement_{name}')
        CChromaEditorLibrary.PluginInvertColorsAllFramesName(base_layer)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation30(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Movement_{name}')
        CChromaEditorLibrary.PluginDuplicateMirrorFramesName(base_layer)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation31(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Movement_{name}')
        frame_id = 50
        delay = 20
        CChromaEditorLibrary.PluginInsertDelayName(base_layer, frame_id, delay)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation32(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Movement_{name}')
        CChromaEditorLibrary.PluginReduceFramesName(base_layer, 2)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation33(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Movement_{name}')
        CChromaEditorLibrary.PluginDuplicateFramesName(base_layer)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation34(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Movement_{name}')
        CChromaEditorLibrary.PluginTrimStartFramesName(base_layer, 10)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation35(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Movement_{name}')
        CChromaEditorLibrary.PluginTrimStartFramesName(base_layer, 10)
        CChromaEditorLibrary.PluginTrimEndFramesName(base_layer, 75)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation36(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        CChromaEditorLibrary.PluginFillZeroColorAllFramesRGBName(base_layer, 0, 255, 0)
        frame_count = 20
        CChromaEditorLibrary.PluginDuplicateFirstFrameName(base_layer, frame_count)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)

    @classmethod
    def keyboard(cls):
        base_layer = _get_base_layer(f'CircleSmall_Keyboard')
        frame_count = 20
        CChromaEditorLibrary.PluginDuplicateFirstFrameName(base_layer, frame_count)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation37(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        frame_count = 20
        CChromaEditorLibrary.PluginMakeBlankFramesName(base_layer, frame_count, 0.033, 0)
        CChromaEditorLibrary.PluginFillRandomColorsBlackAndWhiteAllFramesName(base_layer)
        CChromaEditorLibrary.PluginDuplicateFramesName(base_layer)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation38(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        frame_count = 20
        CChromaEditorLibrary.PluginMakeBlankFramesName(base_layer, frame_count, 0.033, 0)
        CChromaEditorLibrary.PluginFillRandomColorsBlackAndWhiteAllFramesName(base_layer)
        CChromaEditorLibrary.PluginDuplicateFramesName(base_layer)
        threshold = 240
        CChromaEditorLibrary.PluginFillThresholdColorsAllFramesName(base_layer, threshold, 0)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation39(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        frame_count = 20
        CChromaEditorLibrary.PluginMakeBlankFramesName(base_layer, frame_count, 0.033, 0)
        CChromaEditorLibrary.PluginFillRandomColorsBlackAndWhiteAllFramesName(base_layer)
        CChromaEditorLibrary.PluginDuplicateFramesName(base_layer)
        min_threshold = 240
        max_threshold = 240
        CChromaEditorLibrary.PluginFillThresholdColorsMinMaxAllFramesRGBName(base_layer, min_threshold, 0, 0, 0, max_threshold, 0, 127, 255)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation40(_Animation):
    @staticmethod
    def _device(name: str, device: enum_CCChromaEditor.ChromaSDK.EChromaSDKDeviceEnum = enum_CCChromaEditor.ChromaSDK.EChromaSDKDeviceEnum.MAX):
        base_layer = _get_base_layer(f'Blank_{name}')
        idle_animation = _get_base_layer(f'BlackAndWhiteRainbow_{name}', False)
        CChromaEditorLibrary.PluginSetIdleAnimationName(idle_animation)
        CChromaEditorLibrary.PluginUseIdleAnimation(device, True)
        frame_count = 30
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.1, 255, 255, 255)
        color1 = CChromaEditorLibrary.PluginGetRGB(0, 255, 0)
        color2 = CChromaEditorLibrary.PluginGetRGB(255, 0, 0)
        CChromaEditorLibrary.PluginMultiplyColorLerpAllFramesName(base_layer, color1, color2)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, False)

    @classmethod
    def keyboard(cls):
        cls._device('Keyboard', enum_CCChromaEditor.ChromaSDK.EChromaSDKDeviceEnum.Keyboard)

    @classmethod
    def chroma_link(cls):
        cls._device('ChromaLink', enum_CCChromaEditor.ChromaSDK.EChromaSDKDeviceEnum.ChromaLink)

    @classmethod
    def headset(cls):
        cls._device('Headset', enum_CCChromaEditor.ChromaSDK.EChromaSDKDeviceEnum.Headset)

    @classmethod
    def mousepad(cls):
        cls._device('Mousepad', enum_CCChromaEditor.ChromaSDK.EChromaSDKDeviceEnum.Mousepad)

    @classmethod
    def mouse(cls):
        cls._device('Mouse', enum_CCChromaEditor.ChromaSDK.EChromaSDKDeviceEnum.Mouse)

    @classmethod
    def keypad(cls):
        cls._device('Keypad', enum_CCChromaEditor.ChromaSDK.EChromaSDKDeviceEnum.Keypad)


class Animation41(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        frame_count = 50
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.033, 64, 255, 64)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)

    @classmethod
    def keyboard(cls):
        base_layer = _get_base_layer(f'Blank_Keyboard')
        frame_count = 50
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.033, 64, 0, 64)
        max_row = CChromaEditorLibrary.PluginGetMaxRow(enum_CCChromaEditor.ChromaSDK.EChromaSDKDevice2DEnum.Keyboard)
        max_column = CChromaEditorLibrary.PluginGetMaxColumn(enum_CCChromaEditor.ChromaSDK.EChromaSDKDevice2DEnum.Keyboard)
        start_column = math.floor(random.randrange(ctyped.const.RAND_MAX + 1) / ctyped.const.RAND_MAX * max_column) % 22
        start_row = math.floor(random.randrange(ctyped.const.RAND_MAX + 1) / ctyped.const.RAND_MAX * max_row) % 6
        color = CChromaEditorLibrary.PluginGetRGB(0, 255, 0)
        radius = 0
        speed = 25 / frame_count
        line_width = 2
        for frame_index in range(frame_count):
            stroke = radius
            for t in range(line_width):
                for i in range(360):
                    angle = i * math.pi / 180
                    r = math.floor(start_row + stroke * math.sin(angle))
                    c = math.floor(start_column + stroke * math.cos(angle))
                    if 0 <= r < max_row and 0 <= c < max_column:
                        key = (r << 8) | c
                        CChromaEditorLibrary.PluginSetKeyColorName(base_layer, frame_index, key, color)
                stroke += speed
            radius += speed
        CChromaEditorLibrary.PluginSetChromaCustomFlagName(base_layer, True)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation42(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        frame_count = 50
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.033, 64, 255, 64)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)

    @classmethod
    def keyboard(cls):
        base_layer = _get_base_layer(f'Blank_Keyboard')
        frame_count = 1
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.033, 64, 0, 64)
        max_row = CChromaEditorLibrary.PluginGetMaxRow(enum_CCChromaEditor.ChromaSDK.EChromaSDKDevice2DEnum.Keyboard)
        max_column = CChromaEditorLibrary.PluginGetMaxColumn(enum_CCChromaEditor.ChromaSDK.EChromaSDKDevice2DEnum.Keyboard)
        point_a_column = math.floor(random.randrange(ctyped.const.RAND_MAX + 1) / ctyped.const.RAND_MAX * max_column) % 22
        point_a_row = math.floor(random.randrange(ctyped.const.RAND_MAX + 1) / ctyped.const.RAND_MAX * max_row) % 6
        point_b_column = point_a_column
        point_b_row = point_a_row
        while point_a_column == point_b_column and point_a_row == point_b_row:
            point_b_column = math.floor(random.randrange(ctyped.const.RAND_MAX + 1) / ctyped.const.RAND_MAX * max_column) % 22
            point_b_row = math.floor(random.randrange(ctyped.const.RAND_MAX + 1) / ctyped.const.RAND_MAX * max_row) % 6
        color = CChromaEditorLibrary.PluginGetRGB(0, 255, 0)
        frame_index = 0
        for i in range(0, 100, 4):
            i /= 100
            r = math.floor(CChromaEditorLibrary.PluginLerp(point_a_row, point_b_row, i))
            c = math.floor(CChromaEditorLibrary.PluginLerp(point_a_column, point_b_column, i))
            if 0 <= r < max_row and 0 <= c < max_column:
                key = (r << 8) | c
                CChromaEditorLibrary.PluginSetKeyColorName(base_layer, frame_index, key, color)
        CChromaEditorLibrary.PluginSetChromaCustomFlagName(base_layer, True)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation43(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'BlackAndWhiteRainbow_{name}')
        CChromaEditorLibrary.PluginReduceFramesName(base_layer, 2)
        CChromaEditorLibrary.PluginReduceFramesName(base_layer, 2)
        color1 = CChromaEditorLibrary.PluginGetRGB(64, 64, 0)
        color2 = CChromaEditorLibrary.PluginGetRGB(64, 0, 64)
        CChromaEditorLibrary.PluginMultiplyTargetColorLerpAllFramesName(base_layer, color1, color2)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)

    @classmethod
    def keyboard(cls):
        base_layer = _get_base_layer(f'BlackAndWhiteRainbow_Keyboard')
        CChromaEditorLibrary.PluginReduceFramesName(base_layer, 2)
        CChromaEditorLibrary.PluginReduceFramesName(base_layer, 2)
        color1 = CChromaEditorLibrary.PluginGetRGB(64, 64, 0)
        color2 = CChromaEditorLibrary.PluginGetRGB(64, 0, 64)
        CChromaEditorLibrary.PluginMultiplyTargetColorLerpAllFramesName(base_layer, color1, color2)
        keys = ctyped.array(
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_W,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_A,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_S,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_D,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_P,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_M,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F1, type=ctyped.type.c_int)
        color = CChromaEditorLibrary.PluginGetRGB(0, 255, 0)
        CChromaEditorLibrary.PluginSetKeysColorAllFramesName(base_layer, keys, len(keys), color)
        CChromaEditorLibrary.PluginSetChromaCustomFlagName(base_layer, True)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation44(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'BlackAndWhiteRainbow_{name}')
        CChromaEditorLibrary.PluginReduceFramesName(base_layer, 2)
        CChromaEditorLibrary.PluginReduceFramesName(base_layer, 2)
        color1 = CChromaEditorLibrary.PluginGetRGB(32, 32, 32)
        color2 = CChromaEditorLibrary.PluginGetRGB(64, 64, 64)
        CChromaEditorLibrary.PluginMultiplyTargetColorLerpAllFramesName(base_layer, color1, color2)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)

    @classmethod
    def keyboard(cls):
        base_layer = _get_base_layer(f'Spiral_Keyboard')
        layer2 = _get_base_layer(f'Rainbow_Keyboard')
        color1 = CChromaEditorLibrary.PluginGetRGB(32, 32, 32)
        color2 = CChromaEditorLibrary.PluginGetRGB(64, 64, 64)
        CChromaEditorLibrary.PluginMultiplyTargetColorLerpAllFramesName(base_layer, color1, color2)
        keys = ctyped.array(
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_W,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_A,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_S,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_D,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_P,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_M,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F1, type=ctyped.type.c_int)
        CChromaEditorLibrary.PluginCopyKeysColorAllFramesName(layer2, base_layer, keys, len(keys))
        CChromaEditorLibrary.PluginSetChromaCustomFlagName(base_layer, True)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation45(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        frame_count = 50
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.1, 255, 255, 255)
        CChromaEditorLibrary.PluginFadeStartFramesName(base_layer, frame_count // 2)
        CChromaEditorLibrary.PluginFadeEndFramesName(base_layer, frame_count // 2)
        color1 = CChromaEditorLibrary.PluginGetRGB(0, 64, 0)
        color2 = CChromaEditorLibrary.PluginGetRGB(0, 255, 0)
        CChromaEditorLibrary.PluginMultiplyTargetColorLerpAllFramesName(base_layer, color1, color2)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)

    @classmethod
    def keyboard(cls):
        base_layer = _get_base_layer(f'Blank_Keyboard')
        frame_count = 120
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.1, 64, 64, 64)
        keys = ctyped.array(
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_W,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_A,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_S,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_D, type=ctyped.type.c_int)
        CChromaEditorLibrary.PluginSetKeysColorAllFramesRGBName(base_layer, keys, len(keys), 255, 255, 0)
        keys = ctyped.array(
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F1,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F2,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F3,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F4,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F5,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F6, type=ctyped.type.c_int)
        t = 0
        speed = 0.05
        for frame_id in range(frame_count):
            t += speed
            hp = abs(math.cos(math.pi / 2 + t))
            for i, key in enumerate(keys):
                # ratio = (i + 1) / len(keys)
                # color = CChromaEditorLibrary.PluginGetRGB(0, int(255 * (1 - hp)), 0)
                if (i + 1) / (len(keys) + 1) < hp:
                    color = CChromaEditorLibrary.PluginGetRGB(0, 255, 0)
                else:
                    color = CChromaEditorLibrary.PluginGetRGB(0, 100, 0)
                CChromaEditorLibrary.PluginSetKeyColorName(base_layer, frame_id, key, color)
        CChromaEditorLibrary.PluginSetChromaCustomFlagName(base_layer, True)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation46(_Animation):
    @staticmethod
    def _device(name: str):
        base_layer = _get_base_layer(f'Blank_{name}')
        frame_count = 50
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.1, 255, 255, 255)
        CChromaEditorLibrary.PluginFadeStartFramesName(base_layer, frame_count // 2)
        CChromaEditorLibrary.PluginFadeEndFramesName(base_layer, frame_count // 2)
        color1 = CChromaEditorLibrary.PluginGetRGB(64, 64, 0)
        color2 = CChromaEditorLibrary.PluginGetRGB(255, 255, 0)
        CChromaEditorLibrary.PluginMultiplyTargetColorLerpAllFramesName(base_layer, color1, color2)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)

    @classmethod
    def keyboard(cls):
        base_layer = _get_base_layer(f'Blank_Keyboard')
        frame_count = 120
        CChromaEditorLibrary.PluginMakeBlankFramesRGBName(base_layer, frame_count, 0.1, 64, 64, 64)
        keys = ctyped.array(
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_W,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_A,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_S,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_D, type=ctyped.type.c_int)
        CChromaEditorLibrary.PluginSetKeysColorAllFramesRGBName(base_layer, keys, len(keys), 255, 0, 0)
        keys = ctyped.array(
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F7,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F8,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F9,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F10,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F11,
            enum_CCChromaEditor.ChromaSDK.Keyboard.RZKEY.RZKEY_F12, type=ctyped.type.c_int)
        t = 0
        speed = 0.05
        for frame_id in range(frame_count):
            t += speed
            hp = abs(math.cos(math.pi / 2 + t))
            for i, key in enumerate(keys):
                # ratio = (i + 1) / len(keys)
                # color = CChromaEditorLibrary.PluginGetRGB(0, int(255 * (1 - hp)), 0)
                if (i + 1) / (len(keys) + 1) < hp:
                    color = CChromaEditorLibrary.PluginGetRGB(255, 255, 0)
                else:
                    color = CChromaEditorLibrary.PluginGetRGB(100, 100, 0)
                CChromaEditorLibrary.PluginSetKeyColorName(base_layer, frame_id, key, color)
        CChromaEditorLibrary.PluginSetChromaCustomFlagName(base_layer, True)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)


class Animation47(_Animation):
    @staticmethod
    def _device(name: str, embed: ctyped.Pointer[ctyped.type.BYTE] = None):
        base_layer = _get_base_layer(f'Blank_{name}', False)
        CChromaEditorLibrary.PluginOpenAnimationFromMemory(embed, base_layer)
        CChromaEditorLibrary.PluginOverrideFrameDurationName(base_layer, 0.033)
        CChromaEditorLibrary.PluginPlayAnimationName(base_layer, True)

    @classmethod
    def keyboard(cls):
        cls._device('Keyboard', ctyped.array(
            1, 0, 0, 0, 1, 0, 26, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 33, 37, 40, 0, 0, 0, 0, 0, 40, 41, 45, 0, 217,
            221, 220, 0, 226, 226, 227, 0, 36, 39, 44, 0, 41, 44, 49, 0, 20, 25, 29, 0, 24, 28, 31, 0, 21, 26, 32, 0,
            35, 43, 46, 0, 8, 154, 117, 0, 23, 147, 117, 0, 21, 144, 116, 0, 21, 139, 115, 0, 21, 135, 112, 0, 20, 131,
            112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 35, 38, 0, 34, 38, 41, 0, 36, 36,
            38, 0, 212, 217, 213, 0, 208, 210, 207, 0, 55, 56, 58, 0, 38, 41, 46, 0, 25, 30, 34, 0, 13, 16, 21, 0, 26,
            29, 36, 0, 25, 30, 36, 0, 33, 38, 44, 0, 13, 162, 119, 0, 22, 149, 119, 0, 23, 143, 118, 0, 20, 138, 114, 0,
            18, 134, 113, 0, 20, 128, 112, 0, 17, 125, 109, 0, 19, 121, 108, 0, 19, 116, 105, 0, 0, 0, 0, 0, 32, 36, 39,
            0, 22, 23, 27, 0, 40, 40, 42, 0, 199, 207, 204, 0, 186, 192, 192, 0, 41, 43, 49, 0, 10, 13, 18, 0, 16, 17,
            22, 0, 29, 32, 37, 0, 39, 44, 50, 0, 42, 47, 53, 0, 45, 50, 54, 0, 22, 157, 117, 0, 22, 151, 118, 0, 21,
            146, 116, 0, 23, 141, 115, 0, 20, 138, 114, 0, 18, 131, 111, 0, 18, 127, 108, 0, 17, 122, 107, 0, 18, 120,
            107, 0, 0, 0, 0, 0, 24, 28, 29, 0, 22, 23, 27, 0, 30, 31, 35, 0, 211, 245, 159, 0, 204, 232, 149, 0, 13, 12,
            17, 0, 17, 16, 22, 0, 17, 18, 23, 0, 15, 20, 24, 0, 11, 16, 22, 0, 52, 57, 63, 0, 23, 163, 122, 0, 0, 0, 0,
            0, 23, 157, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 134, 114, 0, 19, 130, 111, 0, 19, 126, 110, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 38, 43, 45, 0, 0, 0, 0, 0, 34, 38, 39, 0, 159, 211, 78, 0, 131, 179, 123, 0, 138,
            201, 53, 0, 12, 16, 19, 0, 12, 13, 18, 0, 27, 31, 38, 0, 28, 33, 37, 0, 26, 31, 37, 0, 26, 169, 125, 0, 0,
            0, 0, 0, 24, 160, 120, 0, 0, 0, 0, 0, 22, 147, 117, 0, 0, 0, 0, 0, 19, 136, 110, 0, 19, 132, 112, 0, 19,
            128, 109, 0, 17, 124, 108, 0, 0, 0, 0, 0, 53, 71, 42, 0, 201, 230, 130, 0, 133, 190, 32, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 22, 26, 29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 45, 51, 0, 28, 170, 122, 0, 25,
            166, 123, 0, 25, 160, 120, 0, 23, 154, 120, 0, 22, 149, 119, 0, 20, 143, 114, 0, 0, 0, 0, 0, 21, 137, 114,
            0, 18, 129, 110, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 224, 250, 168, 0, 0, 0, 0, 0, 23, 27, 30, 0,
            197, 198, 200, 0, 216, 217, 219, 0, 88, 89, 91, 0, 30, 33, 38, 0, 33, 36, 41, 0, 22, 25, 30, 0, 28, 31, 36,
            0, 38, 43, 49, 0, 43, 48, 52, 0, 22, 149, 119, 0, 21, 146, 116, 0, 21, 141, 113, 0, 21, 139, 115, 0, 20,
            134, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 177, 221, 104, 0, 34, 38, 40, 0,
            26, 30, 34, 0, 161, 162, 164, 0, 194, 199, 198, 0, 197, 198, 193, 0, 38, 39, 41, 0, 27, 31, 35, 0, 30, 33,
            38, 0, 25, 28, 33, 0, 27, 30, 36, 0, 37, 42, 48, 0, 45, 51, 57, 0, 23, 153, 119, 0, 22, 146, 117, 0, 22,
            141, 115, 0, 20, 137, 114, 0, 20, 132, 112, 0, 19, 128, 111, 0, 18, 125, 109, 0, 19, 121, 108, 0, 0, 0, 0,
            0, 68, 121, 14, 0, 27, 28, 33, 0, 32, 36, 39, 0, 209, 210, 214, 0, 200, 206, 206, 0, 188, 194, 194, 0, 19,
            22, 26, 0, 29, 32, 37, 0, 34, 37, 42, 0, 27, 30, 35, 0, 37, 42, 48, 0, 45, 50, 56, 0, 35, 158, 122, 0, 24,
            156, 119, 0, 22, 149, 119, 0, 21, 146, 116, 0, 22, 140, 114, 0, 20, 136, 113, 0, 18, 131, 111, 0, 20, 127,
            111, 0, 19, 124, 109, 0, 0, 0, 0, 0, 158, 224, 58, 0, 22, 23, 27, 0, 18, 19, 23, 0, 33, 37, 39, 0, 224, 246,
            173, 0, 188, 217, 126, 0, 29, 30, 34, 0, 17, 18, 23, 0, 23, 24, 29, 0, 24, 29, 33, 0, 38, 43, 49, 0, 55, 58,
            65, 0, 0, 0, 0, 0, 24, 160, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 138, 114, 0, 20, 133, 113, 0,
            19, 130, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 196, 233, 116, 0, 0, 0, 0, 0, 22, 26, 27, 0, 15, 19, 29, 0, 203,
            237, 147, 0, 181, 230, 107, 0, 155, 206, 66, 0, 12, 16, 19, 0, 18, 19, 24, 0, 26, 31, 35, 0, 34, 39, 45, 0,
            41, 46, 52, 0, 0, 0, 0, 0, 25, 166, 124, 0, 0, 0, 0, 0, 23, 151, 118, 0, 0, 0, 0, 0, 22, 140, 116, 0, 21,
            137, 114, 0, 20, 131, 112, 0, 20, 129, 110, 0, 0, 0, 0, 0, 29, 34, 42, 0, 171, 208, 84, 0, 192, 224, 104, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 36, 40, 0, 35, 40,
            46, 0, 27, 168, 125, 0, 24, 165, 123, 0, 23, 157, 120, 0, 22, 153, 119, 0, 23, 148, 118, 0, 0, 0, 0, 0, 22,
            140, 116, 0, 20, 133, 113, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 38, 41, 46, 0, 0, 0, 0, 0, 31, 35,
            38, 0, 25, 29, 32, 0, 217, 218, 220, 0, 223, 225, 224, 0, 9, 13, 16, 0, 36, 39, 44, 0, 34, 37, 42, 0, 28,
            33, 37, 0, 32, 37, 43, 0, 38, 43, 49, 0, 41, 44, 49, 0, 24, 149, 119, 0, 22, 145, 117, 0, 21, 141, 114, 0,
            20, 138, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 61, 62, 65, 0, 157, 206, 76, 0,
            28, 32, 35, 0, 20, 23, 27, 0, 207, 208, 211, 0, 223, 225, 224, 0, 219, 221, 215, 0, 37, 38, 40, 0, 10, 14,
            19, 0, 28, 31, 36, 0, 29, 32, 37, 0, 34, 39, 45, 0, 30, 35, 41, 0, 46, 145, 119, 0, 22, 150, 118, 0, 22,
            146, 117, 0, 21, 139, 114, 0, 20, 136, 114, 0, 20, 132, 112, 0, 18, 128, 110, 0, 18, 123, 108, 0, 0, 0, 0,
            0, 17, 32, 4, 0, 13, 14, 12, 0, 26, 30, 33, 0, 21, 25, 28, 0, 177, 178, 182, 0, 207, 213, 213, 0, 198, 204,
            204, 0, 7, 9, 24, 0, 34, 39, 43, 0, 38, 41, 46, 0, 19, 22, 27, 0, 27, 32, 38, 0, 42, 47, 53, 0, 24, 159,
            119, 0, 23, 153, 119, 0, 22, 149, 119, 0, 22, 145, 116, 0, 22, 140, 116, 0, 21, 135, 112, 0, 18, 131, 111,
            0, 20, 127, 111, 0, 0, 0, 0, 0, 26, 30, 40, 0, 17, 22, 22, 0, 26, 27, 31, 0, 26, 27, 31, 0, 26, 30, 32, 0,
            212, 232, 156, 0, 222, 244, 160, 0, 29, 30, 34, 0, 0, 0, 5, 0, 21, 22, 27, 0, 22, 27, 31, 0, 35, 40, 46, 0,
            0, 0, 0, 0, 27, 161, 122, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 142, 115, 0, 20, 138, 114, 0, 20, 133,
            113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 45, 44, 0, 0, 0, 0, 0, 49, 51, 41, 0, 20, 24, 25, 0, 18, 22, 23, 0, 185,
            226, 122, 0, 192, 228, 119, 0, 174, 218, 96, 0, 19, 22, 27, 0, 25, 26, 31, 0, 27, 32, 36, 0, 38, 43, 49, 0,
            0, 0, 0, 0, 24, 167, 123, 0, 0, 0, 0, 0, 23, 154, 120, 0, 0, 0, 0, 0, 22, 145, 117, 0, 22, 140, 116, 0, 18,
            134, 111, 0, 19, 132, 112, 0, 0, 0, 0, 0, 32, 33, 37, 0, 6, 5, 3, 0, 165, 200, 76, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 131, 187, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 39, 44, 0, 29, 34, 38, 0, 41, 46,
            52, 0, 26, 167, 124, 0, 26, 161, 121, 0, 23, 157, 120, 0, 23, 153, 119, 0, 0, 0, 0, 0, 20, 143, 114, 0, 21,
            137, 114, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 52, 57, 61, 0, 0, 0, 0, 0, 224, 250, 168, 0, 36, 40,
            43, 0, 19, 23, 26, 0, 247, 248, 250, 0, 229, 229, 229, 0, 42, 46, 49, 0, 28, 31, 36, 0, 36, 39, 44, 0, 26,
            29, 34, 0, 34, 39, 45, 0, 41, 46, 52, 0, 34, 39, 43, 0, 25, 147, 119, 0, 22, 145, 117, 0, 21, 141, 114, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 37, 41, 46, 0, 24, 27, 16, 0, 177, 221, 104, 0,
            33, 37, 40, 0, 20, 24, 28, 0, 237, 238, 241, 0, 209, 214, 213, 0, 197, 198, 193, 0, 38, 39, 41, 0, 27, 31,
            35, 0, 30, 33, 38, 0, 30, 33, 38, 0, 38, 41, 48, 0, 41, 46, 52, 0, 25, 152, 120, 0, 22, 150, 118, 0, 22,
            146, 117, 0, 20, 139, 113, 0, 20, 136, 114, 0, 20, 132, 112, 0, 20, 128, 110, 0, 0, 0, 0, 0, 30, 38, 40, 0,
            203, 228, 125, 0, 25, 28, 26, 0, 21, 22, 27, 0, 27, 31, 34, 0, 216, 217, 221, 0, 206, 212, 212, 0, 188, 194,
            194, 0, 19, 22, 26, 0, 29, 32, 37, 0, 34, 37, 42, 0, 28, 31, 36, 0, 26, 31, 37, 0, 43, 54, 56, 0, 23, 158,
            118, 0, 23, 153, 119, 0, 22, 149, 119, 0, 21, 144, 115, 0, 22, 140, 116, 0, 20, 136, 113, 0, 19, 132, 112,
            0, 0, 0, 0, 0, 46, 51, 54, 0, 187, 226, 95, 0, 35, 40, 41, 0, 30, 31, 35, 0, 23, 24, 28, 0, 26, 30, 32, 0,
            219, 239, 172, 0, 188, 217, 126, 0, 29, 30, 34, 0, 17, 18, 23, 0, 23, 24, 29, 0, 18, 23, 27, 0, 0, 0, 0, 0,
            40, 45, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 145, 116, 0, 22, 142, 115, 0, 20, 138, 114, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 32, 37, 40, 0, 0, 0, 0, 0, 193, 224, 105, 0, 44, 43, 26, 0, 14, 18, 19, 0, 15, 19, 28, 0,
            204, 241, 146, 0, 181, 230, 107, 0, 155, 206, 66, 0, 12, 16, 19, 0, 18, 19, 24, 0, 39, 44, 48, 0, 0, 0, 0,
            0, 42, 47, 53, 0, 0, 0, 0, 0, 24, 160, 122, 0, 0, 0, 0, 0, 22, 150, 117, 0, 22, 145, 117, 0, 22, 140, 116,
            0, 20, 136, 113, 0, 0, 0, 0, 0, 50, 54, 57, 0, 26, 27, 31, 0, 19, 15, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 145, 222, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 31, 35, 0, 33, 36, 41, 0, 44, 49, 53, 0, 51,
            52, 57, 0, 25, 166, 123, 0, 26, 161, 121, 0, 23, 157, 120, 0, 0, 0, 0, 0, 21, 148, 118, 0, 22, 142, 115, 0,
            0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 23, 28, 32, 0, 0, 0, 0, 0, 41, 46, 50, 0, 38, 59, 16, 0, 28, 32,
            35, 0, 28, 32, 35, 0, 224, 225, 229, 0, 222, 224, 223, 0, 44, 48, 51, 0, 21, 24, 29, 0, 40, 43, 48, 0, 34,
            39, 43, 0, 28, 33, 39, 0, 37, 42, 48, 0, 40, 43, 48, 0, 22, 149, 119, 0, 20, 144, 115, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 33, 37, 0, 41, 46, 50, 0, 45, 50, 53, 0, 174, 220, 77, 0, 28,
            32, 35, 0, 21, 25, 28, 0, 80, 80, 82, 0, 216, 220, 219, 0, 218, 220, 217, 0, 76, 77, 79, 0, 17, 20, 25, 0,
            20, 25, 29, 0, 19, 22, 27, 0, 29, 34, 40, 0, 35, 41, 47, 0, 22, 153, 119, 0, 21, 149, 116, 0, 21, 144, 116,
            0, 21, 141, 116, 0, 20, 136, 113, 0, 21, 132, 113, 0, 0, 0, 0, 0, 40, 44, 47, 0, 21, 26, 29, 0, 114, 134,
            71, 0, 53, 66, 61, 0, 30, 31, 36, 0, 26, 27, 31, 0, 201, 200, 205, 0, 215, 221, 219, 0, 196, 202, 202, 0,
            38, 39, 36, 0, 15, 18, 23, 0, 26, 29, 34, 0, 18, 21, 26, 0, 14, 19, 25, 0, 45, 50, 54, 0, 22, 157, 117, 0,
            22, 154, 117, 0, 23, 147, 118, 0, 21, 144, 115, 0, 21, 139, 113, 0, 19, 137, 113, 0, 0, 0, 0, 0, 40, 44, 47,
            0, 26, 31, 34, 0, 181, 210, 117, 0, 46, 60, 54, 0, 24, 25, 29, 0, 15, 16, 20, 0, 21, 25, 28, 0, 192, 225,
            126, 0, 203, 237, 134, 0, 18, 16, 22, 0, 0, 0, 5, 0, 24, 25, 30, 0, 0, 0, 0, 0, 30, 35, 41, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 22, 152, 118, 0, 22, 147, 117, 0, 23, 142, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 38,
            41, 0, 0, 0, 0, 0, 19, 24, 28, 0, 172, 203, 73, 0, 34, 38, 29, 0, 23, 27, 28, 0, 14, 19, 22, 0, 194, 232,
            133, 0, 90, 153, 25, 0, 142, 205, 55, 0, 6, 10, 13, 0, 8, 9, 14, 0, 0, 0, 0, 0, 28, 33, 37, 0, 0, 0, 0, 0,
            24, 163, 122, 0, 0, 0, 0, 0, 23, 153, 119, 0, 21, 149, 116, 0, 20, 145, 115, 0, 22, 142, 115, 0, 0, 0, 0, 0,
            33, 37, 40, 0, 32, 36, 39, 0, 29, 30, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 156, 200, 70, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 17, 20, 0, 20, 25, 29, 0, 27, 30, 35, 0, 25, 30, 34, 0, 27, 171, 122, 0, 25,
            166, 123, 0, 25, 161, 121, 0, 0, 0, 0, 0, 23, 154, 120, 0, 22, 147, 117, 0, 0, 0, 0, 0, 205, 204, 204, 61,
            0, 0, 0, 0, 45, 65, 60, 0, 0, 0, 0, 0, 29, 34, 38, 0, 46, 51, 55, 0, 46, 66, 28, 0, 40, 44, 47, 0, 51, 54,
            59, 0, 207, 211, 212, 0, 224, 226, 225, 0, 21, 25, 28, 0, 24, 27, 32, 0, 31, 36, 40, 0, 34, 39, 43, 0, 28,
            33, 39, 0, 42, 47, 53, 0, 34, 39, 43, 0, 24, 147, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 43, 52, 51, 0, 36, 41, 45, 0, 22, 27, 31, 0, 31, 37, 35, 0, 175, 225, 86, 0, 25, 29, 32, 0, 29, 32,
            37, 0, 108, 108, 110, 0, 223, 227, 226, 0, 211, 213, 210, 0, 56, 57, 59, 0, 23, 26, 31, 0, 21, 24, 29, 0,
            24, 27, 32, 0, 39, 44, 50, 0, 32, 37, 43, 0, 24, 151, 121, 0, 23, 148, 118, 0, 21, 144, 116, 0, 21, 141,
            116, 0, 22, 136, 113, 0, 0, 0, 0, 0, 35, 40, 43, 0, 33, 37, 40, 0, 30, 35, 38, 0, 214, 237, 147, 0, 41, 51,
            43, 0, 28, 29, 34, 0, 22, 26, 29, 0, 226, 226, 231, 0, 205, 211, 211, 0, 198, 204, 204, 0, 36, 39, 26, 0,
            26, 29, 34, 0, 25, 28, 33, 0, 28, 31, 36, 0, 38, 43, 49, 0, 46, 47, 52, 0, 23, 158, 118, 0, 23, 151, 118, 0,
            23, 147, 119, 0, 21, 144, 115, 0, 22, 140, 114, 0, 0, 0, 0, 0, 38, 43, 46, 0, 47, 51, 54, 0, 42, 47, 50, 0,
            202, 241, 115, 0, 38, 44, 41, 0, 25, 26, 30, 0, 17, 18, 22, 0, 20, 24, 27, 0, 210, 243, 166, 0, 200, 236,
            130, 0, 15, 14, 19, 0, 11, 11, 17, 0, 0, 0, 0, 0, 29, 34, 38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23,
            155, 118, 0, 22, 152, 118, 0, 22, 145, 116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 28, 31, 0, 0, 0, 0, 0, 48, 53,
            56, 0, 43, 48, 51, 0, 171, 209, 61, 0, 49, 51, 38, 0, 13, 17, 18, 0, 21, 27, 28, 0, 195, 236, 153, 0, 111,
            168, 52, 0, 153, 213, 64, 0, 12, 16, 19, 0, 0, 0, 0, 0, 26, 29, 36, 0, 0, 0, 0, 0, 27, 166, 124, 0, 0, 0, 0,
            0, 23, 157, 120, 0, 23, 153, 119, 0, 21, 149, 116, 0, 21, 146, 116, 0, 0, 0, 0, 0, 38, 50, 50, 0, 21, 25,
            28, 0, 42, 46, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 176, 205, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 124, 155, 75, 0, 18, 22, 25, 0, 25, 30, 34, 0, 32, 35, 40, 0, 35, 40, 46, 0, 28, 170, 122, 0, 25, 166,
            123, 0, 0, 0, 0, 0, 24, 159, 119, 0, 22, 150, 117, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 55, 112,
            93, 0, 0, 0, 0, 0, 58, 61, 66, 0, 38, 43, 47, 0, 21, 25, 31, 0, 230, 254, 178, 0, 29, 33, 36, 0, 41, 45, 48,
            0, 210, 216, 214, 0, 206, 206, 207, 0, 33, 36, 41, 0, 29, 32, 37, 0, 25, 30, 34, 0, 38, 39, 44, 0, 32, 37,
            43, 0, 35, 40, 46, 0, 40, 51, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 58, 96, 83,
            0, 58, 64, 64, 0, 26, 31, 35, 0, 26, 31, 35, 0, 32, 32, 44, 0, 182, 224, 122, 0, 25, 29, 32, 0, 27, 30, 35,
            0, 207, 208, 212, 0, 222, 226, 225, 0, 234, 236, 231, 0, 34, 35, 37, 0, 32, 37, 41, 0, 28, 31, 36, 0, 36,
            41, 47, 0, 34, 39, 45, 0, 44, 49, 55, 0, 22, 152, 118, 0, 22, 147, 117, 0, 23, 143, 116, 0, 20, 140, 115, 0,
            0, 0, 0, 0, 49, 70, 64, 0, 42, 45, 49, 0, 35, 39, 43, 0, 57, 61, 64, 0, 192, 221, 121, 0, 6, 15, 1, 0, 23,
            27, 30, 0, 21, 23, 27, 0, 175, 177, 182, 0, 195, 203, 202, 0, 194, 200, 197, 0, 18, 19, 20, 0, 24, 28, 33,
            0, 27, 31, 35, 0, 12, 17, 23, 0, 35, 40, 46, 0, 61, 143, 121, 0, 23, 155, 119, 0, 21, 150, 118, 0, 22, 146,
            117, 0, 22, 145, 116, 0, 0, 0, 0, 0, 33, 42, 44, 0, 34, 38, 41, 0, 54, 58, 61, 0, 32, 37, 40, 0, 156, 219,
            54, 0, 23, 25, 22, 0, 25, 26, 30, 0, 22, 23, 27, 0, 22, 27, 30, 0, 191, 221, 168, 0, 201, 230, 137, 0, 27,
            28, 32, 0, 0, 0, 0, 0, 6, 7, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 157, 120, 0, 22, 153, 119, 0,
            22, 150, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 57, 55, 0, 0, 0, 0, 0, 44, 48, 51, 0, 41, 46, 49, 0, 17, 23,
            23, 0, 193, 229, 109, 0, 15, 16, 19, 0, 23, 25, 27, 0, 25, 29, 31, 0, 180, 226, 110, 0, 196, 231, 132, 0,
            174, 217, 101, 0, 0, 0, 0, 0, 25, 26, 31, 0, 0, 0, 0, 0, 38, 43, 49, 0, 0, 0, 0, 0, 24, 160, 120, 0, 25,
            157, 120, 0, 22, 152, 118, 0, 22, 150, 117, 0, 0, 0, 0, 0, 21, 195, 130, 0, 29, 33, 36, 0, 60, 64, 67, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 196, 225, 106, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 124, 190, 44, 0, 0,
            2, 11, 0, 10, 15, 19, 0, 38, 43, 47, 0, 34, 39, 45, 0, 42, 47, 53, 0, 23, 171, 123, 0, 0, 0, 0, 0, 25, 161,
            121, 0, 24, 156, 119, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 29, 165, 125, 0, 0, 0, 0, 0, 49, 61, 59,
            0, 49, 52, 57, 0, 36, 41, 45, 0, 26, 32, 38, 0, 32, 36, 39, 0, 34, 38, 41, 0, 31, 32, 36, 0, 222, 226, 225,
            0, 76, 80, 83, 0, 57, 60, 65, 0, 29, 32, 37, 0, 20, 28, 31, 0, 30, 33, 38, 0, 31, 36, 42, 0, 42, 47, 53, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 173, 124, 0, 49, 80, 72, 0, 66, 72, 72, 0,
            29, 34, 38, 0, 23, 28, 31, 0, 30, 31, 35, 0, 59, 68, 65, 0, 20, 21, 25, 0, 31, 34, 39, 0, 198, 201, 206, 0,
            211, 213, 210, 0, 220, 222, 217, 0, 19, 23, 26, 0, 22, 27, 31, 0, 34, 37, 44, 0, 30, 35, 41, 0, 45, 50, 56,
            0, 23, 151, 118, 0, 21, 151, 117, 0, 23, 146, 117, 0, 22, 142, 115, 0, 0, 0, 0, 0, 29, 177, 127, 0, 36, 48,
            48, 0, 41, 44, 49, 0, 53, 56, 61, 0, 32, 36, 37, 0, 186, 226, 105, 0, 18, 28, 27, 0, 23, 27, 30, 0, 34, 35,
            39, 0, 196, 200, 208, 0, 187, 196, 194, 0, 191, 196, 192, 0, 29, 30, 34, 0, 24, 27, 32, 0, 26, 29, 34, 0,
            39, 44, 50, 0, 35, 40, 46, 0, 25, 157, 120, 0, 24, 155, 121, 0, 22, 149, 119, 0, 22, 147, 116, 0, 0, 0, 0,
            0, 29, 181, 130, 0, 36, 47, 47, 0, 37, 41, 44, 0, 49, 53, 56, 0, 2, 5, 1, 0, 139, 213, 50, 0, 27, 32, 28, 0,
            15, 16, 20, 0, 21, 22, 26, 0, 30, 34, 37, 0, 164, 186, 165, 0, 192, 218, 143, 0, 0, 0, 0, 0, 14, 14, 20, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 160, 120, 0, 23, 157, 120, 0, 22, 153, 119, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 29, 178, 123, 0, 0, 0, 0, 0, 43, 48, 51, 0, 37, 41, 44, 0, 40, 45, 48, 0, 38, 42, 41, 0, 188, 228, 99, 0,
            34, 37, 32, 0, 17, 16, 21, 0, 21, 22, 27, 0, 198, 225, 181, 0, 147, 197, 59, 0, 0, 0, 0, 0, 29, 32, 37, 0,
            0, 0, 0, 0, 36, 41, 47, 0, 0, 0, 0, 0, 24, 165, 123, 0, 24, 160, 120, 0, 24, 155, 119, 0, 24, 154, 120, 0,
            0, 0, 0, 0, 30, 190, 130, 0, 48, 65, 61, 0, 36, 40, 43, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 26, 7, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 129, 210, 47, 0, 154, 209, 76, 0, 13, 17, 20, 0, 16, 19, 24, 0, 43, 46,
            51, 0, 29, 34, 40, 0, 39, 44, 50, 0, 0, 0, 0, 0, 23, 164, 121, 0, 23, 158, 118, 0, 0, 0, 0, 0, 205, 204,
            204, 61, 0, 0, 0, 0, 24, 163, 122, 0, 0, 0, 0, 0, 73, 128, 110, 0, 39, 55, 52, 0, 72, 77, 81, 0, 41, 46, 50,
            0, 23, 28, 30, 0, 34, 38, 41, 0, 26, 29, 32, 0, 41, 43, 47, 0, 227, 229, 226, 0, 65, 69, 72, 0, 25, 29, 34,
            0, 45, 48, 53, 0, 32, 37, 41, 0, 22, 26, 30, 0, 37, 42, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 24, 170, 125, 0, 22, 172, 124, 0, 65, 95, 87, 0, 57, 63, 63, 0, 32, 37, 41, 0, 22, 27, 30, 0,
            33, 37, 39, 0, 56, 64, 65, 0, 29, 30, 34, 0, 20, 23, 28, 0, 212, 217, 223, 0, 221, 223, 220, 0, 226, 228,
            225, 0, 38, 41, 46, 0, 18, 21, 26, 0, 39, 42, 49, 0, 38, 43, 49, 0, 37, 42, 48, 0, 21, 152, 118, 0, 22, 150,
            117, 0, 22, 145, 116, 0, 0, 0, 0, 0, 25, 175, 124, 0, 40, 87, 71, 0, 19, 31, 31, 0, 28, 31, 36, 0, 31, 34,
            39, 0, 45, 49, 50, 0, 182, 220, 113, 0, 29, 39, 38, 0, 24, 28, 31, 0, 35, 36, 40, 0, 197, 202, 207, 0, 203,
            209, 206, 0, 191, 196, 192, 0, 42, 46, 49, 0, 34, 37, 42, 0, 41, 44, 49, 0, 39, 44, 50, 0, 40, 55, 58, 0,
            24, 156, 119, 0, 23, 154, 120, 0, 23, 151, 118, 0, 0, 0, 0, 0, 26, 178, 127, 0, 37, 69, 58, 0, 32, 38, 40,
            0, 32, 36, 39, 0, 36, 40, 43, 0, 50, 52, 48, 0, 111, 206, 12, 0, 33, 37, 36, 0, 26, 27, 31, 0, 15, 19, 22,
            0, 19, 19, 20, 0, 190, 201, 197, 0, 0, 0, 0, 0, 1, 4, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65, 54, 63,
            0, 26, 161, 121, 0, 24, 156, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 183, 126, 0, 0, 0, 0, 0, 37, 50, 48, 0, 33,
            38, 41, 0, 45, 49, 52, 0, 44, 48, 51, 0, 59, 63, 60, 0, 174, 212, 100, 0, 23, 25, 26, 0, 17, 16, 21, 0, 27,
            30, 29, 0, 190, 209, 187, 0, 0, 0, 0, 0, 197, 234, 140, 0, 0, 0, 0, 0, 28, 33, 37, 0, 0, 0, 0, 0, 30, 167,
            125, 0, 25, 166, 124, 0, 24, 160, 120, 0, 23, 157, 120, 0, 0, 0, 0, 0, 27, 185, 127, 0, 24, 191, 129, 0, 35,
            49, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 47, 50, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 234,
            150, 0, 145, 210, 66, 0, 124, 188, 49, 0, 10, 14, 17, 0, 10, 13, 18, 0, 46, 49, 54, 0, 24, 29, 35, 0, 0, 0,
            0, 0, 23, 171, 123, 0, 24, 163, 122, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 23, 159, 119, 0, 0, 0, 0,
            0, 26, 163, 121, 0, 43, 119, 89, 0, 51, 76, 70, 0, 54, 59, 62, 0, 44, 49, 53, 0, 41, 46, 50, 0, 111, 123,
            84, 0, 43, 47, 50, 0, 36, 40, 43, 0, 217, 223, 219, 0, 61, 62, 64, 0, 16, 17, 22, 0, 29, 34, 38, 0, 40, 43,
            48, 0, 28, 31, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 165, 123, 0, 26, 167,
            124, 0, 27, 169, 123, 0, 49, 104, 85, 0, 41, 53, 51, 0, 34, 39, 43, 0, 30, 35, 39, 0, 27, 32, 35, 0, 169,
            232, 81, 0, 30, 35, 38, 0, 31, 35, 38, 0, 71, 71, 73, 0, 214, 218, 217, 0, 216, 218, 217, 0, 38, 43, 47, 0,
            24, 27, 32, 0, 19, 22, 27, 0, 26, 31, 37, 0, 44, 49, 55, 0, 9, 58, 50, 0, 22, 151, 118, 0, 0, 0, 0, 0, 23,
            169, 124, 0, 25, 173, 123, 0, 24, 178, 126, 0, 52, 70, 66, 0, 36, 44, 46, 0, 41, 44, 49, 0, 31, 35, 38, 0,
            11, 20, 3, 0, 36, 41, 38, 0, 27, 30, 35, 0, 38, 42, 45, 0, 192, 196, 199, 0, 199, 206, 199, 0, 213, 215,
            212, 0, 37, 40, 45, 0, 32, 35, 40, 0, 21, 24, 29, 0, 23, 28, 34, 0, 45, 50, 56, 0, 29, 155, 121, 0, 24, 156,
            119, 0, 0, 0, 0, 0, 25, 174, 124, 0, 26, 178, 127, 0, 36, 175, 126, 0, 52, 62, 63, 0, 35, 39, 42, 0, 24, 28,
            31, 0, 39, 44, 47, 0, 181, 224, 101, 0, 3, 10, 21, 0, 24, 28, 31, 0, 29, 33, 36, 0, 39, 40, 43, 0, 0, 0, 0,
            0, 192, 201, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 41, 47, 0, 41, 46, 52, 0, 23, 161, 120, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 27, 179, 128, 0, 0, 0, 0, 0, 27, 185, 127, 0, 43, 67, 59, 0, 31, 36, 39, 0, 12, 16, 19,
            0, 47, 52, 55, 0, 19, 24, 29, 0, 185, 227, 94, 0, 15, 20, 23, 0, 18, 19, 23, 0, 16, 17, 21, 0, 0, 0, 0, 0,
            99, 149, 74, 0, 0, 0, 0, 0, 25, 24, 30, 0, 0, 0, 0, 0, 25, 30, 36, 0, 38, 43, 49, 0, 23, 166, 123, 0, 23,
            162, 121, 0, 0, 0, 0, 0, 28, 181, 125, 0, 28, 184, 127, 0, 29, 189, 129, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 33, 37, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 23, 21, 0, 166, 205, 115, 0, 155, 223, 75, 0, 144,
            211, 65, 0, 10, 14, 17, 0, 24, 27, 32, 0, 28, 31, 36, 0, 0, 0, 0, 0, 33, 38, 44, 0, 26, 167, 124, 0, 0, 0,
            0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 23, 154, 120, 0, 0, 0, 0, 0, 24, 160, 120, 0, 23, 162, 121, 0, 24, 167,
            123, 0, 51, 119, 96, 0, 60, 72, 72, 0, 56, 61, 65, 0, 55, 60, 64, 0, 36, 41, 45, 0, 24, 28, 31, 0, 33, 34,
            38, 0, 33, 37, 40, 0, 220, 222, 221, 0, 43, 46, 51, 0, 44, 49, 53, 0, 29, 30, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 159, 119, 0, 26, 162, 122, 0, 24, 165, 123, 0, 25, 168, 125, 0, 28,
            170, 124, 0, 46, 90, 75, 0, 61, 70, 69, 0, 35, 40, 44, 0, 31, 36, 40, 0, 44, 52, 64, 0, 159, 211, 61, 0, 24,
            28, 31, 0, 20, 23, 28, 0, 219, 225, 223, 0, 64, 66, 65, 0, 34, 39, 45, 0, 29, 34, 38, 0, 35, 38, 43, 0, 32,
            35, 42, 0, 35, 40, 46, 0, 39, 44, 50, 0, 0, 0, 0, 0, 25, 164, 123, 0, 26, 167, 124, 0, 25, 170, 124, 0, 26,
            173, 123, 0, 28, 119, 86, 0, 45, 59, 59, 0, 46, 49, 54, 0, 33, 36, 41, 0, 29, 33, 36, 0, 215, 240, 147, 0,
            25, 30, 23, 0, 35, 39, 42, 0, 30, 31, 36, 0, 192, 201, 200, 0, 210, 212, 209, 0, 22, 23, 28, 0, 35, 40, 44,
            0, 29, 32, 37, 0, 43, 46, 51, 0, 35, 40, 46, 0, 53, 55, 61, 0, 0, 0, 0, 0, 26, 169, 123, 0, 26, 172, 123, 0,
            28, 176, 126, 0, 26, 178, 127, 0, 46, 82, 68, 0, 15, 25, 26, 0, 39, 43, 46, 0, 32, 36, 39, 0, 32, 37, 40, 0,
            192, 244, 112, 0, 31, 37, 35, 0, 20, 24, 27, 0, 0, 0, 0, 0, 22, 23, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 28, 31, 36, 0, 18, 21, 26, 0, 41, 46, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 173, 125, 0, 0, 0, 0, 0, 25,
            177, 126, 0, 27, 180, 126, 0, 26, 184, 126, 0, 55, 65, 64, 0, 40, 44, 47, 0, 38, 42, 45, 0, 48, 52, 55, 0,
            67, 66, 68, 0, 152, 207, 58, 0, 21, 23, 25, 0, 0, 0, 0, 0, 22, 26, 29, 0, 0, 0, 0, 0, 73, 99, 51, 0, 0, 0,
            0, 0, 24, 25, 30, 0, 18, 23, 27, 0, 27, 32, 38, 0, 3, 38, 31, 0, 0, 0, 0, 0, 27, 175, 127, 0, 27, 179, 128,
            0, 25, 184, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 38, 42, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            24, 39, 7, 0, 8, 16, 9, 0, 9, 12, 11, 0, 187, 225, 121, 0, 149, 195, 48, 0, 20, 39, 0, 0, 16, 19, 24, 0, 0,
            0, 0, 0, 15, 20, 24, 0, 20, 25, 31, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 22, 148, 118, 0, 0, 0, 0,
            0, 23, 155, 118, 0, 23, 158, 120, 0, 23, 159, 119, 0, 24, 162, 121, 0, 35, 112, 84, 0, 53, 80, 73, 0, 45,
            53, 55, 0, 34, 39, 43, 0, 40, 45, 49, 0, 127, 139, 117, 0, 25, 29, 32, 0, 32, 36, 39, 0, 202, 206, 208, 0,
            78, 79, 81, 0, 33, 37, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 153, 117, 0,
            23, 157, 120, 0, 23, 159, 119, 0, 23, 164, 122, 0, 25, 166, 123, 0, 26, 169, 126, 0, 53, 168, 129, 0, 63,
            90, 83, 0, 39, 44, 48, 0, 43, 48, 52, 0, 43, 48, 51, 0, 24, 30, 27, 0, 20, 22, 19, 0, 21, 24, 29, 0, 218,
            223, 219, 0, 220, 222, 219, 0, 16, 17, 22, 0, 25, 30, 34, 0, 19, 22, 27, 0, 32, 35, 40, 0, 35, 40, 46, 0, 0,
            0, 0, 0, 26, 158, 121, 0, 23, 162, 121, 0, 24, 165, 122, 0, 26, 169, 125, 0, 28, 171, 125, 0, 23, 173, 125,
            0, 47, 85, 72, 0, 41, 49, 51, 0, 42, 45, 50, 0, 32, 35, 40, 0, 2, 5, 6, 0, 192, 233, 128, 0, 25, 30, 30, 0,
            29, 33, 36, 0, 207, 216, 212, 0, 213, 215, 213, 0, 85, 86, 88, 0, 30, 33, 38, 0, 36, 39, 44, 0, 33, 36, 41,
            0, 22, 27, 33, 0, 0, 0, 0, 0, 25, 161, 121, 0, 26, 167, 124, 0, 27, 170, 124, 0, 25, 173, 123, 0, 26, 177,
            126, 0, 29, 178, 126, 0, 38, 58, 52, 0, 35, 39, 42, 0, 34, 38, 41, 0, 47, 52, 55, 0, 42, 49, 41, 0, 168,
            220, 103, 0, 0, 0, 0, 0, 29, 30, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 27, 32, 0, 27, 28, 33, 0,
            32, 35, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 166, 123, 0, 0, 0, 0, 0, 25, 173, 125, 0, 26, 177, 126, 0, 26,
            178, 127, 0, 28, 182, 128, 0, 43, 183, 132, 0, 41, 52, 52, 0, 49, 53, 56, 0, 55, 59, 62, 0, 52, 56, 59, 0,
            175, 203, 99, 0, 0, 0, 0, 0, 16, 17, 21, 0, 0, 0, 0, 0, 158, 218, 63, 0, 0, 0, 0, 0, 24, 27, 32, 0, 18, 19,
            24, 0, 23, 26, 31, 0, 20, 25, 31, 0, 0, 0, 0, 0, 27, 170, 124, 0, 26, 174, 126, 0, 27, 178, 127, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 188, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 40, 43, 0, 41, 44, 50,
            0, 200, 240, 134, 0, 18, 24, 22, 0, 178, 222, 94, 0, 156, 203, 105, 0, 116, 173, 33, 0, 0, 0, 0, 0, 15, 16,
            21, 0, 22, 27, 31, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 22, 142, 115, 0, 0, 0, 0, 0, 24, 149, 117,
            0, 23, 153, 119, 0, 23, 155, 118, 0, 24, 159, 119, 0, 25, 161, 121, 0, 24, 163, 122, 0, 54, 109, 90, 0, 58,
            74, 73, 0, 34, 39, 43, 0, 28, 33, 37, 0, 90, 91, 96, 0, 22, 26, 29, 0, 43, 44, 48, 0, 28, 29, 31, 0, 22, 23,
            25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 146, 117, 0, 22, 149, 119, 0, 24,
            154, 120, 0, 22, 158, 120, 0, 24, 160, 120, 0, 24, 163, 122, 0, 26, 167, 124, 0, 26, 168, 122, 0, 57, 116,
            96, 0, 43, 57, 57, 0, 67, 72, 76, 0, 32, 37, 41, 0, 32, 40, 43, 0, 17, 24, 21, 0, 39, 43, 46, 0, 211, 212,
            216, 0, 222, 224, 221, 0, 54, 55, 57, 0, 30, 33, 38, 0, 24, 32, 35, 0, 18, 26, 29, 0, 0, 0, 0, 0, 23, 152,
            119, 0, 25, 157, 120, 0, 22, 160, 122, 0, 23, 162, 121, 0, 24, 165, 122, 0, 26, 169, 123, 0, 25, 171, 122,
            0, 25, 173, 123, 0, 44, 63, 59, 0, 44, 50, 53, 0, 44, 47, 52, 0, 28, 32, 35, 0, 27, 40, 4, 0, 24, 29, 32, 0,
            30, 34, 37, 0, 210, 213, 222, 0, 221, 225, 226, 0, 195, 195, 195, 0, 32, 33, 37, 0, 31, 34, 39, 0, 24, 27,
            32, 0, 0, 0, 0, 0, 25, 157, 120, 0, 24, 160, 120, 0, 23, 164, 121, 0, 25, 168, 124, 0, 25, 171, 124, 0, 27,
            173, 124, 0, 27, 176, 126, 0, 32, 84, 64, 0, 34, 44, 45, 0, 53, 57, 60, 0, 36, 40, 43, 0, 22, 26, 29, 0, 0,
            0, 0, 0, 24, 47, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 197, 203, 203, 0, 34, 37, 45, 0, 19, 24, 28, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 23, 159, 119, 0, 0, 0, 0, 0, 25, 166, 123, 0, 24, 170, 123, 0, 27, 173, 126, 0, 25,
            176, 125, 0, 25, 178, 124, 0, 28, 182, 128, 0, 56, 88, 77, 0, 29, 37, 39, 0, 51, 55, 58, 0, 45, 50, 53, 0,
            0, 0, 0, 0, 131, 203, 35, 0, 0, 0, 0, 0, 22, 26, 29, 0, 0, 0, 0, 0, 196, 225, 136, 0, 8, 6, 11, 0, 14, 15,
            20, 0, 20, 21, 26, 0, 0, 0, 0, 0, 26, 162, 122, 0, 26, 167, 124, 0, 24, 172, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 25, 183, 125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 45, 48, 0, 45, 49, 52, 0, 18, 22, 23,
            0, 177, 215, 85, 0, 29, 33, 33, 0, 6, 10, 19, 0, 205, 242, 144, 0, 0, 0, 0, 0, 142, 205, 52, 0, 19, 20, 25,
            0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 21, 135, 112, 0, 0, 0, 0, 0, 22, 142, 115, 0, 21, 146, 116, 0,
            23, 148, 116, 0, 23, 151, 118, 0, 21, 154, 120, 0, 24, 159, 119, 0, 24, 160, 120, 0, 25, 161, 121, 0, 59,
            99, 88, 0, 40, 52, 52, 0, 28, 33, 37, 0, 28, 33, 37, 0, 27, 32, 29, 0, 34, 38, 41, 0, 35, 36, 40, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 138, 114, 0, 21, 144, 116, 0, 22, 145, 116, 0, 22,
            149, 119, 0, 23, 153, 119, 0, 24, 158, 121, 0, 24, 160, 120, 0, 24, 163, 122, 0, 25, 166, 123, 0, 26, 167,
            124, 0, 39, 104, 80, 0, 61, 80, 76, 0, 36, 41, 45, 0, 58, 63, 66, 0, 107, 139, 32, 0, 27, 31, 34, 0, 30, 34,
            37, 0, 204, 210, 206, 0, 207, 207, 205, 0, 48, 49, 51, 0, 32, 37, 41, 0, 0, 0, 0, 0, 23, 143, 118, 0, 21,
            148, 118, 0, 23, 151, 118, 0, 25, 155, 119, 0, 24, 158, 121, 0, 23, 164, 122, 0, 24, 165, 123, 0, 25, 168,
            124, 0, 24, 171, 124, 0, 27, 171, 122, 0, 48, 73, 67, 0, 58, 63, 63, 0, 36, 41, 45, 0, 17, 22, 25, 0, 33,
            56, 16, 0, 31, 32, 36, 0, 22, 25, 30, 0, 219, 225, 223, 0, 216, 218, 215, 0, 226, 228, 225, 0, 21, 22, 27,
            0, 0, 0, 0, 0, 21, 148, 118, 0, 24, 152, 119, 0, 23, 157, 120, 0, 23, 159, 119, 0, 23, 164, 121, 0, 24, 167,
            123, 0, 25, 171, 126, 0, 26, 172, 123, 0, 27, 175, 125, 0, 51, 178, 133, 0, 62, 73, 73, 0, 35, 39, 42, 0, 0,
            0, 0, 0, 38, 44, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 166, 167, 171, 0, 193, 199, 199, 0, 191, 197,
            197, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 150, 118, 0, 0, 0, 0, 0, 23, 158, 118, 0, 25, 161, 121, 0, 25, 164, 122,
            0, 24, 170, 123, 0, 26, 172, 125, 0, 26, 177, 126, 0, 27, 180, 126, 0, 26, 179, 127, 0, 67, 85, 79, 0, 39,
            47, 49, 0, 0, 0, 0, 0, 35, 39, 42, 0, 0, 0, 0, 0, 31, 35, 36, 0, 0, 0, 0, 0, 21, 25, 28, 0, 190, 224, 144,
            0, 182, 216, 119, 0, 16, 16, 15, 0, 0, 0, 0, 0, 23, 153, 119, 0, 23, 157, 120, 0, 24, 163, 122, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 177, 126, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 111, 77, 0, 36, 41, 45,
            0, 59, 63, 66, 0, 32, 36, 39, 0, 171, 209, 61, 0, 49, 51, 38, 0, 13, 17, 18, 0, 0, 0, 0, 0, 183, 236, 99, 0,
            152, 210, 69, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 21, 128, 112, 0, 0, 0, 0, 0, 22, 135, 115, 0,
            20, 138, 114, 0, 20, 142, 115, 0, 22, 146, 116, 0, 22, 150, 117, 0, 22, 153, 119, 0, 24, 156, 119, 0, 23,
            158, 121, 0, 22, 161, 120, 0, 40, 119, 90, 0, 43, 73, 61, 0, 45, 50, 54, 0, 29, 34, 38, 0, 34, 39, 43, 0,
            34, 39, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 132, 112, 0, 21, 137, 114, 0,
            22, 140, 116, 0, 21, 144, 115, 0, 23, 148, 118, 0, 22, 150, 117, 0, 23, 153, 119, 0, 23, 157, 120, 0, 24,
            160, 120, 0, 23, 162, 121, 0, 24, 165, 122, 0, 24, 167, 123, 0, 49, 91, 77, 0, 22, 27, 31, 0, 48, 53, 57, 0,
            32, 36, 33, 0, 34, 37, 42, 0, 19, 23, 26, 0, 247, 248, 250, 0, 225, 227, 226, 0, 16, 17, 19, 0, 0, 0, 0, 0,
            19, 137, 113, 0, 22, 140, 116, 0, 20, 145, 115, 0, 21, 148, 118, 0, 23, 153, 119, 0, 22, 156, 119, 0, 23,
            159, 119, 0, 24, 163, 122, 0, 24, 165, 123, 0, 26, 169, 125, 0, 25, 171, 124, 0, 48, 103, 84, 0, 46, 61, 58,
            0, 36, 41, 45, 0, 22, 27, 30, 0, 198, 241, 117, 0, 25, 34, 34, 0, 35, 38, 43, 0, 210, 211, 215, 0, 220, 224,
            223, 0, 220, 222, 217, 0, 0, 0, 0, 0, 21, 139, 115, 0, 22, 147, 117, 0, 24, 149, 119, 0, 23, 154, 120, 0,
            23, 157, 120, 0, 25, 162, 120, 0, 25, 164, 122, 0, 26, 167, 124, 0, 24, 171, 126, 0, 25, 174, 124, 0, 24,
            176, 127, 0, 55, 88, 77, 0, 0, 0, 0, 0, 47, 50, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 32, 35, 0,
            32, 33, 35, 0, 191, 200, 199, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 144, 115, 0, 0, 0, 0, 0, 22, 150, 117, 0, 23,
            155, 120, 0, 23, 158, 120, 0, 23, 164, 122, 0, 24, 165, 122, 0, 26, 169, 121, 0, 23, 172, 122, 0, 26, 176,
            126, 0, 25, 178, 126, 0, 21, 182, 126, 0, 0, 0, 0, 0, 34, 38, 41, 0, 0, 0, 0, 0, 174, 223, 86, 0, 0, 0, 0,
            0, 23, 24, 28, 0, 29, 31, 35, 0, 23, 23, 26, 0, 184, 226, 96, 0, 0, 0, 0, 0, 21, 145, 117, 0, 23, 151, 118,
            0, 22, 156, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 171, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            28, 183, 126, 0, 27, 179, 123, 0, 42, 52, 51, 0, 33, 38, 41, 0, 29, 33, 36, 0, 35, 40, 36, 0, 174, 231, 101,
            0, 0, 0, 0, 0, 17, 16, 21, 0, 32, 51, 19, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 20, 122, 109, 0, 0,
            0, 0, 0, 19, 130, 111, 0, 20, 133, 113, 0, 20, 136, 113, 0, 21, 139, 115, 0, 21, 144, 115, 0, 23, 148, 118,
            0, 24, 152, 119, 0, 22, 154, 117, 0, 23, 157, 120, 0, 23, 159, 121, 0, 26, 158, 118, 0, 48, 95, 82, 0, 37,
            47, 48, 0, 36, 41, 45, 0, 40, 45, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18,
            126, 110, 0, 20, 131, 112, 0, 21, 133, 111, 0, 20, 138, 114, 0, 21, 141, 114, 0, 21, 144, 115, 0, 21, 148,
            118, 0, 22, 152, 118, 0, 24, 156, 119, 0, 23, 158, 118, 0, 23, 159, 119, 0, 26, 162, 122, 0, 25, 164, 122,
            0, 52, 95, 83, 0, 34, 37, 42, 0, 33, 38, 42, 0, 32, 36, 43, 0, 14, 22, 7, 0, 30, 34, 37, 0, 46, 49, 54, 0,
            206, 212, 211, 0, 0, 0, 0, 0, 19, 130, 111, 0, 19, 134, 114, 0, 21, 139, 115, 0, 23, 143, 116, 0, 22, 147,
            117, 0, 22, 150, 117, 0, 24, 154, 118, 0, 23, 157, 120, 0, 23, 161, 120, 0, 24, 163, 122, 0, 24, 165, 122,
            0, 24, 169, 125, 0, 28, 169, 122, 0, 53, 75, 70, 0, 38, 43, 47, 0, 32, 37, 40, 0, 40, 44, 47, 0, 25, 36, 28,
            0, 20, 24, 27, 0, 23, 27, 30, 0, 219, 225, 223, 0, 0, 0, 0, 0, 21, 134, 114, 0, 21, 139, 115, 0, 20, 143,
            114, 0, 22, 147, 117, 0, 23, 151, 118, 0, 22, 156, 121, 0, 24, 158, 121, 0, 24, 163, 122, 0, 25, 166, 123,
            0, 25, 168, 124, 0, 26, 172, 125, 0, 26, 174, 124, 0, 0, 0, 0, 0, 59, 84, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 22, 27, 32, 0, 20, 24, 27, 0, 31, 32, 37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 137, 114, 0, 0, 0, 0, 0,
            19, 143, 115, 0, 23, 148, 118, 0, 24, 152, 119, 0, 25, 157, 120, 0, 24, 160, 120, 0, 24, 165, 123, 0, 26,
            167, 124, 0, 27, 170, 124, 0, 27, 173, 124, 0, 25, 177, 126, 0, 0, 0, 0, 0, 52, 84, 73, 0, 0, 0, 0, 0, 31,
            33, 37, 0, 0, 0, 0, 0, 49, 59, 58, 0, 23, 27, 30, 0, 16, 20, 23, 0, 21, 25, 28, 0, 0, 0, 0, 0, 20, 138, 114,
            0, 21, 144, 116, 0, 24, 149, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 164, 121, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 26, 177, 126, 0, 28, 181, 127, 0, 27, 185, 127, 0, 40, 52, 52, 0, 12, 16, 19, 0, 47, 52,
            55, 0, 11, 11, 25, 0, 0, 0, 0, 0, 11, 20, 16, 0, 23, 24, 28, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0,
            19, 116, 105, 0, 0, 0, 0, 0, 19, 124, 109, 0, 20, 127, 111, 0, 19, 130, 111, 0, 20, 133, 113, 0, 20, 138,
            114, 0, 21, 143, 116, 0, 20, 144, 115, 0, 23, 148, 118, 0, 22, 153, 119, 0, 22, 156, 119, 0, 23, 157, 120,
            0, 23, 159, 119, 0, 60, 132, 111, 0, 69, 96, 89, 0, 32, 42, 44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 18, 120, 107, 0, 18, 123, 108, 0, 19, 127, 111, 0, 19, 132, 112, 0, 22, 135, 115, 0, 20,
            138, 114, 0, 22, 142, 115, 0, 22, 145, 116, 0, 22, 149, 119, 0, 22, 152, 118, 0, 22, 156, 121, 0, 23, 157,
            120, 0, 23, 162, 121, 0, 25, 164, 122, 0, 59, 96, 86, 0, 62, 70, 72, 0, 35, 40, 44, 0, 40, 45, 49, 0, 27,
            32, 42, 0, 42, 46, 49, 0, 46, 47, 51, 0, 0, 0, 0, 0, 18, 123, 108, 0, 20, 129, 110, 0, 19, 132, 112, 0, 19,
            137, 113, 0, 22, 140, 116, 0, 19, 144, 114, 0, 22, 147, 117, 0, 22, 152, 118, 0, 24, 156, 119, 0, 23, 157,
            118, 0, 24, 160, 120, 0, 23, 164, 122, 0, 25, 166, 123, 0, 20, 172, 123, 0, 55, 78, 72, 0, 53, 58, 62, 0,
            30, 35, 39, 0, 34, 40, 52, 0, 183, 226, 101, 0, 19, 23, 26, 0, 21, 24, 29, 0, 0, 0, 0, 0, 20, 127, 111, 0,
            20, 131, 114, 0, 20, 136, 113, 0, 22, 140, 116, 0, 20, 144, 116, 0, 22, 147, 117, 0, 22, 152, 118, 0, 24,
            156, 119, 0, 23, 159, 121, 0, 24, 163, 122, 0, 24, 165, 122, 0, 26, 169, 125, 0, 0, 0, 0, 0, 26, 172, 123,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 52, 56, 58, 0, 174, 219, 116, 0, 24, 29, 32, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 19, 130, 111, 0, 0, 0, 0, 0, 19, 137, 113, 0, 21, 141, 114, 0, 21, 144, 115, 0, 22, 150, 117, 0, 22, 153,
            119, 0, 23, 157, 120, 0, 22, 161, 120, 0, 24, 165, 123, 0, 25, 168, 122, 0, 25, 171, 123, 0, 0, 0, 0, 0, 26,
            177, 126, 0, 0, 0, 0, 0, 38, 42, 45, 0, 0, 0, 0, 0, 41, 41, 49, 0, 162, 219, 75, 0, 24, 28, 29, 0, 19, 20,
            24, 0, 0, 0, 0, 0, 19, 130, 111, 0, 20, 136, 113, 0, 22, 142, 115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            23, 157, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 172, 124, 0, 26, 177, 126, 0, 26, 178, 127, 0, 26,
            184, 126, 0, 48, 60, 60, 0, 43, 47, 50, 0, 63, 67, 70, 0, 0, 0, 0, 0, 57, 59, 56, 0, 26, 31, 33, 0, 0, 0, 0,
            0, 205, 204, 204, 61, 0, 0, 0, 0, 15, 112, 103, 0, 0, 0, 0, 0, 18, 118, 106, 0, 20, 122, 108, 0, 19, 126,
            110, 0, 21, 130, 111, 0, 21, 135, 112, 0, 20, 138, 114, 0, 22, 142, 115, 0, 24, 144, 116, 0, 23, 148, 118,
            0, 22, 152, 118, 0, 23, 155, 118, 0, 23, 157, 120, 0, 24, 159, 119, 0, 36, 123, 93, 0, 55, 88, 79, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 115, 106, 0, 17, 119, 106, 0, 20, 122, 108, 0, 18,
            126, 110, 0, 19, 130, 111, 0, 19, 132, 112, 0, 21, 139, 115, 0, 22, 140, 116, 0, 22, 145, 116, 0, 23, 148,
            118, 0, 22, 152, 118, 0, 22, 155, 120, 0, 25, 157, 120, 0, 23, 161, 121, 0, 31, 164, 124, 0, 66, 108, 98, 0,
            43, 54, 54, 0, 48, 53, 57, 0, 29, 34, 38, 0, 23, 23, 22, 0, 42, 46, 49, 0, 0, 0, 0, 0, 18, 118, 106, 0, 20,
            122, 109, 0, 21, 128, 112, 0, 18, 131, 111, 0, 20, 136, 113, 0, 21, 139, 115, 0, 20, 143, 115, 0, 23, 146,
            117, 0, 22, 149, 119, 0, 23, 154, 120, 0, 22, 156, 119, 0, 23, 159, 119, 0, 24, 163, 122, 0, 26, 167, 124,
            0, 54, 171, 132, 0, 73, 100, 93, 0, 44, 52, 54, 0, 41, 46, 50, 0, 18, 23, 26, 0, 209, 237, 147, 0, 27, 31,
            34, 0, 0, 0, 0, 0, 18, 123, 108, 0, 20, 127, 111, 0, 20, 131, 112, 0, 20, 136, 113, 0, 21, 139, 115, 0, 19,
            143, 115, 0, 23, 148, 118, 0, 23, 151, 118, 0, 24, 156, 119, 0, 23, 157, 120, 0, 23, 162, 121, 0, 24, 165,
            122, 0, 0, 0, 0, 0, 27, 170, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 48, 53, 0, 27, 31, 32, 0, 196,
            231, 129, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 125, 109, 0, 0, 0, 0, 0, 20, 131, 112, 0, 19, 135, 112, 0, 21, 141,
            114, 0, 22, 145, 117, 0, 22, 150, 117, 0, 22, 152, 118, 0, 23, 157, 120, 0, 24, 160, 120, 0, 24, 163, 122,
            0, 25, 166, 123, 0, 0, 0, 0, 0, 25, 171, 122, 0, 0, 0, 0, 0, 50, 65, 62, 0, 0, 0, 0, 0, 34, 38, 41, 0, 18,
            22, 25, 0, 160, 224, 71, 0, 15, 19, 18, 0, 0, 0, 0, 0, 18, 125, 109, 0, 18, 131, 111, 0, 19, 137, 113, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 152, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 167, 124, 0, 25,
            172, 124, 0, 25, 176, 125, 0, 27, 178, 127, 0, 28, 182, 128, 0, 40, 62, 59, 0, 27, 31, 34, 0, 0, 0, 0, 0,
            29, 34, 37, 0, 136, 205, 26, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 18, 111, 103, 0, 0, 0, 0, 0, 19,
            116, 105, 0, 20, 120, 108, 0, 19, 124, 109, 0, 20, 129, 110, 0, 20, 133, 113, 0, 20, 138, 114, 0, 21, 139,
            113, 0, 23, 143, 115, 0, 22, 147, 117, 0, 22, 150, 117, 0, 22, 153, 119, 0, 24, 156, 119, 0, 24, 159, 119,
            0, 41, 168, 128, 0, 49, 108, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 113,
            105, 0, 17, 117, 105, 0, 17, 122, 108, 0, 18, 125, 109, 0, 20, 128, 112, 0, 21, 132, 113, 0, 20, 136, 113,
            0, 21, 139, 115, 0, 21, 144, 116, 0, 21, 146, 116, 0, 21, 149, 119, 0, 23, 153, 119, 0, 24, 156, 119, 0, 22,
            160, 120, 0, 24, 165, 122, 0, 44, 112, 89, 0, 29, 50, 45, 0, 53, 58, 62, 0, 40, 45, 49, 0, 26, 31, 35, 0,
            139, 153, 109, 0, 0, 0, 0, 0, 18, 118, 106, 0, 18, 123, 109, 0, 20, 125, 110, 0, 17, 130, 110, 0, 21, 132,
            113, 0, 20, 138, 114, 0, 23, 141, 117, 0, 20, 144, 116, 0, 23, 148, 118, 0, 22, 151, 120, 0, 25, 156, 122,
            0, 22, 158, 120, 0, 25, 161, 121, 0, 24, 165, 122, 0, 23, 170, 125, 0, 52, 104, 87, 0, 56, 66, 67, 0, 32,
            37, 41, 0, 39, 44, 47, 0, 21, 25, 24, 0, 17, 19, 13, 0, 0, 0, 0, 0, 17, 119, 106, 0, 19, 126, 110, 0, 19,
            130, 111, 0, 21, 134, 114, 0, 20, 138, 114, 0, 22, 142, 117, 0, 21, 146, 116, 0, 24, 149, 117, 0, 23, 153,
            119, 0, 25, 157, 120, 0, 22, 161, 122, 0, 24, 163, 122, 0, 0, 0, 0, 0, 26, 169, 125, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 62, 65, 70, 0, 29, 33, 36, 0, 78, 92, 43, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 123, 108, 0, 0, 0,
            0, 0, 19, 130, 111, 0, 20, 134, 111, 0, 21, 137, 114, 0, 22, 142, 115, 0, 22, 147, 117, 0, 22, 150, 117, 0,
            24, 155, 121, 0, 23, 158, 118, 0, 25, 161, 121, 0, 25, 166, 123, 0, 0, 0, 0, 0, 26, 172, 125, 0, 0, 0, 0, 0,
            44, 75, 65, 0, 0, 0, 0, 0, 36, 40, 43, 0, 31, 36, 39, 0, 199, 222, 132, 0, 10, 35, 0, 0, 0, 0, 0, 0, 18,
            123, 108, 0, 18, 129, 110, 0, 20, 134, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 150, 117, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 165, 122, 0, 24, 170, 123, 0, 26, 173, 126, 0, 25, 176, 125, 0, 27, 181, 127,
            0, 50, 80, 70, 0, 28, 36, 38, 0, 0, 0, 0, 0, 49, 53, 56, 0, 50, 50, 64, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0,
            0, 0, 0, 17, 110, 102, 0, 0, 0, 0, 0, 19, 115, 104, 0, 18, 118, 106, 0, 20, 122, 108, 0, 19, 126, 110, 0,
            17, 130, 110, 0, 22, 134, 112, 0, 20, 138, 114, 0, 21, 141, 114, 0, 22, 145, 116, 0, 23, 147, 118, 0, 22,
            152, 118, 0, 23, 154, 120, 0, 23, 156, 119, 0, 24, 159, 119, 0, 43, 134, 103, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 111, 103, 0, 18, 115, 106, 0, 17, 119, 106, 0, 20, 122, 108, 0, 18,
            126, 110, 0, 19, 130, 111, 0, 19, 132, 112, 0, 20, 138, 114, 0, 22, 140, 116, 0, 21, 144, 115, 0, 22, 147,
            117, 0, 22, 152, 118, 0, 23, 154, 120, 0, 23, 159, 121, 0, 24, 163, 122, 0, 25, 163, 121, 0, 59, 105, 94, 0,
            44, 52, 54, 0, 37, 42, 46, 0, 49, 54, 58, 0, 47, 45, 53, 0, 0, 0, 0, 0, 18, 115, 106, 0, 17, 118, 106, 0,
            20, 122, 109, 0, 20, 127, 111, 0, 18, 130, 111, 0, 21, 134, 114, 0, 20, 138, 114, 0, 20, 142, 115, 0, 22,
            145, 116, 0, 22, 149, 119, 0, 22, 153, 119, 0, 25, 156, 122, 0, 23, 159, 119, 0, 24, 163, 122, 0, 25, 168,
            124, 0, 29, 166, 122, 0, 55, 85, 77, 0, 29, 34, 37, 0, 40, 45, 49, 0, 27, 32, 35, 0, 135, 201, 40, 0, 0, 0,
            0, 0, 16, 117, 105, 0, 18, 123, 108, 0, 19, 126, 110, 0, 19, 130, 111, 0, 22, 136, 113, 0, 21, 139, 115, 0,
            21, 144, 116, 0, 21, 146, 116, 0, 23, 151, 118, 0, 24, 155, 121, 0, 22, 156, 119, 0, 23, 162, 121, 0, 0, 0,
            0, 0, 24, 165, 122, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 48, 53, 0, 42, 45, 50, 0, 45, 49, 50, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 18, 120, 107, 0, 0, 0, 0, 0, 20, 127, 109, 0, 20, 131, 112, 0, 19, 135, 112, 0, 22,
            140, 114, 0, 22, 145, 117, 0, 21, 149, 116, 0, 23, 151, 118, 0, 25, 157, 120, 0, 24, 160, 120, 0, 24, 163,
            122, 0, 0, 0, 0, 0, 27, 170, 126, 0, 0, 0, 0, 0, 25, 177, 124, 0, 0, 0, 0, 0, 39, 43, 46, 0, 17, 21, 24, 0,
            18, 20, 24, 0, 130, 205, 48, 0, 0, 0, 0, 0, 17, 122, 108, 0, 20, 127, 111, 0, 19, 132, 112, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 23, 148, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 163, 122, 0, 27, 169, 123,
            0, 25, 171, 124, 0, 25, 176, 125, 0, 26, 180, 126, 0, 28, 182, 128, 0, 38, 57, 55, 0, 0, 0, 0, 0, 39, 43,
            46, 0, 48, 53, 56, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 15, 105, 98, 0, 0, 0, 0, 0, 16, 112, 104,
            0, 19, 115, 104, 0, 18, 118, 106, 0, 19, 122, 108, 0, 20, 128, 110, 0, 18, 130, 111, 0, 21, 135, 113, 0, 20,
            138, 114, 0, 22, 142, 116, 0, 22, 146, 116, 0, 22, 147, 118, 0, 22, 151, 118, 0, 22, 154, 118, 0, 23, 156,
            119, 0, 24, 159, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 110, 102, 0, 19,
            112, 104, 0, 18, 115, 106, 0, 18, 118, 106, 0, 18, 123, 108, 0, 19, 127, 111, 0, 20, 131, 112, 0, 21, 134,
            114, 0, 20, 138, 114, 0, 22, 140, 114, 0, 22, 145, 116, 0, 23, 148, 118, 0, 21, 151, 117, 0, 24, 156, 119,
            0, 24, 160, 120, 0, 24, 163, 122, 0, 30, 165, 124, 0, 50, 78, 71, 0, 68, 76, 78, 0, 32, 37, 41, 0, 16, 21,
            25, 0, 0, 0, 0, 0, 17, 110, 102, 0, 18, 115, 104, 0, 18, 120, 107, 0, 18, 123, 108, 0, 18, 126, 110, 0, 20,
            131, 112, 0, 19, 135, 112, 0, 20, 138, 114, 0, 21, 143, 116, 0, 22, 145, 116, 0, 22, 149, 119, 0, 22, 153,
            119, 0, 23, 157, 120, 0, 24, 160, 120, 0, 24, 165, 122, 0, 25, 167, 124, 0, 49, 124, 97, 0, 32, 46, 46, 0,
            47, 52, 56, 0, 28, 33, 37, 0, 17, 24, 22, 0, 0, 0, 0, 0, 17, 112, 104, 0, 18, 118, 106, 0, 18, 123, 109, 0,
            20, 127, 111, 0, 18, 129, 110, 0, 20, 136, 115, 0, 20, 138, 114, 0, 21, 143, 118, 0, 22, 147, 117, 0, 23,
            150, 120, 0, 24, 154, 120, 0, 24, 158, 121, 0, 0, 0, 0, 0, 24, 163, 122, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 35, 44, 43, 0, 24, 29, 33, 0, 46, 51, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 116, 105, 0, 0, 0, 0, 0, 18,
            123, 108, 0, 19, 128, 109, 0, 19, 132, 112, 0, 19, 137, 113, 0, 21, 141, 114, 0, 21, 144, 115, 0, 22, 150,
            117, 0, 24, 152, 119, 0, 22, 156, 119, 0, 23, 159, 119, 0, 0, 0, 0, 0, 24, 165, 122, 0, 0, 0, 0, 0, 28, 176,
            126, 0, 0, 0, 0, 0, 65, 73, 75, 0, 59, 63, 66, 0, 29, 33, 36, 0, 22, 23, 27, 0, 0, 0, 0, 0, 17, 117, 105, 0,
            18, 123, 108, 0, 20, 128, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 144, 115, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 23, 159, 119, 0, 25, 164, 122, 0, 27, 169, 123, 0, 26, 172, 125, 0, 27, 178, 127, 0, 26, 180,
            126, 0, 28, 182, 128, 0, 0, 0, 0, 0, 22, 26, 29, 0, 44, 48, 51, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0,
            0, 18, 103, 100, 0, 0, 0, 0, 0, 18, 109, 102, 0, 17, 112, 104, 0, 19, 116, 105, 0, 19, 119, 107, 0, 20, 125,
            110, 0, 21, 128, 112, 0, 21, 132, 113, 0, 20, 136, 113, 0, 22, 140, 116, 0, 20, 143, 118, 0, 20, 147, 117,
            0, 23, 150, 120, 0, 22, 154, 117, 0, 22, 156, 121, 0, 23, 157, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 15, 105, 101, 0, 17, 110, 102, 0, 17, 112, 104, 0, 19, 116, 105, 0, 19, 121, 108, 0,
            18, 125, 109, 0, 19, 127, 111, 0, 19, 130, 111, 0, 22, 136, 113, 0, 20, 138, 114, 0, 22, 142, 115, 0, 21,
            146, 116, 0, 22, 149, 119, 0, 22, 153, 119, 0, 23, 159, 119, 0, 23, 161, 120, 0, 23, 164, 122, 0, 49, 104,
            87, 0, 40, 59, 55, 0, 23, 28, 32, 0, 32, 37, 41, 0, 0, 0, 0, 0, 18, 109, 102, 0, 18, 113, 105, 0, 17, 117,
            105, 0, 16, 121, 107, 0, 19, 124, 109, 0, 18, 129, 110, 0, 20, 131, 112, 0, 20, 136, 113, 0, 21, 139, 115,
            0, 21, 144, 116, 0, 23, 148, 118, 0, 23, 150, 120, 0, 25, 155, 121, 0, 24, 158, 121, 0, 25, 164, 123, 0, 24,
            165, 122, 0, 22, 169, 124, 0, 65, 99, 89, 0, 60, 70, 72, 0, 40, 45, 49, 0, 38, 43, 46, 0, 0, 0, 0, 0, 18,
            111, 103, 0, 20, 116, 105, 0, 19, 121, 108, 0, 19, 124, 109, 0, 21, 128, 112, 0, 20, 133, 113, 0, 20, 138,
            114, 0, 22, 140, 116, 0, 21, 144, 115, 0, 22, 149, 119, 0, 23, 151, 118, 0, 25, 155, 119, 0, 0, 0, 0, 0, 23,
            162, 121, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 56, 79, 73, 0, 40, 45, 45, 0, 28, 33, 37, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 19, 115, 104, 0, 0, 0, 0, 0, 19, 121, 108, 0, 18, 125, 109, 0, 19, 130, 111, 0, 20, 133, 112, 0,
            21, 137, 114, 0, 23, 141, 115, 0, 22, 147, 117, 0, 22, 150, 117, 0, 24, 154, 120, 0, 24, 157, 119, 0, 0, 0,
            0, 0, 24, 165, 122, 0, 0, 0, 0, 0, 26, 174, 124, 0, 0, 0, 0, 0, 53, 69, 66, 0, 43, 47, 50, 0, 33, 37, 40, 0,
            38, 42, 45, 0, 0, 0, 0, 0, 17, 114, 103, 0, 18, 120, 107, 0, 18, 125, 109, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 21, 141, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 157, 120, 0, 25, 161, 121, 0, 26, 165, 123,
            0, 25, 171, 124, 0, 25, 176, 125, 0, 25, 178, 124, 0, 26, 179, 127, 0, 0, 0, 0, 0, 34, 46, 46, 0, 31, 35,
            38, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 17, 102, 99, 0, 0, 0, 0, 0, 18, 109, 102, 0, 17, 112, 104,
            0, 18, 115, 104, 0, 18, 118, 106, 0, 19, 124, 109, 0, 21, 128, 112, 0, 20, 131, 112, 0, 20, 136, 115, 0, 22,
            140, 116, 0, 21, 143, 116, 0, 22, 147, 115, 0, 22, 149, 119, 0, 22, 154, 117, 0, 23, 154, 120, 0, 23, 157,
            120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 105, 101, 0, 17, 110, 102, 0, 19,
            112, 104, 0, 18, 115, 104, 0, 18, 119, 106, 0, 19, 124, 109, 0, 19, 126, 110, 0, 19, 131, 112, 0, 21, 135,
            112, 0, 20, 138, 114, 0, 22, 141, 115, 0, 22, 147, 117, 0, 22, 148, 118, 0, 23, 154, 120, 0, 23, 158, 118,
            0, 25, 161, 121, 0, 24, 163, 121, 0, 51, 116, 94, 0, 56, 76, 72, 0, 68, 74, 76, 0, 33, 38, 42, 0, 0, 0, 0,
            0, 17, 108, 101, 0, 19, 112, 104, 0, 17, 117, 105, 0, 18, 120, 107, 0, 19, 124, 109, 0, 18, 129, 110, 0, 20,
            131, 112, 0, 20, 136, 113, 0, 21, 139, 115, 0, 21, 144, 116, 0, 23, 146, 117, 0, 22, 149, 119, 0, 23, 153,
            119, 0, 24, 158, 121, 0, 24, 163, 122, 0, 25, 166, 123, 0, 27, 167, 122, 0, 58, 104, 88, 0, 57, 67, 68, 0,
            29, 32, 37, 0, 19, 24, 27, 0, 0, 0, 0, 0, 18, 109, 102, 0, 19, 115, 104, 0, 19, 119, 107, 0, 21, 123, 109,
            0, 21, 128, 112, 0, 20, 131, 112, 0, 19, 137, 115, 0, 21, 139, 115, 0, 23, 143, 118, 0, 21, 148, 118, 0, 23,
            151, 118, 0, 25, 155, 121, 0, 0, 0, 0, 0, 25, 161, 121, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 39, 70, 62,
            0, 45, 49, 50, 0, 42, 47, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 113, 105, 0, 0, 0, 0, 0, 18, 120, 107, 0, 18,
            125, 109, 0, 19, 130, 111, 0, 19, 132, 112, 0, 21, 137, 114, 0, 23, 141, 115, 0, 21, 146, 116, 0, 23, 151,
            118, 0, 23, 153, 119, 0, 23, 157, 120, 0, 0, 0, 0, 0, 23, 164, 121, 0, 0, 0, 0, 0, 27, 173, 124, 0, 0, 0, 0,
            0, 38, 64, 55, 0, 32, 36, 39, 0, 49, 53, 56, 0, 27, 31, 34, 0, 0, 0, 0, 0, 19, 114, 106, 0, 17, 119, 106, 0,
            18, 125, 109, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 141, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            23, 157, 120, 0, 25, 161, 121, 0, 25, 164, 122, 0, 24, 170, 123, 0, 24, 175, 124, 0, 28, 177, 127, 0, 27,
            179, 127, 0, 0, 0, 0, 0, 34, 47, 47, 0, 31, 35, 38, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 17, 102,
            99, 0, 0, 0, 0, 0, 18, 109, 102, 0, 17, 112, 104, 0, 18, 115, 104, 0, 18, 118, 106, 0, 19, 124, 109, 0, 21,
            128, 112, 0, 20, 131, 112, 0, 20, 136, 115, 0, 22, 140, 116, 0, 20, 142, 117, 0, 21, 146, 114, 0, 22, 149,
            119, 0, 22, 152, 116, 0, 23, 154, 120, 0, 23, 157, 121, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 15, 104, 100, 0, 16, 109, 101, 0, 18, 111, 103, 0, 18, 115, 104, 0, 18, 119, 106, 0, 18, 123,
            108, 0, 19, 126, 110, 0, 19, 131, 112, 0, 20, 133, 113, 0, 19, 137, 113, 0, 22, 141, 115, 0, 22, 145, 116,
            0, 22, 148, 118, 0, 22, 153, 119, 0, 23, 158, 120, 0, 25, 161, 121, 0, 24, 163, 122, 0, 57, 125, 102, 0, 58,
            80, 74, 0, 38, 44, 47, 0, 43, 48, 52, 0, 0, 0, 0, 0, 17, 108, 101, 0, 19, 112, 104, 0, 19, 116, 105, 0, 18,
            120, 107, 0, 19, 124, 109, 0, 18, 129, 110, 0, 20, 131, 112, 0, 20, 136, 113, 0, 21, 139, 115, 0, 21, 144,
            116, 0, 22, 145, 116, 0, 22, 149, 119, 0, 23, 153, 119, 0, 24, 158, 121, 0, 24, 163, 122, 0, 24, 165, 122,
            0, 26, 167, 124, 0, 55, 103, 87, 0, 64, 74, 75, 0, 22, 25, 30, 0, 31, 36, 39, 0, 0, 0, 0, 0, 18, 109, 102,
            0, 19, 115, 104, 0, 19, 119, 107, 0, 18, 123, 109, 0, 21, 128, 112, 0, 20, 131, 112, 0, 19, 137, 115, 0, 21,
            139, 115, 0, 23, 143, 118, 0, 22, 147, 117, 0, 22, 150, 117, 0, 25, 155, 121, 0, 0, 0, 0, 0, 24, 160, 120,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 47, 81, 72, 0, 67, 71, 72, 0, 24, 29, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            18, 113, 105, 0, 0, 0, 0, 0, 18, 120, 107, 0, 18, 125, 109, 0, 20, 129, 110, 0, 19, 132, 112, 0, 18, 136,
            112, 0, 23, 141, 115, 0, 21, 146, 116, 0, 22, 150, 117, 0, 23, 153, 119, 0, 23, 157, 120, 0, 0, 0, 0, 0, 25,
            164, 123, 0, 0, 0, 0, 0, 27, 173, 124, 0, 0, 0, 0, 0, 52, 79, 70, 0, 35, 40, 43, 0, 40, 44, 47, 0, 34, 38,
            41, 0, 0, 0, 0, 0, 19, 114, 106, 0, 17, 119, 106, 0, 18, 125, 109, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            22, 140, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 157, 120, 0, 25, 161, 121, 0, 25, 164, 122, 0, 24,
            170, 123, 0, 25, 176, 125, 0, 27, 176, 126, 0, 26, 180, 126, 0, 0, 0, 0, 0, 31, 45, 45, 0, 26, 30, 33, 0, 0,
            0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 17, 102, 99, 0, 0, 0, 0, 0, 18, 109, 102, 0, 17, 112, 104, 0, 18,
            115, 104, 0, 18, 118, 106, 0, 19, 124, 109, 0, 21, 128, 112, 0, 20, 131, 112, 0, 20, 136, 115, 0, 22, 140,
            116, 0, 20, 142, 117, 0, 21, 146, 114, 0, 22, 149, 119, 0, 22, 152, 116, 0, 23, 154, 120, 0, 23, 157, 121,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 104, 100, 0, 16, 109, 101, 0, 18, 111,
            103, 0, 18, 115, 104, 0, 18, 119, 106, 0, 18, 123, 108, 0, 19, 126, 110, 0, 19, 131, 112, 0, 20, 133, 113,
            0, 19, 137, 113, 0, 22, 141, 115, 0, 22, 145, 116, 0, 22, 148, 118, 0, 22, 153, 119, 0, 23, 158, 120, 0, 25,
            161, 121, 0, 24, 163, 122, 0, 57, 125, 102, 0, 58, 80, 74, 0, 38, 44, 47, 0, 43, 48, 52, 0, 0, 0, 0, 0, 17,
            108, 101, 0, 19, 112, 104, 0, 19, 116, 105, 0, 18, 120, 107, 0, 19, 124, 109, 0, 18, 129, 110, 0, 20, 131,
            112, 0, 20, 136, 113, 0, 21, 139, 115, 0, 21, 144, 116, 0, 22, 145, 116, 0, 22, 149, 119, 0, 23, 153, 119,
            0, 24, 158, 121, 0, 24, 163, 122, 0, 24, 165, 122, 0, 26, 167, 124, 0, 55, 103, 87, 0, 64, 74, 75, 0, 22,
            25, 30, 0, 31, 36, 39, 0, 0, 0, 0, 0, 18, 109, 102, 0, 19, 115, 104, 0, 19, 119, 107, 0, 18, 123, 109, 0,
            21, 128, 112, 0, 20, 131, 112, 0, 19, 137, 115, 0, 21, 139, 115, 0, 23, 143, 118, 0, 22, 147, 117, 0, 22,
            150, 117, 0, 25, 155, 121, 0, 0, 0, 0, 0, 24, 160, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 47, 81, 72,
            0, 67, 71, 72, 0, 24, 29, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 113, 105, 0, 0, 0, 0, 0, 18, 120, 107, 0, 18,
            125, 109, 0, 20, 129, 110, 0, 19, 132, 112, 0, 18, 136, 112, 0, 23, 141, 115, 0, 21, 146, 116, 0, 22, 150,
            117, 0, 23, 153, 119, 0, 23, 157, 120, 0, 0, 0, 0, 0, 25, 164, 123, 0, 0, 0, 0, 0, 27, 173, 124, 0, 0, 0, 0,
            0, 52, 79, 70, 0, 35, 40, 43, 0, 40, 44, 47, 0, 34, 38, 41, 0, 0, 0, 0, 0, 19, 114, 106, 0, 17, 119, 106, 0,
            18, 125, 109, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 140, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            23, 157, 120, 0, 25, 161, 121, 0, 25, 164, 122, 0, 24, 170, 123, 0, 25, 176, 125, 0, 27, 176, 126, 0, 26,
            180, 126, 0, 0, 0, 0, 0, 31, 45, 45, 0, 26, 30, 33, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 17, 102,
            99, 0, 0, 0, 0, 0, 19, 110, 103, 0, 16, 111, 103, 0, 19, 115, 104, 0, 18, 118, 106, 0, 19, 124, 109, 0, 21,
            128, 112, 0, 20, 131, 112, 0, 19, 135, 114, 0, 22, 140, 116, 0, 20, 142, 115, 0, 21, 146, 114, 0, 23, 150,
            120, 0, 22, 152, 116, 0, 22, 153, 119, 0, 23, 157, 122, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 15, 104, 100, 0, 16, 109, 101, 0, 18, 111, 103, 0, 18, 115, 104, 0, 18, 118, 106, 0, 18, 123,
            108, 0, 18, 126, 110, 0, 19, 130, 111, 0, 20, 133, 113, 0, 19, 137, 113, 0, 22, 141, 114, 0, 22, 145, 116,
            0, 23, 148, 118, 0, 22, 153, 119, 0, 23, 158, 120, 0, 24, 160, 120, 0, 24, 162, 122, 0, 41, 111, 87, 0, 48,
            71, 65, 0, 39, 45, 47, 0, 31, 36, 40, 0, 0, 0, 0, 0, 17, 108, 101, 0, 19, 112, 104, 0, 19, 116, 105, 0, 17,
            119, 106, 0, 19, 124, 109, 0, 19, 127, 111, 0, 19, 130, 111, 0, 19, 135, 112, 0, 20, 138, 114, 0, 21, 144,
            116, 0, 22, 145, 116, 0, 22, 149, 119, 0, 23, 153, 119, 0, 23, 157, 120, 0, 24, 163, 122, 0, 24, 165, 122,
            0, 26, 167, 124, 0, 46, 97, 80, 0, 51, 61, 62, 0, 33, 36, 41, 0, 11, 16, 19, 0, 0, 0, 0, 0, 19, 110, 103, 0,
            19, 115, 104, 0, 19, 119, 107, 0, 18, 123, 109, 0, 21, 128, 112, 0, 20, 131, 112, 0, 20, 136, 115, 0, 21,
            139, 115, 0, 23, 143, 118, 0, 22, 147, 117, 0, 24, 149, 117, 0, 25, 155, 121, 0, 0, 0, 0, 0, 24, 160, 120,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 66, 104, 91, 0, 49, 53, 54, 0, 26, 31, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            17, 112, 104, 0, 0, 0, 0, 0, 18, 120, 107, 0, 19, 124, 109, 0, 20, 129, 110, 0, 19, 132, 112, 0, 18, 136,
            112, 0, 22, 140, 114, 0, 22, 145, 116, 0, 22, 150, 117, 0, 23, 153, 119, 0, 23, 157, 120, 0, 0, 0, 0, 0, 25,
            164, 123, 0, 0, 0, 0, 0, 26, 172, 123, 0, 0, 0, 0, 0, 46, 76, 66, 0, 36, 41, 44, 0, 32, 36, 39, 0, 43, 47,
            50, 0, 0, 0, 0, 0, 18, 113, 105, 0, 17, 119, 106, 0, 18, 125, 109, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            21, 139, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 156, 119, 0, 24, 160, 120, 0, 25, 164, 122, 0, 24,
            170, 123, 0, 25, 176, 125, 0, 27, 176, 126, 0, 26, 180, 126, 0, 0, 0, 0, 0, 40, 53, 53, 0, 19, 23, 26, 0, 0,
            0, 0, 0, type=ctyped.type.BYTE))

    @classmethod
    def chroma_link(cls):
        cls._device('ChromaLink', ctyped.array(
            1, 0, 0, 0, 0, 0, 26, 0, 0, 0, 205, 204, 204, 61, 174, 195, 174, 0, 35, 36, 38, 0, 225, 229, 228, 0, 211,
            213, 210, 0, 52, 55, 60, 0, 205, 204, 204, 61, 25, 26, 29, 0, 21, 25, 28, 0, 213, 216, 221, 0, 206, 208,
            205, 0, 94, 96, 95, 0, 205, 204, 204, 61, 20, 21, 25, 0, 37, 41, 44, 0, 31, 34, 39, 0, 208, 213, 216, 0,
            227, 229, 226, 0, 205, 204, 204, 61, 18, 20, 19, 0, 159, 228, 62, 0, 21, 25, 28, 0, 32, 37, 41, 0, 216, 222,
            220, 0, 205, 204, 204, 61, 148, 218, 88, 0, 17, 22, 25, 0, 192, 243, 108, 0, 29, 30, 34, 0, 30, 34, 37, 0,
            205, 204, 204, 61, 59, 67, 48, 0, 44, 49, 53, 0, 47, 54, 39, 0, 37, 40, 50, 0, 34, 38, 41, 0, 205, 204, 204,
            61, 34, 38, 41, 0, 29, 34, 38, 0, 31, 36, 39, 0, 10, 21, 5, 0, 20, 28, 30, 0, 205, 204, 204, 61, 34, 38, 41,
            0, 59, 68, 67, 0, 45, 50, 54, 0, 35, 40, 43, 0, 178, 229, 89, 0, 205, 204, 204, 61, 40, 44, 47, 0, 50, 91,
            79, 0, 56, 61, 65, 0, 23, 28, 32, 0, 32, 37, 40, 0, 205, 204, 204, 61, 31, 43, 43, 0, 26, 169, 125, 0, 51,
            100, 84, 0, 58, 68, 68, 0, 49, 54, 58, 0, 205, 204, 204, 61, 27, 181, 127, 0, 24, 163, 122, 0, 24, 167, 123,
            0, 29, 166, 122, 0, 52, 74, 69, 0, 205, 204, 204, 61, 28, 176, 126, 0, 24, 158, 121, 0, 24, 163, 122, 0, 25,
            166, 123, 0, 25, 168, 124, 0, 205, 204, 204, 61, 26, 169, 121, 0, 23, 153, 119, 0, 22, 156, 119, 0, 23, 159,
            119, 0, 24, 163, 121, 0, 205, 204, 204, 61, 23, 164, 122, 0, 22, 145, 116, 0, 24, 149, 119, 0, 23, 153, 119,
            0, 23, 158, 118, 0, 205, 204, 204, 61, 22, 154, 117, 0, 20, 138, 114, 0, 21, 144, 115, 0, 20, 147, 117, 0,
            22, 152, 118, 0, 205, 204, 204, 61, 22, 150, 117, 0, 21, 132, 113, 0, 20, 138, 114, 0, 21, 141, 114, 0, 22,
            145, 116, 0, 205, 204, 204, 61, 23, 143, 116, 0, 18, 126, 110, 0, 19, 132, 112, 0, 22, 136, 113, 0, 21, 139,
            115, 0, 205, 204, 204, 61, 21, 137, 114, 0, 18, 122, 108, 0, 19, 126, 110, 0, 20, 131, 112, 0, 22, 136, 113,
            0, 205, 204, 204, 61, 21, 135, 112, 0, 17, 118, 106, 0, 18, 125, 109, 0, 21, 130, 111, 0, 20, 133, 113, 0,
            205, 204, 204, 61, 20, 131, 112, 0, 17, 117, 105, 0, 18, 123, 108, 0, 19, 126, 110, 0, 19, 130, 111, 0, 205,
            204, 204, 61, 21, 129, 113, 0, 17, 114, 105, 0, 18, 118, 106, 0, 16, 123, 107, 0, 20, 127, 109, 0, 205, 204,
            204, 61, 18, 126, 110, 0, 17, 112, 104, 0, 19, 116, 105, 0, 18, 120, 107, 0, 19, 126, 110, 0, 205, 204, 204,
            61, 18, 126, 110, 0, 18, 111, 103, 0, 19, 116, 105, 0, 18, 120, 107, 0, 18, 125, 109, 0, 205, 204, 204, 61,
            19, 126, 110, 0, 18, 111, 103, 0, 19, 116, 105, 0, 18, 120, 107, 0, 18, 125, 109, 0, 205, 204, 204, 61, 19,
            126, 110, 0, 18, 111, 103, 0, 19, 116, 105, 0, 18, 120, 107, 0, 18, 125, 109, 0, 205, 204, 204, 61, 19, 126,
            110, 0, 18, 111, 103, 0, 19, 115, 104, 0, 18, 120, 107, 0, 18, 125, 109, 0, type=ctyped.type.BYTE))

    @classmethod
    def headset(cls):
        cls._device('Headset', ctyped.array(
            1, 0, 0, 0, 0, 1, 26, 0, 0, 0, 205, 204, 204, 61, 2, 3, 7, 0, 14, 18, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 205, 204, 204, 61, 11, 12, 16, 0, 24, 27, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204,
            61, 16, 17, 21, 0, 41, 44, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 12, 13, 17, 0, 29,
            33, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 35, 51, 50, 0, 14, 15, 19, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 31, 202, 132, 0, 23, 24, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 205, 204, 204, 61, 29, 200, 130, 0, 5, 6, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61,
            29, 198, 131, 0, 7, 8, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 29, 195, 131, 0, 23,
            24, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 29, 189, 129, 0, 16, 17, 21, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 28, 182, 128, 0, 22, 25, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 205, 204, 204, 61, 25, 176, 125, 0, 29, 199, 130, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204,
            204, 61, 26, 169, 125, 0, 30, 196, 130, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 24, 158,
            121, 0, 28, 190, 130, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 22, 152, 118, 0, 29, 183,
            126, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 23, 143, 116, 0, 28, 176, 126, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 20, 136, 113, 0, 26, 169, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 205, 204, 204, 61, 20, 131, 112, 0, 24, 165, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204,
            204, 61, 20, 129, 110, 0, 24, 163, 122, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 18, 125,
            109, 0, 24, 160, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 18, 123, 109, 0, 22, 156,
            119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 18, 118, 106, 0, 24, 154, 118, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 18, 118, 106, 0, 21, 151, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 205, 204, 204, 61, 17, 118, 106, 0, 21, 151, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204,
            204, 61, 17, 118, 106, 0, 21, 151, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 17, 118,
            106, 0, 22, 150, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, type=ctyped.type.BYTE))

    @classmethod
    def mousepad(cls):
        cls._device('Mousepad', ctyped.array(
            1, 0, 0, 0, 0, 2, 26, 0, 0, 0, 205, 204, 204, 61, 20, 138, 114, 0, 22, 145, 116, 0, 24, 154, 120, 0, 22,
            158, 118, 0, 24, 166, 123, 0, 27, 176, 124, 0, 162, 217, 126, 0, 50, 143, 0, 0, 25, 30, 33, 0, 19, 22, 27,
            0, 36, 41, 44, 0, 14, 15, 19, 0, 30, 31, 35, 0, 20, 30, 17, 0, 20, 26, 26, 0, 205, 204, 204, 61, 21, 141,
            114, 0, 22, 150, 117, 0, 23, 157, 120, 0, 25, 164, 123, 0, 27, 168, 123, 0, 31, 174, 126, 0, 120, 198, 62,
            0, 22, 69, 11, 0, 30, 34, 37, 0, 11, 14, 19, 0, 38, 48, 49, 0, 31, 35, 38, 0, 33, 37, 40, 0, 35, 40, 43, 0,
            35, 40, 43, 0, 205, 204, 204, 61, 21, 144, 116, 0, 22, 153, 119, 0, 24, 160, 120, 0, 25, 166, 123, 0, 28,
            172, 126, 0, 30, 180, 124, 0, 125, 214, 70, 0, 136, 199, 50, 0, 12, 16, 21, 0, 26, 29, 34, 0, 37, 56, 54, 0,
            42, 52, 51, 0, 22, 26, 29, 0, 31, 35, 38, 0, 33, 38, 42, 0, 205, 204, 204, 61, 22, 149, 119, 0, 24, 158,
            121, 0, 26, 165, 123, 0, 26, 172, 125, 0, 28, 177, 125, 0, 114, 194, 69, 0, 82, 154, 47, 0, 24, 29, 32, 0,
            5, 8, 13, 0, 40, 48, 50, 0, 52, 83, 70, 0, 22, 213, 136, 0, 23, 28, 31, 0, 49, 53, 56, 0, 28, 33, 36, 0,
            205, 204, 204, 61, 20, 156, 120, 0, 24, 163, 122, 0, 25, 171, 124, 0, 26, 177, 126, 0, 26, 184, 126, 0, 117,
            211, 60, 0, 163, 229, 85, 0, 12, 16, 19, 0, 31, 34, 39, 0, 26, 40, 40, 0, 29, 212, 134, 0, 29, 205, 132, 0,
            25, 199, 130, 0, 20, 33, 33, 0, 69, 92, 86, 0, 205, 204, 204, 61, 53, 56, 61, 0, 11, 42, 36, 0, 32, 47, 48,
            0, 27, 181, 127, 0, 44, 186, 140, 0, 68, 147, 4, 0, 25, 31, 31, 0, 18, 21, 26, 0, 37, 42, 45, 0, 54, 80, 71,
            0, 28, 210, 135, 0, 32, 203, 133, 0, 29, 193, 130, 0, 33, 181, 129, 0, 60, 122, 99, 0, 205, 204, 204, 61,
            35, 40, 46, 0, 44, 49, 55, 0, 41, 46, 52, 0, 32, 187, 129, 0, 126, 199, 64, 0, 125, 203, 34, 0, 30, 34, 37,
            0, 13, 16, 21, 0, 36, 46, 47, 0, 43, 80, 62, 0, 29, 208, 134, 0, 31, 197, 131, 0, 28, 190, 130, 0, 26, 180,
            126, 0, 26, 167, 124, 0, 205, 204, 204, 61, 34, 39, 45, 0, 16, 21, 27, 0, 24, 29, 32, 0, 32, 36, 35, 0, 88,
            200, 36, 0, 168, 232, 90, 0, 9, 12, 17, 0, 40, 43, 48, 0, 34, 48, 48, 0, 31, 211, 135, 0, 32, 203, 132, 0,
            30, 196, 132, 0, 28, 187, 129, 0, 27, 178, 127, 0, 25, 165, 123, 0, 205, 204, 204, 61, 26, 27, 32, 0, 24,
            28, 32, 0, 14, 19, 23, 0, 11, 20, 19, 0, 0, 74, 0, 0, 20, 25, 28, 0, 7, 10, 15, 0, 32, 36, 39, 0, 35, 58,
            50, 0, 33, 209, 134, 0, 30, 200, 131, 0, 28, 191, 128, 0, 27, 185, 127, 0, 25, 174, 124, 0, 25, 163, 122, 0,
            205, 204, 204, 61, 23, 26, 31, 0, 22, 25, 30, 0, 36, 39, 44, 0, 7, 11, 14, 0, 128, 225, 49, 0, 18, 22, 25,
            0, 14, 17, 22, 0, 35, 45, 46, 0, 30, 212, 133, 0, 29, 205, 130, 0, 26, 196, 131, 0, 27, 187, 127, 0, 26,
            179, 125, 0, 26, 169, 123, 0, 23, 158, 118, 0, 205, 204, 204, 61, 17, 22, 26, 0, 185, 191, 199, 0, 45, 68,
            23, 0, 12, 13, 18, 0, 20, 21, 25, 0, 26, 27, 31, 0, 35, 43, 45, 0, 38, 73, 59, 0, 30, 206, 133, 0, 28, 197,
            130, 0, 28, 187, 129, 0, 25, 178, 124, 0, 25, 171, 124, 0, 24, 163, 122, 0, 22, 152, 118, 0, 205, 204, 204,
            61, 214, 216, 213, 0, 195, 201, 201, 0, 131, 205, 51, 0, 10, 11, 15, 0, 6, 7, 11, 0, 33, 37, 40, 0, 27, 48,
            41, 0, 31, 209, 135, 0, 30, 201, 131, 0, 28, 191, 128, 0, 27, 180, 126, 0, 25, 171, 124, 0, 25, 164, 123, 0,
            24, 156, 119, 0, 21, 145, 116, 0, 205, 204, 204, 61, 35, 39, 42, 0, 19, 23, 26, 0, 200, 226, 126, 0, 11, 12,
            16, 0, 15, 16, 20, 0, 25, 35, 36, 0, 24, 214, 133, 0, 30, 204, 132, 0, 29, 195, 131, 0, 29, 184, 126, 0, 25,
            171, 124, 0, 25, 163, 121, 0, 23, 157, 120, 0, 22, 150, 117, 0, 21, 139, 115, 0, 205, 204, 204, 61, 13, 17,
            20, 0, 23, 29, 29, 0, 84, 109, 58, 0, 8, 9, 13, 0, 41, 46, 49, 0, 28, 207, 134, 0, 30, 204, 132, 0, 30, 196,
            132, 0, 28, 186, 128, 0, 27, 175, 125, 0, 23, 162, 121, 0, 23, 153, 119, 0, 21, 148, 118, 0, 21, 141, 114,
            0, 18, 131, 111, 0, 205, 204, 204, 61, 27, 32, 36, 0, 15, 23, 7, 0, 36, 41, 44, 0, 10, 11, 15, 0, 41, 58,
            52, 0, 30, 206, 133, 0, 29, 198, 129, 0, 27, 189, 129, 0, 26, 179, 125, 0, 25, 166, 123, 0, 23, 155, 118, 0,
            22, 145, 116, 0, 21, 141, 114, 0, 21, 132, 113, 0, 18, 125, 109, 0, 205, 204, 204, 61, 32, 37, 41, 0, 31,
            34, 39, 0, 29, 33, 36, 0, 13, 19, 19, 0, 21, 214, 131, 0, 30, 201, 131, 0, 28, 192, 129, 0, 28, 182, 128, 0,
            24, 170, 123, 0, 24, 159, 119, 0, 22, 147, 117, 0, 20, 138, 114, 0, 21, 132, 113, 0, 19, 127, 111, 0, 18,
            118, 106, 0, 205, 204, 204, 61, 47, 83, 69, 0, 45, 50, 53, 0, 37, 42, 46, 0, 31, 201, 132, 0, 31, 205, 133,
            0, 29, 195, 129, 0, 27, 187, 127, 0, 27, 175, 125, 0, 24, 163, 122, 0, 22, 152, 118, 0, 20, 138, 114, 0, 19,
            130, 111, 0, 19, 126, 110, 0, 18, 120, 107, 0, 17, 112, 104, 0, 205, 204, 204, 61, 50, 145, 111, 0, 49, 79,
            71, 0, 1, 55, 34, 0, 28, 197, 130, 0, 29, 200, 130, 0, 28, 191, 128, 0, 26, 180, 126, 0, 24, 170, 123, 0,
            23, 157, 120, 0, 21, 146, 116, 0, 19, 132, 112, 0, 19, 124, 109, 0, 19, 121, 108, 0, 18, 115, 104, 0, 18,
            109, 102, 0, 205, 204, 204, 61, 25, 161, 121, 0, 63, 110, 92, 0, 28, 186, 128, 0, 30, 196, 132, 0, 29, 198,
            129, 0, 27, 189, 129, 0, 26, 179, 125, 0, 26, 167, 124, 0, 24, 155, 121, 0, 21, 144, 115, 0, 19, 130, 111,
            0, 18, 123, 109, 0, 18, 118, 106, 0, 17, 112, 104, 0, 16, 107, 100, 0, 205, 204, 204, 61, 23, 159, 119, 0,
            26, 174, 124, 0, 27, 185, 127, 0, 30, 194, 131, 0, 30, 197, 128, 0, 27, 187, 127, 0, 28, 176, 126, 0, 24,
            165, 122, 0, 22, 152, 118, 0, 22, 140, 116, 0, 19, 127, 111, 0, 19, 121, 108, 0, 17, 117, 105, 0, 16, 111,
            103, 0, 16, 105, 99, 0, 205, 204, 204, 61, 22, 157, 120, 0, 24, 171, 122, 0, 28, 183, 126, 0, 28, 192, 129,
            0, 27, 193, 129, 0, 26, 183, 128, 0, 25, 171, 124, 0, 23, 159, 119, 0, 23, 148, 118, 0, 20, 136, 113, 0, 18,
            125, 109, 0, 17, 117, 105, 0, 17, 112, 104, 0, 16, 108, 101, 0, 16, 102, 99, 0, 205, 204, 204, 61, 23, 157,
            120, 0, 26, 169, 125, 0, 25, 179, 125, 0, 27, 189, 129, 0, 28, 191, 128, 0, 27, 180, 126, 0, 26, 169, 123,
            0, 23, 157, 120, 0, 21, 146, 116, 0, 18, 134, 113, 0, 19, 121, 108, 0, 19, 114, 106, 0, 17, 110, 102, 0, 16,
            105, 101, 0, 16, 101, 98, 0, 205, 204, 204, 61, 22, 156, 119, 0, 26, 169, 125, 0, 27, 180, 126, 0, 29, 189,
            129, 0, 28, 190, 130, 0, 26, 179, 125, 0, 25, 168, 122, 0, 24, 156, 119, 0, 21, 144, 115, 0, 20, 133, 113,
            0, 19, 121, 108, 0, 18, 113, 105, 0, 17, 110, 102, 0, 15, 104, 100, 0, 15, 100, 97, 0, 205, 204, 204, 61,
            22, 156, 119, 0, 26, 169, 125, 0, 27, 180, 126, 0, 29, 189, 129, 0, 28, 190, 130, 0, 26, 179, 125, 0, 25,
            168, 122, 0, 24, 156, 119, 0, 21, 144, 115, 0, 20, 133, 113, 0, 19, 121, 108, 0, 18, 113, 105, 0, 17, 110,
            102, 0, 16, 105, 101, 0, 15, 100, 97, 0, 205, 204, 204, 61, 22, 156, 119, 0, 26, 169, 125, 0, 27, 180, 126,
            0, 29, 189, 129, 0, 28, 190, 130, 0, 26, 179, 125, 0, 25, 168, 122, 0, 24, 156, 119, 0, 21, 144, 115, 0, 20,
            133, 113, 0, 19, 121, 108, 0, 18, 113, 105, 0, 17, 110, 102, 0, 16, 105, 101, 0, 15, 100, 97, 0, 205, 204,
            204, 61, 22, 156, 119, 0, 26, 169, 125, 0, 26, 179, 125, 0, 29, 189, 129, 0, 28, 190, 130, 0, 26, 179, 125,
            0, 25, 168, 122, 0, 24, 156, 119, 0, 21, 144, 115, 0, 19, 132, 112, 0, 18, 120, 107, 0, 18, 113, 105, 0, 17,
            110, 102, 0, 16, 105, 101, 0, 15, 100, 97, 0, type=ctyped.type.BYTE))

    @classmethod
    def mouse(cls):
        cls._device('Mouse', ctyped.array(
            1, 0, 0, 0, 1, 2, 26, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 17, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28,
            33, 39, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 20, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 45, 51, 0, 5, 15,
            4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 30, 36, 0, 23, 26, 31, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 34, 40, 0, 5, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 45, 49, 0, 18, 19, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 42, 47, 53, 0, 40, 43, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 31,
            35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204,
            61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 176, 192, 175, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 37, 43, 0, 137, 206, 35, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 14, 15, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33, 38, 44, 0, 157, 208, 81, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 31, 37, 0, 121, 186, 39, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 23, 28, 36, 0, 171, 210, 103, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            46, 51, 55, 0, 6, 10, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 35, 38, 0, 18,
            23, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 20, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 19, 24, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 193, 205, 197, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 29, 34, 0, 112, 183, 37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 7, 11, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 23, 26, 31, 0, 162, 187, 175, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            32, 37, 41, 0, 156, 213, 81, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 28, 33, 0,
            130, 203, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 38, 43, 0, 23, 27, 29, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 30, 35, 0, 38, 46, 49, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 12, 16, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 50, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 30, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9,
            10, 15, 0, 20, 24, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 208, 231, 148, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 17, 22, 0,
            18, 32, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 14, 0, 174, 215, 84, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 18, 23, 0, 147, 208, 71, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 12, 16, 0, 10, 18, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 15, 18, 23, 0, 6, 11, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 17, 21, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 34, 39, 43, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36,
            40, 43, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 37, 42, 0, 23, 24, 28, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 210, 243, 166, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 27, 31, 0, 19, 20, 22, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 24, 27, 0, 6, 19, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 10, 14, 17, 0, 164, 212, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 15, 19, 22, 0, 11, 12, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 16,
            20, 0, 22, 26, 29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 8, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 27, 32, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 34, 37, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 187, 129, 0, 26, 27, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 25, 28, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 135, 200, 43, 0, 21, 24, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 132, 195, 51, 0, 9, 30, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 131, 193,
            56, 0, 186, 223, 96, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 161, 195, 100, 0, 12,
            15, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 8, 6, 0, 20, 21, 25, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 11, 12, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 37, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 38, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 192, 201, 200, 0, 24, 33, 29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 24, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 206, 236,
            133, 0, 143, 205, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 73, 124, 16, 0, 181,
            217, 92, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 146, 200, 62, 0, 12, 13, 17, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 206, 58, 0, 15, 20, 24, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 27, 12, 0, 12, 13, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12, 16,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 38, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 183, 236, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 199, 205, 205, 0,
            145, 216, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 24, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 39, 3, 0, 190, 224, 104,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 129, 174, 39, 0, 69, 70, 72, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 167, 230, 83, 0, 30, 36, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 125, 197, 46, 0, 20, 24, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 86, 155, 0, 0, 14, 15, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 13, 17, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 3, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204,
            204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 73, 74, 78, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 31, 35, 0, 26, 29, 37, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 30, 34, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 23, 27, 0, 27, 32, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 32, 26, 0, 30, 35, 39, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 34, 45, 37, 0, 37, 41, 44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 199, 234,
            114, 0, 37, 41, 44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 123, 176, 30, 0, 30, 31,
            35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 8, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 14, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 38, 42, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 21, 22, 26, 0, 28, 32, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 186, 236, 107, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 19, 20, 24, 0, 51, 55, 58, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 24, 28,
            0, 37, 41, 44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 27, 26, 0, 35, 39, 42, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 148, 180, 105, 0, 23, 27, 30, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 78, 100, 49, 0, 35, 39, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12,
            16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 44, 49, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 29, 39, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 32, 0, 0, 37,
            47, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 39, 43, 46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 153, 228, 75, 0, 49, 59, 60, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 147, 203, 58, 0, 50, 60, 61, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 171, 209, 61, 0, 43, 39, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 1, 0, 39, 51, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 28, 32, 29, 0, 59, 152, 115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 20, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 19,
            23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204,
            61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 176, 126, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 42, 46, 48, 0, 25, 180, 126, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 29, 33, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 42, 47, 50, 0, 29, 183, 129, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 47, 51, 54, 0, 28, 186, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 42, 46, 49, 0, 28, 188, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            15, 19, 22, 0, 28, 190, 130, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 39, 42, 0,
            29, 192, 129, 0, 0, 0, 0, 0, 0, 0, 0, 0, 55, 195, 139, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33, 37, 40, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 172, 125, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 38, 43, 0, 27, 175, 125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 43, 86, 69, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 20, 24, 27, 0, 27, 178, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 25, 29, 32, 0, 26, 180, 126, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 45,
            48, 0, 25, 184, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 39, 43, 46, 0, 26, 185,
            127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 55, 59, 62, 0, 28, 187, 129, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 29, 198, 129, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 33, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 166, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 49, 82, 71, 0, 25, 168, 122, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 172, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            47, 80, 69, 0, 24, 170, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 55, 88, 75, 0,
            26, 174, 126, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 62, 48, 0, 27, 175, 125, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 187, 128, 0, 25, 178, 124, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 194, 128, 0, 27, 180, 126, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28,
            190, 130, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 192, 129, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 23, 159, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26,
            173, 123, 0, 25, 161, 121, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 167, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 176, 126,
            0, 24, 165, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 178, 127, 0, 25, 166,
            123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 181, 127, 0, 26, 169, 123, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 184, 126, 0, 24, 172, 124, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 185, 127, 0, 25, 173, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 185,
            127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 186, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 23, 154, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 169, 125,
            0, 21, 155, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 162, 121, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 171, 126, 0, 23,
            157, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 173, 124, 0, 24, 160, 120, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 176, 125, 0, 24, 163, 122, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 179, 125, 0, 23, 165, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 180, 126, 0, 25, 168, 125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 178, 124, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 27, 181, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 22, 147, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 163, 122, 0, 24,
            149, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 156, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 164, 122, 0, 22, 150, 117,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 166, 123, 0, 23, 153, 119, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 171, 124, 0, 22, 156, 121, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 171, 124, 0, 23, 157, 122, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 26, 174, 126, 0, 23, 159, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 171, 124, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 25, 176, 125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            22, 142, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 158, 121, 0, 21, 144, 115,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 151, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 160, 120, 0, 22, 147, 117, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 163, 122, 0, 23, 149, 118, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 164, 122, 0, 22, 150, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 25, 167, 124, 0, 22, 152, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 26, 169, 123, 0, 23, 154, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 165, 122, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            25, 171, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205,
            204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 140,
            116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 157, 120, 0, 22, 142, 117, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 24, 149, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 159, 119, 0, 22, 145, 117, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 161, 121, 0, 22, 145, 116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 163, 121, 0, 24, 149, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 23, 165, 122, 0, 23, 151, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            25, 168, 124, 0, 22, 152, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 165, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 169,
            125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204,
            61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 138, 114, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 154, 120, 0, 22, 140, 116, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 22, 147, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 157, 120, 0, 22, 142, 115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 159, 119, 0, 21, 144, 116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 23, 162, 121, 0, 22, 145, 116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 24, 163, 121, 0, 22, 147, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 163,
            121, 0, 22, 150, 117, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 161, 121, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 165, 123, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 133, 113, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 151, 118, 0, 20, 136, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            23, 143, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 153, 119, 0, 22, 138, 115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 157, 120, 0, 22, 138, 115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 23, 157, 120, 0, 22, 142, 115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            24, 160, 120, 0, 21, 144, 116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 160, 120,
            0, 20, 145, 115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 157, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 163, 122, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 131, 111, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 148, 118, 0, 20, 133, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 140,
            116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 151, 118, 0, 21, 135, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 22, 153, 119, 0, 20, 138, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 23, 155, 121, 0, 20, 138, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 156,
            119, 0, 21, 141, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 158, 120, 0, 21,
            144, 116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 155, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 160, 120, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 131, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 148, 118, 0, 19, 132, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 139, 115,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 150, 117, 0, 20, 134, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 23, 153, 119, 0, 21, 137, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            24, 155, 121, 0, 20, 138, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 157, 120,
            0, 20, 140, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 157, 120, 0, 20, 143,
            115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 154, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 159, 119, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 131, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 148, 118, 0, 19, 132, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 139, 115, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 22, 149, 117, 0, 20, 134, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 23, 152, 118, 0, 21, 137, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 154,
            120, 0, 20, 138, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 157, 120, 0, 20,
            140, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 156, 119, 0, 20, 143, 115, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 23, 154, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 159, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 131, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 23, 148, 118, 0, 19, 132, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 139, 115, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 22, 149, 117, 0, 20, 134, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            23, 152, 118, 0, 21, 137, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 154, 120,
            0, 20, 138, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 157, 120, 0, 20, 140,
            113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 156, 119, 0, 20, 143, 115, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 23, 154, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 159, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 205, 204, 204, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 131, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 23, 148, 118, 0, 20, 131, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 139, 115, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 22, 149, 117, 0, 19, 134, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 152,
            118, 0, 21, 137, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 154, 120, 0, 20,
            138, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 157, 120, 0, 21, 139, 115, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 156, 119, 0, 20, 143, 115, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 23, 154, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 159, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, type=ctyped.type.BYTE))

    @classmethod
    def keypad(cls):
        cls._device('Keypad', ctyped.array(
            1, 0, 0, 0, 1, 1, 26, 0, 0, 0, 205, 204, 204, 61, 217, 219, 216, 0, 52, 53, 58, 0, 25, 28, 33, 0, 34, 37,
            42, 0, 40, 41, 46, 0, 208, 210, 207, 0, 37, 38, 40, 0, 28, 33, 37, 0, 19, 22, 27, 0, 13, 16, 21, 0, 196,
            205, 204, 0, 56, 59, 67, 0, 43, 46, 51, 0, 22, 25, 30, 0, 31, 35, 39, 0, 188, 223, 114, 0, 146, 185, 78, 0,
            21, 24, 29, 0, 16, 19, 24, 0, 23, 28, 32, 0, 205, 204, 204, 61, 231, 233, 230, 0, 196, 196, 196, 0, 18, 21,
            26, 0, 37, 40, 45, 0, 29, 30, 35, 0, 221, 226, 220, 0, 231, 232, 227, 0, 42, 46, 49, 0, 26, 31, 35, 0, 28,
            31, 36, 0, 199, 205, 205, 0, 206, 212, 212, 0, 38, 39, 36, 0, 23, 27, 32, 0, 28, 31, 36, 0, 130, 196, 37, 0,
            209, 236, 152, 0, 17, 33, 11, 0, 26, 29, 34, 0, 23, 24, 29, 0, 205, 204, 204, 61, 188, 193, 199, 0, 230,
            232, 231, 0, 35, 35, 35, 0, 10, 14, 18, 0, 28, 31, 36, 0, 210, 214, 218, 0, 213, 217, 217, 0, 213, 215, 212,
            0, 17, 21, 24, 0, 33, 38, 42, 0, 29, 31, 34, 0, 200, 206, 206, 0, 189, 195, 195, 0, 31, 34, 26, 0, 34, 37,
            42, 0, 21, 25, 26, 0, 188, 218, 112, 0, 182, 213, 134, 0, 22, 31, 31, 0, 17, 20, 25, 0, 205, 204, 204, 61,
            35, 38, 43, 0, 209, 210, 213, 0, 229, 231, 230, 0, 52, 52, 53, 0, 22, 26, 31, 0, 20, 24, 27, 0, 210, 213,
            222, 0, 187, 189, 187, 0, 214, 216, 211, 0, 17, 21, 24, 0, 21, 25, 28, 0, 28, 28, 33, 0, 215, 221, 219, 0,
            186, 191, 190, 0, 36, 39, 26, 0, 18, 19, 23, 0, 21, 25, 28, 0, 151, 183, 112, 0, 156, 182, 141, 0, 15, 22,
            14, 0, 205, 204, 204, 61, 36, 40, 43, 0, 30, 34, 37, 0, 219, 220, 222, 0, 218, 220, 219, 0, 50, 51, 53, 0,
            28, 32, 35, 0, 30, 34, 38, 0, 217, 220, 225, 0, 231, 233, 230, 0, 211, 213, 208, 0, 37, 38, 42, 0, 25, 24,
            29, 0, 23, 23, 25, 0, 201, 207, 207, 0, 191, 196, 197, 0, 24, 26, 25, 0, 26, 27, 31, 0, 17, 18, 22, 0, 64,
            72, 59, 0, 192, 226, 118, 0, 205, 204, 204, 61, 157, 207, 66, 0, 19, 23, 26, 0, 32, 36, 39, 0, 204, 204,
            206, 0, 230, 232, 229, 0, 17, 51, 0, 0, 32, 34, 38, 0, 20, 23, 28, 0, 181, 186, 192, 0, 216, 218, 215, 0,
            44, 61, 32, 0, 22, 23, 28, 0, 24, 27, 30, 0, 236, 239, 240, 0, 207, 216, 215, 0, 170, 227, 88, 0, 19, 23,
            25, 0, 22, 23, 27, 0, 22, 23, 27, 0, 185, 222, 94, 0, 205, 204, 204, 61, 27, 31, 36, 0, 31, 51, 3, 0, 34,
            38, 41, 0, 30, 34, 37, 0, 214, 218, 218, 0, 13, 20, 1, 0, 26, 27, 24, 0, 29, 30, 34, 0, 25, 30, 34, 0, 205,
            210, 213, 0, 213, 241, 130, 0, 32, 38, 23, 0, 26, 25, 31, 0, 30, 31, 36, 0, 194, 199, 203, 0, 18, 36, 0, 0,
            52, 62, 57, 0, 24, 25, 29, 0, 24, 27, 31, 0, 23, 27, 30, 0, 205, 204, 204, 61, 25, 30, 33, 0, 40, 40, 45, 0,
            1, 11, 13, 0, 15, 19, 22, 0, 31, 35, 38, 0, 35, 39, 42, 0, 97, 125, 45, 0, 14, 21, 21, 0, 37, 41, 44, 0, 32,
            33, 35, 0, 29, 33, 36, 0, 205, 241, 119, 0, 38, 47, 43, 0, 18, 22, 25, 0, 30, 31, 35, 0, 29, 34, 37, 0, 167,
            220, 79, 0, 10, 15, 14, 0, 24, 28, 31, 0, 23, 24, 28, 0, 205, 204, 204, 61, 17, 22, 26, 0, 36, 41, 44, 0,
            66, 66, 70, 0, 15, 21, 18, 0, 29, 33, 36, 0, 45, 48, 53, 0, 22, 27, 30, 0, 84, 109, 47, 0, 33, 47, 42, 0,
            24, 28, 31, 0, 39, 43, 46, 0, 25, 29, 30, 0, 192, 222, 126, 0, 28, 39, 33, 0, 26, 30, 33, 0, 57, 61, 64, 0,
            41, 49, 51, 0, 174, 234, 86, 0, 13, 18, 21, 0, 21, 22, 26, 0, 205, 204, 204, 61, 59, 71, 71, 0, 51, 54, 59,
            0, 39, 44, 48, 0, 29, 35, 42, 0, 210, 238, 135, 0, 67, 71, 72, 0, 30, 35, 39, 0, 31, 36, 39, 0, 30, 33, 42,
            0, 45, 63, 44, 0, 49, 54, 57, 0, 26, 29, 34, 0, 38, 41, 46, 0, 15, 20, 10, 0, 47, 64, 45, 0, 22, 26, 29, 0,
            45, 49, 52, 0, 34, 38, 41, 0, 10, 19, 0, 0, 28, 63, 15, 0, 205, 204, 204, 61, 27, 165, 125, 0, 38, 86, 70,
            0, 39, 55, 52, 0, 55, 60, 64, 0, 27, 32, 36, 0, 29, 173, 124, 0, 58, 88, 80, 0, 36, 45, 44, 0, 41, 46, 50,
            0, 43, 48, 51, 0, 47, 171, 127, 0, 66, 82, 79, 0, 39, 42, 47, 0, 31, 34, 39, 0, 29, 33, 36, 0, 30, 179, 127,
            0, 23, 33, 34, 0, 53, 57, 60, 0, 33, 37, 40, 0, 38, 43, 46, 0, 205, 204, 204, 61, 24, 163, 122, 0, 24, 163,
            121, 0, 13, 129, 92, 0, 57, 91, 82, 0, 70, 75, 78, 0, 26, 169, 125, 0, 26, 169, 126, 0, 49, 112, 90, 0, 57,
            74, 72, 0, 63, 68, 72, 0, 26, 172, 125, 0, 25, 173, 125, 0, 50, 94, 79, 0, 66, 76, 77, 0, 31, 34, 39, 0, 25,
            177, 126, 0, 25, 179, 125, 0, 43, 77, 66, 0, 30, 38, 40, 0, 36, 40, 43, 0, 205, 204, 204, 61, 23, 158, 118,
            0, 24, 160, 120, 0, 23, 162, 121, 0, 21, 167, 122, 0, 57, 116, 98, 0, 26, 162, 122, 0, 24, 165, 122, 0, 24,
            167, 123, 0, 28, 167, 126, 0, 50, 88, 75, 0, 25, 166, 123, 0, 26, 169, 123, 0, 24, 170, 122, 0, 27, 171,
            122, 0, 54, 79, 73, 0, 26, 172, 123, 0, 26, 172, 123, 0, 27, 175, 125, 0, 27, 181, 127, 0, 59, 71, 69, 0,
            205, 204, 204, 61, 22, 152, 118, 0, 23, 154, 120, 0, 25, 157, 120, 0, 23, 158, 118, 0, 25, 161, 121, 0, 23,
            157, 120, 0, 23, 157, 120, 0, 24, 160, 120, 0, 23, 162, 120, 0, 25, 166, 123, 0, 24, 160, 122, 0, 23, 164,
            122, 0, 26, 165, 124, 0, 25, 168, 124, 0, 25, 171, 124, 0, 23, 164, 122, 0, 24, 165, 122, 0, 27, 170, 126,
            0, 24, 171, 124, 0, 26, 177, 126, 0, 205, 204, 204, 61, 20, 145, 115, 0, 23, 148, 118, 0, 22, 151, 118, 0,
            22, 154, 117, 0, 23, 157, 120, 0, 22, 149, 119, 0, 22, 152, 118, 0, 23, 155, 118, 0, 23, 158, 118, 0, 25,
            161, 121, 0, 23, 154, 120, 0, 25, 157, 120, 0, 24, 159, 119, 0, 25, 161, 121, 0, 24, 165, 123, 0, 23, 159,
            121, 0, 25, 160, 119, 0, 24, 163, 121, 0, 25, 166, 123, 0, 25, 171, 125, 0, 205, 204, 204, 61, 21, 139, 115,
            0, 23, 143, 116, 0, 23, 144, 115, 0, 21, 148, 118, 0, 23, 151, 118, 0, 21, 144, 116, 0, 21, 146, 116, 0, 24,
            149, 119, 0, 23, 153, 119, 0, 25, 157, 120, 0, 21, 148, 118, 0, 22, 150, 117, 0, 23, 153, 119, 0, 23, 157,
            120, 0, 23, 159, 119, 0, 23, 151, 118, 0, 23, 154, 120, 0, 23, 157, 120, 0, 23, 159, 119, 0, 26, 165, 123,
            0, 205, 204, 204, 61, 20, 133, 113, 0, 20, 136, 113, 0, 21, 139, 115, 0, 20, 143, 115, 0, 23, 146, 117, 0,
            19, 137, 113, 0, 21, 139, 114, 0, 21, 144, 116, 0, 20, 145, 115, 0, 21, 150, 119, 0, 22, 140, 116, 0, 22,
            145, 116, 0, 22, 147, 117, 0, 22, 149, 119, 0, 24, 154, 119, 0, 21, 144, 115, 0, 22, 147, 117, 0, 23, 151,
            118, 0, 23, 154, 120, 0, 24, 159, 119, 0, 205, 204, 204, 61, 20, 129, 110, 0, 19, 130, 111, 0, 22, 136, 113,
            0, 20, 138, 114, 0, 22, 142, 115, 0, 19, 132, 112, 0, 22, 135, 115, 0, 20, 138, 114, 0, 22, 142, 115, 0, 21,
            146, 116, 0, 20, 136, 113, 0, 20, 138, 114, 0, 22, 142, 115, 0, 22, 145, 116, 0, 22, 149, 119, 0, 21, 139,
            115, 0, 21, 144, 116, 0, 22, 146, 116, 0, 22, 149, 119, 0, 21, 155, 120, 0, 205, 204, 204, 61, 20, 127, 109,
            0, 19, 130, 111, 0, 20, 133, 113, 0, 20, 136, 113, 0, 21, 139, 113, 0, 20, 131, 112, 0, 22, 133, 114, 0, 21,
            137, 114, 0, 22, 140, 116, 0, 21, 144, 115, 0, 21, 134, 114, 0, 19, 137, 113, 0, 22, 140, 116, 0, 20, 144,
            116, 0, 23, 148, 118, 0, 21, 137, 114, 0, 21, 141, 116, 0, 21, 143, 116, 0, 23, 148, 118, 0, 23, 153, 119,
            0, 205, 204, 204, 61, 18, 125, 109, 0, 21, 128, 112, 0, 19, 130, 111, 0, 21, 135, 112, 0, 20, 138, 114, 0,
            21, 130, 111, 0, 18, 131, 111, 0, 21, 134, 114, 0, 20, 138, 114, 0, 22, 142, 115, 0, 18, 131, 111, 0, 21,
            134, 114, 0, 20, 138, 114, 0, 22, 142, 115, 0, 22, 145, 116, 0, 19, 135, 112, 0, 20, 138, 114, 0, 23, 142,
            118, 0, 21, 144, 115, 0, 22, 150, 117, 0, 205, 204, 204, 61, 18, 123, 109, 0, 18, 124, 109, 0, 20, 127, 111,
            0, 19, 131, 112, 0, 22, 136, 113, 0, 18, 125, 109, 0, 19, 127, 111, 0, 19, 131, 112, 0, 21, 135, 112, 0, 20,
            138, 114, 0, 20, 129, 110, 0, 20, 131, 112, 0, 21, 134, 114, 0, 20, 138, 114, 0, 22, 142, 115, 0, 20, 131,
            112, 0, 19, 135, 114, 0, 19, 137, 113, 0, 22, 140, 116, 0, 21, 146, 116, 0, 205, 204, 204, 61, 17, 119, 106,
            0, 20, 122, 109, 0, 18, 125, 109, 0, 21, 130, 111, 0, 19, 132, 112, 0, 17, 123, 108, 0, 18, 126, 110, 0, 21,
            130, 111, 0, 20, 131, 112, 0, 20, 136, 113, 0, 19, 126, 110, 0, 18, 129, 110, 0, 20, 131, 112, 0, 20, 135,
            112, 0, 21, 139, 115, 0, 18, 129, 110, 0, 20, 131, 112, 0, 19, 135, 114, 0, 21, 139, 115, 0, 20, 144, 116,
            0, 205, 204, 204, 61, 17, 119, 106, 0, 19, 121, 108, 0, 18, 125, 109, 0, 20, 129, 110, 0, 19, 132, 112, 0,
            17, 122, 108, 0, 18, 125, 109, 0, 20, 129, 110, 0, 20, 131, 112, 0, 22, 136, 113, 0, 18, 125, 109, 0, 19,
            127, 111, 0, 19, 130, 111, 0, 21, 135, 112, 0, 19, 137, 113, 0, 19, 127, 111, 0, 19, 130, 111, 0, 19, 134,
            114, 0, 20, 138, 114, 0, 20, 144, 116, 0, 205, 204, 204, 61, 18, 118, 106, 0, 19, 121, 108, 0, 19, 124, 109,
            0, 20, 129, 110, 0, 19, 132, 112, 0, 17, 122, 107, 0, 18, 125, 109, 0, 20, 127, 111, 0, 19, 130, 111, 0, 22,
            136, 113, 0, 18, 125, 109, 0, 19, 127, 111, 0, 19, 130, 111, 0, 21, 135, 112, 0, 19, 137, 113, 0, 20, 127,
            111, 0, 18, 129, 110, 0, 19, 134, 114, 0, 20, 138, 114, 0, 19, 143, 115, 0, 205, 204, 204, 61, 18, 118, 106,
            0, 19, 121, 108, 0, 19, 124, 109, 0, 20, 129, 110, 0, 19, 132, 112, 0, 17, 122, 107, 0, 18, 125, 109, 0, 20,
            127, 111, 0, 19, 130, 111, 0, 22, 136, 113, 0, 18, 125, 109, 0, 19, 127, 111, 0, 19, 130, 111, 0, 21, 135,
            112, 0, 19, 137, 113, 0, 20, 127, 111, 0, 18, 129, 110, 0, 19, 134, 114, 0, 20, 138, 114, 0, 19, 143, 115,
            0, 205, 204, 204, 61, 18, 118, 106, 0, 19, 121, 108, 0, 19, 124, 109, 0, 20, 129, 110, 0, 18, 131, 111, 0,
            17, 122, 107, 0, 18, 125, 109, 0, 20, 127, 111, 0, 19, 130, 111, 0, 22, 136, 113, 0, 18, 125, 109, 0, 19,
            127, 111, 0, 19, 130, 111, 0, 21, 135, 112, 0, 20, 138, 114, 0, 20, 127, 111, 0, 18, 129, 110, 0, 19, 134,
            115, 0, 20, 138, 114, 0, 19, 143, 115, 0, type=ctyped.type.BYTE))


ctyped.lib.add_path(ntpath.join(ntpath.dirname(__file__)))

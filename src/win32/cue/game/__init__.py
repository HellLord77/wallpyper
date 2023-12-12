from __future__ import annotations as _

import enum
import logging
import ntpath

from libs import ctyped
from libs.ctyped.enum import CgSDK as enum_CgSDK
from libs.ctyped.lib import CgSDK_2019

logger = logging.getLogger(__name__)

FLAG_RESET_GAME = False


def _bytes(o: bytes | str | _Profile) -> bytes:
    if isinstance(o, _Profile):
        o = o.name
    if isinstance(o, str):
        o = o.encode()
    return o


def handshake() -> bool:
    details = CgSDK_2019.CgSdkPerformProtocolHandshake()
    return bool(details.sdkProtocolVersion) and not details.breakingChanges


def set_game(name: bytes | str) -> bool:
    return CgSDK_2019.CgSdkSetGame(_bytes(name))


def set_state(profile: bytes | str | _Profile) -> bool:
    return CgSDK_2019.CgSdkSetState(_bytes(profile))


def set_event(profile: bytes | str | _Profile) -> bool:
    return CgSDK_2019.CgSdkSetEvent(_bytes(profile))


def clear_state(*profiles: bytes | str | _Profile) -> bool:
    if profiles:
        cleared = True
        for profile in profiles:
            cleared = CgSDK_2019.CgSdkClearState(_bytes(profile)) and cleared
    else:
        cleared = CgSDK_2019.CgSdkClearAllStates()
    return cleared


def clear_event() -> bool:
    return CgSDK_2019.CgSdkClearAllEvents()


class _Control:
    def __init__(self):
        CgSDK_2019.CgSdkRequestControl(enum_CgSDK.CorsairAccessMode.ExclusiveLightingControl)

    def __del__(self):
        CgSDK_2019.CgSdkReleaseControl(enum_CgSDK.CorsairAccessMode.ExclusiveLightingControl)

    def __enter__(self):
        pass

    def __exit__(self, _, __, ___):
        self.__del__()


class _Profile(enum.IntEnum):
    _game: _Game

    def __enter__(self) -> bool:
        return self.set()

    def __exit__(self, _, __, ___):
        self.clear()

    def set(self, loop: bool = True) -> bool:
        if FLAG_RESET_GAME:
            cls = type(self)
            name = cls.__qualname__.split('.')[0]
            logging.debug('Setting game: %s', name)
            cls._game = globals()[name]()
        return (set_state if loop else set_event)(self)

    clear = clear_state


class _Game:
    _name = ''
    _init = False

    # noinspection PyPep8Naming
    class profile(_Profile):
        pass

    def __init_subclass__(cls):
        if not cls._name:
            cls._name = cls.__name__

    def __init__(self):
        self._init = handshake()
        if self._init:
            self._control = _Control()
            self._init = set_game(self._name)

    def __del__(self):
        if self:
            clear_state() and clear_event()
        self._control = None
        self._init = False

    def __bool__(self):
        return self._init

    def __enter__(self) -> _Game:
        return self

    def __exit__(self, _, __, ___):
        self.__del__()


class AgainstTheStorm(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        ATSM_Clearance = 50
        ATSM_Coral = 45
        ATSM_Drizzle = 55
        ATSM_Map = 740
        ATSM_Menu = 750
        ATSM_Storm = 60
        SDKL_EnvAutumn = 745
        SDKL_EnvDarkBlue = 40
        SDKL_EnvDarkOrange = 25
        SDKL_EnvGreen = 30
        SDKL_Explosion = 335
        SDKL_LootTeal = 345
        SDKL_Poison = 747
        SDKL_PulseTan = 340
        SDKL_PulseTeal = 350
        SDKL_SplashGrey = 250
        SDKL_StaticBlack = 800
        SDKL_WaterCyan = 35


class BeyondContact(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        BECO_Menu = 600
        BECO_Options = 596
        BECO_Snow = 42
        SDKL_Alarm = 496
        SDKL_AlarmBlue = 492
        SDKL_AlarmOrange = 494
        SDKL_Cobalt = 322
        SDKL_Crimson = 20
        SDKL_EnvDarkGrey = 598
        SDKL_EnvDarkPink = 18
        SDKL_EnvDarkPurple = 14
        SDKL_EnvDarkRed = 30
        SDKL_EnvSand = 16
        SDKL_EnvTech = 46
        SDKL_EnvWhite = 36
        SDKL_Explosion = 408
        SDKL_FadeToBlack = 498
        SDKL_Fire = 404
        SDKL_FireYellow = 402
        SDKL_Freezing = 406
        SDKL_Ice = 502
        SDKL_IceDark = 44
        SDKL_Lava = 32
        SDKL_LootBlue = 314
        SDKL_LootGold = 308
        SDKL_LootPurple = 310
        SDKL_LootWhite = 316
        SDKL_Neon = 10
        SDKL_Nuclear = 12
        SDKL_Poison = 500
        SDKL_PulseBarBlack = 324
        SDKL_PulseBarBlue = 320
        SDKL_PulseBarGreen = 318
        SDKL_PulseBarPurple = 306
        SDKL_PulsePurple = 302
        SDKL_RocketsPurple = 304
        SDKL_Snow = 400
        SDKL_SplashPurple = 326
        SDKL_Underwater = 26
        SDKL_UnderwaterBrown = 24
        SDKL_UnderwaterCyan = 22
        SDKL_WaterCyan = 28
        SDKL_WaveRightCyan = 300
        SDKL_WaveUpBlue = 312


class BlairWitch(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        BLW_Blackout = 39
        BLW_Bundle = 72
        BLW_Bye = 73
        BLW_Camera = 42
        BLW_CameraWalk = 43
        BLW_Cart = 40
        BLW_Carving = 70
        BLW_Command = 130
        BLW_DayBlue = 34
        BLW_DayGreen = 30
        BLW_DayGrey = 36
        BLW_DayYellow = 32
        BLW_Death = 170
        BLW_FlashBlack = 149
        BLW_FlashBlue = 147
        BLW_FlashRed = 148
        BLW_FlashWhite = 150
        BLW_Flashlight = 41
        BLW_FlashlightFlicker = 128
        BLW_Loading = 247
        BLW_Logo = 246
        BLW_Menu = 245
        BLW_Night = 38
        BLW_Notification = 118
        BLW_Phone = 44
        BLW_Photos = 71
        BLW_PoliceLights = 108
        BLW_Radio = 46
        BLW_Redout = 126
        BLW_Totem = 74
        SDKL_StaticBlack = 124
        SDKL_StaticWhite = 122


class Breakpoint(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        BKPT_Beat = 22
        SDKL_AlertEdgesOrange = 40
        SDKL_DeathShock = 130
        SDKL_EnvTech = 20
        SDKL_FireworksYellowWhiteOrange = 120
        SDKL_FlashGrey = 69
        SDKL_FlashWhite = 70
        SDKL_PulseBlue = 85
        SDKL_PulseCyan = 110
        SDKL_PulseLime = 90
        SDKL_PulseOrange = 95
        SDKL_PulsePink = 105
        SDKL_PulsePurple = 115
        SDKL_PulseRed = 80
        SDKL_PulseStarGrey = 50
        SDKL_RocketsBlue = 30
        SDKL_Smoke = 25
        SDKL_SplashGrey = 60
        SDKL_SplashWhite = 65


class Chernobylite(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_Alarm = 320
        SDKL_AlertEdgesGreen = 324
        SDKL_AlertEdgesRed = 326
        SDKL_BloodSplatter = 328
        SDKL_Corrosive = 500
        SDKL_EnvAutumn = 42
        SDKL_EnvDarkBlue = 46
        SDKL_EnvDarkGrey = 48
        SDKL_Fog = 50
        SDKL_Gas = 54
        SDKL_PulseBarGreen = 280
        SDKL_PulseBarRed = 300
        SDKL_PulseStarGreen = 286
        SDKL_Smoke = 56
        SDKL_SplashRed = 322
        SDKL_UnderwaterCyan = 44


class Common(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_Alarm = 556
        SDKL_AlertEdgesBlack = 410
        SDKL_AlertEdgesBlue = 412
        SDKL_AlertEdgesCyan = 414
        SDKL_AlertEdgesGreen = 416
        SDKL_AlertEdgesGrey = 418
        SDKL_AlertEdgesLime = 420
        SDKL_AlertEdgesOrange = 422
        SDKL_AlertEdgesPink = 424
        SDKL_AlertEdgesPurple = 426
        SDKL_AlertEdgesRed = 428
        SDKL_AlertEdgesWhite = 430
        SDKL_AlertEdgesYellow = 432
        SDKL_Bees = 558
        SDKL_Bleeding = 654
        SDKL_BloodSplatter = 611
        SDKL_Brimstone = 10
        SDKL_Cobalt = 12
        SDKL_Corrosive = 14
        SDKL_Crimson = 16
        SDKL_Cutscene = 760
        SDKL_DamageCenter = 610
        SDKL_DamageClaws = 612
        SDKL_DamageSides = 614
        SDKL_DamageXSlash = 616
        SDKL_Day = 18
        SDKL_Death = 810
        SDKL_DeathExplosion = 812
        SDKL_DeathFire = 814
        SDKL_DeathGasGreen = 816
        SDKL_DeathShock = 818
        SDKL_DeathWater = 820
        SDKL_DeathWaterBlue = 822
        SDKL_Downed = 658
        SDKL_EnvAutumn = 20
        SDKL_EnvDark = 22
        SDKL_EnvDarkBlue = 24
        SDKL_EnvDarkGreen = 26
        SDKL_EnvDarkGrey = 28
        SDKL_EnvDarkYellow = 30
        SDKL_EnvMud = 32
        SDKL_EnvSand = 34
        SDKL_EnvSummer = 36
        SDKL_EnvSunset = 38
        SDKL_EnvTech = 40
        SDKL_EnvWhite = 42
        SDKL_EnvWinter = 44
        SDKL_Explosion = 560
        SDKL_FadeToBlack = 776
        SDKL_Fire = 530
        SDKL_FireBlack = 532
        SDKL_FireBlue = 534
        SDKL_FireCyan = 536
        SDKL_FireGreen = 538
        SDKL_FireGrey = 540
        SDKL_FireHit = 622
        SDKL_FireHitBlack = 624
        SDKL_FireHitBlue = 626
        SDKL_FireHitCyan = 628
        SDKL_FireHitGreen = 630
        SDKL_FireHitGrey = 632
        SDKL_FireHitLime = 634
        SDKL_FireHitOrange = 636
        SDKL_FireHitPink = 638
        SDKL_FireHitPurple = 640
        SDKL_FireHitRed = 642
        SDKL_FireHitWhite = 644
        SDKL_FireHitYellow = 646
        SDKL_FireLime = 542
        SDKL_FireOrange = 544
        SDKL_FirePink = 546
        SDKL_FirePurple = 548
        SDKL_FireRed = 550
        SDKL_FireWhite = 552
        SDKL_FireYellow = 554
        SDKL_FireworksRedWhiteBlue = 562
        SDKL_FlashBlack = 710
        SDKL_FlashBlue = 712
        SDKL_FlashCyan = 714
        SDKL_FlashGreen = 716
        SDKL_FlashGrey = 718
        SDKL_FlashLime = 722
        SDKL_FlashOrange = 724
        SDKL_FlashPink = 726
        SDKL_FlashPurple = 728
        SDKL_FlashRed = 730
        SDKL_FlashWhite = 732
        SDKL_FlashYellow = 734
        SDKL_Flashlight = 720
        SDKL_FlyingDown = 352
        SDKL_FlyingUp = 354
        SDKL_Fog = 46
        SDKL_GasGreen = 564
        SDKL_GlowBlack = 110
        SDKL_GlowBlue = 112
        SDKL_GlowCyan = 114
        SDKL_GlowGreen = 116
        SDKL_GlowGrey = 118
        SDKL_GlowLime = 120
        SDKL_GlowOrange = 122
        SDKL_GlowPink = 124
        SDKL_GlowPurple = 126
        SDKL_GlowRed = 128
        SDKL_GlowWhite = 130
        SDKL_GlowYellow = 132
        SDKL_Healing = 762
        SDKL_HeartPink = 764
        SDKL_HeartRed = 766
        SDKL_HintBlack = 134
        SDKL_HintBlue = 136
        SDKL_HintCyan = 138
        SDKL_HintGreen = 140
        SDKL_HintGrey = 142
        SDKL_HintLime = 144
        SDKL_HintOrange = 146
        SDKL_HintPink = 148
        SDKL_HintPurple = 150
        SDKL_HintRed = 152
        SDKL_HintWhite = 154
        SDKL_HintYellow = 156
        SDKL_Ice = 48
        SDKL_IceHit = 648
        SDKL_Injured = 618
        SDKL_LightningStrike = 572
        SDKL_LootBlack = 158
        SDKL_LootBlue = 160
        SDKL_LootCyan = 162
        SDKL_LootGold = 164
        SDKL_LootGreen = 166
        SDKL_LootGrey = 168
        SDKL_LootLime = 170
        SDKL_LootOrange = 172
        SDKL_LootPink = 174
        SDKL_LootPurple = 176
        SDKL_LootRed = 178
        SDKL_LootWhite = 180
        SDKL_LootYellow = 182
        SDKL_Melee = 620
        SDKL_MushroomCloud = 566
        SDKL_Neon = 50
        SDKL_Night = 52
        SDKL_NightDark = 54
        SDKL_Nuclear = 56
        SDKL_Overheat = 574
        SDKL_PillarsBlack = 356
        SDKL_PillarsBlue = 358
        SDKL_PillarsCyan = 360
        SDKL_PillarsGreen = 362
        SDKL_PillarsGrey = 364
        SDKL_PillarsLime = 366
        SDKL_PillarsOrange = 368
        SDKL_PillarsPink = 370
        SDKL_PillarsPurple = 372
        SDKL_PillarsRed = 374
        SDKL_PillarsWhite = 376
        SDKL_PillarsYellow = 378
        SDKL_Poison = 58
        SDKL_PoisonGreen = 60
        SDKL_PoliceLightsFull = 568
        SDKL_PowerOn = 768
        SDKL_PulseBarBlack = 434
        SDKL_PulseBarBlue = 436
        SDKL_PulseBarCyan = 438
        SDKL_PulseBarGreen = 440
        SDKL_PulseBarGrey = 442
        SDKL_PulseBarLime = 444
        SDKL_PulseBarOrange = 446
        SDKL_PulseBarPink = 448
        SDKL_PulseBarPurple = 450
        SDKL_PulseBarRed = 452
        SDKL_PulseBarWhite = 454
        SDKL_PulseBarYellow = 456
        SDKL_PulseBlack = 458
        SDKL_PulseBlue = 460
        SDKL_PulseCyan = 462
        SDKL_PulseGreen = 464
        SDKL_PulseGrey = 466
        SDKL_PulseLime = 468
        SDKL_PulseOrange = 470
        SDKL_PulsePink = 472
        SDKL_PulsePurple = 474
        SDKL_PulseRed = 476
        SDKL_PulseStarBlack = 478
        SDKL_PulseStarBlue = 480
        SDKL_PulseStarCyan = 482
        SDKL_PulseStarGreen = 484
        SDKL_PulseStarGrey = 486
        SDKL_PulseStarLime = 488
        SDKL_PulseStarOrange = 490
        SDKL_PulseStarPink = 492
        SDKL_PulseStarPurple = 494
        SDKL_PulseStarRed = 496
        SDKL_PulseStarWhite = 498
        SDKL_PulseStarYellow = 500
        SDKL_PulseWhite = 502
        SDKL_PulseYellow = 504
        SDKL_Radioactive = 62
        SDKL_Rain = 64
        SDKL_RangeHit = 770
        SDKL_RocketsBlue = 380
        SDKL_RocketsOrange = 382
        SDKL_Shadow = 66
        SDKL_ShapeSpinWhite = 772
        SDKL_ShockBlack = 506
        SDKL_ShockBlue = 508
        SDKL_ShockCyan = 510
        SDKL_ShockGreen = 512
        SDKL_ShockGrey = 514
        SDKL_ShockLime = 516
        SDKL_ShockOrange = 518
        SDKL_ShockPink = 520
        SDKL_ShockPurple = 522
        SDKL_ShockRed = 524
        SDKL_ShockWhite = 526
        SDKL_ShockYellow = 528
        SDKL_Smoke = 68
        SDKL_Snow = 70
        SDKL_SonarBlack = 184
        SDKL_SonarBlue = 186
        SDKL_SonarCyan = 188
        SDKL_SonarGreen = 190
        SDKL_SonarGrey = 192
        SDKL_SonarLime = 194
        SDKL_SonarOrange = 196
        SDKL_SonarPink = 198
        SDKL_SonarPurple = 200
        SDKL_SonarRed = 202
        SDKL_SonarWhite = 204
        SDKL_SonarYellow = 206
        SDKL_SparksBlack = 208
        SDKL_SparksBlue = 210
        SDKL_SparksCyan = 212
        SDKL_SparksGreen = 214
        SDKL_SparksGrey = 216
        SDKL_SparksLime = 218
        SDKL_SparksOrange = 220
        SDKL_SparksPink = 222
        SDKL_SparksPurple = 224
        SDKL_SparksRed = 226
        SDKL_SparksWhite = 228
        SDKL_SparksYellow = 230
        SDKL_SplashBlack = 232
        SDKL_SplashBlue = 234
        SDKL_SplashCyan = 236
        SDKL_SplashGreen = 238
        SDKL_SplashGrey = 240
        SDKL_SplashLime = 242
        SDKL_SplashOrange = 244
        SDKL_SplashPink = 246
        SDKL_SplashPurple = 248
        SDKL_SplashRed = 250
        SDKL_SplashWhite = 252
        SDKL_SplashYellow = 254
        SDKL_Spotted = 570
        SDKL_StaticBlack = 736
        SDKL_StaticBlue = 738
        SDKL_StaticCyan = 740
        SDKL_StaticGreen = 742
        SDKL_StaticGrey = 744
        SDKL_StaticLime = 746
        SDKL_StaticOrange = 748
        SDKL_StaticPink = 750
        SDKL_StaticPurple = 752
        SDKL_StaticRed = 754
        SDKL_StaticWhite = 756
        SDKL_StaticYellow = 758
        SDKL_Suffocate = 656
        SDKL_TVNoise = 84
        SDKL_Titanium = 72
        SDKL_Underwater = 74
        SDKL_UnderwaterBlue = 76
        SDKL_Water = 78
        SDKL_WaterBlue = 80
        SDKL_WaterBrown = 82
        SDKL_WaterHit = 650
        SDKL_WaterHitBlue = 652
        SDKL_WaveDownBlack = 256
        SDKL_WaveDownBlue = 258
        SDKL_WaveDownCyan = 260
        SDKL_WaveDownGreen = 262
        SDKL_WaveDownGrey = 264
        SDKL_WaveDownLime = 266
        SDKL_WaveDownOrange = 268
        SDKL_WaveDownPink = 270
        SDKL_WaveDownPurple = 272
        SDKL_WaveDownRed = 274
        SDKL_WaveDownWhite = 276
        SDKL_WaveDownYellow = 278
        SDKL_WaveLeftBlack = 280
        SDKL_WaveLeftBlue = 282
        SDKL_WaveLeftCyan = 284
        SDKL_WaveLeftGreen = 286
        SDKL_WaveLeftGrey = 288
        SDKL_WaveLeftLime = 290
        SDKL_WaveLeftOrange = 292
        SDKL_WaveLeftPink = 294
        SDKL_WaveLeftPurple = 296
        SDKL_WaveLeftRed = 298
        SDKL_WaveLeftWhite = 300
        SDKL_WaveLeftYellow = 302
        SDKL_WaveRightBlack = 304
        SDKL_WaveRightBlue = 306
        SDKL_WaveRightCyan = 308
        SDKL_WaveRightGreen = 310
        SDKL_WaveRightGrey = 312
        SDKL_WaveRightLime = 314
        SDKL_WaveRightOrange = 316
        SDKL_WaveRightPink = 318
        SDKL_WaveRightPurple = 320
        SDKL_WaveRightRed = 322
        SDKL_WaveRightWhite = 324
        SDKL_WaveRightYellow = 326
        SDKL_WaveUpBlack = 328
        SDKL_WaveUpBlue = 330
        SDKL_WaveUpCyan = 332
        SDKL_WaveUpGreen = 334
        SDKL_WaveUpGrey = 336
        SDKL_WaveUpLime = 338
        SDKL_WaveUpOrange = 340
        SDKL_WaveUpPink = 342
        SDKL_WaveUpPurple = 344
        SDKL_WaveUpRed = 346
        SDKL_WaveUpWhite = 348
        SDKL_WaveUpYellow = 350
        SDKL_WipeWhite = 774


class CoreKeeper(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        CORE_Inventory = 80
        CORE_Menu = 800
        CORE_Mold = 30
        SDKL_Alarm = 250
        SDKL_BloodSplatter = 350
        SDKL_EnvDarkGreen = 25
        SDKL_EnvDarkGrey = 15
        SDKL_EnvMud = 20
        SDKL_EnvSand = 10
        SDKL_EnvTech = 40
        SDKL_Explosion = 380
        SDKL_FadeToBlack = 500
        SDKL_Lava = 45
        SDKL_LootOrange = 235
        SDKL_LootPurple = 230
        SDKL_PillarsBlue = 220
        SDKL_PulseBlue = 212
        SDKL_PulseStarBlue = 305
        SDKL_PulseStarCyan = 215
        SDKL_ShockBlue = 210
        SDKL_SplashBlue = 205
        SDKL_UnderwaterBlue = 35
        SDKL_WaveDownBlue = 300
        SDKL_WaveUpGreen = 200


class Dwerve(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        DWVE_Build = 125
        DWVE_Combat = 35
        DWVE_Menu = 500
        DWVE_Recall = 130
        SDKL_AlertEdgesRed = 135
        SDKL_Crimson = 25
        SDKL_EnvAutumn = 5
        SDKL_EnvDarkGrey = 15
        SDKL_EnvDarkPurple = 20
        SDKL_EnvDarkRed = 10
        SDKL_EnvSand = 30
        SDKL_FadeToGrey = 245
        SDKL_FireworksYellowWhiteOrange = 225
        SDKL_Injured = 40
        SDKL_LootBlue = 110
        SDKL_LootGold = 115
        SDKL_LootGrey = 120
        SDKL_LootRed = 105
        SDKL_PillarsWhite = 220
        SDKL_PulseBarOrange = 210
        SDKL_PulseStarOrange = 215
        SDKL_SplashLime = 100
        SDKL_WaveDownGreen = 205
        SDKL_WaveUpRed = 200


class Embr(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        EMBR_Default = 10
        EMBR_Findr = 75
        EMBR_Logo = 245
        SDKL_AlertEdgesRed = 115
        SDKL_Corrosive = 120
        SDKL_Death = 175
        SDKL_Downed = 160
        SDKL_EnvDark = 15
        SDKL_Explosion = 170
        SDKL_Fire = 130
        SDKL_FlashYellow = 180
        SDKL_FlyingDown = 80
        SDKL_FlyingUp = 30
        SDKL_HeartRed = 165
        SDKL_PulseBarWhite = 70
        SDKL_ShockYellow = 140
        SDKL_WaterBlue = 110


class FarCryNewDawn(_Game):
    _name = 'Far Cry New Dawn'

    # noinspection PyPep8Naming
    class profile(_Profile):
        FCDN_Loot = 130
        FCND_Base = 100
        FCND_BaseStation = 103
        FCND_Bonfire = 205
        FCND_Craft = 99
        FCND_Credits = 243
        FCND_Danger = 219
        FCND_Day = 2
        FCND_ExpedEnd = 238
        FCND_ExpedStart = 237
        FCND_Father = 234
        FCND_FireHitPink = 230
        FCND_FlyDay = 3
        FCND_FlyNight = 8
        FCND_GFH = 102
        FCND_GFHCom = 183
        FCND_Indoors = 9
        FCND_ItemEpic = 241
        FCND_ItemLegend = 239
        FCND_ItemRare = 240
        FCND_Liberty = 231
        FCND_Menu = 236
        FCND_Night = 7
        FCND_NorthDay = 16
        FCND_Sisters = 185
        FCND_Symbol = 206
        FCND_TheNorth = 15
        FC_Bees = 220
        FC_Benchmark = 245
        FC_Death = 232
        FC_Drug = 202
        FC_Drunk = 201
        FC_Fish = 21
        FC_Spotted = 210
        FC_Takedown = 227
        SDKL_Alarm = 190
        SDKL_Claws = 225
        SDKL_Corrosive = 226
        SDKL_Cutscene = 233
        SDKL_Explosion = 221
        SDKL_FireHit = 224
        SDKL_FlashRed = 228
        SDKL_FlashWhite = 229
        SDKL_FlashYellow = 182
        SDKL_GlowOrange = 200
        SDKL_Healing = 135
        SDKL_Melee = 223
        SDKL_MushroomCloud = 235
        SDKL_PoisonGreen = 155
        SDKL_PulseGreen = 180
        SDKL_PulsePink = 242
        SDKL_PulseWhite = 110
        SDKL_PulseYellow = 150
        SDKL_RangeHit = 222
        SDKL_Shadow = 195
        SDKL_Underwater = 46
        SDKL_Water = 45


class FarCry5(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        FCHOD_Day = 4
        FCHOD_Liberty = 236
        FCHOD_Menu = 246
        FCLOM_BroBot = 175
        FCLOM_DustCloud = 150
        FCLOM_Exterior = 5
        FCLOM_GravityBelt = 100
        FCLOM_Hemoleum = 211
        FCLOM_Intertior = 9
        FCLOM_Menu = 247
        FCLOM_Overheat = 198
        FCLOM_PowerOn = 199
        FCLOM_QueenKill = 151
        FCLOM_Restored = 234
        FCLOM_SpaceWings = 101
        FC_AnimalAttack = 225
        FC_Arcade = 17
        FC_ArcadeCoin = 18
        FC_ArcadeMenu = 16
        FC_Bees = 220
        FC_Benchmark = 1
        FC_Bliss = 203
        FC_CrouchDay = 5
        FC_CrouchNight = 10
        FC_Cutscene = 19
        FC_Day = 3
        FC_Death = 235
        FC_Down = 233
        FC_Drug = 202
        FC_Drunk = 201
        FC_Equip = 180
        FC_Explosion = 221
        FC_Fire = 224
        FC_FireFlag = 229
        FC_Fish = 21
        FC_FlightDay = 6
        FC_FlightNight = 11
        FC_FlyRaceCheckpoint = 227
        FC_Liberty = 233
        FC_LibertyBlue = 232
        FC_LibertyFlag = 231
        FC_MPLoss = 242
        FC_MPWin = 241
        FC_Melee = 223
        FC_Menu = 245
        FC_Night = 8
        FC_NightLight = 40
        FC_Psychedelic = 204
        FC_RaceCheckpoint = 228
        FC_Shoot = 222
        FC_Skunk = 226
        FC_Spotted = 210
        FC_Takedown = 230
        FC_Underwater = 46
        FC_Water = 45


class FarCry6(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        FC6_Death = 165
        FC6_EnvCity = 23
        FC6_EnvFlight = 24
        FC6_EnvOutside = 20
        FC6_EnvUnderground = 21
        FC6_EnvVillage = 22
        FC6_EnvWater = 25
        FC6_Horn = 85
        FC6_Liberated = 180
        FC6_MatchLost = 176
        FC6_MatchWon = 175
        FC6_MenuDark = 214
        FC6_MenuLight = 215
        FC6_MenuMain = 220
        FC6_MenuMap = 218
        FC6_MenuMission = 217
        FC6_Mission = 170
        FC6_Phone = 80
        FC6_Spotted = 130
        FC6_TimeDawn = 13
        FC6_TimeDay = 10
        FC6_TimeDusk = 11
        FC6_TimeNight = 12
        SDKL_Alarm = 156
        SDKL_AlertEdgesPurple = 130
        SDKL_BloodSplatter = 110
        SDKL_Cutscene = 255
        SDKL_DamageSides = 140
        SDKL_Downed = 164
        SDKL_Explosion = 142
        SDKL_Fire = 143
        SDKL_FireRed = 144
        SDKL_FlashGreen = 80
        SDKL_FlashWhite = 18
        SDKL_Flashlight = 19
        SDKL_HintBlue = 101
        SDKL_HintGreen = 103
        SDKL_HintRed = 102
        SDKL_HintYellow = 100
        SDKL_Injured = 155
        SDKL_LightningStrike = 41
        SDKL_Melee = 141
        SDKL_Rain = 40
        SDKL_StaticBlack = 255
        SDKL_StaticBlue = 59
        SDKL_StaticCyan = 58
        SDKL_StaticGreen = 60
        SDKL_StaticRed = 56
        SDKL_StaticYellow = 105
        SDKL_WaterBlue = 26
        SDKL_WaveUpRed = 106
        SDKL_WaveUpYellow = 109


class FreshlyFrosted(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        FRFR_Menu = 250
        FRFR_Play_World01 = 100
        FRFR_Play_World02 = 105
        FRFR_Play_World03 = 110
        FRFR_Play_World04 = 115
        FRFR_Play_World05 = 120
        FRFR_Play_World06 = 125
        FRFR_Play_World07 = 130
        FRFR_Play_World08 = 140
        FRFR_Play_World09 = 145
        FRFR_Play_World10 = 150
        FRFR_Play_World11 = 155
        FRFR_Play_World12 = 160
        FRFR_World01 = 10
        FRFR_World02 = 15
        FRFR_World03 = 20
        FRFR_World04 = 25
        FRFR_World05 = 30
        FRFR_World06 = 35
        FRFR_World07 = 40
        FRFR_World08 = 45
        FRFR_World09 = 50
        FRFR_World10 = 55
        FRFR_World11 = 60
        FRFR_World12 = 65
        SDKL_AlertEdgesRed = 200
        SDKL_LootWhite = 205
        SDKL_StaticBlack = 210


class Gamedec(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        GMDC_InterrogationBase = 200
        GMDC_InterrogationOne = 202
        GMDC_InterrogationTwo = 204
        GMDC_Menu = 600
        SDKL_Crimson = 10
        SDKL_Day = 32
        SDKL_EnvAutumn = 26
        SDKL_EnvDark = 12
        SDKL_EnvDarkBlue = 30
        SDKL_EnvDarkGrey = 28
        SDKL_EnvDarkRed = 31
        SDKL_EnvMud = 24
        SDKL_EnvSand = 22
        SDKL_EnvSummer = 34
        SDKL_EnvSunset = 40
        SDKL_EnvTech = 36
        SDKL_FadeToBlack = 500
        SDKL_FireHit = 398
        SDKL_FireworksYellowWhiteBlue = 400
        SDKL_HeartRed = 402
        SDKL_LootBlue = 404
        SDKL_PulseBarBlue = 418
        SDKL_PulseBarGreen = 406
        SDKL_PulseBarRed = 416
        SDKL_PulseBarYellow = 410
        SDKL_PulseOrange = 418
        SDKL_PulseStarGreen = 422
        SDKL_SplashBlue = 414
        SDKL_SplashYellow = 408
        SDKL_WaveDownBlue = 252
        SDKL_WaveDownGreen = 256
        SDKL_WaveDownPink = 420
        SDKL_WaveDownPurple = 254
        SDKL_WaveDownYellow = 250
        SDKL_WaveUpGreen = 412


class Ghostrunner(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        GHST_Blink = 110
        GHST_CyberVoid = 20
        GHST_CyberVoidDestination = 21
        GHST_CyberVoidRed = 22
        GHST_Death = 170
        GHST_Dharma = 45
        GHST_IndustryGreen = 31
        GHST_IndustryMain = 30
        GHST_IndustryOrange = 32
        GHST_IndustryRed = 35
        GHST_Menu = 235
        GHST_Sensory = 80
        GHST_Zipline = 65
        SDKL_AlertEdgesOrange = 165
        SDKL_AlertEdgesYellow = 160
        SDKL_Melee = 85
        SDKL_PulseBarBlue = 155
        SDKL_PulseBarWhite = 150
        SDKL_ScreenReactive = 60
        SDKL_SplashBlue = 145
        SDKL_SplashGrey = 140
        SDKL_SplashYellow = 135


class GridForce(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        GRID_Dream = 60
        GRID_Menu = 220
        SDKL_EnvBlossom = 19
        SDKL_EnvDark = 18
        SDKL_EnvDarkBlue = 13
        SDKL_EnvDarkGreen = 15
        SDKL_EnvDarkGrey = 10
        SDKL_EnvDarkPink = 17
        SDKL_EnvGreen = 20
        SDKL_EnvSand = 14
        SDKL_EnvSummer = 11
        SDKL_EnvWinter = 12
        SDKL_FadeToBlack = 170
        SDKL_Night = 16
        SDKL_PulseBarWhite = 122
        SDKL_PulsePink = 201
        SDKL_PulseStarPink = 120
        SDKL_SplashGrey = 150
        SDKL_SplashPink = 121
        SDKL_TVNoise = 200
        SDKL_Titanium = 22
        SDKL_UnderwaterBlue = 21
        SDKL_WaveDownPink = 125
        SDKL_WaveUpWhite = 130


class HelloNeighbor2(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        HENE_MenuMain = 500
        SDKL_Cutscene = 450
        SDKL_EnvAutumn = 15
        SDKL_EnvDarkBlue = 30
        SDKL_EnvDarkOrange = 5
        SDKL_EnvDarkPink = 20
        SDKL_EnvDarkRed = 35
        SDKL_EnvDarkYellow = 25
        SDKL_EnvMud = 40
        SDKL_EnvSummer = 45
        SDKL_FlashGrey = 320
        SDKL_LootGold = 330
        SDKL_PulseBlack = 350
        SDKL_SparksRed = 300
        SDKL_TVNoise = 200
        SDKL_WaterBlue = 10


class Hyperscape(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        HYPE_Assist = 109
        HYPE_Break = 103
        HYPE_Card = 70
        HYPE_Crown = 121
        HYPE_CrownAlmost = 122
        HYPE_CrownStart = 120
        HYPE_Damage = 140
        HYPE_DamageEMP = 142
        HYPE_DamageMelee = 144
        HYPE_DamageShot = 143
        HYPE_DamageZone = 141
        HYPE_Day = 10
        HYPE_Death = 161
        HYPE_Default = 15
        HYPE_Emote = 80
        HYPE_EmoteCorsair = 81
        HYPE_Fog = 19
        HYPE_GameOver = 182
        HYPE_HackArmor = 62
        HYPE_HackBall = 50
        HYPE_HackBallBounce = 51
        HYPE_HackDefault = 66
        HYPE_HackEMP = 64
        HYPE_HackFirewall = 63
        HYPE_HackHeal = 59
        HYPE_HackInvisibility = 54
        HYPE_HackMagnet = 61
        HYPE_HackMine = 58
        HYPE_HackPickup = 93
        HYPE_HackPowerRay = 65
        HYPE_HackReveal = 53
        HYPE_HackShockwave = 57
        HYPE_HackSlam = 55
        HYPE_HackSlamHit = 56
        HYPE_HackTeleport = 60
        HYPE_HackWall = 52
        HYPE_Healing = 108
        HYPE_Hyperscape = 235
        HYPE_Insert = 82
        HYPE_InsertFast = 83
        HYPE_JumpPad = 106
        HYPE_Kill = 110
        HYPE_Loading = 240
        HYPE_Lobby = 20
        HYPE_Map = 236
        HYPE_Morning = 14
        HYPE_Night = 11
        HYPE_Pipe = 104
        HYPE_Revealed = 107
        HYPE_Revive = 131
        HYPE_Reviving = 132
        HYPE_Spirit = 160
        HYPE_SquadAid = 130
        HYPE_SquadDeath = 129
        HYPE_StaticHighlight1 = 211
        HYPE_StaticHighlight2 = 212
        HYPE_Sunrise = 12
        HYPE_Sunset = 13
        HYPE_Tower = 105
        HYPE_Victory = 180
        HYPE_VictoryCrown = 181
        HYPE_WeaponFusion = 94
        HYPE_WeaponMFusion = 95
        HYPE_WeaponMelee = 91
        HYPE_WeaponPickup = 92
        HYPE_WeaponShoot = 90
        HYPE_ZoneClosing = 17
        SDKL_Cutscene = 220
        SDKL_Rain = 21
        SDKL_StaticWhite = 210


class INMOST(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        INMO_Menu = 10
        SDKL_DamageCenter = 60
        SDKL_EnvDark = 30
        SDKL_EnvDarkBlue = 15
        SDKL_EnvDarkGreen = 25
        SDKL_EnvSunset = 20
        SDKL_EnvWinter = 35
        SDKL_Fire = 40
        SDKL_Injured = 45
        SDKL_PulseBarWhite = 50
        SDKL_PulseStarGrey = 55
        SDKL_WipeWhite = 200


class IXION(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        IXIO_Construction = 150
        IXIO_EKP = 550
        IXIO_Exterior = 75
        IXIO_GameOver = 590
        IXIO_Interior = 70
        IXIO_Loading = 610
        IXIO_MenuMain = 750
        IXIO_Overload = 160
        IXIO_Space = 80
        IXIO_Vohle = 560
        SDKL_AudioGold = 145
        SDKL_Cutscene = 615
        SDKL_EnvSand = 120
        SDKL_EnvWinter = 140
        SDKL_Explosion = 350
        SDKL_GlowOrange = 310
        SDKL_GlowRed = 315
        SDKL_LightningStrike = 130
        SDKL_PulseBarBlue = 360
        SDKL_PulseGreen = 370
        SDKL_PulseYellow = 380
        SDKL_ShockRed = 125
        SDKL_Snow = 135
        SDKL_StaticBlack = 170
        SDKL_StaticEdgeGold = 540
        SDKL_TVNoise = 345
        SDKL_Titanium = 165
        SDKL_WaveUpWhite = 110


class MetroExodus(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        METE_Autumn = 11
        METE_BloodSplatter = 74
        METE_Charger = 105
        METE_DeadCity = 15
        METE_DeathExplosion = 163
        METE_DeathFire = 162
        METE_DeathGas = 161
        METE_DeathWater = 164
        METE_DeathWound = 160
        METE_Desert = 13
        METE_Drinks = 91
        METE_Furnace = 90
        METE_Gas = 130
        METE_Guitar = 30
        METE_Heart = 75
        METE_Interior = 14
        METE_Invisible = 120
        METE_KarmaBad = 155
        METE_KeyHint = 150
        METE_Knockout = 73
        METE_LightOff = 93
        METE_LightOn = 92
        METE_Lighter = 70
        METE_Menu = 235
        METE_Mushroom = 101
        METE_Sandstorm = 40
        METE_Sleep = 36
        METE_Smoke = 41
        METE_SplashAqua = 140
        METE_SplashSpider = 141
        METE_Suffocate = 151
        METE_Summer = 10
        METE_Takedown = 72
        METE_Taxi = 80
        METE_WebBurn = 71
        METE_Winter = 12
        METE_Workbench = 35
        SDKL_Alarm = 157
        SDKL_Cutscene = 210
        SDKL_Explosion = 138
        SDKL_FireHit = 137
        SDKL_FlashRed = 146
        SDKL_FlashWhite = 156
        SDKL_Healing = 100
        SDKL_Injured = 145
        SDKL_Lightning = 57
        SDKL_Melee = 135
        SDKL_Qte = 158
        SDKL_Radioactive = 47
        SDKL_Rain = 55
        SDKL_RangeHit = 136
        SDKL_ShockBlue = 139
        SDKL_Snow = 56
        SDKL_Underwater = 46
        SDKL_Water = 45


class MidnightGhostHunt(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        MNGH_Menu = 220
        MNGH_Midnight = 70
        SDKL_AlertEdgesRed = 160
        SDKL_BloodSplatter = 170
        SDKL_EnvDark = 30
        SDKL_EnvDarkBlue = 33
        SDKL_EnvDarkGreen = 31
        SDKL_EnvDarkGrey = 35
        SDKL_EnvSand = 32
        SDKL_LootBlue = 120
        SDKL_LootRed = 121
        SDKL_Night = 36
        SDKL_SmokeBlackout = 34


class OldWorld(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        OLDW_MenuMain = 500
        SDKL_BloodSplatter = 353
        SDKL_EnvAutumn = 50
        SDKL_FireHitRed = 396
        SDKL_LootYellow = 400
        SDKL_PulseBarWhite = 350
        SDKL_SplashWhite = 356
        SDKL_StaticEdgeBlue = 302
        SDKL_StaticEdgeGold = 306
        SDKL_StaticEdgeGreen = 308
        SDKL_StaticEdgeGrey = 300
        SDKL_StaticEdgeOrange = 310
        SDKL_StaticEdgePink = 314
        SDKL_StaticEdgePurple = 304
        SDKL_StaticEdgeRed = 320
        SDKL_StaticEdgeWhite = 322
        SDKL_StaticEdgeYellow = 324
        SDKL_WaveDownRed = 354
        SDKL_WaveUpBlue = 398
        SDKL_WaveUpYellow = 358


class Overloop(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        OVLP_BossArena = 90
        OVLP_Menu = 701
        OVLP_Reactor = 95
        SDKL_AlertEdgesRed = 150
        SDKL_BloodSplatter = 170
        SDKL_Day = 10
        SDKL_EnvDark = 12
        SDKL_EnvDarkBlue = 14
        SDKL_EnvDarkGrey = 16
        SDKL_EnvDarkRed = 18
        SDKL_EnvMud = 20
        SDKL_EnvSand = 22
        SDKL_EnvSummer = 24
        SDKL_EnvSunset = 26
        SDKL_EnvWhite = 28
        SDKL_Explosion = 175
        SDKL_FadeToBlack = 650
        SDKL_FadeToWhite = 660
        SDKL_FlashBlue = 180
        SDKL_FlyingDown = 190
        SDKL_LootBlue = 280
        SDKL_Night = 30
        SDKL_PulseBarBlue = 210
        SDKL_PulseBarGreen = 220
        SDKL_PulseBarYellow = 230
        SDKL_PulseGrey = 240
        SDKL_PulseStarBlue = 250
        SDKL_PulseStarYellow = 260
        SDKL_SplashBlue = 270
        SDKL_StaticBlack = 600
        SDKL_UnderwaterBlue = 32
        SDKL_WaveDownWhite = 100


class PHOGS(_Game):
    _name = 'PHOGS!'

    # noinspection PyPep8Naming
    class profile(_Profile):
        PHOG_Food = 15
        PHOG_Play = 20
        PHOG_Tutorial = 30
        SDKL_AlertEdgesRed = 185
        SDKL_AlertEdgesWhite = 165
        SDKL_Fire = 57
        SDKL_FireHitYellow = 180
        SDKL_FirePink = 60
        SDKL_FireRed = 55
        SDKL_FireWhite = 50
        SDKL_FlashWhite = 190
        SDKL_FlyingUp = 130
        SDKL_Ice = 80
        SDKL_Poison = 25
        SDKL_PulseOrange = 150
        SDKL_PulseStarGrey = 175
        SDKL_ShapeSpinWhite = 210
        SDKL_SparksWhite = 170
        SDKL_SplashYellow = 160
        SDKL_Suffocate = 155
        SDKL_WaterBlue = 45
        SDKL_WaterBrown = 40
        SDKL_WipeWhite = 200


class PlagueTaleRequiem(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        APTR_Menu = 750
        APTR_Rats = 255
        APTR_Sense = 250
        SDKL_Alarm = 345
        SDKL_BloodSplatter = 350
        SDKL_EnvAutumn = 5
        SDKL_EnvDark = 25
        SDKL_EnvDarkGrey = 20
        SDKL_EnvMud = 15
        SDKL_EnvShallows = 30
        SDKL_EnvSickly = 35
        SDKL_EnvSummer = 40
        SDKL_EnvVillage = 10
        SDKL_Sunset = 45
        SDKL_Titanium = 450


class ProjectWinter(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        PWIN_Ghost = 20
        PWIN_Menu = 400
        PWIN_Neutral = 18
        PWIN_Survivor = 16
        PWIN_Traitor = 14
        SDKL_DamageClaws = 98
        SDKL_Drunk = 156
        SDKL_EnvDarkBlue = 13
        SDKL_EnvWhite = 306
        SDKL_EnvWinter = 10
        SDKL_FadeToWhite = 154
        SDKL_Ice = 40
        SDKL_Injured = 100
        SDKL_Lighter = 22
        SDKL_LootRed = 304
        SDKL_LootYellow = 300
        SDKL_Neon = 157
        SDKL_Night = 12
        SDKL_PulseBarYellow = 302
        SDKL_PulseCyan = 56
        SDKL_PulseGreen = 54
        SDKL_PulseOrange = 52
        SDKL_PulsePurple = 58
        SDKL_PulseStarBlack = 150
        SDKL_PulseStarOrange = 158
        SDKL_PulseYellow = 50
        SDKL_SplashRed = 180
        SDKL_StaticBlack = 350


class RedSolstice2(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        RSL2_Menu = 190
        SDKL_Alarm = 108
        SDKL_EnvDarkGreen = 26
        SDKL_EnvDarkGrey = 28
        SDKL_EnvMud = 32
        SDKL_EnvWinter = 44
        SDKL_Explosion = 120
        SDKL_FadeToBlack = 200
        SDKL_Fire = 110
        SDKL_LootBlue = 116
        SDKL_MushroomCloud = 150
        SDKL_Night = 74
        SDKL_PulseBarRed = 118
        SDKL_PulseBarYellow = 114
        SDKL_Smoke = 68
        SDKL_WaveDownPurple = 112


class RhythmSprout(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        RHSP_Castle = 5
        RHSP_Menu = 500
        SDKL_EnvDarkGreen = 30
        SDKL_EnvDarkPink = 110
        SDKL_EnvDarkPurple = 20
        SDKL_EnvDesert = 10
        SDKL_EnvGreen = 115
        SDKL_EnvJungle = 35
        SDKL_EnvSand = 65
        SDKL_EnvShallows = 40
        SDKL_EnvSummer = 60
        SDKL_EnvTech = 70
        SDKL_EnvVillage = 85
        SDKL_EnvWinter = 15
        SDKL_Explosion = 200
        SDKL_FirePink = 55
        SDKL_FireworksPinkWhiteCyan = 300
        SDKL_GlowRed = 205
        SDKL_LootPurple = 410
        SDKL_Neon = 50
        SDKL_Poison = 45
        SDKL_StaticBlack = 400
        SDKL_StaticGrey = 54
        SDKL_UnderwaterCyan = 25
        SDKL_WaterCyan = 140


class SerialCleaners(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_EnvAlpine = 10
        SDKL_EnvDark = 16
        SDKL_EnvDarkBlue = 30
        SDKL_EnvDarkGreen = 12
        SDKL_EnvDarkGrey = 11
        SDKL_EnvDarkOrange = 13
        SDKL_EnvDarkRed = 20
        SDKL_EnvDarkYellow = 18
        SDKL_EnvSand = 17
        SDKL_FlashBlack = 200
        SDKL_PoliceLightsTop = 51
        SDKL_PulseBarGreen = 80
        SDKL_PulseBlue = 175
        SDKL_Rain = 50
        SDKL_SplashWhite = 174
        SDKL_SplashYellow = 176
        SDKL_Sunset = 15
        SECL_Arcade = 14


class SeveredSteel(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_Cobalt = 115
        SDKL_EnvDark = 135
        SDKL_EnvDarkBlue = 105
        SDKL_EnvTech = 250
        SDKL_Explosion = 240
        SDKL_FadeToBlack = 245
        SDKL_Nuclear = 130
        SDKL_Poison = 125
        SDKL_PulsePink = 235
        SDKL_SpeedLines = 200
        SDKL_Titanium = 110
        SDKL_WaterBlue = 100
        SDKL_WaterCyan = 120


class ShipOfFools(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_EnvDarkGreen = 130
        SDKL_FadeToBlack = 450
        SDKL_GlowRed = 320
        SDKL_Lava = 160
        SDKL_LightningStrike = 250
        SDKL_PulseStarWhite = 370
        SDKL_WaterBlue = 140
        SDKL_WaterCyan = 120
        SHIP_Boss = 350
        SHIP_Edge = 150
        SHIP_Menu = 750


class SIFU(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_Brimstone = 18
        SDKL_EnvDarkBlue = 16
        SDKL_EnvDarkGrey = 10
        SDKL_EnvDarkRed = 12
        SDKL_FadeToBlack = 100
        SDKL_FadeToWhite = 102
        SDKL_PulseBarWhite = 104
        SDKL_SmokeBlackout = 300
        SDKL_SplashBlue = 56
        SDKL_SplashGreen = 52
        SDKL_SplashRed = 54
        SDKL_SplashTan = 60
        SDKL_SplashWhite = 50
        SDKL_SplashYellow = 58
        SDKL_StaticWhite = 400
        SDKL_Titanium = 20
        SIFU_Squats = 14
        SIFU_Tower = 22
        SIFU_Wuguan = 24


class Starmancer(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_Brimstone = 13
        SDKL_Cobalt = 10
        SDKL_Crimson = 12
        SDKL_Fire = 130
        SDKL_FireGreen = 131
        SDKL_FireYellow = 132
        SDKL_HintBlue = 140
        SDKL_Nuclear = 14
        SDKL_Poison = 11
        SDKL_PulseBarBlue = 80
        SDKL_PulseStarBlue = 180
        SDKL_StaticBlack25 = 20
        SDKL_StaticBlack50 = 21
        SDKL_StaticBlack75 = 22
        SDKL_WaveDownRed = 161
        STAR_Menu = 200
        STAR_Purge = 162
        STAR_SpeedDouble = 42
        STAR_SpeedNormal = 41
        STAR_SpeedPaused = 40
        STAR_SpeedTriple = 43


class SubnauticaBZ(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_Alarm = 120
        SDKL_AlertEdgesBlue = 105
        SDKL_AlertEdgesRed = 90
        SDKL_AlertEdgesYellow = 100
        SDKL_BloodSplatter = 83
        SDKL_EnvDarkBlue = 45
        SDKL_EnvDarkGreen = 50
        SDKL_EnvWinter = 10
        SDKL_FadeToBlack = 200
        SDKL_Fire = 115
        SDKL_FireLime = 81
        SDKL_Ice = 20
        SDKL_Night = 55
        SDKL_NightDark = 80
        SDKL_SparksWhite = 110
        SDKL_Underwater = 75
        SDKL_UnderwaterBlue = 30
        SDKL_UnderwaterCyan = 40
        SDKL_WaterBlue = 15
        SDKL_WaterBrown = 60
        SDKL_WaterCyan = 25


class SuperMagBot(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        MAGB_ChargeB1 = 401
        MAGB_ChargeB2 = 402
        MAGB_ChargeR1 = 403
        MAGB_ChargeR2 = 404
        MAGB_Charges = 400
        MAGB_DashBlue = 72
        MAGB_DashRed = 70
        MAGB_Magnetia = 58
        MAGB_Menu = 500
        SDKL_Brimstone = 54
        SDKL_Cutscene = 600
        SDKL_EnvSummer = 50
        SDKL_Ice = 52
        SDKL_Neon = 56
        SDKL_Poison = 450
        SDKL_PulseBarBlue = 120
        SDKL_PulseBarPink = 122
        SDKL_PulseBarRed = 118
        SDKL_PulseBarYellow = 160
        SDKL_PulseStarCyan = 152
        SDKL_PulseStarGreen = 150
        SDKL_PulseStarOrange = 154
        SDKL_PulseStarPink = 156
        SDKL_PulseStarYellow = 158
        SDKL_PulseYellow = 162


class SweetTransit(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_EnvAutumn = 20
        SDKL_EnvDark = 60
        SDKL_EnvMud = 10
        SDKL_EnvSand = 40
        SDKL_EnvSummer = 30
        SDKL_EnvWhite = 230
        SDKL_SplashBlue = 250
        SDKL_UnderwaterBlue = 70
        SWTN_Menu = 500
        SWTN_Town = 110
        SWTN_Trains = 200
        SWTN_Village = 100


class TerraInvicta(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_Alarm = 159
        SDKL_AlertEdgesRed = 160
        SDKL_Explosion = 161
        SDKL_MushroomCloud = 170
        SDKL_PulseBarGreen = 130
        SDKL_PulseBarRed = 131
        SDKL_Zoom = 120
        TRIN_Earth = 11
        TRIN_EncounterAliens = 77
        TRIN_EncounterBlue = 70
        TRIN_EncounterCyan = 74
        TRIN_EncounterGreen = 75
        TRIN_EncounterOrange = 72
        TRIN_EncounterPurple = 76
        TRIN_EncounterRed = 71
        TRIN_EncounterYellow = 73
        TRIN_FactionBlue = 20
        TRIN_FactionCyan = 24
        TRIN_FactionGreen = 25
        TRIN_FactionOrange = 22
        TRIN_FactionPurple = 26
        TRIN_FactionRed = 21
        TRIN_FactionYellow = 23
        TRIN_Menu = 220
        TRIN_Space = 10


class TheDivision2(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        DIV2_Bleed = 132
        DIV2_Blind = 150
        DIV2_Confuse = 129
        DIV2_Day = 10
        DIV2_Death = 160
        DIV2_DeathBleed = 163
        DIV2_DeathFire = 162
        DIV2_DeathPoison = 161
        DIV2_Default = 30
        DIV2_Disrupt = 130
        DIV2_Downed = 140
        DIV2_EnemyDetected = 120
        DIV2_EnemyScanned = 121
        DIV2_Ensnare = 128
        DIV2_Flare = 100
        DIV2_Hint = 50
        DIV2_Keeners = 236
        DIV2_LevelUp = 181
        DIV2_LevelUpSeasons = 182
        DIV2_Loot = 61
        DIV2_Map = 71
        DIV2_Memory = 70
        DIV2_Menu = 235
        DIV2_Night = 11
        DIV2_Poison = 139
        DIV2_Pulse = 73
        DIV2_PulseJam = 72
        DIV2_PulseScan = 75
        DIV2_RogueAgents = 119
        DIV2_SafeZone = 40
        DIV2_Salvage = 60
        DIV2_Shock = 131
        DIV2_Stealth = 25
        DIV2_Victory = 180
        SDKL_Cutscene = 240
        SDKL_Explosion = 127
        SDKL_Fire = 126
        SDKL_FireHit = 125
        SDKL_Fog = 57
        SDKL_Healing = 101
        SDKL_Melee = 123
        SDKL_Rain = 55
        SDKL_RangeHit = 122


class TheMedium(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        MEDI_EnvDarkGreen_H = 26
        MEDI_EnvDarkGreen_V = 28
        MEDI_EnvDark_H = 25
        MEDI_EnvDark_V = 27
        SDKL_Death = 170
        SDKL_EnvDark = 10
        SDKL_EnvDarkBlue = 12
        SDKL_EnvDarkGreen = 13
        SDKL_EnvDarkGrey = 11
        SDKL_EnvDarkRed = 15
        SDKL_EnvMud = 14
        SDKL_FlashGrey = 150
        SDKL_FlashWhite = 145
        SDKL_Injured = 120
        SDKL_LightningStrike = 125
        SDKL_LootWhite = 70
        SDKL_PulseGrey = 71
        SDKL_ShapeSpinWhite = 60
        SDKL_SplashOrange = 80
        SDKL_StaticBlack = 240


class TheSettlers(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_AlertEdgesRed = 500
        SDKL_EnvSand = 20
        SDKL_EnvSummer = 30
        SDKL_LootRed = 504
        SDKL_PillarsWhite = 400
        SDKL_PulseBarGrey = 300
        SDKL_PulseBarRed = 496
        SDKL_PulseGrey = 304
        SDKL_PulseStarBlue = 404
        SDKL_PulseStarOrange = 408
        SDKL_Smoke = 40
        SDKL_SplashWhite = 600
        SDKL_WaveRightYellow = 412
        TSET_GameLost = 700
        TSET_GameWon = 706
        TSET_MainMenu = 800


class Thymesia(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_Cutscene = 245
        SDKL_EnvAutumn = 34
        SDKL_EnvDarkGrey = 35
        SDKL_EnvDarkRed = 32
        SDKL_FadeToBlack = 200
        SDKL_PulseWhite = 123
        SDKL_SmokeBlackout = 221
        SDKL_SparksRed = 120
        SDKL_SplashWhite = 125
        THYM_FlashTeal = 122
        THYM_Fortress = 33
        THYM_MenuPause = 220
        THYM_PulseBarTeal = 201
        THYM_RoyalGarden = 31
        THYM_SeaOfTrees = 30
        THYM_WaveDownTeal = 121


class TribesOfMidgard(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_Alarm = 202
        SDKL_AlertEdgesRed = 288
        SDKL_Bleeding = 200
        SDKL_Cobalt = 480
        SDKL_DamageCenter = 286
        SDKL_EnvAutumn = 28
        SDKL_EnvDark = 26
        SDKL_EnvDarkGrey = 24
        SDKL_EnvMud = 22
        SDKL_EnvSummer = 20
        SDKL_EnvWinter = 30
        SDKL_FadeToGrey = 400
        SDKL_FireHitYellow = 358
        SDKL_LootGreen = 350
        SDKL_LootOrange = 352
        SDKL_LootRed = 354
        SDKL_LootYellow = 356
        SDKL_PulseBarBlue = 300
        SDKL_PulseBarGreen = 302
        SDKL_PulseBarGrey = 304
        SDKL_PulseBarRed = 306
        SDKL_PulseBarYellow = 308
        SDKL_PulseBlue = 310
        SDKL_PulseGreen = 312
        SDKL_PulseGrey = 314
        SDKL_PulsePurple = 316
        SDKL_PulseStarWhite = 318
        SDKL_PulseStarYellow = 320
        SDKL_PulseYellow = 322
        SDKL_SplashWhite = 324
        SDKL_StaticBlack = 504
        SDKL_StaticGrey = 506
        SDKL_StaticOrange25 = 50
        SDKL_StaticOrgange25 = 52
        SDKL_StaticPurple50 = 54
        SDKL_UnderwaterCyan = 32
        SDKL_WaveUpRed = 326
        TOMG_Menu = 500


class Vesper(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_Brimstone = 20
        SDKL_Cobalt = 36
        SDKL_Corrosive = 28
        SDKL_Crimson = 10
        SDKL_EnvDarkBlue = 16
        SDKL_EnvDarkGreen = 22
        SDKL_EnvDarkGrey = 30
        SDKL_EnvDarkRed = 26
        SDKL_FirePurple = 34
        SDKL_Neon = 32
        SDKL_Poison = 18
        SDKL_ShockBlue = 52
        SDKL_Smoke = 100
        SDKL_SparksWhite = 54
        SDKL_StaticWhite = 2
        SDKL_Sunset = 24
        SDKL_TVNoise = 50
        SDKL_UnderwaterBlue = 12
        SDKL_UnderwaterCyan = 14
        SDKL_WaveDownPurple = 56


class Wonderlands(_Game):
    # noinspection PyPep8Naming
    class profile(_Profile):
        SDKL_EnvAlpine = 48
        SDKL_EnvDarkGreen = 20
        SDKL_EnvDarkGrey = 46
        SDKL_EnvMud = 40
        SDKL_EnvSand = 30
        SDKL_EnvSummer = 12
        SDKL_EnvWinter = 18
        SDKL_Injured = 500
        SDKL_LootPurple = 504
        SDKL_LootWhite = 512
        SDKL_Poison = 32
        SDKL_PulseBarPurple = 136
        SDKL_PulseBarTan = 502
        SDKL_PulseGrey = 114
        SDKL_PulseStarTan = 510
        SDKL_PulseTan = 506
        SDKL_SparksBlue = 112
        SDKL_SparksGreen = 536
        SDKL_SplashPurple = 132
        SDKL_SplashWhite = 102
        SDKL_Titanium = 14
        SDKL_WaveDownWhite = 106
        SDKL_WaveUpWhite = 122
        SDKL_WhirlwindPurple = 134
        SDKL_WhirlwindWhite = 110
        TTWL_Abyss = 10
        TTWL_Beanstalk = 38
        TTWL_BrrZerkerRage = 104
        TTWL_CleansingFlames = 116
        TTWL_Climb = 16
        TTWL_DireSacrifice = 126
        TTWL_DungeonDesert = 34
        TTWL_EtherealBow = 124
        TTWL_FFYL = 530
        TTWL_Grasslands = 24
        TTWL_Hubtown = 22
        TTWL_LegendarySpawn = 508
        TTWL_LevelUp = 550
        TTWL_Loading = 700
        TTWL_MenuMain = 800
        TTWL_Mushroom = 26
        TTWL_Oasis = 28
        TTWL_Overworld = 90
        TTWL_PolymorphStart = 118
        TTWL_QuickChange = 750
        TTWL_Reaper = 128
        TTWL_Resurrect = 538
        TTWL_Seabed = 36
        TTWL_ShadowsActive = 130


ctyped.lib.add_path(ntpath.join(ntpath.dirname(__file__)))

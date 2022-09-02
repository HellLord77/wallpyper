__version__ = '0.0.1'  # https://github.com/sindresorhus/cli-spinners

import itertools
import json
import os
from typing import Iterator, Optional

_SPINNERS: Optional[dict[str, dict[str, int | list[str]]]] = None


class Spinner:
    DOTS = 'dots'
    DOTS_2 = 'dots2'
    DOTS_3 = 'dots3'
    DOTS_4 = 'dots4'
    DOTS_5 = 'dots5'
    DOTS_6 = 'dots6'
    DOTS_7 = 'dots7'
    DOTS_8 = 'dots8'
    DOTS_9 = 'dots9'
    DOTS_10 = 'dots10'
    DOTS_11 = 'dots11'
    DOTS_12 = 'dots12'
    DOTS_13 = 'dots13'
    DOTS_8_BIT = 'dots8Bit'
    SAND = 'sand'
    LINE = 'line'
    LINE_2 = 'line2'
    PIPE = 'pipe'
    SIMPLE_DOTS = 'simpleDots'
    SIMPLE_DOTS_SCROLLING = 'simpleDotsScrolling'
    STAR = 'star'
    STAR_2 = 'star2'
    FLIP = 'flip'
    HAMBURGER = 'hamburger'
    GROW_VERTICAL = 'growVertical'
    GROW_HORIZONTAL = 'growHorizontal'
    BALLOON = 'balloon'
    BALLOON_2 = 'balloon2'
    NOISE = 'noise'
    BOUNCE = 'bounce'
    BOX_BOUNCE = 'boxBounce'
    BOX_BOUNCE_2 = 'boxBounce2'
    TRIANGLE = 'triangle'
    ARC = 'arc'
    CIRCLE = 'circle'
    SQUARE_CORNERS = 'squareCorners'
    CIRCLE_QUARTERS = 'circleQuarters'
    CIRCLE_HALVES = 'circleHalves'
    SQUISH = 'squish'
    TOGGLE = 'toggle'
    TOGGLE_2 = 'toggle2'
    TOGGLE_3 = 'toggle3'
    TOGGLE_4 = 'toggle4'
    TOGGLE_5 = 'toggle5'
    TOGGLE_6 = 'toggle6'
    TOGGLE_7 = 'toggle7'
    TOGGLE_8 = 'toggle8'
    TOGGLE_9 = 'toggle9'
    TOGGLE_10 = 'toggle10'
    TOGGLE_11 = 'toggle11'
    TOGGLE_12 = 'toggle12'
    TOGGLE_13 = 'toggle13'
    ARROW = 'arrow'
    ARROW_2 = 'arrow2'
    ARROW_3 = 'arrow3'
    BOUNCING_BAR = 'bouncingBar'
    BOUNCING_BALL = 'bouncingBall'
    SMILEY = 'smiley'
    MONKEY = 'monkey'
    HEARTS = 'hearts'
    CLOCK = 'clock'
    EARTH = 'earth'
    MATERIAL = 'material'
    MOON = 'moon'
    RUNNER = 'runner'
    PONG = 'pong'
    SHARK = 'shark'
    DQPB = 'dqpb'
    WEATHER = 'weather'
    CHRISTMAS = 'christmas'
    GRENADE = 'grenade'
    POINT = 'point'
    LAYER = 'layer'
    BETA_WAVE = 'betaWave'
    FINGER_DANCE = 'fingerDance'
    FIST_BUMP = 'fistBump'
    SOCCER_HEADER = 'soccerHeader'
    MINDBLOWN = 'mindblown'
    SPEAKER = 'speaker'
    ORANGE_PULSE = 'orangePulse'
    BLUE_PULSE = 'bluePulse'
    ORANGE_BLUE_PULSE = 'orangeBluePulse'
    TIME_TRAVEL = 'timeTravel'
    AESTHETIC = 'aesthetic'


def get_spinner(spinner: str) -> tuple[float, Iterator[str]]:
    global _SPINNERS
    if _SPINNERS is None:
        with open(os.path.join(os.path.dirname(__file__), 'spinners.json'), encoding='utf-8') as file:
            _SPINNERS = json.load(file)
    data = _SPINNERS[spinner]
    return data['interval'] / 1000, itertools.cycle(_SPINNERS[spinner]['frames'])

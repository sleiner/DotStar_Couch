"""
clear

This lightshow just turns the whole strip off.

Parameters:
   =====================================================================
   ||                     ||    python     ||   JSON representation   ||
   || fadetime_sec:       ||    numeric    ||        numeric          ||
   =====================================================================
"""

from drivers.fake_apa102 import APA102
import lightshows.solidcolor
from DefaultConfig import Configuration
import logging as log


minimal_number_of_leds = 1


# run this "show"
def run(strip: APA102, conf: Configuration, parameters: dict):
    # check if we have enough LEDs
    global minimal_number_of_leds
    if strip.numLEDs < minimal_number_of_leds:
        log.critical("This show needs a strip of at least {} LEDs to run correctly".format(minimal_number_of_leds))
        return

    fadetime_sec = parameters["fadetime_sec"]

    if fadetime_sec > 0:
        lightshows.solidcolor.blend_to_color(strip, (0, 0, 0), fadetime_sec)  # fadeout
    strip.clearStrip()


# tolerate no parameters
def parameters_valid(parameters: dict) -> bool:
    # is "fadetime_sec" set?
    if "fadetime_sec" not in parameters:
        return False

    # is "fadetime_sec" numeric?
    param_type = type(parameters["fadetime_sec"])
    if not (param_type is int or param_type is float):
        return False

    # is "fadetime_sec" positive?
    if parameters["fadetime_sec"] < 0:
        return False

    # now everything seems alright
    return True

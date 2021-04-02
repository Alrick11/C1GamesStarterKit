#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gamelib
import random
import math
import warnings
from sys import maxsize
import json
"""
Created on Thu Apr  1 01:01:50 2021

@author: alrick
"""

"""
Plan for the attach phase.
"""
def __init__(self):
    super().__init__()
    seed = random.randrange(maxsize)
    random.seed(seed)
    gamelib.debug_write('Random seed: {}'.format(seed))
    MUlocs = {"left":[[3, 10], [4, 9]], "right":[[24, 10], [23, 9]]}
    MUthreshold = 15
    MUmultiplier = 0.99

def place_scouts(self, game_state):
    if (game_state.MP > self.MUthreshold):
        game_state.attempt_spawn(SCOUT, self.MUlocs["left"][0], game_state.MP / 2)
        game_state.attempt_spawn(SCOUT, self.MUlocs["left"][1], game_state.MP / 2)
    self.MUthreshold *= self.MUmultiplier
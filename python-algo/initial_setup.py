#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 23:16:54 2021

@author: alrick
"""

"""
Spawning intial structure.
"""

def Turn0Spawn():
    """
    Inputs: None (Fixed starting strategy)
    Outputs: Coordinates of structure units at the start of the game.
    
    Description: Return positions of Wall, Turrets and Support at the start of 
    game. Function is called in Algo_strategy.strategy function when turn==0.
    """
    #U-shape WALL
    WALL_LOC = [[11,4],[10,5],[9,6],[8,7],[7,8],[6,9],[5,10],[4,11],[3,12],[2,13],\
                [1,13],[0,13],\
                [16,4],[17,5],[18,6],[19,7],[20,8],[21,9],[22,10],[23,11],[24,12],\
                [25,13],[26,13],[27,13]]
    
    #TURRETs at end positions
    #Place [15,3] next round
    TURR_LOC = [[12,3],[2,12],[25,12]]
    
    #SUPPORTS CURRENTLY NOT DECIDED EXACT LOCATIONS.
    
    return [WALL_LOC, TURR_LOC]

def Turn1Spawn():
    """
    Inputs: None
    Outputs: Coordindate of Turret
    
    Description: Since One Turret is short at the center due to SP getting over
    ,we need to spawn it on turnnumber 1.
    """
    
    return [[15,3]]
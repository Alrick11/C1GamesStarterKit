#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 01:02:20 2021

@author: alrick
"""

"""
Plan for the defense phase.
"""

import json

CREATE=1
REPAIR=2
UPGRADE=3

def PriorityQueue(config):
    """
    Creates the Priority Queue based on actions, to and not to
    """
    
    WALL = config["unitInformation"][0]["shorthand"]
    SUPPORT = config["unitInformation"][1]["shorthand"]
    TURRET = config["unitInformation"][2]["shorthand"]
    
    # WALL = "WALL"
    # TURRET = "TURRET"
    # SUPPORT = "SUPPORT"
    
    PQ = {"HIGH":[], "MEDIUM":{}, "LOW":[]}
    
    """
    Intially start with V-shape walls having very high priority.
    With ones closer to opponent with higher PQ.
    """
    t_wall_create=[]
    for i in range(3):
        t_wall_create.append([WALL, [i, 13], CREATE])
        
    for i in [25,26,27]:
        t_wall_create.append([WALL, [i, 13], CREATE])
        
    i, j = 3, 12
    while (i<=11):
        t_wall_create.append([WALL, [i, j], CREATE])
        i+=1
        j-=1
        
    i,j=24,12
    while (i>=16):
        t_wall_create.append([WALL, [i,j], CREATE])
        i-=1
        j-=1
        
    PQ["HIGH"]+=t_wall_create
    
    #ADD TURRETS AT THE IMPORTANT POSITIONS
    t_turr_create = [[TURRET, [12,3], CREATE], [TURRET, [2,12], CREATE], [TURRET, [25,12], CREATE],\
         [TURRET, [15,3], CREATE], [TURRET, [15,4], CREATE], [TURRET, [12,4],CREATE]]
    
    PQ["HIGH"]+=t_turr_create
    
    #WALLS JUST NEAR THE INITIAL TURRETS FOR PROTECTION.
    t_walls_protect = [[WALL, [1,12], CREATE], [WALL, [3,13], CREATE], \
                       [WALL, [26,12], CREATE], [WALL, [24,13], CREATE]]
    
    PQ["HIGH"]+=t_walls_protect
        
    #NEXT PQ FOR REPAIRING UNITS, SINCE UPGRADING LOW HEALTH UNITS WONT MAKE SENSE
    t_wall_repair=[]
    for elem in t_wall_create:
        t_wall_repair.append(elem[:-1] + [REPAIR])
        
    t_turr_repair=[]
    for elem in t_turr_create:
        t_turr_repair.append(elem[:-1] + [REPAIR])
    
    PQ["HIGH"]+=t_wall_repair
    PQ["HIGH"]+=t_turr_repair
    
    #MID LEVEL IMPORTANCE. FIRST ADD WALLS NEAR THE EDGES (CROWD THAT AREA)
    t_walls_near_edges = [[WALL, [4,12], CREATE], [WALL, [4,13], CREATE], \
                          [WALL, [5,12], CREATE], [WALL, [5,13], CREATE], \
                        [WALL, [22,12], CREATE], [WALL, [22,13], CREATE], \
                        [WALL, [23,12], CREATE], [WALL, [23,13], CREATE]]
    
    #UPGRADE WALLS NEAR EDGES
    #MEDIUM HAS OPTIONS FOR UPGRADING EITHER LEFT OR RIGHT. CAN COME HANDY LATER.
    t_walls_left_upgrade = [[WALL, [0,13], UPGRADE], [WALL, [1,13], UPGRADE], \
                            [WALL, [2,13], UPGRADE]]
    t_walls_right_upgrade = [[WALL, [27,13], UPGRADE], [WALL, [26,13], UPGRADE],\
                             [WALL, [25,13], UPGRADE]]
    
    PQ["MEDIUM"]["HIGH"] = {"LEFT":[], "RIGHT":[]}
    PQ["MEDIUM"]["HIGH"]["LEFT"]+= t_walls_left_upgrade
    PQ["MEDIUM"]["HIGH"]["RIGHT"]+= t_walls_right_upgrade
    
    #UPGRADE LEFT AND RIGHT TURRETS
    PQ["MEDIUM"]["MEDIUM"] = [[TURRET, [2,12], UPGRADE], [TURRET, [25,12], UPGRADE]]
    PQ["MEDIUM"]["MEDIUM"] += t_walls_near_edges

    #ADD TURRETS AND SUPPORTS IN THE CENTER
    PQ["MEDIUM"]["LOW"] = [[TURRET, [12,5], CREATE], [TURRET, [15,5], CREATE]]
    PQ["MEDIUM"]["LOW"] += [[SUPPORT, [6,10], CREATE], [SUPPORT, [11,5], CREATE]]
    PQ["MEDIUM"]["LOW"] += [[TURRET, [12,7], CREATE], [TURRET, [15,7], CREATE]]
    PQ["MEDIUM"]["LOW"] += [[SUPPORT, [10,6], CREATE], [SUPPORT, [7,9], CREATE],\
                            [SUPPORT, [8,8], CREATE]]
        
    #LOW PRIORITY: UPGRADE SUPPORTS AND ADD WALLS
    PQ["LOW"] = [[SUPPORT, [6,10], UPGRADE], [SUPPORT, [11,5], UPGRADE]]
    
    return PQ
    
    
if __name__=="__main__":
    """
    Testing code.
    """
    PriorityQueue()
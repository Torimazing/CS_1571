#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:32:46 2019

@author: milos
"""

# a heuristic function for the 'current' state and the target state
# currently returns 0 (no heuristics used)
def h_function(state,target_state):
    h = 0
    for tile in range(len(state)):
        if state[tile] == target_state[tile]:
            h+=1
    return h  
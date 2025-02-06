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
        pos_target = target_state.index(state[tile])
        h += abs(int(tile/3)-int(pos_target/3)) + abs((tile%3)-(pos_target%3))
    return h 
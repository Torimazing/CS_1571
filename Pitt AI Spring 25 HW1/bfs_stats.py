#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:00 2019
vanilla breadth first search
- relies on  Puzzle8.py module

@author: milos
"""

from Puzzle8 import *


 #### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 #### breadth first search         
        
global expanded_count
global generated_count
global max_len
global solution_len

expanded_count = 0
generated_count = 0
max_len = 0
solution_len = 0

def breadth_first_search(problem):
     global expanded_count, generated_count, max_len, solution_len
     queue =deque([])
     root=TreeNode(problem,problem.initial_state)
     queue.append(root)   
     while len(queue)>0:
         if len(queue) > max_len:
             max_len = len(queue)
         expanded_count += 1
         next=queue.popleft()
         if next.goalp():
             del(queue)
             solution_len = len(next.path())
             return next.path()
         else:
             new_nodes=next.generate_new_tree_nodes()
             for new_node in new_nodes:
                  generated_count += 1
                  queue.append(new_node)         
     print('No solution')
     return NULL

  
problem=Puzzle8_Problem(Example1) 
output=  breadth_first_search(problem)
print('Solution Example 1:')
print_path(output)
print("Nodes Expanded: "+str(expanded_count) + "\nNodes Generated: "+ str(generated_count) + "\nMax Queue Length: " + str(max_len) + "\nSolution Length: " + str(solution_len))

expanded_count = 0
generated_count = 0
max_len = 0
solution_len = 0

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example2) 
output=  breadth_first_search(problem)
print('Solution Example 2:')
print("Nodes Expanded: "+str(expanded_count) + "\nNodes Generated: "+ str(generated_count) + "\nMax Queue Length: " + str(max_len) + "\nSolution Length: " + str(solution_len))
print_path(output)

expanded_count = 0
generated_count = 0
max_len = 0
solution_len = 0

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example3) 
output=  breadth_first_search(problem)
print('Solution Example 3:')
print("Nodes Expanded: "+str(expanded_count) + "\nNodes Generated: "+ str(generated_count) + "\nMax Queue Length: " + str(max_len) + "\nSolution Length: " + str(solution_len))
print_path(output)

expanded_count = 0
generated_count = 0
max_len = 0
solution_len = 0

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example4) 
output=  breadth_first_search(problem)
print('Solution Example 4:')
print("Nodes Expanded: "+str(expanded_count) + "\nNodes Generated: "+ str(generated_count) + "\nMax Queue Length: " + str(max_len) + "\nSolution Length: " + str(solution_len))
print_path(output)

expanded_count = 0
generated_count = 0
max_len = 0
solution_len = 0

# Solution to Example 5 may take too long to calculate using vanilla bfs
# problem=Puzzle8_Problem(Example5) 
# print("Nodes Expanded: "+str(expanded_count) + "\nNodes Generated: "+ str(generated_count) + "\nMax Queue Length: " + str(max_len) + "\nSolution Length: " + str(solution_len))
# output=  breadth_first_search(problem)
# print('Solution Example 5:')
# print_path(output)
 
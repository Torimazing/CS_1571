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
global repeats_table

expanded_count = 0
generated_count = 0
max_len = 0
solution_len = 0
repeats_table = HashTable()

def breath_search_repeats(node):
    if repeats_table.in_hashp(node.state):
        return False
    return True

def breadth_first_search(problem):
     global expanded_count, generated_count, max_len, solution_len, repeats_table
     queue =deque([])
     root=TreeNode(problem,problem.initial_state)
     queue.append(root)   
     while len(queue)>0:
         if len(queue) > max_len:
             max_len = len(queue)
         expanded_count += 1
         next=queue.popleft()
         repeats_table.add_hash(next.state)
         if next.goalp():
             del(queue)
             solution_len = len(next.path())
             return next.path()
         else:
             new_nodes=next.generate_new_tree_nodes()
             for new_node in new_nodes:
                  if breath_search_repeats(new_node):
                      generated_count += 1
                      queue.append(new_node)
     print('No solution')
     return NULL

  
problem=Puzzle8_Problem(Example1) 
output=  breadth_first_search(problem)
print('Solution Example 1:')
print("Nodes Expanded: "+str(expanded_count) + "\nNodes Generated: "+ str(generated_count) + "\nMax Queue Length: " + str(max_len) + "\nSolution Length: " + str(solution_len))
print_path(output)

expanded_count = 0
generated_count = 0
max_len = 0
solution_len = 0
repeats_table = HashTable()

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
repeats_table = HashTable()

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
repeats_table = HashTable()

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
repeats_table = HashTable()

# Solution to Example 5 may take too long to calculate using vanilla bfs
problem=Puzzle8_Problem(Example5) 
output=  breadth_first_search(problem)
print('Solution Example 5:')
print("Nodes Expanded: "+str(expanded_count) + "\nNodes Generated: "+ str(generated_count) + "\nMax Queue Length: " + str(max_len) + "\nSolution Length: " + str(solution_len))
print_path(output)
 
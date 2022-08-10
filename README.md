# Google_Foobar_2022

Questions from the challenges I received while participating in Google's Foobar challenge in August 2022.
Brief descriptions of the thought process for my solutions are also provided.
Didn't bother copying the exact questions for the first two challenges so I only have condensed descriptions 
for those questions. 

## Challenge 1

Given an amount material (integer), return a list of the possible squares that can be made using that amount of material. 
The list should be in descending order. Example input: 12, Output: [9, 1, 1, 1]

*Solution:* Since each output needs to be a square, taking the square root of the value will lead to the largest square possible.
Repeat until the value is consumed.

## Challenge 2

**Question 1:**  
Given a list of integers, return the largest number that is divisible by three that can be made using the numbers in the list.
Not every number in the list needs to be used. Example input: [4, 0, 9, 6, 3], Output: 9630

*Solution:* Brute force solution is to just take every permutation of every subset of numbers in the list. There probably is a more
clever solution.

**Question 2:**  
Given an 8x8 grid with positions labeled 0 - 63, a starting position, and a goal, return the least number of moves to reach the goal. Only caveat is that you can only move using the "L-shape" pattern a knight uses in chess, i.e., move two squares in any direction vertically followed by one square horizontally, or two squares in any direction horizontally followed by one square vertically.
Example input: (start=0, goal=1), Output: 3

*Solution:* Simple breadth-first search works fine. Need to convert Start and Goal values into 2D coordinates.

## Challenge 3

**Question 1:**  
Prepare the Bunnies' Escape

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of 
the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Test cases:
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases -- 
Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
    7

Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Output:
    11

*Solution:*

**Question 2:**

**Question 3:**
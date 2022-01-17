# AI_Projects

## Approach to Part 1: The 2021 Puzzle

<h3>Abstraction:</h3>
<u><b>Set of Valid states</b></u>: Set of all probable boards which contains all unique numbers<br><br>
<u><b>Successor Function</b></u>: This function takes the board, generates all the possible boards by performing rotations i.e.,<b>{'R1','R2','R3','R4','R5','L1','L2','L3','L4','L5','U1','U2','U3','U4','U5','D1','D2','D3','D4','D5','Oc','Ic','Occ','Icc'}</b><br>
<p style="margin-left: 30px;">  where <b>R</b> stands for Right rotation of row for specified row,<br>
      <b>L</b> stands for Left rotation of row for specified row,<br>
      <b>U</b> stands for Up rotation of column for specified row,<br>
      <b>D</b> stands for Down rotation of column for specified row,<br>
      <b>Ic</b> stands for Inner clockwise rotation,<br>
      <b>Icc</b> stands for Inner counter-clockwise rotation,<br>
      <b>Oc</b> stands for Outer clockwise rotation,<br>
      <b>Occ</b> stands for Outer Counter clockwise rotation.<br></p>
After generating all the successor boards it calculates the heuristic_score for all boards and stores into the list.<br><br>
<u><b>Cost Function</b></u>: The cost of a generating successor is uniform: 1.<br><br>
<u><b>Goal State</b></u>: Board which contains all numbers from 1 to 25 in correct positions.<br><br>
<u><b>Initial State</b></u>: The board provided which has all unique numbers which are misplaced after certain valid rotations.<br><br>
<u><b>Heuristic Functions</b></u>: The first heuristic function I have used and thought of heuristic which was <b>Number of Misplaced Tiles</b> comparing to the goal state. Later in the process, I found it is overestimating for some boards along with that it was taking more amount to solve the board.

So, We thought of optimizing the heuristic function, so instead of above one tried implementing <b>Manhattan Distances</b> of each successor board which is better than the previous heuristic function which takes less time and got to know that this will be inadmissible when we are nearing the goal state.<br><br>

<br>
<i><h3>Description of Algorithm:</h3></i>
Implemented using uniform cost search algorithm with an heuristic and cost function.
<ol>
<li>I have used frontier(fringe) which is Priority Queue implemented using heapq module to store all the boards.Initially pushing the initial board on to the frontier.</li>
<li>Maintaing explored states which is empty at the initial point.</li>
<li>Looping till the frontier is not empty:</li>
<ol><li>Pop the board using heappop method in heapq module which gives the minheap board which has less heuristic score.</li>
<li>Checking whether the board popped is the goal state. If yes, the return and print the board.</li>
<li>Otherwise, add this board to explored list</li>
<li>Generate all the successors boards for this board.</li>

<ol>
<li>For each successor board, calculates the F_score which is the sum of heuristic score and no of rotations taken from the initial state to reach successor state.</li>
<li>If the successor board is not in explored and not in frontier, then heappush the board into frontier with f_score of that board.</li>
<li>If the successor board is in frontier with high f_score then the current successor board, then replace it with the current board.</li>
</ol></ol>
</ol></ol>

<b>1. In this problem, what is the branching factor of the search tree?</b><br>
The branching factor of this search tree is we get 24 childs(successors) everytime for a board.<br><br>

<b>2. If the solution can be reached in 7 moves, about how many states would we need to explore before we found it if we used BFS instead of A* search? A rough answer is fine.</b><br>
If we are implementing using BFS, we expand the board in level(breadth) from left to right wise. So for every board we get 24 child boards and for every child board we get other 24 childs so on till we get the goal board.

The branching factor is 24 because we have 24 valid rotations.<br>
<b>'R1','R2','R3','R4','R5','L1','L2','L3','L4','L5','U1','U2','U3','U4','U5','D1','D2','D3','D4','D5','Oc','Ic','Occ','Icc'}</b><br>
<br>
The simplified equation for finding how many states while using BFS approach is:
<br><p style="margin-left: 100px;"><b>
&sum;<sub>k=0</sub><sup>N</sup> 24<sup>k</sup>
    <br>where N here is 7 moves.</b>
</p>



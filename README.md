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

<h3>Approach to Raichu</h3>
<h4>Abstraction</h4>
<p><b>Set of Valid states: </b>All possible ways to arrange all the pieces such as pichu's,pikachu's and raichu's on the N*N board.<p>
<p><b>Initial State: </b> Consists of 4 parameters white/black piece turn explicitly mentioned through command line parameters followed by board size, initial board arrangement and timilimit.</p>
<p><b>Successor Function: </b>All possible moves to the given initial board arragements based on the rules defined for pichu's,Pikachu's and Raichu's.</p>
<p>This function would take board,player and board size as an arugument and generates all possible moves for the initial board arrangement.</p>
<p>Set of Valid Moves based on rules defined.</p>
<ul Type='disc'>
  <li><b>Black/White Pichu's left/right diagonal empty move:</b> Pichu's move one step to their right/left diagonal given the following square is empty(i.e it's value is'.')</li>
  <li><b>Black/White Pichu's left/right diagonal attack move:</b> Pichu's can jump over opposite colour pichu right/left diagonally given the following square is empty and replace the jumped opposite piece square value to '.'</li>
  <li><b>Black/White Pikachu's left/right/forward 1(or)2 steps empty move:</b>Pikachu's can move one/two steps to their right/left/forward given the following squares are with values'.'</li>
  <li><b>Black/White Pikachu's left/right/forward 2(or)3 steps attack move:</b>Pikachu's can jump over opposite colour pichu/pikachu right/left/forward if the attack piece is either one step way/2 steps away(given the sqaure in between is '.') and the sqaure after the jump also needs to be '.' and replace the jumped opposite piece square value to '.'</li>
  <li><b>Black/White Raichu's possible empty moves:</b>Raichu's can move any in all possible directions given that the destination sqaures needs to be '.'
  <li><b>Black/White Raichu's possible attack moves:</b>Raichu's can jump over opposite colour pichu/pikachu/raichu in all possible given direction give that all the squares in between are '.' and the jumped square piece position value is replaced by '.' and after the jump it can move in all possible directions again given that the destination squares needs to be '.'
</ul>
<p><b>Evaluation Function:</b> Evaluation function is given by:
  <p>Assumption in coding: pichu cost=1,pikachu cost=10, raichu cost=50.
  <p><b>e(s) = 1(number of white pichus − number of black pichus) + 10(number of white pikachus − number of black pikachus) + 50(number of white raichus - number of black raichus)</b></p>
 <p><b>Terminal State:</b>To find the best possible move for the given initial board arrangement based on the minimax algorithm and the evaluation function incorporated in it.</p>
 <p><b>Description of Algorithm:</b></p>
 <ol>
  <li>Implemented using the Minimax Algorithm with an evaluation function.</p></li>
  <li>Initially the horizon vaue is 1, hence it would explore all possible successors for depth 1 and start calculating the cost for leaf nodes based on evaluation function.</p></li>
  <li>Based on the values obtained for leaves,push back values to parents based on given level if it min then it would take max of it's successors and if it is max it would take the min of it's successors. That's how minimax algorithm wold work.</p></li>
 <li>Return the best possible move for that horizon which has max value</p></li>
  <li>Eventaully we would increase the horizon level and repeat the minimax algorithm with evaluation function.</p></li>
  <li><p>So our program would yield best poosible move for every horizon given time limit is not provided if not it would return the previous best possible move calculated as it keeps on yielding the result.</p></li>
  </ol>
  
<p><b>Problems Faced during implementation</b><p>
  <p>Raichu Problems:</p>
  <ul>
    <li>we need to check if at all we did jump over the oppsoite piece it needs to make sure it does only once per given chance to make sure this we made use of some kind of flag and resolved the problem.</li>
    <li>After jumping over the piece then we need to make sure to calculate all the next possible moves to raichu by making the jumped piece position to '.' and then we need to calculate the successors from that until an obstacle is found.</li>
  </ul
  <ul>
    <p>Evaluation Function:</p>
      <ul>
        <li>To figure out best possible evaluation we kind of asigned weights based on it's moves and designed the evaluation function.</li>
  </ul>



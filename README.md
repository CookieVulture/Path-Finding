# Path-Finding
 Path finding visualization with <b> A* algorithm</b>
 <br><br>
 <b> Modules - </b><br>
 <a href="https://www.pygame.org/">pygame</a> and <a href="https://wiki.python.org/moin/TkInter">tkinter</a>
 <br><br>
 <b>Language - </b>
 <br>Python
 
<br><br>
<strong> How Program works? </strong><br>
Run the program(main.py) and after that a box will open up. Choose two points. After that user can draw wall with Mouse and then press Space key to start Algorithm. Path can't pass through wall.
 <br><br>
 
 The <b>A* algorithm </b> works on principle of<br><center> F = G + H</center></br> 
 <br>
 <ul>
 <li> F is the total cost of node.</li>
 <li> G is distance between the current node and start node</li>
 <li> H is the heuristic - estimated distance from current node to end node.</li>
 </ul>
<img src="https://miro.medium.com/max/600/1*iSt-urlSaXDABqhXX6xveQ.png" alt="A* algorithm">
<br>
Let's assume node(0) is starting position and node(19) is end position. The current node is on node(4).
<br><br>
<strong>H</strong>
<br>
H is estimated distance from current node to end node. node(19) isover 7 spaces and 3 spaces from node(4). 
<br>
Here, use Pythagorus theorem,<br>
 a² + b² = c²<br>
 So, for currentnode the value of H is 7² + 3² = 58.
 <br>
 <strong> Note - </strong>
<br><p> Even if we don't apply the square root to 58, we will still get same output so skip that calculation. </p>
<br>
It's important that the estimated distance is always underestimation of total path or overstimation will lead to A* searching for nodes which are not <i>best</i> in terms of <b>F</b>.
<br><br>
<b>G</b><br>
G is the distance between current node and start node.
<br>
node(4) is 4 spaces away from initial node. So, value of G for currentNode is 4.
<br><br>
<b>F</b>
<br>
F is total cost of the node. So, value of F for currentNode is sum of G and H of currentNode which is 4+58 = 62.
<br><br>
<b> Why F?</b><br>
<img src="https://miro.medium.com/max/263/1*HppvOLfDxXqQRFn0Cv2dHQ.gif">
Rather than checking all node, pick the ones that have the highest chance of getting us to our goal with help of F value.
<br><br>
<b> Why not Djikstra?</b>
<br>
<img src="https://miro.medium.com/max/263/1*2jRCHqAbTCY7W7oG5ntMOQ.gif">
Take a good look. The Dijkstra keeps searching. It has no idea which node is 'good' and how we can achieve best result so it calculates paths for all available nodes.
<br>
<br>

<strong> Pseudo Code</strong>
<br>
Check out pseudo code for A* from <a href="http://www.policyalmanac.org/games/aStarTutorial.htm">Patrick Lester's blog</a>. 
<br>
<br>1. Add the starting square (or node) to the open list.
<br>2. Repeat the following:<br>
<br>A) Look for the lowest F cost square on the open list. We refer to this as the current square.
<br>B). Switch it to the closed list.
<br>C) For each of the 8 squares adjacent to this current square …<br>
<br><i>!)If it is not walkable or if it is on the closed list, ignore it. Otherwise do the following.
<br>!!)If it isn’t on the open list, add it to the open list. Make the current square the parent of this square. Record the F, G, and H costs of the square.
<br>!!!)If it is on the open list already, check to see if this path to that square is better, using G cost as the measure. A lower G cost means that this is a better path. If so, change the parent of the square to the current square, and recalculate the G and F scores of the square. If you are keeping your open list sorted by F score, you may need to resort the list to account for the change.
<br><b>D)</b></i> Stop when you:
Add the target square to the closed list, in which case the path has been found, or
Fail to find the target square, and the open list is empty. In this case, there is no path.
<br><br>3. Save the path. Working backwards from the target square, go from each square to its parent square until you reach the starting square. That is your path.

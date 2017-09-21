# Grid_World_Problem
### Problem

|&nbsp;|&nbsp;|&nbsp;|&nbsp;|
|---|---|---|---|
|**S**|&nbsp;|&nbsp;|&nbsp;|
|&nbsp;|**B**|&nbsp;|&nbsp;|
|&nbsp;|&nbsp;|&nbsp;|**G**|

An agent starting in the start state S must reach the goal state G. At each time step, the agent can go up, down, left or right. However, the agent’s movements are a bit noisy since it goes in the intended direction with a high probability a and in one of the two lateral directions with a low probability b. For instance, when executing the action up, the agent will indeed go up by one square with probability a, but may go left with probability b and right with probability b (here a + b + b = 1). Similarly, when executing the action left, the agent will indeed go left with probability a, but may go up with probability b and down with probability b, When an action takes the agent out of the grid world, the agent simply bounces off the wall and stays in its current location. For example, when the agent executes left in the start state it stays in the start state with probability a, it goes up with probability b and down with probability b. Similarly, when the agent executes up from the start state, it goes up with probability a, right with probability b and stays in the start state with probability b. Finally, when the agent is in the goal state, the task is over and the agent transitions to a special end state with probability 1 (for any action). This end state is absorbing, meaning that the agent cannot get out of the end state (i.e., it stays in the end state with probability 1 for every action).The agent receives a reward of 100 when it reaches the goal state, -70 for the bad state and -1 for every other state, except the end state, which has a 0 reward. The agent’s task is to find a policy to reach the goal state as quickly as possible, while avoiding the bad state.

### Aims
**for Value iteration:**   
Find the optimal policies and optimal value functions found for a = 0.9, b = 0.05 and for a = 0.8, b = 0.1  
Compare the differences in the optimal policies and value functions for the different combinations of a and b.  
**for Q-learning:**  
Find the optimal policies and optimal value functions found for ε = 0.05 and ε = 0.2.  
Find the impact of ε on the convergence of Q-learning.

### Discussion  
For value iteration, as the probability of lateral movement increases (from b = 0.05 to b = 0.1) the agent has an increased probability of accidentally moving into the bad state. This is reflected in both the value function (lower values, especially near the bad state) and the policy (the policy at state 5 and 6 actively avoid the bad state).  

For Q-learning, the higher ε is the more exploration there will be and convergence should be more uniform through- out the grid. We can see this in our examples above (compare the value function at states 2 and 3 for the different values of ε). The policies to which the algorithm converges varies with ε. A large ε means there will be more exploration, which decreases the likelihood that we will get stuck in a suboptimal policy. Note how in the examples above the policy when ε = 0.2 matches that of Q1 (ignoring the top row). When ε = 0.05 we see that the agent does not find the optimal policy from Q1 due to a lack of exploration.As for the rate of convergence, when ε is low the algorithm tends to converge quickly to a sub- optimal solution. When ε is high the algorithm converges slower than with low ε, but generally achieves a better solution.
import numpy as np
import random 
import InterationValue as iv

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
ACTIONS = [UP, DOWN, LEFT, RIGHT]

def initial(numStates, numActions):
	Q = np.zeros(numStates * numActions).reshape(numStates, numActions)
	N = np.zeros(numStates * numActions).reshape(numStates, numActions)
	T, R = iv.gridWorld(0.9, 0.05)
	return Q, N, T, R

def nextState(state, action, row = 4, colum = 4):
	availableAction = available_action(state)
	if action not in availableAction:
		return state
	if action == UP:
		return state - colum
	if action == DOWN:
		return state + colum
	if action == RIGHT:
		return state + 1
	if action == LEFT:
		return state - 1

def selectAction(Q, T, state, epsilon):
	rate = random.uniform(0, 1)

	action = np.where( Q[state,:] ==  Q[state,:].max())[0]
	bestaction = np.random.choice(action, 1)[0] 

	if rate < epsilon:
		action = [UP, DOWN, LEFT, RIGHT]
		bestaction = np.random.choice(action, 1)[0]

	states = iv.transition(state, bestaction)
	beststate = nextState(state, bestaction)
	rate_ = random.uniform(0, 1)
	if rate_ > T[state, beststate, bestaction]:
		beststate = np.random.choice(states, 1)[0]

	return beststate, bestaction

def available_action(state, row = 4, colum = 4):
	i = state / colum
	j = state % row
	nextAction = []
	nextAction =[UP if i - 1 >= 0 else -1,
            	DOWN if i + 1 < row else -1,
            	LEFT if j - 1 >= 0 else -1,
            	RIGHT if j + 1 < colum else -1]
	return  filter(lambda a: a != -1, nextAction)

def QNext(Q, state):
	nextAction = available_action(state)
	return Q[state, nextAction].max()

def Q_learning(Q, R, N, T, startState, goalState, endState, discount, episodes, epsilon):
	for times in range (0, episodes):
		state = startState
		while state != endState:
			s1, action = selectAction(Q, T, state, epsilon)
			if state == goalState:
				s1 = endState
			N[state, action] += 1
			Q[state, action] = Q[state, action] + (1.0 / N[state, action]) *(R[state] + discount * QNext(Q, s1) - Q[state, action])
			state = s1
	
	return Q
	
def policyChoosing(numStates, Q):
	pi = np.zeros(numStates)
	for state in range(0, numStates):
		pi[state] = np.argmax(Q[state, :])

	return pi

def main():
	numStates = 17
	numActions = 4
	startState = 4
	goalState = 15
	endState = 16

	Q, N, T, R = initial(numStates, numActions)
	Q = Q_learning(Q, R, N, T, startState, goalState, endState, 0.99, 10000, 0.2)
	print Q
	print policyChoosing(16, Q)
	
if __name__ == "__main__":
	main()
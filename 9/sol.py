#use deque?! how?!
from collections import deque

num,last_marble=map(int,open('input.txt','r').read().replace('points','').split(' players; last marble is worth '))

last_marble*=100

players=[0]*num
marbles=deque([0])

#ith marble
for move in range(1,last_marble+1):
	if move%23==0:
		marbles.rotate(7)
		players[move%num]+=(marbles.pop()+move)
		marbles.rotate(-1)
	else:
		marbles.rotate(-1)
		marbles.append(move)
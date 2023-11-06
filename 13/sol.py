#	1st Intersection: Left
#	2nd Intersection: Straight
#	3rd Intersection: Right
# 	So on and so forth. with i the ith time it reached an intersection, i%3=0 then left, i%3=1 then straight, i%3=2 then right.

#think of directions as numbers?
#     ^ 1
#  0 < > 2
#   3 v 

# going straight: do nothing to direction
# going right: (encoded_direction+1)%4
# going left: (encoded_direction-1)%4


# ^ and you encounter / your direction was 1 and becomes 2	  1 -> 2
# v and you encounter / your direction was 3 and becomes 0 -- 3 -> 0
# > and you encounter / your direction was 2 and becomes 1 -- 2 -> 1
# < and you encounter / your direction was 0 and becomes 3.   0 -> 3


# ^ and you encounter \ your direction was 1 and becomes 0    1 -> 0
# v and you envounter \ your direction was 3 and becomes 2 -- 3 -> 2
# > and you encounter \ your direction was 2 and becomes 3 -- 2 -> 3
# < and you encounter \ your direction was 0 and becomes 1    0 -> 1

st=open('input.txt','r').read().split('\n')
#map(lambda x:x.replace('<','-').replace('>','-')
carts=[]

for i in range(len(st)):
	for j in range(len(st[i])):
		direction=-1
		if st[i][j]=='<':
			direction=0
		elif st[i][j]=='^':
			direction=1
		elif st[i][j]=='>': 
			direction=2
		elif st[i][j]=='v':
			direction=3
		if direction>=0:
			carts.append({'intersection':0,'direction':direction,'location':(i,j),'ok':True})

carts.sort(key=lambda x:x['location'])

#remove carts, should be a grid
railroad=[list(s.replace('<','-').replace('>','-').replace('^','|').replace('v','|')) for s in st]

# def print_cart(cart):
# 	location=cart['location']
# 	direction=cart['direction']
# 	for i in range(len(railroad)):
# 		row=''
# 		for j in range(len(railroad[i])):
# 			if location==(i,j):
# 				if direction==0:
# 					row+='<'
# 				elif direction==1:
# 					row+='^'
# 				elif direction==2:
# 					row+='>'
# 				elif direction==3:
# 					row+='v'
# 			else:
# 				row+=railroad[i][j]
# 		print(row)

# def print_carts():
# 	locations={}
# 	crash=set()
# 	for cart in carts:
# 		if cart['location'] not in locations:
# 			locations[cart['location']]=cart['direction']
# 		else:
# 			crash.add(cart['location'])

# 	for i in range(len(railroad)):
# 		row=''
# 		for j in range(len(railroad[i])):
# 			if (i,j) in locations and (i,j) not in crash:
# 				direction=locations[(i,j)]
# 				if direction==0:
# 					row+='<'
# 				elif direction==1:
# 					row+='^'
# 				elif direction==2:
# 					row+='>'
# 				elif direction==3:
# 					row+='v'
# 			elif (i,j) in crash:
# 				row+='X'
# 			else:
# 				row+=railroad[i][j]
# 		print(row)

def next_location(location,direction):
	x,y=location
	if direction==0:
		return (x,y-1)
	if direction==1:
		return (x-1,y)
	if direction==2:
		return (x,y+1)
	if direction==3:
		return (x+1,y)

#improve!!
def step(cart):
	direction=cart['direction']
	nx,ny=next_location(cart['location'],direction)
	intersection=cart['intersection']
	char=railroad[nx][ny]
	if char=='/':
		if direction in (1,3):
			direction=(direction+1)%4
		else:
			direction=(direction-1)%4
	elif char=='\\':
		if direction in (1,3):
			direction-=1
		else:
			direction+=1
	elif char=='+':
		if intersection%3==0:
			direction=(direction-1)%4
		elif intersection%3==2:
			direction=(direction+1)%4
		intersection+=1
	cart['direction']=direction
	cart['location']=(nx,ny)
	cart['intersection']=intersection

def crash(cart,other):
	return cart!=other and cart['location']==other['location']


#a tick consists of moving each cart once
def tick():
	carts.sort(key=lambda x:x['location'])
	for cart in carts:
		step(cart)
		for other in carts:
			if crash(cart,other):
				cart['ok']=other['ok']=False
				print('crash reported in '+str(cart['location'][1])+','+str(cart['location'][0]) )


def print_carts_position():
    for i in carts:
        print((i['location'][1],i['location'][0]))






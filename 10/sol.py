st=list(map(lambda x:x.split('velocity='),open('input.txt','r').read().replace('<','').replace('>','').replace(' ','').replace('position=','').split('\n')))
start_position={i:list(map(int,v[0].split(','))) for i,v in enumerate(st)}
velocity={i:list(map(int,v[1].split(','))) for i,v in enumerate(st)}

#move from original position
def move(index,t):
	x,y=start_position[index]
	x_,y_=velocity[index]
	return (x+(x_*t),y+(y_*t))



def grid(tf):
	return {i:move(i,tf) for i in start_position}

def area(grid):
	x0=min(i[0] for i in grid.values())
	x1=max(i[0] for i in grid.values())
	y0=min(i[1] for i in grid.values())
	y1=max(i[1] for i in grid.values())

	return (x1-x0)*(y1-y0)

def min_area():
	t=0
	curr=area(start_position)
	prev=curr+1
	for i in range(100000):
		prev=curr
		curr=area(grid(i))
		if curr>prev:
			print(i-1)
			break

def print_grid(grid):
	x0=min(i[0] for i in grid.values())
	x1=max(i[0] for i in grid.values())
	y0=min(i[1] for i in grid.values())
	y1=max(i[1] for i in grid.values())

	for y in range(y0,y1+1):
		line=''
		for x in range(x0,x1+1):
			if (x,y) in grid.values():
				line+='#'
			else:
				line+=' '
		print(line)

import functools
import collections
########################################################################################################
########################################################################################################
############							WARNING												############
############						SHIT CODE AHEAD											############
############																				############
############							REFACTOR											############
########################################################################################################
########################################################################################################

manhattan_distance=lambda p1,p2:abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

st=open('input.txt','r').read().split('\n')
points={i:tuple(map(int,st[i].split(', '))) for i in range(len(st))}
x0=min(point[0] for point in points.values())
x1=max(point[0] for point in points.values())
y0=min(point[1] for point in points.values())
y1=max(point[1] for point in points.values())

def part1grid():
	grid={}
	#for each point in the grid, calculate manhattan distance with each point, get lowest.
	for x in range(x0,x1+1):
		for y in range(y0,y1+1):
			distances=sorted([(idx,manhattan_distance((x,y),points[idx])) for idx in points],key=lambda x:x[1])
			#shares closest dist with two points, not useful.
			if distances[0][1]==distances[1][1]:
				grid[(x,y)]=None
			else:
				#else we get the index of the closest point
				grid[(x,y)]=distances[0][0]
	return grid

def get_boundary_idx(grid):
	boundary_idx=set()
	for point,idx in grid.items():
		if point[0] in (x0,x1) or point[1] in (y0,y1):
			boundary_idx.add(idx)
	return boundary_idx

def part2grid():
	grid={}
	for x in range(x0,x1+1):
		for y in range(y0,y1+1):
			distances=[manhattan_distance((x,y), point) for point in points.values()]
			grid[(x,y)]=sum(distances)
	return grid

def print_grid_part1(grid):
	#print grid
	line=''
	for y in range(y0,y1+1):
		for x in range(x0,x1+1):
			if grid[(x,y)] is not None:
				num=grid[(x,y)]+97
				if (x,y) in points.values():
					num=grid[(x,y)]+65
				line+=chr(num)
			else:
				line+='.'
		print(line)
		line=''


def print_grid_part2(grid):
	line=''
	for y in range(y0,y1+1):
		for x in range(x0,x1+1):
			if (x,y) in grid:	
				if grid[(x,y)]<32:
					if (x,y) in points.values():
						for i in points:
							if (x,y)==points[i]:
								line+=chr(i+65)
					else:
						line+='#'
				else:
					line+='?'
			else:
				if (x,y) in points.values():
					for i in points:
						if (x,y)==points[i]:
							line+=chr(i+65)
				else:
					line+='.'
		print(line)
		line=''



grid1=part1grid()
boundary_idx=get_boundary_idx(grid1)
area=collections.Counter()
for point,idx in grid1.items():
	if idx not in boundary_idx:
		area[idx]+=1
count=0
grid2=part2grid()
for point,total in grid2.items():
	if total<10000:
		count+=1



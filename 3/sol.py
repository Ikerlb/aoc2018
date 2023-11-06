strs=list(map(lambda x:x.replace(" ","").replace("@",":")[1:],open("input.txt","r").read().split("\n")))
side=1000
grid=[[0 for x in range(side)] for y in range(side)]

def part1():
	for st in map(lambda x:x.split(":")[1:],strs):
		pad=list(map(int,st[0].split(",")))
		wh=list(map(int,st[1].split("x")))
		for i in range(wh[0]):
 			for j in range(wh[1]):
 				grid[pad[0]+i][pad[1]+j]+=1
	s=0
	for i in range(side):
		s+=sum([1 for x in grid[i] if x>1])
	return s		

#FIRST TRY! WRONG!
# def part2():
# 	seen=set()
# 	for st in map(lambda x:x.split(":"),strs):
# 		iden=int(st[0])
# 		pad=list(map(int,st[1].split(",")))
# 		wh=list(map(int,st[2].split("x")))
# 		seen.add(iden)
# 		for i in range(wh[0]):
#  			for j in range(wh[1]):
#  				if grid[pad[1]+j][pad[0]+i] in seen:
# 	 					seen.remove(grid[pad[1]+j][pad[0]+i])
# 	 					if iden in seen:
# 	 						seen.remove(iden)
#  				grid[pad[1]+j][pad[0]+i]=iden
# 	print(seen)

#looks inefficient but mehhhh
def part2():
	overlaps=set()
	for st in map(lambda x:x.split(":"),strs):
		iden=int(st[0])
		pad=list(map(int,st[1].split(",")))
		wh=list(map(int,st[2].split("x")))
		for i in range(wh[0]):
			for j in range(wh[1]):
				if grid[pad[1]+j][pad[0]+i]!=0:
					 overlaps.add(iden)
					 overlaps.add(grid[pad[1]+j][pad[0]+i])
				grid[pad[1]+j][pad[0]+i]=iden
	for i in range(1,1350):
		if not(i in overlaps):
			print(i)

def print_grid():
	st=[]
	for i in range(side):
		st.append(''.join(list(map(lambda x: '.' if x==0 else str(x),grid[i]))))
	print("\n".join(st))


# def part1():

# def part2():
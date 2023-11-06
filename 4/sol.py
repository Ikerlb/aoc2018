import functools

st=list(map(lambda x:x.replace("[","").split("] "),open("input.txt","r").read().split("\n")))
timeline=list(map(lambda x:[x[0],x[1].replace(" begins shift","").replace("Guard #","")],sorted(st,key=lambda x:x[0])))
current=0
count={}
for i in range(len(timeline)):
	if timeline[i][1].isdigit():
		current=int(timeline[i][1])
	elif timeline[i][1].count('wakes')>0:
		if not(current in count):
			count[current]=[0]*60
			for j in range(int(timeline[i-1][0].split(':')[1]),int(timeline[i][0].split(':')[1])):
				count[current][j]=1
		else:
			for j in range(int(timeline[i-1][0].split(':')[1]),int(timeline[i][0].split(':')[1])):
				count[current][j]+=1
	
def part1():
	maxid=functools.reduce(lambda x,y:x if sum(count[x])>sum(count[y]) else y,count)
	#return count
	return (maxid,functools.reduce(lambda x,y:x if count[maxid][x]>count[maxid][y] else y,range(len(count[maxid]))))

def part2():
	maxid=functools.reduce(lambda x,y:x if max(count[x])>max(count[y]) else y,count)
	return (maxid,functools.reduce(lambda x,y:x if count[maxid][x]>count[maxid][y] else y,range(len(count[maxid]))))


strs=open('input.txt','r').read().split()

def twos_threes(st):
	d={}
	for i in st:
		if i in d:
			val=d[i]
			d[i]=val+1
		else:
			d[i]=1
	threes=0
	twos=0
	for i in d:
		if d[i]==3:
			threes=1
		elif d[i]==2:
			twos=1
		if threes+twos==2:
			return (1,1)
	return (twos,threes)

def part1():
	z=list(zip(*map(twos_threes,strs)))
	return sum(z[0])*sum(z[1])

def differs_by_one(s1,s2):
	return len(list(filter(lambda x:x[0]!=x[1],list(zip(*[s1,s2])))))<=1

def part2():
	candidates=[]
	for i in range(len(strs)):
		for j in range(i+1,len(strs)):
			if differs_by_one(strs[i],strs[j]):
				candidates.append((i,j))


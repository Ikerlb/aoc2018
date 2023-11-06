import functools

og=open("input.txt","r").read()

def reduce(before):
	i=0
	res=before
	while i<len(res)-1:
		if abs(ord(res[i])-ord(res[i+1]))==32:
			res=(res[:i]+res[i+2:])
			i-=1
			if i<0:
				i=0
		else:
			i+=1
	return res	

def part1():
	return len(reduce(og))

def part2():
	return min([len(reduce(og.replace(chr(t),'').replace(chr(t+32),''))) for t in range(65,91)])
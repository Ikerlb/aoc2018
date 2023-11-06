import functools

changes=list(map(int,open('input.txt','r').read().split()))

def part1():
	return functools.reduce(lambda x,y:x+y,changes)

def part2():
	s={0}
	freq=0
	i=0
	while True:
		freq+=changes[i%len(changes)]
		if freq in s:
			return freq
		s.add(freq)
		i+=1
	return None

print(part1())
print(part2())
nums=list(map(int,open('input.txt','r').read().split(' ')))

def parse(it):
    # read the number of children and number of metadata
    num_children, num_metadata = next(it), next(it)
    # recursively parse children nodes
    children = [parse(it) for _ in range(num_children)]
    # read the metadata
    metadata = [next(it) for _ in range(num_metadata)]
    return (metadata, children)

root=parse(iter(nums))

def part1(tup):
	s=sum(tup[0])
	for child in tup[1]:
		s+=part1(child)
	return s

def part2(tup):
	if not tup[1]:
		return sum(tup[0])
	s=0
	for md in tup[0]:
		if md in range(1,len(tup[1])+1):
			s+=part2(tup[1][md-1])
	return s

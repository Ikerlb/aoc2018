txt=(open('input.txt','r').read()).split('\n')
st=txt[0].replace('initial state: ','')
initial_state={i for i,_ in enumerate(st) if st[i]=='#'}

rules=list(map(lambda x:x.split(' => '),txt[2:]))
rules={rule[0]:rule[1] for rule in rules}

def next_gen(state):
	#only way it gets distributed beyond initial state is if:
	# ..***
	# nneei
	new=state.copy()
	for i in range(min(state)-2,max(state)+3):
		st=''
		#create string
		for c in range(i-2,i+3):
			if c in state:
				st+='#'
			else:
				st+='.'
		#check if string is in rules dict.
		if st in rules:
			if rules[st]=='.':
				new.discard(i)
			else:
				new.add(i)
	return new

def stringify(state):
	st=''
	for i in range(min(state),max(state)+1):
		if i in state:
			st+='#'
		else:
			st+='.'
	return st


def part1():
	state=initial_state
	for _ in range(20):
		state=next_gen(state)
	print(state)
	print(sum(state))

def part2():
	prev=0
	summ=0
	state=initial_state
	for i in range(1000):
		prev=summ
		state=next_gen(state)
		summ=sum(state)
	print(summ+((summ-prev)*(50000000000-(i+1))))




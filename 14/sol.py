after=int(open('input.txt','r').read())

#recipies board
recipes=['3','7']
#elves current recipes
current=[0,1]

def create():
	recipes.extend(list(str(int(recipes[current[0]])+int(recipes[current[1]]))))

def update():
	current[0]=((1+current[0]+int(recipes[current[0]]))%len(recipes))
	current[1]=((1+current[1]+int(recipes[current[1]]))%len(recipes))

def part1(after):
	while(len(recipes)<after+11):
		create()
		update()
	print(''.join(recipes[after:after+10]))

def part2():
	while(True):
		create()
		update()
		if ''.join(recipes).find('110201')!=-1:
			print(''.join(recipes).find('110201'))
			break

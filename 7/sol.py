#FIX THIS GOD DAMMNED MESS!

st=map(lambda x:x.split(' must be finished before step '),open("input.txt","r").read().split("\n"))
filtered=[[x[0].replace('Step ',''),x[1].replace(' can begin.','')] for x in st]

depends_on=lambda char: {i[0] for i in filtered if char in i[1]}
result=[]

chars={}
total=set()
for l in filtered:
	total.add(l[0])
	if l[0] in chars:
		chars[l[0]].add(l[1])
		total.add(l[1])
	else:
		chars[l[0]]={l[1]}
		total.add(l[1])

# #where to start? get start ones!
not_available=set()
for c in chars:
	not_available|=chars[c]

stack=sorted(total-not_available)

def first_poppable_index():
	for i in range(len(stack)):
		if len(depends_on(stack[i])-set(result))==0:
			return i
	return -1

while stack:
	idx=first_poppable_index()
	popped=stack.pop(idx)
	if popped in chars:
		result.append(popped)
		stack=sorted(chars[popped]|set(stack))

last={i[0] for i in chars}

for i in sorted(total-last):
	result.append(i)

result=[]

num=5
count=[0]*num
worker=['']*num
t=0

stack=sorted(total-not_available)

while stack or sum(count)!=0:
	to_pop=[]
	#for each free character
	for c in stack:
		#check if character is available
		if len(depends_on(c)-set(result))==0:
			#find, if there is, available worker
			for i in range(num):
				if count[i]==0:
					#ord(c)-64+60
					count[i]=ord(c)-4
					worker[i]=c
					to_pop.append(c)
					#break loop
					break
	stack=[c for c in stack if c not in to_pop]
	#check if any worker has value 1! as it is about to be done, free and add its dependees to stack
	for i in range(num):
		if count[i]==1:
			result.append(worker[i])
			if worker[i] in chars:
				stack=sorted(chars[worker[i]]|set(stack))
			count[i]-=1
		elif count[i]>1:
			count[i]-=1
	t+=1
	print(count,worker,t,stack,result)






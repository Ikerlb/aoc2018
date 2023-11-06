#todo summed area!! no clue how though

serial=int(open('input.txt','r').read())
grid=[[0 for _ in range(301)] for _ in range(301)]


def power_level(x,y):
	rid=x+10
	pl=rid*y
	pl+=serial
	pl*=rid
	return (((pl%1000)-(pl%100))//100)-5

#populate grid
for y in range(1,301):
	for x in range(1,301):
		grid[x][y]=power_level(x,y)

#convolute
def largest_of_size(k):
	values={}
	for x in range(1,301-k):
		for y in range(1,301-k):
			s=0
			for i in range(x,x+k):
				for j in range(y,y+k):
					s=s+grid[i][j]
			values[(x,y)]=s

	m=0
	midx=-1
	for c in values:
		if values[c]>m:
			midx=c
			m=values[c]

	return (midx,m)

for i in range(2,100):
	m=0
	midx=-1
	lidx,lk=largest_of_size(i)
	if lk>m:
		m=lk
		midx=lidx
		print('for size',i,'largest total power is',lk,'and result is',lidx)
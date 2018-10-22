import itertools

def fuck(fight, team):
	win = fight[team].count(1)
	lose = fight[team].count(-1)
	undicide = [index for index, value in enumerate(fight[team]) if value == 0]
	if (len(fight) - 1)//2 - win < 0 or (len(fight) - 1)//2 - lose < 0:
		return 0
	aller = list(itertools.combinations(undicide,  (len(fight) - 1)//2 - win))
	result = 0
	for i in aller:
		newfight = [row[:] for row in fight]
		ok = True
		for j in undicide:
			if j in i:
				newfight[team][j] = 1
				newfight[j][team] = -1
			else:
				newfight[team][j] = -1
				newfight[j][team] = 1
			if (newfight[j].count(1) > (len(fight) - 1)//2) or (newfight[j].count(-1) > (len(fight) - 1)//2):
				ok = False
				break
		if ok == True:
			if team != 0:
				result += fuck(newfight, team - 1)
			else:
				result += 1
		
	return result
			

while True:
	a = int(input())
	if a == 0:
		break
	else:
		b = int(input())
		fight = [[0 for i in range(a)] for j in range(a)]
		for i in range(a):
			fight[i][i] = 'x'
		for i in range(b):
			temp = input().split()
			temp = [int(j) for j in temp]
			fight[temp[0] - 1][temp[1] - 1] = 1
			fight[temp[1] - 1][temp[0] - 1] = -1
		
		print (fuck(fight, a - 1))
				
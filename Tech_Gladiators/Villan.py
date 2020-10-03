
players=[]
villans=[]

def getPlayer(unit):
    playercopy=players.copy()
    while len(playercopy)>0:
        temp=min(playercopy)
        if temp>=unit:
            return temp
        else:
            playercopy.remove(temp)
    return None


n=int(input())

for i in range(n):
	villans=[int(x) for x in input().split()]
	players=[int(x) for x in input().split()]
	not_ass=villans.copy()
	answer={}

	if sum(players)<sum(villans):
            print("LOSE")
            continue

	for cvillan in villans:
		player_of_villan=getPlayer(cvillan)
		if player_of_villan:
			answer[player_of_villan]=cvillan
			players.remove(player_of_villan)
			not_ass.remove(cvillan)

	if not_ass:
		print("LOSE")
	else:
		print("WIN")

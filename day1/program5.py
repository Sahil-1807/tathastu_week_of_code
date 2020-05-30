runs=[eval(x) for x in input("run in 60 balls for 3 players seperated by comma").split(",")]
print(runs)
st_rate=[x*100/60 for x in runs]
print("strike rate of the players is",st_rate )
runs2=[x*2 for x in runs]
print("if players played 60 balls more then their score is ",runs2)
sixes=[int(x/6) for x in runs]
print("max number of sixes by players in 60 balls",sixes)

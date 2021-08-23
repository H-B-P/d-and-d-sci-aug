import numpy as np
import pandas as pd
import random
import math

def roll_dX(X):
 return random.choice(list(range(X)))+1

def roll_NdX(N,X):
 op=0
 for i in range(N):
  op+=roll_dX(X)
 return op





def solar_func_1(i):
 return [0,-2,-2,-2,-7,-7,-7,-7,-7,-7,-2,-2,-2,0,0,1,2,3,6,7,8,8,7,6,3,2,1,0][i%28]

def solar_func_2(i):
 return [-3,3,4,4,4,3,-3,-6,-6][i%9]

def supernovae(i):
 if i>60 and i<63:
  return 7
 if i>200 and i<205:
  return 12
 if i>262 and i<269:
  return 9
 if i>365 and i<372:
  return 24
 return 0

def get_next_solar(i):
 return 40+solar_func_1(i)+solar_func_2(i)+supernovae(i)+roll_dX(2)-roll_dX(2)

def get_next_lunar(i, solars):
 if len(solars)<15:
  return 0
 return 75 - solars[-15]

def get_next_flame(i, flames):
 if len(flames)==0:
  return 10
 return flames[-1]-flames[-1]/4+min(roll_dX(20), roll_dX(20), roll_dX(20))

def get_next_ash(i, flames):
 if len(flames)<2:
  return 0
 return flames[-2]/4

def get_next_world(i):
 return 68 + [-10,-9,-7,-4,-1,0,0,1,4,7,9,10,9,7,4,1,0,0,-1,-4,-7,-9][i%22] + roll_dX(4) - roll_dX(4)

def get_next_earth_and_ocean(i):
 world = get_next_world(i)
 division = 15+roll_dX(80)
 earth = world*division/100
 ocean = world-earth
 return earth, ocean

def get_next_breeze(i):
 X = [6,8,8,6,4,2,4][i%7]
 return 13 + roll_dX(X) - roll_dX(X)

def doom_roll(i):
 if i==34:
  return 8
 if i==91:
  return -3
 if i==181:
  return 11
 if i==249:
  return 12
 return roll_dX(6)

def get_next_doom(i):
 return 24+[3,5,7,-7,-5,-3,-1,1][i%8] + doom_roll(i)

def get_next_void(i):
 return 24 + roll_dX(8)-roll_dX(8)

def get_next_spite(i):
 tot = 0
 if (i%4)==1:
  tot+=13
 if (i%5)==2:
  tot+=7
 if (i%7)==5:
  tot+=18
 if (i%14)==3:
  tot+=6
 return tot

dayList=[]
solarList = []
lunarList = []
flameList = []
ashList = []
earthList = []
oceanList = []
breezeList = []
doomList = []
voidList = []
spiteList = []

random.seed(0)

for i in range(-20, 375):
 dayList.append(i)
 solarList.append(get_next_solar(i))
 lunarList.append(get_next_lunar(i, solarList))
 flameList.append(get_next_flame(i,flameList))
 ashList.append(get_next_ash(i,flameList))
 earth, ocean = get_next_earth_and_ocean(i)
 earthList.append(earth)
 oceanList.append(ocean)
 breezeList.append(get_next_breeze(i))
 doomList.append(get_next_doom(i))
 voidList.append(get_next_void(i))
 spiteList.append(get_next_spite(i))

dictForDf = {"Day":dayList,"Solar":solarList, "Lunar":lunarList, "Flame":flameList, "Ash":ashList, "Earth":earthList, "Ocean":oceanList, "Breeze":breezeList, "Doom":doomList, "Void":voidList, "Spite":spiteList}

df = pd.DataFrame(dictForDf)

df = df[['Day','Solar','Lunar','Ocean','Breeze','Flame','Ash','Earth','Void','Doom','Spite']]

df = df[df['Day']>0]

print(df)

df.to_csv("dset.csv")




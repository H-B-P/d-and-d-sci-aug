
def roll_dX(X):
 op = {}
 for i in range(X):
  op[i+1] = 1.0/X
 return op

def app(dyct,key,val):
 if key in dyct:
  dyct[key]+=val
 else:
  dyct[key]=val
 return dyct

def p_add(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey+bkey, a[akey]*b[bkey])
 return op

def p_subtract(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey-bkey, a[akey]*b[bkey])
 return op

def p_multiply(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey*bkey, a[akey]*b[bkey])
 return op

def p_divide(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey/bkey, a[akey]*b[bkey])
 return op

def p_min(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, min(akey,bkey), a[akey]*b[bkey])
 return op

def amt_greater(a,b): #what is the probability that a>b?
 greater = 0
 for akey in a:
  for bkey in b:
   if akey>bkey:
    greater += a[akey]*b[bkey]
 return greater

def p_minusdivide(a,b): #special thing for Flame
 op={}
 for akey in a:
  for bkey in b:
   op = app(op, akey-akey/bkey, a[akey]*b[bkey])
 return op

def p_minusdivide_II(a,b): #special thing for Ocean
 op={}
 for akey in a:
  for bkey in b:
   op = app(op, akey - akey*bkey/100, a[akey]*b[bkey])
 return op

Solar = p_subtract(p_add({45:1.0}, roll_dX(2)), roll_dX(2))
Lunar = {16:1.0}

World = p_subtract(p_add({77:1.0}, roll_dX(4)), roll_dX(4))
split = p_add({15:1.0},roll_dX(80))
print(split)
Earth = p_divide(p_multiply(World, split), {100:1.0})
Ocean = p_minusdivide_II(World, split)
print(World)
print(Earth)
print(Ocean)

Breeze = p_subtract(p_add({13:1.0}, roll_dX(4)), roll_dX(4))

Flame = {30:1.0} #day 374
Flame_addon = p_min(roll_dX(20), roll_dX(20))
Flame = p_add(p_minusdivide(Flame, {4:1.0}),Flame_addon) #day 375
Flame = p_add(p_minusdivide(Flame, {4:1.0}),Flame_addon) #day 376
Flame = p_add(p_minusdivide(Flame, {4:1.0}),Flame_addon) #day 377
Flame = p_add(p_minusdivide(Flame, {4:1.0}),Flame_addon) #day 378
Flame = p_add(p_minusdivide(Flame, {4:1.0}),Flame_addon) #day 379
Flame = p_add(p_minusdivide(Flame, {4:1.0}),Flame_addon) #day 380
Flame = p_add(p_minusdivide(Flame, {4:1.0}),Flame_addon) #day 381
Flame = p_add(p_minusdivide(Flame, {4:1.0}),Flame_addon) #day 382
Flame = p_add(p_minusdivide(Flame, {4:1.0}),Flame_addon) #day 383
FlameAndAsh = p_add(Flame, Flame_addon)
Ash = p_divide(Flame, {4:1.0})
Flame = p_add(p_minusdivide(Flame, {4:1.0}),Flame_addon)

for thing in Flame:
 print(thing)
for thing in Flame:
 print(Flame[thing])

for thing in Ash:
 print(thing)
for thing in Ash:
 print(Ash[thing])

Void = p_subtract(p_add({24:1.0}, roll_dX(8)), roll_dX(8))
Doom = p_add({27:0.99, 99:0.01}, roll_dX(6))
Spite = {0:1.0}

manas = {"Solar":Solar, "Lunar":Lunar, "Ocean":Ocean, "Breeze":Breeze, "Flame":Flame, "Ash":Ash, "Earth":Earth, "Void":Void, "Doom":Doom, "Spite":Spite}

badmanas = ["Void", "Doom", "Spite"]

outcomes={}

for mana1 in manas:
 outcomes[mana1]={}
 for mana2 in manas:
  outcomes[mana1][mana2] = {"Demon":0, "Failure":0, "Success":0}
  if (mana1=="Flame" and mana2=="Ash") or (mana1=="Ash" and mana2=="Flame"):
   outcomes[mana1][mana2]["Success"] = amt_greater(FlameAndAsh,{69:1.0})
   outcomes[mana1][mana2]["Failure"] = 1.0 - outcomes[mana1][mana2]["Success"]
  elif (mana1=="Earth" and mana2=="Ocean") or (mana1=="Ocean" and mana2=="Earth"):
   outcomes[mana1][mana2]["Success"] = amt_greater(World,{69:1.0})
   outcomes[mana1][mana2]["Failure"] = 1.0 - outcomes[mana1][mana2]["Success"]
  elif mana1!=mana2:
   for key1 in manas[mana1]:
    for key2 in manas[mana2]:
     if (((mana1 in badmanas) and (key1>key2)) or ((mana2 in badmanas) and (key1<key2))):
      outcomes[mana1][mana2]["Demon"] += manas[mana1][key1]*manas[mana2][key2]
     else:
      if (key1+key2)>69: #nice
       outcomes[mana1][mana2]["Success"] += manas[mana1][key1]*manas[mana2][key2]
      else:
       outcomes[mana1][mana2]["Failure"] += manas[mana1][key1]*manas[mana2][key2]

print(outcomes)

prettyOutcomes={}

for mana1 in manas:
 for mana2 in manas:
  if mana1!=mana2:
   prettyOutcomes[mana1+" "+mana2] = {}
   prettyOutcomes[mana1+" "+mana2]["Demon"] = str(round(outcomes[mana1][mana2]["Demon"]*100,2))+"%"
   prettyOutcomes[mana1+" "+mana2]["Failure"] = str(round(outcomes[mana1][mana2]["Failure"]*100,2))+"%"
   prettyOutcomes[mana1+" "+mana2]["Success"] = str(round(outcomes[mana1][mana2]["Success"]*100,2))+"%"
   print(mana1,mana2,prettyOutcomes[mana1+" "+mana2])

print(prettyOutcomes)

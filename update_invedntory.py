curInv = [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]]
newInv = [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]
 
def invent(curInv,newInv) :
  for i in newInv:
    was_element_found = False
    for j in curInv:
      if(j[1]==i[1]):
        newInv.append([j[0] + i[0], j[1]])
        curInv.remove(j)
        was_element_found = True
    if not was_element_found:
        curInv.append(i)
  curInv.sort(key=lambda x: x[1])
  print (curInv)
  return
 
invent(curInv,newInv)

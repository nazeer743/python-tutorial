weight = int(input("weight: "))
unit = input("(K)kgs or (L)lbs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in lbs: " +str(converted))
else:
    converted= weight* 0.45
    print("weight in kg: " +str( converted))
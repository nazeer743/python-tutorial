weight = input(weight: )
unit = input("(K)kgs or (L)lbs")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in lbs: " + converted)
else:
    converted= weight* 0.45
    print("weight in kg: " + converted)
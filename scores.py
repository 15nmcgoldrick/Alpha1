total=int(input("Please enter the total marks you can get"))

yourmarks=int(input("Please enter how many marks you got"))

answer=(yourmarks/total*100)

print(answer)


if answer < 10:
    print("G")

elif answer < 25 > 10:
    print("F")

elif answer < 40 > 25:
    print("E")

elif answer < 55 > 40:
    print("D")

elif answer < 70 > 55:
    print("C")

elif answer < 85 > 70:
    print("B")

elif answer > 85:
    print("A")

else:
    print("ERROR")





print("A pass is D or above") 

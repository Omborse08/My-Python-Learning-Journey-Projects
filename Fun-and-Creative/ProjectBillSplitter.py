boy1 = int(input("boy1 how much you pay? "))
boy2 = int(input("boy2 how much you pay? "))
boy3 = int(input("boy3 how much you pay? "))

total_bill = boy1 + boy2 + boy3
average = total_bill / 3

boyA = boy1 - average 
boyB = boy2 - average 
boyC = boy3 - average 

print(total_bill)
print(average)



if boy1 == average:
    print("settled")
elif boy1 < average:
    print("Boy1 Has to Give More:",abs(boyA))
elif boy1 > average:
    print("Boy1 have to return his money",abs(boyA))


if boy2 == average:
    print("settled")
elif boy2 < average:
    print("Boy2 Has to Give More:",abs(boyB))
elif boy2 > average:
    print("Boy2 have to return his money",abs(boyB))

if boy3 == average:
    print("settled")
elif boy3 < average:
    print("Boy3 Has to Give More:",abs(boyC))
elif boy3 > average:
    print("Boy3 have to return his money",abs(boyC))



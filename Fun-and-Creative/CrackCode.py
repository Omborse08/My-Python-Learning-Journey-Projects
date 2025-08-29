free = input("Enter Your Message: ").split(" ")
coding = input("Enter 1 or 0 To Decode or Encode: ")
coding = True if coding == "1" else False

if (coding):
    nworlds = []
    for work in free:
        if len(work) >= 3:
            r1 = "hgc"
            r2 = "tsd"
            new_cd = r1+ work[1:] + work[0] + r2
            nworlds.append(new_cd)
        else:
            nworlds.append(work[::-1])
    print(" ".join(nworlds))


else:
    nworlds = []
    for work in free:
        if len(work) >= 3:
            new_cf = work[3:-3]
            new_cf = new_cf[-1] + new_cf[:-1]
            nworlds.append(new_cf)
        else:
            nworlds.append(work[::-1])
    print(" ".join(nworlds))
def flames(l):
    if l == 1:
        print("Just be a Friend")
    elif l == 2:
        print("Perfect match for a Love relationship")
    elif l == 3:
        print("That person has Affection for you")
    elif l == 4:
        print("Congratulations, you are a perfect couple to get Married")
    elif l == 5:
        print("That person is your Enemy")
    elif l == 6:
        print("This person is your Sibling")
    else:
        print("None")

name = input("Enter your Name: ").lower().replace(" ", "")
pname = input("Enter your Partner's Name: ").lower().replace(" ", "")
res = set(name).symmetric_difference(pname)
l = len(res)

if l < 7:
    flames(l)
else:
    l = l % 6
    flames(l)


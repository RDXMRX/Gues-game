num = 20
while(True):
    inp = int(input("Gues the number in program:"))
    if inp>20:
        print("Enter lesser than")
        continue
    elif inp<20:
        print("Enter larger than")
        continue
    if inp==20:
        print("You are won")
        break
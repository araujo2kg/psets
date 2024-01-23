def shout(shout1="GODDAMIT!"):
    print(shout1)

shout1 = input("Shout here your indignation!: ").lower()

if shout1:
        shout(shout1)
else:
        shout()



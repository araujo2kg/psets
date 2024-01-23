def main():
    time = input("What time is it? ")
    time = convert(time)

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")
    else:
        print("Not meal time")
        exit() #not really necessary, but does not make a difference

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time = float(hours) + float(minutes/60.0) # minutes(int) / 60.0 does an equivalent number conversion
    return time                               # similar in how you can /100 to use a percent value

if __name__ == "__main__":
   main()


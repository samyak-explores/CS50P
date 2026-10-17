def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        return None



def convert(time):
    h,m = time.split(":")    #hr and min
    h = int(h)
    m = int(m)

    f = m/60   #fraction
    time = float(h + f)

    return time


if __name__ == "__main__":
    main()

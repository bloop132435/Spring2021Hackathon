# THIS FILE IS ONLY A RAW ALGORITHM
# INPUT & OUTPUT METHOD HAS TO BE CHANGED IN ACTUAL IMPLENMENTATION

# this algorithm determines the possible meeting times for a group of people
# based on people adding their possible time sections with their availability

# availability scale: 0 - 10 (default: 0, meaning not available at the time)
# current time scale (need to be changed to actual asc time later): 0 - 30
# input time with format "<start> <end>" eg."2 6", meaning time section 2 - 6

# -----------------------------------------------------------------

# n is the number of people
n = int(input("please enter the number of people: "))

# store their names
names = []
for i in range(n):
    names.append(input("please enter the person " + str(i + 1) + "'s name: "))

# get their available time & store them
freeTimes = []
for i in range(n):
    freeTimes.append([])

while True:
    option = input("enter the option: ")

    if (option == "done"):
        break;

    elif (option.isdigit()):
        index = int(option)

        # input available time & availability
        if ((index >= 0) and (index < n)):
            time = input("enter the time section: ").split()
            availability = int(input("enter the availability: "))
            freeTimes[index].append((int(time[0]), int(time[1]), availability))


# THIS FILE IS ONLY A RAW ALGORITHM
# INPUT & OUTPUT METHOD HAS TO BE CHANGED IN ACTUAL IMPLENMENTATION

# this algorithm determines the possible meeting times for a group of people
# based on people adding their possible time sections with their availability

# availability scale: 0 - 10 (default: 0, meaning not available at the time)
# time scale: 0 - 48
# input time with format "<start> <end>" eg."2 6", meaning time section 2 - 6

# -----------------------------------------------------------------

# n is the number of people
n = int(input("please enter the number of people: "))

"""
# store their names
names = []
for i in range(n):
    names.append(input("please enter the person " + str(i) + "'s name: "))
"""

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

# all possible overlapped available times with a number of people or greater
def allMeetings(timeList, num):
    ''' allMeetings(times, num) -> (())
    timeList: free time list
    num: number of people '''

    possiMeetings = []

    timeBlocks = []

    for i in range(48):
        timeBlocks.append(0)

    for p in timeList:
        for t in p:
            for i in range(t[0], t[1]):
                timeBlocks[i] += 1

    b = False
    start = -1
    end = -1
    for i in range(len(timeBlocks)):
        if (timeBlocks[i] >= num):
            if (not b):
                start = i
                b = True

        else:
            if (b):
                end = i
                b = False
                possiMeetings.append((start, end))

    if (not(start == -1) and (end == -1)):
        possiMeetings.append((start, 48))
        
    return tuple(possiMeetings)

# max availability of all meetings with at least 2 people
def maxAviMeetings(timeList):

    ''' allMeetings(times) -> (())
    timeList: free time list'''

    possiMeetings = []

    timeBlocks = []
    avai = []

    for i in range(48):
        timeBlocks.append(0)
        avai.append(0)

    for p in timeList:
        for t in p:
            for i in range(t[0], t[1]):
                timeBlocks[i] += 1
                avai[i] += t[2]

    b = False
    start = -1
    end = -1
    maxAvai = max(avai)
    for i in range(len(timeBlocks)):
        if ((timeBlocks[i] >= 2) and (avai[i] == maxAvai)):
            if (not b):
                start = i
                b = True

        else:
            if (b):
                end = i
                b = False
                possiMeetings.append((start, end))

    if (not(start == -1) and (end == -1)):
        possiMeetings.append((start, 48))
        
    return tuple(possiMeetings

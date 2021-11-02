#Cameron Mitchell
#26/10/21
#Task 10K

size = int(input("How many student are there: "))


name = [""] * size
age = [0] * size
time1 = [0.0] * size
time2 = [0.0] * size
time3 = [0.0] * size
time4 = [0.0] * size
time5 = [0.0] * size
time6 = [0.0] * size
section = [""] * size
averagetime = [0.0] * size
average = 0.0
minmid = 0.0


for index in range(size):
    name[index] = str(input("Please input students name: "))
    age[index] = int(input("Please enter there age: "))

    while age[index] < 12 or age[index] > 18:
        age[index] = int(input("Invalid age please enter age between 12 and 18: "))

    print("Please input times in seconds!")
    time1[index] = float(input("Please input first time : "))
    time2[index] = float(input("Please input second time: "))
    time3[index] = float(input("Please input third time: "))
    time4[index] = float(input("Please input fourth time: "))
    time5[index] = float(input("Please input fith time: "))
    time6[index] = float(input("Please input sixth time: "))


for index in range(size):
    minmid = 0.0
    minmid = minmid + (time1[index] / 60)
    minmid = minmid + (time2[index] / 60)
    minmid = minmid + (time3[index] / 60)
    minmid = minmid + (time4[index] / 60)
    minmid = minmid + (time5[index] / 60)
    minmid = minmid + (time6[index] / 60)
    minmid = minmid / 6
    averagetime[index] = minmid



for index in range(size):

    if averagetime[index] <= 35:
        section[index] = "Experienced"
    elif averagetime[index] <= 60:
        section[index] = "Intermedidiate"
    elif averagetime[index] <= 84:
       section[index] = "Beginner"
    else:
        section[index] = "Not elligable"



for index in range(size):
    print("Name:", name[index])
    print("Age:", age[index])
    print("Average time:", averagetime[index])
    print("Section:", section[index])
    print()










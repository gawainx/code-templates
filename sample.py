import random

trainSrc = open("", "r")
sampleTrain = open("sampleTrain.txt", 'w')
count = 0
while count < 1000:
    for line in trainSrc:
        r = random.randint(0, 100)
        if r % 9 == 0:
            print(line, file=sampleTrain)
            count = count + 1

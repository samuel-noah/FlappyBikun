def writeScore(score):
    file = open('score.txt', 'a')
    file.write('\n'+ str(score))
    file.close()


def maxScore():
    maxScore = 0
    file = open('score.txt', 'r')
    for line in file:
        if int(line) > maxScore:
            maxScore = int(line) 
    file.close()
    return maxScore
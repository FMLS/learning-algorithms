import random
import numpy as np
from matplotlib import pyplot as plt

def getFiveNums(data:list):
    data.sort()
    minimum = data[0]
    length = len(data)
    midpoint = length // 2
    q1 = np.median(data[0:midpoint])

    median = np.median(data)
    if length % 2 == 0:
        q3 = np.median(data[midpoint:])
    else:
        q3 = np.median(data[midpoint + 1:])

    maximum = data[-1]

    return (minimum, q1, median, q3, maximum)
    

def eliminateOutliers(data:list):
    eliminateData = []
    while True:
        minium, q1, median, q3, maximum = getFiveNums(data)
        IRQ = q3 - q1

        maxSubMedian = maximum - median
        medianSubMinium = median - minium
        furthest = maximum if maxSubMedian > medianSubMinium else minium
    
        if abs(furthest - median) > 1.5 * IRQ:
            eliminateData.append(furthest)
            data.remove(furthest)
        else:
            return eliminateData




#data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
#data = [53.0, 55.0, 51.0, 50.0, 60.0, 52.0]
#eliminateOutliers(data)
#print(data)

if __name__ == '__main__':

#100 组数据
    for x in range(1000):
        data = []
        data.append(np.random.randint(8550, 9010))
        data.append(8990)
        data.append(9000)
        data.append(9010)
        data.append(np.random.randint(9000, 9450))
        eliminateData = eliminateOutliers(data)

        for e in eliminateData:
            plt.plot(x, e, 'or')
            plt.annotate(f'{(e - 9000) / 9000 * 100:.2f}%', (x, e))


        #for y in data:
        #    plt.plot(x, y, 'og')

        # 剔除数据后的平均值
        plt.plot(x, np.mean(data), 'og')
        


    plt.title("IRQ")
    plt.show()
    
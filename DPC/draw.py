import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as color
from itertools import cycle, islice

def filterColor():
    result = []
    for index,value in  enumerate(color._colors_full_map.values()):
        if(index % 15 == 1):
            result.append(value)
    return result

def draw(y_pred, dataSet, name):
    colorArr = np.array(list(islice(cycle(filterColor()),int(max(y_pred) - min(y_pred) + 1))))
    color_y = colorArr[y_pred]
    for begin in range(len(color_y)):
        if y_pred[begin] == -1:
            color_y[begin] = '#555555'

    plt.clf()
    plt.title(name, size = 18)

    plt.scatter(dataSet[:, 0], dataSet[:, 1], marker='.', color = color_y)
    plt.xticks([])
    plt.yticks([])

    plt.savefig('result/' + name + '.png', facecolor='white', edgecolor='none')
    #plt.show()
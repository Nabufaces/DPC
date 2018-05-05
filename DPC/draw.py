import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle, islice

def draw(y_pred, dataSet, name):

    colors = np.array(list(islice(cycle(['r', 'y', 'g', 'b', 'c', 'm', 'k', 'darkviolet', 'lightpink',
                                         'darkorange', 'gold', 'mediumspringgreen']),int(max(y_pred) + 1))))
    plt.clf()

    plt.title(name, size = 18)

    plt.scatter(dataSet[:, 0], dataSet[:, 1], marker='.', color = colors[y_pred])

    plt.xticks(())
    plt.yticks(())

    plt.savefig('result/' + name + '.png', facecolor='white', edgecolor='none')
    plt.show()
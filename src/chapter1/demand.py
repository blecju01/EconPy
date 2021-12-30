import matplotlib.pyplot as plt
import numpy as np

def plotDemand(slope, intercept, x_range):
    # Determine demand curve relationship
    # Return graphic using matplotlib & numpy
    x = np.linspace(x_range[0],x_range[1],100)
    y = 2*x+1
    plt.plot(x, y, '-r', label='y=2x+1')
    plt.title('Graph of y=2x+1')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


def supply(equation):
    # Parse equation
    # Determine supply curve relationship
    # Return graphic using matplotlib & numpy
    pass

# plotDemand(4.5, -1, [0,0])
# plotDemand("Hello", -1, [0,0])




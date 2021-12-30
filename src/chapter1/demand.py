import matplotlib.pyplot as plt
import numpy as np

def plotDemand(slope, intercept, x_range):
    # Determine demand curve relationship
    # Return graphic using matplotlib & numpy
    #error handling
    if type(slope) is not int and type(slope) != float:
        raise TypeError("ERROR: Slope must be an integer or float value!")
    if type(intercept) is not int and type(intercept) != float:
        raise TypeError("ERROR: Intercept must be an integer or float value!")
    if len(x_range) != 2:
        raise Exception("ERROR: You can only use two numbers to define the bounds of a range!") 
    if x_range[0] > x_range[1]:
        raise Exception("ERROR: First number in the range must be smaller than the second!") 
    x = np.linspace(x_range[0],x_range[1],100)
    y = slope*x+intercept
    plt.plot(x, y, '-r', label='Q={}P+{}'.format(slope, intercept))
    plt.title('Graph of Q={}P+{}'.format(slope,intercept))
    plt.xlabel('Quantity Demanded', color='#1C2833')
    plt.ylabel('Price', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def plotSupply(slope, intercept, x_range):
    # Parse equation
    # Determine supply curve relationship
    # Return graphic using matplotlib & numpy
    if type(slope) is not int and type(slope) != float:
        raise TypeError("ERROR: Slope must be an integer or float value!")
    if type(intercept) is not int and type(intercept) != float:
        raise TypeError("ERROR: Intercept must be an integer or float value!")
    x = np.linspace(0,intercept,intercept//5)
    y = slope*x+intercept
    plt.plot(x, y, '-r', label='Q={}P+{}'.format(slope, intercept))
    plt.title('Graph of Q={}P+{}'.format(slope,intercept))
    plt.xlabel('Quantity Demanded', color='#1C2833')
    plt.ylabel('Price', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
    pass

# plotDemand(4.5, -1, [0,0])
# plotDemand("Hello", -1, [0,0])

if __name__ == "__main__":
    plotDemand(2.76, 349.33, [0,400])


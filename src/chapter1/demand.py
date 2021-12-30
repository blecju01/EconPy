import matplotlib.pyplot as plt
import numpy as np

def plotDemand(slope, intercept):
    # Determine demand curve relationship
    # Return graphic using matplotlib & numpy
    #error handling
    if type(slope) is not int and type(slope) != float:
        raise TypeError("ERROR: Slope (First Argument) must be an integer or float value!")
    if type(intercept) is not int and type(intercept) != float:
        raise TypeError("ERROR: Base Quanity Demanded (2nd Arugment) must be an integer or float value!")
    if intercept <0:
        raise Exception("ERROR: Quanity Demanded when Price is 0 cannot be less than 0!")
    label = ""
    #label is a variable with an empty string
    if slope<0:
        label = "Q={}-{}P".format(intercept, abs(slope))
    elif slope==0:
        label = "Q={}".format(intercept)
    else:
        label = "Q={}+{}P".format(intercept, slope)
    x = np.linspace(0,intercept,intercept//5)
    y = (intercept - x)/(-1*slope)
    plt.plot(x, y, 'b-', label=label)
    plt.title('Demand Curve {}'.format(label))
    plt.xlabel('Quantity Demanded', color='#1C2833')
    plt.ylabel('Price', color='#1C2833')
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

def plotSupply(slope, intercept):
    # Parse equation
    # Determine supply curve relationship
    # Return graphic using matplotlib & numpy
    if type(slope) is not int and type(slope) != float:
        raise TypeError("ERROR: Slope must be an integer or float value!")
    if type(intercept) is not int and type(intercept) != float:
        raise TypeError("ERROR: Intercept must be an integer or float value!")
    x = np.linspace(0,intercept,intercept//5)
    y = (intercept - x)/(-1*slope)
    plt.plot(x, y, 'b-', label='Q={}P+{}'.format(slope, intercept))
    plt.title('Graph of Q={}P+{}'.format(slope,intercept))
    plt.xlabel('Quantity Demanded', color='#1C2833')
    plt.ylabel('Price', color='#1C2833')
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()
    

# plotDemand(4.5, -1, [0,0])
# plotDemand("Hello", -1, [0,0]) --> Error

if __name__ == "__main__":
    plotDemand(-200, 1000)


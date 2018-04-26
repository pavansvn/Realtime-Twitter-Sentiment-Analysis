import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
from matplotlib.animation import FuncAnimation
import numpy as np

style.use("ggplot")
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    pullData = open("twitter_KA_Polls.txt","r").read()
    lines = pullData.split('\n')
    print()
    xar = []
    yar = []
    x = 0
    y = 0
    
    for line in lines[-300:-1]:
        x += 1
        if line != ' ':
            a = float(line)
            #print(a)
            if a> 0.0:
                y += a
            elif a < 0.0:
                y -= abs(a)
            yar.append(y)
            xar.append(x)
            ax1.clear()
            ax1.plot(xar,yar)


ani = animation.FuncAnimation(fig, animate, interval=10)

plt.show()
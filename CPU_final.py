import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import psutil
import collections

def my_function(i):
    cpu.popleft()
    cpu.append(psutil.cpu_percent())

    ram.popleft()
    ram.append(psutil.virtual_memory().percent)
    
    ax.cla()
    ax1.cla()

    ax.plot(cpu, c='#EC5E29')
    ax.scatter(len(cpu)-1, cpu[-1], c='#EC5E29')
    ax.text(len(cpu)-1, cpu[-1]+2, "{}%".format(cpu[-1]))

    ax.set_xticks(np.arange(-1,10,2))
    ax.set_xticklabels(np.arange(10,-1,-2))
    ax.set_xlabel('Seconds')
    ax.set_title('CPU %\n')
    ax.set_ylim(0,100)

    # remove spines
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # grid
    ax.set_axisbelow(True)
    ax.yaxis.grid(linestyle='dashed', alpha=0.8)

    ax1.plot(ram, c='#1787AD')
    ax1.scatter(len(ram)-1, ram[-1], c='#1787AD')
    ax1.text(len(ram)-1, ram[-1]+2, "{}%".format(ram[-1]))

    ax1.set_xticks(np.arange(-1,10,2))
    ax1.set_xticklabels(np.arange(10,-1,-2))
    ax1.set_xlabel('Seconds')
    ax1.set_title('RAM %\n')
    ax1.set_ylim(0,100)
    # remove spines
    ax1.spines['left'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)

    # grid
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(linestyle='dashed', alpha=0.8)

cpu = collections.deque(np.zeros(10))
ram = collections.deque(np.zeros(10))

fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')

ax = plt.subplot(121)
ax1 = plt.subplot(122)

ax.set_facecolor('#DEDEDE')
ax1.set_facecolor('#DEDEDE')

animation = FuncAnimation(plt.gcf(), my_function, interval=1000)

plt.show()

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

# function to update the data
def my_function(i):
    # get data
    now = datetime.now()
    c_time = now.strftime("%H:%M:%S")
    h, m, s = [int(i) for i in c_time.split(':')]
    if int(h) > 12: h -= 12

    full = 12*60
    total_h = (h * 60) + m
    h = total_h/ full
    full = 60*60
    m = ((m*60) + s)/full
    s = s/60

    plt.cla()
    plt.title(c_time, color='w')
    plt.pie([h, 1-h], startangle=90, counterclock=False, radius=1, colors=['#787878', 'black'])
    plt.pie([m, 1-m], startangle=90, counterclock=False, radius=0.75, colors=['#525252', 'black'])
    plt.pie([s, 1-s], startangle=90, counterclock=False, radius=0.5, colors=['#373737', 'black'])

    my_circle=plt.Circle( (0,0), 0.25, color='black')
    p=plt.gcf()
    p.gca().add_artist(my_circle)

# define and adjust figure
fig = plt.figure(figsize=(6,6), facecolor='black')

# animate
ani = FuncAnimation(fig, my_function, interval=1000)

plt.show()

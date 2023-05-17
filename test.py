import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

duration = 2 # in sec
refreshPeriod = 10 # in ms
fig, ax = plt.subplots()

ax.plot([1,2,3,4,5], [5,5,5,5,5])
line = ax.axvline(0, ls='-', color='r', lw=1, zorder=10)
ax.set_xlim(0,duration)



def animate(i,vl,period):
    t = i*period / 1000
    vl.set_xdata([t,t])
    return vl,


ani = animation.FuncAnimation(fig, animate, frames=int(duration/(refreshPeriod/1000)), fargs=(line,refreshPeriod), interval=refreshPeriod)


# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

ani.save('test.gif')

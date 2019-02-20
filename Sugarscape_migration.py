""" Adpated from Think Complexity 2 edition by Allen Downey (thank you very much).
    Available at https://github.com/AllenDowney/ThinkComplexity2/blob/master/code/chap09.ipynb
    Copyright 2016 Allen Downey, MIT License
    """

import matplotlib.pyplot as plt

from thinkstats2 import Cdf, RandomSeed
import thinkplot
from Sugarscape import Sugarscape, SugarscapeViewer

# # # Migration I
# RandomSeed(17)
#
# env = Sugarscape(50, num_agents=300, starting_box=(20, 20), max_vision=16)
#
# viewer = SugarscapeViewer(env)
# anim = viewer.animate(frames=20, interval=500)
# plt.show()

# # # Migration II


env = Sugarscape(50, num_agents=300, starting_box=(20, 20), max_vision=16)
viewer = SugarscapeViewer(env)

thinkplot.preplot(cols=3)
viewer.draw()

thinkplot.subplot(2)
for i in range(6):
    viewer.step()
viewer.draw()

thinkplot.subplot(3)
for i in range(6):
    viewer.step()
viewer.draw()

thinkplot.tight_layout()
thinkplot.save('chap09-5')


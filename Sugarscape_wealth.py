""" Adpated from Think Complexity 2 edition by Allen Downey (thank you very much).
    Available at https://github.com/AllenDowney/ThinkComplexity2/blob/master/code/chap09.ipynb
    Copyright 2016 Allen Downey, MIT License
    """

import matplotlib.pyplot as plt

from thinkstats2 import Cdf, RandomSeed
import thinkplot
from Sugarscape import Sugarscape, SugarscapeViewer

# env = Sugarscape(50, num_agents=250,
#                  min_lifespan=60, max_lifespan=100,
#                  replace=True)
#
# viewer = SugarscapeViewer(env)
# anim = viewer.animate(frames=100)
# # plt.show()

RandomSeed(17)

env = Sugarscape(50, num_agents=250,
                 min_lifespan=60, max_lifespan=100,
                 replace=True)

cdfs = []
for i in range(5):
    [env.step() for i in range(100)]
    cdf = Cdf(agent.sugar for agent in env.agents)
    cdfs.append(cdf)



thinkplot.preplot(cols=2)
thinkplot.Cdfs(cdfs[:-1], color='gray', alpha=0.3)
thinkplot.Cdf(cdfs[-1])
thinkplot.config(xlabel='Wealth', ylabel='CDF')
thinkplot.bigger_text()

thinkplot.subplot(2)
thinkplot.Cdfs(cdfs[:-1], color='gray', alpha=0.3)
thinkplot.Cdf(cdfs[-1])
thinkplot.config(xlabel='Wealth', ylabel='CDF', xscale='log')
thinkplot.bigger_text()

thinkplot.save('chap09-4')

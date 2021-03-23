import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

n=35
p=0.1
k=np.arange(0,13)
binomial=stats.binom.pmf(k,n,p)
plt.plot(k,binomial,'o-')
plt.title('Binomial: n=%i,p=%.2f' % (n,p),fontsize=15)
plt.xlabel('Number of successes')
plt.ylabel('Probability of successes',fontsize=15)
plt.show()
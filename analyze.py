# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:11:02 2019

@author: Dell
"""

from matplotlib import pyplot as plt

med=[0.00035823917945714315,0.00029993000816603155]
mod=[0.0002666133386663111,0.0005498075336835701]
disp=[4.6643455113484474e-08,5.568675573365476e-08]
name=['эксперимент 1','эксперимент 2']

plt.bar(name,med)
plt.title('Медиана')
plt.show()

plt.bar(name,mod)
plt.title('Мода')
plt.show()

plt.bar(name,disp)
plt.title('Дисперсия')
plt.show()



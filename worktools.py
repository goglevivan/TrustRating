# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:25:45 2019

@author: Dell
"""
import linalgebra_vectors
from matplotlib import pyplot as plt
import random
from collections import Counter

# скалярное произведение

def dot(v,w):
    ''' v_1*w_1+....+v_n*w_n '''
    return sum(v_i*w_i for v_i,w_i in zip(v,w))


def mean (x):
    return sum(x)/len(x)
# cумма квадратов
def sum_of_squares(v):
    return dot(v,v)    
def median(v):
    '''Возвращает ближайшее к середине значение для v '''
    n = len(v)
    sorted_v=sorted(v)
    midpoint = n//2
    
    if n%2 == 1:
        #если нечётное, то вернуть среднее значение
        return sorted_v[midpoint]
    else:
        #если чётное вернуть среднее двух значений
        lo = midpoint - 1
        hi = midpoint
        return(sorted_v[lo]+sorted_v[hi])/2

def mode(x):
    ''' Возвращает список, так как мод может быть больше одной'''
    counts = Counter(x)
    max_count= max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

# вектор отклонения от среднего (центрировать вектор)
def de_mean(x):
    '''Пересчитать x, вычтя из него среднее '''
    x_bar = mean(x)
    return[x_i-x_bar for x_i in x]
#дисперсия
def variance(x):
    ''' Предполагается что вектор x состоит минимум из 2-х элементов'''
    n=len(x)
    deviations = de_mean(x)
    zn = sum_of_squares(deviations)
    return zn/(n-1)
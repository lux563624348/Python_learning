#from math import *
#from matplotlib.pyplot import *
import plot_f as plot_f
import func_py as fp
import numpy as np
import OI as oi
print('Start !')
#a = input('The start parameters.')
#print(a)

t_end = fp.time_end_set()
t_end = oi.f_read('data.dat')
#print(f)

ratio_k_m = 1
t_stepsize = 0.1
stepnumber = int( t_end/t_stepsize)
print(stepnumber)
t = [0]
v = [-1]
x = [1]

for i in range(1, stepnumber, 1):
	t.append(i*t_stepsize)
	x.append(x[i-1]+ v[i-1]*t_stepsize)
	v.append(v[i-1]-x[i]*t_stepsize)

oi.f_write('data_out.dat', t,x)
plot_f.plot_2d(t,x)





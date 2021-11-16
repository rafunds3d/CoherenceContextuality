import numpy as np #for vector analysis in python, not sure I am using it
import math
import cmath
import time #to calculate how much time it took 
from qutip import * #to make quantum calculations, specifically overlap
from random import * #import something to make complex numbers

Violation = 0 #violation parameter starts with zero
count=1
dimension = 2 #test for more dimensions
start_time = time.time()
maxS = 5 #maximum violation of the inequality
#rand_kets are Nx1 Qobj types. 

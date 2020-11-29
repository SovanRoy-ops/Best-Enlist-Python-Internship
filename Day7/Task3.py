# 3.Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run

import random as r
import math
rand = math.floor(r.random()*100)+1
print(rand)
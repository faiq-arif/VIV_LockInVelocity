# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:20:23 2022

@author: Faiq Muhammad Arif
"""

import math

Ce = 15.5
E = 2*10**9
I = 2.13*(10**-4)
Me = 240.2527713 - 12.84848563
Ls = 31.05573348
fn = (Ce/2*math.pi)*math.sqrt((E*I)/(Me*(Ls**4)))
fs = 0
err = 100
i = 0.001
vk = 9.29*(10**-7)
D = 0.324
Uc = 0
S = 0

while err >= 0.01:
    Uc += i
    print(Uc)
    re = (Uc*D)/vk
    if (45 <= re < 1300):
        S = 0.22*(1-22/re)
    elif (1300 <= re < 5*(10**5)):
        S = 0.213-0.0248*(math.log(re/1300, 10))**2+0.0095*(math.log(re/1300,10))**3
    elif (5*(10**5) <= re < 10**7):
        S = 0.22
    fs = (S*Uc)/D
    print(fs)
    err = 100*((abs(fs-fn))/fn)
    print(err)
    
print(Uc)
        
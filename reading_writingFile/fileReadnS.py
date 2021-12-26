# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 22:01:44 2021

@author: yussi
"""

import shelve
import pprint

# myshel = shelve.open("mydata")
# mydata = ['code','eat', 'sleep']
# myshel['mydata'] = mydata


# print(myshel['mydata'])
# myshel.close()

dict_names = [
    {'name': "coded1", 'age': 21, 'color': "black"},
    {'name': "coded2", 'age': 22, 'color': "black"},
    {'name': "coded2", 'age': 23, 'color': "black"}
]

# pprint.pformat(dict_names, indent= 5)
# print(dict_names)
names =  open('users.text', mode="w")
names.write(pprint.pformat(dict_names, indent= 5))
names.close()
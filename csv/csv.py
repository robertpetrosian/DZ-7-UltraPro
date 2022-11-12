# -*- coding: utf-8 -*-
# модуль работы с csv файлами

import os
import json

f_avto='..'+os.sep+'data'+os.sep+'data_avto.txt' # info about avto
f_outcsv = '..'+ os.sep+ 'data'+os.sep+'avto.csv' # output csv
f_outjson = '..'+ os.sep+ 'data'+os.sep+'avto.json' # output json

with open(f_avto, 'r') as f:
    # read file into list
    lst_strok = f.readlines()

with open(f_outcsv, 'w') as f:
    for x in lst_strok:
        f.write(x.replace(' ',';') )

lst_avto=list(map(lambda x : x.split(), lst_strok)) # list of avto
lst_keys = lst_avto.pop(0) # list of columns
lst_rows = list(map( lambda x: dict(zip(lst_keys, x)) , lst_avto)) # list of dict
dumps = json.dumps(lst_rows)
with open(f_outjson ,'w') as f:
    f.write(dumps)




# модуль работы с DOC файлами

import os
import docxtpl

f_avto= '..'+os.sep+'data'+os.sep+'data_avto.txt' # info about avto
f_out = '..'+os.sep+'data'+os.sep+'avto.docx' # output docx
f_tmpl = 'templates'+os.sep+'tmpl_avto.docx' # template docx

with open(f_avto) as f:
    lst_strok = f.readlines()

lst_avto=list(map(lambda x : x.split(), lst_strok)) # list of avto
lst_keys = lst_avto.pop(0) # list of columns

lst_rows = list(map( lambda x: dict(zip(lst_keys, x)) , lst_avto)) # list of dict

tm=docxtpl.DocxTemplate(f_tmpl)
dict_avto = {'nof':f_avto,
             'lst_rows':lst_rows ,
             }

rez = tm.render(dict_avto)
tm.save(f_out)

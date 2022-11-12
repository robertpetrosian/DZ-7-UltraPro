# модуль работы с html файлами

import os
import jinja2

f_avto='..'+os.sep+'data'+os.sep+'data_avto.txt' # info about avto
f_tmpl = 'templates'+os.sep+'tmpl_avto.html' # template html
f_out = '..'+ os.sep+ 'data'+os.sep+'avto.html' # output html

with open(f_avto, encoding='utf-8') as f:
    # read file into list
    lst_strok = f.readlines()

lst_avto=list(map(lambda x : x.split(), lst_strok)) # list of avto
lst_keys = lst_avto.pop(0)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates', encoding='utf-8'),
    autoescape=jinja2.select_autoescape(['html']))

tm = env.get_template('tmpl_avto.html')

dict_avto = {'nof':f_avto,
             'lst_keys':lst_keys,
             'one_avto':lst_avto,
             }

rez = tm.render(dict_avto)

with open(f_out, 'w') as f:
    f.write(rez)

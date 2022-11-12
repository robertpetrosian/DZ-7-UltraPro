# class Tmpl for create template and use it
import jinja2


class Tmpl():
    def create_tmpl(self):
        '''

        :param file: name of template file
        :return:
        '''
        txt = '''
        <!DOCTYPE html> 
        <html lang="ru"> 
            <head> <meta charset="windows-1251">
                <title> Автомобили  </title>
            </head>
            <body>
                <table border=1>
                    <caption>
                    <tr>
                    {% for item in lst_avto[0] %}
                        <td>item</td>
                    {% endfor %}
                    </tr>
                    </caption>
                    <tr>
                        {% for item in lst_avto[1:] %}
                            <td>item</td>
                        {% endfor %}
                    </tr>
                </table>
            </body>
        </html>
        '''
        with open(file=self.html, mode='w') as f:
            f.write(txt)


    def create_html(self):
        '''

        :param file: name of template file
        :param list_avto: list of avto from data file
        :return:
        '''
        tm = jinja2.Template(self.tmpl)
        rez=tm.render({'lst_avto' : self.lst_avto} )
        print(rez)




    def __init__(self,tmpl='tmpl', mode='html', list_avto=[]):
        '''
        init instance for fill and use template
        :param mode: type of file, aviable: docx (default) , html,csv,json
        :param tmpl:name of template / tmpl - default
        '''

        self.html = tmpl+'.'+mode
        self.tmpl = 't_'+ self.html
        self.lst_avto = list_avto

        self.create_tmpl()
        self.create_html()





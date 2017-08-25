import sys
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('./templates/'))

def t_render(template_file, context):
    return env.get_template(template_file).render(context)

def htmlstr(raw_string):
    return raw_string.replace('\n','<br>').replace('\t',' ').replace(' ','&nbsp;')

def create_index_html(index):
    textfile = 'char'+str(index)+'.txt'
    with open(textfile,'r') as t:
        sheet = t.read()
    html_sheet=htmlstr(sheet)
    filename = 'char'+str(index)+'.html'
    context = {
        'char_name':'角色'+str(index),
        'sheet': html_sheet
    }
    with open(filename, 'w') as f:
        html = t_render('index.html',context)
        f.write(html)

def main():
    for x in range(0,100):
        create_index_html(x)

if __name__ == '__main__':
    main()




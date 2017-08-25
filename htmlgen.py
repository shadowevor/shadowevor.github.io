import sys
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('./templates/'))

def t_render(template_file, context):
    return env.get_template(template_file).render(context)

def create_index_html():
    filename = 'output.html'
    urls = ['http://dnd.com','http://dcc.com']
    context = {
        'urls':urls
    }
    with open(filename, 'w') as f:
        html = t_render('index.html',context)
        f.write(html)

def main():
    create_index_html()

if __name__ == '__main__':
    main()




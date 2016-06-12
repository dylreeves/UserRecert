from jinja2 import Environment, FileSystemLoader
from weasy import HTML
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('report.html')
template_vars = {"username" : "dylan.reeves"}
html_out = template.render(template_vars)
HTML(string=html_out).write_pdf("test.pdf")

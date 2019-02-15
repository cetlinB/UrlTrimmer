from . import utils
from django.http import HttpResponse


def index(request):
    html_code = """<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <title>Title</title>
                        </head>
                        <body>
                        """
    shortcuts = utils.readAll()
    for x in shortcuts:
        html_code += """<div>""" + x[0] + "  :  " + x[1] + """</div>"""
    return HttpResponse(html_code)



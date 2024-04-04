PAGE_TITLE = "My website"

def generate_body():
    body = "<h2>This is my Python Webpage</h2>\n"
    body += "<p>The body of this html doc is from a Python string</p>"
    return body

page = (f'''
<DOCTYPE! html>
<html>
    <head>
        <title> {PAGE_TITLE} </title>
    </head>
    <body>
        {generate_body()}
    </body>
   
</html>
''')
#page = page.replace("_TITLE_", PAGE_TITLE)
#page = page.replace("_BODY_", generate_body())

print(page)

import cgi
 
html = """
    <meta charset="utf-8" />
    <form method="post" action="wsgi.4.py">
        <fieldset>
            <legend>
                <input type="submit" value="odeslat">
            </legend>
            <p>
                Jméno (<em>jedinečná hodnota</em>): <input type="text" name="jmeno" value="{name}">
            </p>
            <p>
                Jazyky (<em>více hodnot</em>):
                angličtina <input name="jazyky" type="checkbox" value="eng" {eng}/> ,
                ruština <input name="jazyky" type="checkbox" value="rus" {rus}> ,
                japonština <input name="jazyky" type="checkbox" value="jap" {jap}>
            </p>
        </fieldset>
    </form>
    <p>
        {body}
    </p>
"""
 
def application(environ, start_response):
    #print(environ['wsgi.input'])
    #print(environ['wsgi.input'].read())
    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
    body = '<em>getlist()</em> pro <em>wsgi.input</em>:<br/>'
    for key in sorted(form):
        body += str(key) + ': ' + str(form.getlist(key)) + '<br/>'
    
    name = form.getlist('jmeno')[0] if 'jmeno' in form else ''
    
    lengs = form.getlist('jazyky') if 'jazyky' in form else ''
    eng = 'checked' if 'eng' in lengs else ''
    rus = 'checked' if 'rus' in lengs else ''
    jap = 'checked' if 'jap' in lengs else ''
    
    response_body = html.format(
        name = name, eng = eng, rus = rus, jap = jap, body = body)
    response_body = bytes(response_body, encoding='utf-8')
    response_headers = [
        ("Content-type", "text/html"),
        ("Content-length", str(len(response_body)) ),
    ]
    start_response("200 OK", response_headers)
    return [response_body,]
 
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('localhost', 8080, application)
    server.serve_forever()
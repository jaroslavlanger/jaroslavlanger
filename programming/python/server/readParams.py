'''
Writes parameters written behind the localhost.
http://localhost:8080/?THIS_WILL_BE_SEEN!
'''
def application(environ, start_response):
    #body = 'ENVIRON\n\n'
    '''
    for key, value in sorted(environ.items()):
        body += str(key) + ': ' + str(value) + '\n'
    '''
    body = str(environ['QUERY_STRING']) 
    body = bytes(body, encoding='utf-8')
    response_headers = [
        ("Content-type", "text/plain; charset=utf-8"),
        ("Content-length", str(len(body)) ),
    ]
    start_response("200 OK", response_headers)
    return [body,]
    ##return [environ['QUERY_STRING']]
 
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('localhost', 8080, application)
    server.handle_request()
    server.serve_forever()
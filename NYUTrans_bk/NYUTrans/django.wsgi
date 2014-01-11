def application(environ, start_response):
    status = '200 OK'
    output = 'Hello Donato!! this is loading from the file at /var/www/vhosts/donatocruz.com/html/NYUTrans/django.wsgi'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]

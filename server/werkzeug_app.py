from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(f'This is a web server running at {request.remote_addr}')
    return Response('A WSGI application generated this response')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )
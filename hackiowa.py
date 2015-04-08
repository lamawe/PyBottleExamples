from bottle import get, post, request, route, run, static_file, template

#
# HomePage (index.html)
@route('/')
@route('/home')
@route('/index.html')
def welcome():
    return template('home.tpl')

@route('/camera')
def camera():
    return template('camform.tpl')

@post('/camera')
def camera_action():
    filetype = request.forms.get('filetype')
    return '''
       <p>Username: %s</p>
    ''' % (filetype)    

#
# Manage static resources
@route('/static/<path:path>')
def serve_static_files(path):
    return static_file(path, root='./static')

#
# Handle Errors (404 - File Not Found)
@error(404)
def error404(error):
    return 'Page Missing.'

#
# Run the web server.  
run(host='192.168.56.101', port=8080, debug=True)

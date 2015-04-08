from bottle import get, post, request, route, run, static_file, template

@route('/hello')
def hello():
    return "<h1>Hello</h1>"


#
# HomePage (index.html)
@route('/')
def welcome():
   return static_file("index.html", root="./")
@route('/index.html')
def welcome():
   return static_file("index.html", root="./")

@route('/camera')
def camera():
    return '''
       <form action="/camera" method="post">
       File Format: <select name="filetype">
                    <option value="jpg">JPG</option>
                    <option value="gif">GIF</option>
                    <option value="bmp">BMP</option>
                    </select><br/>
       
       <input value="Go" type="submit" />
       </form>
    '''

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
# Run the web server.  
run(host='192.168.56.101', port=8080, debug=True)

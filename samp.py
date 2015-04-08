
#!/usr/bin/python
#

from bottle import app, get, post, redirect, request, route, run, static_file, template
from beaker.middleware import SessionMiddleware

session_options = {
    'session.type': 'file',
    'session.data_dir': './session',
    'session.auto': True,
}

app_session = SessionMiddleware(app(), session_options)

@route('/login')
def login():
    app_session = request.environ.get('beaker.session')
    app_session['logged_in'] = True
    return 'You have just logged in'

@route('/logout')
def logout():
    app_session = request.environ.get('beaker.session')
    if app_session.get('logged_in'):
        app_session['logged_in'] = False
        return 'You just logged out'
    redirect('/login')

@route('/dashboard')
def dashboard():
    app_session = request.environ.get('beaker.session')
    if app_session.get('logged_in'):
        return 'You were already logged in'
    redirect('/login')

run(app=app_session, host='192.168.56.101', port=8080, debug=True, reloader=True)

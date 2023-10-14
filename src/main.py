#!/bin/env python3

from bottle import Bottle, request

import webview

server = Bottle()

@server.route('/')
@server.route('/hello/<name>')
def hello(name='Stranger'):
    return f'''
        <h1>Hello {name}!</h1>
        <form action="/login" method="post">
            Name: <input name="name" type="text" required />
            <input value="Login" type="submit" />
        </form>
    '''

@server.route("/login", method='POST')
def login():
    name = request.forms.get('name')
    return f'''
        <h1>Hello {name}!</h1>
        Go to <a href="https://www.google.com">Google</a>!
    '''

webview.create_window('Use pywebview in flatpak', server)
webview.start()

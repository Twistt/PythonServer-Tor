from flask import Flask, render_template, send_from_directory, request, url_for
import sqlite3
from ESECrypto import ESEC



if __name__ == "__main__":

    app = Flask("example")
    port = 5000
    host = "127.0.0.1"
    serverencryptionkey = "OverthesPaghettiMonsteristhechEEse"

    @app.route('/js/<path:path>')
    def send_js(path):
        return send_from_directory('js', path)


    @app.route('/css/<path:path>')
    def send_css(path):
        return send_from_directory('css', path)


    @app.route('/img/<path:path>')
    def send_img(path):
        return send_from_directory('img', path)


    @app.route('/fonts/<path:path>')
    @app.route('/static/<path:path>')
    def send_static(path):
        return send_from_directory('static', path)


    @app.route('/')
    @app.route('/<name>')
    def hello_world(name=None):
        return render_template('index.html', name=name)


    @app.route('/register')
    @app.route('/register/')
    def register():
        return render_template('register.html')

    @app.route('/completeregistration', methods=['POST'])
    def register_submit():
        mstatus = ""
        statusbit = 1
        serverkey = "asfgsdfg32545"
        name = request.form['screenname']
        passw = request.form['password']

        if name == "" or passw == "":
            statusbit = 0
            mstatus = "You registration failed because you MUST specify a screen name and password (so no one can pretend they are you)."
        else:
            statusbit = 1
            # todo: create database save logic here.
            e = ESEC()
            serverkey = e.encrypt(name+passw, serverencryptionkey)
            mstatus = "User created successfully!"
        return render_template('register.html', screenname=name, password=passw, status=mstatus, statusbit=statusbit, responsekey=serverkey.decode('utf-8'))
    def log_page_hit():
        pass

app.run()

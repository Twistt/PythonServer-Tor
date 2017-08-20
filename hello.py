from stem.control import Controller
from flask import Flask, render_template, send_from_directory

if __name__ == "__main__":

    app = Flask("example")
    port = 5000
    host = "127.0.0.1"
    hidden_svc_dir = "/home/twist/Documents/tor/"


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


    print (" * Getting controller")
    controller = Controller.from_port(address="127.0.0.1", port=9051)
    try:
        controller.authenticate(password="")
        controller.set_options([
            ("HiddenServiceDir", hidden_svc_dir),
            ("HiddenServicePort", "80 %s:%s" % (host, str(port)))
            ])
        svc_name = open(hidden_svc_dir + "/hostname", "r").read().strip()
        print (" * Created host: %s" % svc_name)
    except Exception as e:
        print (e)
    app.run()

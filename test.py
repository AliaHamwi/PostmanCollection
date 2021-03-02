from flask import Flask,url_for,jsonify
from postman_collection_generation import generate_collection

app = Flask(__name__)



@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route("/postapi", methods=["POST"])
def site_map():
    return 'postapi'


@app.route("/routes", methods=["GET"])
def getRoutes():
    routes = {}
    for r in app.url_map._rules:
        routes[r.rule] = {}
        routes[r.rule]["functionName"] = r.endpoint
        routes[r.rule]["methods"] = list(r.methods)

    routes.pop("/static/<path:filename>")

    return jsonify(routes)


@app.route("/generate", methods=["GET"])
def generate_collection_api(type='api',name='testname',url_domain='localhost',port=5000,output_path = '.'):
    generate_collection(app,type='api',name='testname',url_domain='localhost',port=5000,output_path = '.')
    return jsonify({"result":"Done!"})

if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request
import json
import std

app = Flask(__name__)
api = Api(app)

#sampledict = {"1":10,"2":12,"3":14,"4":8,"5":11,"6":1000}
parser = reqparse.RequestParser()

class HelloWorld(Resource):
    def get(self,dictionary):
        return std.detect_anomalies(dictionary)
    # def post(self):
    #     incoming_report = request.get_json()
    #     data = json.loads(incoming_report)
    #     # parser.add_argument("number")
    #     # args = parser.parse_args()
    #     id = int(max(sampledict.keys()))+1
    #     sampledict[id] = data[1]
    #     return sampledict[id],201
    def post(self,dictionary):
        #dicty =request.data
        #return std.detect_anomalies(dictionary)
        args = parser.parse_args()
        un = str(args[1])
        pw = str(args[2])
        return jsonify(u=un, p=pw)

api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request
import json
import std
import sys
import os

app = Flask(__name__)
api = Api(app)

sampledict = {"1":10,"2":12,"3":14,"4":8,"5":11,"6":1000}
anomaly_put_args = reqparse.RequestParser()


class AnomalyAPI(Resource):
    def get(self):
        return "get works"


    def put(self):
        print(request.form)
        numbers =[]
        resultArray = []
        for key in request.form.keys():
            numbers.append(int(request.form[key]))
        print(numbers)
        resultArray = std.anomaly_detector(numbers)
        return resultArray

api.add_resource(AnomalyAPI,'/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 5000)
#!/usr/bin/env python

from flask import Flask, request
from flask.ext.restful import Resource, Api, reqparse
import generate_tl as tl

app = Flask(__name__)
api = Api(app)

class TrafficLight(Resource):
    def create_data_structure(self,args):
        data = {
            'type': args['type'],
            'size_g': args['size_g'],
            'fat': {
                'hundred_g': args['fat_100'],
                'serving_g': args['fat_serving'],
            },
            'sat': {
                'hundred_g': args['sat_100'],
                'serving_g': args['sat_serving'],
            },
            'sugar': {
                'hundred_g': args['sugar_100'],
                'serving_g': args['sugar_serving'],
            },
            'salt': {
                'hundred_g': args['salt_100'],
                'serving_g': args['salt_serving'],        
            }
        }
        return data

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('size_g', type=int)
        parser.add_argument('fat_100', type=float)
        parser.add_argument('fat_serving', type=float)
        parser.add_argument('sat_100', type=float)
        parser.add_argument('sat_serving', type=float)
        parser.add_argument('sugar_100', type=float)
        parser.add_argument('sugar_serving', type=float)
        parser.add_argument('salt_100', type=float)
        parser.add_argument('salt_serving', type=float)
        args = parser.parse_args()
        nutrition_data = tl.define_limits()
        food_data = self.create_data_structure(args)
        colours = tl.generate_tl(nutrition_data, food_data)

        return {'tl_data': colours}

api.add_resource(TrafficLight, '/')

if __name__ == '__main__':
    app.run(debug=True)
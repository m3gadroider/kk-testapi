#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
import os
from flask import Flask, jsonify, abort, make_response, request, Response
from math import sqrt

app = Flask(__name__)
#Authentification

@app.route('/api/Fibonacci', methods=['GET'])
def get_fibo():
    try: 
        n = int(request.args.get('n'))
    except:
        return jsonify({"message": "The request is invalid."})    
    return jsonify(int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))))

@app.route('/api/ReverseWords', methods=['GET'])
def get_reverse():
    sen_list = request.args.get('sentence').split()
    rev_sen_list = []
    for item in sen_list:
        rev_sen_list.append(item[::-1])
    new_sen = ' '.join(rev_sen_list)
    #resp = Response(response=new_sen,status=200,mimetype="application/json")
    return jsonify(new_sen)

@app.route('/api/TriangleType', methods=['GET'])
def get_triangle_type():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    c = int(request.args.get('c'))

    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        print "in here"
        if a == b == c:
            return jsonify("Equilateral")
        elif a != b != c:
            return jsonify("Scalene")
        else:
            return jsonify("Isosceles")
    else:
        return jsonify("Error")

@app.route('/api/Token', methods=['GET'])
def get_token():
    return jsonify("00000000-0000-0000-0000-000000000000")

#404 not found 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404) 
 
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
#!/usr/bin/env python

import json
from flask import Flask
from flask_cors import CORS
from flask import request
from flask import jsonify

from ChatNet import IntentModel

# Instatiate flask server
app = Flask(__name__)
CORS(app)
cNet = IntentModel()

# Set up one endpoint
@app.route('/', methods=['GET'])
def landing():
    # Return JSON body
    return """Welcome to PalindREST, a simple REST API for reversing a string. Submit a PUT request using the 'input' \
    KEY and a string VALUE of your choice and the reverse string will be returned as the VALUE of the 'body' KEY.""", 200

# Final PUT endpoint
@app.route('/', methods=['PUT'])
def string_flip():
    print("request received")
    request_body = json.loads(request.get_data().decode('utf-8'))
    print('request_body:', request_body)
    print("request_body['input']",request_body['input'])
    put_input = request_body ['input']
    print('put_input', put_input)
    
    ## put_input = request.args.get('input') ## The Old way. . . uses the built in query string rather than Body

    try:
        # Get response
        ints = cNet.predict_class(put_input, cNet.model)
        body_output = cNet.get_response(ints, cNet.intents)
        print(body_output)
    except Exception as e:
        print(e)
    # except:
    #     body_output = 'Sorry API seems to have experianced an error'
    #     print(body_output)
    return jsonify(body=body_output), 200

# Run Code
if __name__ == '__main__':
    app.run(host="0.0.0.0")
    # app.run()

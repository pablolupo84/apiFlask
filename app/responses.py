from flask import jsonify

def bad_request(message_error="not error"):
    return jsonify({
        'success': False,
        'data': {},
        'messages':'Bad request',
        'code': 400,
        'message_error':message_error
    }),400

def not_found():
    return jsonify(
        {
            'success': False,
            'data': {},
            'message': 'Resource not found',
            'code': 404
        }
        ),404  

def response(data):
    return jsonify(
        {
            'success': True,
            'data': data
        }
    ),200
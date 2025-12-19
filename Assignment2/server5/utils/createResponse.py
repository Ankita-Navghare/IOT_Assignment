from flask import jsonify


def createResponse(msg, error=False):
    d = dict()
    if error == True:
        # error
        d = {
            'Response code' : '?',
            'Response string' : '?',
            'extra MSG' : msg
        }
    else:
        # no error
        d = {
            'Response code' : '200',
            'Response string' : 'OK',
            'Extra Data/Msg' : msg
        }

    return jsonify(d)


import hmac
import hashlib
import time
import ast

from flask import request, make_response

# Basic Auth
def login_required(func):
    '''Basic Auth http for URI's'''
    def wrapper(self, **kwargs):
        if request.authorization \
            and request.authorization['username'] == 'rusbel' \
            and request.authorization['password'] == 'pass':
            return func(self, **kwargs)
        return make_response('Could not verify your login!', 401, 
            {'WWW-Authencticate': 'Basic realm="Login Required"'}
            )
    
    return wrapper


# Hmac implementation
SECRET_KEY = 'ESTA ES LA LLAVE SECRETA'

def generate_hash():
    'Generates hash this should be done for the client '
    timestamp = str(int(time.time()))
    # Creates first hash object with the following args
    # digestmod contains the name of a hash algorithm.
    hash_api = hmac.new(key=SECRET_KEY.encode(), digestmod=hashlib.sha1)
    # Attach the message in this case will be the burned user_id
    hash_api.update('1'.encode())
    # Attach a the time stamp to the mixture in hexadecimal representation
    hash_api.update(timestamp.encode())
    # This data will be compared with headers of request
    data = {"hash": hash_api.hexdigest(), "timestamp": timestamp}

    return data


def auth_required(func):
    def wrapper(self):
        hash_api = request.headers.get('X-HASH')
        hash_client = hmac.new(key=SECRET_KEY.encode(), digestmod=hashlib.sha1)
        # Attach the message
        hash_client.update(request.headers.get('X-UID').encode())
        # Attach the timestamp of request
        hash_client.update(request.headers.get('X-TIMESTAMP').encode())
        hash_client = hash_client.hexdigest()
        # Comparing both hashes,
        hmac_valitation = hmac.compare_digest(hash_api, hash_client)

        if hmac_valitation:
            return func(self)

        return make_response('Could not verify your login!', 401, {'WWW-Autencticate': 'Basic reaml="Login Required"'})

    return wrapper
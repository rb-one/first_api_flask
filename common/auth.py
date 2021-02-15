'''Basic Auth'''
from flask import request, make_response

def login_required(func):
    '''Login required for URI's'''
    def wrapper(self, **kwargs):
        if request.authorization \
            and request.authorization['username'] == 'rusbel' \
            and request.authorization['password'] == 'pass':
            return func(self, **kwargs)
        return make_response('Could not verify your login!', 401, 
            {'WWW-Authencticate': 'Basic realm="Login Required"'}
            )
    
    return wrapper


## Refer https://pythonhosted.org/Flask-JWT/
from werkzeug.security import safe_str_cmp


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# create an object for user 
users = [User(1, 'user1', 'abcxyz')]

# construct table/dict from the object 
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

def secrettoken():
    return "testuser"    



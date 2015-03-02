import hashlib
import web
import auth_model
import urlparse
import re
import base64
import json

urls=(
    '/','Ask',
    '/login','Login',
    '/logout','Logout',
    '/new','New',
    '/secrets/(.*)','Secrets',
)

class Secrets:
    def GET(self, secret_id):
        if not session_data["loggedin"]:
          web.ctx.status = '401 Unauthorized'
          return "You must log-in before asking for secrets"

        username = session_data['username']

        if secret_id:
          response = auth_model.get_secret(username, secret_id)
        else:
          response = auth_model.get_secrets(username)

        return json.dumps(list(response))

    # Saves a new secret for the given user
    # Ignores secret_id
    def POST(self, secret_id):
        if not session_data["loggedin"]:
          web.ctx.status = '401 Unauthorized'
          return "You must log-in before posting secrets"
          
        username = session_data['username']
        secret = web.data()
        secret_id = auth_model.new_secrets(username, secret)

        if not secret_id or secret_id < 0:
          raise web.InternalError (message="Coudln't save secret. Try again later.")

        return json.dumps({"id": secret_id, "secret": secret})

    # Deletes the given secret
    def DELETE(self, secret_id):
        if not session_data["loggedin"]:
            web.ctx.status = '401 Unauthorized'
            return "You must log-in before deleting secrets"
        
        username = session_data['username']
        
        if not secret_id or len(secret_id) == 0:
          raise web.BadRequest (message="Must supply a secret ID in the URL")

        response = auth_model.delete_secret (username, secret_id)

        if response > 0:
          return "OK"
       
        raise web.BadRequest (message="Couldn't delete secret. Ensure the secret ID is valid by calling GET /secrets")

    # Updates a secret
    def PATCH(self, secret_id):
        if not session_data["loggedin"]:
            web.ctx.status = '401 Unauthorized'
            return "You must log-in before deleting secrets"

        username = session_data['username']

        if not secret_id or len(secret_id) == 0:
          raise web.BadRequest (message="Must supply a secret ID in the URL")
       
        # New secret
        secret = web.data()
        response = auth_model.modify_secret (username, secret_id, secret)

        return json.dumps({"id": secret_id, "secret": secret})

class Login:
    def POST(self):
        auth_header = web.ctx.env.get('HTTP_AUTHORIZATION')

        if not auth_header:
          raise web.BadRequest("Authorization header must be present.") 
        
        try:
          credentials = re.sub('^Basic ', '', auth_header)
          # Not doing base64 encoding/decoding for simplicity
          username, password = credentials.split(":")
        except:
          raise web.BadRequest("Authorization header is malformed.")

        pwdhash = hashlib.md5(password).hexdigest()
        pwdstore = list(auth_model.get_pass(username))
      
        if not pwdstore or len(pwdstore)==0 or pwdstore[0]['password'] != pwdhash:
            web.ctx.status = '401 Unauthorized'
            return "Incorrect username/password combination"
        else:
            session_data['loggedin'] = True
            session_data['username'] = username
            return "You are now logged in as %s" % username

class Logout:
    def GET(self):
        session_data['loggedin'] = False
        return "You are now logged out!"

class New:
    def POST(self):
        data = urlparse.parse_qs(web.data())
        USER_KEY='user'
        PWD1_KEY='pwd1'
        PWD2_KEY='pwd2'

        if USER_KEY not in data or PWD1_KEY not in data or PWD2_KEY not in data:
          raise web.BadRequest (message = "Must send user, pwd1 and pwd2 in url encoded format")

        user=data['user'][0]
        pwd1=data['pwd1'][0]
        pwd2=data['pwd2'][0]

        if auth_model.check_user(user):
            return web.BadRequest (message = "Username already exists!")
        elif pwd1 != pwd2:
            return web.BadRequest (message = "Passwords do not match")
        else:
            pwdhash=hashlib.md5(pwd1).hexdigest()
            auth_model.new_user(user,pwdhash)
            session_data['loggedin'] = True
            session_data['username'] = user
            return "Signed up! You are also logged in now!"

app=web.application(urls,globals())
#store session on disk or in db?
web.config.debug=False
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'loggedin': False,'username':''})
session_data = session._initializer

if __name__=='__main__':
    app.run()

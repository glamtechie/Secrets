import web

db=web.database(dbn='mysql',db='secrets',user='poojanaik',pw='password')

def new_user(name,text):
    db.insert('user_info',username=name,password=text)

def get_pass(user):
    return db.where('user_info',what='password',username=user)

def check_user(user):
    return db.where('user_info',what='username',username=user)

def get_secrets(user):
    return db.where('user_secrets',what='id,secret',username=user)

def get_secret(user, secret_id):
    return db.where('user_secrets',what='id,secret',username=user, id=secret_id)

def new_secrets(user,text):
    return db.insert('user_secrets',username=user,secret=text)

def modify_secret(user, secret_id, text):
    where_dict = { "id" : secret_id, "user" : user }
    return db.update('user_secrets', vars=where_dict, where="username=$user and id=$id",secret=text)

def get_user(id):
    return db.where('user_secrets',what='username',id=id)

def delete_secret(user, secret_id):
    where_dict = { "id" : secret_id, "user" : user }
    return db.delete('user_secrets', vars=where_dict, where="username=$user and id=$id")

# Warning! Deletes all secrets for a user.
def delete_secrets(user):
    return db.delete('user_secrets', where="username=$user")

from peewee import *
from datetime import datetime



db = SqliteDatabase("blog.db")

class BaseModel(Model):
    class Meta:
        database = db



class User(BaseModel):
    username = CharField(unique=True)


class Post(BaseModel):
    title = CharField()
    content = TextField()
    created_at = DateTimeField(formats="%Y-%m-%d %H:%M:%S", default=datetime.now)
    user_id= ForeignKeyField(User , backref='posts')
    

# Entry point 
if __name__== '__main__':
    #db.connect()
    #db.create_tables([User,Post])

    #ajouter un nouvel utilisateur
    #adam = User.create(username='anassitos')
    
    anas=User.get(User.username=='anassitos')
    new_post= Post.create(title='discover new places', content='come and visit this place with your friends', user_id = anas)



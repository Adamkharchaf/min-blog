from peewee import *
from datetime import datetime



db = SqliteDatabase("blog.db")

class BaseModel(Model):
    class Meta:
        database = db



class category(BaseModel):
    name = CharField(max_length=100 , unique=True)
    date_added = DateField(formats="%Y-%m-%d" ,default=datetime.now)

class User(BaseModel):
    #country list:
    username = CharField(unique=True)
    age = IntegerField()
    country = CharField()
    join_date = DateTimeField(formats="%Y-%m-%d %H:%M:%S" , default=datetime.now)



class comment(BaseModel):
    content= CharField(max_length=255, null=False)
    created_at = DateField(formats="%Y-%m-%d" , default=datetime.now)
    is_published = BooleanField(default=False)
    user= ForeignKeyField(model=User, backref="comments")



class Post(BaseModel):
    title = CharField()
    content = TextField()
    created_at = DateTimeField(formats="%Y-%m-%d %H:%M:%S", default=datetime.now)
    user= ForeignKeyField(User , backref='posts')
    category = ForeignKeyField(model=category , backref="posts")

    

# Entry point 
if __name__== '__main__':
   db.connect()
   db.create_tables([User,comment,category,Post])

    



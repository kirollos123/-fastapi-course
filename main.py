from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts=[{"title": "title of post 1" ,"content":"content of post 1","id":1},{"title ":"favorite food","content": "i like piazz","id":2}]

@app.get("/")
def read_root():
    return {"data": my_posts}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}
@app.get("/posts/{id}")#path parmeter 
def get_post(id):
    print(id)
    return {"post_detail": f"here is post {id}"}
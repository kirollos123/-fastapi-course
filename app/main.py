from typing import Optional

from fastapi import FastAPI , Response,status,HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    


my_posts=[{"title": "title of post 1" ,"content":"content of post 1","id":1},{"title ":"favorite food","content": "i like piazz","id":2}]
def find_post (id):
    for p in my_posts:
        if p [ "id"]== id :
            return p
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
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
def get_post(id:int, response :Response):
    
    post= find_post ( id)
    if not post : 
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} was not found")
      #  response.status_code=status.HTTP_404_NOT_FOUND
     
      #return{'massage':f"post with id {id} was not found"}
    return {"post_detail": post}
@app.get("/posts/latest")
def get_latest_post():
    post=  my_posts[len(my_posts)-1]
    return{"detail ":post}
@app.delete("/posts/{id}")

def delete_post(id: int):
    index = find_index_post(id)

    if index is None:
        raise HTTPException(status_code=404, detail="Post not found")

    my_posts.pop(index)
    return {"message": "Post was successfully deleted"}
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index is None:
            raise HTTPException(status_code=404, detail="Post not found")
    
    post_dict=post.dict()
    post_dict ['id']=id
    my_posts [index ]=post_dict
    
    return {"data": post_dict}
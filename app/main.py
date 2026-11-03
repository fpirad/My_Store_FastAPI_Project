#......................................................................... test:
# from fastapi import FastAPI
# from app.database import engine,Base
# from app import models
# from pydantic import BaseModel
# from app import routers

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# # @app.get("/user/")
# # async def root():
# #     return {"message": "Hello user"}

# @app.get("/user/customer")
# async def root():
#     return {"message": "Hello customer"}

# @app.get("/user/{name}/")
# async def root(name):
#     return {"message": f"Hello {name}"}

# # @app.get("/user/{name}/{family}/")
# # async def root(name,family):
# #     return {"message": f"Hello {name} {family}"}

# @app.get("/user/test/{id}/")
# async def root(id:int):
#     return {"message": f"Helloooo {id}"}

# @app.get("/user/{id}/")
# async def root(id:int):
#     return {"message": f"Helloooo {id}"}

# @app.get("/user/")
# async def show_user(id:int,name:str='fahim'):
#     return {"message": f"Helloooo {id} with name {name}"}

# #......................................................................... test2 schemas:

# user_list = [
#     {'id':1,'name':'fahimeh','family':'rad','age':33,'password':'123'},
#     {'id':2,'name':'hashem','family':'haji','age':38,'password':'1234'}
# ]

# class UserBase(BaseModel):
#     name: str
#     family: str
#     age: int
# class UserCreate(UserBase):
#     id: int
#     password : str
# class UserUpdate(UserBase):
#     id: int
#     password : str
# class UserOut(UserBase):
#     id: int

# app = FastAPI()

# @app.get('/users/',response_model=list[UserBase])
# async def read_all_users():
#     return user_list

# @app.get('/users/{id:int}',response_model=UserOut | dict)
# async def read_user_by_id(id:int):
#     for i in user_list:
#         if i['id']==id:
#             return i
#     else:
#         return {'message':'Not Found'}

# @app.post('/users/',response_model=list[UserOut])
# async def add_user(user: UserCreate):
#     user_list.append(user)
#     return user_list

# @app.put('/users/{id}',response_model=list[UserOut])
# async def update_user(id:int,user: UserUpdate):
#     for i in user_list:
#         if i['id']==id:
#             i['name'] = user.name
#             i['family'] = user.family
#             return user_list
#     else:
#         return {'message':'Not Found'}

# @app.delete('/users/{id:int}',response_model= dict)
# async def delete_user(id:int):
#     for index,user in enumerate(user_list):
#         if user['id']==id:
#             user_list.pop(index)
#             return {'message':'okkk'}
#     else:
#         return {'message':'Not okkk'}

# #?????????????????????????????????????????????????????????????????????????????????????????????soal:
# # @app.delete('/users/{id:int}',response_model= UserOut | dict)
# # async def delete_user(id:int):
# #     for index,user in enumerate(user_list):
# #         if user['id']==id:
# #             user_list.pop(index)
# #             return user_list
# #     else:
# #         return {'message':'Not deleted'}   # chera inja moshkel dare va agar pak ham bokone baz mige not deleted?

#.........................................................................................
from fastapi import FastAPI
from app.database import engine,Base
from app import models
from pydantic import BaseModel
from app.routers import customer_router
from app.routers import product_router
from app.routers import factor_router
from app.routers import factor_item_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title='Welcome To MY Store Shop :)',description='Fahimeh frist API working :)',version='1.0.0') #,docs_url=None,redoc_url=None
app.include_router(customer_router.router)
app.include_router(product_router.router)
app.include_router(factor_router.router)
app.include_router(factor_item_router.router)

# print(app.routes)

@app.get('/')
def root():
    return {'message':'welcome to the shop management API :)'}
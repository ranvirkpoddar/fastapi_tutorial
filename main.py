from fastapi import FastAPI, Body, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()



list_of_usernames = list()

class NameValue(BaseModel):
    name: str
    country: str
    age: int
    base_salary: float

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def token_generate(form_data : OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token":form_data.username, "token_type":"bearer"}

@app.post("/get_profile_photo")
async def get_profile(token :str = Depends(oauth_scheme)):
    print(token)
    return{
        "the authenticated token is": token
    }

@app.post("/nameValue")
def name_value(namevalue: NameValue, marital_status = Body(...)):
    print(namevalue.name)
    return{
        "name": namevalue.name,
        "marital status" : marital_status
    }



@app.get("/home/{user_name}/")
def write_home(user_name:str, query):
    return {
        "Name" : user_name,
        "Age" : 33,
        "query" : query
    }

@app.get("/")
def real_home():
    return {
        "data" : "This is real home"
    }

@app.put("/username/{user_name}")
def put_data(user_name:str):
    print(user_name)
    list_of_usernames.append(user_name)
    return{
        user_name
    }

@app.post("/postData")
def post_data(user_name:str):
    print(user_name)
    list_of_usernames.append(user_name)
    return{
        "usernames": list_of_usernames
    }

@app.delete("/deleteData")
def delete_data(user_name :str):
    list_of_usernames.remove(user_name)

@app.api_route("/homedata",methods=['GET','POST','PUT','DELETE'])
def handle_homedata(username:str):
    print(username)
    return {
        "username" : username
    }
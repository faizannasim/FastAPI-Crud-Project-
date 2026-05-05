from fastapi import FastAPI,HTTPException
from database import engine,SessionLocal
from models import Base,User
from schemas import CreateUser


Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

    
@app.get("/")
def HomePage():
    return {"Message":"This is RestAPI"}


@app.get("/users")
def GetAll_user():
    db = get_db()
    users = db.query(User).all()
    result = []

    for user in users:
         result.append({
        "id":user.id,
        "name":user.name,
        "email":user.email,
        "password":user.password,
        "description":user.description
         })
    return result


@app.post("/users")
def PostUser(user:CreateUser):
    db = get_db()

    new_user  = User(
        name=user.name,
        email=user.email,
        password=user.password,
        description=user.description
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
    "Message": f"User has been created for ID {new_user.id}",
    "id": new_user.id,
    "data":{
        "id":new_user.id,
        "name":new_user.name,
        "email":new_user.email,
        "password":new_user.password,
        "description":new_user.description

    }
}
        

@app.get("/users/{user_id}")
def GetSingle_user(user_id:int):
    db = get_db()
    user = db.query(User).filter(User.id ==user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User Not Found")
    return{
        "id":user.id,
        "name":user.name,
        "email":user.email,
        "password":user.password,
        "description":user.description 
    }
   

@app.put("/users/{user_id}")
def UpdateUser(user_id:int,update_user:CreateUser):
    db = get_db()
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User id not found")
    
    user.name = update_user.name
    user.email = update_user.email
    user.password = update_user.password
    user.description = update_user.description

    db.commit()
    db.refresh(user)

    return {
        "message":"User updated successfully ",
        "data":{
            "id":user.id,
            "name":user.name,
            "email":user.email,
            "password":user.password,
            "description":user.description
           }
    }




@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    db = get_db()
    user  = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User Not found")
    
    db.delete(user)
    db.commit()
    
    return{
        "Message":"user has been Deleted"
    }

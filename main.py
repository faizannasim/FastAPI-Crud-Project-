from fastapi import FastAPI, HTTPException
from database import engine, SessionLocal
from models import Base, User
from schemas import CreateUser


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


@app.get("/")
def HomePage():
    return {
        "message": "Welcome to the User Management REST API"
    }


@app.get("/users")
def GetAll_user():
    db = get_db()
    users = db.query(User).all()
    result = []

    if not users:
        return {
            "message": "No users found in the database",
            "data": []
        }

    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "description": user.description
        })

    return {
        "message": "Users retrieved successfully",
        "total_users": len(result),
        "data": result
    }


@app.post("/users")
def PostUser(user: CreateUser):
    db = get_db()

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password,
        description=user.description
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": f"User account created successfully with ID {new_user.id}",
        "data": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "description": new_user.description
        }
    }


@app.get("/users/{user_id}")
def GetSingle_user(user_id: int):
    db = get_db()
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"No user found with ID {user_id}"
        )

    return {
        "message": "User retrieved successfully",
        "data": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "description": user.description
        }
    }


@app.put("/users/{user_id}")
def UpdateUser(user_id: int, update_user: CreateUser):
    db = get_db()
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"Cannot update because no user exists with ID {user_id}"
        )

    user.name = update_user.name
    user.email = update_user.email
    user.password = update_user.password
    user.description = update_user.description

    db.commit()
    db.refresh(user)

    return {
        "message": f"User with ID {user_id} updated successfully",
        "data": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "description": user.description
        }
    }


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = get_db()
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"Cannot delete because no user exists with ID {user_id}"
        )

    db.delete(user)
    db.commit()

    return {
        "message": f"User with ID {user_id} deleted successfully"
    }
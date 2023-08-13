from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from database import engine, cache_engine
from models import User, Cache, main_metadata, cache_metadata

app = FastAPI()

SessionLocalMain = sessionmaker(bind=engine)
SessionLocalCache = sessionmaker(bind=cache_engine)

@app.post("/create_user/")
def create_user(username: str):
    session_main = SessionLocalMain()
    user = User(username=username)
    session_main.add(user)
    session_main.commit()
    session_main.refresh(user)
    session_main.close()
    return {"id": user.id}

@app.get("/read_user/")
def read_user(user_id: int):
    session_main = SessionLocalMain()
    user = session_main.query(User).filter(User.id == user_id).first()
    session_main.close()
    return user

@app.put("/update_user/")
def update_user(user_id: int, username: str):
    session_main = SessionLocalMain()
    user = session_main.query(User).filter(User.id == user_id).first()
    user.username = username
    session_main.commit()
    session_main.close()
    return {"message": "User updated successfully"}

@app.delete("/delete_user/")
def delete_user(user_id: int):
    session_main = SessionLocalMain()
    user = session_main.query(User).filter(User.id == user_id).first()
    session_main.delete(user)
    session_main.commit()
    session_main.close()
    return {"message": "User deleted successfully"}

@app.post("/create_cache/")
def create_cache(data: str):
    session_cache = SessionLocalCache()
    cache = Cache(data=data)
    session_cache.add(cache)
    session_cache.commit()
    session_cache.refresh(cache)
    session_cache.close()
    return {"id": cache.id}

# You can continue to add more endpoints for interacting with the Cache tablefrom fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from database import engine, cache_engine
from models import User, Cache, main_metadata, cache_metadata

app = FastAPI()

SessionLocalMain = sessionmaker(bind=engine)
SessionLocalCache = sessionmaker(bind=cache_engine)

# Create tables if they do not exist
main_metadata.create_all(bind=engine)
cache_metadata.create_all(bind=cache_engine)

@app.post("/create_user/")
def create_user(username: str):
    session_main = SessionLocalMain()
    user = User(username=username)
    session_main.add(user)
    session_main.commit()
    session_main.refresh(user)
    session_main.close()
    return {"id": user.id}

@app.get("/read_user/")
def read_user(user_id: int):
    session_main = SessionLocalMain()
    user = session_main.query(User).filter(User.id == user_id).first()
    session_main.close()
    return user

@app.put("/update_user/")
def update_user(user_id: int, username: str):
    session_main = SessionLocalMain()
    user = session_main.query(User).filter(User.id == user_id).first()
    user.username = username
    session_main.commit()
    session_main.close()
    return {"message": "User updated successfully"}

@app.delete("/delete_user/")
def delete_user(user_id: int):
    session_main = SessionLocalMain()
    user = session_main.query(User).filter(User.id == user_id).first()
    session_main.delete(user)
    session_main.commit()
    session_main.close()
    return {"message": "User deleted successfully"}

@app.post("/create_cache/")
def create_cache(data: str):
    session_cache = SessionLocalCache()
    cache = Cache(data=data)
    session_cache.add(cache)
    session_cache.commit()
    session_cache.refresh(cache)
    session_cache.close()
    return {"id": cache.id}


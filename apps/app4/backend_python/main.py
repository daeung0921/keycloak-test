import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from schemas import userPayload
from routers import get_user_info
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

APP_HOST=os.getenv("APP_HOST")
APP_PORT= int(os.getenv("APP_PORT"))

origins = ["*"] # allow requests from any origin
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

@app.get("/healthy") 
def health_check():
    return {'status': 'healthy'}

@app.get("/secure")
async def root(user: userPayload = Depends(get_user_info)):
    return {"message": f"ID={user.sub}, Realm Roles={user.realm_roles}"}

if __name__ == '__main__':
    uvicorn.run( "main:app", host=APP_HOST, port=APP_PORT, reload=True)
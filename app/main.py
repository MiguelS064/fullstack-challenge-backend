from fastapi import FastAPI
from app.routes import stack, vuelos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stack.router, prefix="/stack")
app.include_router(vuelos.router, prefix="/vuelos")
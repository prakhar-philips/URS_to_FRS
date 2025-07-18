from fastapi import FastAPI
from backend.routers import frs_router
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="URS to FRS Generator")

app.include_router(frs_router.router, prefix="/api/frs")

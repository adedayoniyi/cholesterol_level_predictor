from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API route from cholesterol_prediction.py
from cholesterol_prediction import router as cholesterol_router

app.include_router(cholesterol_router, prefix="/cholesterol", tags=["cholesterol"])

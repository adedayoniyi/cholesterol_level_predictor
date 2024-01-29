from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


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

if __name__ == "__main__":
    # No need to specify host and port when deploying on Render
    uvicorn.run(app, host="0.0.0.0", port=8000)

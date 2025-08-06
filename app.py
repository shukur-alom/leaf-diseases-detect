from fastapi import FastAPI

app = FastAPI()

@app.get('/disease-detection')
async def disease_detection():  
    return {"message": "Leaf Disease Detection API is running"}
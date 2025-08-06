from fastapi import FastAPI, Request

app = FastAPI()

@app.post('/disease-detection')
async def disease_detection(request: Request):
    data = await request.json()
    image_base64 = data.get("image")
    # Next: decode and process image
    return {"received": bool(image_base64)}
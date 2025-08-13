from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import logging
from utils import test_with_base64_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Leaf Disease Detection API", version="1.0.0")


@app.post('/disease-detection')
async def disease_detection(request: Request):
    """
    Endpoint to detect diseases in leaf images using base64 encoded image data.

    Expected JSON payload:
    {
        "image": "base64_encoded_image_string"
    }

    Returns:
    - Disease analysis results including detection status, disease name, severity, etc.
    """
    try:
        # Parse request data
        data = await request.json()
        image_base64 = data.get("image")

        # Validate input
        if not image_base64:
            raise HTTPException(
                status_code=400, detail="No image data provided")

        if not isinstance(image_base64, str):
            raise HTTPException(
                status_code=400, detail="Image data must be a base64 string")

        logger.info("Processing disease detection request")

        # Process image using utils.py function
        result = test_with_base64_data(image_base64)

        if result is None:
            raise HTTPException(
                status_code=500, detail="Failed to process image")

        logger.info("Disease detection completed successfully")
        return JSONResponse(content=result)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in disease detection: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {str(e)}")


@app.get("/")
async def root():
    """Root endpoint providing API information"""
    return {
        "message": "Leaf Disease Detection API",
        "version": "1.0.0",
        "endpoints": {
            "disease_detection": "/disease-detection (POST)"
        }
    }

from fastapi import FastAPI, Request, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
import logging
import os
from utils import convert_image_to_base64_and_test, test_with_base64_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Leaf Disease Detection API", version="1.0.0")

@app.post('/disease-detection-file')
async def disease_detection_file(file: UploadFile = File(...)):
    """
    Endpoint to detect diseases in leaf images using direct image file upload.
    Accepts multipart/form-data with an image file.
    """
    try:
        logger.info("Received image file for disease detection")
        
        # Read uploaded file into memory
        contents = await file.read()
        
    # Process file directly from memory
        result = convert_image_to_base64_and_test(contents)
        
    # No cleanup needed since file is not saved locally
        
        if result is None:
            raise HTTPException(status_code=500, detail="Failed to process image file")
        logger.info("Disease detection from file completed successfully")
        return JSONResponse(content=result)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in disease detection (file): {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.get("/")
async def root():
    """Root endpoint providing API information"""
    return {
        "message": "Leaf Disease Detection API",
        "version": "1.0.0",
        "endpoints": {
            "disease_detection_file": "/disease-detection-file (POST, file upload)"
        }
    }

"""
API Test Script for Leaf Disease Detection
==========================================

This script tests the FastAPI endpoints to ensure they work correctly.
"""

import requests
import base64
import json
from pathlib import Path


def encode_image_to_base64(image_path: str) -> str:
    """Convert an image file to base64 string"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')




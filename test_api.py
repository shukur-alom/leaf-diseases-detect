"""
API Test Script for Leaf Disease Detection
==========================================

This script tests the FastAPI endpoints to ensure they work correctly.
"""

import requests
import base64
import json
from pathlib import Path


def test_api_endpoint(api_url: str = "http://localhost:8000"):
    """Test the disease detection API endpoint (base64 and file upload)"""
    test_image = "Media/brown-spot-4 (1).jpg"
    if not Path(test_image).exists():
        print(f"Error: Test image not found at {test_image}")
        return
    # Test file upload endpoint
    try:
        print(f"Sending image file to {api_url}/disease-detection-file...")
        with open(test_image, "rb") as img_file:
            files = {"file": (Path(test_image).name, img_file, "image/jpeg")}
            response = requests.post(
                f"{api_url}/disease-detection-file",
                files=files
            )
        if response.status_code == 200:
            result = response.json()
            print("✓ File upload API request successful!")
            print("\nResponse:")
            print(json.dumps(result, indent=2))
        else:
            print(f"✗ File upload API request failed with status {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error (file upload endpoint): {str(e)}")


def test_root_endpoint(api_url: str = "http://localhost:8000"):
    """Test the root endpoint"""
    try:
        response = requests.get(f"{api_url}/")
        if response.status_code == 200:
            print("✓ Root endpoint working!")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"✗ Root endpoint failed with status {response.status_code}")
    except Exception as e:
        print(f"Error testing root endpoint: {str(e)}")


if __name__ == "__main__":
    print("Leaf Disease Detection API Test")
    print("=" * 40)

    api_url = "http://localhost:8000"

    print("\n1. Testing root endpoint...")
    test_root_endpoint(api_url)

    print("\n2. Testing disease detection endpoint...")
    test_api_endpoint(api_url)

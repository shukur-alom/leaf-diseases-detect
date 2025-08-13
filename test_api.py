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


def test_api_endpoint(api_url: str = "http://localhost:8000"):
    """Test the disease detection API endpoint"""

    # Test image path
    test_image = "Media/brown-spot-4 (1).jpg"

    if not Path(test_image).exists():
        print(f"Error: Test image not found at {test_image}")
        return

    try:
        # Encode image to base64
        print("Encoding image to base64...")
        base64_image = encode_image_to_base64(test_image)
        print(f"Image encoded successfully ({len(base64_image)} characters)")

        # Prepare request payload
        payload = {
            "image": base64_image
        }

        # Make API request
        print(f"Sending request to {api_url}/disease-detection...")
        response = requests.post(
            f"{api_url}/disease-detection",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        # Check response
        if response.status_code == 200:
            result = response.json()
            print("✓ API request successful!")
            print("\nResponse:")
            print(json.dumps(result, indent=2))
        else:
            print(f"✗ API request failed with status {response.status_code}")
            print(f"Response: {response.text}")

    except FileNotFoundError:
        print(f"Error: Could not find test image at {test_image}")
    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to API at {api_url}")
        print("Make sure the API server is running with: uvicorn app:app --reload")
    except Exception as e:
        print(f"Error: {str(e)}")


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



"""
Base64 Image Test for Leaf Disease Detection
===========================================

This script demonstrates how to send base64 image data directly to the detector.
"""

import json
import sys,
import base64
from pathlib import Path

# Add the Leaf Disease directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "Leaf Disease"))

try:
    from main import LeafDiseaseDetector
except ImportError as e:
    print(f'{{"error": "Could not import LeafDiseaseDetector: {str(e)}"}}')
    sys.exit(1)


def test_with_base64_data(base64_image_string: str):
    """
    Test disease detection with base64 image data

    Args:
        base64_image_string (str): Base64 encoded image data
    """
    try:
        detector = LeafDiseaseDetector()
        result = detector.analyze_leaf_image_base64(base64_image_string)
        print(json.dumps(result, indent=2))
        return result
    except Exception as e:
        print(f'{{"error": "{str(e)}"}}')
        return None


def convert_image_to_base64_and_test(image_path: str):
    """
    Convert an image file to base64 and test it

    Args:
        image_path (str): Path to the image file
    """
    try:
        if not Path(image_path).exists():
            print(f'{{"error": "Image file not found: {image_path}"}}')
            return None

        # Read and convert to base64
        # Save to a writable /tmp directory (works on Vercel & locally)
        temp_path = os.path.join("/tmp", f"temp_{file.filename}")
        with open(temp_path, "wb") as f:
            f.write(contents)

        base64_string = base64.b64encode(image_bytes).decode('utf-8')

        print(f"Converted image to base64 ({len(base64_string)} characters)")

        # Test with the base64 data
        return test_with_base64_data(base64_string)

    except Exception as e:
        print(f'{{"error": "{str(e)}"}}')
        return None


def main():
    """Test with base64 conversion"""
    image_path = "Media/brown-spot-4 (1).jpg"
    convert_image_to_base64_and_test(image_path)


if __name__ == "__main__":
    main()

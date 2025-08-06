from groq import Groq
import os
import base64
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def encode_image(image_path):
    """Encode image to base64 string"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Load and encode the local image
image_path = "Media/brown-spot-4 (1).jpg"
base64_image = encode_image(image_path)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """Analyze this leaf image for diseases and return the results in JSON format. 
                    
                    Please identify:
                    1. Disease name (if any)
                    2. Disease type/category
                    3. Severity level (mild, moderate, severe)
                    4. Confidence score (0-100%)
                    5. Symptoms observed
                    6. Possible causes
                    7. Treatment recommendations
                    8. Bounding box locations of diseased areas (if any)
                    
                    For bounding boxes, provide coordinates as percentages of image dimensions (0-100):
                    - x: left edge percentage
                    - y: top edge percentage  
                    - width: box width percentage
                    - height: box height percentage
                    
                    Return only valid JSON in this format:
                    {
                        "disease_detected": true/false,
                        "disease_name": "name of disease or null",
                        "disease_type": "fungal/bacterial/viral/pest/nutrient deficiency/healthy",
                        "severity": "mild/moderate/severe/none",
                        "confidence": 85,
                        "symptoms": ["list", "of", "symptoms"],
                        "possible_causes": ["list", "of", "causes"],
                        "treatment": ["list", "of", "treatments"]
                    }"""
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    temperature=0.3,  # Lower temperature for more consistent JSON output
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

# Get the response content
response_content = completion.choices[0].message.content

# Clean up the response - remove markdown code blocks if present
if response_content.startswith('```json'):
    response_content = response_content.replace(
        '```json', '').replace('```', '').strip()

try:
    # Try to parse as JSON
    disease_info = json.loads(response_content)
    print("Leaf Disease Detection Results:")
    print(json.dumps(disease_info, indent=2))
except json.JSONDecodeError:
    print("Raw response (not valid JSON):")
    print(response_content)
    print("\nAttempting to extract JSON from response...")

    # Try to find JSON in the response
    import re
    json_match = re.search(r'\{.*\}', response_content, re.DOTALL)
    if json_match:
        try:
            disease_info = json.loads(json_match.group())
            print("Extracted JSON:")
            print(json.dumps(disease_info, indent=2))
        except json.JSONDecodeError:
            print("Could not parse extracted JSON")

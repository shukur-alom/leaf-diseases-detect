"""
Leaf Disease Detection System
============================

A professional leaf disease detection system using Groq's vision API
to analyze plant leaf images and identify diseases with detailed analysis.

Author: Your Name
Version: 1.0.0
Date: August 2025
"""

import os
import base64
import json
import logging
import sys
from pathlib import Path
from typing import Dict, Optional, List, Tuple
from dataclasses import dataclass
from datetime import datetime

from groq import Groq
from dotenv import load_dotenv


# Configure logging (console only, no file logging)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


@dataclass
class DiseaseAnalysisResult:
    """Data class for storing disease analysis results"""
    disease_detected: bool
    disease_name: Optional[str]
    disease_type: str
    severity: str
    confidence: float
    symptoms: List[str]
    possible_causes: List[str]
    treatment: List[str]
    analysis_timestamp: str = datetime.now().isoformat()


class LeafDiseaseDetector:
    """Professional Leaf Disease Detection System"""

    # Supported image formats
    SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}

    # Model configuration
    MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"
    DEFAULT_TEMPERATURE = 0.3
    DEFAULT_MAX_TOKENS = 1024

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Leaf Disease Detector

        Args:
            api_key (str, optional): Groq API key. If not provided, will load from environment.
        """
        # Load environment variables
        load_dotenv()

        # Initialize API client
        self.api_key = api_key or os.environ.get("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError(
                "GROQ_API_KEY not found in environment variables or provided directly")

        self.client = Groq(api_key=self.api_key)
        logger.info("Leaf Disease Detector initialized successfully")

    def validate_image_path(self, image_path: str) -> Path:
        """
        Validate image path and format

        Args:
            image_path (str): Path to the image file

        Returns:
            Path: Validated Path object

        Raises:
            FileNotFoundError: If image file doesn't exist
            ValueError: If image format is not supported
        """
        path = Path(image_path)

        if not path.exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")

        if path.suffix.lower() not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported image format: {path.suffix}. "
                             f"Supported formats: {', '.join(self.SUPPORTED_FORMATS)}")

        return path

    def encode_image(self, image_path: str) -> str:
        """
        Encode image to base64 string with error handling

        Args:
            image_path (str): Path to the image file

        Returns:
            str: Base64 encoded image string

        Raises:
            FileNotFoundError: If image file doesn't exist
            ValueError: If image format is not supported
            IOError: If image cannot be read
        """
        try:
            validated_path = self.validate_image_path(image_path)
            logger.info(f"Encoding image: {validated_path}")

            with open(validated_path, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode('utf-8')
                logger.info(
                    f"Image encoded successfully. Size: {len(encoded)} characters")
                return encoded

        except Exception as e:
            logger.error(f"Failed to encode image {image_path}: {str(e)}")
            raise

    def create_analysis_prompt(self) -> str:
        """
        Create the analysis prompt for the AI model

        Returns:
            str: Formatted prompt for disease analysis
        """
        return """Analyze this leaf image for diseases and return the results in JSON format. 
        
        Please identify:
        1. Disease name (if any)
        2. Disease type/category
        3. Severity level (mild, moderate, severe)
        4. Confidence score (0-100%)
        5. Symptoms observed
        6. Possible causes
        7. Treatment recommendations
        
        Return only valid JSON in this exact format:
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

    def analyze_leaf_image(self, image_path: str,
                           temperature: float = None,
                           max_tokens: int = None) -> DiseaseAnalysisResult:
        """
        Analyze leaf image for diseases

        Args:
            image_path (str): Path to the leaf image
            temperature (float, optional): Model temperature for response generation
            max_tokens (int, optional): Maximum tokens for response

        Returns:
            DiseaseAnalysisResult: Analysis results

        Raises:
            Exception: If analysis fails
        """
        try:
            logger.info(f"Starting analysis for image: {image_path}")

            # Encode image
            base64_image = self.encode_image(image_path)

            # Prepare request parameters
            temperature = temperature or self.DEFAULT_TEMPERATURE
            max_tokens = max_tokens or self.DEFAULT_MAX_TOKENS

            # Make API request
            completion = self.client.chat.completions.create(
                model=self.MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": self.create_analysis_prompt()
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
                temperature=temperature,
                max_completion_tokens=max_tokens,
                top_p=1,
                stream=False,
                stop=None,
            )

            logger.info("API request completed successfully")
            return self._parse_response(completion.choices[0].message.content)

        except Exception as e:
            logger.error(f"Analysis failed for {image_path}: {str(e)}")
            raise

    def _parse_response(self, response_content: str) -> DiseaseAnalysisResult:
        """
        Parse and validate API response

        Args:
            response_content (str): Raw response from API

        Returns:
            DiseaseAnalysisResult: Parsed and validated results

        Raises:
            ValueError: If response cannot be parsed
        """
        try:
            # Clean up response - remove markdown code blocks if present
            cleaned_response = response_content.strip()
            if cleaned_response.startswith('```json'):
                cleaned_response = cleaned_response.replace(
                    '```json', '').replace('```', '').strip()
            elif cleaned_response.startswith('```'):
                cleaned_response = cleaned_response.replace('```', '').strip()

            # Parse JSON
            disease_data = json.loads(cleaned_response)
            logger.info("Response parsed successfully as JSON")

            # Validate required fields and create result object
            return DiseaseAnalysisResult(
                disease_detected=bool(
                    disease_data.get('disease_detected', False)),
                disease_name=disease_data.get('disease_name'),
                disease_type=disease_data.get('disease_type', 'unknown'),
                severity=disease_data.get('severity', 'unknown'),
                confidence=float(disease_data.get('confidence', 0)),
                symptoms=disease_data.get('symptoms', []),
                possible_causes=disease_data.get('possible_causes', []),
                treatment=disease_data.get('treatment', [])
            )

        except json.JSONDecodeError:
            logger.warning(
                "Failed to parse as JSON, attempting to extract JSON from response")

            # Try to find JSON in the response using regex
            import re
            json_match = re.search(r'\{.*\}', response_content, re.DOTALL)
            if json_match:
                try:
                    disease_data = json.loads(json_match.group())
                    logger.info("JSON extracted and parsed successfully")

                    return DiseaseAnalysisResult(
                        disease_detected=bool(
                            disease_data.get('disease_detected', False)),
                        disease_name=disease_data.get('disease_name'),
                        disease_type=disease_data.get(
                            'disease_type', 'unknown'),
                        severity=disease_data.get('severity', 'unknown'),
                        confidence=float(disease_data.get('confidence', 0)),
                        symptoms=disease_data.get('symptoms', []),
                        possible_causes=disease_data.get(
                            'possible_causes', []),
                        treatment=disease_data.get('treatment', [])
                    )
                except json.JSONDecodeError:
                    pass

            # If all parsing attempts fail, log the raw response and raise error
            logger.error(
                f"Could not parse response as JSON. Raw response: {response_content}")
            raise ValueError(
                f"Unable to parse API response as JSON: {response_content[:200]}...")

    def format_results(self, result: DiseaseAnalysisResult) -> str:
        """
        Format analysis results for display

        Args:
            result (DiseaseAnalysisResult): Analysis results

        Returns:
            str: Formatted results string
        """
        output = []
        output.append("=" * 60)
        output.append("LEAF DISEASE DETECTION RESULTS")
        output.append("=" * 60)
        output.append(f"Analysis Timestamp: {result.analysis_timestamp}")
        output.append(
            f"Disease Detected: {'YES' if result.disease_detected else 'NO'}")

        if result.disease_detected:
            output.append(f"Disease Name: {result.disease_name or 'Unknown'}")
            output.append(f"Disease Type: {result.disease_type}")
            output.append(f"Severity Level: {result.severity}")
            output.append(f"Confidence Score: {result.confidence}%")

            if result.symptoms:
                output.append("\nSymptoms Observed:")
                for symptom in result.symptoms:
                    output.append(f"  • {symptom}")

            if result.possible_causes:
                output.append("\nPossible Causes:")
                for cause in result.possible_causes:
                    output.append(f"  • {cause}")

            if result.treatment:
                output.append("\nRecommended Treatments:")
                for treatment in result.treatment:
                    output.append(f"  • {treatment}")

        output.append("=" * 60)
        return "\n".join(output)


def main():
    """Main execution function"""
    try:
        # Configuration
        IMAGE_PATH = "Media/brown-spot-4 (1).jpg"

        # Initialize detector
        detector = LeafDiseaseDetector()

        # Analyze image
        logger.info("Starting leaf disease detection analysis...")
        result = detector.analyze_leaf_image(IMAGE_PATH)

        # Display results
        print(detector.format_results(result))

        # Also print JSON for programmatic use
        print("\nJSON Output:")
        print(json.dumps(result.__dict__, indent=2))

    except Exception as e:
        logger.error(f"Application failed: {str(e)}")
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

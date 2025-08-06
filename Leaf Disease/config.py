"""
Configuration module for Leaf Disease Detection System
"""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class AppConfig:
    """Application configuration settings"""

    # API Configuration
    groq_api_key: str
    model_name: str = "meta-llama/llama-4-scout-17b-16e-instruct"
    model_temperature: float = 0.3
    max_completion_tokens: int = 1024

    # Logging Configuration
    log_level: str = "INFO"
    log_file: str = "disease_detection.log"

    # Analysis Configuration
    supported_formats: tuple = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

    @classmethod
    def from_env(cls) -> 'AppConfig':
        """Create configuration from environment variables"""
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY environment variable is required")

        return cls(
            groq_api_key=groq_api_key,
            model_name=os.getenv("MODEL_NAME", cls.model_name),
            model_temperature=float(
                os.getenv("MODEL_TEMPERATURE", cls.model_temperature)),
            max_completion_tokens=int(
                os.getenv("MAX_COMPLETION_TOKENS", cls.max_completion_tokens)),
            log_level=os.getenv("LOG_LEVEL", cls.log_level),
            log_file=os.getenv("LOG_FILE", cls.log_file)
        )

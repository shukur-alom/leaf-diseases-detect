"""
Configuration module for Leaf Disease Detection System.

This module provides centralized configuration management for the leaf disease
detection application. It handles API keys, model parameters, logging settings,
and other application-wide configurations through environment variables and
default values.

Classes:
    AppConfig: Main configuration dataclass containing all application settings

Usage:
    >>> config = AppConfig.from_env()
    >>> detector = LeafDiseaseDetector(api_key=config.groq_api_key)
"""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class AppConfig:
    """
    Application configuration settings for the Leaf Disease Detection System.

    This dataclass encapsulates all configuration parameters required for the
    application to function properly. It provides a centralized way to manage
    API credentials, model settings, logging configuration, and file format
    specifications.

    The configuration can be loaded from environment variables using the
    from_env() class method, which provides a convenient way to deploy the
    application with different settings across environments.

    Attributes:
        groq_api_key (str): API key for Groq AI services (required)
        model_name (str): Name of the AI model to use for analysis
        model_temperature (float): Temperature parameter for model response generation
        max_completion_tokens (int): Maximum tokens allowed in model responses
        log_level (str): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file (str): Path to the log file for application logging
        supported_formats (tuple): Tuple of supported image file extensions

    Example:
        >>> # Create config from environment variables
        >>> config = AppConfig.from_env()
        >>> 
        >>> # Create config with custom values
        >>> config = AppConfig(
        ...     groq_api_key="your-api-key",
        ...     model_temperature=0.5,
        ...     log_level="DEBUG"
        ... )
    """

    # API Configuration
    groq_api_key: str  # Required API key for Groq AI services
    model_name: str = "meta-llama/llama-4-scout-17b-16e-instruct"  # AI model identifier
    # Controls randomness in model responses (0.0-2.0)
    model_temperature: float = 0.3
    max_completion_tokens: int = 1024  # Maximum tokens in model responses

    # Logging Configuration
    log_level: str = "INFO"  # Logging verbosity level
    log_file: str = "disease_detection.log"  # Path to application log file

    # Analysis Configuration
    # Supported image formats
    supported_formats: tuple = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

    @classmethod
    def from_env(cls) -> 'AppConfig':
        """
        Create configuration instance from environment variables.

        This class method provides a convenient way to initialize the configuration
        by reading values from environment variables. It uses sensible defaults
        for optional parameters while requiring critical settings like API keys.

        Environment Variables:
            GROQ_API_KEY (required): API key for Groq AI services
            MODEL_NAME (optional): Override default AI model name
            MODEL_TEMPERATURE (optional): Override default model temperature
            MAX_COMPLETION_TOKENS (optional): Override default max tokens
            LOG_LEVEL (optional): Override default logging level
            LOG_FILE (optional): Override default log file path

        Returns:
            AppConfig: Configured instance with values from environment variables

        Raises:
            ValueError: If GROQ_API_KEY environment variable is not set

        Example:
            >>> import os
            >>> os.environ['GROQ_API_KEY'] = 'your-api-key'
            >>> os.environ['LOG_LEVEL'] = 'DEBUG'
            >>> config = AppConfig.from_env()
            >>> print(config.log_level)  # Output: DEBUG
        """
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

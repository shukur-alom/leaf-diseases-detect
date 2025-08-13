# Leaf Diseases Detect

A Python-based application for detecting leaf diseases from images. This project provides an API for image-based disease detection and includes utilities for configuration and testing.

## Features
- Detects leaf diseases from uploaded images
- API endpoint for predictions
- Configurable settings
- Includes sample images for testing

## Folder Structure
```
leaf-diseases-detect/
├── app.py                # Main API application
├── requirements.txt      # Python dependencies
├── test_api.py           # API test script
├── utils.py              # Utility functions
├── vercel.json           # Vercel deployment config
├── Leaf Disease/
│   ├── config.py         # Configuration settings
│   ├── main.py           # Core detection logic
│   └── __pycache__/
├── Media/
│   ├── brown-spot-4 (1).jpg
│   └── DanLeaf2.jpg      # Sample images
└── __pycache__/
```

## Setup
1. Clone the repository:
   ```powershell
   git clone <repo-url>
   cd leaf-diseases-detect
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Usage
- Run the API:
  ```powershell
  python app.py
  ```
- Test the API:
  ```powershell
  python test_api.py
  ```

## Deployment
- The project includes a `vercel.json` for deployment on Vercel.

## License
This project is licensed under the terms of the LICENSE file.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For questions or support, please contact the repository owner.

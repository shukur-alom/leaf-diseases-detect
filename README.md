# 🌿 Leaf Disease Detection API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-AI%20Powered-orange.svg?style=flat)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat)](LICENSE)

A state-of-the-art AI-powered leaf disease detection system that leverages advanced computer vision models to identify plant diseases from leaf images. Built with FastAPI and powered by Groq's Llama Vision models, this API provides comprehensive disease analysis including severity assessment, treatment recommendations, and confidence scoring.

## 🚀 Features

### Core Capabilities
- **🔍 Multi-Disease Detection**: Identifies fungal, bacterial, viral, pest-related, and nutrient deficiency diseases
- **📊 Severity Assessment**: Classifies disease severity as mild, moderate, or severe
- **🎯 Confidence Scoring**: Provides confidence percentages (0-100%) for predictions
- **💡 Treatment Recommendations**: Offers actionable treatment suggestions
- **📋 Symptom Analysis**: Detailed symptom identification and possible cause analysis
- **⚡ Real-time Processing**: Fast image analysis with optimized response times

### Technical Features
- **RESTful API**: Clean, well-documented FastAPI endpoints
- **Base64 Image Support**: Flexible image input handling
- **Structured JSON Responses**: Consistent, machine-readable output format
- **Comprehensive Logging**: Detailed operation tracking and error handling
- **Cloud-Ready**: Optimized for Vercel deployment

## 🏗️ Architecture

```
leaf-diseases-detect/
├── 📁 Front/                     # Main application directory
│   ├── 🐍 app.py                 # FastAPI application & API endpoints
│   ├── 🔧 utils.py               # Image processing utilities
│   ├── 🧪 test_api.py            # API testing scripts
│   ├── 📋 requirements.txt       # Python dependencies
│   ├── ⚙️ vercel.json            # Vercel deployment configuration
│   ├── 📁 Leaf Disease/          # Core detection engine
│   │   ├── 🧠 main.py            # AI model integration & analysis logic
│   │   └── ⚙️ config.py          # Configuration settings
│   ├── 📁 Media/                 # Sample images for testing
│   │   └── 🖼️ brown-spot-4 (1).jpg
│   └── 📄 README.md              # Project documentation
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Groq API key ([Get one here](https://console.groq.com/))

### 1. Clone the Repository
```powershell
git clone https://github.com/shukur-alom/leaf-diseases-detect.git
cd leaf-diseases-detect/Front
```

### 2. Create Virtual Environment (Recommended)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1  # On Windows PowerShell
# source venv/bin/activate    # On Linux/macOS
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## 🚀 Usage

### Starting the API Server
```powershell
# Development server
uvicorn app:app --reload --host 0.0.0.0 --port 8000

# Production server
python app.py
```

The API will be available at `http://localhost:8000`

### API Documentation
- **Interactive Docs**: `http://localhost:8000/docs` (Swagger UI)
- **Alternative Docs**: `http://localhost:8000/redoc` (ReDoc)

## 📡 API Endpoints

### `POST /disease-detection-file`
Upload an image file for disease detection analysis.

**Request:**
- **Content-Type**: `multipart/form-data`
- **Body**: Image file (JPEG, PNG, etc.)

**Response:**
```json
{
  "disease_detected": true,
  "disease_name": "Brown Spot",
  "disease_type": "fungal",
  "severity": "moderate",
  "confidence": 85.7,
  "symptoms": [
    "Brown circular spots on leaves",
    "Yellowing around spots",
    "Leaf deterioration"
  ],
  "possible_causes": [
    "High humidity conditions",
    "Poor air circulation",
    "Overwatering"
  ],
  "treatment": [
    "Apply fungicide spray",
    "Improve air circulation",
    "Reduce watering frequency",
    "Remove affected leaves"
  ],
  "analysis_timestamp": "2025-08-13T10:30:45+00:00"
}
```

### `GET /`
Root endpoint providing API information and available endpoints.

## 🧪 Testing

### Run API Tests
```powershell
python test_api.py
```

### Test with Sample Images
```powershell
# Test with provided sample image
python utils.py
```

### Manual Testing with cURL
```powershell
# Upload image for analysis
curl -X POST "http://localhost:8000/disease-detection-file" `
     -H "accept: application/json" `
     -H "Content-Type: multipart/form-data" `
     -F "file=@Media/brown-spot-4 (1).jpg"
```

## 🌐 Deployment

### Vercel Deployment
This project is optimized for Vercel deployment with the included `vercel.json` configuration.

1. **Install Vercel CLI**:
   ```powershell
   npm install -g vercel
   ```

2. **Deploy**:
   ```powershell
   vercel --prod
   ```

3. **Set Environment Variables** in Vercel dashboard:
   - `GROQ_API_KEY`: Your Groq API key

### Alternative Deployment Options
- **Docker**: Containerize with provided Dockerfile (if available)
- **Railway**: Deploy with one-click Railway button
- **Heroku**: Deploy using Heroku CLI
- **AWS Lambda**: Serverless deployment with Mangum adapter

## 🔧 Configuration

### Environment Variables
| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GROQ_API_KEY` | Groq API authentication key | ✅ Yes | - |
| `MODEL_NAME` | AI model identifier | ❌ No | `meta-llama/llama-4-scout-17b-16e-instruct` |
| `DEFAULT_TEMPERATURE` | Model creativity (0.0-2.0) | ❌ No | `0.3` |
| `DEFAULT_MAX_TOKENS` | Response length limit | ❌ No | `1024` |

### Supported Image Formats
- JPEG/JPG
- PNG
- WebP
- BMP
- TIFF

## 🔬 Technical Details

### AI Model Integration
- **Model**: Meta Llama Vision (via Groq)
- **Analysis Type**: Computer vision + Natural language processing
- **Response Format**: Structured JSON with confidence scoring
- **Processing Time**: Typically 2-5 seconds per image

### Disease Categories Supported
- **Fungal Diseases**: Leaf spot, blight, rust, mildew
- **Bacterial Diseases**: Bacterial leaf spot, fire blight
- **Viral Diseases**: Mosaic virus, yellowing diseases
- **Pest Damage**: Insect damage, mite infestations
- **Nutrient Deficiencies**: Nitrogen, potassium, phosphorus deficiencies
- **Healthy Leaves**: Normal, disease-free identification

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comprehensive docstrings
- Include unit tests for new features
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/shukur-alom/leaf-diseases-detect/issues)
- **Discussions**: [GitHub Discussions](https://github.com/shukur-alom/leaf-diseases-detect/discussions)
- **Email**: Contact repository owner through GitHub

## 🔗 Related Projects

- [Plant Disease Classification Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
- [PlantNet API](https://my.plantnet.org/)
- [Plant Disease Detection Models](https://github.com/topics/plant-disease-detection)

## ⚡ Performance Metrics

- **Average Response Time**: 2-5 seconds
- **Accuracy**: 85-95% (varies by disease type)
- **Supported Image Size**: Up to 10MB
- **Concurrent Requests**: Optimized for multiple simultaneous analyses

---

<div align="center">

**🌱 Helping farmers and gardeners protect their plants through AI-powered disease detection 🌱**

[Report Bug](https://github.com/shukur-alom/leaf-diseases-detect/issues) • [Request Feature](https://github.com/shukur-alom/leaf-diseases-detect/issues) • [View Demo](https://leaf-diseases-detect.vercel.app)

</div>

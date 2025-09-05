# GrowthZI API Documentation

This simple guide explains how to use the GrowthZI API.

## Getting Started

1. Import the `GrowthZI_API_Collection.postman_collection.json` file into Postman
2. Make sure the Flask server is running on port 8080
3. Try the example requests

## Available Endpoints

### 1. Resume Parser

**Endpoint**: `POST /api/portfolio`

Upload a resume file and get structured data.

**How to use**:
- Select a PDF or DOC file to upload
- Send the request
- View the structured data response

### 2. Text Translator

**Endpoint**: `POST /api/translate?target_lang=es`

Translate JSON content by adding language prefix to text.

**How to use**:
- Send JSON content in request body
- Set target_lang query parameter (es, fr, de, etc.)
- Get back the same JSON with text values prefixed

### 3. Price Calculator

**Endpoint**: `GET /api/pricing?country=JP`

Get product pricing for a specific country.

**How to use**:
- Set country code query parameter (US, JP, GB, etc.)
- Get pricing details in the appropriate currency

# Seperate Generator

## Overview
This project is designed to automate the generation of validation documents using advanced NLP techniques. It leverages BERT for text embedding, FAISS for similarity search, and a classifier to predict document types. The project includes a backend (Python) and a Streamlit-based frontend for user interaction.

## Features
- Upload and process validation documents
- Text preprocessing and embedding using BERT
- Similarity search with FAISS
- Document type prediction
- PDF export functionality
- Modular backend structure

## Project Structure
```
backend/
  ├── main.py                # Entry point for backend API
  ├── models/                # Data models
  ├── routers/               # API route definitions
  ├── services/              # Core logic and utilities
  └── tests/                 # Backend tests
frontend_streamlit.py        # Streamlit frontend app
docs/                        # Documentation and diagrams
```

## Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone https://github.com/prakhar-philips/URS_to_FRS.git
   cd URS_to_FRS
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r backend/requirements.txt
   ```
4. **Run the backend:**
   ```sh
   python backend/main.py
   ```
5. **Run the frontend:**
   ```sh
   streamlit run frontend_streamlit.py
   ```

## Usage
- Access the Streamlit app in your browser to upload and process documents.
- The backend API handles document parsing, embedding, similarity search, and classification.

## Documentation
- See the `docs/` folder for workflow diagrams and additional documentation.

## License
This project is licensed under the MIT License. 
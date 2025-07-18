# URS to FRS Converter

## Overview
This project automates the conversion of User Requirement Specifications (URS) into Functional Requirement Specifications (FRS) using advanced NLP techniques. It is designed to streamline the requirements engineering process by leveraging language models and similarity search to generate high-quality FRS documents from URS inputs.

## Features
- Upload and parse URS documents
- Extract and preprocess requirements
- Use BERT for text embedding
- Perform similarity search with FAISS
- Classify and map URS to FRS
- Export generated FRS as PDF
- Modular backend and Streamlit-based frontend

## Project Structure
```
backend/
  ├── main.py                # Backend API entry point
  ├── models/                # Data models for URS/FRS
  ├── routers/               # API route definitions
  ├── services/              # Core logic: parsing, generation, export
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
- Use the Streamlit app to upload URS documents and generate FRS outputs.
- The backend handles document parsing, embedding, similarity search, and FRS generation.
- Export the generated FRS as a PDF for documentation or review.

## Documentation
- See the `docs/` folder for workflow diagrams and additional documentation.

## License
This project is licensed under the MIT License. 
 AI Notes Summarizer

## Overview

AI Notes Summarizer is an AI-powered document summarization platform that enables users to upload PDF documents or provide text input to generate concise and meaningful summaries. The application utilizes *Local AI Inference using Ollama (Llama 3.2)* and optionally supports *BYOK (Bring Your Own Key) integration with Google Gemini API*.

The system follows a modular architecture that separates the user interface, document processing, business logic, and AI inference layers to ensure scalability and maintainability.

---

## High-Level Architecture

text
                 User
                   ↓
      AI Provider Selection Layer
     (Local AI / BYOK Support)
                   ↓
          Streamlit Interface
                   ↓
         Input Processing Layer
          (PDF / Text Input)
                   ↓
      Document Processing Module
                   ↓
           AI Inference Layer
      (Ollama or Gemini API)
                   ↓
          Summary Generation
                   ↓
                Results


---

## System Components

### 1. User Interface Layer

*Technology*

* Streamlit

*Responsibilities*

* Accept user input
* Upload PDF documents
* Receive direct text input
* Allow AI provider selection
* Display AI-generated summaries

*File*

* app.py

---

### 2. Document Processing Layer

*Technology*

* PyPDF2

*Responsibilities*

* Read uploaded PDF files
* Extract textual content
* Prepare extracted text for AI processing

*File*

* app.py

---

### 3. Text Processing Module

*Technology*

* NLTK

*Responsibilities*

* Tokenize extracted text
* Preprocess and clean textual data
* Prepare input for summarization models

*File*

* app.py

---

### 4. AI Summarization Module

*Responsibilities*

* Generate concise summaries
* Identify key information
* Reduce document length while preserving meaning
* Process both PDF and manually entered text

*File*

* app.py

---

### 5. AI Inference Layer

*Technology*

* Ollama (Local AI Inference)
* Google Gemini API (BYOK Support)

*Responsibilities*

* Runtime AI model selection
* Local document summarization using Ollama
* Cloud-based summarization using Gemini (optional)
* Natural Language Understanding
* AI-powered summary generation

*File*

* app.py

---

## Data Flow

text
                 User
                   ↓
      AI Provider Selection Layer
                   ↓
          Streamlit Interface
                   ↓
      PDF Upload / Text Input
                   ↓
      Document Processing Layer
                   ↓
           AI Inference Layer
      (Ollama / Gemini API)
                   ↓
         Summary Generation
                   ↓
                Results


---

## Security Considerations

The application follows a hybrid AI architecture supporting both *Local AI Inference* and *Bring Your Own Key (BYOK)*.

* Users may optionally provide their own Gemini API key.
* API keys are not permanently stored by the application.
* Uploaded PDF documents are processed temporarily during runtime.
* No permanent storage of user-uploaded documents or sensitive information is performed.
* Local AI processing through Ollama ensures enhanced privacy and offline capability.

---

## Scalability Considerations

Future versions may include:

* Multiple AI model providers
* Multi-language document summarization
* OCR support for scanned PDF files
* User authentication and profile management
* Summary download and export options
* Cloud deployment
* Analysis history and document management
* Advanced AI models for abstractive summarization

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Services

* Ollama (Local AI Inference)
* Google Gemini API (BYOK Support)

### Document Processing

* PyPDF2

### Natural Language Processing

* NLTK

### Dependency Management

* pip / uv

---

## Version

*AI Notes Summarizer v1.0*
*Hackathon 2 Prototype Architecture Documentation*
import os
import re
import json
from PyPDF2 import PdfReader
import docx

# Function to extract text from PDF and Word files
def extract_text_from_file(file_path):
    file_extension = os.path.splitext(file_path)[-1].lower()
    text = ""

    try:
        if file_extension == '.pdf':
            pdf_reader = PdfReader(file_path)
            for page in pdf_reader.pages:
                text += page.extract_text()
        elif file_extension in ('.doc', '.docx'):
            doc = docx.Document(file_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text
        else:
            print(f"Unsupported file format: {file_extension}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

    return text

# Function to extract structured data using regex
def extract_info(resume_text):
    phone_numbers = re.findall(r"\b\d{10}\b", resume_text)
    emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", resume_text)
    
    # Example: Add other patterns like address, education, etc.
    addresses = re.findall(r"\b\d{1,4}\s+\w+\s+\w+", resume_text)  # Basic address pattern; update as needed

    # Structure extracted data into JSON format
    extracted_data = {
        "name": "",  # Could use NLP libraries or patterns to extract a name
        "phoneNumbers": phone_numbers,
        "emails": emails,
        "addresses": addresses,
        "summary": "",  # Placeholder; could be extracted with more refined methods
        # Add more fields as necessary
    }

    return extracted_data

# Function to rank resumes based on keyword frequency
def rank_resume(resume_text, keyword):
    return resume_text.lower().count(keyword.lower())

# Directory with resumes and a keyword for ranking
resume_directory = r'C:\Users\durga\Downloads'
keyword = "Python"
ranked_resumes = []

# Process each resume file
for filename in os.listdir(resume_directory):
    if filename.endswith((".pdf", ".doc", ".docx")):
        print(f"Processing file: {filename}")
        
        resume_path = os.path.join(resume_directory, filename)
        resume_text = extract_text_from_file(resume_path)
        
        # Extract structured information and calculate score
        extracted_info = extract_info(resume_text)
        score = rank_resume(resume_text, keyword)
        
        # Store result with JSON format and score
        ranked_resumes.append({"json": extracted_info, "score": score})

# Sort resumes by score in descending order
ranked_resumes.sort(key=lambda x: x["score"], reverse=True)

# Display sorted resumes with their scores
for idx, resume in enumerate(ranked_resumes):
    print(f"Rank {idx+1} - Score: {resume['score']}")
    print(json.dumps(resume['json'], indent=4))

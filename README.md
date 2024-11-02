
# Resume Processor

This project automates the process of reading, extracting, and ranking resumes from a folder or cloud storage based on specific keywords. Resumes are converted to a structured JSON format to help identify the best candidates quickly and efficiently.

## Features

- **File Extraction**: Reads text from `.pdf`, `.doc`, and `.docx` resume files.
- **Data Extraction**: Parses essential details (e.g., phone numbers, emails) using regex.
- **Keyword Ranking**: Scores resumes based on the occurrence of specific keywords.
- **JSON Output**: Outputs structured data in JSON format for easy parsing and integration.

## Prerequisites

- Python 3.7 or above
- Libraries:
  - `PyPDF2`
  - `python-docx`

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/ResumeProcessor.git
   cd ResumeProcessor
   ```

2. **Install required packages**:

   ```bash
   pip install PyPDF2 python-docx
   ```

## Usage

1. **Set Resume Directory**:
   In the code, specify the directory containing the resume files by updating the `resume_directory` variable:

   ```python
   resume_directory = r'path\to\your\resumes'
   ```

2. **Run the Script**:

   Execute the script to process all resumes in the specified directory:

   ```bash
   python resu.py
   ```

3. **View Output**:
   The output JSON for each resume, along with its score based on keyword relevance, is printed in the terminal.

## Example Output

```json
{
  "name": "John Doe",
  "phoneNumbers": ["1234567890"],
  "emails": ["john.doe@example.com"],
  "addresses": ["123 Main St"],
  "summary": "",
  "education": [
    {
      "school": "XYZ University",
      "degree": "B.S.",
      "fieldOfStudy": "Computer Science",
      "startDate": "2015",
      "endDate": "2019"
    }
  ],
  "workExperience": [
    {
      "company": "ABC Corp",
      "position": "Software Engineer",
      "startDate": "2020",
      "endDate": "Present"
    }
  ],
  "skills": [
    {
      "name": "Python"
    }
  ],
  "certifications": [
    {
      "name": "AWS Certified Developer"
    }
  ]
}
```

## License

This project is licensed as "None".
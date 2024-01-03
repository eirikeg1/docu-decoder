# docu-decoder
_Work in progress_

Uses LLAMA2 and GPT to encode and decode documents. Stores document data in SUPABASE database.

# Installation
---

## Installing requirements
```pip install -r requirements.txt```

## Usage

This project can be run using `make`. The following rules are available:

`clean`:               `Delete all compiled Python files`
`create_environment`:  `Set up python interpreter environment` 
`data`:                `Make Dataset`
`lint`:                `Lint using flake8`
`requirements`:        `Install Python Dependencies`
`sync_data_from_s3`:   `Download Data from S3`
`sync_data_to_s3`:     `Upload Data to S3`
`test_environment`:    `Test python environment is setup correctly`

### Encoding the documents
In order to use the decoder you first need to add the documents to the `documents` folder. Give them descriptive names, if it is an article let this be the title and main author(s) last name. The documents should either be in `.txt`, `.pdf`, `.docx` or `.pptx`. 

Then run the following command:

```
python encode.py
```

This will encode the documents and save them in the `encoded_documents` folder. A description of each file will be at the start of this file along with keywords and search lookups. This can be edited if needed. It is usually better to have more keywords than less.

### Searching for documents



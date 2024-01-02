# docu-decoder
_Work in progress_

Uses LLAMA2 and GPT to encode and decode documents. Stores document data in SUPABASE database.

# Installation
---

## Installing requirements
```pip install -r requirements.txt```

## Usage

### Encoding the documents
In order to use the decoder you first need to add the documents to the `documents` folder. Give them descriptive names, if it is an article let this be the title and main author(s) last name. The documents should either be in `.txt`, `.pdf`, `.docx` or `.pptx`. 

Then run the following command:

```
python encode.py
```

This will encode the documents and save them in the `encoded_documents` folder. A description of each file will be at the start of this file along with keywords and search lookups. This can be edited if needed. It is usually better to have more keywords than less.

### Searching for documents
To search for documents run the following command:

```
python search.py
```


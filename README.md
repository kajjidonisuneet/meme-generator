## Meme Generator
A web and command line application that generates random or custom memes.
Deployed link https://suneet-meme-generator.herokuapp.com/

### Buit With
- Python
- Flask
- Pillow

### Prerequisites
Install all dependencies given in the `requirements.txt` file using `pip`.
```bash
pip install -r requirements.txt
```
In addition to the above download and install the `pdftotext` command line tool.

### Usage

#### Web Application
The application can be started by running the following command:
```bash
python app.py
```
#### Command Line Tool
The command line tool can be using the following command:
```
python3 meme --path <path_of_the_file> --body <quote_body> --author <quote_author>
```
#### Sample Output meme
![plot](_data/sample_out/sample_1.png)
![plot](_data/sample_out/sample_2.png)

## QuoteEngine Module
QuoteEngine module includes all the classes and methods that are used in the web and command line application.
QuoteEngine module reads quotes from various files and returns a collection of processed quotes.

### Dependencies
[pandas](https://pandas.pydata.org/) => This library is required to read and extract quotes from CSV files.
[python-docx](https://python-docx.readthedocs.io/en/latest/) => This library is required to read DOCX files.
[pdftotext](https://www.xpdfreader.com/pdftotext-man.html) => This is a command line application used to convert PDF to TXT files.

### Usage

Import the `Ingestor` class and use its class method `parse`.

### Models

#### QuoteModel
QuoteModel takes two parameters `body` and `author` of the quote. The `__repr__` method is defined for printing the value stored in this model in a human readable format.

#### Ingestor
Ingestor class calls all the other ingestor classes (CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor). Its `parse` method requires the file path as an argument and returns the suitable ingestor.

#### IngestorInterface
IngestorInterface class is an interface that is used as a base class for defining all other ingestors (CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor). It has a complete class method `verify` that checks if a file
extension is supported or not and a abstract class method `parse` used by the derived classes to parse files.

#### CSVIngestor
CSVIngestor overrides the `parse` method of IngestorInterface class to read CSV files, extract lines and return a collection of quotes object. It uses the `pandas` library to read CSVs.

#### DocxIngestor
DocxIngestor overrides the `parse` method of IngestorInterface class to read DOCX files, extract lines and return a collection of quotes objects. It uses the `python-docx` library to read DOCX files.

#### PDFIngestor
PDFIngestor overrides the `parse` method of IngestorInterface class to covert PDF files to TXT files. The converted text file is then parsed using the `TextIngestor`. PDF file is converted to TXT file using the `subprocess` library to call the `pdftotext` command line tool.

#### TextIngestor
TextIngestor overrides the `parse` method of IngestorInterface class to read TXT files, extract lines and return a collection of quotes object. It uses the in-built file reading methods to read text files.

## Meme Module
The Meme Module has all the class and required for generating memes.

### Dependencies
[pillow](https://pillow.readthedocs.io/en/stable/) => This library is used to manipulate and draw text over images.

### Usage
Import and use `MemeEngine` class by instantiating a variable with output director's path. Further, calling the `make_meme` method by providing image path, meme body and author.

### Models
#### MemeEngine
MemeEngine requires an output directory path as an argument while instantiating. The `make_meme` method creates the meme image and saves it in the provided output directory and returns a path to the created meme image. It uses the `pillow` library to manipulate image and draw text on it.

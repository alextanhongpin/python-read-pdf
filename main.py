import PyPDF2
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename = 'name.pdf'

with open(filename, 'rb') as f:
    pdfReader = PyPDF2.PdfFileReader(f)
    num_pages = pdfReader.numPages
    print(num_pages)

    count = 0
    text = ''
    while count < 2:
        page = pdfReader.getPage(count)
        count += 1
        text += page.extractText()
        print('got {} for page {}',  text, page)

    if text != '':
        text = text
    else:
        text = textract.process(filename, method='tesseract', language='eng')

    print(text)

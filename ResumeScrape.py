import io
import docx

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

def scrapeResume(file):
  if(file[(len(file) - 4):] == "docx"):
    document = docx.Document(file)
    docText = []
    for p in document.paragraphs:
      docText.append(p.text)
    return(" ".join(docText))

  elif(file[(len(file) - 3):] == "pdf"):
    manager = PDFResourceManager()
    handler = io.StringIO()
    converter = TextConverter(manager, handler)
    interpreter = PDFPageInterpreter(manager, converter)
 
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            interpreter.process_page(page)
        text = handler.getvalue()
    converter.close()
    handler.close()
 
    if text:
        return text
    else:
      return " "

  
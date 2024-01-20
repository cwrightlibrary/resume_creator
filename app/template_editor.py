from docx import Document
from os.path import abspath, dirname, join, realpath

block_basic_folder = abspath(join(dirname(__file__), "..", "document-templates", "blocky-basic"))
print(block_basic_folder)

doc = Document(join(block_basic_folder, "blocky-basic-resume.docx"))

_A_NAME = doc.paragraphs[0].text
_B_PHONE = doc.paragraphs[4].text

for paragraphs in range(len(doc.paragraphs)):
    print(paragraphs, doc.paragraphs[paragraphs].text)

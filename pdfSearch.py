import logging
import os
import shutil
import PyPDF2
import pyperclip

# https://drive.google.com/drive/folders/1iTaI_bIe47RtjtPg7FDWDPHYIB3G2fvo?usp=sharing

# Set the folder path where the PDF files are located
folderPath = r'C:\Documents\Mehrshad\User Intent Modeling\farshidi'
newFolderPath = r'C:\Documents\Mehrshad\User Intent Modeling'
# Set the search string
titleDict = {
    'Web service recommendation for mashup creation based on graph network':
    1017,
    'User intent prediction search engine system based on query analysis and image recognition technologies':1006,
    'DHSIRS':1010,
    'Recommendation model based on multi-grained interaction that fuses users’ dynamic interests':1020,
}
renameDict = {}
logging.getLogger('PyPDF2').setLevel(logging.CRITICAL)
# Loop through each file in the folder
for filename in os.listdir(folderPath):
    if filename.endswith('.pdf'):
        pdfReader = PyPDF2.PdfReader(
            open(os.path.join(folderPath, filename), 'rb'))
        pageObj = pdfReader.pages[0]
        txt = pageObj.extract_text().lower().replace(' ', '').replace('\n', '')
        for title, rowNum in titleDict.items():
            if title.lower().replace(' ', '').replace(
                    '\n', '') in txt and f'{rowNum}.pdf' not in os.listdir(
                        newFolderPath):
                print(f"found: {filename}")
                renameDict[
                    f'{folderPath}\{filename}'] = f'{newFolderPath}\{rowNum}.pdf'
                pyperclip.copy(filename[:-4])
for i, j in renameDict.items():
    shutil.move(i, j)
    # os.rename(i, j)
    print(f'{j} done!')
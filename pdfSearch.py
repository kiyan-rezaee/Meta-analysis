import os
import PyPDF2
import logging
import pyperclip

# https://drive.google.com/drive/folders/1iTaI_bIe47RtjtPg7FDWDPHYIB3G2fvo?usp=sharing

# Set the folder path where the PDF files are located
folderPath = r'C:\Documents\Mehrshad\User Intent Modeling\9th Part (1038-1068)'
# Set the search string
title = 'Conversational artificial intelligence in the AEC industry: A review of present status, challenges and opportunities'

logging.getLogger('PyPDF2').setLevel(logging.CRITICAL)
# Loop through each file in the folder
for filename in os.listdir(folderPath):
    if filename.endswith('.pdf'):
        # print(f"Checking {filename}...")
        pdfReader = PyPDF2.PdfReader(
            open(os.path.join(folderPath, filename), 'rb'))
        pageObj = pdfReader.pages[0]
        txt = pageObj.extract_text().lower().replace(' ', '').replace('\n', '')
        # print(txt)
        # print(title in txt)
        if title.lower().replace(' ', '').replace('\n', '') in txt:
            print(f"found:\n{filename}")
            pyperclip.copy(filename[:-4])
            exit()
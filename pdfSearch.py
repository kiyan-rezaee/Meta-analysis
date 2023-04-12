import os
import PyPDF2
import logging
import pyperclip

# https://drive.google.com/drive/folders/1iTaI_bIe47RtjtPg7FDWDPHYIB3G2fvo?usp=sharing

# Set the folder path where the PDF files are located
folderPath = r'C:\Documents\Mehrshad\User Intent Modeling\farshidi'
# Set the search string
title = 'Goal-oriented conditional variational autoencoders for proactive and knowledge-aware conversational recommender system'

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
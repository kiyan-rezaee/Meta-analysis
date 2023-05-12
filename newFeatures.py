import os
import PyPDF2
import pyperclip

# folder path
kiyan = r""
sara = r""
morteza = r""
amirhossein = r""
mehrshad = r"C:\Documents\Mehrshad\User Intent Modeling\Phase 4.1"

# change it to your name
active = mehrshad

# all pdfs in your entered path (sorted by name)
allpdf = True

# prints currently checking file
status = True

# list of pdf names (with or without .pdf)
filesList = ['file1', 'file2.pdf', '...']

# list of features
features = [["Rank"], ["Prediction", "predicting"], ["Behavior"], ["Template"],
            ["Term Weight"], ["Historical"], ["Topic Model"], ["Content"],
            ["Interact"], ["Filter"], ["Generative"], ["Activity"], ["Hybrid"],
            ["Occurrence"], ["Semantic"], ["Trained"], ["Context"], ["Query"],
            ["Text Similar"], ["Smooth"], ["Click"], ["Rule", "Tagging"],
            ["Language Diversity", "Multilingual"], ["Recommendation"],
            ["Dimensional", "Multidimensional"], ["Cluster"],
            ["Geographic", "location"], ["Network"], ["Pruning"], ["Rating"],
            ["Attentive"], ["End-To-End"], ["Data Modal",
                                            "Multimodal"], ["Query Suggest"],
            ["Represent"], ["Memory"], ["Flexibility", "Algorithm-Agnostic"],
            ["Pre-Trained"], ["Criteria"], ["Time"], ["Session"], ["Feedback"],
            ["Hierarchical"], ["Neighbor"], ["Search Trail"], ["Time-Aware"],
            ["Tree"], ["Opinion"], ["Density"], ["Sampling"],
            ["Relevance Feedback", "Positive Feedback"], ["Graph"], ["Image"],
            ["Query Scop"], ["Frequen"], ["Pattern"], ["Random"],
            ["Uncertain"], ["Query Refinement"], ["Constraint"],
            ["Segmentation"], ["Contextual Graph"], ["Structure"], ["Entit"],
            ["Tag Relevan"], ["Image Similar"], ["Graph Generat"],
            ["Image Recogn"], ["Transformer"], ["Multi-Task"],
            ["Parameter Estimat"], ["Anomal"], ["Dimensionality Reduction"],
            ["Feature Select"]]

print(f"Features count: {len(features)}")

if '\\' not in active[-2:]:
    active = active + r'\\'
if allpdf:
    filesList = []
    for file in os.listdir(active):
        if file.endswith('.pdf'):
            filesList.append(file)
output = []
for z in filesList:
    item = str(z)
    if '.pdf' not in item:
        item = item + '.pdf'
    if status:
        print(f'Checking: {item}')
    path = active + item
    try:
        pdfFileObj = open(path, 'rb')
    except:
        print(f'Error: {path} not found!')
        break
    features = dict(zip([str(i) for i in features], ['0'] * len(features)))
    featuresandquality = features
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    for i in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[i]
        page = pageObj.extract_text().lower()
        for j in featuresandquality.keys():
            if featuresandquality[j] == "1":
                continue
            for k in eval(j):
                if k.lower() in page:
                    featuresandquality[j] = '1'
                    break

    keys = []
    values = []

    for key, col in zip(featuresandquality, range(9999)):
        keys.append(key)
        values.append(featuresandquality[key])
    output.append('\t'.join(values))
pyperclip.copy('\n'.join(output))
print('\nCopied to your clipboard!\nPaste from "AZ" column!')
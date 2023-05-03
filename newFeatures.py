from Shortcut import shortcut
import PyPDF2
import pyperclip

# set your path here and change the name below
kiyan = r"C:\Users\kiyan\Desktop\research code\code\papers\1312.1611.pdf"
sara = r"C:\Users\saram\Desktop\10.pdf"
morteza = r"../unige_102091_attachment01.pdf"
features = [['Graph Gener'], ['Image recogn'], ['Transformer'],
            ['Multi-task', "Multitask"], ['Parameter estim'],
            ['Anomaly detect'], ['Dimensionality reduct'], ['Feature Select']]
output = []
print(f"Features count: {len(features)}")
ls = [1062]
t = ls[0]
for number in ls:
    if type(number) != int:
        output.append('')
        continue
    mehrshad = shortcut(number)
    pdfFileObj = open(mehrshad, 'rb')
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
    t = number
print(output)
pyperclip.copy('\n'.join(output))
print('\nCopied to clipboard!')
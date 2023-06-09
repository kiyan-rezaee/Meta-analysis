import PyPDF2
import re

address = r"C:\Documents\Mehrshad\User Intent Modeling\A survey of sentiment analysis in social media.pdf"

# The first boolean is for printing founded items
ls = {
    "phase 4": {
        "quality": [True, []],
        "feature": [True, []],
        "evaluation": [False, []],
        "model": [False, []]
    },
    "phase 4.1": {
        "quality": [True, []],
        "feature": [True, []],
        "evaluation": [False, []],
        "model": [False, []]
    }
}

with open('data.json', 'r') as file:
    data = eval(file.read())

with open(address, 'rb') as file:
    pdf = PyPDF2.PdfFileReader(file)
    numPage = pdf.getNumPages()
    for pageNum in range(numPage):
        pageObj = pdf.getPage(pageNum)
        pageText = pageObj.extractText()
        for a in ['phase 4', 'phase 4.1']:
            for b in ["quality", "feature", "evaluation", "model"]:
                searchList = data[a][b]
                for item in searchList:
                    if b in ['model', 'evaluation']:
                        if item in pageText:
                            # print(f'String "{item}" found on page {pageNum+1}')
                            ls[a][b][-1].append(item)
                            break
                    else:
                        if re.search(item, pageText, re.IGNORECASE):
                            print(f'String "{item}" found on page {pageNum+1}')
                            ls[a][b][-1].append(item)
                            break
print('---')

for phase in ls.keys():
    for category in ls[phase].keys():
        temp = set(ls[phase][category][-1])
        print(f"{phase} - {category} - count: {len(temp)}")
        if ls[phase][category][0]:
            print('\n'.join(temp))
        print('---')
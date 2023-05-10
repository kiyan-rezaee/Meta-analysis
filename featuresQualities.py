from Shortcut import shortcut
import PyPDF2
import pyperclip

# set your path here and change the name below
kiyan = r"C:\Users\kiyan\Desktop\research code\code\papers\1312.1611.pdf"
sara = r"C:\Users\saram\Desktop\10.pdf"
morteza = r"../unige_102091_attachment01.pdf"
mehrshad = shortcut(932)

# creating a pdf file object
pdfFileObj = open(mehrshad, 'rb')

quality = [
    # ['Performance'],
    # ['effectiveness'],
    # ['Diversity'],
    # ['stability'],
    # ['usefulness'],
    # ['Scalability'],
    # ['Recommendation performance'],
    # ['Satisfaction'],
    # ['Coverage'],
    # ['Resource Efficiency'],
    # ['robustness'],
    # ['Simplicity'],
    # ['reliability'],
    # ['validity'],
    # ['Novelty'],
    # ['Resource utilization'],
    # ['Computational cost'],
    # ['interpretability'],
    # ['retrieval performance'],
    # ['convergence'],
    # ['Recommendation Effectiveness'],
    # ['Transparency'],
    # ['Flexibility'],
    # ['informativeness'],
    # ['Recommendation Efficiency'],
    # ['Classification accuracy'],
    # ['predictability'],
    # ['classification performance'],
    # ['Appropriateness'],
    # ['Query accuracy'],
    # ['comparability'],
    # ['Readability'],
    # ['Retrieval accuracy'],
    # ['Clarification'],
    # ['Persuasiveness'],
    # ['Scrutability'],
    # ['Unexpectedness'],
    # ['memory efficiency'],
]
features = [["Ranking"], ["Prediction"], ["Session-based Recommendations"],
            ["graph generation"], ["Term Weighting"],
            ["Historical Data-Driven Recommendations"], ["Topic Modeling"],
            ["content-based Recommendations"], ["User Interaction"],
            ["Filtering"], ["Generative model"],
            ["Activity-Based Recommendations"], ["hybrid recommendation"],
            ["Co-Occurrence Analysis"], ["semantic analysis"], ["Model-based"],
            ["Context-aware Recommendations"], ["Query-based"],
            ["text similarity"], ["Smoothing"],
            ["Click-through Recommendations"], ["rule-based tagging"],
            ["Language Diversity"], ["Item recommendation"],
            ["Data Dimensionality"], ["Word cluster"],
            ["Geographic Support Recommendations"], ["network architecture"],
            ["Pruning"], ["Ratings Prediction"], ["Attentive"],
            ["end-to-end approach"], ["Data Modality"], ["Query Suggestions"],
            ["Representation learning"], ["Memory-based approaches"],
            ["Algorithm Flexibil"], ["Pre-trained Model"],
            ["Multi-criteria ratings"], ["time-based Recommendations"],
            ["Session-based"], ["Negative feedback"],
            ["hierarchical clustering"], ["neighborhood-based"],
            ["Search trail Recommendations"], ["time-aware Recommendations"],
            ["Tree Based"], ["opinion mining"], ["Density-Based"],
            ["Sampling based"], ["positive relevance feedback"],
            ["graph ranking"], ["image-based"], ["query scoping"],
            ["frequency-based"], ["Pattern-based"], ["randomization"],
            ["Prediction uncertainty"], ["Query refinement"],
            ["Constraint-based"], ["Query Segmentation"], ["contextual graph"],
            ["structure-based"], ["Entity Variability"], ["Tag relevance"],
            ["image similarity"], ["template-based"], ['Graph Gener'],
            ['Image recogn'], ['Transformer'], ['Multi-task', "Multitask"],
            ['Parameter estim'], ['Anomaly detect'], ['Dimensionality reduct'],
            ['Feature Select']]
print(f"Qualities count: {len(quality)}")
print(f"Features count: {len(features)}")
quality = dict(zip([str(i) for i in quality], ['0'] * len(quality)))
features = dict(zip([str(i) for i in features], ['0'] * len(features)))
featuresandquality = quality.copy()
featuresandquality.update(features)

# creating a pdf reader object
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


def excelCol(num):
    n = num + 14  # N
    result = ""
    while True:
        if n > 26:
            n, r = divmod(n - 1, 26)
            result = chr(r + ord('A')) + result
        else:
            return chr(n + ord('A') - 1) + result


print('\nQUALITIES:')
flag = True
for key, col in zip(featuresandquality, range(9999)):
    if col >= len(quality.keys()) and flag:
        flag = False
        print('\nFEATURES:')
    if featuresandquality[key] == '1':
        print(f"{excelCol(col)}: {eval(key)[0]}")
    keys.append(key)
    values.append(featuresandquality[key])

for i in range(len(quality)):
    if values[i] == "1":
        if i == list(quality.keys()).index("['Computational cost']"):
            values[i] = "Low"
        else:
            values[i] = "High"

pyperclip.copy('\t'.join(values))
print('\nCopied to clipboard!')

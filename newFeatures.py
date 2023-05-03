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
# features = [["Ranking"], ["Prediction"], ["Session-based Recommendations"],
#             ["graph generation"], ["Term Weighting"],
#             ["Historical Data-Driven Recommendations"], ["Topic Modeling"],
#             ["content-based Recommendations"], ["User Interaction"],
#             ["Filtering"], ["Generative model"],
#             ["Activity-Based Recommendations"], ["hybrid recommendation"],
#             ["Co-Occurrence Analysis"], ["semantic analysis"], ["Model-based"],
#             ["Context-aware Recommendations"], ["Query-based"],
#             ["text similarity"], ["Smoothing"],
#             ["Click-through Recommendations"], ["rule-based tagging"],
#             ["Language Diversity"], ["Item recommendation"],
#             ["Data Dimensionality"], ["Word cluster"],
#             ["Geographic Support Recommendations"], ["network architecture"],
#             ["Pruning"], ["Ratings Prediction"], ["Attentive"],
#             ["end-to-end approach"], ["Data Modality"], ["Query Suggestions"],
#             ["Representation learning"], ["Memory-based approaches"],
#             ["Algorithm Flexibil"], ["Pre-trained Model"],
#             ["Multi-criteria ratings"], ["time-based Recommendations"],
#             ["Session-based"], ["Negative feedback"],
#             ["hierarchical clustering"], ["neighborhood-based"],
#             ["Search trail Recommendations"], ["time-aware Recommendations"],
#             ["Tree Based"], ["opinion mining"], ["Density-Based"],
#             ["Sampling based"], ["positive relevance feedback"],
#             ["graph ranking"], ["image-based"], ["query scoping"],
#             ["frequency-based"], ["Pattern-based"], ["randomization"],
#             ["Prediction uncertainty"], ["Query refinement"],
#             ["Constraint-based"], ["Query Segmentation"], ["contextual graph"],
#             ["structure-based"], ["Entity Variability"], ["Tag relevance"],
#             ["image similarity"], ["template-based"], ['Graph Gener'],
#             ['Image recogn'], ['Transformer'], ['Multi-task', "Multitask"],
#             ['Parameter estim'], ['Anomaly detect'], ['Dimensionality reduct'],
#             ['Feature Select']]

output = []
missing = []
print(f"Features count: {len(features)}")
ls = [1017, 1020]
t = ls[0]
for number in ls:
    if type(number) != int:
        output.append('')
        continue
    try:
        mehrshad = shortcut(number)
        pdfFileObj = open(mehrshad, 'rb')
    except:
        print(number)
        missing.append(str(number))
        output.append('')
        break
        continue
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
if len(missing) != 0:
    print(f'Missing files: {"-".join(missing)}')
pyperclip.copy('\n'.join(output))
print('Copied to clipboard!')
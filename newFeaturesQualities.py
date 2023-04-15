from Shortcut import shortcut
import PyPDF2
import pyperclip

# set your path here and change the name below
kiyan = r"C:\Users\kiyan\Desktop\research code\code\papers\1312.1611.pdf"
sara = r"C:\Users\saram\Desktop\10.pdf"
morteza = r"../unige_102091_attachment01.pdf"
mehrshad = shortcut(1053)

# creating a pdf file object
pdfFileObj = open(mehrshad, 'rb')

quality = [
    ['Performance'],
    ['effectiveness'],
    ['Diversity'],
    ['stability'],
    ['usefulness'],
    ['Scalability'],
    ['Recommendation performance'],
    ['Satisfaction'],
    ['Coverage'],
    ['Resource Efficiency'],
    ['robustness'],
    ['Simplicity'],
    ['reliability'],
    ['validity'],
    ['Novelty'],
    ['Resource utilization'],
    ['Computational cost'],
    ['interpretability'],
    ['retrieval performance'],
    ['convergence'],
    ['Recommendation Effectiveness'],
    ['Transparency'],
    ['Flexibility'],
    ['informativeness'],
    ['Recommendation Efficiency'],
    ['Classification accuracy'],
    ['predictability'],
    ['classification performance'],
    ['Appropriateness'],
    ['Query accuracy'],
    ['comparability'],
    ['Readability'],
    ['Retrieval accuracy'],
    ['Clarification'],
    ['Persuasiveness'],
    ['Scrutability'],
    ['Unexpectedness'],
    ['memory efficiency'],
    #    ['Helpfulness'], ['Portability'], ['Aboutness'],
    #    ['run-time efficiency'], ['Low-cost deployability'],
    #    ['Segment accuracy'], ['Endurability'], ['Judgeability'],
    #    ['Representativeness']
]
features = [
    ['Ranking'],
    ['Prediction'],
    ['behavior-based', 'behavior based'],
    ['graph based', 'graph-based'],
    ['Term Weighting'],
    ['Historical data'],
    ['Topic Modeling'],
    ['content-based'],
    ['interactivity'],
    ['Filtering'],
    ['Generative model'],
    ['Activity-based'],
    ['hybrid recommendation'],
    ['co-occurrence'],
    ['semantic analysis'],
    ['Model-based'],
    ['Context-aware'],
    ['Query-based'],
    ['text similarity'],
    ['Smoothing'],
    ['Click-through'],
    ['rule-based tagging'],
    ['Multilingual'],
    ['Item recommendation'],
    ['Multidimensional'],
    ['Word cluster'],
    ['Location-based'],
    ['network architecture'],
    ['Pruning'],
    ['Ratings Prediction'],
    ['Attentive'],
    ['end-to-end approach'],
    ['Multimodal'],
    ['Query Suggestions'],
    ['Representation learning'],
    ['Memory-based approaches'],
    ['algorithm-agnostic'],
    ['Pre-trained Model'],
    ['Multi-criteria ratings'],
    ['time-based'],
    ['Session-based'],
    ['Negative feedback'],
    ['hierarchical clustering'],
    ['neighborhood-based'],
    ['Search trail'],
    ['time-aware'],
    ['Tree Based', 'Tree-Based'],
    ['opinion mining'],
    ['Density-Based'],
    ['Sampling based', 'Sampling-based'],
    ['positive relevance feedback'],
    ['graph ranking'],
    ['image-based'],
    ['query scoping'],
    ['frequency-based'],
    ['Pattern-based'],
    ['randomization'],
    ['Prediction uncertainty'],
    ['Query refinement'],
    ['Constraint-based'],
    ['Query Segmentation'],
    ['contextual graph'],
    ['structure-based'],
    ['multi-type entities'],
    ['Tag relevance'],
    ['image similarity'],
    ['template-based'],
    # ['Subjective Questions'],
    # ['Alleviating data sparsity'], ['Vertical-Intent'],
    # ['Identical queries'], ['reading level'], ['feature-oriented'],
    # ['probability-based'], ['Critiquing-based'], ['gradient-based'],
    # ['Relation extraction'], ['Vertical search engines'],
    # ['user-oriented topics'], ['time-oriented topics'],
    # ['Adaptive Weights'], ['Multi-granularity'],
    # ['Situational context'], ['Transfer learning'], ['Age Detection'],
    # ['name entity recognition'], ['underlying recommendation'],
    # ['conceptual map'], ['Short-term history'], ['Long-term history'],
    # ['emotion-aware']
]
print(f"Qualities count: {len(quality)}")
print(f"Features count: {len(features)}")
quality = dict(zip([str(i) for i in quality], [""] * len(quality)))
features = dict(zip([str(i) for i in features], [""] * len(features)))
featuresandquality = quality.copy()
featuresandquality.update(features)

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

for i in range(len(pdfReader.pages)):
    pageObj = pdfReader.pages[i]
    page = pageObj.extract_text().lower()
    for j in featuresandquality.keys():
        if featuresandquality[j] == "X":
            continue
        for k in eval(j):
            if k.lower() in page:
                featuresandquality[j] = 'X'
                break

keys = []
values = []


def excelCol(num):
    n = num + 14
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
    if featuresandquality[key] == 'X':
        print(f"{excelCol(col)}: {eval(key)[0]}")
    keys.append(key)
    values.append(featuresandquality[key])

for i in range(len(quality)):
    if values[i] == "X":
        if i == list(quality.keys()).index("['Computational cost']"):
            values[i] = "Low"
        else:
            values[i] = "High"

pyperclip.copy('\t'.join(values))
print('\nCopied to clipboard!')

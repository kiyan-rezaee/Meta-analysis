from optparse import Values
from Shortcut import shortcut
import pandas as pd
import PyPDF2
import pyperclip

# set your path here and change the name below
kiyan = r"C:\Users\kiyan\Desktop\research code\code\papers\1611.03971.pdf"
sara = r"C:\Users\saram\Desktop\3.pdf"
morteza = r"../Community_aware_user_profile_enrichment.pdf"
mehrshad = shortcut(813)

# creating a pdf file object
pdfFileObj = open(sara, 'rb')

quality = [
    ["Performance"],
    ["Recommendation performance"],
    ["Resource Efficiency", "Efficiency"],
    ["Resource utilization"],
    ["stability", "stable"],
    ["interpretability"],
    ["Scalability"],
    ["effectiveness"],
    ["Recommendation Effectiveness"],
    ["Computational cost"],
    ["Recommendation Efficiency"],
    ["Explainability"],
    ["Prediction uncertainty"],
    ["flexibility"],
    ["competitive"],
    ["usefulness"],
    ["Jointly learning"],
    ["informativeness"],
    ["validity"],
    ["reliability"],
    ["comparability"],
    ["Retrieval accuracy"],
    ["Search quality"],
    ["specificity"],
    ["interactivity", "interaction"],
    ["Predictability"],
    ["diversity", "diverse", "diversify"],
    ["randomization"],
    ["Satisfaction"],
    ["Persuasiveness"],
    ["Transparency"],
    ["Scrutab"],
    ["latency"],
    ["Low-cost deployability"],
    ["simplicity"],
    ["Extending access"],
    ["classification performance"],
    ["Classification accuracy"],
    ["Segment accuracy"],
    ["Query accuracy"],
    ["Novelty"],
    ["Portability"],
    ["retrieval performance"],
    ["familiarity"],
    ["Felt Involvement"],
    ["Focused Attention"],
    ["Perceived Usability"],
    ["Endurability"],
    ["Aboutness"],
    ["Coverage"],
    ["Appropriateness"],
    ["run-time efficiency", "runtime efficiency"],
    ["Unexpectedness"],
    ["Clarification"],
    ["scrutability"],
    ["memory-efficient", "memory efficient", "memory efficiency", "memory-efficiency"],
    ["robustness"],
    ["convergence", "convergent"],
]
features = [
    ["Text based", "Text-based"],
    ["Rank"],
    ["Multi-criteria ratings"],
    ["Single ratings"],
    ["multi-type entities"],
    ["Prediction", "predict"],
    ["Multi lingual", "Multi lingual", "Multi-lingual", "Multilingual"],
    ["Historical data", "data history", "search histories", "history"],
    ["Filter"],
    ["behavior"],
    ["graph based", "graph-based", "graph"],
    ["relevance-based", "relevant"],
    ["Community Question Answering"],
    ["Unlabeled data"],
    ["Objective Questions"],
    ["Clarifying Question"],
    ["Subjective Questions"],
    ["Item recommendation"],
    ["Pre-trained Model"],
    ["Vertical search engines"],
    ["Text similarity", "text-similarity"],
    ["colour similarity", "color similarity"],
    ["Topic similarity", "Topic-similarity"],
    ["Rating behaviors"],
    ["Topic Model"],
    ["user-oriented topics"],
    ["time-oriented topics"],
    ["data sparseness"],
    ["Language model"],
    ["Context-aware", "Context aware"],
    ["asynchronous training"],
    ["network architecture"],
    ["optimization perspective"],
    ["feature perspective"],
    ["generative"],
    ["machine reading comprehension"],
    ["Quality control"],
    ["query scoping"],
    ["colour representation", "color representation"],
    ["co-occurrence"],
    ["Adaptive Weights"],
    ["Smoothing"],
    ["Social Questions"],
    ["Term Frequency"],
    ["Sampling based"],
    ["Query-based"],
    ["lexical items"],
    ["sponsored search"],
    ["navigational"],
    ["informational"],
    ["transactional"],
    ["Alleviating data sparsity"],
    ["Heuristic", "Ranking Heuristic"],
    ["query refinement"],
    ["Partitional"],
    ["Density-Based", "Density Based"],
    ["Pruning"],
    ["Negative feedback"],
    ["topic coverage"],
    ["search goal", "search task"],
    ["Search trail"],
    ["labeled data"],
    ["commercial queries"],
    ["Query Suggestions"],
    ["Empirically"],
    ["Weight"],
    ["Query privacy", "Query-privacy"],
    ["sophisticated"],
    ["tag relevan", "tag-relevan"],
    ["Query Segmentation"],
    ["name entity recognition"],
    ["part-of-speech", "part of speech"],
    ["word cluster", "word-cluster"],
    ["click through", "click-through"],
    ["vertical intent", "vertical-intent"],
    ["image similarity"],
    ["geolocation"],
    ["end-to-end"],
    ["similarity computation", "similarity-computation"],
    ["ambiguous queries"],
    ["Simulation-based"],
    ["Semantic interpretation"],
    ["Query independent", "Query independent", "Query independence"],
    ["stepwise"],
    ["time-based"],
    ["Semantic similarity", "Semantic-similarity"],
    ["tag-based", "tagbased", "tag based"],
    ["content-based", "content based"],
    ["algorithm-independent"],
    ["agnostic"],
    ["domain-independent"],
    ["underlying recommendation"],
    ["Rule-based Template Completion"],
    ["Modification", "Query Modifications"],
    ["Identical queries"],
    ["Query Overlap"],
    ["statistical methods"],
    ["contextual graph", "contextual diagram"],
    ["matrix factorization"],
    ["conceptual map"],
    ["tail queries"],
    ["TEXTUAL SIMILARITY"],
    ["Multidimensional", "Multi-dimensional"],
    ["Activity"],
    ["Location-based", "Location base"],
    ["Ontology"],
    ["Logic-based", "Logic based", "logical"],
    ["reading level"],
    ["intuition"],
    ["trust-based", "trust based"],
    ["rule based", "rule-based", "rules based", "rules-based"],
    ["statistical tag"],
    ["principle component analysis"],
    ["keyword based", "keyword-based"],
    ["retrieval-based", "retrieval based"],
    ["hashtag analys"],
    ["semantic analysis"],
    ["data-intensive", "data intensive"],
    ["feature-orient", "feature orient"],
    ["graph ranking", "graph-ranking"],
    ["neighborhood-based", "neighborhood based"],
    ["feature weighting", "feature-weighting"],
    ["query expansion"],
    ["Lexicon-Based", "Lexicon Based"],
    ["pseudo-relevance feedback"],
    ["Content-Based Filtering", "content based filtering"],
    ["Recommendation based On Typicality"],
    ["Model-based", "model based"],
    ["Memory-based", "memory based"],
    ["Item similarity", "Item-similarity", "Item to Item Similarity"],
    ["Multi granularity", "Multi-granularity", "Multigranularity"],
    ["Interaction-focused", "Interaction focused"],
    ["Short-term history"],
    ["Long-term history"],
    ["Situational context"],
    ["Query split"],
    ["Document split"],
    ["Joint split"],
    ["Inverse Document Frequency"],
    [
        "Ratings Prediction", "Ratings-Prediction", "Rating Prediction",
        "Rating-Prediction"
    ],
    ["tensor factorization", "tensor-factorization"],
    ["frequency based", "frequency-based"],
    ["Sequence labeling"],
    ["Utility-based", "Utility based"],
    ["goal based", "goal-based"],
    ["image-based", "image-aware"],
    ["Representation learning"],
    ["hybrid"],
    ["query rewriting", "query-rewriting"],
    ["probability-based", "probability based"],
    ["semantic-based", "semantics-based"],
    ["spatiotemporal-aware", "spatiotemporal aware"],
    ["Pattern-based"],
    ["region-rating"],
    ["evolutionary"],
    ["hierarchical cluster"],
    ["emotion-aware", "emotion-base"],
    ["Incremental Update"],
    ["attentive", "attention mechanism", "neural attention"],
    ["preference aggregation"],
    ["VISUALLY-AWARE", "VISUALLY AWARE", "VISUAL-AWARE", "visual aware"],
    ["score aggregation"],
    ["Rating-based"],
    ["Case-based"],
    ["Knowledge-based"],
    ["Critiquing-based"],
    ["Personality-based"],
    ["Constraint-based"],
    ["structure-based"],
    ["template-based"],
    ["Semantic Graph-Based"],
    ["Tree Based", "Tree-Based"],
    ["Multimodal", "Multi modal", "Multi-modal"],
    ["chunk-based", "Chunking"],
    ["Item diversified", "diversification"],
    ["auto-suggest"],
    ["multi-objective", "multi objective"],
    ["gradient-based"],
    ["time-aware"],
    ["sequence-aware"],
    ["Query extraction"],
    ["Gender Detection"],
    ["database compression"],
    ["Stemming"],
    ["lemmatization", 'Lemmatisation'],
    ["word embedding"],
    ["Age Detection"],
]
print(f"Qualities count: {len(quality)}")
print(f"Features count: {len(features)}")
quality = dict(
    zip([str(i) for i in quality], [""] * len(quality)))
features = dict(
    zip([str(i) for i in features], [""] * len(features)))
featuresandquality = quality.copy()
featuresandquality.update(features)

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    page = pageObj.extractText().lower()
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
    if col > len(quality.keys()) and flag:
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

# importing required modules
from optparse import Values
import pandas as pd
import PyPDF2

# creating a pdf file object
pdfFileObj = open(
    r"C:\Documents\Mehrshad\User Intent Modeling\Context-aware ranking in web search.pdf",
    'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

quality = {
    '["Performance"]': "",
    '["Recommendation performance"]': "",
    '["Resource Efficiency"]': "",
    '["Resource utilization"]': "",
    '["stability", "stable"]': "",
    '["interpretability"]': "",
    '["Scalability"]': "",
    '["effectiveness"]': "",
    '["Recommendation Effectiveness"]': "",
    '["Computational cost"]': "",
    '["Recommendation Efficiency"]': "",
    '["Explainability", "interpretability"]': "",
    '["Prediction uncertainty"]': "",
    '["Flexibility"]': "",
    '["competitive"]': "",
    '["usefulness"]': "",
    '["Jointly learning"]': "",
    '["informativeness"]': "",
    '["validity"]': "",
    '["reliability"]': "",
    '["comparability"]': "",
    '["Retrieval accuracy"]': "",
    '["Search quality"]': "",
    '["specificity"]': "",
    '["robustness"]': "",
}
features = {
    '["Text based", "Text-based"]': "",
    '["Rank"]': "",
    '["Multi-criteria ratings"]': "",
    '["Single ratings"]': "",
    '["multi-type entities"]': "",
    '["Prediction", "predict"]': "",
    '["Multi lingual", "Multi lingual", "Multi-lingual"]': "",
    '["Historical data", "data history", "search histories", "history"]': "",
    '["Filter"]': "",
    '["behavior"]': "",
    '["graph based","graph-based"]': "",
    '["relevance-based", "relevant"]': "",
    '["Community Question Answering"]': "",
    '["Unlabeled data"]': "",
    '["Objective Questions"]': "",
    '["Clarifying Question"]': "",
    '["Subjective Questions"]': "",
    '["Item recommendation"]': "",
    '["Pre-trained Model"]': "",
    '["Vertical search engines"]': "",
    '["Text similarity"]': "",
    '["colour similarity","color similarity"]': "",
    '["Topic similarity"]': "",
    '["Rating behaviors"]': "",
    '["Topic Model"]': "",
    '["user-oriented topics"]': "",
    '["time-oriented topics"]': "",
    '["data sparseness"]': "",
    '["Language model"]': "",
    '["Context-aware","Context aware"]': "",
    '["asynchronous training"]': "",
    '["network architecture"]': "",
    '["optimization perspective"]': "",
    '["feature perspective"]': "",
    '["generative"]': "",
    '["machine reading comprehension"]': "",
    '["Quality control"]': "",
    '["query scoping"]': "",
    '["colour representation","color representation"]': "",
    '["co-occurrence"]': "",
    '["Adaptive Weights"]': "",
    '["Smoothing"]': "",
    '["Social Questions"]': "",
    '["Term Frequency"]': "",
    '["Sampling based"]': "",
    '["Query-based"]': "",
    '["lexical items"]': "",
    '["sponsored search"]': "",
    '["navigational"]': "",
    '["informational"]': "",
    '["transactional"]': "",
    '["Alleviating data sparsity"]': "",
    '["Heuristic"]': "",
    '["query refinement"]': "",
    '["Partitional"]': "",
    '["Density-Based","Density Based"]': "",
    '["Pruning"]': "",
    '["Negative feedback"]': "",
    '["topic coverage"]': "",
    '["search goal","search task"]': "",
    '["Search trail"]': "",
    '["labeled data"]': "",
    '["commercial queries"]': "",
    '["Query Suggestions"]': "",
    '["Empirically"]': "",
    '["Term Weight","Weighting term","Term-Weight"]': "",
    '["Query privacy","Query-privacy"]': "",
    '["Inverse Document Frequency"]': ""
}
print(f"qualities count: {len(quality)}")
print(f"features count: {len(features)}")
featuresandquality = quality.copy()
featuresandquality.update(features)

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


for key,col in zip(featuresandquality,range(9999)):
    if featuresandquality[key] == 'X':
        print(excelCol(col),key)
    keys.append(key)
    values.append(featuresandquality[key])

for i in range(len(quality)):
    if values[i] == "X":
        values[i] = "High"

# pdfFileObj.close()

df = pd.DataFrame()

for i in range(len(keys)):
    df[keys[i]] = 0

df.loc[len(df)] = values

# print(df)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('features-quality.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.close()

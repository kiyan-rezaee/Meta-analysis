# importing required modules
from optparse import Values
import PyPDF2
 
# creating a pdf file object
pdfFileObj = open(r'C:\Users\kiyan\Desktop\research code\code\papers\7.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
featuresandquality = {
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
    '["Flexibility"]' : "",
    '["competitive"]': "",
    '["usefulness"]': "",
    '["Jointly learning"]': "",
    '["informativeness"]' : "",
    '["validity"]' : "",
    '["robustness"]': "",
    #features
    '["Text based", "Text-based"]': "",
    '["Rank"]': "",
    '["Multi-criteria ratings"]': "",
    '["Single ratings"]': "",
    '["multi-type entities"]': "",
    '["Prediction", "predict"]': "",
    '["Multi lingual", "Multi lingual", "Multi-lingual"]': "",
    '["Historical data", "data history", "search histories"]': "",
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
    '["Vertical search engines"]' : "", 
    '["Text similarity"]' : "" ,
    '["colour similarity"]' : "", 
    '["Topic similarity"]' : "" ,
    '["Rating behaviors"]' : "" ,
    '["Topic Model"]' : "" ,
    '["user-oriented topics"]' : "", 
    '["time-oriented topics"]' : "" ,
    '["data sparseness"]' : "" ,
    '["Language model"]' : "" ,
    '["Context-aware"]' : "" ,
    '["asynchronous training"]': "",
    '["network architecture"]': "",
    '["optimization perspective"]': "",
    '["feature perspective"]' : "" ,
    '["generative"]': "",
    '["machine reading comprehension"]': "",
    '["Quality control"]': "",
    '["query scoping"]': "",
    '["colour representation"]': "",
    '["co-occurrence"]': "",
    '["Adaptive Weights"]':"",
    '["Smoothing"]':"",
    '["Social Questions"]': "",
    '["Term Frequency"]': "",
    '["Sampling based"]':"",
    '["Query-based"]': "",	
    '["lexical items"]' : "", 
    '["Inverse Document Frequency"]': ""
}

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

for key in featuresandquality:
    keys.append(key)
    values.append(featuresandquality[key]) 

for i in range(20):
    if values[i] == "X":
        values[i] = "High"

# pdfFileObj.close()
print(len(values))

import pandas as pd

# dataframe Name and Age columns
df = pd.DataFrame()

for i in range(len(keys)):
    df[keys[i]] = 0


df.loc[len(df)] = values

print(df)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.close()
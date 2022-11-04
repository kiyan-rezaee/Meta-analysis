models = [
    'HSG', 'DTW', 'PMI', 'Pagerank', 'NER', 'PPV', 'Log Analysis',
    'query relaxation', 'DCD', 'CIAP-LDA', 'CIAP-LDAC', 'LDAC', 'CDAP', 'HMM',
    'CRF', 'CKNN', 'KL', 'TA', 'TF-IDF', 'KNN', 'rPMF', 'auxTransfer',
    'crossIntegration', 'Foster', 'SR-GNN', 'NISER+', 'SGNN-HN', 'LESSR',
    'SHARE', 'GC-SAN', 'Item-KNN', 'ISP', 'KBV', 'HFT', 'SGD', 'LFM', 'SM',
    'FSM', 'RBM', 'AutoRec', 'BTM', 'Gibbs sampling', 'DQN', 'MR-BPR', 'BPR',
    'WMF', 'SLIM', 'HLM', 'PLSA', 'NowcastIndi', 'BoostedTree', 'MF', 'PMF',
    'TA-FPMC', 'TD', 'CD', 'FPMC', 'ISWE', 'DT', 'BatchRank', 'CascadeUCB1',
    'CascadeKL-UCB', 'RankedExp3', 'DPG', 'CDL', 'CKE', 'VBPR', 'CFN', 'DBN',
    'KNRM', 'Conv-KNRM', 'SLTB', 'HRNN', 'PTM', 'PSGAN', 'MDPRank', 'RLPer',
    'NARM', 'GRU4Rec', 'upper confidence bound', 'positive relevance feedback',
    'thompson sampling', 'HIN', 'causal disentanglement model',
    'causal intervention', 'standard TREC collections',
    'negative  relevance feedback', 'Kullback–Leibler divergence',
    'Probabilistic Latent Semantic Analysis', 'Skip-gram', 'SVM', 'AcTS',
    'LR-FC', 'NNID-ZP', 'NNID-FC', 'NSS', 'FRL', 'UIN', 'FEM', 'HIEM', 'MLM',
    'BERT4Rec', 'S3-Rec', 'Transfer learning ', 'EM', 'BERT', 'mean-pooling',
    'self-attention', 'Max-pooling', 'MMR', 'FCTH', 'THREAD & POST', 'LDA',
    'HEM', 'ZAM', 'DREM', 'CTR', 'Levenshtein distance',
    'multi-view preference mapper', 'user-centric modeling', 'BM25',
    'result types', 'LambdaRank', 'DSSM', 'DRMM', 'K-NRM', 'CDSSM',
    'LambdaMART', 'RankNet', 'RankSVM', 'QCM', 'LightFM', 'ALS', 'CF', 'LR',
    'PNN', 'Deep&Cross', 'xDeepFM', 'FmFM', 'Distill',
    'Query-question Matching', 'Loss Function', 'pseudo-labels', 'k-means',
    'Conv-KRNM', 'GraphConfRec', 'DARWR', 'DAKATZ', 'CNAVER', 'DDTCDR', 'HAN',
    'few-shot learning', 'Siamese Network', 'R2D2', 'LSTM', 'GNNs', 'GPT-3',
    'DisSig', 'TLGNN', 'HyperGAT', 'NNID', 'Modeller Intention Detection',
    'Model Validation', 'Intention to Modelling Specification Mapping',
    'TextCNN', 'KBRD', 'COLING20', 'KGSF', 'CR-Walker', 'CRFR', 'DNN', 'uDin',
    'NCF', 'KG-based', 'LinUCB', 'ConUCB', 'GBFM', 'HOFMs', 'DeepFM',
    'AutoFIS', 'MHA', 'NFM', 'DSIN', 'AFM', 'Temporal Convolutional Network',
    'SimNet', 'FINet', 'WordNet-based', 'FM', 'Wide&Deep', 'AutoInt', 'AFN',
    'PLM', 'QDM', 'MAUT', 'AllenNLP', 'DHP', 'Max Category', 'MLP ', 'GBDT',
    'XGBoost', 'icsiboost', 'IGNet', 'Logistic Regression', 'Naive Bayes',
    'Bubble filters', 'Result Rank', 'Dwell Time', 'Re-ranking',
    'Query filtering', 'CTW', 'DCM', 'FCM', 'DAM', 'TransRec', 'GRU4Rec+',
    'T-LSTM', 'QL', 'RM3', 'ERM', 'SDM', 'BERT-NeuQS', 'LRS', 'MC', 'LOF',
    'LMCL', 'BiLSTM', 'SVD++', 'CASER', 'DIEN', 'RUM', 'SHAN', 'NeuMF',
    'Markov', 'FOT', 'SI-Gamma', 'SI-Beta', 'MI-Purchase and MI-Explore',
    'TRLM', 'BOW', 'Multipartite graph', 'CMF', 'CDAC', 'NMIR', 'BART', 'EAR',
    'CRM', 'SasRec', 'GRU', 'GPT-2', 'RLC', 'LEAM', 'Fast Text', 'ER',
    'Micros', 'Macros', 'TextGCN', 'PTE', 'LSA', 'PG', 'RSA', 'ABS', 'JRE',
    'DLA', 'NMF', 'ConvMF', 'DeepCoNN', 'SAT', 'Att2Seq', 'ResNet', 'QRFA',
    'CIR6', 'MDP', 'AEM', 'TEM', 'LSE', 'PPWE', 'PWEBA', 'UserKNN', 'TOP',
    'HRM', 'HTMM', 'RANDOM', 'MCoC', 'MART', 'SERP', 'Rocchio', 'Perturbation',
    'SingleNeg', 'MultiNeg', 'GPR'
]

ls = ['' for i in range(len(models))]
models = dict(zip(models, ls))
# importing required modules
from optparse import Values
import PyPDF2

# creating a pdf file object

pdfFileObj = open(
    "../sp0771-giannopoulosPS2.pdf",
    'rb')

# creating a pdf reader object

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

for i in range(pdfReader.numPages):

    pageObj = pdfReader.getPage(i)

    page = pageObj.extractText()

    for j in models.keys():

        if j in page:
            models[j] = 'X'

keys = []

values = []

# print(models)
print({k: v for k, v in models.items() if v == "X"})
exit()
for key in models:
    keys.append(key)
    values.append(models[key])

for i in range(19):

    if values[i] == "X":

        values[i] = "High"

# pdfFileObj.close()

import pandas as pd

# dataframe Name and Age columns

df = pd.DataFrame()

for i in range(len(keys)):

    df[keys[i]] = 0

df.loc[len(df)] = values

print(df)

# Create a Pandas Excel writer using XlsxWriter as the engine.

writer = pd.ExcelWriter('models.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.

df.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.

writer.close()

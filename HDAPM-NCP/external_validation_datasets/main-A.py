from consistency_projection import NSP
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score
import warnings
warnings.filterwarnings("ignore")

df_dis = pd.read_csv(r"../data/disease_kernel/disease_id.csv", header=None, names=['id', 'DiseaseId'],engine="python")
df_herb = pd.read_csv(r"../data/herb_kernel/herb_id.csv", header=None, names=['id', 'HerbId'],engine="python")
df_dis.set_index('DiseaseId', inplace=True)
df_herb.set_index('HerbId', inplace=True)
di_herb=np.loadtxt(r"../data/disease_herb/disease_herb01.txt", dtype=int,delimiter=',')
d1=np.loadtxt(r"../data/disease_kernel/disease_target.txt", dtype=float, delimiter=',')
d2=np.loadtxt(r"../data/disease_kernel/disease_ingredients.txt", dtype=float, delimiter=',')
d3=np.loadtxt(r"../data/disease_kernel/disease_ingredients_ref.txt", dtype=float, delimiter=',')
d4=np.loadtxt(r"../data/disease_kernel/disease_similarty_kernel.txt", dtype=float, delimiter=',')

d501=np.loadtxt(r"../data_cross_verification/cross_verification1/guass_dis-1.txt", dtype=float, delimiter=',')
d502=np.loadtxt(r"../data_cross_verification/cross_verification2/guass_dis-2.txt", dtype=float, delimiter=',')
d503=np.loadtxt(r"../data_cross_verification/cross_verification3/guass_dis-3.txt", dtype=float, delimiter=',')
d504=np.loadtxt(r"../data_cross_verification/cross_verification4/guass_dis-4.txt", dtype=float, delimiter=',')
d505=np.loadtxt(r"../data_cross_verification/cross_verification5/guass_dis-5.txt", dtype=float, delimiter=',')

h1=np.loadtxt(r"../data/herb_kernel/herb_target.txt", dtype=float, delimiter=',')
h2=np.loadtxt(r"../data/herb_kernel/herb_go_enrichment.txt", dtype=float, delimiter=',')
h3=np.loadtxt(r"../data/herb_kernel/herb_ingredient.txt", dtype=float, delimiter=',')
h4=np.loadtxt(r"../data/herb_kernel/herb_KEGG_enrichment.txt", dtype=float, delimiter=',')
h5=np.loadtxt(r"../data/herb_kernel/herb_Gene_Targets.txt", dtype=float, delimiter=',')

h601=np.loadtxt(r"../data_cross_verification/cross_verification1/guass_herb-1.txt", dtype=float, delimiter=',')
h602=np.loadtxt(r"../data_cross_verification/cross_verification2/guass_herb-2.txt", dtype=float, delimiter=',')
h603=np.loadtxt(r"../data_cross_verification/cross_verification3/guass_herb-3.txt", dtype=float, delimiter=',')
h604=np.loadtxt(r"../data_cross_verification/cross_verification4/guass_herb-4.txt", dtype=float, delimiter=',')
h605=np.loadtxt(r"../data_cross_verification/cross_verification5/guass_herb-5.txt", dtype=float, delimiter=',')

disease_average_matrices_1="data/disease_average1.txt"
disease_average_matrices_2="data/disease_average2.txt"
disease_average_matrices_3="data/disease_average3.txt"
disease_average_matrices_4="data/disease_average4.txt"
disease_average_matrices_5="data/disease_average5.txt"

herb_average_matrices_1="data/herb_average1.txt"
herb_average_matrices_2="data/herb_average2.txt"
herb_average_matrices_3="data/herb_average3.txt"
herb_average_matrices_4="data/herb_average4.txt"
herb_average_matrices_5="data/herb_average5.txt"

predict_filename_1="data/predict1.txt"
predict_filename_2="data/predict2.txt"
predict_filename_3="data/predict3.txt"
predict_filename_4="data/predict4.txt"
predict_filename_5="data/predict5.txt"

cross_verifiction_1="../data_cross_verification/cross_verification1/herb_disease01cross_verification-1.txt"
cross_verifiction_2="../data_cross_verification/cross_verification2/herb_disease01cross_verification-2.txt"
cross_verifiction_3="../data_cross_verification/cross_verification3/herb_disease01cross_verification-3.txt"
cross_verifiction_4="../data_cross_verification/cross_verification4/herb_disease01cross_verification-4.txt"
cross_verifiction_5="../data_cross_verification/cross_verification5/herb_disease01cross_verification-5.txt"

one_to_zero_1="../data_cross_verification/cross_verification1/1A.txt"
one_to_zero_2="../data_cross_verification/cross_verification2/2A.txt"
one_to_zero_3="../data_cross_verification/cross_verification3/3A.txt"
one_to_zero_4="../data_cross_verification/cross_verification4/4A.txt"
one_to_zero_5="../data_cross_verification/cross_verification5/5A.txt"

fu_random_1="data/furandom1.txt"
fu_random_2="data/furandom2.txt"
fu_random_3="data/furandom3.txt"
fu_random_4="data/furandom4.txt"
fu_random_5="data/furandom5.txt"

sample_filename_1="data/samples_DP_HP_1.txt"
sample_filename_2="data/samples_DP_HP_2.txt"
sample_filename_3="data/samples_DP_HP_3.txt"
sample_filename_4="data/samples_DP_HP_4.txt"
sample_filename_5="data/samples_DP_HP_5.txt"

roc_filename_1= "Forecast-result/roc_1.png"
roc_filename_2= "Forecast-result/roc_2.png"
roc_filename_3= "Forecast-result/roc_3.png"
roc_filename_4= "Forecast-result/roc_4.png"
roc_filename_5= "Forecast-result/roc_5.png"

pr_filename_1= "Forecast-result/pr_1.png"
pr_filename_2= "Forecast-result/pr_2.png"
pr_filename_3= "Forecast-result/pr_3.png"
pr_filename_4= "Forecast-result/pr_4.png"
pr_filename_5= "Forecast-result/pr_5.png"


def max_matrix(matrix1, matrix2):
    n = len(matrix1)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = max(matrix1[i][j], matrix2[i][j])

    return result

def average_matrices(filename,matric,*matrices):
    if len(matrices) == 0:
        print("The number of matrices is 0")
        return None

    shape = matrices[0].shape
    for matrix in matrices[1:]:
        if matrix.shape != shape:
            return None

    matrix_sum = np.zeros(shape)
    for matrix in matrices:
        matrix_sum += matrix

    matrix_average = matrix_sum / len(matrices)
    matrix_average=max_matrix(matrix_average,matric)
    np.savetxt(filename, matrix_average, fmt="%f", delimiter=',')

    return matrix_average


def predict(disease_filename,herb_filename,di_herbfilename,predict_filename):
    disease = np.loadtxt(disease_filename, dtype=float, delimiter=',')
    herb = np.loadtxt(herb_filename, dtype=float, delimiter=',')
    di_herb = np.loadtxt(di_herbfilename, dtype=float, delimiter=',')
    nsp = NSP(disease, herb, di_herb)
    predict = nsp.network_NSP()
    np.savetxt(predict_filename, predict, fmt="%s", delimiter=',')


def select_positive_and_negative_samples(predict_filename,one_to_zero,random_seed,fu_random,sample_filename):
    predict = np.loadtxt(predict_filename, dtype=float, delimiter=',')
    herb_disease_Data = np.loadtxt(one_to_zero, dtype=str, delimiter=',')
    sample = []
    j = 0
    for data in herb_disease_Data:
        j = j + 1
        if j > 0:
            row = int(df_dis.loc[data[0]].id)
            column = int(df_herb.loc[data[1]].id)
            temp = []
            temp.append(predict[row - 1][column - 1])
            temp.append("1")
            sample.append(temp)
    fu = 852
    random.seed(random_seed)
    numbers1 = random.sample(range(1, 10000), 6000)
    numbers2 = []
    def find_row_column(x):
        row = x // 25
        column = x % 25
        return row, column
    numberix = 0
    for ix in numbers1:
        row, column = find_row_column(ix)
        if int(di_herb[row][column]) == 1:
            continue
        else:
            numberix = numberix + 1
            numbers2.append(ix)
            temp2 = []
            temp2.append(predict[row][column])
            temp2.append("0")
            sample.append(temp2)

        if numberix >= fu:
            break
    numbers2 = np.array(numbers2)
    np.savetxt(fu_random, numbers2, fmt="%s", delimiter=',')
    np.savetxt(sample_filename, sample, fmt="%s", delimiter=',')


def roc_draw(sample_filename,roc_filename,pr_filename):
    predict = np.loadtxt(sample_filename, dtype=float, delimiter=',')
    preds = []
    labels = []
    for line in predict:
        preds.append(float(line[0]))
        labels.append(int(line[1]))
    fpr, tpr, _ = roc_curve(labels, preds)
    roc_auc = auc(fpr, tpr)

    precision, recall, _ = precision_recall_curve(labels, preds)
    pr_auc = average_precision_score(labels, preds)

    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.4f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")

    plt.savefig(roc_filename)

    plt.figure()
    plt.step(recall, precision, color='b', alpha=0.2, where='post')
    plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title('Precision-Recall curve: AP={0:0.4f}'.format(pr_auc))
    plt.savefig(pr_filename)
    plt.show()
    return roc_auc, pr_auc





average_matrices(disease_average_matrices_1, d2,d1,d3,d4,d501)
average_matrices(herb_average_matrices_1, h601,h1,h2,h3,h4,h5)
predict(disease_average_matrices_1,herb_average_matrices_1,cross_verifiction_1,predict_filename_1)
select_positive_and_negative_samples(predict_filename_1,one_to_zero_1,1,fu_random_1,sample_filename_1)



average_matrices(disease_average_matrices_2, d2,d1,d3,d4,d502)
average_matrices(herb_average_matrices_2, h602,h1,h2,h3,h4,h5)
predict(disease_average_matrices_2,herb_average_matrices_2,cross_verifiction_2,predict_filename_2)
select_positive_and_negative_samples(predict_filename_2,one_to_zero_2,2,fu_random_2,sample_filename_2)



average_matrices(disease_average_matrices_3, d2,d1,d3,d4,d503)
average_matrices(herb_average_matrices_3, h603,h1,h2,h3,h4,h5)
predict(disease_average_matrices_3,herb_average_matrices_3,cross_verifiction_3,predict_filename_3)
select_positive_and_negative_samples(predict_filename_3,one_to_zero_3,3,fu_random_3,sample_filename_3)



average_matrices(disease_average_matrices_4, d2,d1,d3,d4,d504)
average_matrices(herb_average_matrices_4, h604,h1,h2,h3,h4,h5)
predict(disease_average_matrices_4,herb_average_matrices_4,cross_verifiction_4,predict_filename_4)
select_positive_and_negative_samples(predict_filename_4,one_to_zero_4,4,fu_random_4,sample_filename_4)



average_matrices(disease_average_matrices_5, d2,d1,d3,d4,d505)
average_matrices(herb_average_matrices_5, h605,h1,h2,h3,h4,h5)
predict(disease_average_matrices_5,herb_average_matrices_5,cross_verifiction_5,predict_filename_5)
select_positive_and_negative_samples(predict_filename_5,one_to_zero_5,5,fu_random_5,sample_filename_5)


import numpy as np
from sklearn.metrics import roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
roc_data = []
pr_data = []
colors = plt.cm.rainbow(np.linspace(0, 1, 6))
file_name=np.array(
          ['Fold1',  'Fold2',  'Fold3',  'Fold4',  'Fold5'

           ])
i=0
for element in file_name:
    i=i+1
    if i<6:
        all_predictions = []
        all_labels = []
        for j in range(1, 2):
            file_name = f"data/samples_DP_HP_{i}.txt"
            data = np.loadtxt(file_name, dtype=float, delimiter=',')
            positive_predictions = data[:852, 0]
            positive_labels = data[:852, 1]
            negative_predictions = data[852:, 0]
            negative_labels = data[852:, 1]
            all_predictions.extend([positive_predictions, negative_predictions])
            all_labels.extend([positive_labels, negative_labels])

        all_predictions = np.concatenate(all_predictions)
        all_labels = np.concatenate(all_labels)
        fpr, tpr, thresholds_roc = roc_curve(all_labels, all_predictions)
        roc_auc = auc(fpr, tpr)
        precision, recall, thresholds_pr = precision_recall_curve(all_labels, all_predictions)
        pr_auc = auc(recall, precision)
        roc_data.append((fpr, tpr, roc_auc, colors[i - 1],element))
        pr_data.append((recall, precision, pr_auc, colors[i - 1],element))

plt.figure()

for fpr, tpr, roc_auc, color,element in roc_data:
    plt.plot(fpr, tpr, label=f'{element} AUROC = {roc_auc:.4f}', color=color)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right',prop={'size':10})
plt.savefig('ROC_curve.pdf',dpi=600)
plt.figure()
for recall, precision, pr_auc, color,element in pr_data:
    plt.plot(recall, precision, label=f'{element} AUPR = {pr_auc:.4f}', color=color)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='lower right',prop={'size':10})
plt.savefig('PR_curve.pdf',dpi=600)









# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:53:19 2019

@author: tsungyu
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import itertools
from costcla.metrics import cost_loss, savings_score
from costcla.models import CostSensitiveRandomForestClassifier


##########################################################################
def display_summary(true,pred):
    tn, fp, fn, tp = confusion_matrix(true,pred).ravel()  #網路資料版
    print('confusion matrix')
    print(np.array([[fn,tn],[tp,fp]]))
    print('sensitivity is %f',1.*tp/(tp+fn))
    print('specificity is %f',1.*tn/(tn+fp))
    print('accuracy is %f',1.*(tp+tn)/(tp+tn+fp+fn))
    print('balanced accuracy is %',1./2*(1.*tp/(tp+fn)+1.*tn/(tn+fp)))

#print('Gaussian NB')
#display_summary(y_test,y_pred_nb)

##########################################################################

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
#    else:
#        print('Confusion matrix, without normalization')

#    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    
######################################################################
def show_data(cm, print_res = 0):
    tp = cm[0,0]
    fn = cm[1,0]
    fp = cm[0,1]
    tn = cm[1,1]
    if print_res == 1:
        print('Precision =     {:.8f}'.format(tp/(tp+fp)))
        print('Recall (TPR)(sensitivity) =  {:.8f}'.format(tp/(tp+fn)))
        print('Fallout (FPR) = {:.8e}'.format(fp/(fp+tn)))
        print('Specificity = {:.8e}'.format(tn/(fp+tn)))
    return tp/(tp+fp), tp/(tp+fn), fp/(fp+tn)


df_credit = pd.read_csv('C:/Users/tsungyu/Downloads/creditcarddata/creditcard.csv')
 
col_names = df_credit.columns
feature_cols = col_names[:-1]
df_negative = df_credit[df_credit[col_names[-1]]==0]
df_positive = df_credit[df_credit[col_names[-1]]==1]
X = df_credit[feature_cols]
y = df_credit[col_names[-1]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)




cost_mat_train = np.zeros((len(y_train),4))
#X_train['Amount']=abs(X_train['Amount']-5) ###############!!!!!!

#false positives cost 5
cost_mat_train[:,0]=2
#false negatives cost the transaction amount
cost_mat_train[:,1]=250
#true positives also cost 5
cost_mat_train[:,2]=0
cost_mat_train[:,3]=0



cost_mat_test = np.zeros((len(y_test),4))

cost_mat_test[:,0]=2
cost_mat_test[:,1]=250
cost_mat_test[:,2]=0
cost_mat_test[:,3]=0


g = CostSensitiveRandomForestClassifier()
g.fit(np.array(X_train), np.array(y_train), cost_mat_train)
y_pred_rf_cslr=g.predict(np.array(X_test))

print('--------CostSensitiveRandomForestClassifier------')
display_summary(y_test,y_pred_rf_cslr)



cm = confusion_matrix(y_test, y_pred_rf_cslr)
tn, fp, fn, tp = confusion_matrix(y_test,y_pred_rf_cslr).ravel()

plot_confusion_matrix(cm, ['0', '1'], )
pr, tpr, fpr = show_data(cm, print_res = 1);


# Savings using only RandomForest
print("savings_score=" , savings_score(y_test, y_pred_rf_cslr, cost_mat_test))
print("cost_loss=" , cost_loss(y_test, y_pred_rf_cslr, cost_mat_test))
print('F1_score  =     {:.8f}'.format(2*(((tp/(tp+fp))*(tp/(tp+fn)))/((tp/(tp+fp))+(tp/(tp+fn))))))
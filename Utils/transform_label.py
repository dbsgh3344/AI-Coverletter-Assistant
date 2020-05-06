import re
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
import seaborn as sns
import matplotlib.pyplot as plt



def manyhot_label(label_col):

    ''' transform str or int label to manyhot encoding label'''

    '''Parameters

        label_col : Input Series Type str or int label column '''

    pat = re.compile('[^0-9]')
    label_col = label_col.apply(lambda x : np.array(x))
    int_label = label_col[label_col.notnull()].apply(lambda x: [int(i) for i in list(pat.sub('',x))])

    mlb = MultiLabelBinarizer()
    manyhot_labels = mlb.fit_transform(int_label)

    return manyhot_labels

def label_visualize(manyhot_labels):
    lists = [0] * 9 
    for i in manyhot_labels:
        for j in range(9):
            if i[j] ==1:
                lists[j] +=1


    ax= sns.barplot(np.arange(len(manyhot_labels[0])),y=lists)

    #adding the text labels
    rects = ax.patches
    labels = lists
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom', fontsize=10)

    return plt.show()
        



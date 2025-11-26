"""evaluation.py
Functions to compute and save evaluation metrics and plots for classification.
"""
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def save_confusion_matrix(y_true, y_pred, labels=None, filename='confusion_matrix.png'):
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    fig, ax = plt.subplots(figsize=(6,5))
    im = ax.imshow(cm, interpolation='nearest')
    ax.set_title('Confusion Matrix')
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    fig.colorbar(im)
    plt.savefig(BASE / 'outputs' / 'charts' / filename, bbox_inches='tight')
    plt.close(fig)

def save_roc_curve(clf, X_test, y_test, filename='roc_curve.png'):
    # Works for binary classification
    if len(set(y_test)) != 2:
        print('ROC curve helper works for binary classification only.')
        return
    probs = clf.predict_proba(X_test)[:,1]
    fpr, tpr, _ = roc_curve(y_test, probs)
    roc_auc = auc(fpr, tpr)
    fig, ax = plt.subplots(figsize=(6,5))
    ax.plot(fpr, tpr, label=f'ROC curve (area = {roc_auc:.2f})')
    ax.plot([0,1],[0,1],'--')
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('ROC Curve')
    ax.legend(loc='lower right')
    fig.savefig(BASE / 'outputs' / 'charts' / filename, bbox_inches='tight')
    plt.close(fig)

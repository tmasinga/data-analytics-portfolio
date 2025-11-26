"""visualization.py
Simple plotting helpers for classification outputs.
"""
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def plot_feature_importance(importances, feature_names, top_n=20, filename='feature_importance.png'):
    feat_imp = pd.Series(importances, index=feature_names).sort_values(ascending=False).head(top_n)
    fig, ax = plt.subplots(figsize=(8,6))
    feat_imp.plot(kind='bar', ax=ax)
    ax.set_title('Top Feature Importances')
    ax.set_ylabel('Importance')
    fig.savefig(BASE / 'outputs' / 'charts' / filename, bbox_inches='tight')
    plt.close(fig)

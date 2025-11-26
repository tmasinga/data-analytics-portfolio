"""model_training.py
Train classification models, compare performance, and save the best model.
"""
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, f1_score, classification_report
from pathlib import Path
import pandas as pd
from src.preprocessing import make_train_test, load_data

BASE = Path(__file__).resolve().parents[1]

def train_baseline_models(X_train, y_train):
    """Train simple baseline models and return a dict of results."""
    models = {
        'logreg': LogisticRegression(max_iter=1000),
        'rf': RandomForestClassifier(n_estimators=100, random_state=42)
    }
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        scores = cross_val_score(model, X_train, y_train, cv=5, scoring='f1_macro')
        results[name] = {'model': model, 'cv_f1_macro_mean': float(scores.mean())}
    return results

def evaluate_and_save(best_model, X_test, y_test, name='best_model'):
    """Evaluate a model on test set and save model + metrics."""
    preds = best_model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds, average='macro')
    report = classification_report(y_test, preds)
    print('Accuracy:', acc)
    print('F1 (macro):', f1)
    print(report)
    joblib.dump(best_model, BASE / 'outputs' / 'model_artifacts' / f'{name}.pkl')
    # Save simple metrics
    with open(BASE / 'outputs' / 'model_results' / f'{name}_metrics.txt', 'w') as f:
        f.write(f'accuracy: {acc}\nf1_macro: {f1}\n\n{report}')

if __name__ == '__main__':
    # Example run (requires a CSV path and target)
    # Place your CSV at data/raw/your_data.csv and set target variable below, then run:
    # python src/model_training.py
    data_path = BASE / 'data' / 'raw' / 'your_data.csv'
    target_col = 'target'  # change to your target column
    if data_path.exists():
        df = load_data(data_path)
        X_train, X_test, y_train, y_test = make_train_test(df, target_col)
        results = train_baseline_models(X_train, y_train)
        # pick best by cv score
        best_name = max(results.keys(), key=lambda k: results[k]['cv_f1_macro_mean'])
        best_model = results[best_name]['model']
        evaluate_and_save(best_model, X_test, y_test, name=best_name)
    else:
        print(f'Place your dataset CSV at {data_path} and set target_col in this script.')

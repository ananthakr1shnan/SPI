import os
import sys
import numpy as np 
import pandas as pd
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
        best_model = None
        best_score = float("-inf")

        for model_name, model in models.items():
            try:
                print(f"Tuning {model_name}...")

                if param.get(model_name) and len(param[model_name]) > 0:
                    gs = GridSearchCV(model, param[model_name], cv=3, n_jobs=-1)
                    gs.fit(X_train, y_train)
                    tuned_model = gs.best_estimator_
                else:
                    tuned_model = model
                    tuned_model.fit(X_train, y_train)

                y_test_pred = tuned_model.predict(X_test)
                test_model_score = r2_score(y_test, y_test_pred)

                if not np.isnan(test_model_score):
                    report[model_name] = test_model_score
                    print(f"{model_name} R² score: {test_model_score:.4f}")

                    if test_model_score > best_score:
                        best_score = test_model_score
                        best_model = tuned_model
            except Exception as e:
                print(f"{model_name} failed: {e}")

        if best_model is None:
            raise Exception("All models failed during training or prediction.")

        return report, best_model

    except Exception as e:
        raise CustomException(e, sys)



def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)

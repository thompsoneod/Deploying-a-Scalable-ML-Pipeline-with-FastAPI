import pytest

import numpy as np

from ml.model import compute_model_metrics, train_model, inference
from sklearn.ensemble import RandomForestClassifier
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    # Test that the train_model function returns a RandomForestClassifier
    """
    # Your code here
    X_train = np.random.rand(100, 10)
    y_train = np.random.randint(2, size=100)
    
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Model is not a RandomForestClassifier"



# TODO: implement the second test. Change the function name and input as needed
def test_inference():
    """
    # Test that the inference function returns an array of the correct shape
    """
    # Your code here
    X_test = np.random.rand(20,10)
    model = RandomForestClassifier().fit(np.random.rand(100, 10), np.random.randint(2, size=100))
    preds = inference(model, X_test)
    assert preds.shape[0] == X_test.shape[0], "Inference did not return predictions of correct shape"


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # Test that compute_model_metrics returns the correct metrics values.
    """
    # Your code here
    y_true = np.array([1, 0, 1, 1, 0, 1, 1, 0, 1, 0])
    y_pred = np.array([1, 0, 1, 1, 0, 1, 0, 1, 0, 0])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    
    assert 0 <= precision <= 1, "Precision is out of range"
    assert 0 <= recall <= 1, "Recall is out of range"
    assert 0 <= fbeta <= 1, "F-beta score is out of range"
    

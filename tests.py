import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from model import RANDOM_STATE, TEST_SIZE, get_accuracy, train_and_predict


def _get_expected_test_target():
    iris = load_iris()
    _, X_test, _, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=iris.target,
    )
    return X_test, y_test


def test_predictions_not_none():
    preds, _ = train_and_predict()
    assert preds is not None, "Predictions should not be None."


def test_predictions_length():
    preds, _ = train_and_predict()
    _, y_test = _get_expected_test_target()
    assert len(preds) > 0, "Predictions should not be empty."
    assert len(preds) == len(y_test), "Predictions length should match test sample count."


def test_predictions_value_range():
    preds, _ = train_and_predict()
    assert np.all(np.isin(preds, [0, 1, 2])), "Predictions should contain only Iris classes: 0, 1, 2."


def test_model_accuracy():
    preds, _ = train_and_predict()
    _, y_test = _get_expected_test_target()
    accuracy = get_accuracy(y_test, preds)
    assert accuracy >= 0.7, f"Model accuracy should be at least 70%, got {accuracy:.2%}."


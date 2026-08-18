# Model evaluation logic for Titanic survival prediction

from sklearn.metrics import accuracy_score, confusion_matrix


def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model and return accuracy and confusion matrix."""

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print(f"Logistic Regression Accuracy: {accuracy:.2%}")
    print("\nConfusion Matrix:")
    print(cm)

    return accuracy, cm
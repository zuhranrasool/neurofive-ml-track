# Model training logic for Titanic survival prediction

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from preprocessing import create_preprocessor


def train_model(X_train, y_train):
    """Create, train, and return the Logistic Regression model."""

    preprocessor = create_preprocessor()

    logistic_model = LogisticRegression(max_iter=1000)

    model_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", logistic_model)
        ]
    )

    model_pipeline.fit(X_train, y_train)

    return model_pipeline
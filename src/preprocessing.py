# Preprocessing logic for Titanic survival prediction

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


categorical_features = ["Sex", "Embarked"]

numerical_features = ["Pclass", "Age", "SibSp", "Parch", "Fare"]


def create_preprocessor():
    """Create and return the preprocessing pipeline."""

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features
            ),
            (
                "numerical",
                StandardScaler(),
                numerical_features
            )
        ]
    )

    return preprocessor
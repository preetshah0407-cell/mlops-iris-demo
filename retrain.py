
from pycaret.classification import (
    setup, compare_models, finalize_model
)
from pycaret.datasets import get_data
import joblib

iris = get_data("iris")

setup(
    data=iris,
    target="species",
    session_id=42,
    verbose=False,
    html=False,
    log_experiment=False
)

best_model = compare_models()
final_model = finalize_model(best_model)

joblib.dump(final_model, "iris_model.pkl")
print("Retraining complete: iris_model.pkl")

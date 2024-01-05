# Airline Delay Prediction
Overview
This project focuses on predicting arrival delays in airlines using a binary classification model, specifically employing the Random Forest algorithm. Notably, departure delay is intentionally excluded as an input feature to explore the model's capability to predict arrival delays independently.

Utilizing raw data
Applying Principal Component Analysis (PCA) transformation to the data
It was observed that the PCA-transformed data yielded marginal improvements in model performance.

Parameter Tuning
Grid search was employed to find the optimal hyperparameters for the Random Forest model. This ensures the selected model is fine-tuned for the best predictive performance.

Evaluation
The model's performance was evaluated using 10-fold cross-validation, providing a robust assessment of its generalization capabilities.

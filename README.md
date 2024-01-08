# Airline Delay Prediction
Overview
This project focuses on predicting arrival delays in airlines using a binary classification model, specifically employing the Random Forest algorithm. Notably, departure delay is intentionally excluded as an input feature to explore the model's capability to predict arrival delays independently.

- Utilizing raw data
- Applying Principal Component Analysis (PCA) transformation to the data
- It was observed that the PCA-transformed data yielded marginal improvements in model performance.
- Grid search was employed to find the optimal hyperparameters for the Random Forest model. This ensures the model is fine-tuned for the best predictive performance.
- The model's performance was evaluated using 10-fold cross-validation, providing a robust assessment of its generalization capabilities.

The app is built using the Flask web framework and offers an intuitive interface to predict arrival delays in airliness[Video](https://drive.google.com/file/d/1jOVZH4nUHl-4o3PGauEOlcPz-bVlRftE/view?usp=sharing). You can access the live version of this web application [here](https://airlinedelays.azurewebsites.net/).

![Image Alt Text](https://github.com/ThaminduSulakshana/Airline-delay-prediction/blob/b720f0b326667b92f91c274c0a7f424597cdd8ee/Screenshot%20(282).png)

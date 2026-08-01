# Car Price Prediction Web Application

## Participant Name
Athulyakrishna K

## MUID
YOUR_MUID

---

## Project Overview

This project predicts the selling price of a used car using a Random Forest Regression model. The model was trained on the CarDekho Used Car dataset and deployed as an interactive web application using Streamlit.

Users can enter car details such as manufacturing year, present price, kilometers driven, fuel type, seller type, transmission type, and owner count to receive a predicted selling price.

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## Machine Learning Model

- Algorithm: Random Forest Regressor

---

## Deployment Approach

1. Trained the Random Forest model.
2. Saved the trained model using Joblib.
3. Built a Streamlit web application.
4. Uploaded the project to GitHub.
5. Deployed the application using Streamlit Community Cloud.

---

## Project Structure

```
Car-Price-Prediction/
│── app.py
│── model.pkl
│── model_columns.pkl
│── cardekho_dataset.csv
│── requirements.txt
│── README.md
```

---

## Key Observations

- Random Forest provided accurate and stable predictions.
- Streamlit made it easy to create a simple interactive interface.
- Users can obtain predictions instantly by entering vehicle details.

---

## Challenges Faced

- Saving the trained model and preprocessing information.
- Matching the input features used during training.
- Deploying the application and managing dependencies.

---

## Future Improvements

- Improve the user interface with better styling.
- Add charts and model performance metrics.
- Support additional vehicle features.
- Enhance prediction accuracy through feature engineering and hyperparameter tuning.

---

## GitHub Repository

https://github.com/YOUR_USERNAME/Car-Price-Prediction

---

## Deployment Link

https://YOUR-APP.streamlit.app

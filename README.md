 Credit Card Fraud Detection System

## 📓 Notebook

| Notebook | Link |
|----------|------|
| Credit Risk Fraud Detection | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ruslancabbarov/End-to-End-DataScience-Project/blob/main/Credit_Risk_Fraud_Detection.ipynb) |

  Project OverviewThis project is an end-to-end Machine Learning solution designed to detect fraudulent credit card transactions in real-time. It transitions from deep data analysis and model optimization to a production-ready REST API.
 
 
 Key FeaturesFeature Engineering: 
 
 Calculated transaction distances using the Haversine formula and identified high-risk time windows (is_night).Imbalanced Data Handling: Optimized XGBoost with scale_pos_weight to prioritize fraud detection (Recall) over simple accuracy

 Model Deployment: 

 Built a high-performance API using FastAPI to serve model predictions.
 
 
  Model PerformanceAfter comparing Logistic Regression and Random Forest, XGBoost was selected as the final model due to its superior separation power.MetricScoreXGBoost AUC Score0.998Recall (Fraud)96%Precision (Fraud)0.30ROC Curve AnalysisThe AUC of 0.998 proves the model is nearly perfect at distinguishing between legitimate users and fraudsters, ensuring minimal "False Positives" (blocking honest customers).
  
  Strategic InsightsThe model identified the following as the top predictors of fraud:
  
  Category (gas_transport): Fraudsters often make small "test" purchases at gas stations to verify stolen cards.Amount (amt): High-value transactions remain a significant risk factor.Distance: Unusual distances between the customer's home and the merchant.
  
  Tech StackCore: Python, Pandas, Scikit-learn, XGBoost.API: FastAPI, Uvicorn, Pydantic, Pickle.
  
  How to RunInstall Dependencies:
   pip install -r requirements.txtStart API: uvicorn main:app --reloadTest: Visit http://127.0.0.1:8000/docs to use the interactive Swagger UI.

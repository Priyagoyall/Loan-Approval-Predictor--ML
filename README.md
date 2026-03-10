**Loan Approval Prediction Model**<br>
**Project Overview**<br>
Financial institutions receive thousands of loan applications, and manually reviewing them can be time-consuming and error-prone. This project builds a machine learning model to predict whether a loan application should be approved or rejected based on applicant information.

The project demonstrates a complete data science workflow, including:
- Data exploration and visualization
- Data preprocessing and feature preparation
- Model building using machine learning algorithms
- Model evaluation using classification metrics

The final model uses XGBoost Classifier, a powerful ensemble learning algorithm known for high predictive performance.

**Business Problem**<br>

Banks need a reliable system to assess loan applications quickly while minimizing risk. Incorrect approvals can lead to loan defaults, while rejecting eligible customers can reduce business opportunities.<br>

This project helps answer:<br>
Can we predict loan approval based on applicant data?<br>

Such a model can support data-driven decision making in credit risk assessment.

**Dataset**<br>

The dataset used in this project contains information about loan applicants, including financial details and loan-related attributes.
Typical features include:
- Applicant income
- Loan amount
- Credit history
- Employment status
- Other applicant financial indicators

**Target Variable**<Br>
loan_status
- 1 → Loan Approved
- 0 → Loan Rejected

**Project Workflow**<br>
**1. Exploratory Data Analysis (EDA)**<br>
EDA was performed to understand the dataset and identify patterns.
Key analysis included:<br>
- Dataset structure and summary statistics
- Missing value analysis
- Distribution of loan approval status
- Feature relationship analysis
- Data visualization using charts

Libraries used:<br>
- Pandas
- Numpy
- scikit learn
- Matplotlib
- Seaborn

**2. Data Preprocessing**<br>

Data preprocessing steps included:
- Removing unnecessary columns
- Handling missing values
- Encoding categorical variables
- Feature preparation for machine learning

Splitting dataset into training and testing sets
Train/Test split:<br>
- 80% Training Data
- 20% Testing Data

**3. Model Training**<br>
Three machine learning models were implemented:

**1. Logistic Regression**<br>
A baseline classification model used for binary classification.

**2. Random Forest Classifier**<br>
An ensemble learning method that improves prediction accuracy by combining multiple decision trees.

**3. XGBoost Classifier**<br>
The final model was built using XGBoost, an optimized gradient boosting algorithm widely used in machine learning competitions and real-world applications.

**Model Evaluation**<br>

The model performance was evaluated using multiple classification metrics:<br>
- Accuracy Score
- Confusion Matrix
- Classification Report
- Precision
- Recall
- F1 Score
- ROC Curve
These metrics help measure how effectively the model predicts loan approval outcomes.

**Key Insight:**<br>
Applicants with strong credit history have a significantly higher loan approval rate.


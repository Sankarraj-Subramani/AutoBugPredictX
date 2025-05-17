# AutoBugPredictX – AI-Powered Bug Prediction Engine for QA

## 📖 Overview
AutoBugPredictX is an open-source AI tool that predicts the probability of bugs in QA test modules based on historical test execution data. 
It enables QA teams to proactively focus on high-risk areas during testing, improving software quality and efficiency.

## 🔥 Features
- Logistic Regression-based bug prediction
- Risk heatmap visualizations
- Upload test execution data (CSV)
- Real-time prediction dashboard (Streamlit)
- Lightweight, cloud-deployable design

## 🛠️ Tech Stack
- Python 3.9+
- pandas, scikit-learn
- Streamlit (for UI)

## 🚀 How to Run
1. Clone the repo:
    ```
    git clone https://github.com/your_username/AutoBugPredictX.git
    cd AutoBugPredictX
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Launch Streamlit app:
    ```
    streamlit run streamlit_app/app.py
    ```
## Sample Data Format to use for uploading
To test the app, a sample dataset is provided at:
```
📁 /data/sample_test_logs.csv
```
## Sample Data Format
| module_name | no_of_test_cases | no_of_failed_tests | code_changes | past_bugs | bug_found |
|-------------|------------------|--------------------|--------------|-----------|-----------|
| LoginModule | 10               | 2                  | 5            | 1         | 1         |

- `bug_found` = 1 indicates presence of a bug, 0 otherwise.

## 🏆 Contributions
Contributions are welcome! Feel free to create a pull request to add new models, improve UI/UX, or add new visualizations.

## 📄 License
MIT License.

---

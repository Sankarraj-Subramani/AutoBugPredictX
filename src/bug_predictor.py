from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def predict_bug_probability(model, input_data):
    return model.predict_proba(input_data)[:, 1]  # Probability of bug = 1

import joblib
import sys
import sklearn

text = sys.argv[3]
headling = sys.argv[1]
author = sys.argv[2]

vectorised = joblib.load('vectorizer.pkl')

preprocessed_text = vectorised.transform([text])

LogisticRegression = joblib.load('LogisticRegression.pkl')

prob = LogisticRegression.predict_log_proba(preprocessed_text)

output_class_map = {0: 'True Article',
                    1: 'Fake Article'}

output = LogisticRegression.predict(preprocessed_text)
output = output_class_map[int(output[0])]
prob = f'Truth probability: {float(prob[0,0]) * 100:.2f}%'

# print(output)
# print(prob)


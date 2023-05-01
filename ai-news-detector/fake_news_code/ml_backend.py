import joblib
import sys
import sklearn


text = sys.argv[1]
headling = sys.argv[2]
author = sys.argv[3]



vectorised = joblib.load('./fake_news_code/vectorizer.pkl')

preprocessed_text = vectorised.transform([text])

LogisticRegression = joblib.load('./fake_news_code/LogisticRegression.pkl')

prob = LogisticRegression.predict_proba(preprocessed_text)

output_class_map = {0: 'True Article',
                    1: 'Fake Article'}

output = LogisticRegression.predict(preprocessed_text)
output = output_class_map[int(output[0])]
prob = f'Truth probability: {float(prob[0,0]) * 100:.2f}%'

print(output)
print(prob)



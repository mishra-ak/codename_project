
from model_prediction import CustomModelPrediction

def find(ques):
  classifier = CustomModelPrediction.from_path('/home/akshay/FlaskTemplates/model_in_flask')
  results = classifier.predict(ques)
  return results
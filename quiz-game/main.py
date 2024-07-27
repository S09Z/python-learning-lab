from question_model import Question
from quiz_brain import QuizBrain

import os
import pandas as pd
import json


# Define the directory containing the JSON files
directory = './questions/'
jsonFileName = 'common_knowledge_questions_set_'

# Check if the directory exists
if os.path.exists(directory):
    index = 1
    quizStore = []

    for f in os.listdir(directory):
        if (f.find(jsonFileName) >= 0):
            data = pd.read_json(f"{directory}/{f}")
            df = pd.DataFrame(data)
            quizStore.append(Question(df["Question"], df["Answer"]))
        index += 1

    # print(quizStore)

    QuizBrain(quizStore)
else:
    print(f"The directory {directory} does not exist.")

from question_model import Question
from quiz_brain import QuizBrain

import os
import pandas as pd
import json


# Define the directory containing the JSON files
directory = './questions/'
jsonFileName = 'common_knowledge_questions_set_'

# https://opentdb.com/api_config.php more questions data to load.

# Check if the directory exists
if os.path.exists(directory):
    index = 1
    quizStore = pd.DataFrame()

    for f in os.listdir(directory):
        if (f.find(jsonFileName) >= 0):
            data = pd.read_json(f"{directory}/{f}")
            df = pd.DataFrame(data)
            quizStore = pd.concat([quizStore, df[["Question", "Answer"]]], ignore_index=True)
        index += 1

    quiz = QuizBrain(quizStore.sample(frac=1).reset_index(drop=True).to_dict(orient='records'))
    while (quiz.still_has_question_left()):
        quiz.next_question()
else:
    print(f"The directory {directory} does not exist.")

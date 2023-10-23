import bardapi
import os
import csv

# set your __Secure-1PSID value to key
token = 'cQhhRdM4uJnAYu1l3mtJcuMOgeno_qO5rQdH9G2Rc5FAjRspXI6cUv_Vosumdzx2SguEKw.'

# set your input text
# input_text = "What movie would you recommend?"

# Send an API request and get a response.
# response = bardapi.core.Bard(token).get_answer(input_text)
# print(response)

csvFinalResult = open('results/classification_result2.csv', 'w', newline='')
writerResult = csv.writer(csvFinalResult) 
data = []
with open("dataset/dataset_label_2.csv", 'rt') as fileFake:
    reader = csv.reader(fileFake)
    next(reader)
    for row in reader:
        prompt = "'" + row[1] + "' Does the given text contain characteristics of fake news? It spreads misinformation? Answer only with yes or no."
        classification = bardapi.core.Bard(token).get_answer(prompt)
        data.append([row[1], row[3], classification['content']])
    writerResult.writerow(['text', 'is_fake_news', 'gpt_classification'])
    writerResult.writerows(data)
    fileFake.close()
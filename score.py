from custom_test import custom_top10, check_information, get_answer
from utils import get_qa, get_chunks, make_dataset
import random

for _type in ['general', 'comprehensive']:
    chunks = get_chunks()
    queries = get_qa(_type='general')

    qas, ordered_chunks, ordered_keys = make_dataset(queries, chunks)
    questions = [_['question'] for _ in qas]
    answers = custom_top10(questions, ordered_chunks)

    correct1 = 0
    correct3 = 0
    correct5 = 0
    correct10 = 0

    for idx, answer in enumerate(answers):

        a = qas[idx]['key']
        answer = [ordered_keys[_] for _ in answer]
        if a == answer[0]:
            correct1 += 1
        if a in answer[:3]:
            correct3 += 1
        if a in answer[:5]:
            correct5 += 1
        if a in answer[:10]:
            correct10 += 1

    real_true = 0
    real_false = 0
    for qa in qas:
        question = qa['question']
        answer = qa['key']
        indexes = list(range(len(ordered_chunks)))
        while True:
            random.shuffle(indexes)
            labels = [ordered_keys[_] for _ in indexes[:10]]
            if answer in labels:
                continue
            contexts = [ordered_chunks[_] for _ in indexes[:10]]
            answer = check_information(contexts, question)
            if answer == False:
                real_false += 1
            break
        while True:
            random.shuffle(indexes)
            labels = [ordered_keys[_] for _ in indexes[:9]]
            if answer in labels:
                continue
            contexts = [ordered_chunks[_] for _ in indexes[:9]]
            real_idx = ordered_keys.index(qa['key'])
            contexts.append(ordered_chunks[real_idx])
            random.shuffle(contexts)
            answer = check_information(contexts, question)
            if answer == True:
                real_true += 1
            break

    with open(f'{_type}.txt', 'w', encoding='utf-8') as f:
        f.write('')
    for idx, answer in enumerate(answers):

        qa = qas[idx]
        contexts = [ordered_chunks[_] for _ in answer]
        question = qa['question']
        gold = qa['answer']

        answer = get_answer(contexts, question)
        with open(f'{_type}.txt', 'a', encoding='utf-8') as f:
            f.write(f'Question: {question}\n')
            f.write(f'Correct Answer: {gold}\n')
            f.write(f'Generated Response: {answer}\n\n')

    print(f'Results of {_type} task is as follow:')
    print(f'\n------------recall performance------------\n')
    print(f'top 1 recall: {correct1/len(qas)}')
    print(f'top 3 recall: {correct3/len(qas)}')
    print(f'top 5 recall: {correct5/len(qas)}')
    print(f'top 10 recall: {correct10/len(qas)}')
    print(f'\n------------judging performance-----------\n')
    print(f'Real True: {real_true/len(qas)}')
    print(f'Real False: {real_false/len(qas)}')
    print(f'\n------------------------------------------\n')
    print(f'Result of inference successfully saved to {_type}.txt.')
    print('')
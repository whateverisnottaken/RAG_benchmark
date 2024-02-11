import json

def read_json_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read().strip()
        
    data = data.split('\n')
    data = [json.loads(_) for _ in data]
    return data

def get_qa(parts=[], _type='comprehensive'):
    dataset = read_json_lines(f'questions/{_type}.json')
    if parts:
        if type(parts) == str:
            parts = [parts]
        dataset = [_ for _ in dataset if _['page'] in parts]
        return dataset
    else:
        return dataset

def get_chunks(parts=[]):
    dataset = read_json_lines('all_chunks.json')
    if parts:
        if type(parts) == str:
            parts = [parts]
        dataset = [_ for _ in dataset if _['page'] in parts]
        return dataset
    else:
        return dataset

def make_dataset(qas, chunks):
    ordered_keys = []
    ordered_chunks = []
    for chunk in chunks:
        key = chunk['page']+'_'+chunk['num']
        ordered_keys.append(key)
        text = chunk['text']
        ordered_chunks.append(text)
    new_qas = []
    for qa in qas:
        q = qa['question']
        key = qa['page']+'_'+qa['chunk']
        d = {}
        d['question'] = q
        d['key'] = key
        d['answer'] = qa['answer']
        new_qas.append(d)
    return new_qas, ordered_chunks, ordered_keys

def custom_top10(queries, docs):
    # Please implement this function for your benchmark
    # query is a list of strings, it contains all query stings in the test dataset.
    # docs is a list of candidate documents.
    # The goal of this function is to get the top 10 related documents of for each queries.
    # The return should be a list of exactly 10 integers.
    # Note that the index should start from 0, but not 1.

    # Below is an example for randomly choosing 10 answers.
    import random
    indexes = list(range(len(docs)))
    answer = []
    for i in range(len(queries)):
        random.shuffle(indexes)
        answer.append(indexes[:10].copy())
    return answer

def check_information(contexts, query):
    # Please implement this function for checking if the contexts contain the necessary information for the query.
    # The contexts is a list of strings.
    # Query is a string.
    # The return should be a boolean value, True if contains, False is not contain.

    # Below is an example:
    import random
    return random.choice([True, False])

def get_answer(contexts, query):
    # Please implement this function to get the answer for the query, given the contexts.
    # The contexts is a list of strings.
    # The query is a string.
    # The return should be a string.

    # Below is an example:
    return 'Hello, world!'

def textQueries(sentences, queries):
    sent_hash = dict()

    for s in range(len(sentences)):
        sent_hash[s] = set(sentences[s].split(' '))

    # for each query
    for query in queries:
        query_list = query.split(' ')
        # for each word in query
        isExists = False
        for s in range(len(sentences)):
            if set(query_list).issubset(sent_hash[s]):
                isExists = True
                print(s, end = " ")

        if not isExists:
            print(-1, end = " ")
        print()



if __name__ == '__main__':
    sentences_count = int(input().strip())

    sentences = []

    for _ in range(sentences_count):
        sentences_item = input()
        sentences.append(sentences_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    textQueries(sentences, queries)

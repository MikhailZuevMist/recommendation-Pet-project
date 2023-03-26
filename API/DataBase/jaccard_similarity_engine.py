import nltk


def jaccard_similarity(doc1, doc2):
    # Helper function to calculate Jaccard similarity between two documents
    text = nltk.word_tokenize(doc1.lower())
    words_doc_NN_VB_1 = set([i[0] for i in nltk.pos_tag(text) if i[1] in ['NN', 'VB']])
    words_doc_JJ_1 = set([i[0] for i in nltk.pos_tag(text) if i[1] in ['JJ']])
    text = nltk.word_tokenize(doc2.lower())
    words_doc_NN_VB_2 = set([i[0] for i in nltk.pos_tag(text) if i[1] in ['NN', 'VB']])
    words_doc_JJ_2 = set([i[0] for i in nltk.pos_tag(text) if i[1] in ['JJ']])
    intersection_NN_VB = words_doc_NN_VB_1.intersection(words_doc_NN_VB_2)
    intersection_JJ = words_doc_JJ_1.intersection(words_doc_JJ_2)
    union_NN_VB = words_doc_NN_VB_1.union(words_doc_NN_VB_2)
    union_JJ = words_doc_JJ_1.union(words_doc_JJ_2)
    return (len(intersection_NN_VB) / len(union_NN_VB)) + (len(intersection_JJ) / len(union_JJ) * 1)


# js = lambda doc: jaccard_similarity(doc, df_games_reshaped['Atmosphere'][0]) + \
#                  jaccard_similarity(doc, df_games_reshaped['Tags'][0]) + \
#                  jaccard_similarity(doc, df_games_reshaped['summary'][0])
# lst = [[i, js(i)] for i in df_movie_reshaped['Atmosphere']]
# max(lst, key=lambda x: x[1])

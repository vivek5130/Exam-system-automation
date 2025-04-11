def extractsKeywords(doc):
    #originalAnswer = 'Naive Bayes is a kind of classifier which uses the Bayes Theorem. It predicts membership probabilities for each class such as the probability that given record or data point belongs to a particular class. The class with the highest probability is considered as the most likely class'
    #stud_ans = 'Naive bayes is Classification technique, here based on one variable we need to find another one. so to work witj naive byes we should know about its fetures and number of parameter of the target variables so that we can get the proper answers and there is scalableity to recudes the first function and its hot codeing'

    #originalAnswer = originalAnswer.lower()
    #stud_ans = stud_ans.lower()


    from nltk import tokenize
    from operator import itemgetter
    import math

    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize 
    stop_words = set(stopwords.words('english'))

    total_words = doc.split()
    total_word_length = len(total_words)
    #print(total_word_length)
    total_sentences = tokenize.sent_tokenize(doc)
    total_sent_len = len(total_sentences)
    #print(total_sent_len)

    tf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.','')
        if each_word not in stop_words:
            if each_word in tf_score:
                tf_score[each_word] += 1
            else:
                tf_score[each_word] = 1

    # Dividing by total_word_length for each dictionary element
    tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())
    #print(tf_score)

    def check_sent(word, sentences): 
        final = [all([w in x for w in word]) for x in sentences] 
        sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
        return int(len(sent_len))

    idf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.','')
        if each_word not in stop_words:
            if each_word in idf_score:
                idf_score[each_word] = check_sent(each_word, total_sentences)
            else:
                idf_score[each_word] = 1

    # Performing a log and divide
    idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())

    #print(idf_score)

    tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
    #print(tf_idf_score)
    def get_top_n(dict_elem, n):
        result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
        return result
    keyswords = get_top_n(tf_idf_score, 50)
    #return keyswords.keys()
    return list(keyswords.keys())
def getKeyWordPercentage(og,stud_ans):    
    from .ReturnKeywordsFromParagraph import extractsKeywords
    key1 = extractsKeywords(og)
    key2 = extractsKeywords(stud_ans)
    #print(sum(x == y for x, y in zip(key1, key2)))
    #print(key1)
    #print(key2)
    originalSize = len(key1)
    count = 0
    for k1 in key1:
        c= 0
        for k2 in key2:        
            if k1==k2:
                c= c+1
        count= count+c        
            
    keyPercentage = (count/originalSize)*100
    print("key percentage -", keyPercentage)
    return keyPercentage




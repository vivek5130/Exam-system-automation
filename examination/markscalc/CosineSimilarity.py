from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def findingCosineSimilarity(X, Y):
    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y)
    # sw contains the list of stopwords
    sw = stopwords.words('english') 
    l1 =[];l2 =[]
    # remove stop words from the string
    X_set = {w for w in X_list if not w in sw} 
    Y_set = {w for w in Y_list if not w in sw}  
    # form a set containing keywords of both strings 
    rvector = X_set.union(Y_set) 
    for w in rvector:
        if w in X_set: l1.append(1) # create a vector
        else: l1.append(0)
        if w in Y_set: l2.append(1)
        else: l2.append(0)
    c = 0  
    # cosine formula 
    for i in range(len(rvector)):
            c+= l1[i]*l2[i]
    try:
        cosine = c / float((sum(l1)*sum(l2))**0.5)
    except:
        return 0
    print("cosine -", cosine*100)
    return cosine*100

    

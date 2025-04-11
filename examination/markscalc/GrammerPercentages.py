# A function that compares two texts and returns 
# the number of matches and differences
def compare(text1, text2):  
    l1 = text1.split()
    l2 = text2.split()
    good = 0
    bad = 0
    for i in range(0, len(l1)):
        if l1[i] != l2[i]:
            bad += 1
        else:
            good += 1
    return (good, bad)

# Helper function to calculate the percentage of misspelled words
def percentageOfBad(x):
    return (x[1] / (x[0] + x[1])) * 100
def calculateGrammerPercentage(text):
    from textblob import TextBlob
    t3 = TextBlob(text).correct()
    originalCompCorrected = compare(t3,text)
    #print("Original compared to corrected ", originalCompCorrected)
    v1 = 100 - percentageOfBad(originalCompCorrected)
    print("grammar percent -", v1)
    return v1

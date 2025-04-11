# def calculatePOSPercentage(text):
#     import language_check
#     # Mention the language keyword
#     tool = language_check.LanguageTool('en-US')
#     i = 0
#     fin = text.split('.')
#     for line in fin:
#         matches = tool.check(line)
#         i = i + len(matches)     
#         pass
#     # prints total mistakes which are found 
#     # from the document
#     #print("No. of mistakes found in document is ", i)
#     #l = len(fin)
#     #print(l)
#     #print("Total Length=",l)
#     # prints mistake one by one 
#     #for mistake in matches:
#         #print(mistake)
#         #print()
#     temp = 0.3*i
#     totalPercentage = 100-temp
#     return totalPercentage
    
#--------------------------

from textblob import TextBlob

def calculatePOSPercentage(text):
    blob = TextBlob(text)
    corrections = len([word for word, pos in blob.tags if pos == 'VB'])  # just an example for verb checking
    temp = 0.3 * corrections
    totalPercentage = 100 - temp
    print("pos-",totalPercentage)
    return totalPercentage


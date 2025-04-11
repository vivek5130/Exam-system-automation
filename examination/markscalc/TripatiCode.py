# originalAnswer = 'Naive Bayes is a kind of classifier which uses the Bayes Theorem. It predicts membership probabilities for each class such as the probability that given record or data point belongs to a particular class. The class with the highest probability is considered as the most likely class'
# stud_ans = 'Naive bayes is Classification technique, uses here based on one variable we need to find another one. so to work with prediction naive byes we should know about its fetures and number of parameter of the target variables so that we can get the proper answers and there is scalableity to recudes the first function and its hot codeing'
# stud_ans = 'Naive Bayes is a kind of classifier which uses the Bayes Theorem. It predicts membership probabilities for each class such as the probability that given record or data point belongs to a particular class. The class with the highest probability is considered as the most likely class'
class CalculateMarks():
    def myMarksCalcs(self,originalAnswer,stud_ans):
        # Total marks for the answer is 10
        # Step 1
        og = originalAnswer.lower()
        stud_ans = stud_ans.lower()



        # Step 5  4 marks
        from .CosineSimilarity import findingCosineSimilarity
        ot_len = og.split(" ")
        std_len = og.split(" ")
        o1 = len(ot_len)
        s1 = len(std_len)
        o11 = o1/2
        
        cosineSimilarity = findingCosineSimilarity(og, stud_ans)
        s5 = (4 / 100) * cosineSimilarity
        if(s5>2.0 and  o11<s1):
            print('Cosine Similarity:', cosineSimilarity, 'S5:', s5)
            # Step 2  For Step2 2 marks
            from .GrammerPercentages import calculateGrammerPercentage
            gramPercentage = calculateGrammerPercentage(stud_ans)
            s2 = (2 / 100) * gramPercentage

            print('Grammer Percentage %=', gramPercentage, '%', 'S2=', s2)

            # Step 3 2marks
            from .PartsofSpeechDRK import calculatePOSPercentage
            pos = calculatePOSPercentage(stud_ans)
            s3 = (2 / 100) * pos
            print('POS %=', pos, "S3=", s3)

            # Step 4 # 2marks
            from .ReturnKeywordsFromParagraph import getKeyWordPercentage
            keywordPercentage = getKeyWordPercentage(og, stud_ans)
            s4 = (2 / 100) * keywordPercentage
            print('Keyword Compare %=', keywordPercentage, 'S4:', s4)

        

            total = s2 + s3 + s4 + s5
            total = round(total, 1)
            print('Total Marks :', total)
            return total
        else:
            print("0 ended")
            return 0






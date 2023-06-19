import math
error = 0.00001
#value = 2
#start = 0
#end = value

def come_back_question_challenge_one(value,start,end):
    mid = (end+start)/2
    if abs(mid*mid - value) >= error:
        if mid*mid>value:
            end=mid
            return come_back_question_challenge_one(value,start,end)
        else:
            start=mid
            return come_back_question_challenge_one(value,start,end)
    else:
        print(mid)
        print(math.sqrt(2))

come_back_question_challenge_one(2,0,2)

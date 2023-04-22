"""Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.

The criteria for a candidate to be qualified in the coding interview is:

The candidate should have complete all the questions.
The maximum time given to complete the interview is 120 minutes.
The maximum time given for very easy questions is 5 minutes each.
The maximum time given for easy questions is 10 minutes each.
The maximum time given for medium questions is 15 minutes each.
The maximum time given for hard questions is 20 minutes each.
If all the above conditions are satisfied, return "qualified", else return "disqualified".

You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.

Given a list , in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].

The maximum time to complete the interview includes a buffer time of 20 minutes."""

candidate=[5,5,10,10,15,15,5,20]

def Is_qualified(Tasks, totalTime):
    if (Tasks[0] > 5):
        print("Candidate was disqalified because the the easiest question took him too much time to answer..")
        return "disqualified"
    elif (Tasks[1] > 5):
        print("Candidate was disqalified because the the easiest question took him too much time to answer..")
        return "disqualified"
    elif (Tasks[2] > 10):
        print("Candidate was disqalified because easy question took him too much time to answer..")
        return "disqualified"
    elif (Tasks[3] > 15):
        print("Candidate was disqalified because easy question took him too much time to answer..")
        return "disqualified"
    elif (Tasks[4] > 15):
        print("Candidate was disqalified because medium question took him too much time to answer..")
        return "disqualified"
    elif (Tasks[1] > 20):
        print("Candidate was disqalified because medium question took him too much time to answer..")
        return "disqualified"
    elif (Tasks[2] > 20):
        print("Candidate was disqalified because hard question took him too much time to answer..")
        return "disqualified"
    elif (Tasks[3] > 20):
        print("Candidate was disqalified because hard question took him too much time to answer..")
        return "disqualified"
    elif (sum(Tasks)>100):
        print("Candidate was disqalified because questions took him too much time to answer..")
        return "disqualified"
    elif (totalTime > 120):
        print("Candidate was disqalified because the whole interviev took too long..")
        return "disqualified"
    else:
        print("Candidate has met the necesery conditions")
        return "qualified"
    
    
    
Is_qualified(candidate,110)



from StackPostfix import *
# Driver program to test above function
exp = "231*+9-"
obj = Evaluate(len(exp))
print("postfix evaluation:for :"+exp+" is ",(obj.evaluatePostfix(exp)))

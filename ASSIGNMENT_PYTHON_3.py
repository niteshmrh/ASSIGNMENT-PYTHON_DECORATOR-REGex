"""
Create a class that takes a list of n element such that n is odd number, take input from user, and contains the function
that returns a list in which at index 0, mean of list; at index 1, median of list; at index 2, mode of tuple.
[Hint: mean refer to average, median refer to the middle value and mode refers to the element with highest frequency, if
 no element is repeated then list does not have mode hence list will contain None for mode]
"""


class StaticsProb:
    def InputList(self, n):
        list1 = []
        for i in range(0, n):
            ele = int(input())
            list1.append(ele)
        return list1

    def calculator(self, list1, n):
        self.list1 = list1
        self.n = n
        list2 = []
        sum = 0
        for i in self.list1:
            sum += i
        mean = sum / self.n
        median = self.n // 2 + 1
        mode = max(self.list1)
        list2.append(mean)
        list2.append(self.list1[median-1])
        list2.append(mode)
        print(list2)


if __name__ == "__main__":
    n = int(input("Enter the Number of Element you want to insert(odd number requied) :"))
    x = StaticsProb()
    y=x.InputList(n)
    print("Your Inserted List is :",y)
    x.calculator(y,n)

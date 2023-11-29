"""Module providing comparing 2 lists()."""
class AverageCounter:
    """Class count average meaning of list()"""
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return f'{self.my_list}'

    def average_of_list(self):
        """Count average meaning of list()"""
        if len(self.my_list) > 0:
            return sum(self.my_list) / len(self.my_list)
        else:
            raise ValueError("Пустой список")

class ListComparator:
    """Class compare average meanings of 2 lists()"""
    def __init__(self, test_list1, test_list2):
        self.average1 = AverageCounter(test_list1).average_of_list()
        self.average2 = AverageCounter(test_list2).average_of_list()

    def compare_of_lists(self):
        """Compare average meanings of 2 lists()"""
        if self.average1 > self.average2:
            return "Первый список имеет большее среднее значение"
        elif self.average1 < self.average2:
            return "Второй список имеет большее среднее значение"
        elif self.average1 == self.average2:
            return "Средние значения равны"

# my_list1 = [1,2,3,4,5]
# my_list2 = [6,7,8,9,10]
# my_list3 = []
# my_list4 = [-6,-7,-8,-9,-10]
# avg1 = AverageCounter(my_list1).average_of_list()
# avg2 = AverageCounter(my_list2).average_of_list()
# avg4 = AverageCounter(my_list4).average_of_list()
# print(f'AVG of {my_list1} is {avg1}')
# print(f'AVG of {my_list2} is {avg2}')
# print(f'AVG of {my_list4} is {avg4}')

# print(List_comparator(my_list1,my_list2).compare_of_lists())

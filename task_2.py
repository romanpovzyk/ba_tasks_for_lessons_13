class Mathematician:
    def __init__(self):
        self.list_for_square = []
        self.list_for_square_result = []
        self.list_for_neg = []
        self.list_for_neg_result = []
        self.list_for_years = []
        self.list_for_years_result = []

    def square_nums(self, list_for_square):
        for num in self.list_for_square:
            self.list_for_square_result.append(num*num)
            return list_for_square_result

    def remove_positives(self, list_for_neg):
        for num in self.list_for_neg:
            if num < 0:
                self.list_for_neg_result.append(num)
            return list_for_neg_result

    def filter_leaps(self, list_for_years):
        for num in self.list_for_years:
            if num % 4:
                self.list_for_years_result.append(num)
            return list_for_years_result


m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))


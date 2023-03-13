"""
Create a function that takes a Roman numeral as its argument
and returns its value
as a numeric decimal integer.
You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit
of the number
to be encoded separately, starting with the leftmost digit and skipping
any 0s.
So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and
2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral
for 1666, "MDCLXVI",
uses each letter in descending order.

Example:

solution('XXI') # should return 21
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000 """


def solution(roman):
    roman_letters = {"I": 1, "V": 5, "X": 10, "L": 50,
                     "C": 100, "D": 500, "M": 1000}
    sum_ = 0
    previous_ = 0
    for element in roman:
        if roman_letters[element] > previous_:
            sum_ = sum_ - previous_ + roman_letters[element] - previous_
        else:
            sum_ += roman_letters[element]
        previous_ = roman_letters[element]
    return sum_


"""
Let us consider this example (array written in general format):

ls = [0, 1, 3, 6, 10]

Its following parts:

ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

The function parts_sums (or its variants in other languages) will take
as parameter a list ls and return a list of the sums of its parts
as defined above.

Other Examples:
ls = [1, 2, 3, 4, 5, 6]
parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504,
                   9291414, 9291270, 2581057, 2580168, 2579358,0]
Notes
Take a look at performance: some lists have thousands of elements.
Please ask before translating.
"""


def parts_sums(list_):

    n = len(list_)
    sum_ = 0
    for bypass in range(0, n):
        sum_ += list_[bypass]
    previous = 0
    for bypass in range(0, n):
        previous1 = list_[bypass]
        list_[bypass] = sum_ - previous
        previous += previous1
    return list_ + [0]


if __name__ == '__main__':
    print(solution("MCMXC"))
    print(parts_sums([1, 2, 3, 4, 5, 6]))

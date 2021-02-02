#URL: https://www.hackerrank.com/challenges/validate-a-roman-number/problem
regex_pattern = r"M{,3}(CD|D?C{,3}|C{,3}|CM)(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.
import re
print(str(bool(re.match(regex_pattern, input()))))

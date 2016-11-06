#https://www.hackerrank.com/challenges/string-validators
inp = raw_input()
print any([inp_.isalnum() for inp_ in inp])
print any([inp_.isalpha() for inp_ in inp])
print any([inp_.isdigit() for inp_ in inp])
print any([inp_.islower() for inp_ in inp])
print any([inp_.isupper() for inp_ in inp])
import re

def arithmetic_arranger(problems):
# test = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

  # refornonnums = [^\s0-9.+-]

  for problem in problems:
    if(re.search("[^\s0-9.+-]",problem)):
      return "Error: Numbers must only contain digits."
    print('all good')

  return
import re

def arithmetic_arranger(problems, solve = False):
  if(len(problems) > 5):
    return "Error: Too many problems."

  firstLine = ""
  secondLine = ""
  hyphenLine = ""
  totals = ""
  arranged = ""
  
  for problem in problems:
    if(re.search("[^\s0-9.+-]", problem)):
      if(re.search("[*]", problem) or re.search("[/]",problem)):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    firstNum = problem.split(" ")[0]
    secondNum = problem.split(" ")[2]
    operator = problem.split(" ")[1]

    if(len(firstNum) > 4 or len(secondNum) > 4):
      return "Error: Numbers cannot be more than four digits."

    sum = ""
    if(operator == "+"):
      sum = str(int(firstNum) + int(secondNum))
    elif(operator == "-"):
      sum = str(int(firstNum) - int(secondNum))

    myLength =max(len(firstNum), len(secondNum)) +2
    top = str(firstNum).rjust(myLength)
    # don't forget to add operator here
    bottom = operator + str(secondNum).rjust(myLength-1)
    result = str(sum).rjust(myLength)

    line = ""
    for space in range(myLength):
      line += "-"
    
    if(problem != problems[-1]):
      firstLine += top + "    "
      secondLine += bottom + "    "
      hyphenLine += line + "    "
      totals += result + "    "
    else:
      firstLine += top
      secondLine += bottom
      hyphenLine += line
      totals += result

  if(solve):
    print('it true')
    arranged = firstLine + "\n" + secondLine + "\n" + hyphenLine + "\n" + totals
  else:
    arranged = firstLine + "\n" + secondLine + "\n" + hyphenLine
  return arranged

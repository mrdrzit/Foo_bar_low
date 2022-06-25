import _thread as t

def solution(area):
  '''solution(area) takes as its input a single unit of measure representing the total area of solar panels you have 
  (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make out of those panels, 
  starting with the largest squares first. So, solution(12) would return [9, 1, 1, 1].'''

  # X^2 so that X < 12
  # Rephrasing: What is the largest integer that does not exceed X and have remainder > 0 for the first number?
  max, rem = largest(area)
  pass

def largest(x):
  tmp = 0
  y = 0
  while True:
    if y**2 >= x:
      largest = tmp
      remainder = x - largest
      break
    tmp = y
    y += 1
  return largest, remainder



solution(15324)
def calculate_average(score1: float, score2: float , score3: float ):
  return (score1 + score2 + score3) / 3.0

def get_performance(average: float ):
  if average >= 85:
     return "Mastrery"
  elif average >= 70:
     return "Devloping"
  else:
     return "Needs Review"

def is_eligible(avergae: float, completed_task: int):
  return average >= 85 and completed_task >= 3

score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))

completed_task = int(input("Completed Tasks: "))
average = calculate_average(score1, score2, score3 )
performance = get_performance(average)
eligible = is_eligible(average, completed_task)

print(f"Average: {average:.2f}")
print(f"Performance: {performance}")
print(f"Eligible for Challenge: {eligible}")

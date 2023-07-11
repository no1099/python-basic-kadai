class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def check_adult(self):
    if self.age >= 20:
      print(f"{self.name}さんは大人です。") 
    else:
      print(f"{self.name}さんは大人ではありません。")

personal_data = {"侍一郎": 30, "侍二郎": 20, "侍三郎": 10}
for name, age in personal_data.items():
  user = Human(name, age)
  user.check_adult()
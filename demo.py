class Person:

  def __init__(self, firstname, secondname, age, password) -> None:
    #public attributes
    self.firstname = firstname
    self.secondname = secondname
    self.age = age
    #private attribute
    self.__password = password

  def get_full_name(self):
    return self.firstname + " " + self.secondname

  def get_password(self):
    return self.__password


john = Person("john", "krasinski", 20, 1234)
print(john.get_password)

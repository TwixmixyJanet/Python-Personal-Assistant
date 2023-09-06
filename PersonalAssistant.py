# Give the class a name
class PersonalAssistant:
  # Add an __init__ function here
  def __init__(self, todos, birthdays):

    self.todos = todos
    self.birthdays = birthdays

    # Complete the get_contact function code
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "That contact does not exist."

  def add_todo(self,new_item):
    self.todos.append(new_item)

  def remove_todo(self,todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
      return f'{todo_item} was removed'
    else:
      print("To-do is not in the list!")

  def get_todos(self):
    return self.todos

  def get_birthdays(self):
    return self.birthdays

  def get_birthday(self, name):
    if name in self.birthdays:
      return f"{name}'s birthday is on {self.birthdays[name]}."
    else:
      return "Can't find birthday for this person."

  def add_birthday(self, name, date):
    if name in self.birthdays:
      return f"You already have a birthday for {name}"
    else:
      self.birthdays[name] = date
      return f"{name}'s birthday has been added."

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      return f"{name}'s birthday has been removed."
    else:
      return "That birthday is not in the list!"


      
#    if name == "Janet":
#      return "Janet's birthday is 09/24/1985"
#    elif name == "Rowan":
#      return "Rowan's birthday is 08/08/1987"
#    elif name == "Winona":
#      return "Winona's birthday is 10/10/2020"
#    else:
#      return "That birthday is not in the system"


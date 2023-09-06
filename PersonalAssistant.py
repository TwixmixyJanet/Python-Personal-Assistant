# Give the class a name
class PersonalAssistant:
  # Add an __init__ function here
  def __init__(self, todos, birthdays, contacts):

    self.todos = todos
    self.birthdays = birthdays
    self.contacts = contacts

# TO-DO LIST
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

# BIRTHDAY LIST
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

# CONTACT LIST
  def get_contact(self, name):
    if name in self.contacts:
      return f"{name} is a {self.contacts[name]}."
    else:
      return "Can't find contact for this person."

  def add_contact(self, name, position):
    if name in self.contacts:
      return f"You already have a contact for {name}"
    else:
      self.contacts[name] = position
      return f"{name}'s contact has been added."

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name)
      return f"{name}'s contact has been removed."
    else:
      return "That contact is not in the list!"

  def get_contacts(self):
    return self.contacts
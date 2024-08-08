import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def add_reminder(reminder):
  if reminder is not None:
    app_tables.reminder_tbl.add_row(**reminder) #task=reminder('task'), status=False)

@anvil.server.callable
def get_reminders(username):
  return app_tables.reminder_tbl.search(
    user=username,
    tables.order_by("status", ascending=True)
  )

@anvil.server.callable
def update_reminder_status(reminder, new_status):
  # print(f"updating reminder {reminder['task']} {new_status}")
  # get the task from the reminders table
  row = app_tables.reminder_tbl.get(task=reminder['task'])
  
  if row: # if exist, update status of reminder
    row['status'] = new_status
    
@anvil.server.callable
def update_reminder(old_reminder, new_reminder):
  # print(f"updating reminder {reminder['task']} {new_status}")
  # get the task from the reminders table
  print(old_reminder)
  row = app_tables.reminder_tbl.get(task=old_reminder)

  if row: # if exist, update task description and status of reminder
    row['task']   = new_reminder['task']
    row['status'] = new_reminder['status']

@anvil.server.callable
def delete_reminder(reminder):
  reminder.delete()
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
def add_reminder(reminder, current_user):
  if reminder is not None:
    current_user = app_tables.user_tbl.search(username=current_user)
    # print(*current_user[0]['username'])
  
    if current_user is not None:
      app_tables.reminder_tbl.add_row(**reminder, user=current_user[0]) #task=reminder('task'), status=False)

@anvil.server.callable
def get_reminders(username):
  current_user = app_tables.user_tbl.search(username=username)
  # print(*current_user[0]['username'])

  if current_user is not None:
    return app_tables.reminder_tbl.search(
      tables.order_by("status", ascending=True),
      user=current_user[0]
    )

@anvil.server.callable
def update_reminder_status(reminder, new_status):
  # print(f"updating reminder {reminder['task']} {new_status}")
  # get the task from the reminders table
  row = app_tables.reminder_tbl.get(task=reminder['task'], user=reminder['user'])
  
  if row: # if exist, update status of reminder
    row['status'] = new_status
    
@anvil.server.callable
def update_reminder(old_reminder, new_reminder):
  # print(f"updating reminder {reminder['task']} {new_status}")
  # get the task from the reminders table
  print(old_reminder)
  row = app_tables.reminder_tbl.get(task=old_reminder, user=new_reminder['user'])

  if row: # if exist, update task description and status of reminder
    row['task']   = new_reminder['task']
    row['status'] = new_reminder['status']
    row['due']    = new_reminder['due']

@anvil.server.callable
def delete_reminder(reminder):
  reminder.delete()

@anvil.server.callable
def update_due_date(reminder, new_date):
  # print(f"updating reminder {reminder['task']} {new_status}")
  # get the task from the reminders table
  row = app_tables.reminder_tbl.get(task=reminder['task'], user=reminder['user'])
  
  if row: # if exist, update status of reminder
    row['due'] = new_date
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
def get_reminders():
  return app_tables.reminder_tbl.search(
    tables.order_by("status", ascending=True)
  )

@anvil.server.callable
def update_reminder(reminder):
  if app_tables.reminder_tbl.has_row(reminder['task']):
    row = app_tables.reminder_tbl.search(task=reminder['task'])
    row['task'] = reminder['task']
    row['status'] = reminder['status']
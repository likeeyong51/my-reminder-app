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
def add_reminders(desc):
  print(desc)
  app_tables.reminder_tbl.add_row(*desc) #description=desc, done=False)

@anvil.server.callable
def get_reminders():
  return app_tables.reminder_tbl.search(
    tables.order_by("done", ascending=True)
  )

@anvil.server.callable
def update_reminders(desc, done):
  if app_tables.reminder_tbl.has_row(desc):
    pass
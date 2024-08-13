import anvil.email
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
def create_user(username, password):
  row = app_tables.user_tbl.search(username=username, password=password)

  # check if user exists
  if len(row) == 1:
    return False # user exists 

  # add new user to the user table
  app_tables.user_tbl.add_row(username=username, password=password)
  return True

@anvil.server.callable
def authenticate_user(username, password):
  row = app_tables.user_tbl.search(username=username, password=password)

    # if user exist
  if len(row) == 1:
    return True # found

  # user does not exist yet
  return False # not found
from ._anvil_designer import My_RemindersTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class My_Reminders(My_RemindersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    for row in app_tables.reminder_tbl.search(tables.app_tables.reminder_tbl):
      rd = get_reminder()

    # Any code you write here will run before the form opens.

  def add_reminder_click(self, **event_args):
    """This method is called when the button is clicked"""
    


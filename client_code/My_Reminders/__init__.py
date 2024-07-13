from ._anvil_designer import My_RemindersTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Edit_reminder import Edit_reminder

class My_Reminders(My_RemindersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # populate reminders
    self.refresh_reminders()

    # Any code you write here will run before the form opens.

  def add_reminder_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Initialise an empty dictionary to store the user inputs
    new_reminder = {}
    # open an alert displaying the ARticleEdit form
    save_clicked = alert(
      content = Edit_reminder(item=new_reminder),
      title="Add Reminder",
      large=True,
      buttons=[("Save", True),("Cancel", False)]
    )
    
    # If the alert returned 'True', the save button was clicked
    if save_clicked:
      anvil.server.call('add_reminder', new_reminder)
      self.refresh_reminders()
    

  def refresh_reminders(self):
    self.reminders_pnl.items = anvil.server.call('get_reminders')

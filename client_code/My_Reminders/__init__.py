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

    self.item['username'] = properties['username']
    #print(self.item['username'])
    # populate reminders
    self.refresh_reminders()

    # set delete_reminder event handler to the reminders_pnl
    self.reminders_pnl.set_event_handler('x-delete-reminder', self.delete_reminder)
    
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
      # Then, add new reminder to the database
      anvil.server.call('add_reminder', new_reminder, self.item['username'])
      self.refresh_reminders()
    

  def refresh_reminders(self):
    # populate reminders_pnl items with the list of reminders
    #print(self.item['username'])
    self.reminders_pnl.items = anvil.server.call('get_reminders', self.item['username'])
    

  def delete_reminder(self, reminder, **event_args):
    anvil.server.call('delete_reminder', reminder)
    self.refresh_reminders()

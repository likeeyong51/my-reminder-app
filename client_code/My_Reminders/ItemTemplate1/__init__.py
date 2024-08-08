from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Edit_reminder import Edit_reminder

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
   
  def status_chk_change(self, **event_args):
    """update the status of a reminder"""
    # print(f"Checked status: {self.status_chk.checked}")
    
    anvil.server.call('update_reminder_status', self.item, self.status_chk.checked)

  def delete_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if confirm("Are you sure you want to delete?"):
      # anvil.server.call('delete_reminder', self.item)
      self.parent.raise_event('x-delete-reminder', reminder=self.item)

  def update_btn_click(self, **event_args):
    """update existing reminder"""
    old_reminder = self.item['task']
    new_reminder = dict(self.item)
    
    print(old_reminder)
    # open an alert displaying the ArticleEdit form
    save_clicked = alert(
      content = Edit_reminder(item=new_reminder),
      title   = "Update Reminder",
      large   = True,
      buttons = [("Save", True),("Cancel", False)]
    )

    if save_clicked:
      print(new_reminder)
      self.task_lbl.text      = new_reminder['task']
      self.status_chk.checked = new_reminder['status']
      self.due_dpk.date       = new_reminder['due']
      anvil.server.call('update_reminder', old_reminder, new_reminder)

  def due_dpk_change(self, **event_args):
    """update due date"""
    anvil.server.call('update_due_date', self.item, self.due_dpk.date)
    



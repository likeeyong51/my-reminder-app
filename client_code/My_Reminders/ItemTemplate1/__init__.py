from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def status_chk_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    print(f"Checked status: {self.status_chk.checked}")
    
    # if self.status_chk.checked:
    anvil.server.call('update_reminder', dict(self.item), self.status_chk.checked)

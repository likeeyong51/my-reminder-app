from ._anvil_designer import My_RemindersTemplate
from anvil import *


class My_Reminders(My_RemindersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

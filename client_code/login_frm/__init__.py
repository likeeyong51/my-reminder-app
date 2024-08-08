from ._anvil_designer import login_frmTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class login_frm(login_frmTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def signup_chk_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.signup_chk.checked:
      if self.username_txb.text != '' and self.password_txb.text != '':
        # app_tables.user_tbl.add_row(username=self.item['username'], password=self.item['password'])
        anvil.server.call('create_user', self.item['username'], self.item['password'])
        if anvil.server.call('authenticate_user', self.item['username'], self.item['password']):
          self.reset_form()
          alert('You are signed up! Please attempt a login now')
      else:
        alert("Please enter a username and password")

  def sign_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    # user_exist = anvil.server.call('authenticate_user', self.username_txb.text, self.password_txb.text)
    user_exist = anvil.server.call('authenticate_user', self.item['username'], self.item['password'])

    if user_exist:
      alert("Welcome to your reminder app")
      open_form('My_Reminders', username=self.item['username'])
    else:
      alert("Error: please check your login credentials and try again...")

  def reset_form(self):
    self.username_txb.text = ''
    self.password_txb.text = ''
    self.signup_chk.checked = False
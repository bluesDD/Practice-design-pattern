import os
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

class SpreadSheet:
  def __init__(self):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    file_dir = os.path.dirname(__file__)
    credential_file = "etcpasswd-spreadsheet-8f98ea5f479c.json"
    credential_file_path = os.path.join(file_dir, credential_file)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file_path, scope)
    googleAPI = gspread.authorize(credentials)
    SPREADSHEET_KEY = "1nQw7UPYlvtKth0opm03jVai_IQpEGqMdOfIhlQgav1U"
    self.__worksheet = googleAPI.open_by_key(SPREADSHEET_KEY).sheet1

  def update_single_cell(self, cell: str, text: str):
    self.__worksheet.update_acell(cell, text)

function get_diff() {
  const array1 = [1, 2, 3, 4, 5, 6];
  const array2 = [1, 2, 3, 4];


  array3 = array1.filter(i => array2.indexOf(i) == -1)
  return array3; // [5, 6]
}


function get_sheet_data (sheet_name) {
  const sheet = SpreadsheetApp.openById("");
  const data = sheet.getSheetByName(sheet_name);
  const data2 = data.getRange(1, 1, sheet.getLastRow(), sheet.getLastColumn()).getValues();
  Logger.log(data2);
  
}

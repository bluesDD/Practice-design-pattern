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

function get_today () {
  var date = new Date();
  var today = Utilities.formatDate(date, 'Asia/Tokyo', 'yyyyMMdd');
  return today;
}

function diff_date(d1="2020/11/15") {
  var now = Moment.moment();
  var d2 = Moment.moment(d1);
  var d = now.diff(d2, "d");
  Logger.log(d + "日 "); // ログに出力
  return d
}


function get_data_from_rows(row_num=4) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getActiveSheet();
  var rows = sh.getRange(1, row_num, sh.getLastRow()).getValues();
  Logger.log(Array.prototype.concat.apply([], rows));

}

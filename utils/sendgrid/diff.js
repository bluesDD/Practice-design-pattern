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

function diff_date() {
  var dt = Math.abs(d1.getTime() - d2.getTime()); // ミリ秒数値を引き算
  var d = dt / (1000 * 60 * 60 * 24); // １日のミリ秒数で割り算
  Logger.log(d + "日 "); // ログに出力
  }

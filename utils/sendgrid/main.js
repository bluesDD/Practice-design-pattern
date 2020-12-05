function main() {
  var row_num = 4
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getActiveSheet();
  var rows = sh.getRange(1, row_num, sh.getLastRow()).getValues();
  var dates = Array.prototype.concat.apply([], rows);
  var expires_in_30 = false
  var expires_in_40 = false

  dates.map(function(value) {
    var now = Moment.moment();
    var expired_day = Moment.moment(value);
    var expires_in = now.diff(expired_day, "d");
    if (expires_in < 30) {
      expires_in_30 = true
    }
    if (expires_in < 40) {
      expires_in_40 = true
    }
  })
  
  if (expires_in_30) {
    notify_slack(30)
  }
  if (expires_in_40) {
    notify_slack(40)
  }
  
}

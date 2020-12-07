function main() {
  var expiry_date_row = 4
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getActiveSheet();
  var row_items = sh.getRange(1, expiry_date_row, sh.getLastRow()).getValues();
  var expiry_dates = Array.prototype.concat.apply([], row_items);
  var expires_in_30 = false
  var expires_in_40 = false

  expiry_dates.map(function(value) {
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

function caliculate_remaining_days(days, base_date) {
  var no_target_items = 0
  if (days < base_date) {
    return days
  }
  return no_target_items
}

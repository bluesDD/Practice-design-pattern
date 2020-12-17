function main() {
  var expiry_date_row = 4
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getActiveSheet();
  var row_items = sh.getRange(1, expiry_date_row, sh.getLastRow()).getValues();
  var expiry_dates = Array.prototype.concat.apply([], row_items);
  var remaining_days = 0;

  expiry_dates.map(function(value) {
    var now = Moment.moment();
    var expired_day = Moment.moment(value);
    var expires_in = now.diff(expired_day, "d");
    if (expires_in < 30) {
      remaining_days = 30
    }
    if (expires_in < 40) {
      remaining_days = 40
    }
  })
  
  if (remaining_days) {
    notify_slack(remaining_days)
  }
  
}

function caliculate_remaining_days(days, base_date) {
  var no_target_items = 0
  if (days < base_date) {
    return days
  }
  return no_target_items
}

function set_property(key, value) {
  var document_properties = PropertiesService.getDocumentProperties();
  document_properties.setProperty(key ,value)
}

function get_property(key) {
  var document_properties = PropertiesService.getDocumentProperties();
  return document_properties.getProperty(key)
}

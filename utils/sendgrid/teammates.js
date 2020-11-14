SENDGRID_TEAMMATES_READONLY_API_KEY = ""
SENDGRID_BASE_ENDPOINT = "https://api.sendgrid.com/v3"
SENDGRID_TEAMMATES_PATH = "/teammates"
SENDGRID_TEAMMATES_ENDPOINT = SENDGRID_BASE_ENDPOINT + SENDGRID_TEAMMATES_PATH


function retrieve_teammates() {
  Logger.log("Starting Retrieve Teammates...");

  try {
    const res =   UrlFetchApp.fetch(SENDGRID_TEAMMATES_ENDPOINT, {
      method: 'GET',
      headers: { "Content-Type": 'application/json',
                "Authorization": "Bearer "+ SENDGRID_TEAMMATES_READONLY_API_KEY}
    });
    
    const res_text = JSON.parse(res.getContentText());
    
    Logger.log("Retrieve teammates completed!");
    var teammates = [];
    for (var i in res_text.result) {
      teammates.push(Object.values(res_text.result[i]));
    }

    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sh = ss.getActiveSheet();
    var rows = teammates.length;
    var cols = teammates[0].length;
    
    sh.getRange(1,1,rows,cols).setValues(teammates);

  } catch(e) {
    Logger.log("Retrieving teammates failed...")
    Logger.log(e)
  }
}


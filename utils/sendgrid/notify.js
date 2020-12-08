function notify_slack(message) {
  var post_url  = "";
  var slack_message = message + "日以内に期限が切れる証明書・ドメインがあります！→ https://docs.google.com/spreadsheets/d/1aN96iDo_9we9t_LQZ4oxrUna-jQIXvIeie59Ll5fZps/edit#gid=827799759"

  var options = {
    "method" : "POST",
    "payload" : JSON.stringify({
      "text": slack_message
    })
  }
  try {
    UrlFetchApp.fetch(post_url, options);
  } catch (e) {
    Logger.log(e)
  }
}

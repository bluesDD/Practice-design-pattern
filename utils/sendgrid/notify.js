function notifySlack() {
  let postUrl  = ""
  let userName = "テストbotくん"   // Slackに通知する時の名前になります
  let icon     = ":innocent:"    // 表示されるアイコン
  let message  = "これはGASからのテストメッセージです" // 送信するメッセージ
 
  // ここで以下をオプションに設定できます
  // username(通知者の名前)
  // icon_emoji(アイコン)
  // text (送信するメッセージ)
  let jsonData = {
    "username" : userName,
    "icon_emoji" : icon,
    "text" : message
  }  
 
  // 上の送信内容を設定  
  let payload = JSON.stringify(jsonData)
 
  // オプションを設定
  let options =
  {
    "method" : "post",
    "contentType" : "application/json",
    "payload" : payload
  };
 
  // Slackに通知する
  UrlFetchApp.fetch(postUrl, options);  
 }

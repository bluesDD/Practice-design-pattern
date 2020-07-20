import http.client
import json

class UserPosts:
  USER_ID = "bluesDD"
  POSTS_COUNT = 10
  PAGE = "1"
  PER_PAGE = "10"

  def __init__(self):
    connection = http.client.HTTPSConnection("qiita.com", 443)
    connection.request("GET", "/api/v2/users/" + self.USER_ID + "/items?page=" + self.PAGE + "&per_page=" + self.PER_PAGE)
    res = connection.getresponse()
    print(res.status, res.reason)
    data = res.read().decode("utf-8")

    json_res_data = json.loads(data)

    for i in range(self.POSTS_COUNT):
      print (json_res_data[i]["created_at"] + json_res_data[i]["title"] + "Likes" + str(json_res_data[i]["likes_count"])
      list = []
      index = 0
      for t in json_res_data[i]["tags"]: 
        list.append(json_res_data[i]["tags"][index]["name"])
        index += 1
      print (list)
    connection.close()

if __name__ == "__main__":
  up = UserPosts()


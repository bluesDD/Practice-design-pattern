import os
from fetchInfoPasswd import FetchInfoPasswd

script_dir = os.path.dirname(__file__) 
file_name = "dev01-dig-adm_passwd.log"
file_path = os.path.join(script_dir, file_name)


f = open(file_path)

for row in f:
  passwd = FetchInfoPasswd(row)
  print (passwd.fetchPasswd())
f.close()

import glob

class FileNames:
  def getFileNames(file_path):
    return glob.glob(file_path)

f = FileNames
for file in f.getFileNames("./*.md"):
  print(file)

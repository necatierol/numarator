import json
import csv
import shutil
from tempfile import NamedTemporaryFile
from collections import defaultdict

class Data():
  def __init__(self):
    super().__init__()
    self.__readJsonFile()

  def __readJsonFile(self):
    with open('config.json', 'r') as file:
      dataFile = file.read()

    self.data = json.loads(dataFile)

  def getComportSettings(self):
    return self.data["comport_settings"]

  def getUISettings(self):
    return self.data["ui_settings"]

  def getCommands(self):
    return self.data["commands"]

  def getWindowTitle(self):
    return self.data["messages"]["title"]

  def getCreateNumberButtonMessage(self):
    return self.data["messages"]["create_number_button"]

  def getCompanyName(self):
    return self.data["messages"]["company"]

  def getDate(self):
    return self.data["date"]

  def getGrouppedNumbers(self):
    numbers = defaultdict(list)  # each entry of the dict is, by default, an empty list

    with open('data/numbers.csv', 'r') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for row in csvreader:
        numbers[row[0]].append(row[1])

    return numbers

  def createNumber(self):
    new_number = 1
    with open('data/numbers.csv', 'r') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
      rows = list(csvreader)
      if (len(rows) > 0):
        new_number = int(rows[-1][1]) + 1

    with open('data/numbers.csv', 'a') as csvfile:
      csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
      csvwriter.writerow(['#', str(new_number)])

    return new_number

  def getNextNumber(self, key = "A"):
    # numbers = self.getGrouppedNumbers()
    # next_number = int(numbers["#"][:1][0])
    filename = 'data/numbers.csv'
    tempfile = NamedTemporaryFile(mode='w', delete=False)

    next_number = 0
    with open(filename, 'r') as csvfile, tempfile:
      csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
      csvwriter = csv.writer(tempfile, delimiter=',', quotechar='"')

      for row in csvreader:
        if (row[0] == "#" and next_number == 0):
          next_number = int(row[1])
          row[0] = key
        
        csvwriter.writerow(row)

    shutil.move(tempfile.name, filename)
    print("number {} is called by {}".format(next_number, key))

    return next_number

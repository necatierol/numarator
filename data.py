import json
import csv
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

  def getDate(self):
    return self.data["date"]

  def getGrouppedNumbers(self):
    numbers = defaultdict(list)  # each entry of the dict is, by default, an empty list

    with open('data/numbers.csv', 'r') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for row in csvreader:
        numbers[row[0]].append(row[1])

    return numbers
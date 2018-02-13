
import requests


def collect_from_spreadsheet():
    url = 'https://docs.google.com/spreadsheets/d/1S6ZzPISCJNlkHgfiIMnSBOGiRCw1VOC-fApwtYkkOTk/edit#gid=1951913618'


def collect_from_wikia():
    url = 'http://riseofberk.wikia.com/wiki/Dragon_Statistics_Lv124'
    page = requests.get(url)


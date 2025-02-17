# Databricks notebook source
import requests

response = requests.get('http://health.data.ny.gov/api/views/jxy9-yhdk/rows.csv')
csvfile = response.content.decode('utf-8')
dbutils.fs.put("/Volumes/dbacademy/labuser9128531_1739377194/retail/babynames.csv", csvfile, True)
import requests
import aiohttp
import random as r 
import discord
from discord.ext import commands

def otp():
  webook_discord = '' #your webhook discord
  otp = r.randint(50, 250) + r.randint(70,120)
  data = {
    "username" : "OTP Logs",
    "content" : f"{otp}"
}

  result = requests.post(url, json = data)
  otps = input("Verification code : ")
  if otps == otp:
    print("Correct")
    pass
  else:
    exit()

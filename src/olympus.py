import binascii
import hashlib
import requests

class Olympus:
  coalition = 'blue'
  country = 'CJTF_BLUE'
  hostname = 'localhost'
  port = 3001
  username = ''
  password = ''

  def __init__(self, config={}):
    if "hostname" in config:
      self.hostname = config["hostname"]
    if "password" in config:
      self.password = config["password"]
    if "port" in config:
      self.port = config["port"]
    if "username" in config:
      self.username = config["username"]

  def auth_token(self):
    password_digest = hashlib.sha256(self.password.encode()).hexdigest()
    return binascii.b2a_base64(f'{self.username}:{password_digest}'.encode()).decode()
  
  def command(self, command_name, payload):
    arguments = self.common_arguments() | payload
    json = {command_name: arguments}
    return requests.put(self.url(), headers=self.headers(), json=json)

  def common_arguments(self):
    return {
      "coalition": self.coalition,
      "country": self.country,
      "immediate": False,
      "spawnPoints": 0
    }

  def headers(self):
    return {
      'Authorization': f'Basic {self.auth_token().strip()}',
      'Content-Type': 'application/json',
    }

  def url(self):
    return f'http://{self.hostname}:{self.port}/olympus'

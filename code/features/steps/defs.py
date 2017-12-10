from aloe import step
from requests import get


@step(r'user "([^"]*)" has hash "([^"]*)"')
def hash(self, username, hashcode):
  get('http://localhost:8080/mine')

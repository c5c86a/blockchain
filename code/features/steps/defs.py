from aloe import step
from requests import get
from aloe import before
import coverage

@before.all
def before_all():
  coverage.process_startup()

@step(r'user "([^"]*)" has hash "([^"]*)"')
def hash(self, username, hashcode):
  get('http://localhost:8080/mine')

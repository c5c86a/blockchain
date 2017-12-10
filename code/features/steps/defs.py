from aloe import step

@step(r'user "([^"]*)" has hash "([^"]*)"')
def hash(self, username, hashcode):
  pass

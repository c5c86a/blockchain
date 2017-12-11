from aloe import step
from requests import get
from tinyblockchain import app



@step(r'user "([^"]*)" has hash "([^"]*)"')
def hash(self, username, hashcode):
  peer_nodes = []

  bob = app.Node()
  peer_nodes.append(bob)
  alice = app.Node()
  peer_nodes.append(alice)
  trudy = app.Node()
  peer_nodes.append(trudy)

  bob.start(peer_nodes)
  alice.start(peer_nodes)
  trudy.start(peer_nodes)

  bob.post_transaction('{"from": "alice", "to":"bob", "amount": 3}')
  alice.post_transaction('{"from": "alice", "to":"pete", "amount": 5}')
  trudy.post_transaction('{"from": "jeff", "to":"joe", "amount": 5}')

  bob.get_mine()
  alice.get_mine()
  trudy.get_mine()

  assert bob.get_blocks() == alice.get_blocks(), alice.get_blocks()
  assert trudy.get_blocks() == alice.get_blocks()


  # get('http://localhost:5001/blocks')

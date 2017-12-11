import json

import falcon


class TransactionResource(object):
    def __init__(self, state):
        self.state = state

    def on_post(self, req, resp, **params):
        resp.status = falcon.HTTP_200
        # On each new POST request, extract the transaction data
        new_txion = req.stream.read().decode('utf-8')
        resp.body = self.process(new_txion)

    def process(self, new_txion):
        new_txion = json.loads(new_txion)
        self.state.node_transactions.append(new_txion)
        print("New transaction")
        print("FROM: {}".format(new_txion['from'].encode('ascii', 'replace')))
        print("TO: {}".format(new_txion['to'].encode('ascii', 'replace')))
        print("AMOUNT: {}\n".format(new_txion['amount']))
        return 'Transaction submission successful'



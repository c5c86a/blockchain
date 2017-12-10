#!/usr/bin/env bash

curl "localhost:5001/transaction" -H "Content-Type: application/json" -d '{"from": "alice", "to":"bob", "amount": 3}'
curl "localhost:5002/transaction" -H "Content-Type: application/json" -d '{"from": "alice", "to":"pete", "amount": 5}';
curl "localhost:5003/transaction" -H "Content-Type: application/json" -d '{"from": "jeff", "to":"joe", "amount": 5}'
curl "localhost:5001/mine" 
curl "localhost:5002/mine"
curl "localhost:5003/mine"

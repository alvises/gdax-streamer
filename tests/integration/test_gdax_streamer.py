import pytest, json
from gdax.streamer import GdaxStreamer

def test__connect_and_get_subscription_confirmation():
	gdax = GdaxStreamer(['LTC-EUR'],['matches'])
	gdax._connect()
	gdax._subscribe()

	_ = gdax._ws.recv()
	subscriptions_res = gdax._ws.recv()
	r = json.loads(subscriptions_res)

	assert r['type'] == 'subscriptions'



def test__connect_and_get_last_match():
	gdax = GdaxStreamer(['LTC-EUR'],['matches'])
	gdax._connect()
	gdax._subscribe()
	msg = gdax._ws.recv()

	assert 'last_match' in json.loads(msg)['type']


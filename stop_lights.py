import pprint

def switch_lights(stoplights):
	for key in stoplights.keys():
		if stoplights[key] == 'green':
			stoplights[key] = 'yellow'
		elif stoplights[key] == 'yellow':
			stoplights[key] = 'red'
		elif stoplights[key] == 'red':
			stoplights[key] = 'green'
	assert 'red' in stoplights.values(), 'Neither light is red! ' + str(stoplights)
	return stoplights


market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

market_2nd = switch_lights(market_2nd)
pprint.pprint(market_2nd)
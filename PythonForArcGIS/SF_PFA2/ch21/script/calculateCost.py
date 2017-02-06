def calculateCost(trail_ID, vegetation, length):
  '''Calculate trail maintenance based on
      vegetation and length.'''
  rate = 1000
  if vegetation[trail_ID] == 'barren':
    rate = 800
  elif vegetation[trail_ID] == 'some bare ground':
    rate = 900
  cost = length[trail_ID]*rate
  return cost
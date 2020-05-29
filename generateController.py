import json, os, yaml, sys
hostFile = sys.argv[1]
hostCluster = sys.argv[2]
outputFile = sys.argv[3]
with open(hostFile, 'r') as stream:
    data_loaded = yaml.load(stream)
stream.close
try:
  controllerLeader = [*data_loaded['all']['children']['controller']['hosts']][0]
except:
  exit()
if len([*data_loaded['all']['children']['controller']['hosts']]) == 1:
  controller = {}
  controller['leader'] = controllerLeader
if len([*data_loaded['all']['children']['controller']['hosts']]) == 3:
  controller = {}
  controller['leader'] = controllerLeader
  ip = []
  ip.append([*data_loaded['all']['children']['controller']['hosts']][1])
  ip.append([*data_loaded['all']['children']['controller']['hosts']][2])
  controller['followers']['ip'] = ip
  if hostCluster != 'undefined':
    controller['clusterIp'] = hostCluster
with open(outputFile, 'w') as outfile:
    json.dump(controller, outfile)
outfile.close

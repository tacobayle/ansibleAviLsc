import json, os, yaml, sys
hostFile = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
version = sys.argv[4]
hostCluster = sys.argv[5]
cloud = sys.argv[6]
outputFile = sys.argv[7]
with open(hostFile, 'r') as stream:
    data_loaded = yaml.load(stream)
stream.close
try:
  controllerLeader = [*data_loaded['all']['children']['controller']['hosts']][0]
except:
  exit()
if hostCluster == 'undefined':
  avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, 'username': username, 'password': password, 'api_version': version}, 'avi_credentials_cluster': {'controller' : controllerLeader, 'username': username, 'password': password, 'api_version': version}, 'cloud': cloud}
else:
  avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, 'username': username, 'password': password, 'api_version': version}, 'avi_credentials_cluster': {'controller' : hostCluster, 'username': username, 'password': password, 'api_version': version}, 'cloud': cloud}
with open(outputFile, 'w') as outfile:
    yaml.dump(avi_credentials, outfile, default_flow_style=False)
outfile.close

import urllib2,time
import json
def parse_dict(init, lkey=''):
    ret = {}
    for rkey,val in init.items():
        key = lkey+rkey
        if isinstance(val, dict):
            ret.update(parse_dict(val, key+'_'))
        else:
            ret[key] = val
    return ret

f = open('chennai.json','r')
json_string = f.read()
oldn = json.loads(json_string)
old = parse_dict(oldn,'')
lst = old.keys()

while True:
    f = open('chennai.json','r')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    newDict = parse_dict(parsed_json,'')
    keylist = newDict.keys()
    time.sleep(2)
    for eachkey in keylist:
	if eachkey in old:
	    if(old[eachkey] == newDict[eachkey]):
		pass
	    else:
		print 'change in value of key',eachkey,":",newDict[eachkey]
	else:
		print 'change in key',eachkey


import netifaces
from bottle import route,run,template

bind_ip = '0.0.0.0'

for iface in netifaces.interfaces():
	addrs = netifaces.ifaddresses(iface)
	if 2 in addrs.keys():
		try:
			#print(addrs[2][0]['broadcast'])
			if '172.' in addrs[2][0]['broadcast']:
				bind_ip = addrs[2][0]['broadcast']
		except KeyError:
			pass
@route('/hello')
@route('/')
@route('/hello/')
@route('/hello/<name>')
def hello(name="World"):
    return template("Hello {{name}}!",name=name)

run(host=bind_ip, port=8080, debug=True)

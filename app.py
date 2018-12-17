from bottle import route, run

import netifaces

myip = ''
interfaces = netifaces.interfaces()
for i in interfaces:
    if i == 'lo':
        continue
    iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
    if iface != None:
        for j in iface:
            if j['addr'].startswith('107.'):
                print(j['addr'])


@route('/')
@route('/hello')
@route('/hello/<name>')
@route('/hello?<name>')
def hello(name='Stranger'):
#       message = "Hello %s!\n" % name
        return "Hello %s!\n"  % name
run ( host=myip, port=9090, debug=True)

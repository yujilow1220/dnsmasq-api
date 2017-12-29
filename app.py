from dns import DNSUtils
from bottle import route, run, post, request

dns_util = DNSUtils()
@route('/add', method='POST')
def add():
    address = request.forms.get('address')
    hostname = request.forms.get('hostname')
    dns_util.add(address, hostname)
    dns_util.reload()
    return "OK"
run(host='0.0.0.0', port=8080, debug=True)

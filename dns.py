from python_hosts import Hosts, HostsEntry
from subprocess import Popen
import shlex
class DNSUtils():
    hosts = Hosts(path='/etc/hosts')
    domain = 'localhost.localdomain'
    def add(self, add_address, add_name):
        if self.domain not in add_name:
            return False
        new_entry = HostsEntry(entry_type='ipv4', address=add_address, names=[add_name, add_name.split(self.domain)[0]])
        self.hosts.add(entries=[new_entry], force=True)
        self.hosts.write()
        return True

    def remove(self, rem_address, rem_name):
        self.hosts.remove_all_matching(address=rem_address, name=rem_name)
        return True

    def reload(self):
        Popen(shlex.split('systemctl restart dnsmasq'))

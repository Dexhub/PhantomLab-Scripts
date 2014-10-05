# file paths #
FILE = "~/.bash_myalias"
CONFIG_FILE = "~/openepc.ssh.config"
# import modules
#import modules used here -- sys is a very standard one
import sys
import os



def main():
    global FILE, CONFIG_FILE
    try:
            os.remove(os.path.expanduser(FILE))
    except OSError:
            pass
    f = open(os.path.expanduser(FILE),'w')
    config_file = open(os.path.expanduser(CONFIG_FILE),'r')
    for line in config_file:
        sp = line.split()
        template = "alias "+sp[0]+ "='ssh -v -X "+sp[1]+".emulab.net'\n"
        print template
        f.write(template)


def get_inet_ips():
  try:
    import netinfo
  except ImportError:
    return None
  else:
    inetIPs = []
    for interface in netinfo.list_active_devs():
      if not interface.startswith('lo'):
        ip = netinfo.get_ip(interface)
        inetIPs.append(ip)
    return inetIPs

if __name__ == '__main__':
  main()

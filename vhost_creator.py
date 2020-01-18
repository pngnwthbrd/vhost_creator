#!/usr/bin/python

import os
import sys
import json
from shutil import copyfile

def createVHOST(argv):
        try:
                vhost_name = argv[1]
        except IndexError:
                print('missing argument - plese enter a vhost name')
        else:
                with open('/usr/share/vhost_creator_conf.json', 'r') as cf:
                        conf = json.load(cf)
                        
                path = conf['server_path'] + vhost_name
                try:
                        os.mkdir("%s" % path)
                        uid = int(os.popen('id -u ' + conf['user']).read())
                        gid = int(os.popen('id -g ' + conf['user']).read())
                        os.chown(path, uid, gid)
                except OSError:
                        print('Creation of the directory %s failed' % path)
                        sys.exit()
                else:
                        print('directory successfuly created.')
                        
                try:
                        vhost_conf = '''\n
<VirtualHost *:80>
    ServerAdmin webmaster@''' + vhost_name + '''.dom
    DocumentRoot "''' + conf['server_path'] + vhost_name + '''"
    ServerName ''' + vhost_name + '''.dom
    ServerAlias www.''' + vhost_name + '''.dom
    ErrorLog "/var/log/httpd/''' + vhost_name + '''.dom-error_log"
    CustomLog "/var/log/httpd/''' + vhost_name + '''.dom-access_log" common
    <Directory "''' + conf['server_path'] + vhost_name + '''">
        Require all granted
    </Directory>
</VirtualHost>
'''
                        copyfile('/etc/httpd/conf/extra/httpd-vhosts.conf', '/etc/httpd/conf/extra/httpd-vhosts.conf.bu')
                        with open('/etc/httpd/conf/extra/httpd-vhosts.conf', 'a') as f:
                                f.write(vhost_conf + "\n\n")
                                
                        copyfile('/etc/hosts', '/etc/hosts.bu')
                        with open('/etc/hosts', 'a') as f:
                                f.write("\n127.0.0.1 " + vhost_name + ".dom")
                        
                except OSError:
                        print('Creation backup files failed')
                else:
                        print('Creation backup files successful')
                        
                try:
                       os.system('systemctl restart httpd.service')
                       print('Httpd.service restart successful')
                except SystemError:
                        print('Restart httpd.service failed\nPlease restart manually')
                print("Done!")

if __name__ == "__main__":
        createVHOST(sys.argv)
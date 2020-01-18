# Arch Linux vhost_creator
A little helper to create vhosts quickly.
Create and modify of required files.

# how to install
For Arch Linux users: you can use the package build.
Download the PKGBUILD file and run the following commands
```
$ makepkg
```
if its ready do
```
# packman -U vhost_creator-0.99_10-1-x86_64.pkg.tar.xz
```

Check the config file **/usr/share/vhost_creator/vhost_creator_cons.json**  
```server_path``` where your vhost location is located  
```user``` your http user

# how to use
```
# vhost_creator.py my-domain-name
```

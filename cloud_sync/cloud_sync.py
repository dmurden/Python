import os
#srcdir = "C:\\Users\\duke_\\Nextcloud\\"
#dstdir = "C:\\Users\\duke_\\OneDrive\\NextcloudCopy\\"
dstdir = "C:\\Users\\duke_\\Nextcloud\\"
srcdir = "C:\\Users\\duke_\\OneDrive\\NextcloudCopy\\"
srcdir_len = len(srcdir)
for root, dirs, files in os.walk(srcdir, topdown=False):
    for name in files:
        #print(os.path.join(root, name))
        statinfo = os.stat(os.path.join(root, name))
        new_root = dstdir + root[srcdir_len:]
        #print(os.path.join(new_root, name))
        new_statinfo = os.stat(os.path.join(new_root, name))
        if statinfo.st_size != new_statinfo.st_size:
            print(os.path.join(root, name))
        if statinfo.st_mtime != new_statinfo.st_mtime:
            print(os.path.join(root, name))
    #for name in dirs:
        #print(os.path.join(root, name))
        #statinfo = os.stat(os.path.join(root, name))
        #print(os.path.join(name))

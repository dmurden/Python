cout = open('convert/debrabro_c.html', 'w')
with open('convert/debrabro.html') as fin:
    line = fin.readline()
    while line:
        cout.write(line + '<br>')
        line = fin.readline()
cout.close()
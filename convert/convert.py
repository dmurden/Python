cout = open('convert/carynbro_c.html', 'w')
with open('convert/carynbro.html') as fin:
    line = fin.readline()
    while line:
        cout.write(line + '<br>')
        line = fin.readline()
cout.close()
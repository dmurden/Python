import cx_Oracle
import datetime
import threading

#subclass of threading.Thread
class SynchThread(threading.Thread):
   def __init__(self, host, sid, startup, dbPwd, usrId, modeType):
       threading.Thread.__init__(self)
       self.host = host
       self.sid = sid
       self.startup = startup
       self.dbPwd = dbPwd
       self.usrId = usrId
       self.modeType = modeType
   def run(self):
       try:
           with cx_Oracle.connect(self.usrId, self.dbPwd, self.sid, mode=self.modeType,
                                   encoding="UTF-8") as self.connection:
               self.cursor = self.connection.cursor()
               self.cursor.execute("select name from v$database")
               self.row = self.cursor.fetchone()
               self.connection.commit()
               mutex.acquire()
               print(fmtOut.format(self.host, self.sid, self.startup, "UP", " ", self.row[0]))
               fout.write(fmtOut.format(self.host, self.sid, self.startup, "UP", " ", self.row[0]) + "\n")
       except cx_Oracle.DatabaseError as exc:
               mutex.acquire()
               error, = exc.args
               if self.startup == "n":
                   print(fmtOut.format(self.host, self.sid, self.startup, "DOWN", " ", error.code))
                   fout.write(fmtOut.format(self.host, self.sid, self.startup, "DOWN", " ", error.code) + "\n")
               else:
                   print(fmtOut.format(self.host, self.sid, self.startup, "DOWN", "**ERROR**", error.code))
                   fout.write(fmtOut.format(self.host, self.sid, self.startup, "DOWN", "**ERROR**", error.code) + "\n")
                   foutb.write(fmtOut.format(self.host, self.sid, self.startup, "DOWN", "**ERROR**", error.code) + "\n")
       mutex.release()

with open('/share/oracle/dat/dboratab') as oratab:
   pwdDev = "Dates8Devel_"
   pwdPrd = "Curry8Dates_"
   pwdSys = "Apple8Berry_"
   fmtOut = "{0:25} {1:20} {2:5} {3:4} {4:9} {5:10}"
   fout = open("/home/oracle/dmurden/db_checkout_mt.txt", "w")
   foutb = open("/home/oracle/dmurden/db_checkout_error_mt.txt", "w")
   fout.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))
   mutex = threading.Lock()

   cnt = 0
   line = oratab.readline()
   th = []
   while line:
       sidori = line.strip().split(':')[0]
       startup = line.strip().split(':')[2]
       vdb = line.strip().split(':')[3]
       dbtype = line.strip().split(':')[4]
       host = line.strip().split(':')[6]
       sid = line.strip().split(':')[10]
       if line.strip().split(':')[7] == "p":
           dbPwd = pwdPrd
       else:
           dbPwd = pwdDev
       if dbtype == "c":
           usrId = "RGADBA"
           modeType = cx_Oracle.DEFAULT_AUTH
       else:
           usrId ="SYS"
           dbPwd = pwdSys
           modeType = cx_Oracle.SYSDBA
       th.append(SynchThread(host, sid, startup, dbPwd, usrId, modeType))
       th[cnt].start()

       line = oratab.readline()
       cnt += 1
   #forcing the main thread to wait until all child threads are done
   for t in th:
       t.join()
fout.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))
fout.close()
foutb.close()
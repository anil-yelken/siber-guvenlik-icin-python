import nmap
#python-nmap 
nmap = nmap.PortScanner() # nmap is the program of python port scanner....
nmap.scan('127.0.0.1', '1-65000','-sV')
print "Nmap komutu: ",nmap.command_line()
print "Tarama bilgisi: ",nmap.scaninfo()
print "Tarama durumu: ",nmap.scanstats()
print "Hostlar: ",nmap.all_hosts()
print nmap.csv()

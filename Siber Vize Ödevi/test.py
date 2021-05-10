import nmap
nmScan = nmap.PortScanner()
hedef = input('Tarama yapmak istediğiniz ip adresi --> ')
nmScan.scan('-oX testtarama 192.168.1.0/24')
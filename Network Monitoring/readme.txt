*****ICMP Functions Program*****

This document describes functions of ICMPMonitoringTool.
Program tested and running in Python version 3.10.7.
Program can work with default Python libraries without needing any external dependencies.

User can run program in two different ways:
1) Open ICMP_Monitoring_Tool.py file as Administrator or root user.
2) (Windows Only) Open CMD as administrator, change into ICMP_Monitoring_Tool.py file directory and write:
python ICMP_Monitoring_Tool.py (for this process, python is need to be defined in Environment Variables)

***WARNING***: Program uses RAW socket to work with ICMP protocol, in UNIX and Windows 
systems, to create RAW socket system need admin privileges to work!
Be sure to run program as root for Linux and Run as Administrator in Windows.


----Ping Host:
	Ping host to check host is alive or not. It sends a dummy packet to check status.
	If host does not answer in 2 second timeout it's assumed that host is not alive.
	
    Syntax:
	are you alive <Destination IP or host name> <Timeout>
	<Destination IP or host name> is required.
	<Timeout> is optional. Default is 2 second.
	
---->RTT Calculator:
	Ping host with multiple packets to calculate minimum, maximum and average 
	RTT times in miliseconds.
	
    Syntax:
	latency <Destination IP or host name> <Number Of Packets>
	<Destination IP or host name> is required.
	<Number Of Packets> is optional. Default is 4.
	
---->Traceroute:
	Pings host 3 time and calculates RTT for each packet with different id and prints 
	informations to console until reach to destination. User has to wait to finish traceroute 
	to use other functions. (Different id usage caused by not to be blocked by firewall of host)
	After traceroute is completed, program will ask user to save informations into a log file
	or not. Using 'y' or 'n' user can save informations into log file named as 
	"log YEAR-MONTH-DAY HOUR-MINUTE-SECONDS".txt in ICMP_Monitoring_Tool.py directory
	
	Syntax:
	how to reach <Destination IP or host name>
	tracert <Destination IP or host name>
	<Destination IP or host name> is required.
	
---->Host IP and Address:
	Prints hosts full name and IP address.
	
	Syntax:
	hostname <Destination IP or host name>
	<Destination IP or host name> is required.
	
If program prints "No command found like that, try again." check input command.
	
This program written by Gorkem Kacakgil for Fundamentals Of Data Network lesson Homework.
contact: gorkemkacakgil@ogr.eskisehir.edu.tr
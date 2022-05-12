print("""
-----------------------------------------------------------------

TRANSPORT CONTROL PROTOCOL(TCP)
- Built on top of IP (Internet Protocol)
- Assumes IP might lose some data - stores and retransmits data if it 
seems to be lost 
- Handles "flow control" using a transmit window
- Provides a nice reliable pipe
----------------------------------------------------------------

TCP CONNECTIONS / SOCKTETS 
- "In computer networking, an internet socket or network socket is an 
endpoint of a bidirectional inter-process communication flow across an
Internet Protocol-based computer network such as the Internet"

Process <---------Internet----------> Process
------------------------------------------------------------------

TCP Port Numbers 
- A port is an application-specific or process-specific software 
communications end-point
- It allows multiple networked applications to coexist on the same server
- There is a list of well-known TCP port numbers 
-------------------------------------------------------------------

COMMON TCP PORTS 
- Telnet(23) - Login
- SSH(22) - Secure Login
- HTTP(80)
- HTTPS(443) - Secure
- SMTP(25) (Mail)
- IMAP(143/220/993) - Mail Retrieval
- POP(109/110) - Mail Retrieval
- DNS(53) - Domain Name
- FTP(21) - File Transfer
---------------------------------------------------------------------

SOCKETS IN PYTHON 
- Python as built-in support for TCP Sockets

>>> import socket 
>>> mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> mysock.connect( ('data.pr4e.org', 80) )

'data.pr4e.org' -> Host 
80 -> Port 

""")


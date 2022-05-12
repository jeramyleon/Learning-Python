print("""
-------------------------------------------------------------------

APPLICATION PROTOCOL
- Since TCP (and Python) gives us a reliable socket, what do we want to 
do with the socket? What problem do we want to solve?
- Application Protocols
    - Mail
    - World Wide Web
------------------------------------------------------------------

HTTP - Hypertext Transfer Protocol
- The dominant Application Layer protocol on the Internet
- Invented for the Web - to retrieve HTML, Images, Documents, etc
- Extended to be data in addition to documents - RSS, Web Servies, etc..
Basic Concept - Make a connection - Requst a document - Retrieve the
Documnet - Close the Connection
-------------------------------------------------------------------

HTTP
- The HyperText Transfer Protocol is the set of rules to allow browsers
to retrieve web documents from servers all over the internet 
---------------------------------------------------------------------

WHAT IS A PROTOCOL? 
- A set of rules that all parties foloow so we can predict each other's
behavior
- And not bump into each other 
    - On two-way roads in USA, drive on the right-hand side of the road
    - On two-way roads in the UK, drive on the left-hand side of the road
-------------------------------------------------------------------------

GETTING DATA FROM THE SERVER 
- Each time the user clicks on an anchor tag with an href= value to switch
to a new page, the browser makes a connection to the web server and issues 
a 'GET' request - to GET the content of the page at the specified URL
- The server returns the HTML document to the browser which formats and 
displays the document to the user.
----------------------------------------------------------------------

INTERNET STANDARDS
- The standards for all of the Internet protocols(inner workings) are
developed by an organization
- Internet Engineering Task Force (IETF)
- www.ietf.org
- Standards are called "RFCs" - Request for Comments"
-------------------------------------------------------------------
MAKING AN HTTP REQUEST 
- Connect to the server like www.dr-chuck.com
- Request a document (or the default document)
    - GET http://www.dr-chuck.com/page1.htm HTTP/1.0
    - GET http://www.mlive.com/ann-arbor/ HTTP/1.0
    - GET http://www.facebook.com HTTP/1.0
---------------------------------------------------------------------




















""")

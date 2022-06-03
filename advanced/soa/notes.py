print(''' 
---------------------------------------------------------------------
SERVICE ORIENTED APPROACH
- Most non-trivial web applications use services
- They use services from other applications 
    - Credit Card Charge
    - Hotel Reservation systems
- Services publish the "rule" applications must follow to make use of the
service(API)
------------------------------------------------------------------------
MULTIPLE SYSTEMS
- Initially - two systems cooperate and split the problem
- As the data/service becomes useful - multiple applications want to use the
information / application
------------------------------------------------------------------------
APPLICATION PROGRAM INTERFACE
- The API itself is largely abstract in that it specifies an interface and
controls the behavior of the objects specified in that interface. The 
software that provides the functionality described by an API is said to be 
an "implementation" of the API. An API is typically defined in terms of the 
programming language used to build an application.
-------------------------------------------------------------------------
API SECURITY AND RATE LIMITING
- The compute resources to run these APIs are not "free"
- The data provided by these APIs is usually valuable
- The data providers might limit the number of requests per day, demand an
API "key", or even charge for usage
- They might change the rules as things progres...''')
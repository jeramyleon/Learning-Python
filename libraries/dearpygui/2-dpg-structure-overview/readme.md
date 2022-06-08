DPG STRUCTURE OVERVIEW 
A DPG app will have an overall structure as follows: 
    - Setup
    - Context 
    - Viewport 
    - Render loop
    - Items 
    - Primary Window 
-------------------------------------------------------------------
SETUP 
All DPG apps must do 3 things: 
    - Create and Destroy context 
    - Create and show Viewport 
    - Setup and start DearPyGui 
-------------------------------------------------------------------
THE CONTEXT 
To access any DPG commands the context must be created with
create_context This should be the first DPG command and it's typical 
to perform this with an import. 

Proper clean up of DPG can be done using destroy_context.

Creating and destroying the context and also setup and start dearpygui
are useful when the DPG needs to be started and stopped multiple times 
in one python session. 

! Warning 
If create_context is not first DPG will not start (and will probably 
crash). 
---------------------------------------------------------------------
THE VIEWPORT 
The viewport is the window created by the operating system. 

The viewport needs to be explicitly created using create_viewport and 
shown using show_viewport 

CODE: the-viewport.py
---------------------------------------------------------------------



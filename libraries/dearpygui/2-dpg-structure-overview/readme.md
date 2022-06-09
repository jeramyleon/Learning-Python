DPG STRUCTURE OVERVIEW
-----------------------------------------------------------------------------

A DPG app will have an overall structure as follows: 

    ..* Setup

    ..* Context 

    ..* Viewport

    ..* Render loop

    ..* Items

    ..* Primary Window 

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

Code: the-viewport.py
---------------------------------------------------------------------
THE RENDER LOOP 
The render loop is responsible for displaying items, partially
maintaining state and callbacks. 

The render loop is completely handled by the start_dearpygui command. 

In some cases it's necessary to explicitly create the render loop so
you can call python commands that may need to run every frame. Such as per-frame ticker or counter update functions. 

code: the-render-loop.py 

!Warning 
The maual render loop must be created after | setup_dearpygui |
--------------------------------------------------------------------
ITEM OVERVIEW 
DPG can be broken down into Items, UI items, Containers 

Items: 
    Items are anything in the library (i.e button, registries, windows, etc).
UI Items:
    Any item in DPG that has a visual component (i.e. button, listbox,window, etc).
Containers: 
    Items that can hold other items. (i.e. window, groups, registries, etc). 
-------------------------------------------------------------------
THE PRIMARY WINDOW 
DPG can assign one window to be the primary window. The primary window will fill the viewport and always be drawn behind other windows. 

code: the-primary-window.py


















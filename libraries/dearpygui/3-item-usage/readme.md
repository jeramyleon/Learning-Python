Creating Items 
------------------------------------------------------

Items are created using their add_*** commands. 

All items must have a tag which can either be specified or are automatically generatd by DPG. 

Tags can be either integers or strings and are used to refer to te item after it has been created. 

Items return their tag when they are created. 

Warning! Item tags must be unique if specified using the tag keyword. Integers 0-10 are reserved for DPG internal itmes. 

code: creating-items.py 

Note! Items can be created and deleted at runtime 

Creating Containers
---------------------------------------------------------------

Below we will add a window, a group and a child window to the code. Items can either be added directly to the context manaher or later by specifying the parent.  

code: creating-containers.py 

Configuration, State, Info
---------------------------------------------------------------------
DPG items consist of configuration, state and info. (AND value but we will cover that seperately)

Each of these can be accessed by their corresponding function 

`get_item_configuration` keywords that control its appearance and behavior(label, callback, width, height)

`get_item_state` keywords that reflect its interaction (visible, hovered, clicked, ect)

`get_item_info` keywords that reflect its information (item type, children, theme,ect)

Note: configuration, state and info are broken into seperate commands that access each individual keyword, instead of returning the entire dictionary 

Examples:
`get_item_label`
`is_item_hovered`
`get_item_children`

Below we will demonstrate the ways to configure items and how to check their state by viewing them through the item registry tool. 

code: configuration-state-info.py

Callbacks
------------------------------------------------------------

Callbacks give items functionality by assigning a function to run when they are 
activated and almost all UI Items in DPG can run callbacks. 

Functions or methods are assigned as UI item callbacks when an item is created or at a later runtime using `set_item_callback`

Callbacks may have up to 3 arguments in the following order. 

sender: the id of the UI item has submitted the callback 

app_data: occasionally UI items will send their own data (ex. file dialog)

user_data: any python object you want to send to the function 

Note: Because they are optional positional arguments you must use the sender and app_data if you want to use user_data standard keyword arguments 

code: callbacks.py 

Item Values
-------------------------------------------------------------------------

Almost all UI items have a value which can be accessed or set. 

All UI items that have a value also have the default_value parameter which will set the items' initial starting value. 

Values can be accessed using `get_value`. 

Below is an example of setting the default_value for two different items, setting a callback to the items and printing their values 

code: item-values.py 





































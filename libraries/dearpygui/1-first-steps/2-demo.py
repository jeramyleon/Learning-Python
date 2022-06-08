print("""
DPG has a complete built-in demo/showcase. It is a good idea to look
into this demo. The code for this can be found in the repo in the 
'demo.py'_ file  

!Note 
The main script must always: 

- Create the context | create_context |
- Create the viewport | create_viewport |
- Setup dearpygui | setup_dearpygui |
- Show the viewport | show_viewport |
- Start dearpygui | start_dearpygui |
- Clean up the context | destroy_context | 
""")


import dearpygui.dearpygui as dpg 
import dearpygui.demo as demo 

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)

demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


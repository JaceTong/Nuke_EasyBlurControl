import Add_Decrese_Value


menubar=nuke.menu("Nodes")
menubar.addMenu("Add_Decrese").addCommand('Add_Value','Add_Decrese_Value.Add_value()', "e", shortcutContext=2)
menubar.addMenu("Add_Decrese").addCommand('Decrese_value','Add_Decrese_Value.De_value()', "shift+e", shortcutContext=2)

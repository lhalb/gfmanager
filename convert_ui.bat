echo off
pyuic5 -x ./gui/gui.ui -o ./gui/GUI.py
pyuic5 -x ./gui/minGui.ui -o ./gui/mingui.py
pyuic5 -x ./gui/trimming.ui -o ./gui/trimming.py
pyuic5 -x ./gui/plotting.ui -o ./gui/plotting.py
pyuic5 -x ./gui/save.ui -o ./gui/save.py
pyrcc5 ./gui/icons.qrc -o ./icons_rc.py
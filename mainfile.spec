# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['F:\\PycharmProjects\\run.py'],
             binaries=[],
             datas=[],
             hiddenimports=['scipy.special.cython_special'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['IPython','FixTk','tcl','tk','_tkinter','tkinter','Tkinter'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas + [
          ('gui/icons/appicon.ico', 'gui/icons/appicon.ico', 'DATA')
          ],
          [],
          name='Grainmanager',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='gui/icons/appicon.ico',
          version='version.rc')

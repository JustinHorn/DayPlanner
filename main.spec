# -*- mode: python -*-

from kivy_deps import sdl2, glew

block_cipher = None


a = Analysis(['production/main.py'],
             pathex=['.'],
             binaries=None,
             datas=None,
             hiddenimports=['MyHiddenImports'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)

a.datas += [('production/maingui.kv', 'production/popmenu.kv', 'DATA')]

exe = EXE(pyz, 
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='DayPlanner',
          debug=False,
          strip=False,
          upx=True,
          console=True)
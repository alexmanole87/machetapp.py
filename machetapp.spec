# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['F:/python/machetapp_py/vers serviciu/machetapp_py_SERN/machetapp.py'],
             pathex=['F:\\python\\machetapp_py\\vers serviciu\\machetapp_py_SERN'],
             binaries=[],
             datas=[('F:/python/machetapp_py/vers serviciu/machetapp_py_SERN', 'machetapp_py_SERN/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='machetapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='F:\\python\\machetapp_py\\vers serviciu\\machetapp_py_SERN\\machetapp.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='machetapp')

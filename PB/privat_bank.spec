# -*- mode: python -*-

block_cipher = None


a = Analysis(['privat_bank.py'],
             pathex=['d:\\Users\\�������������\\Desktop\\Python\\CODE\\PB'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='privat_bank',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='D:\\Users\\�������������\\Desktop\\Python\\CODE\\PB\\icon.ico')
# -*- coding: utf-8 -*-
from cx_Freeze import setup, Executable
import sys

options={
    'build.exe':{
        "packages": ["multiprocessing","idna.idnadata"],
        'includes':[
            'Ui_pb_gui',
            "idna.idnadata"
        ]
    }
}

exe=exe = Executable(script="privat_bank_gui.py", base="Win32GUI")
setup(
    name='PB_cx_freez',
    version='1.0',
    description='zzzzz',
    options=options,
    executables=[exe]
    # executables=[Executable('privat_bank_gui.py')]
)

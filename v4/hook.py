"""PyInstaller hook configuration to ensure proper EXE bundling."""

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('matplotlib')

hiddenimports = [
    'PyQt5.QtWebEngineWidgets',  
    'pandas',                    
    'openpyxl',                  
    'numpy'                      
]
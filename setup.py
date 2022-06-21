import cx_Freeze


executables = [cx_Freeze.Executable('main.pyw')]

cx_Freeze.setup(
    name = 'BibliotecaPOO',
    options = {'build_exe': {'packages': ['PySimpleGUI', 'datetime'],
                             'include_files': ['imagens', 'login.txt']}},
    executables = executables
)

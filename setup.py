import cx_Freeze
import os.path


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
executables = [cx_Freeze.Executable("underwater.py")]

additional_mods = ['numpy.core._methods', 'numpy.lib.format']

cx_Freeze.setup(name="Underwater Battles",
                options={"build_exe":
                         {'packages':      ['pygame'],
                          'includes': additional_mods,
                          'include_files': [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                                            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                                            'fonts',
                                            'music',
                                            'sound_effects']
                          }
                         },
                executables=executables,
                version = "0.1")

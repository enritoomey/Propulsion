# Used successfully in Python2.5 with matplotlib 0.91.2 and PyQt4 (and Qt 4.3.3)
from distutils.core import setup
import py2exe
import os

# We need to import the glob module to search for all files.
import glob

# We need to exclude matplotlib backends not being used by this executable.  You may find
# that you need different excludes to create a working executable with your chosen backend.
# We also need to include include various numerix libraries that the other functions call.
def include_subdirectory(lista, directory=os.getcwd()):
    for files in os.listdir(directory):
        if os.path.isdir(files):
            include_subdirectory(lista, "\\".join([directory, files]))
        elif files.split(".")[-1] == 'py':
            lista.append("\\".join([directory, files]))


my_includes = []
include_subdirectory(my_includes, directory=os.getcwd()+"\common")
include_subdirectory(my_includes, directory=os.getcwd()+"\JOULE_BRAYTON")
include_subdirectory(my_includes, directory=os.getcwd()+"\SABATHE")
opts = {
    'py2exe': {"includes": ["matplotlib.backends",  "matplotlib.backends.backend_qt4agg",
                            "matplotlib.figure", "pylab", "numpy", "matplotlib.backends.backend_tkagg"],
               'excludes': ['_gtkagg', '_tkagg', '_agg2', '_cairo', '_cocoaagg',
                            '_fltkagg', '_gtk', '_gtkcairo', ],
               'dll_excludes': ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'MSVCP90.dll',
                                'libiomp5md.dll'],
               'compressed': True,
               'dist_dir': "CiclosApp"
               }
}

install_requires = ['numpy', 'matplotlib', 'pyside', 'atmosfera_estandar']

dependency_links = ['git+https://github.com/enritoomey/atmosfera_estandar.git#egg=atmosfera_estandar']

# Changes made to the vesion that compiled in windows7
#  - removed sip from py2exe:includes
#  - MSVCP90.dll and libiomp5md.dll added to avoid compilation problems

# Save matplotlib-data to mpl-data ( It is located in the matplotlib\mpl-data
# folder and the compiled programs will look for it in \mpl-data
# note: using matplotlib.get_mpldata_info
data_files = [(r'mpl-data', glob.glob(r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\*.*')),
                    # Because matplotlibrc does not have an extension, glob does not find it (at least I think that's why)
                    # So add it manually here:
                  (r'mpl-data', [r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\matplotlibrc']),
                  (r'mpl-data\images', glob.glob(r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\images\*.*')),
                  (r'mpl-data\fonts', glob.glob(r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\fonts\*.*'))]

#for console program use 'console = [{"script" : "scriptname.py"}]
setup(windows=[{"script": "CiclosApp.py"}], options=opts,   data_files=data_files, install_requires=install_requires,
      dependency_links=dependency_links)

# cython_play
happly play ....

### bulid
```
# linux or mac os
python setup.py build_ext --inplace

# win 
python setup.py build_ext -i compiler=mingw32 -DMS_WIN64
python setup.py build_ext -i compiler=msvc

# other
import pyximport
pyximport.install()

# notebook
%load_ext Cython
%%cython
```


from hello import say_hello_to
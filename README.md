# fobem

Requirements:
---------------
- Python 2.7+
- Numpy 1.5.0+

- Research SDK library files. These files are available from Emotiv by purchasing the research SDK.
These  must be built for the same architecture as your python installation (either i386 or x86_64),
otherwise ctypes.CDLL will raise an error.
- location known to your system's PATH:
    - Windows: `edk.dll` and `edk_utils.dll` in `windows/system32`
    - OSX: `libedk.dylib` and `libedk_ultils_mac.dylib` in `usr/local/lib`
- `pip install https://github.com/thearn/pyemotiv.git`

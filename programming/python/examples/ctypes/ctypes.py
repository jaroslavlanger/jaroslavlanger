import ctypes
from ctypes import c_char_p, c_void_p

lib = ctypes.cdll.LoadLibrary('./lib_python_ctypes.so')

lib.write_to_file.argtypes = [c_char_p, c_char_p]
lib.write_to_file.restype = c_void_p

lib.write_to_file(b"data/doesnotexist.txt", b"data/out.txt")
lib.write_to_file(b"data/out.txt", "data/❤️_out.txt".encode())

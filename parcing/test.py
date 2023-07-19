import ctypes

unsigned_value = 167
signed_value = ctypes.c_int16(unsigned_value).value

print(signed_value)
c1 = compile("1 + 1", "", 'eval')

code_class = type(c1)

def f(x, y, power=1):
    z = x * y
    return z ** power

c2 = f.__code__
assert type(c2) == code_class

print(dir(c2))

assert c2.co_argcount == 3
assert c2.co_cellvars == ()
# assert isinstance(c2.co_code, bytes)
assert c2.co_consts == (None,)
assert "code.py" in c2.co_filename
assert c2.co_firstlineno == 5
# assert isinstance(c2.co_flags, int) # 'OPTIMIZED, NEWLOCALS, NOFREE'
assert c2.co_freevars == ()
assert c2.co_kwonlyargcount == 0
# assert c2.co_lnotab == 0, c2.co_lnotab  # b'\x00\x01' # Line number table
assert c2.co_name == 'f', c2.co_name
assert c2.co_names == (), c2.co_names # , c2.co_names
assert c2.co_nlocals == 4, c2.co_nlocals #
# assert c2.co_stacksize == ... 2 'co_stacksize',
assert c2.co_varnames == ('x', 'y', 'power', 'z'), c2.co_varnames

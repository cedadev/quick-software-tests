import cf
print("checking that cf built with PP support... ", end="")
f = cf.read("test.pp")
assert f[0].standard_name == "eastward_wind"
print("yes")

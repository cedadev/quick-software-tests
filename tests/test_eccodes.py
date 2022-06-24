import eccodes

print('running eccodes test')

gid = eccodes.codes_grib_new_from_file(open("testdata/gfs20220525132602953.grb"))
values = eccodes.codes_get_values(gid)

assert len(values) == 264
assert 102310 < values[1] < 102311

print('ran eccodes test')

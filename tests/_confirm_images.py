
def images_follow(filenames):
    print(f"""
===================================================================
You are about to see {len(filenames)} plot window(s)
Can be compared with the following file(s) in example_plots directory:
  {filenames}
Afterwards, please close it/them manually to continue.
(libGL errors can be ignored)
===================================================================
""")


def images_launched(filenames):
    print(f"""
===================================================================
The "display" command has been launched to display the following {len(filenames)} images
Can be compared with the following file(s) in example_plots directory:
  {filenames}
You may be seeing them already, or should do in a few seconds.
Afterwards, please close it/them manually.
===================================================================
""")


def image_confirm(test_name):
    print()
    print("============================================")
    resp = input(f"Did you see the expected window(s) ({test_name} test)? ")
    if not resp.lower().startswith('y'):
        raise Exception(f'{test_name} test failed.')

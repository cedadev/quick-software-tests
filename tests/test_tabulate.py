from tabulate import tabulate

resp = tabulate([["Name","Age"],["Alice",24],["Bob",19]],
                headers="firstrow")

assert(resp == 'Name      Age\n------  -----\nAlice      24\nBob        19')


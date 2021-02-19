#!/bin/sh

db=test.db

rm -f $db 
echo 'create table foo(id int primary key not null, blah char(50) not null);' | sqlite3 $db
echo 'insert into foo values (1, "hello");' | sqlite3 $db
echo 'insert into foo values (2, "world");' | sqlite3 $db

value=$(echo 'select blah from foo where id=2;'  | sqlite3 $db)

rm -f $db

if [ "$value" = "world" ]
then
    echo "sqlite test passed"
    exit 0
else
    echo "sqlite test failed"
    exit 1
fi

for script in *.sql; do
    sqlite3 data.sqlite3 < $script;
done

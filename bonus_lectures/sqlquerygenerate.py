fields = "field1, field2, field3, field4"
table = "table"
conditions1 = "condition1=1 "
conditions2 = "AND condition2=2"

sql = (f"SELECT {fields} "
       f"FROM {table} "
       f"WHERE {conditions1}"
       f"{conditions2};")

print(sql)
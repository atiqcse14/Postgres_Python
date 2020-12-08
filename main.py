import psycopg2

con = psycopg2.connect(database="Task_DB", user="postgres", password="1234", host="127.0.0.1", port="5432")

con2 = psycopg2.connect(database="Hospital", user="postgres", password="1234", host="127.0.0.1", port="5432")


print("Database connected successfully")

cur = con.cursor()

cur.execute("Select * from employee_project")
rows = cur.fetchall()
count =0


for row in rows:
    # print("E_ID =", row[0])
    # print("E_FNAME =", row[1])
    # print("E_LNAME =", row[2])
    # print("DEPARTMENT =", row[3], "\n")
    count = count + 1

print("Total rows of first DB:", count, "\n")

print("Operation done successfully")
con.close()



cur2 = con2.cursor()

cur2.execute("Select * from doctor")
rows = cur2.fetchall()

count2 = 0

for row2 in rows:
    # print("P_ID =", row2[0])
    # print("P_NAME =", row2[1])
    # print("P_AGE =", row2[2])
    # print("p_GENDER =", row2[3], "\n")
    count2 = count2 + 1

print("Total rows of second DB:", count2, "\n")

print("Operation 2 done successfully")
con.close()

if count<count2:
    print("Extra rows in second DB table is:", count2 - count, "\n")
elif count2<count:
    print("Extra rows in first DB table is:", count - count2, "\n")
else:
    print("Both DB tables are same")
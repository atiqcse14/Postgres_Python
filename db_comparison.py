import psycopg2

con = psycopg2.connect(database="Task_DB", user="postgres", password="1234", host="127.0.0.1", port="5432")

con2 = psycopg2.connect(database="Hospital", user="postgres", password="1234", host="127.0.0.1", port="5432")

con3 = psycopg2.connect(database="Result", user="postgres", password="1234", host="127.0.0.1", port="5432")


print("Database connected successfully")

cur = con.cursor()
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;")
db_tables1 = cur.fetchall()
#count =0
print(db_tables1)

cur2 = con2.cursor()
cur2.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;")
db_tables2 = cur2.fetchall()
print(db_tables2)


cur3 = con3.cursor()
cur3.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;")
db_tables3 = cur3.fetchall()
print(db_tables3)



for i in range(len(db_tables1)):
        cur.execute("SELECT count(*) FROM " + db_tables1[i][0] + ";")
        count1 = cur.fetchone()[0]
        print(count1)
        cur2.execute("SELECT count(*) FROM " + db_tables2[i][0] + ";")
        count2 = cur2.fetchone()[0]
        print(count2)

        # print("Both "+db_tables1[i][0]+ " and "+db_tables2[j][0]+" tables have equal rows" if len(rows1) == len(rows2)
        #       else db_tables1[i][0]+" has "+str((len(rows1)-len(rows2)))+" more rows than "+db_tables2[j][0]
        # if len(rows1) > len(rows2) else db_tables2[j][0]+" has "+str((len(rows2)-len(rows1)))+" more rows than "+db_tables1[i][0], "\n")

        query ="INSERT into db_compare VALUES ( '" + db_tables1[i][0] +"','" + db_tables2[i][0] +"',"+ str(count1) +" ," + str(count2) +" ,"+ str(abs(count1-count2))+");"
        # #print(query)
        cur3.execute(query)

con3.commit()

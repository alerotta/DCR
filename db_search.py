import mysql.connector


mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "digital_content_retrieval"
)



mycursor = mydb.cursor()

sql_query = "SELECT filename,extension FROM file_storage WHERE name LIKE %s"
usr_query = input("what are you looking for ? ")




# Execute the query
mycursor.execute(sql_query,(f"%{usr_query}%",))
myresult = mycursor.fetchall()

if myresult:
    print("Matching names:")
    for row in myresult:
        if row[1] == "dir":
            print(row[0] + ' - directory')
        else:
            print(row[0] + ' - file')
else:
    print("No matching names found.")

sql_query = "SELECT content,filename,extension FROM file_storage WHERE content LIKE %s"
mycursor.execute(sql_query,(f"%{usr_query}%",))
myresult = mycursor.fetchall()

if myresult:
    print("Matching content:")
    for row in myresult:
        text = str(row[0])
        count = text.count(usr_query)
        if row[2] != "dir":
            print (f"inside {row[1]}, '{usr_query}' was found {count} times")
else:
    print("No matching in content found.")






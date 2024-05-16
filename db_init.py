import mysql.connector
import os


directory = '/Users/alessandrorotta/desktop/project'
skip_dir = "dcr_env"
text_ext = ['txt','csv','tsv','json','xml','yaml','yml','htm','html','md','ini']

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "digital_content_retrieval"
)



mycursor = mydb.cursor()
sql = "INSERT INTO file_storage (filename,name,content,extension) VALUES (%s,%s,%s,%s)"
values = []

for root, directories, files in os.walk(directory):
    rel_root = os.path.relpath(root, directory)

    if skip_dir in directories :
        directories.remove(skip_dir) 
        
    

    for file in files:
        p = os.path.join(rel_root, file)
        
        #skip hidden files
        if (file[0] == '.'):
            continue

        

    
        file_ext = file.split('.')
        if file_ext[1] in text_ext :
            txtfile = open(directory +'/'+p,'r',encoding='utf-8') 
            content = txtfile.read()
            val = (p,file,content,file_ext[1])
        else:
             val = (p,file,None,file_ext[1])

        mycursor.execute(sql,val)
        mydb.commit()
    
    
        

mydb.close()
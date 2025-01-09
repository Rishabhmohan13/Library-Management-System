mypass = "root"
mydatabase = "pylibrary"

def get_db_connection():
    import pymysql
    con = pymysql.connect(
        host="localhost",
        user="root",
        password=mypass,
        database=mydatabase
    )
    return con, con.cursor()
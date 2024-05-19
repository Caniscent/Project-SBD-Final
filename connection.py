import psycopg2

try:
    connection_string = "host='db.tbqsolution.my.id' port='5432' user='postgres' password='@Tbq2412' dbname='db_project_sbd'"
    conn = psycopg2.connect(connection_string)

    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(f"\ntersambung ke {record}")


except(Exception, psycopg2.Error) as err:
    print(f"\nError coy! nih lognya: {err}")

# finally:
#     if conn:
#         cursor.close()
#         conn.close()
#         print(f"koneksi ditutup")
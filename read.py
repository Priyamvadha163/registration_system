from db_config import get_connection

def read_registration():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "select * from Registration"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
if __name__ == "__main__":
    read_registration()
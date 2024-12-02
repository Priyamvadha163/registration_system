from db_config import get_connection

def update_registration(id, name):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "update Registration set name= %s where ID = %s"
        values = (name, id)
        cursor.execute(query, values)
        conn.commit()
        print("Record Updated")
    except Exception as e:
        print("error:", e)
    finally:
        cursor.close()
        conn.close()
if __name__ == "__main__":
    update_registration(1, "Priya")
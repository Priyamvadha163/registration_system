from db_config import get_connection

def delete_registration(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "delete from Registration where ID = %s"
        cursor.execute(query, (id,))
        conn.commit()
        print("Record Deleted")
    except Exception as e:
        print("error:", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    delete_registration(1)
from db_config import get_connection
def create_registration(name, email, dob, phone, address):
    try:
        conn = get_connection()
        cursor =conn.cursor()
        query = "Insert into Registration(Name, Email, DataOfBirth, PhoneNum, Address) values (%s, %s, %s, %s, %s)"
        values = (name, email, dob, phone, address)
        cursor.execute(query, values)
        conn.commit()
        print("Record is inserted")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
if __name__ == "__main__":
    create_registration("Priya", "priya@gmail.com", "2002-11-01", "8989767889", "bnglr")
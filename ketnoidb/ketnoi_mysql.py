import mysql.connector
from mysql.connector import Error

def connect_mysql(host='localhost', user='root', password='', database='qlythuocankhang'):
    """
    Hàm kết nối đến MySQL Database.
    Trả về đối tượng connection nếu thành công, hoặc None nếu thất bại.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,

            database=database
        )
        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print(f"❌ Lỗi khi kết nối MySQL: {e}")
        return None

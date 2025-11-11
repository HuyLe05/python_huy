from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error


def insert_danhmuc(ten_danhmuc, mota=None, trangthai=1):
    """
    Hàm thêm danh mục mới vào bảng 'danhmuc'
    """
    conn = connect_mysql()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        sql = """
        INSERT INTO danhmuc (ten_danhmuc, mota, trangthai)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (ten_danhmuc, mota, trangthai))
        conn.commit()
        print(f"✅ Đã thêm danh mục: {ten_danhmuc}")
        return True
    except Error as e:
        print(f"❌ Lỗi khi thêm danh mục: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

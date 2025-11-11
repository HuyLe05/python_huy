from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def delete_danhmuc(id_danhmuc):
    """
    Hàm xóa 1 danh mục theo id_danhmuc
    """
    conn = connect_mysql()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM danhmuc WHERE id_danhmuc = %s"
        cursor.execute(sql, (id_danhmuc,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có ID {id_danhmuc}")
            return True
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID {id_danhmuc}")
            return False

    except Error as e:
        print(f"❌ Lỗi khi xóa danh mục: {e}")
        return False

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error


def get_all_danhmuc():
    """
    Hàm lấy danh sách tất cả các danh mục trong bảng 'danhmuc'
    Trả về danh sách các dict (mỗi dict là 1 danh mục)
    """
    conn = connect_mysql()
    if conn is None:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id_danhmuc, ten_danhmuc, mota, trangthai FROM danhmuc ORDER BY id_danhmuc ASC")
        result = cursor.fetchall()

        if result:
            print(f"✅ Đã lấy {len(result)} danh mục.")
        else:
            print("⚠️ Không có danh mục nào trong cơ sở dữ liệu.")

        return result

    except Error as e:
        print(f"❌ Lỗi khi lấy danh sách danh mục: {e}")
        return []

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
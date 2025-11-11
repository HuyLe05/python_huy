from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error   


def update_danhmuc(id_danhmuc, ten_danhmuc=None, mota=None, trangthai=None):
    """
    Hàm cập nhật thông tin danh mục theo id_danhmuc.
    Chỉ cập nhật những trường được truyền vào.
    """
    conn = connect_mysql()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Tạo danh sách động các cột cần cập nhật
        updates = []
        params = []

        if ten_danhmuc is not None:
            updates.append("ten_danhmuc = %s")
            params.append(ten_danhmuc)
        if mota is not None:
            updates.append("mota = %s")
            params.append(mota)
        if trangthai is not None:
            updates.append("trangthai = %s")
            params.append(trangthai)

        # Nếu không có gì để cập nhật thì thoát
        if not updates:
            print("⚠️ Không có dữ liệu nào để cập nhật.")
            return False

        sql = f"UPDATE danhmuc SET {', '.join(updates)} WHERE id_danhmuc = %s"
        params.append(id_danhmuc)

        cursor.execute(sql, tuple(params))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục ID {id_danhmuc}")
            return True
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID {id_danhmuc}")
            return False

    except Error as e:
        print(f"❌ Lỗi khi cập nhật danh mục: {e}")
        return False

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
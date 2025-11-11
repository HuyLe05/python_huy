# -------------------------------
# 3️⃣ GIAO DIỆN TKINTER
# -------------------------------
from zoneinfo._common import load_data

from common.delete_danhmuc import delete_danhmuc
from common.insertdanhmuc import insert_danhmuc
from common.update_danhmuc import update_danhmuc
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


def on_tree_select(event):
    selected = tree.focus()
    if selected:
        data = tree.item(selected)['values']
        entry_ten.insert(0, data[1])
        entry_mota.insert(0, data[2])
        entry_trangthai.insert(0, data[3])
def load_data():
    """Hiển thị danh sách danh mục"""
    for row in tree.get_children():
        tree.delete(row)
    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id_danhmuc, ten_danhmuc, mota, trangthai FROM danhmuc ORDER BY id_danhmuc ASC")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        conn.close()
root = tk.Tk()
root.title("Quản lý Danh mục - PetShop")
root.geometry("700x500")
root.resizable(False, False)


# ---- Form nhập
frame_form = tk.LabelFrame(root, text="Thông tin danh mục", padx=10, pady=10)
frame_form.pack(fill="x", padx=10, pady=10)

tk.Label(frame_form, text="Tên danh mục:").grid(row=0, column=0, sticky="w")
entry_ten = tk.Entry(frame_form, width=40)
entry_ten.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Mô tả:").grid(row=1, column=0, sticky="w")
entry_mota = tk.Entry(frame_form, width=40)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Trạng thái (1/0):").grid(row=2, column=0, sticky="w")
entry_trangthai = tk.Entry(frame_form, width=10)
entry_trangthai.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# ---- Nút chức năng
frame_btn = tk.Frame(root)
frame_btn.pack(fill="x", padx=10, pady=5)

tk.Button(frame_btn, text="Thêm", width=10, bg="#4CAF50", fg="white").pack(side="left", padx=5)
tk.Button(frame_btn, text="Sửa", width=10, bg="#2196F3", fg="white").pack(side="left", padx=5)
tk.Button(frame_btn, text="Xoá", width=10, bg="#f44336", fg="white").pack(side="left", padx=5)
tk.Button(frame_btn, text="Làm mới", width=10).pack(side="left", padx=5)

# ---- Bảng hiển thị
frame_table = tk.Frame(root)
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("id_danhmuc", "ten_danhmuc", "mota", "trangthai")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=12)
tree.heading("id_danhmuc", text="ID")
tree.heading("ten_danhmuc", text="Tên danh mục")
tree.heading("mota", text="Mô tả")
tree.heading("trangthai", text="Trạng thái")

tree.column("id_danhmuc", width=50, anchor="center")
tree.column("ten_danhmuc", width=200)
tree.column("mota", width=250)
tree.column("trangthai", width=100, anchor="center")

tree.pack(fill="both", expand=True)
tree.bind("<<TreeviewSelect>>",)

# ---- Load dữ liệu ban đầu
load_data()

root.mainloop()
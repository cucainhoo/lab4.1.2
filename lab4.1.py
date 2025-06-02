# Cho phép người dùng gửi lên 1 file tần suất. Nạp vào kiểu dictionary và in ra ngoài màn hình
import streamlit as st
import ast 
st.title("Phục dựng đoạn văn từ tần suất từ")
tep = st.file_uploader("Chọn tệp .txt chứa tần suất từ", type=["txt"])
if tep:
    # Đọc nội dung file
    noi_dung = tep.read().decode("utf-8")
    tu_dien = ast.literal_eval(noi_dung)
    danh_sach_tu = []
    for tu, so_lan in tu_dien.items():
        danh_sach_tu.extend([tu] * so_lan)
    doan_van = " ".join(danh_sach_tu)
    st.write("Đoạn văn tái tạo: \n",doan_van)
    # Tải về văn bản trực tiếp bằng Streamlit
    st.download_button( 
        label="Tải về văn bản .txt", 
        data=doan_van, 
        file_name="van_ban_tu_dien.txt", 
        mime="text/plain"
    )



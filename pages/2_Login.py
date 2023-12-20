import streamlit as st
import mysql.connector

st.set_page_config(
    page_title="Login",
    page_icon="📝",
    layout="centered",
)
# Koneksi ke database MariaDB
def connect_to_db():   
    try:
        # Ganti dengan informasi koneksi database MariaDB kamu
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ciwong",
            database="tubes_alpro"
        )
        return conn
    except mysql.connector.Error as e:
        st.error(f"Error: {e}")
        return None

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
def login_page():

    st.title("Halaman Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Melakukan validasi login di sini
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()  
            # Ganti dengan query validasi login sesuai kebutuhanmu
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            
            if result:
                st.success("Login berhasil")
            else:
                st.error("Login gagal. Cek kembali username dan password")

def main():
    login_page()

if __name__ == "__main__":
    main()

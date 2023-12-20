import streamlit as st
from streamlit_option_menu import option_menu 
import mysql.connector

st.set_page_config(
    page_title="Buat bisnis model mu disini",
    page_icon="📝",
    layout="wide",
)
# Fungsi menghilangkan footer
hide_st_style = """
    <style>
        footer {visibility: hidden;}
    </style>
"""
def main():
     
    # Navigasi dengan tab
    st.header(":blue[Jasa Pembuatan Business Model Canvas]", divider="orange")
    selected_tab = option_menu(menu_title=None,options=["Menu Utama", "Create Canvas","Contact","Tentang Aplikasi"], icons=["house","book", "person-lines-fill", "briefcase"],orientation="horizontal",key="nav")

    st.write("")
    st.write("")
    st.write("")

    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")

    st.sidebar.image("img/sidebar.png", width=200)
    # Sidebar for admin login
    st.sidebar.subheader("Admin Login") 
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username:
            st.sidebar.success("Login successful!")
        else:
            st.sidebar.error("Invalid credentials")

    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")

    st.sidebar.subheader("Keluar dari akun anda")
    st.sidebar.button("Log Out")
    
    if selected_tab == "Menu Utama":
        h1, h2 ,h3, h4 = st.columns(4)
        with h1:
           st.write("")
        with h2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            st.header("Buat Planning Bisnis")
            st.write("With our platform, you can quantify your skills, grow in your role and stay relevant on critical topics.")
            b1, b2 = st.columns([2,5.3])
            with b1:
                st.button("Get Started")
            with b2:
                st.button("Learn More >")
            with h3:
                st.image("img/header.png", width=400)
            with h4:
                st.write("")
   
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")    

        # Deskripsi Business Model Canvas
        spasi1, spasi2 = st.columns(2)
        with spasi1:
            spasi_c1, spasi_c2, spasi_c3 = st.columns(3)
            with spasi_c1:
                st.write("")
            with spasi_c2:
                st.image("img/konten1.png", width=250)
            with spasi_c3:
                st.image("img/konten2.png", width=250)
        with spasi2:
            spasi2_c1, spasi2_c2, spasi2_c3 = st.columns(3)
            with spasi2_c1:
                st.image("img/konten3.png", width=250)
            with spasi2_c2:
                st.image("img/konten4.png", width=250)
            with spasi2_c3:
                st.write("")

        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")

        s1, s2, s3 = st.columns(3)
        with s1:
            st.write("")
        with s2:
            st.subheader("Components of a business model canvas")
            st.write("")
        with s3:
            st.write("")

        value1, value2, value3 = st.columns(3)
        with value1:
            st.image("img/key-partners.png", width=500)
            st.subheader("Key Partners")
            st.write("External companies or suppliers that’ll help with key activities")
        with value2:
            st.image("img/key-activities.png", width=500)
            st.subheader("Key Activities")
            st.write("Tasks or routines that implement your business model")
        with value3:
            st.image("img/key-resources.png", width=500)
            st.subheader("Key Resources") 
            st.write("Main inputs or sources to keep key activities rolling")

        value4, value5, value6 = st.columns(3)
        with value4:
            st.image("img/customer-relationship.png", width=500)
            st.subheader("Customer Relationhip")
            st.write("Level of interactions and engagements with your market")
        with value5:
            st.image("img/customer-segments.png", width=500)
            st.subheader("Customer Segments")
            st.write(
                "Target demographics of your business whether as individuals"
                "or organizations"
            )
        with value6:
            st.image("img/channels.png", width=500)
            st.subheader("Channels")
            st.write("Customer touchpoints to interact and communicate with your business")
        
        value7, value8, value9 = st.columns(3)
        with value7:
            st.image("img/value-proposition.png", width=500)
            st.subheader("Value Proposition")
            st.write("Unique selling proposition of the benefits of your product or service")
        with value8:
            st.image("img/cost.png", width=500)
            st.subheader("Cost structure")
            st.write("Costs and liabilities associated with running your business")
        with value9:
            st.image("img/revenue-streams.png", width=500)
            st.subheader("Revenue Streams")
            st.write("Sources of money generation and how your value propositions play in earning revenue")
            
    elif selected_tab == "Create Canvas":
        st.subheader("Buat Business Model anda disini")

        col1, col2, col3 = st.columns(3)
        with col1:
             st.text_area("Customer Segments",  "Isi disini")
        with col2:
             st.text_area("Value Propositions", "Isi disini")
        with col3:
             st.text_area("Channels", "Isi disini")

        col1, col2 = st.columns(2)
        with col1:
             st.text_area("Customer Relationships", "Isi disini")
        with col2:
             st.text_area("Revenue Streams", "Isi disini")

        st.text_area("Key Resources", "Isi disini")

        st.text_area("Key Activities", "Isi disini")

        col1, col2 = st.columns(2)
        with col1:
            st.text_area("Key Partnerships", "Isi disini")
        with col2:
            st.text_area("Cost Structure", "Isi disini")

        if st.button("Create Canvas"):
            st.success("Canvas berhasil dibuat!")

    elif selected_tab == "Contact":
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        spasi_kontak1, spasi_kontak2, spasi_kontak3 = st.columns([3,3,1]) 
        with spasi_kontak1:
            st.write("")
        with spasi_kontak2:
            st.header("CONTACT")
        with spasi_kontak3:
            st.write("")

        spasi_kontak4, spasi_kontak5, spasi_kontak6 = st.columns([3,4.2,1]) 
        with spasi_kontak4:
            st.write("")
        with spasi_kontak5:
            st.write("Jika ada pertanyaan lebih lanjut, hubungi kami disini")   
        with spasi_kontak6:
            st.write("")

        st.write("")
        st.write("")


        col1, col2, col3, col4 = st.columns([4,10,0.5,4])
        with col1:
            st.write("")
        with col2:
            with st.form(key='contact_form'):
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input(label='Nama Anda')
                with col2:
                    st.text_input(label='Email Anda')
                st.selectbox(label='Subjek', options=['', 'Pertanyaan', 'Saran', 'Lainnya'])
                st.text_area(label='Pesan')

                submit_button = st.form_submit_button(label='Kirim Pesan')
        with col3:
            st.write("")
        with col4:
            st.write("")
        
    elif selected_tab == "Tentang Aplikasi":
        st.subheader("What is Business Model Canvas?")
        st.write(
            "Business Model Canvas (BMC) adalah strategi manajemen yang disusun untuk menjabarkan ide dan konsep sebuah bisnis ke dalam bentuk visual. Sederhananya, pengertian Business Model Canvas adalah kerangka manajemen untuk memudahkan dalam melihat gambaran ide bisnis dan realisasinya secara cepat."
        )
        st.write(
            "Dibandingkan dengan bisnis plan yang berpuluh-puluh halaman, bisnis model canvas jauh lebih ringkas karena disusun ke dalam satu halaman saja. Maka itu, kerangka bisnis ini paling populer di kalangan bisnis startup."
        )
        st.write(
            "Bisnis model canvas diperkenalkan tahun 2005 oleh Alexander Osterwalder, seorang entrepreneur asal Swiss dalam bukunya berjudul Business Model Generation. Di dalamnya, Ia menjelaskan framework sederhana yang merepresentasikan elemen-elemen penting dalam model bisnis"
        )
        # Kolom dengan deskripsi
        st.subheader("9 Elemen dalam Business Model Canvas")

        gambar_canvas, text = st.columns(2)
        with gambar_canvas:
            st.image("img/g1.png")
        with text:
            st.markdown("1. Customer Segments")
            st.markdown("2. Value Proposition")
            st.markdown("3. Channels")
            st.markdown("4. Revenue Streams")
            st.markdown("5. Key Resource")
            st.markdown("6. Customer Relationship")
            st.markdown("7. Key Activities")
            st.markdown("8. Key Partnership")
            st.markdown("9. Cost Structure")

        st.text("")
        st.text("")

        st.header("Pengertian Elemen")

        elemen1, elemen2 = st.columns(2)
        with elemen1:
            st.subheader("1. Customer Segments (Segmentasi konsumen)")
            st.write("Elemen pertama yang wajib ada dalam bisnis model canvas adalah segmentasi konsumen. Apapun jenis bisnis yang dijalankan, tentukan segmentasi pelanggan dengan tepat di awal. Kamu harus menentukan siapa yang menjadi target bisnis, segmen pelanggan mana yang berpotensi membeli produk atau layananmu.")
            
            st.subheader("2. Value Proposition (Proposisi nilai konsumen)")
            st.write("Setelah menentukan siapa saja target konsumen, kamu harus tahu bagaimana bisnismu bisa bermanfaatnya bagi para pelanggan. Value proposition menjabarkan poin-poin atau nilai yang ditawarkan oleh suatu bisnis bagi segmen konsumennya.")

            st.subheader("3. Channels (Saluran)")
            st.write("Channel merupakan media interaksi antara bisnis dengan konsumen untuk menyampaikan produk dan layanannya. Penentuan channel adalah salah satu faktor penentu kesuksesan dalam berbisnis. Pikirkan dengan baik channel apa saja yang akan digunakan untuk menjangkau pelanggan, misalnya dengan media sosial, ads, marketplace, dan website.")

            st.subheader("4. Customer Relationship (Hubungan konsumen)")
            st.write("Setelah memahami segmentasi konsumen dan channel yang digunakan, saatnya menentukan bagaimana bisnis kamu berinteraksi dengan pelanggan.")
            st.write("Ketahui bagaimana cara menjalin hubungan dengan konsumen agar mereka tidak mudah berpaling ke kompetitor lain. Contoh yang bisa diterapkan misalnya memberikan promo, giveaway, atau program membership.")
            st.write("Karakteristik tiap pelanggan berbeda-beda, maka itu kamu harus memahami bagaimana mengambil hati dan mempertahankan pelanggan yang sudah ada. Bukan hanya saat menjual produk saja, tapi juga ketika menghadapi komplain, menjawab pertanyaan pelanggan, dan sebagainya.")

        with elemen2:
            st.subheader("5. Revenue Streams (Sumber pendapatan)")
            st.write("Elemen pertama yang wajib ada dalam bisnis model canvas adalah segmentasi konsumen. Apapun jenis bisnis yang dijalankan, tentukan segmentasi pelanggan dengan tepat di awal. Kamu harus menentukan siapa yang menjadi target bisnis, segmen pelanggan mana yang berpotensi membeli produk atau layananmu.")   

            st.subheader("6. Key Resource (Sumber daya)")
            st.write("Elemen pertama yang wajib ada dalam bisnis model canvas adalah segmentasi konsumen. Apapun jenis bisnis yang dijalankan, tentukan segmentasi pelanggan dengan tepat di awal. Kamu harus menentukan siapa yang menjadi target bisnis, segmen pelanggan mana yang berpotensi membeli produk atau layananmu.")

            st.subheader("7. Key Activities (Aktivitas yang dijalankan)")
            st.write("Elemen pertama yang wajib ada dalam bisnis model canvas adalah segmentasi konsumen. Apapun jenis bisnis yang dijalankan, tentukan segmentasi pelanggan dengan tepat di awal. Kamu harus menentukan siapa yang menjadi target bisnis, segmen pelanggan mana yang berpotensi membeli produk atau layananmu.")

            st.subheader("8. Key Partnership (Kerja sama)")
            st.write("Elemen pertama yang wajib ada dalam bisnis model canvas adalah segmentasi konsumen. Apapun jenis bisnis yang dijalankan, tentukan segmentasi pelanggan dengan tepat di awal. Kamu harus menentukan siapa yang menjadi target bisnis, segmen pelanggan mana yang berpotensi membeli produk atau layananmu.")

            st.subheader("9. Cost Structure (Struktur biaya)")
            st.write("Elemen pertama yang wajib ada dalam bisnis model canvas adalah segmentasi konsumen. Apapun jenis bisnis yang dijalankan, tentukan segmentasi pelanggan dengan tepat di awal. Kamu harus menentukan siapa yang menjadi target bisnis, segmen pelanggan mana yang berpotensi membeli produk atau layananmu.")   
                
if __name__ == "__main__":
    main()
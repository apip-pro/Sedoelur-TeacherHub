import streamlit as st

# Data Guru SMAN 1 Krian (Tanpa NIS/NIP)
DATA_GURU = [
    {"nama": "AAN AS'ARI, S.Ag., M.Pd.i", "mapel": "Guru Agama Islam", "jabatan": "Guru"},
    {"nama": "AGUS SURIANTO., S.Psi", "mapel": "Bimbingan Konseling", "jabatan": "Guru"},
    {"nama": "ALI AGUS, S.Pd., M.Pd", "mapel": "Guru Kimia", "jabatan": "Guru"},
    {"nama": "BAYU BUDI LUHUR S.Pd., Gr", "mapel": "Guru Olah Raga", "jabatan": "Guru"},
    {"nama": "DANIEL DWI WICAKSONO., S.Pd", "mapel": "Guru Sosiologi", "jabatan": "Guru"},
    {"nama": "DIAH WAHYUNI INDRIANAWATI, S.Pd., Gr", "mapel": "Guru Bahasa Jepang", "jabatan": "Guru"},
    {"nama": "DIAN PRATIWI MURTI., S.Pd", "mapel": "Guru Bahasa Jawa", "jabatan": "Guru"},
    {"nama": "DIAN PRATIWI., S.Pd", "mapel": "Guru Seni Rupa", "jabatan": "Guru"},
    {"nama": "Dra. DWI EMAWATI SUSANANINGSIH", "mapel": "Guru Biologi", "jabatan": "Guru"},
    {"nama": "Dra. NOVA RITA WALELANG", "mapel": "Guru Bahasa Indonesia", "jabatan": "Guru"},
    {"nama": "Dra. SUHESTI", "mapel": "Guru Fisika", "jabatan": "Guru"},
    {"nama": "Dra. YUNI ASTUTI", "mapel": "Guru Bahasa Indonesia", "jabatan": "Guru"},
    {"nama": "Dra. YUNI SUSILOWATI", "mapel": "Guru Bahasa Indonesia", "jabatan": "Guru"},
    {"nama": "Drs. H. TURKHAN", "mapel": "Bimbingan Konseling", "jabatan": "Guru"},
    {"nama": "Drs. ISMAIL", "mapel": "Guru Sejarah", "jabatan": "Guru"},
    {"nama": "Drs. MOCH YAMIN", "mapel": "Guru Matematika", "jabatan": "Guru"},
    {"nama": "Drs. PRANMUJI WAHYUONO, M.Pd", "mapel": "Guru Bahasa Indonesia", "jabatan": "Guru"},
    {"nama": "Drs. RAHADIONO, M.Pd", "mapel": "Guru Bahasa Inggris", "jabatan": "Guru"},
    {"nama": "Drs. WASIS HERU SUPRIYANTO", "mapel": "Guru Matematika", "jabatan": "Guru"},
    {"nama": "DWI HARIYANTI, S.Pd", "mapel": "Guru Bahasa Indonesia", "jabatan": "Guru"},
    {"nama": "DWI SELLY NURIANTI, S.Pd", "mapel": "Guru Sejarah", "jabatan": "Guru"},
    {"nama": "EKNAL YONSA PERIKLES, S.Pd., Gr", "mapel": "Guru Olah Raga", "jabatan": "Guru"},
    {"nama": "ETY SETYAWATI, SE", "mapel": "Guru Ekonomi", "jabatan": "Guru"},
    {"nama": "FADJARIYAH, S.Pd", "mapel": "Guru Fisika", "jabatan": "Guru"},
    {"nama": "FELANA RIZKITA SHINTAWATI, S.Pd., Gr", "mapel": "Guru Pendidikan Pancasila", "jabatan": "Guru"},
    {"nama": "FUJI ANJARWATI, S.Pd., M.Pd", "mapel": "Guru Fisika", "jabatan": "Guru"},
    {"nama": "GLORIA VERNANDA., S.Pd", "mapel": "Guru Agama Katolik", "jabatan": "Guru"},
    {"nama": "HADISTA ARI SANTOSO., S.Pd", "mapel": "Guru Pendidikan Pancasila", "jabatan": "Guru"},
    {"nama": "HUSFINA LAILIYATUS SUAIDAH., S.Pd", "mapel": "Guru Biologi", "jabatan": "Guru"},
    {"nama": "IKA LISTIAWATI., S.Pd", "mapel": "Guru Matematika", "jabatan": "Guru"},
    {"nama": "INDAH JUMIATI, S.Pd", "mapel": "Guru Olah Raga", "jabatan": "Guru"},
    {"nama": "IRMA QURROTA A'YUN., S.Pd", "mapel": "Guru Bahasa Jepang", "jabatan": "Guru"},
    {"nama": "JOKO MARIANTO, S.Pd", "mapel": "Guru Seni Rupa", "jabatan": "Guru"},
    {"nama": "JUWINA RATU WULANDARI., S.Pd", "mapel": "Guru Sosiologi", "jabatan": "Guru"},
    {"nama": "KHRISTI WIDIASTUTIK, S.Pd., Gr", "mapel": "Guru Prakarya", "jabatan": "Guru"},
    {"nama": "KHUSNUL KHOTIMAH, S. Pd., Gr", "mapel": "Guru Bahasa Inggris", "jabatan": "Guru"},
    {"nama": "MALIKATUN NGILMAN NAFIAH., S.Pd", "mapel": "Guru Matematika", "jabatan": "Guru"},
    {"nama": "MARIA ULFA, S.Pd", "mapel": "Guru Matematika", "jabatan": "Guru"},
    {"nama": "MAYA SEPTIANA., S.Pd", "mapel": "Guru Bahasa Indonesia", "jabatan": "Guru"},
    {"nama": "MOCH. SYAUQI., S.Ag", "mapel": "Guru Agama Islam", "jabatan": "Guru"},
    {"nama": "MOH. FANDIK, S.Pd., Gr", "mapel": "Guru Sejarah", "jabatan": "Guru"},
    {"nama": "MUHERI PALWANTO, S.Pd., M.Pd", "mapel": "Guru Seni Rupa", "jabatan": "Guru"},
    {"nama": "NOVI IKA WARDANI., S.Si", "mapel": "Guru Kimia", "jabatan": "Guru"},
    {"nama": "NUNUK DWI ANGGRAENI., S.Psi", "mapel": "Bimbingan Konseling", "jabatan": "Guru"},
    {"nama": "NURHAYATI., S.Pd", "mapel": "Guru Biologi", "jabatan": "Guru"},
    {"nama": "NURKA AYU FAJERIN, S.Pd., Gr", "mapel": "Guru Ekonomi", "jabatan": "Guru"},
    {"nama": "NURUL ZAKQIYAH., S.Pd", "mapel": "Bimbingan Konseling", "jabatan": "Guru"},
    {"nama": "NURYAHYA, S.Pd", "mapel": "Guru Fisika", "jabatan": "Guru"},
    {"nama": "PRISTIANA APRILIA FISKA., S.Pd", "mapel": "Guru Biologi", "jabatan": "Guru"},
    {"nama": "PURBA WAHYU ADI., S.Pd., M.Pd", "mapel": "Guru Ekonomi", "jabatan": "Guru"},
    {"nama": "RETNO SALARAS MAHATI., S.Pd", "mapel": "Guru Geografi", "jabatan": "Guru"},
    {"nama": "RINDRA AYU LOVENIDIANA., S.Pd", "mapel": "Guru Matematika", "jabatan": "Guru"},
    {"nama": "RIRIS VADIYATUN NISWAH, M.Pd", "mapel": "Guru Bahasa Inggris", "jabatan": "Guru"},
    {"nama": "ROSEIDA PRISTIWARDANI S., S.Pd", "mapel": "Guru Ekonomi", "jabatan": "Guru"},
    {"nama": "SIYATIN, S.Pd", "mapel": "Guru Bahasa Inggris", "jabatan": "Guru"},
    {"nama": "SUKARNO., M.Pd.i", "mapel": "Guru Agama Islam", "jabatan": "Guru"},
    {"nama": "SUMARNI, M.Pd", "mapel": "Guru Kimia", "jabatan": "Guru"},
    {"nama": "THERESIA KAROLINA DEWI., S.Pd", "mapel": "Guru Bahasa Inggris", "jabatan": "Guru"},
    {"nama": "TRI KUNCORO., S.Pd", "mapel": "Guru Geografi", "jabatan": "Guru"},
    {"nama": "YANTI INDIRA, S.Pd", "mapel": "Bimbingan Konseling", "jabatan": "Guru"},
    {"nama": "YOFFA DESSY ANTARIKSAWATI., S.Pd", "mapel": "Guru Pendidikan Pancasila", "jabatan": "Guru"},
    {"nama": "YOSEP SUBIANTORO., S.Pd", "mapel": "Guru Agama Kristen", "jabatan": "Guru"},
    {"nama": "YUNITA SYAHWATI., S.Pd", "mapel": "Guru Kimia", "jabatan": "Guru"},
    {"nama": "ZUNAITA HERMIATI, S.Kom", "mapel": "Guru Informatika", "jabatan": "Guru"}
]

# Pengaturan Halaman Streamlit
st.set_page_config(page_title="Informasi Guru SMAN 1 Krian", page_icon="🏫")

# Judul Utama
st.title("🏫 Chatbot Informasi Guru SMAN 1 Krian")
st.write("Cari informasi guru berdasarkan **Nama** atau **Mata Pelajaran** (contoh: *Kimia*, *Ismail*, *Bahasa Inggris*, *Daftar Guru*).")

# Inisialisasi Riwayat Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan Riwayat Chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Mengirim Pesan
if user_input := st.chat_input("Tanyakan nama guru atau mata pelajaran..."):
    # Tampilkan input pengguna
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    query = user_input.strip().lower()

    # Logika Pencarian
    if query in ["daftar guru", "semua guru", "list guru", "semua"]:
        response = f"📋 **Daftar Guru SMAN 1 Krian (Total: {len(DATA_GURU)}):**\n\n"
        for idx, guru in enumerate(DATA_GURU, 1):
            response += f"{idx}. **{guru['nama']}** — {guru['mapel']}\n"
    else:
        # Filter nama atau mata pelajaran
        hasil = [
            g for g in DATA_GURU 
            if query in g["nama"].lower() or query in g["mapel"].lower()
        ]

        if hasil:
            response = f"🎒 **Berikut informasi guru yang ditemukan ({len(hasil)} guru):**\n\n"
            for g in hasil:
                response += f"• **{g['nama']}**\n"
                response += f"  - **Bidang/Mapel:** {g['mapel']}\n"
                response += f"  - **Status:** {g['jabatan']}\n\n"
        else:
            response = f"❌ Maaf, data guru atau mata pelajaran dengan kata kunci '**{user_input}**' tidak ditemukan."

    # Tampilkan respon chatbot
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

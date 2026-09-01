import streamlit as st

# Data Guru Lembaga Sekolah
DATA_GURU = [
    {
        "nama": "Siti Rahma, M.Pd.",
        "mapel": "Biologi",
        "jabatan": "Guru / Wali Kelas X"
    },
    {
        "nama": "Ahmad Fauzi, S.T.",
        "mapel": "Matematika",
        "jabatan": "Kepala Sekolah"
    },
    {
        "nama": "Budi Santoso, S.Pd.",
        "mapel": "Informatika",
        "jabatan": "Pembina OSIS"
    },
    {
        "nama": "Dewi Lestari, S.S.",
        "mapel": "Bahasa Inggris",
        "jabatan": "Guru / Guru Piket"
    }
]

# Pengaturan Halaman
st.set_page_config(page_title="Informasi Guru Sekolah", page_icon="🏫")

# Judul dan Deskripsi
st.title("🏫 Chatbot Informasi Guru Sekolah")
st.write("Cari informasi guru berdasarkan **nama** atau **mata pelajaran** (contoh: *Biologi*, *Budi*, *Daftar Guru*).")

# Inisialisasi Riwayat Chat di Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan Riwayat Chat yang Ada
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input dari Pengguna
if user_input := st.chat_input("Tanyakan nama guru atau mapel..."):
    # Simpan dan tampilkan pesan dari pengguna
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    query = user_input.strip().lower()

    # Logika Pencarian Data Guru
    if query in ["daftar guru", "semua guru", "list guru", "semua"]:
        response = "📋 **Daftar Seluruh Guru:**\n"
        for idx, guru in enumerate(DATA_GURU, 1):
            response += f"{idx}. **{guru['nama']}** — {guru['mapel']} ({guru['jabatan']})\n"
    else:
        # Filter guru berdasarkan nama atau mata pelajaran
        hasil = [
            g for g in DATA_GURU 
            if query in g["nama"].lower() or query in g["mapel"].lower() or query in g["jabatan"].lower()
        ]

        if hasil:
            response = "🎒 **Berikut informasi guru yang ditemukan:**\n\n"
            for g in hasil:
                response += f"• **{g['nama']}**\n"
                response += f"  - **Mata Pelajaran:** {g['mapel']}\n"
                response += f"  - **Peran/Jabatan:** {g['jabatan']}\n\n"
        else:
            response = f"❌ Maaf, data guru atau mata pelajaran dengan kata kunci '**{user_input}**' tidak ditemukan."

    # Simpan dan tampilkan respon chatbot
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

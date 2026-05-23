import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

# =========================
# CONFIG
# =========================

st.set_page_config(
    page_title="ChemInsight",
    page_icon="🧪",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("🧪 ChemInsight")

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "🏠 Home",
        "🧪 Perhitungan pH",
        "⚗️ Molaritas & Normalitas",
        "💧 Pengenceran Larutan",
        "📊 Analisis Titrasi",
        "📈 Grafik Laboratorium",
        "📂 Upload CSV",
        "ℹ️ Tentang Aplikasi"
    ]
)

# =========================
# HOME
# =========================

if menu == "🏠 Home":

    st.title("🧪 ChemInsight")

    st.subheader(
        "Web Aplikasi Analisis Data Laboratorium dan Perhitungan Parameter Kimia"
    )

    st.markdown("""
    ### Fitur Aplikasi
    
    ✅ Perhitungan pH
    
    ✅ Molaritas dan Normalitas
    
    ✅ Pengenceran Larutan
    
    ✅ Analisis Titrasi
    
    ✅ Upload Data CSV
    
    ✅ Visualisasi Grafik
    
    ✅ Statistik Data Laboratorium
    """)

    st.info(
        "Gunakan menu di sidebar untuk memilih fitur analisis."
    )

# =========================
# pH
# =========================

elif menu == "🧪 Perhitungan pH":

    st.title("🧪 Perhitungan pH")

    konsentrasi = st.number_input(
        "Masukkan Konsentrasi H+ (M)",
        min_value=0.0000001,
        format="%f"
    )

    if st.button("Hitung pH"):

        ph = -math.log10(konsentrasi)

        st.success(f"Nilai pH = {ph:.2f}")

# =========================
# MOLARITAS
# =========================

elif menu == "⚗️ Molaritas & Normalitas":

    st.title("⚗️ Molaritas & Normalitas")

    massa = st.number_input("Massa zat (gram)")
    mr = st.number_input("Mr zat")
    volume = st.number_input("Volume larutan (mL)")
    valensi = st.number_input("Valensi")

    if st.button("Hitung Konsentrasi"):

        if mr != 0 and volume != 0:

            mol = massa / mr

            molaritas = mol / (volume / 1000)

            normalitas = molaritas * valensi

            st.success(f"Molaritas = {molaritas:.2f} M")

            st.success(f"Normalitas = {normalitas:.2f} N")

        else:

            st.error("Mr dan volume tidak boleh 0")

# =========================
# PENGENCERAN
# =========================

elif menu == "💧 Pengenceran Larutan":

    st.title("💧 Pengenceran Larutan")

    m1 = st.number_input("Molaritas Awal (M)")
    v1 = st.number_input("Volume Awal (mL)")
    v2 = st.number_input("Volume Akhir (mL)")

    if st.button("Hitung Pengenceran"):

        if v2 != 0:

            m2 = (m1 * v1) / v2

            st.success(f"Molaritas Akhir = {m2:.2f} M")

        else:

            st.error("Volume akhir tidak boleh 0")

# =========================
# TITRASI
# =========================

elif menu == "📊 Analisis Titrasi":

    st.title("📊 Analisis Titrasi")

    m1 = st.number_input("Molaritas Larutan 1")
    v1 = st.number_input("Volume Larutan 1")
    v2 = st.number_input("Volume Larutan 2")

    if st.button("Hitung Titrasi"):

        if v2 != 0:

            m2 = (m1 * v1) / v2

            st.success(f"Molaritas Larutan 2 = {m2:.2f} M")

        else:

            st.error("Volume larutan 2 tidak boleh 0")

# =========================
# GRAFIK
# =========================

elif menu == "📈 Grafik Laboratorium":

    st.title("📈 Grafik Laboratorium")

    file = st.file_uploader(
        "Upload File CSV untuk Grafik",
        type=["csv"]
    )

    if file is not None:

        data = pd.read_csv(file, sep=';')

        st.write("### Data CSV")
        st.dataframe(data)

        kolom_x = st.selectbox(
            "Pilih Sumbu X",
            data.columns
        )

        kolom_y = st.selectbox(
            "Pilih Sumbu Y",
            data.columns
        )

        # ubah koma menjadi titik
        data[kolom_y] = pd.to_numeric(
            data[kolom_y].astype(str).str.replace(',', '.'),
            errors='coerce'
        )

        fig, ax = plt.subplots()

        ax.plot(
            data[kolom_x],
            data[kolom_y],
            marker='o'
        )

        ax.set_xlabel(kolom_x)
        ax.set_ylabel(kolom_y)

        st.pyplot(fig)
        
# =========================
# UPLOAD CSV
# =========================

elif menu == "📂 Upload CSV":

    st.title("📂 Upload Data CSV")

    jenis = st.selectbox(
        "Pilih Jenis Analisis",
        [
            "Perhitungan pH",
            "Molaritas",
            "Pengenceran",
            "Titrasi"
        ]
    )

    file = st.file_uploader(
        "Upload File CSV",
        type=["csv"]
    )

    if file is not None:

        data = pd.read_csv(file, sep=';')

        st.write("### Data Awal")
        st.dataframe(data)

        # ======================
        # pH
        # ======================

        if jenis == "Perhitungan pH":

            data["pH"] = -pd.to_numeric(
    data["Konsentrasi_H+"].astype(str).str.replace(',', '.'),
    errors='coerce'
).apply(math.log10)

            st.write("### Hasil Perhitungan pH")
            st.dataframe(data)

        # ======================
        # MOLARITAS
        # ======================

        elif jenis == "Molaritas":

            data["Molaritas"] = (
                (data["Massa_g"] / data["Mr"])
                /
                (data["Volume_mL"] / 1000)
            )

            st.write("### Hasil Perhitungan Molaritas")
            st.dataframe(data)

        # ======================
        # PENGENCERAN
        # ======================

        elif jenis == "Pengenceran":

            data["M2"] = (
                data["M1"] * data["V1_mL"]
            ) / data["V2_mL"]

            st.write("### Hasil Pengenceran")
            st.dataframe(data)

        # ======================
        # TITRASI
        # ======================

        elif jenis == "Titrasi":

            data["M2"] = (
                data["M1"] * data["V1_mL"]
            ) / data["V2_mL"]

            st.write("### Hasil Analisis Titrasi")
            st.dataframe(data)

        st.write("### Statistik Data")
        st.write(data.describe())

# =========================
# ABOUT
# =========================

elif menu == "ℹ️ Tentang Aplikasi":

    st.title("ℹ️ Tentang ChemInsight")

    st.markdown("""
    ChemInsight merupakan web aplikasi berbasis Streamlit
    yang digunakan untuk analisis data laboratorium dan
    perhitungan parameter kimia secara otomatis.
    
    ### Dibuat Oleh
    Kelompok 3
    
    ### Teknologi
    - Python
    - Streamlit
    - Pandas
    - Matplotlib
    """)

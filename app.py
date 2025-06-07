# =================================================================
# KODE LENGKAP UNTUK APLIKASI MEDIA INTELLIGENCE DASHBOARD
# File: app.py
# =================================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# --- KONFIGURASI HALAMAN ---
# Mengatur konfigurasi halaman Streamlit. 'wide' membuat layout menggunakan seluruh lebar layar.
# Ini harus menjadi perintah Streamlit pertama yang dijalankan.
st.set_page_config(
    page_title="Media Intelligence Dashboard | SwayTea",
    page_icon="📊",
    layout="wide"
)

# --- FUNGSI UNTUK MEMUAT DAN MEMBERSIHKAN DATA ---
# Menggunakan cache agar data tidak perlu dimuat ulang setiap kali ada interaksi dari pengguna.
# Ini sangat meningkatkan performa aplikasi.
@st.cache_data
def load_data(file_path='SwayTea.csv'):
    """
    Memuat data dari file CSV yang ada di repositori.
    Melakukan pembersihan dan transformasi data dasar.
    """
    df = pd.read_csv(file_path)

    # --- Pembersihan & Transformasi Data ---
    # 1. Konversi kolom 'Date' ke format datetime agar bisa difilter berdasarkan rentang waktu.
    df['Date'] = pd.to_datetime(df['Date'])
    
    # 2. Pisahkan kolom 'Influencer_Brand' menjadi 'Influencer' dan 'Brand'.
    #    Menggunakan try-except untuk menangani jika ada baris yang formatnya tidak sesuai.
    try:
        split_cols = df['Influencer_Brand'].str.split('|', expand=True)
        df['Influencer'] = split_cols[0].str.strip()
        df['Brand'] = split_cols[1].str.strip()
    except Exception as e:
        # Jika terjadi error, buat kolom kosong agar aplikasi tidak crash.
        df['Influencer'] = 'N/A'
        df['Brand'] = 'N/A'
        st.warning(f"Gagal memisahkan kolom 'Influencer_Brand'. Error: {e}")

    # 3. Hapus kolom asli yang sudah tidak terpakai.
    df.drop(columns=['Influencer_Brand'], inplace=True)
    
    return df

# --- UI: SIDEBAR UNTUK FILTER ---
# Semua widget filter diletakkan di sidebar agar tampilan utama tetap bersih.
st.sidebar.header("📊 Filter Dashboard")

# Memuat data menggunakan fungsi yang sudah dibuat.
# Pesan spinner memberikan feedback visual kepada pengguna saat data dimuat.
with st.spinner('Memuat data...'):
    df = load_data()

# Filter berdasarkan rentang tanggal
st.sidebar.subheader("Filter Tanggal")
min_date = df['Date'].min().date()
max_date = df['Date'].max().date()
start_date, end_date = st.sidebar.date_input(
    "Pilih rentang tanggal:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)
# Konversi kembali ke tipe datetime untuk filtering
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter lainnya (Platform, Sentimen, Lokasi)
st.sidebar.subheader("Filter Lainnya")
selected_platforms = st.sidebar.multiselect(
    "Pilih Platform:",
    options=df['Platform'].unique(),
    default=df['Platform'].unique()
)
selected_sentiments = st.sidebar.multiselect(
    "Pilih Sentimen:",
    options=df['Sentiment'].unique(),
    default=df['Sentiment'].unique()
)
selected_locations = st.sidebar.multiselect(
    "Pilih Lokasi:",
    options=df['Location'].unique(),
    default=df['Location'].unique()
)

# --- PENERAPAN FILTER KE DATAFRAME ---
# Membuat dataframe baru yang sudah difilter sesuai input pengguna.
df_filtered = df[
    (df['Date'] >= start_date) & (df['Date'] <= end_date) &
    (df['Platform'].isin(selected_platforms)) &
    (df['Sentiment'].isin(selected_sentiments)) &
    (df['Location'].isin(selected_locations))
]

# --- UI: DASHBOARD UTAMA ---
st.title("📊 Interactive Media Intelligence Dashboard")
st.markdown("Analisis Performa Kampanye **SwayTea** di Berbagai Media Sosial")

# Cek jika dataframe hasil filter kosong untuk mencegah error.
if df_filtered.empty:
    st.warning("Tidak ada data yang cocok dengan filter yang Anda pilih. Silakan ubah pilihan filter Anda.")
else:
    # --- Ringkasan Metrik Utama (KPIs) ---
    total_posts = len(df_filtered)
    total_engagements = int(df_filtered['Engagements'].sum())
    avg_engagements = df_filtered['Engagements'].mean()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Posts", value=f"{total_posts:,}")
    with col2:
        st.metric(label="Total Engagements", value=f"{total_engagements:,}")
    with col3:
        st.metric(label="Rata-rata Engagement/Post", value=f"{avg_engagements:,.2f}")

    st.markdown("---")

    # --- Membuat TABS untuk visualisasi yang lebih rapi ---
    tab1, tab2, tab3 = st.tabs(["📈 Analisis Umum", "🧑‍💻 Analisis Detail", "📄 Data Mentah"])

    with tab1:
        st.subheader("Tren Engagement dari Waktu ke Waktu")
        engagement_over_time = df_filtered.groupby('Date')['Engagements'].sum().reset_index()
        fig_time = px.line(engagement_over_time, x='Date', y='Engagements', title='Total Engagement Harian')
        st.plotly_chart(fig_time, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Distribusi Sentimen")
            sentiment_dist = df_filtered['Sentiment'].value_counts().reset_index()
            fig_pie = px.pie(sentiment_dist, names='Sentiment', values='count', 
                             title='Proporsi Sentimen Post', hole=0.4,
                             color_discrete_map={'Positive':'#2ca02c', 'Neutral':'#ff7f0e', 'Negative':'#d62728'})
            st.plotly_chart(fig_pie, use_container_width=True)

        with col2:
            st.subheader("Engagement per Platform")
            platform_engagement = df_filtered.groupby('Platform')['Engagements'].sum().sort_values(ascending=False).reset_index()
            fig_bar_platform = px.bar(platform_engagement, x='Platform', y='Engagements', 
                                      title='Total Engagement Berdasarkan Platform', text_auto=True)
            st.plotly_chart(fig_bar_platform, use_container_width=True)

    with tab2:
        st.subheader("Analisis Performa Berdasarkan Kategori")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Top Influencer berdasarkan Engagement")
            influencer_engagement = df_filtered.groupby('Influencer')['Engagements'].sum().sort_values(ascending=False).reset_index()
            fig_influencer = px.bar(influencer_engagement.head(10), y='Influencer', x='Engagements', 
                                    orientation='h', title='Top 10 Influencer dengan Engagement Tertinggi', text_auto='.2s')
            fig_influencer.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_influencer, use_container_width=True)

        with col2:
            st.subheader("Engagement per Tipe Post")
            post_type_engagement = df_filtered.groupby('Post_Type')['Engagements'].sum().sort_values(ascending=False).reset_index()
            fig_post_type = px.bar(post_type_engagement, x='Post_Type', y='Engagements', 
                                   title='Total Engagement Berdasarkan Tipe Post', text_auto='.2s')
            st.plotly_chart(fig_post_type, use_container_width=True)

        st.subheader("Engagement per Lokasi")
        location_engagement = df_filtered.groupby('Location')['Engagements'].sum().sort_values(ascending=False).reset_index()
        fig_location = px.bar(location_engagement, x='Location', y='Engagements', 
                              title='Total Engagement Berdasarkan Lokasi', text_auto='.2s')
        st.plotly_chart(fig_location, use_container_width=True)

    with tab3:
        st.subheader("Data Mentah Sesuai Filter")
        st.markdown("Anda dapat mengurutkan data dengan mengklik header kolom.")
        st.dataframe(df_filtered)

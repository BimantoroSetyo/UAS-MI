# 📊 Interactive Media Intelligence Dashboard for SwayTea

## 📝 Deskripsi dan Tujuan Proyek

Ini adalah aplikasi dashboard interaktif berbasis web yang dirancang untuk menganalisis dan memvisualisasikan data performa kampanye media sosial untuk brand fiktif "SwayTea".

**Tujuan Proyek:** Dalam konteks **Produksi Media dan Intelijen Media**, alat ini sangat relevan karena mampu mengubah data mentah dari berbagai platform menjadi wawasan strategis yang dapat ditindaklanjuti. Dashboard ini membantu manajer merek, ahli strategi media, dan pembuat konten untuk:
*   Memantau kesehatan kampanye secara *real-time*.
*   Mengidentifikasi platform, influencer, dan tipe konten yang paling efektif.
*   Memahami sentimen audiens terhadap kampanye.
*   Membuat keputusan berbasis data untuk mengoptimalkan strategi media di masa depan.

---

## 🚀 Live Demo

Anda dapat mengakses dan mencoba langsung aplikasi dashboard yang telah di-deploy melalui link berikut:

**[Klik di sini untuk membuka aplikasi]([LINK_APLIKASI_STREAMLIT_ANDA])**

*(Catatan: Ganti `[LINK_APLIKASI_STREAMLIT_ANDA]` dengan URL publik dari Streamlit Community Cloud Anda setelah deploy.)*

---

## 🖼️ Tampilan Aplikasi

![Dashboard Screenshot](link_ke_screenshot_anda.png)

*(Saran: Ambil screenshot aplikasi Anda yang sudah berjalan, upload ke repositori GitHub, lalu ganti `link_ke_screenshot_anda.png` dengan nama file gambar Anda.)*

---

## ✨ Fitur Utama

*   **Dashboard Interaktif:** Visualisasi data yang dinamis dan responsif terhadap input pengguna.
*   **Filter Data Komprehensif:** Pengguna dapat memfilter data berdasarkan:
    *   Rentang Tanggal
    *   Platform Media Sosial (TikTok, X/Twitter, Instagram, YouTube)
    *   Sentimen (Positif, Negatif, Netral)
    *   Lokasi Geografis
*   **Key Performance Indicators (KPIs):** Tampilan metrik utama secara ringkas, seperti Total Post, Total Engagement, dan Rata-rata Engagement per Post.
*   **Analisis Mendalam:** Grafik interaktif untuk menganalisis:
    *   Tren Engagement dari waktu ke waktu.
    *   Distribusi sentimen kampanye.
    *   Performa engagement di setiap platform.
    *   Influencer dengan performa terbaik.
    *   Tipe post yang paling menarik audiens.
*   **Tampilan Data Mentah:** Fitur untuk melihat data tabular yang telah difilter untuk analisis lebih lanjut.

---

## 🛠️ Tech Stack yang Digunakan

Berikut adalah daftar tools, library, dan platform yang digunakan dalam pengembangan proyek ini:

*   **Bahasa Pemrograman:** Python
*   **Framework Aplikasi Web:** Streamlit
*   **Manipulasi Data:** Pandas
*   **Visualisasi Data:** Plotly Express
*   **AI Assistance (Development):** ChatGPT / Gemini digunakan untuk brainstorming, debugging, dan pembuatan dokumentasi.
*   **Version Control:** Git & GitHub
*   **Deployment:** Streamlit Community Cloud
*   **SDK (Potensi Pengembangan):** OpenAI SDK (untuk rencana pengembangan fitur analisis sentimen otomatis atau ringkasan insight berbasis AI).

---

## ⚙️ Cara Menjalankan Proyek Secara Lokal

Jika Anda ingin menjalankan aplikasi ini di komputer Anda sendiri, ikuti langkah-langkah berikut:

1.  **Clone Repositori**
    ```bash
    git clone https://github.com/[NAMA_USER_ANDA]/[NAMA_REPO_ANDA].git
    cd [NAMA_REPO_ANDA]
    ```

2.  **Buat dan Aktifkan Virtual Environment (Direkomendasikan)**
    ```bash
    # Untuk Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Untuk macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Pastikan Anda memiliki file `requirements.txt` di repositori Anda.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Aplikasi Streamlit**
    ```bash
    streamlit run app.py
    ```

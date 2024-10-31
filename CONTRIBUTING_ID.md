# *Contributing ID*

***Contributor***

Kami sangat senang anda telah ikut berkontribusi dalam project sederhana ini, kami memenerima perubahan apapun yang anda lakukan, 
baik itu kecil maupun besar. Tetapi anda harus memperhatikan peraturan dibawah ini:

- Semua hasil kerja kamu adalah buatan kamu sendiri dan tidak ada hak cipta dari orang lain. Berikan referensi jika mengambil dari orang lain.
- Hasil kerja kamu akan berlisensi [MIT](LICENSE) ketika *pull request* kamu sudah di-*merge*.
- Hasil kerja kamu wajib mengikuti standar dan *style* koding dari kami.
- Tidak diperkenankan untuk menggunakan *branch* `main` untuk *pull request*.


# *Pull Request*

***Pull request* yang baik**

- Lakukan fork pada repositori kami.
- Kemudian clone repository yang anda fork
    ```bash
    git clone https://github.com/<username>/<repository>.git
    ```
- install terlebih dahulu pre-commit
    ```bash
    pip install pre-commit # jika belum terinstall
    pre-commit install
    ```
- Buat branch baru, tidak disarankan untuk menggunakan branch default (default branch kami adalah `main`)
    ```bash
    git checkout -b <nama_branch_kamu>
    ```
- Lakukan perubahan yang anda inginkan
- Kemudian tambahkan perubahan dengan menggunakan `git add`
- Kemudian commit perubahan dengan menggunakan `git commit`
  ```bash
  git commit -m "feat: menambahkan fitur terbaru pada phantom"
  ```
  **Saran pesan commit**
  - `feat:` untuk menambah algoritma atau tambahan lainnya;
  - `fix:` untuk mengubah algoritma yang sudah ada atau memperbaiki;
  - `docs:` untuk mengubah atau membuat dokumentasi;
  - `add:` untuk menambah algoritma atau tambahan lainnya (opsional);

  Catatan: pesan commit harus menjelaskan perubahan secara singkat.

  Contoh yang benar:
   - &#9746; feat: test_x.py
   - &#9745; feat: menambahkan fitur terbaru pada phantom

  Lebih lengkapnya bisa dilihat di:
   - [EN](https://www.conventionalcommits.org/en/v1.0.0/)
   - [ID](https://www.conventionalcommits.org/id/v1.0.0/)

- kemudian push ke branch kamu
    ```bash
    git push origin <nama_branch_kamu>
    ```

Pull request akan di-*merge* jika:

- mengikuti standar dan arahan dari `CONTRIBUTING.md`;

**Tambahan**:

- Jika ada kendala atau masalah dalam *pull request*, kamu bisa laporkan masalahnya dalam [issue](https://github.com/dapuntech/phantom/issues).
- Jika ada tes yang tidak lewat atau gagal, kami akan cek kembali perubahan anda.

Untuk *pull request*, disarankan untuk menjelaskan secara detail yang kamu ubah atau tambahkan, dan bersikap sopan serta selalu berterima kasih. Itu salah satu bentuk tata krama yang baik terhadap sesama *contributor* dan *programmer* lainnya.

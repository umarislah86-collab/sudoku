# Ego Check — Sudoku Ekstrem

Game Sudoku berbahasa Melayu: 10 puzzle berbeza, jawapan tunggal, nota pensel, undo, semakan atas permintaan, butang hint usikan (tiada jawapan), jeda, timer dan progres localStorage. Responsif untuk telefon dan desktop. Tiada dependencies frontend, akaun, API, atau font luar.

## Jalankan

```sh
cd /workspace/sudoku
python3 -m http.server 3000 --bind 0.0.0.0
```

Buka melalui akses aplikasi yang disediakan oleh platform. Tiada build diperlukan. `puzzles.js` ialah data siap pakai; tidak perlu jana semula ketika startup.

## Puzzle

`generate.mjs` menjana grid lengkap, membuang petak hanya jika jawapan kekal tunggal, kemudian menapis puzzle yang tidak boleh diselesaikan dengan naked/hidden singles. Ambang carian solver ialah 5,000 nod dan sekurang-kurangnya 45 petak masih kosong selepas teknik singles. Bilangan nod ialah penapis kesukaran komputasi, bukan penarafan kesukaran manusia yang standard. Semua puzzle tahap sama; nombor cabaran bukan jaminan susunan kesukaran.

`python3 validate.py` menyemak semua 10 puzzle secara bebas. Penjanaan semula adalah pilihan dan boleh mengambil masa: `node generate.mjs`.

Progres hanya pada browser yang sama. Timer berhenti apabila tab tersembunyi, game dijeda atau dialog terbuka. Butang Hint memaparkan usikan bergilir dan merekodkan cubaan. Ia tidak mendedahkan nombor atau mengubah isi, nota, pemilihan petak atau sejarah undo.

## GitHub Pages

Workflow `.github/workflows/pages.yml` menerbitkan empat fail frontend sahaja pada push ke `main`. Selepas repo GitHub dibuat dan kod dipush, pilih **Settings → Pages → Source → GitHub Actions**. Jalankan workflow **Deploy Sudoku to GitHub Pages** jika perlu. URL sebenar boleh dilihat selepas deployment berjaya pada GitHub Actions; repo tempatan sahaja tidak bermakna laman sudah live.

Ujian browser tidak dijalankan secara automatik; pemilik akan menyemak UI secara manual.

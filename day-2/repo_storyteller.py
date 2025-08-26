import requests
from datetime import datetime
import pyfiglet

def get_repo_story(repo_url: str):
    parts = repo_url.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]
    api_url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(api_url, params={"per_page": 100})
    if response.status_code != 200:
        return f"❌ Gagal ambil data repo: {response.json().get('message', 'Unknown error')}"

    commits = response.json()
    if not commits:
        return "❌ Tidak ada commit ditemukan."

    first_commit = commits[-1]
    latest_commit = commits[0]

    first_date = datetime.strptime(first_commit["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")
    latest_date = datetime.strptime(latest_commit["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")

    authors = {}
    for c in commits:
        author = c["commit"]["author"]["name"]
        authors[author] = authors.get(author, 0) + 1
    top_author = max(authors, key=authors.get)

    banner = pyfiglet.figlet_format("Repo Storyteller")

    story = f"""{banner}
📖 Sebuah Perjalanan: {owner}/{repo}

🌱 Pada {first_date.strftime('%d %B %Y')}, lahirlah sebuah gagasan.
   {first_commit['commit']['author']['name']} menorehkan baris kode pertama,
   seperti seorang penulis yang menulis kata pembuka dalam sebuah buku.
   Dari sinilah cerita repository ini dimulai.

⏳ Waktu berjalan, commit demi commit hadir.
   Setiap perubahan adalah sebuah bab baru,
   penuh dengan ide, perbaikan, dan semangat untuk tumbuh.

⚡ Hingga akhirnya pada {latest_date.strftime('%d %B %Y')},
   tercatat sebuah commit terbaru yang berbicara lantang:
   → "{latest_commit['commit']['message']}"
   Seolah menjadi tanda bahwa perjalanan ini belum berakhir,
   melainkan sedang menuju ke arah yang lebih besar.

👑 Dari semua tokoh yang hadir dalam kisah ini,
   sosok paling gigih adalah {top_author},
   dengan {authors[top_author]} kontribusi berharga
   dari total {len(commits)} jejak langkah terakhir.

🚀 Maka, repository ini bukan hanya sekumpulan kode.
   Ia adalah saksi perjalanan, wujud ide yang hidup,
   dan bukti bahwa setiap developer meninggalkan cerita
   melalui baris demi baris yang mereka tuliskan.

✨ Dan seperti semua kisah hebat,
   {repo} masih terus menulis bab berikutnya...
"""

    return story


if __name__ == "__main__":
    url = input("Masukkan URL repo GitHub: ").strip()
    story = get_repo_story(url)
    print(story)

    with open("repo_story.txt", "w", encoding="utf-8") as f:
        f.write(story)

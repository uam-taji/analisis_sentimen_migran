
import json
import os

def save_to_json(data, filename):
    os.makedirs("data", exist_ok=True)
    with open(f"data/{filename}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    youtube_results = [
        {"komen": "warga asing makin ramai di KL", "sentimen": "Negatif", "skor": -0.5},
        {"komen": "tindakan imigresen minggu lepas bagus", "sentimen": "Positif", "skor": 0.3}
    ]
    twitter_results = [
        {"komen": "isu PATI perlu ditangani segera", "sentimen": "Negatif", "skor": -0.4},
        {"komen": "tindakan tegas sangat membantu", "sentimen": "Positif", "skor": 0.2}
    ]

    save_to_json(youtube_results, "youtube_komen")
    save_to_json(twitter_results, "twitter_komen")

if __name__ == "__main__":
    main()

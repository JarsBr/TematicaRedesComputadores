from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Caminhos dos arquivos
arquivo_https = "WebScraping/HTTPs/site_https.txt"
arquivo_http  = "WebScraping/HTTP/site_http.txt"

# Lista de stopwords em português (personalizável)
stopwords = set(STOPWORDS)
stopwords.update([
    "de", "da", "do", "em", "para", "e", "a", "o", "que", "com", 
    "por", "um", "uma", "é", "os", "as", "não", "se", "na", "no", "também", "à"
])

def gerar_wordcloud(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        texto = f.read().lower()
        wc = WordCloud(width=800, height=400, background_color="white",
                       stopwords=stopwords, colormap="viridis").generate(texto)
        return wc

# Gerar nuvens
wordcloud_https = gerar_wordcloud(arquivo_https)
wordcloud_http  = gerar_wordcloud(arquivo_http)

# Plotar lado a lado
plt.figure(figsize=(18, 8))

plt.subplot(1, 2, 1)
plt.imshow(wordcloud_https, interpolation="bilinear")
plt.axis("off")
plt.title("HTTPS", fontsize=18)

plt.subplot(1, 2, 2)
plt.imshow(wordcloud_http, interpolation="bilinear")
plt.axis("off")
plt.title("HTTP", fontsize=18)

plt.tight_layout()
plt.show()

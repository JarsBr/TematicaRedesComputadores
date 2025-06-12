import matplotlib.pyplot as plt
from collections import Counter
import re

# Função para processar texto e contar palavras
def contar_palavras(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        texto = f.read().lower()
        palavras = re.findall(r'\b\w+\b', texto)
        contador = Counter(palavras)
        return contador.most_common(10)  # top 10

# Caminhos dos arquivos
arquivo_https = "WebScraping/HTTPs/site_https.txt"
arquivo_http  = "WebScraping/HTTP/site_http.txt"

# Contagem de palavras
top_https = contar_palavras(arquivo_https)
top_http = contar_palavras(arquivo_http)

# Separar palavras e frequências
palavras_https, frequencias_https = zip(*top_https)
palavras_http,  frequencias_http  = zip(*top_http)

# Criar gráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle("Top 10 Palavras Mais Frequentes", fontsize=16)

# Gráfico HTTPS
ax1.barh(palavras_https, frequencias_https, color="steelblue")
ax1.set_title("HTTPS")
ax1.invert_yaxis()
ax1.set_xlabel("Frequência")

# Gráfico HTTP
ax2.barh(palavras_http, frequencias_http, color="darkorange")
ax2.set_title("HTTP")
ax2.invert_yaxis()
ax2.set_xlabel("Frequência")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
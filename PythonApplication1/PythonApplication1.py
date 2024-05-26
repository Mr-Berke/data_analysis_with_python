import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Rastgele say� olu�turma
nokta_sayisi = 500
x = np.random.randint(0, 1000, nokta_sayisi)
y = np.random.randint(0, 1000, nokta_sayisi)

# DataFrame'e kaydetme
cerceve = pd.DataFrame({"x": x, "y": y})

# Excel dosyas�na kaydetme
Excel_yolu = "kordinatlar.xlsx"
cerceve.to_excel(Excel_yolu, index=False)

# Excel dosyas�ndan okuma
cerceve = pd.read_excel(Excel_yolu)

# Koordinatlar� 200'l�k k�s�mlara b�lme
bolum_boyutu = 200
cerceve["bolum_x"] = (cerceve["x"] // bolum_boyutu) * bolum_boyutu
cerceve["bolum_y"] = (cerceve["y"] // bolum_boyutu) * bolum_boyutu

# B�l�mleri tek bir kimlik ile birle�tirme
cerceve["bolum_id"] = cerceve["bolum_x"] + cerceve["bolum_y"]

# B�l�mleri g�rselle�tirme
plt.figure(figsize=(10, 10))
farkli_bolum = cerceve[["bolum_x", "bolum_y", "bolum_id"]].drop_duplicates()
colors = plt.cm.jet(np.linspace(0, 1, len(farkli_bolum["bolum_id"].unique())))

for i, bolum_id in enumerate(farkli_bolum["bolum_id"].unique()):
    nokta_bolumleri = cerceve[cerceve["bolum_id"] == bolum_id]
    plt.scatter(nokta_bolumleri["x"], nokta_bolumleri["y"], color=colors[i])

plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Rastgele Nokta {bolum_boyutu}x{bolum_boyutu} Bolumler')
plt.legend()
plt.grid(True)
plt.savefig('kordinatlar_foto.jpeg')
plt.show()

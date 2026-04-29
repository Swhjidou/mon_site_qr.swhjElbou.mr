import qrcode

# L'adresse officielle de votre site sur GitHub
# C'est cette adresse qui est "encodée" dans le carré noir et blanc
mon_url = "https://swhjidou.github.io/mon_site_qr.swh1.mr/"

# Configuration du design du QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Ajout du lien
qr.add_data(mon_url)
qr.make(fit=True)

# Création de l'image (Noir sur fond Blanc)
img = qr.make_image(fill_color="black", back_color="white")

# Sauvegarde du fichier sur votre ordinateur
img.save("mon_qr_code.png")

print("--------------------------------------------------")
print("Succès ! Le fichier 'mon_qr_code.png' a été créé.")
print(f"Il pointe vers : {mon_url}")
print("--------------------------------------------------")
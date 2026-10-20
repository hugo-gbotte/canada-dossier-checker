# JOUR 4 - Vérificateur de Dossier Canada pour Hugo
print("=== Vérificateur Dossier Canada - Hugo ===")

# Liste de tes documents
documents = ["Passeport", "Diplôme BAC", "Relevés de notes", "Admission Sichuan", "IELTS"]

# On va vérifier ce que tu as déjà
dossier_complet = True

for doc in documents:
    reponse = input(f"As-tu {doc} ? (oui/non): ")
    
    if reponse == "oui":
        print(f"✅ {doc} OK")
    else:
        print(f"❌ Il manque {doc} - À FAIRE")
        dossier_complet = False

print("\n--- Résultat final ---")
if dossier_complet:
    print("🎉 Bravo Hugo ! Ton dossier est COMPLET pour WES Canada")
else:
    print("⚠️ Ton dossier est INCOMPLET. Il faut compléter les documents manquants.")
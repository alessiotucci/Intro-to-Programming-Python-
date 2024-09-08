import os
import re
import ast  # Modulo per valutare in sicurezza espressioni Python-like

# Funzione per cercare tutte le cartelle che iniziano con "Compito"
def find_verofalso_files(base_path):
    verofalso_files = []
    
    # Cerca in tutte le sottocartelle
    for root, dirs, files in os.walk(base_path):
        for dir_name in dirs:
            if re.match(r'Compito', dir_name):  # Regex per cercare le cartelle che iniziano con "Compito"
                compito_path = os.path.join(root, dir_name)
                for file in os.listdir(compito_path):
                    if file.startswith("VeroFalso"):  # Cerca il file VeroFalso
                        verofalso_files.append(os.path.join(compito_path, file))
    
    return verofalso_files

# Funzione per formattare il contenuto del file VeroFalso
def format_verofalso_content(verofalso_file, compito_name):
    with open(verofalso_file, 'r', encoding='utf-8') as file:
        data = file.read()

    try:
        # Usa ast.literal_eval per convertire in modo sicuro il contenuto in un dizionario
        verofalso_data = ast.literal_eval(data)
    except (SyntaxError, ValueError) as e:
        print(f"Errore nel parsing del file {verofalso_file}: {e}")
        return ""

    # Formatta il contenuto
    formatted_content = f"Compito: {compito_name}\n"
    for key, question in verofalso_data.items():
        premessa = question.get('premessa', '')
        domanda = question.get('domanda', '')
        risposta = question.get('ris', '?')
        
        formatted_content += f"{key}. {premessa}\n   {domanda}\n   Risposta: {risposta}\n\n"
    
    return formatted_content

# Funzione principale per gestire tutto il processo
def process_all_verofalso_files(base_path, output_file):
    verofalso_files = find_verofalso_files(base_path)
    
    with open(output_file, 'w', encoding='utf-8') as general_file:
        for verofalso_file in verofalso_files:
            compito_name = os.path.basename(os.path.dirname(verofalso_file))  # Prende il nome del compito
            formatted_content = format_verofalso_content(verofalso_file, compito_name)
            general_file.write(formatted_content + "\n")
    
    print(f"Domande formattate salvate in {output_file}")

# Esegui lo script
base_path = r"C:\Users\Aless\OneDrive\Desktop\ESAME programmazione python"  # Modifica con il percorso corretto
output_file = os.path.join(base_path, "domande_formattate.txt")

process_all_verofalso_files(base_path, output_file)

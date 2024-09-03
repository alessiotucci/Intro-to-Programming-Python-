
import re

def analizza_email(file):
    # 1) aprire il file di testo
    with open(file, 'r') as f:
        testo = f.read()
    
    # 2) creare una lista con tutti gli indirizzi email del file di testo
    pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    email_list = re.findall(pattern_email, testo)
    
    # 3) creare un dizionario con chiave i domini degli indirizzi email (nota bene, qui senza ripetizioni)
    domini = {}
    
    for email in email_list:
        partesinistra, dominio = email.split('@')
        
        # Verifica che la partesinistra non contenga sequenze vuote
        if '..' in partesinistra or partesinistra.startswith('.') or partesinistra.endswith('.'):
            continue
        
        # Conta il numero di sequenze nella partesinistra
        num_sequenze = len(partesinistra.split('.'))
        
        if dominio not in domini:
            domini[dominio] = [0, 0, 0]
        
        # 4) aggiornare i valori delle chiavi in base alla corretteza della parte sinistra della chiocciola dell'indirizzo email
        if num_sequenze == 1:
            domini[dominio][0] += 1
        elif num_sequenze == 2:
            domini[dominio][1] += 1
        else:
            domini[dominio][2] += 1
    
    return domini

# Esempio di utilizzo
file = 'email.txt'
risultato = analizza_email(file)
print(risultato)

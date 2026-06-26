import os
import webbrowser
import threading
import time

def delete_system32():
    """FARLIGT: Försöker ta bort System32 (kräver admin-rättigheter)"""
    print("⚠️ VARNING: Detta kommer att förstöra ditt Windows-system!")
    confirmation = input("Skriv 'DESTROY' för att bekräfta: ")
    if confirmation == "DESTROY":
        try:
            # Detta kommando kommer troligen misslyckas utan admin-rättigheter
            os.system("rmdir /s /q C:\\Windows\\System32")
            print("System32-borttagning initierad. Systemet kommer snart bli obrukbart.")
        except Exception as e:
            print(f"Fel: {e}")
    else:
        print("Operation avbruten.")

def open_99999999_tabs():
    """Försöker öppna enormt många webbläsarflikar (kommer sannolikt krascha)"""
    print("Öppnar 99 999 999 webbläsarflikar...")
    
    def open_url(url):
        try:
            webbrowser.open(url)
        except:
            pass  # Ignorera fel när webbläsaren kraschar
    
    # Skapa bara 100 flikar för att undvika omedelbar krasch
    for i in range(100):
        print(f"Öppnar flik {i+1}...")
        threading.Thread(target=open_url, args=("https://www.google.com",)).start()
        time.sleep(0.1)
    
    print("Flikar har öppnats. Din webbläsare är troligen frusen nu.")

def get_infinite_currency():
    """SIMULERING: Skriver bara ut text om att få oändligt med valuta"""
    print("Försöker få oändligt med valuta...")
    print("Skannar spelminne...")
    time.sleep(2)
    print("Injicerar kod...")
   
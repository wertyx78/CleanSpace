import tkinter as tk
import json
import os

CONFIG_FILE = "settings.json"

def save_settings(lang_code, theme_mode):
    """Uloží nastavení do JSON souboru."""
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"lang": lang_code, "theme": theme_mode}, f)
    except Exception as e:
        print(f"Chyba při ukládání: {e}")

def load_settings():
    """Načte nastavení ze souboru nebo vrátí výchozí."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {"lang": "cs", "theme": "dark"}

class Style:
    THEMES = {
        "dark": {
            "bg": "#0f172a", "sidebar": "#1e293b", "card": "#334155",
            "text": "#f8fafc", "text_dim": "#94a3b8", "accent": "#38bdf8",
            "accent_hover": "#7dd3fc", "btn": "#38bdf8", "danger": "#f43f5e",
            "success": "#22c55e", "entry_bg": "#1e293b"
        },
        "light": {
            "bg": "#f8fafc", "sidebar": "#f1f5f9", "card": "#ffffff",
            "text": "#0f172a", "text_dim": "#64748b", "accent": "#0284c7",
            "accent_hover": "#0369a1", "btn": "#0284c7", "danger": "#e11d48",
            "success": "#16a34a", "entry_bg": "#f1f5f9"
        }
    }

    def __init__(self):
        settings = load_settings()
        self.mode = settings.get("theme", "dark")
        self.current = self.THEMES[self.mode]
        self.FONT_TITLE = ("Segoe UI", 22, "bold")
        self.FONT_MAIN = ("Segoe UI", 10)
        self.FONT_LOG = ("Consolas", 10)
        self.MODERN_BTN = {"relief": "flat", "font": ("Segoe UI", 10, "bold"), "pady": 12, "padx": 25, "cursor": "hand2"}
        self.MODERN_ENTRY = {"relief": "flat", "font": ("Segoe UI", 11), "highlightthickness": 1}

    def toggle_theme(self):
        self.mode = "light" if self.mode == "dark" else "dark"
        self.current = self.THEMES[self.mode]

class LangManager:
    def __init__(self):
        settings = load_settings()
        self.current_lang = settings.get("lang", "cs")
        self.TEXTS = {
"cs": {
                "app_name": "PRO TOOL X",
                "theme_btn": "🌓 Vzhled",
                "lang_btn": "English",
                "exit": "Ukončit",
                "welcome": "Vítejte zpět",
                "desc": "Systém je připraven k práci.",
                "menu_dup": "🔍 Údržba",
                "menu_org": "📂 Třídič",
                "menu_net": "🌐 Síť",
                "menu_img": "🖼 Obrázky",
                "menu_clean": "🧹 Čištění",
                "menu_zip": "📦 Archivátor",
                "dup_title": "Údržba a Duplicity",
                "btn_dup": "Hledat duplicity",
                "btn_sys_clean": "Systémové čištění",
                "org_title": "Automatický třídič",
                "btn_select_org": "Vybrat složku a TŘÍDIT",
                "net_title": "Síťové testy",
                "btn_ping": "Test odezvy (Ping)",
                "btn_speed": "Rychlost internetu",
                "img_title": "Editor obrázků",
                "label_size": "Nová velikost (Š x V):",
                "btn_res_file": "Změnit jeden soubor",
                "btn_res_folder": "Změnit celou složku",
                "label_conv": "Konverze formátu:",
                "btn_conv_img": "Převést formát",
                "btn_conv_file": "Změnit příponu",
                "label_rename": "Hromadné přejmenování:",
                "btn_rename_folder": "Přejmenovat složku",
                "img_done": "Hotovo!",
                "clean_title": "Pokročilé čištění",
                "btn_trash": "Vysypat koš",
                "btn_old": "Hledat staré soubory",
                "archive_title": "Archivátor (ZIP)",
                "btn_zip": "Zabalit do ZIP",
                "btn_unzip": "Rozbalit ZIP"
            },
            "en": {
                "app_name": "PRO TOOL X",
                "theme_btn": "🌓 Theme",
                "lang_btn": "Čeština",
                "exit": "Quit",
                "welcome": "Welcome back",
                "desc": "System is ready to work.",
                "menu_dup": "🔍 Maintenance",
                "menu_org": "📂 Organizer",
                "menu_net": "🌐 Network",
                "menu_img": "🖼 Images",
                "menu_clean": "🧹 Cleanup",
                "menu_zip": "📦 Archiver",
                "dup_title": "Maintenance & Duplicates",
                "btn_dup": "Find duplicates",
                "btn_sys_clean": "System cleanup",
                "org_title": "Auto Organizer",
                "btn_select_org": "Select folder & ORGANIZE",
                "net_title": "Network Tests",
                "btn_ping": "Ping Test",
                "btn_speed": "Internet Speed",
                "img_title": "Image Editor",
                "label_size": "New size (W x H):",
                "btn_res_file": "Resize single file",
                "btn_res_folder": "Resize folder",
                "label_conv": "Format conversion:",
                "btn_conv_img": "Convert format",
                "btn_conv_file": "Change extension",
                "label_rename": "Bulk renaming:",
                "btn_rename_folder": "Rename folder",
                "img_done": "Done!",
                "clean_title": "Advanced Cleanup",
                "btn_trash": "Empty Bin",
                "btn_old": "Find old files",
                "archive_title": "Archiver (ZIP)",
                "btn_zip": "Pack to ZIP",
                "btn_unzip": "Extract ZIP"
            },
"fr": {
                "app_name": "PRO TOOL X",
                "theme_btn": "🌓 Thème",
                "lang_btn": "fr",
                "exit": "Quitter",
                "welcome": "Bienvenue",
                "desc": "Système prêt à l'emploi.",
                
                # Menu
                "menu_dup": "🔍 Maintenance",
                "menu_org": "📂 Organiseur",
                "menu_net": "🌐 Réseau",
                "menu_img": "🖼 Images",
                "menu_clean": "🧹 Nettoyage",
                "menu_zip": "📦 Archiveur",

                # Moduly
                "dup_title": "Maintenance & Doublons",
                "btn_dup": "Chercher doublons",
                "btn_sys_clean": "Nettoyage système",
                
                "org_title": "Organisateur Auto",
                "btn_select_org": "ORGANISER le dossier",
                
                "net_title": "Tests Réseau",
                "btn_ping": "Test de Ping",
                "btn_speed": "Vitesse Internet",
                
                "img_title": "Éditeur d'Images",
                "label_size": "Taille (L x H):",
                "btn_res_file": "Redimensionner",
                "btn_conv_img": "Convertir format",
                
                "clean_title": "Nettoyage Avancé",
                "btn_trash": "Vider la corbeille",
                "btn_old": "Fichiers anciens",
                
                "archive_title": "Archiveur (ZIP)",
                "btn_zip": "Compresser en ZIP",
                "btn_unzip": "Extraire le ZIP"
            },
 "es": {
                "app_name": "PRO TOOL X",
                "theme_btn": "🌓 Tema",
                "lang_btn": "es",
                "exit": "Salir",
                "welcome": "Bienvenido",
                "desc": "El sistema está listo.",
                
                # Menu
                "menu_dup": "🔍 Mantenimiento",
                "menu_org": "📂 Organizador",
                "menu_net": "🌐 Red",
                "menu_img": "🖼 Imágenes",
                "menu_clean": "🧹 Limpieza",
                "menu_zip": "📦 Archivador",

                # Módulos
                "dup_title": "Mantenimiento y Duplicados",
                "btn_dup": "Buscar duplicados",
                "btn_sys_clean": "Limpieza de sistema",
                
                "org_title": "Organizador Automático",
                "btn_select_org": "ORGANIZAR carpeta",
                
                "net_title": "Pruebas de Red",
                "btn_ping": "Prueba de Ping",
                "btn_speed": "Velocidad de Red",
                
                "img_title": "Editor de Imágenes",
                "label_size": "Tamaño (A x A):",
                "btn_res_file": "Redimensionar",
                "btn_conv_img": "Convertir formato",
                
                "clean_title": "Limpieza Avanzada",
                "btn_trash": "Vaciar papelera",
                "btn_old": "Archivos antiguos",
                
                "archive_title": "Archivador (ZIP)",
                "btn_zip": "Comprimir en ZIP",
                "btn_unzip": "Extraer ZIP"
            },
"de": {
                "app_name": "PRO TOOL X",
                "theme_btn": "🌓 Design",
                "lang_btn": "de",
                "exit": "Beenden",
                "welcome": "Willkommen",
                "desc": "Das System ist bereit.",
                
                # Menu
                "menu_dup": "🔍 Wartung",
                "menu_org": "📂 Organizer",
                "menu_net": "🌐 Netzwerk",
                "menu_img": "🖼 Bilder",
                "menu_clean": "🧹 Reinigung",
                "menu_zip": "📦 Archivierer",

                # Module
                "dup_title": "Wartung & Duplikate",
                "btn_dup": "Duplikate suchen",
                "btn_sys_clean": "Systemreinigung",
                
                "org_title": "Auto-Organizer",
                "btn_select_org": "Ordner SORTIEREN",
                
                "net_title": "Netzwerktests",
                "btn_ping": "Ping-Test",
                "btn_speed": "Internet-Tempo",
                
                "img_title": "Bildbearbeitung",
                "label_size": "Größe (B x H):",
                "btn_res_file": "Skalieren",
                "btn_conv_img": "Format ändern",
                
                "clean_title": "Erweiterte Reinigung",
                "btn_trash": "Papierkorb leeren",
                "btn_old": "Alte Dateien",
                
                "archive_title": "Archivierer (ZIP)",
                "btn_zip": "In ZIP packen",
                "btn_unzip": "ZIP entpacken"
            },
 "pl": {
                "app_name": "PRO TOOL X",
                "theme_btn": "🌓 Motyw",
                "lang_btn": "pl",
                "exit": "Wyjdź",
                "welcome": "Witaj",
                "desc": "System jest gotowy.",
                
                # Menu
                "menu_dup": "🔍 Konserwacja",
                "menu_org": "📂 Organizator",
                "menu_net": "🌐 Sieć",
                "menu_img": "🖼 Obrazy",
                "menu_clean": "🧹 Czyszczenie",
                "menu_zip": "📦 Archiwizator",

                # Moduły
                "dup_title": "Konserwacja i Duplikaty",
                "btn_dup": "Znajdź duplikaty",
                "btn_sys_clean": "Czyszczenie systemu",
                
                "org_title": "Auto Organizator",
                "btn_select_org": "ORGANIZUJ folder",
                
                "net_title": "Testy Sieci",
                "btn_ping": "Test Ping",
                "btn_speed": "Prędkość sieci",
                
                "img_title": "Edytor Obrazów",
                "label_size": "Rozmiar (S x W):",
                "btn_res_file": "Zmień rozmiar",
                "btn_conv_img": "Konwertuj format",
                
                "clean_title": "Zaawansowane Czyszczenie",
                "btn_trash": "Opróżnij kosz",
                "btn_old": "Stare pliki",
                
                "archive_title": "Archiwizator (ZIP)",
                "btn_zip": "Pakuj do ZIP",
                "btn_unzip": "Rozpakuj ZIP"
            }
        }

    def get(self, key):
        return self.TEXTS[self.current_lang].get(key, key)

# 2. TEPRVE POTÉ VYTVÁŘÍME INSTANCE (Tady byla ta chyba!)
style = Style()
lang = LangManager()
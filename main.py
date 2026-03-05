import tkinter as tk
# PŘIDÁNO: import save_settings z tvého configu
from config import style, lang, save_settings 

# Importy tvých modulů (Ujisti se, že soubory jsou ve složce modules/)
from modules.duplicate_finder import DuplicateFinder
from modules.file_organizer import FileOrganizer
from modules.network_tools import NetworkTools
from modules.image_tools import ImageTools
from modules.cleaner_pro import CleanerPro
from modules.archiver import Archiver

class MainApp:
    def __init__(self, root):
        self.root = root
        self.active_module_class = None
        self.setup_window()
        self.draw_interface()

    def setup_window(self):
        """Základní nastavení okna."""
        self.root.title(lang.get("app_name"))
        self.root.geometry("1100x750")
        self.root.minsize(1000, 700)

    def draw_interface(self):
        """Vykreslí celé UI. Volá se i při změně tématu/jazyka."""
        # Vymazat vše staré (pro refresh)
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg=style.current["bg"])

        # --- BOČNÍ PANEL (SIDEBAR) ---
        self.sidebar = tk.Frame(self.root, bg=style.current["sidebar"], width=260)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo / Název
        tk.Label(
            self.sidebar, text="⚡ " + lang.get("app_name"),
            fg=style.current["accent"], bg=style.current["sidebar"],
            font=("Segoe UI", 20, "bold"), pady=40
        ).pack()

        # Tlačítka menu
        menu_items = [
            ("menu_dup", DuplicateFinder),
            ("menu_org", FileOrganizer),
            ("menu_net", NetworkTools),
            ("menu_img", ImageTools),
            ("menu_clean", CleanerPro),
            ("menu_zip", Archiver)
        ]

        for key, m_class in menu_items:
            # lang.get(key) zajistí, že se název tlačítka načte v aktuálním jazyce
            self.create_menu_button(lang.get(key), m_class)

        # Tlačítko ukončit dole
        tk.Button(
            self.sidebar, text=lang.get("exit"), command=self.root.quit,
            bg=style.current["danger"], fg="white", relief="flat",
            font=("Segoe UI", 9, "bold"), pady=10
        ).pack(side="bottom", fill="x", padx=20, pady=20)

        # --- HLAVNÍ KONTEJNER ---
        self.main_area = tk.Frame(self.root, bg=style.current["bg"])
        self.main_area.pack(side="right", expand=True, fill="both")

        # Horní lišta (Settings)
        self.top_bar = tk.Frame(self.main_area, bg=style.current["bg"], height=60)
        self.top_bar.pack(side="top", fill="x", padx=20, pady=10)

        # --- ROZBALOVACÍ VÝBĚR JAZYKA ---
        self.languages = ["cs", "en", "fr", "es", "de", "pl"]
        self.lang_var = tk.StringVar(self.root)
        self.lang_var.set(lang.current_lang) 

        lang_menu = tk.OptionMenu(
            self.top_bar, 
            self.lang_var, 
            *self.languages, 
            command=self.change_lang_direct
        )
        
        lang_menu.config(
            bg=style.current["card"], 
            fg=style.current["accent"], 
            relief="flat", 
            font=("Segoe UI", 10, "bold"),
            highlightthickness=0,
            padx=15
        )
        lang_menu["menu"].config(
            bg=style.current["card"], 
            fg=style.current["text"],
            relief="flat"
        )
        lang_menu.pack(side="right", padx=5)

        # Tlačítko pro změnu tématu
        tk.Button(
            self.top_bar, text=lang.get("theme_btn"), command=self.toggle_theme,
            bg=style.current["card"], fg=style.current["text"], relief="flat", padx=15
        ).pack(side="right", padx=5)

        # Plochá karta pro obsah modulu
        self.content_card = tk.Frame(self.main_area, bg=style.current["card"], padx=30, pady=30)
        self.content_card.pack(expand=True, fill="both", padx=40, pady=(0, 40))

        # Refresh obsahu
        if self.active_module_class:
            self.load_module(self.active_module_class)
        else:
            self.show_welcome()

    def create_menu_button(self, text, m_class):
        """Vytvoří interaktivní tlačítko v menu."""
        btn = tk.Button(
            self.sidebar, text=text, command=lambda: self.load_module(m_class),
            bg=style.current["sidebar"], fg=style.current["text_dim"],
            relief="flat", font=("Segoe UI", 11), anchor="w", padx=30, pady=15,
            activebackground=style.current["accent"], cursor="hand2"
        )
        btn.pack(fill="x")
        
        # Hover efekty s použitím aktuálních barev z configu
        btn.bind("<Enter>", lambda e: btn.config(fg=style.current["text"]))
        btn.bind("<Leave>", lambda e: btn.config(fg=style.current["text_dim"]))

    def load_module(self, m_class):
        """Přepne obsah karty na vybraný modul."""
        self.active_module_class = m_class
        for widget in self.content_card.winfo_children():
            widget.destroy()
        
        # Spustí třídu modulu a předá jí content_card jako rodiče
        m_class(self.content_card)

    def show_welcome(self):
        """Úvodní obrazovka."""
        tk.Label(
            self.content_card, text=lang.get("welcome"),
            fg=style.current["text"], bg=style.current["card"],
            font=("Segoe UI", 26, "bold")
        ).pack(pady=(120, 10))
        
        tk.Label(
            self.content_card, text=lang.get("desc"),
            fg=style.current["text_dim"], bg=style.current["card"],
            font=("Segoe UI", 12)
        ).pack()

    def toggle_theme(self):
        """Změní téma a uloží nastavení."""
        style.toggle_theme()
        save_settings(lang.current_lang, style.mode)
        self.draw_interface()

    def change_lang_direct(self, selected_lang):
        """Změní jazyk a uloží nastavení."""
        lang.current_lang = selected_lang
        save_settings(lang.current_lang, style.mode)
        self.draw_interface()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
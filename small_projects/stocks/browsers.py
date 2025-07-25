import tkinter as tk
import webbrowser

def open_browser(url):
    webbrowser.open(url)

class BrowserApp:
    def __init__(self, master):
        self.master = master
        master.title("Browser App")

        self.label = tk.Label(master, text="Enter URL:")
        self.label.pack()

        self.url_entry = tk.Entry(master, width=40)
        self.url_entry.pack()

        self.open_button = tk.Button(master, text="Open Browser", command=self.open_browser)
        self.open_button.pack()

    def open_browser(self):
        url = self.url_entry.get()
        open_browser(url)

if __name__ == "__main__":
    root = tk.Tk()
    app = BrowserApp(root)
    root.mainloop()
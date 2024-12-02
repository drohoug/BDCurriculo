from tkinter import Tk, Label, Entry, Frame, Button
from tkinter import ttk
from PIL import Image, ImageTk
import os

root = Tk()

root.title("Prática Engenharia - Banco de Currículos")
root.geometry("600x400")  # tamanho da tela padrao
root.iconbitmap("C:/Users/Pedro/Downloads/praticasvg/favicon.ico")

main_frame = Frame(root)
main_frame.pack(padx=10, pady=10, fill="x")

# Caminho para o arquivo de imagem
image_path = "C:/Users/Pedro/Downloads/praticasvg/logo.png"

# Checar se o arquivo existe antes de tentar abrir
if os.path.exists(image_path):
    # Carregando a logo
    image = Image.open(image_path)  # Caminho da imagem
    logo = ImageTk.PhotoImage(image)

    # exibindo logo
    label = Label(main_frame, image=logo)
    label.pack(side="left", padx=5)
else:
    # Exibe uma mensagem se o arquivo não for encontrado
    label = Label(main_frame, text="Logo não encontrada.")
    label.pack(side="left", padx=5)

# Criando Input__
search_entry = Entry(main_frame, width=40)
search_entry.pack(side="left", padx=5)

# botão de busca
search_button = Button(main_frame, width=5, text=" Buscar ", command=lambda: buscar())
search_button.pack(side="left", padx=10, pady=20)


# Log de busca
def buscar():
    print("Buscar clicado! Texto da busca:", search_entry.get())


# tabela para os resultados
result_frame = Frame(root)
result_frame.pack(padx=10, pady=10, fill="both", expand=True)

tree = ttk.Treeview(result_frame, columns=("Nome", "Cidade", "Telefone", "E-mail"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Cidade", text="Cidade")
tree.heading("Telefone", text="Telefone")
tree.heading("E-mail", text="Email")

# Tamanhos das colunas
tree.column("Nome", width=150)
tree.column("Cidade", width=100)
tree.column("Telefone", width=120)
tree.column("E-mail", width=200)

tree.pack(fill="both", expand=True)

# dados de exemplo na tabela
example_data = (
    ("Ana Silva", "São Paulo", "123-456-789", "ana.silva@example.com"),
    ("Carlos Santos", "Rio de Janeiro", "987-654-321", "carlos.santos@example.com"),
)

for row in example_data:
    tree.insert("", "end", values=row)

root.mainloop()

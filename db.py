import sqlite3

conexao = sqlite3.connect('usuarios.db')

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

conexao.commit()

cursor.execute(
    "INSERT OR IGNORE INTO usuarios (nome, email) VALUES (?, ?)",
    ("Lucas", "Lucas@gmail")
)

conexao.commit()
conexao.close()

print("Banco de dados e tabela criados com sucesso!")

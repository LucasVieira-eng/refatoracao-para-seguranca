import sqlite3

def busca_usario_por_email(email_digitado):
    if "@" not in email_digitado:
        raise ValueError("Email inválido")

    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    query = "SELECT nome, email FROM usuarios WHERE email = ?"

    cursor.execute(query, (email_digitado,))

    return cursor.fetchone()

print(busca_usario_por_email("Lucas@gmail"))
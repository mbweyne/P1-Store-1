import streamlit as st

# Título e introdução
st.title("📊 Projeto 1 – Store 1")
st.write("Bem-vindo! Este app simula o tratamento de dados de clientes da Store 1.")

# Simulação do usuário
st.header("🧍 Dados do Usuário")

user_id = '32415'
user_name = ' mike_reed '
user_name = user_name.strip().replace('_', ' ')
user_age = 32

st.write(f"🧑 Usuário ID: {user_id}")
st.write(f"👤 Nome formatado: {user_name}")
st.write(f"🎂 Idade: {user_age}")

# Divisão de nome
name_split = user_name.split()
st.write("🔤 Nome dividido:", name_split)

# Lista de categorias favoritas
st.header("📦 Categorias favoritas")
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = [cat.lower() for cat in fav_categories]

st.write("Categorias originais:", fav_categories)
st.write("Categorias em minúsculas:", fav_categories_low)

# Gastos por categoria
st.header("💰 Gastos por categoria")
spendings_per_category = [894, 213, 173]
total = sum(spendings_per_category)
min_val = min(spendings_per_category)
max_val = max(spendings_per_category)

st.write(f"Total gasto: ${total}")
st.write(f"Gasto mínimo: ${min_val}")
st.write(f"Gasto máximo: ${max_val}")

# Simulação de novas compras
st.header("🛍️ Simulação de novas compras até atingir $1500")
from random import randint

total_amount_spent = 1280
target_amount = 1500
compras = []

while total_amount_spent < target_amount:
    nova = randint(30, 80)
    compras.append(nova)
    total_amount_spent += nova

st.write(f"Compras simuladas: {compras}")
st.write(f"Total final com compras: ${total_amount_spent}")

# Resumo final
st.header("📄 Resumo")
user_info = f"Usuário {user_id} chama-se {name_split[0]} e tem {user_age} anos."
st.success(user_info)

# Receita total da empresa
st.header("💼 Receita Total da Store 1")

users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'shoes'], [439, 390]],
]

revenue = sum([sum(user[4]) for user in users])
st.write(f"Receita total estimada: ${revenue}")

# Filtro por idade < 30
st.header("🧒 Clientes com menos de 30 anos")
for user in users:
    if user[2] < 30:
        st.write("👥", ' '.join(user[1]), "-", user[2], "anos")

# Clientes < 30 anos com gastos > 1000
st.header("💸 Jovens com gastos acima de $1000")
for user in users:
    if user[2] < 30 and sum(user[4]) > 1000:
        st.write("🔥", ' '.join(user[1]), "-", f"${sum(user[4])}")

# Clientes que compraram roupas
st.header("👗 Clientes que compraram 'clothes'")
for user in users:
    if 'clothes' in user[3]:
        st.write("🛍️", ' '.join(user[1]), "-", f"{user[2]} anos")
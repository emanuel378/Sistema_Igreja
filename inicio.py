import streamlit as st


st.title("Orações.com")

st.write("Feliz aniversario doida,aproveite o seu dia e se precisar de qualquer coisa e so pedir,fiz esse sistema pra quando vc quiser orar alguma oração. ")

st.write("Para tornar esse novo ano ainda mais especial, queremos te apresentar o Sistema de Oração [Orações.com], uma iniciativa que nasceu do desejo de fortalecer a conexão com Deus e entre as pessoas através da oração.")

st.write("""Este sistema é um espaço dedicado para:
Compartilhar pedidos de oração: Para que possamos interceder uns pelos outros.
Agradecer pelas bênçãos: Reconhecendo as maravilhas que Deus realiza em nossas vidas.
Reflexões e mensagens diárias: Para te inspirar e renovar sua fé todos os dias.""")

opções = ["As opções","Oração de agradecimento","Quando estiver triste","Oração por alguem"]

a = st.selectbox("Escolha",opções)

if a ==opções[1]:
    st.switch_page("pages/Agradecimento.py")
elif a ==opções[2]:
        st.switch_page("pages/Tristeza.py")
elif a ==opções[3]:
      st.switch_page('pages/Por_alguem.py')
st.sidebar.image("https://alexandrealeluia.com.br/wp-content/uploads/2023/10/Wallpaper-de-Nossa-Senhora-Aparecida-03-jpeg.webp")
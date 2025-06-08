import streamlit as st
import google.generativeai as genai


# Configuração da API Key e Modelo (conforme solicitado)
api_key = "AIzaSyCJgPa7Tl1QyhFgmZc9CsxU_TTYOq1pruA" 
genai.configure(api_key=api_key)

try:
    # Utilizando o modelo especificado
    model = genai.GenerativeModel("gemini-2.0-flash")
except Exception as e:
    st.error(f"Erro ao carregar o modelo Gemini 'gemini-2.0-flash': {e}")
    st.info("Verifique se o nome do modelo está correto e se sua chave API tem acesso a ele.")
    st.stop()

def gerar_resposta_gemini(prompt_completo):
    try:
        response = model.generate_content(prompt_completo)

        if response.parts:
            return response.text
        else:
            if response.prompt_feedback:
                st.warning(f"O prompt foi bloqueado. Razão: {response.prompt_feedback.block_reason}")
                if response.prompt_feedback.safety_ratings:
                    for rating in response.prompt_feedback.safety_ratings:
                        st.caption(f"Categoria: {rating.category}, Probabilidade: {rating.probability}")
            return "A IA não pôde gerar uma resposta para este prompt. Verifique as mensagens acima ou tente reformular seu pedido."
    except Exception as e:
        st.error(f"Erro ao gerar resposta da IA: {str(e)}")
        if hasattr(e, 'message'): # Tenta obter mais detalhes do erro da API do Gemini
            st.error(f"Detalhe da API Gemini: {e.message}")
        return None

# Título do aplicativo
st.title("Crie sua historia com o Gemini 📚")

# Inputs
personagem = st.text_input("Me conte o nome do nosso personagem principal")

genero = st.selectbox ("Qual o gênero da nossa historia?", 
                      ["Fantasia", "Ficção Cientifica", "Romance", "Suspense", "Aventura", "Terror"])

local = st.radio("Qual o local da nossa historia?", 
                 ["Castelo Antigo", "Floresta Assombrada", "Cidade Futurista", "Parque de Jogos", "Casa na Praia"])

frase = st.text_input("Frase de Efeito ou Desafio Inicial da nossa historia")

# Botão para gerar a resposta
if st.button("Gerar inico da nossa história"):
    if not personagem or not frase:
        st.warning("Por favor, preencha todos os campos.")
    else:
        prompt_historia = (
            f"Crie um historia com o seguinte personagem: {personagem}. \n"
            f"A historia deve ter o seguinte gênero: {genero},\n"
            f"e deve ter o seguinte local: {local}.\n "
            f"A historia deve ter como frase de efeito ou desafio inicial: {frase}. \n"
        )

        st.markdown("---")
        st.markdown("⚙️ **Prompt que será enviado para a IA (para fins de aprendizado):**")
        st.text_area("",prompt_historia, height=100)
        st.markdown("---")

        st.info("Aguarde, a IA está montando nossa historia...")
        resposta_ia = gerar_resposta_gemini(prompt_historia)

        if resposta_ia:
            st.markdown("### ✨ Sugestão de Historia:")
            st.markdown(resposta_ia)
        else:
            st.error("Não foi possível gerar o roteiro. Verifique as mensagens acima ou tente novamente mais tarde.")

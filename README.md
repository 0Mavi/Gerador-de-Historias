
# 📚 Gerador de Início de História com IA

Este aplicativo permite que o usuário crie o início de uma história literária com base em suas preferências. Ele utiliza o **Streamlit** para a interface e a **IA Gemini da Google** para gerar os textos com base em engenharia de prompt.

---

## 🚀 Acesse o App Online

👉 **[Clique aqui para usar o aplicativo no navegador]((https://gerador-de-historias-ia.streamlit.app/))**  


---

## 🧠 Objetivo

Permitir que alunos explorem como as escolhas do usuário moldam prompts de IA, e como esses prompts afetam a historia criada.

---

## 🖼️ Funcionalidades do App

O usuário informa:

1. **Nome do Protagonista**
2. **Gênero Literário**: Fantasia, Ficção Científica, Mistério, Aventura
3. **Local Inicial da História**: Uma floresta antiga, Uma cidade futurista, Um castelo assombrado, Uma nave espacial à deriva
4. **Frase de Efeito ou Desafio Inicial**: Texto livre

Ao clicar no botão **"Gerar Início da História"**, um prompt é enviado para a IA e o app exibe a história gerada.

---

## 💻 Como Executar Localmente

1. Clone ou baixe o repositório
2. Crie e ative o ambiente virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # No Windows
   source venv/bin/activate  # No Linux/macOS
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Substitua `"SUA_CHAVE_GEMINI"` no `app.py` pela sua chave de API Gemini:
   - Obtenha em: https://makersuite.google.com/app/apikey

5. Execute o aplicativo:

   ```bash
   streamlit run app.py
   ```

---

## 📄 Requisitos

- Python 3.9+
- streamlit
- google-generativeai



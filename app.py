
import streamlit as st
import streamlit.components.v1 as components
import base64

# Configuração da página
st.set_page_config(page_title="Para Iara ❤️", page_icon="❤️")

# Função para converter imagem em base64 (ajuda a não perder o link da foto)
def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Estilização Geral
st.markdown("""
    <style>
    .stApp { background-color: #fff5f5; }
    .message-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 18px;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

if 'aceitou' not in st.session_state:
    st.session_state.aceitou = False

if not st.session_state.aceitou:
    st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>❤️ Iara, você me desculpa? ❤️</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SIM! 😍", use_container_width=True):
            st.session_state.aceitou = True
            st.rerun()
            
    with col2:
        # O botão 'Não' que foge do mouse
        components.html("""
            <button id="no-btn" style="
                position: absolute; padding: 10px 20px; 
                background-color: #ff4b4b; color: white; 
                border: none; border-radius: 10px; cursor: pointer;
                font-weight: bold; transition: 0.1s;
            ">Não</button>
            <script>
                const btn = document.getElementById('no-btn');
                btn.addEventListener('mouseover', function() {
                    btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
                    btn.style.top = Math.random() * (window.innerHeight - 50) + 'px';
                });
            </script>
        """, height=200)

else:
    st.balloons()
    st.markdown("<h2 style='text-align: center;'>Eu te amo muito! ❤️</h2>", unsafe_allow_html=True)
    
    # Coloque o nome da imagem que você salvou no GitHub aqui
    # Exemplo: st.image("foto_iara.jpg")
    try:
        st.image("WhatsApp Image 2026-05-12 at 17.22.11.jpeg", use_container_width=True)
    except:
        st.info("Aqui aparecerá a nossa foto!")

    st.markdown("""
    <div class="message-box">
        Iara, me desculpa de verdade. Senti que você ficou chateada e, realmente, eu não estava bravo com você. 
        Sei que não foi o melhor jeito de fazer uma crítica; acabo me frustrando quando as coisas dão errado 
        e desconto em você, que não tem nada a ver com a situação. <br><br>
        Não gosto de te ver triste. Além de sentir o seu desânimo, vi no seu rosto a falta do seu sorriso, 
        e isso me incomoda muito. Temos que melhorar e não ficar apenas emburrados um com o outro. 
        Concordo com você: precisamos evoluir nesse ponto, e vamos fazer isso juntos, porque te amo 
        demais e quero ver apenas esse sorriso lindo no seu rosto.
    </div>
    """, unsafe_allow_html=True)

import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(
    page_title="Para Iara ❤️", 
    page_icon="❤️", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# Estilização CSS personalizada
st.markdown("""
    <style>
    /* Fundo e Fonte */
    .stApp {
        background: linear-gradient(180deg, #fff5f5 0%, #ffe3e3 100%);
    }
    
    /* Ajuste de visibilidade da primeira tela */
    .main-container {
        padding-top: 50px;
        text-align: center;
    }

    /* Caixa de mensagem */
    .message-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #ff4b4b;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.05);
        text-align: center;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #444;
        margin-top: 20px;
    }

    /* Título */
    .main-title {
        color: #ff4b4b;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-weight: bold;
        padding: 40px 10px;
        font-size: 2.5rem;
    }

    /* Animação de Corações Subindo */
    @keyframes hearts {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }
    .heart {
        position: fixed;
        bottom: -10px;
        color: #ff4b4b;
        font-size: 20px;
        user-select: none;
        z-index: 1000;
        animation: hearts 4s linear infinite;
    }
    </style>
    """, unsafe_allow_html=True)

if 'aceitou' not in st.session_state:
    st.session_state.aceitou = False

if not st.session_state.aceitou:
    # Container para melhorar a visualização inicial
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>❤️ Iara, você me desculpa? ❤️</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SIM! 😍", use_container_width=True):
            st.session_state.aceitou = True
            st.rerun()
            
    with col2:
        components.html("""
            <div id="area" style="width: 100%; height: 250px; position: relative; display: flex; justify-content: center; align-items: flex-start;">
                <button id="no-btn" style="
                    position: absolute; 
                    padding: 12px 0; 
                    width: 90%;
                    max-width: 150px;
                    background-color: #ff4b4b; 
                    color: white; 
                    border: none; 
                    border-radius: 8px; 
                    cursor: pointer;
                    font-weight: bold; 
                    font-size: 16px;
                    box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
                    transition: 0.2s;
                    touch-action: none;
                ">Não</button>
            </div>
            <script>
                const btn = document.getElementById('no-btn');
                const area = document.getElementById('area');
                
                function moveButton() {
                    const maxX = area.clientWidth - btn.clientWidth;
                    const maxY = area.clientHeight - btn.clientHeight;
                    const newX = Math.random() * maxX;
                    const newY = Math.random() * maxY;
                    btn.style.left = newX + 'px';
                    btn.style.top = newY + 'px';
                }

                btn.addEventListener('mouseover', moveButton);
                btn.addEventListener('touchstart', function(e) {
                    e.preventDefault();
                    moveButton();
                });
            </script>
        """, height=300)
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # Efeito de Neve (o mais próximo de corações caindo nativo)
    st.snow()
    
    # Injeção de Corações subindo via HTML
    heart_html = "".join([f'<div class="heart" style="left: {i*10}%; animation-delay: {i*0.5}s;">❤️</div>' for i in range(10)])
    st.markdown(heart_html, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>Eu te amo muito! ❤️</h2>", unsafe_allow_html=True)
    
    try:
        st.image("WhatsApp Image 2026-05-12 at 17.22.11.jpeg", use_container_width=True)
    except:
        st.info("Aqui aparecerá a nossa foto!")

    st.markdown("""
    <div class="message-box">
        <b>Iara, me desculpa de verdade.</b><br><br>
        Senti que você ficou chateada e, realmente, eu não estava bravo com você. <br>
        Sei que não foi o melhor jeito de fazer uma crítica; acabo me frustrando quando as coisas dão errado 
        e desconto em você, que não tem nada a ver com a situação. <br><br>
        Não gosto de te ver triste. Além de sentir o seu desânimo, vi no seu rosto a falta do seu sorriso, 
        e isso me incomoda muito. Temos que melhorar e não ficar apenas emburrados um com o outro. <br><br>
        <b>Concordo com você:</b> precisamos evoluir nesse ponto, e vamos fazer isso juntos, porque te amo 
        demais e quero ver apenas esse sorriso lindo no seu rosto.
    </div>
    """, unsafe_allow_html=True)

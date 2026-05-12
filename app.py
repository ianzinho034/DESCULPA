import streamlit as st
import streamlit.components.v1 as components

# Configuração da página - Essencial para Mobile
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

    /* Ajuste para o container dos botões no mobile */
    div[data-testid="column"] {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    /* Título */
    .main-title {
        color: #ff4b4b;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-weight: bold;
        padding: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

if 'aceitou' not in st.session_state:
    st.session_state.aceitou = False

if not st.session_state.aceitou:
    st.markdown("<h1 class='main-title'>❤️ Iara, você me desculpa? ❤️</h1>", unsafe_allow_html=True)
    
    # Criando colunas para os botões ficarem lado a lado
    col1, col2 = st.columns(2)
    
    with col1:
        # Botão SIM oficial do Streamlit (Estilizado automaticamente)
        if st.button("SIM! 😍", use_container_width=True):
            st.session_state.aceitou = True
            st.rerun()
            
    with col2:
        # Botão NÃO que foge (HTML/JS)
        # Altura de 300px para dar espaço para a "fuga" no celular
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
                    // Limita a fuga para dentro da área visível da coluna
                    const maxX = area.clientWidth - btn.clientWidth;
                    const maxY = area.clientHeight - btn.clientHeight;
                    
                    const newX = Math.random() * maxX;
                    const newY = Math.random() * maxY;
                    
                    btn.style.left = newX + 'px';
                    btn.style.top = newY + 'px';
                }

                btn.addEventListener('mouseover', moveButton);
                btn.addEventListener('touchstart', function(e) {
                    e.preventDefault(); // Impede o clique no celular
                    moveButton();
                });
            </script>
        """, height=300)

else:
    # Tela de Sucesso
    st.balloons()
    st.markdown("<h2 style='text-align: center; color: #ff4b4b;'>Eu te amo muito! ❤️</h2>", unsafe_allow_html=True)
    
    # Centralização da imagem
    try:
        st.image("WhatsApp Image 2026-05-12 at 17.22.11.jpeg", use_container_width=True)
    except:
        st.info("Aqui aparecerá a nossa foto!")

    st.markdown("""
    <div class="message-box">
        <b>Iara, me desculpa de verdade.</b><br><br>
        Senti que você ficou chateada e, realmente, eu não estava bravo com você. 
        Sei que não foi o melhor jeito de fazer uma crítica; acabo me frustrando quando as coisas dão errado 
        e desconto em você, que não tem nada a ver com a situação. <br><br>
        Não gosto de te ver triste. Além de sentir o seu desânimo, vi no seu rosto a falta do seu sorriso, 
        e isso me incomoda muito. Temos que melhorar e não ficar apenas emburrados um com o outro. <br><br>
        <b>Concordo com você:</b> precisamos evoluir nesse ponto, e vamos fazer isso juntos, porque te amo 
        demais e quero ver apenas esse sorriso lindo no seu rosto.
    </div>
    """, unsafe_allow_html=True)

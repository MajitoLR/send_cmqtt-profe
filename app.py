# ------------------ ESTILO ROSADO ------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #FAD1E6, #F3B6D4);
    font-family: 'Segoe UI', sans-serif;
}

/* Espacio arriba */
.block-container {
    padding-top: 4rem;
}

/* ❌ ELIMINA EL BLOQUE BLANCO */
h1 + div {
    display: none;
}

/* Título */
h1 {
    text-align: center;
    color: #7A2E5E;
    font-weight: 800;
    margin-bottom: 25px;
}

/* Tarjeta */
.card {
    background: white;
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 10px 25px rgba(214, 51, 132, 0.25);
    max-width: 500px;
    margin: auto;
    text-align: center;
}

/* Subbloques */
.block {
    background: #FCE4F1;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 15px;
    color: #5A2A4D;
    font-size: 14px;
}

/* Botones */
.stButton>button {
    background: #F472B6;
    color: white;
    border-radius: 15px;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton>button:hover {
    background: #EC4899;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

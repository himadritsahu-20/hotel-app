import streamlit as st

st.set_page_config(
    page_title="H&H Luxury Hotels India",
    page_icon="🏨",
    layout="wide"
)

# --- HOME PAGE CSS ---
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #ffd700, #ffed4e);
        padding: 3rem;
        border-radius: 25px;
        text-align: center;
        color: #1a1a1a;
        margin-bottom: 3rem;
        box-shadow: 0 20px 50px rgba(255,215,0,0.3);
    }
    .explore-btn {
        background: linear-gradient(135deg, #5f259f, #7b33cc) !important;
        color: white !important;
        border-radius: 35px !important;
        padding: 25px 60px !important;
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        box-shadow: 0 20px 50px rgba(95,37,159,0.5) !important;
        border: none !important;
        width: 100% !important;
        height: 90px !important;
        margin: 2rem 0 !important;
    }
    .explore-btn:hover {
        transform: translateY(-8px) !important;
        box-shadow: 0 30px 60px rgba(95,37,159,0.7) !important;
    }
    .feature-card {
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 15px 40px rgba(0,0,0,0.1);
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

# HOME PAGE CONTENT
st.markdown("<div class='main-header'><h1>👑 H&H Luxury Hotels India</h1><p>20 Premium Properties | 10 Exquisite Regions</p></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h2 style="color: #5f259f; margin-bottom: 1rem;">🏨 20 Luxury Hotels</h2>
        <p style="font-size: 1.3rem; color: #666;">Handpicked 5⭐ properties</p>
        <ul style="text-align: left; font-size: 1.1rem; color: #444; margin-top: 1rem;">
            <li>📍 10 Regions</li>
            <li>⭐ All 5-Star</li>
            <li>💰 ₹5K - ₹32K/night</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=800&q=80", use_column_width=True)

st.markdown("---")

# BIG EXPLORE BUTTON
col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("<h2 style='color: #5f259f; text-align: center;'>Start Your Journey</h2>", unsafe_allow_html=True)
with col2:
    st.markdown('<button class="explore-btn">🚀 Explore Luxury Properties</button>', unsafe_allow_html=True)
    st.caption("👈 Click sidebar or button above to explore hotels")

st.markdown("### 📞 Get In Touch")
col1, col2, col3 = st.columns(3)
with col1: 
    st.info("**support@hhluxury.com**")
with col2: 
    st.info("**+91 98765 43210**")
with col3: 
    st.info("**24/7 Luxury Support**")

import streamlit as st
from hotels_data import df

# Initialize Session State FIRST
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

st.set_page_config(
    page_title="H&H Luxury Hotels India",
    page_icon="🏨",
    layout="wide"
)

# --- CSS ---
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
    }
    .explore-btn:hover {
        transform: translateY(-8px) !important;
        box-shadow: 0 30px 60px rgba(95,37,159,0.7) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION FUNCTIONS ---
def go_to_home():
    st.session_state.current_page = "home"
    st.rerun()

def go_to_hotels():
    st.session_state.current_page = "hotels"
    st.switch_page("pages/1_Hotels.py")

def go_to_booking():
    st.session_state.current_page = "booking"
    st.switch_page("pages/2_Booking.py")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🏨 H&H Navigation")
    selected_page = st.radio(
        "Go to:",
        ["🏠 Home", "🏨 Hotels", "💳 Booking"],
        key="sidebar_nav",
        index=0 if st.session_state.current_page == "home" else 
              1 if st.session_state.current_page == "hotels" else 2
    )
    
    if selected_page == "🏠 Home":
        if st.button("🏠 Go Home", key="sidebar_home"):
            go_to_home()
    elif selected_page == "🏨 Hotels":
        if st.button("🏨 Browse Hotels", key="sidebar_hotels"):
            go_to_hotels()
    elif selected_page == "💳 Booking":
        if st.button("💳 Book Now", key="sidebar_booking"):
            go_to_booking()

# --- SIMPLIFIED HOME PAGE CONTENT ---
if st.session_state.current_page == "home":
    # MAIN HEADER
    st.markdown("<div class='main-header'><h1>👑 H&H Luxury Hotels India</h1><p>20 Premium Properties | 10 Exquisite Regions</p></div>", unsafe_allow_html=True)
    
    # FULL WIDTH IMAGE
    st.image("https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1400&q=80", use_container_width=True)
    
    # BIG EXPLORE BUTTON (Centered)
    st.markdown("---")
    st.markdown("<div style='text-align: center; margin: 4rem 0;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #5f259f;'>Ready to Discover Luxury?</h2>", unsafe_allow_html=True)
    
    if st.button("🚀 Explore Luxury Properties", key="main_explore_btn", on_click=go_to_hotels, use_container_width=True):
        st.success("🎉 Redirecting to Hotels...", icon="🚀")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # CONTACT INFO (Bottom)
    st.markdown("---")
    st.markdown("<h3 style='text-align: center; color: #5f259f;'>📞 Get In Touch</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: 
        st.info("**support@hhluxury.com**")
    with col2: 
        st.info("**+91 98765 43210**")
    with col3: 
        st.info("**24/7 Luxury Support**")

elif st.session_state.current_page == "hotels":
    st.switch_page("pages/1_Hotels.py")

elif st.session_state.current_page == "booking":
    st.switch_page("pages/2_Booking.py")

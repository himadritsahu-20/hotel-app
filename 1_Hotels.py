import streamlit as st
from hotels_data import df

# Set session state for hotels page
if 'current_page' not in st.session_state:
    st.session_state.current_page = "hotels"

st.set_page_config(page_title="Hotels | H&H Luxury", layout="wide")

# DARK THEME CSS (Same as before)
st.markdown("""
<style>
    /* [Same dark theme CSS as previous version] */
    [data-testid="stAppViewContainer"] { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%) !important; color: white !important; }
    h1, h2, h3 { color: #ffd700 !important; text-shadow: 2px 2px 8px rgba(255,215,0,0.5) !important; }
    .filter-box { background: rgba(26,26,46,0.95) !important; border: 3px solid #ffd700 !important; border-radius: 25px !important; padding: 2.5rem !important; }
    .hotel-card { background: rgba(255,255,255,0.95) !important; border-radius: 20px !important; border: 2px solid #ffd700 !important; }
    .stButton > button { background: linear-gradient(135deg, #ffd700, #ffed4e) !important; color: #1a1a2e !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🔍 Find Your Perfect Stay</h1>", unsafe_allow_html=True)
st.info(f"📊 **{len(df['region'].unique())} Regions | {len(df)} Luxury Hotels**")

# FILTERS (Same as before)
col1, col2, col3 = st.columns(3)
# ... [filters code same as previous] ...

# HOTEL GRID (Same as before)
# ... [hotel grid code same as previous] ...

# FIXED NAVIGATION BUTTONS
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_page = "home"
        st.switch_page("app.py")
with col2:
    if st.button("💳 Book Now", use_container_width=True):
        st.session_state.current_page = "booking"
        st.switch_page("pages/2_Booking.py")
with col3:
    st.empty()

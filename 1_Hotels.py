import streamlit as st
from hotels_data import df
import pandas as pd

# Initialize Session State (CRITICAL)
if 'current_page' not in st.session_state:
    st.session_state.current_page = "hotels"

st.set_page_config(
    page_title="Hotels | H&H Luxury Hotels",
    page_icon="🏨",
    layout="wide"
)

# --- DARK THEME CSS (Premium Golden Accents) ---
st.markdown("""
<style>
    /* Dark Luxury Theme */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%) !important;
        color: white !important;
    }
    
    /* Golden Headings */
    h1 { 
        color: #ffd700 !important; 
        text-shadow: 3px 3px 12px rgba(255,215,0,0.6) !important; 
        font-size: 3rem !important; 
        font-weight: 800 !important;
    }
    h2 { 
        color: #ffd700 !important; 
        text-shadow: 2px 2px 8px rgba(255,215,0,0.5) !important; 
        font-size: 2rem !important;
    }
    
    /* Filter Boxes - Dark with Golden Glow */
    .filter-box {
        background: rgba(26,26,46,0.95) !important;
        border: 4px solid #ffd700 !important;
        border-radius: 30px !important;
        padding: 3rem !important;
        margin: 2rem 0 !important;
        backdrop-filter: blur(20px) !important;
        box-shadow: 0 25px 60px rgba(255,215,0,0.2), 0 0 40px rgba(255,215,0,0.1) !important;
    }
    
    /* Hotel Cards - White with Golden Border */
    .hotel-card {
        background: rgba(255,255,255,0.97) !important;
        border-radius: 25px !important;
        padding: 2rem !important;
        margin: 1.5rem 0 !important;
        border: 3px solid #ffd700 !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 15px 40px rgba(0,0,0,0.3) !important;
    }
    
    .hotel-card:hover {
        transform: translateY(-10px) rotate(1deg) !important;
        box-shadow: 0 30px 70px rgba(255,215,0,0.4), 0 0 50px rgba(255,215,0,0.2) !important;
        border-color: #ffed4e !important;
    }
    
    /* Golden Text */
    .golden-text {
        color: #ffd700 !important;
        font-weight: 700 !important;
        text-shadow: 1px 1px 4px rgba(255,215,0,0.5) !important;
    }
    
    /* Slider */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #ffd700, #ffed4e, #ff6b35) !important;
    }
    
    /* Multiselect */
    .stMultiSelect > label {
        color: #ffd700 !important;
        font-weight: 800 !important;
        font-size: 1.4rem !important;
    }
    
    /* Navigation Buttons */
    .nav-btn {
        background: linear-gradient(135deg, #ffd700, #ffed4e) !important;
        color: #1a1a2e !important;
        border-radius: 25px !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 15px 35px rgba(255,215,0,0.5) !important;
        height: 55px !important;
    }
    
    /* Info Box */
    .stInfo {
        background: rgba(255,215,0,0.15) !important;
        border-left: 6px solid #ffd700 !important;
        border-radius: 20px !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION FUNCTIONS ---
def go_to_home():
    st.session_state.current_page = "home"
    st.switch_page("app.py")

def go_to_booking():
    st.session_state.current_page = "booking"
    st.switch_page("pages/2_Booking.py")

# --- MAIN HEADER ---
st.markdown("""
<div style="background: linear-gradient(135deg, rgba(26,26,46,0.95), rgba(22,33,62,0.95)); 
            padding: 3rem; border-radius: 30px; margin-bottom: 3rem; 
            border: 3px solid #ffd700; text-align: center;">
    <h1>🔍 Discover Luxury Hotels</h1>
    <p style="font-size: 1.3rem; color: #ffd700;">20 Premium Properties | 10 Exquisite Regions</p>
</div>
""", unsafe_allow_html=True)

# --- ADVANCED FILTERS ---
st.markdown("<h2>🎛️ Refine Your Search</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="filter-box">', unsafe_allow_html=True)
    st.markdown("<h3 class='golden-text'>🌍 Destination</h3>", unsafe_allow_html=True)
    selected_regions = st.multiselect(
        "Select regions",
        options=sorted(df['region'].unique()),
        default=sorted(df['region'].unique())[:3],
        format_func=lambda x: f"📍 {x}"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="filter-box">', unsafe_allow_html=True)
    st.markdown("<h3 class='golden-text'>💰 Budget</h3>", unsafe_allow_html=True)
    min_price, max_price = st.slider(
        "Price per night (₹)",
        3000, 35000, (5000, 25000), 500,
        help="Drag to set your luxury budget"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="filter-box">', unsafe_allow_html=True)
    st.markdown("<h3 class='golden-text'>✨ Amenities</h3>", unsafe_allow_html=True)
    amenities = st.multiselect(
        "Featured facilities",
        options=["🏊 Infinity Pool", "🧖 Spa & Wellness", "🏖️ Beach Access", "⛰️ Mountain View", "🏰 Heritage", "🚤 Lakefront"],
        default=["🏊 Infinity Pool", "🧖 Spa & Wellness"],
        max_selections=3
    )
    st.markdown('</div>', unsafe_allow_html=True)

# --- FILTER & RESULTS ---
filtered_df = df[
    (df['region'].isin(selected_regions)) &
    (df['price'].between(min_price, max_price))
]

st.markdown(f"<h2>{len(filtered_df)} Luxury Gems Found ✨</h2>", unsafe_allow_html=True)

if len(filtered_df) > 0:
    # RESPONSIVE 3-COLUMN GRID
    cols = st.columns(3)
    for idx, hotel in enumerate(filtered_df.itertuples()):
        col_idx = idx % 3
        with cols[col_idx]:
            st.markdown(f"""
            <div class="hotel-card">
                <div style="height: 200px; 
                            background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('{hotel.amenity_img}'); 
                            background-size: cover; background-position: center; 
                            border-radius: 20px; margin-bottom: 1.5rem;"></div>
                
                <h4 class="golden-text" style="margin: 0 0 0.5rem 0; font-size: 1.3rem;">
                    {hotel.name}
                </h4>
                
                <p style="color: #666; margin: 0.3rem 0; font-size: 1rem;">
                    📍 {hotel.region}
                </p>
                
                <div style="font-size: 1.8rem; color: #ffd700; font-weight: 900; margin: 1rem 0;">
                    ₹{hotel.price:,}
                    <span style="font-size: 1rem; font-weight: 500;">/night</span>
                </div>
                
                <div style="color: #5f259f; font-size: 1rem; font-weight: 600; 
                            background: rgba(95,37,159,0.1); padding: 0.8rem; 
                            border-radius: 15px; text-align: center;">
                    ✨ {hotel.amenity_name}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # STATS BELOW GRID
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🔍 Showing", f"{len(filtered_df)}/{len(df)}")
    with col2:
        st.metric("💰 Avg Price", f"₹{filtered_df['price'].mean():,.0f}")
    with col3:
        st.metric("📊 Regions", len(filtered_df['region'].unique()))

else:
    st.markdown("""
    <div style="text-align: center; padding: 4rem; background: rgba(255,215,0,0.1); 
                border-radius: 25px; border: 2px dashed #ffd700; color: #ffd700;">
        <h2>🔍 No Matches Found</h2>
        <p style="font-size: 1.2rem;">Try adjusting your filters above</p>
        <div style="font-size: 4rem; margin: 2rem 0;">✨</div>
    </div>
    """, unsafe_allow_html=True)

# --- PERFECT NAVIGATION BAR ---
st.markdown("---")
st.markdown("""
<div style="background: rgba(26,26,46,0.9); padding: 2.5rem; 
            border-radius: 30px; border: 3px solid #ffd700; text-align: center;">
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🏠 Home", key="nav_home_hotels", on_click=go_to_home, use_container_width=True):
        st.success("🏠 Going home...", icon="🏠")

with col2:
    if st.button("💳 Book Selected", key="nav_booking_hotels", on_click=go_to_booking, use_container_width=True):
        st.success("💳 Redirecting to booking...", icon="💳")

with col3:
    if st.button("🔄 Clear Filters", key="nav_clear_hotels", use_container_width=True):
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# --- QUICK STATS ---
st.markdown(f"""
<div style="background: rgba(255,215,0,0.1); padding: 2rem; border-radius: 20px; 
            border-left: 6px solid #ffd700; margin-top: 3rem;">
    <h3 class="golden-text">📊 Collection Overview</h3>
    <p><strong>{len(df)}</strong> hotels across <strong>{len(df['region'].unique())}</strong> regions | 
    Price range: ₹{df['price'].min():,} - ₹{df['price'].max():,}</p>
</div>
""", unsafe_allow_html=True)

import streamlit as st
from hotels_data import df

st.set_page_config(page_title="Hotels | H&H Luxury", layout="wide")

# DARK THEME CSS
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%) !important;
        color: white !important;
    }
    h1, h2, h3 { color: #ffd700 !important; text-shadow: 2px 2px 8px rgba(255,215,0,0.5) !important; }
    .filter-box { 
        background: rgba(26,26,46,0.95) !important; 
        border: 3px solid #ffd700 !important; 
        border-radius: 25px !important; 
        padding: 2.5rem !important; 
        margin: 1.5rem 0 !important; 
        box-shadow: 0 20px 40px rgba(0,0,0,0.5) !important;
    }
    .hotel-card {
        background: rgba(255,255,255,0.95) !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        border: 2px solid #ffd700 !important;
        transition: transform 0.3s ease !important;
    }
    .hotel-card:hover { transform: translateY(-5px) !important; box-shadow: 0 20px 40px rgba(255,215,0,0.3) !important; }
    .stSlider > div > div > div { background: linear-gradient(90deg, #ffd700, #ffed4e) !important; }
    .stMultiSelect > label { color: #ffd700 !important; font-weight: 800 !important; font-size: 1.3rem !important; }
    .stButton > button { 
        background: linear-gradient(135deg, #ffd700, #ffed4e) !important; 
        color: #1a1a2e !important; 
        font-weight: 800 !important; 
        box-shadow: 0 15px 35px rgba(255,215,0,0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🔍 Find Your Perfect Stay</h1>", unsafe_allow_html=True)
st.info(f"📊 **{len(df['region'].unique())} Regions | {len(df)} Luxury Hotels**")

# FILTERS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="filter-box">', unsafe_allow_html=True)
    st.markdown("<h3>🌍 Select Region</h3>", unsafe_allow_html=True)
    selected_regions = st.multiselect("Choose destinations", list(df['region'].unique()), default=list(df['region'].unique())[:3])
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="filter-box">', unsafe_allow_html=True)
    st.markdown("<h3>💰 Price Range</h3>", unsafe_allow_html=True)
    min_price, max_price = st.slider("₹ Per Night", 3000, 35000, (5000, 20000), 1000)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="filter-box">', unsafe_allow_html=True)
    st.markdown("<h3>✨ Amenities</h3>", unsafe_allow_html=True)
    amenities = st.multiselect("Features", ["🏊 Pool", "🧖 Spa", "🏖️ Beach", "⛰️ Mountain", "🏰 Heritage"])
    st.markdown('</div>', unsafe_allow_html=True)

# FILTER RESULTS
filtered_df = df[(df['region'].isin(selected_regions)) & (df['price'].between(min_price, max_price))]
st.markdown(f"<h2>🏨 {len(filtered_df)} Properties Found</h2>", unsafe_allow_html=True)

if len(filtered_df) > 0:
    cols = st.columns(3)
    for idx, hotel in enumerate(filtered_df.itertuples()):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="hotel-card">
                <div style="height:180px; background-image:url('{hotel.amenity_img}'); 
                            background-size:cover; border-radius:15px; margin-bottom:1rem;"></div>
                <h4 style="color:#1a1a2e; margin:0.5rem 0;">{hotel.name}</h4>
                <p style="color:#666;">📍 {hotel.region}</p>
                <div style="font-size:1.5rem; color:#ffd700; font-weight:800;">
                    ₹{hotel.price:,}/night
                </div>
                <div style="color:#5f259f; font-size:0.9rem; font-weight:600;">
                    ✨ {hotel.amenity_name}
                </div>
            </div>
            """, unsafe_allow_html=True)
else:
    st.warning("🔍 No matches. Try different filters!")

st.markdown("---")
if st.button("🏠 Home", use_container_width=True):
    st.switch_page("app.py")

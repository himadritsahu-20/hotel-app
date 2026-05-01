import streamlit as st
import pandas as pd
import time

# --- GLOBAL PAGE CONFIG ---
st.set_page_config(
    page_title="H&H Luxury Hotels India",
    page_icon="🏨",
    layout="wide"
)

# --- 20 HOTELS DATA (10 Regions × 2 Hotels) ---
hotels_data = [
    # 1. GOA (2 Hotels)
    {"name": "H&H Signature Baga", "region": "Goa", "price": 8500, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Beachfront Infinity Pool"},
    {"name": "Taj Exotica Palolem", "region": "Goa", "price": 12500, "amenity_img": "https://images.unsplash.com/photo-1578631615436-393305d0edef?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Private Golden Beach"},
    
    # 2. RAJASTHAN (2 Hotels)
    {"name": "Oberoi Udaivilas", "region": "Rajasthan", "price": 28500, "amenity_img": "https://images.unsplash.com/photo-1583736913811-86d4f318425b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Lake Pichola Palace"},
    {"name": "Taj Lake Palace", "region": "Rajasthan", "price": 32000, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Floating Marble Spa"},
    
    # 3. KERALA (2 Hotels)
    {"name": "Taj Kumarakom Resort", "region": "Kerala", "price": 14200, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Backwater Houseboats"},
    {"name": "The Zuri Munnar", "region": "Kerala", "price": 7600, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Tea Estate Infinity Pool"},
    
    # 4. HIMACHAL PRADESH (2 Hotels)
    {"name": "The Grand Manali", "region": "Himachal Pradesh", "price": 6200, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Snow Mountain Spa"},
    {"name": "Taj Theog Resort", "region": "Himachal Pradesh", "price": 8900, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Pine Forest Villas"},
    
    # 5. UTTARAKHAND (2 Hotels)
    {"name": "Ananda Himalayas", "region": "Uttarakhand", "price": 28500, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Yoga Retreat Palace"},
    {"name": "Taj Corbett Resort", "region": "Uttarakhand", "price": 15600, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Tiger Safari Decks"},
    
    # 6. MAHARASHTRA (2 Hotels)
    {"name": "JW Marriott Mumbai", "region": "Maharashtra", "price": 13500, "amenity_img": "https://images.unsplash.com/photo-1564507592333-cdd505798f28?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Arabian Sea Infinity Pool"},
    {"name": "Taj Lands End", "region": "Maharashtra", "price": 11800, "amenity_img": "https://images.unsplash.com/photo-1578631615436-393305d0edef?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Bandra Bandstand Views"},
    
    # 7. TAMIL NADU (2 Hotels)
    {"name": "ITC Grand Chola", "region": "Tamil Nadu", "price": 11200, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Chola Dynasty Spa"},
    {"name": "Taj Coromandel", "region": "Tamil Nadu", "price": 9800, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Marina Beach Club"},
    
    # 8. KARNATAKA (2 Hotels)
    {"name": "Taj West End Bengaluru", "region": "Karnataka", "price": 13200, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Banyan Tree Gardens"},
    {"name": "The Oberoi Bengaluru", "region": "Karnataka", "price": 16800, "amenity_img": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Silicon Valley Spa"},
    
    # 9. ANDHRA PRADESH (2 Hotels)
    {"name": "Novotel Visakhapatnam", "region": "Andhra Pradesh", "price": 7200, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Bay of Bengal Beach"},
    {"name": "Taj Deccan Hyderabad", "region": "Andhra Pradesh", "price": 12400, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Golconda Fort Views"},
    
    # 10. GUJARAT (2 Hotels)
    {"name": "Taj Skyline Ahmedabad", "region": "Gujarat", "price": 10800, "amenity_img": "https://images.unsplash.com/photo-1564507592333-cdd505798f28?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Sabarmati Riverfront"},
    {"name": "The Gateway Vadodara", "region": "Gujarat", "price": 6800, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Laxmi Vilas Palace"}
]

df = pd.DataFrame(hotels_data)

# --- HOME PAGE CSS ---
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #ffd700, #ffed4e);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: #1a1a1a;
        margin-bottom: 2rem;
    }
    .explore-btn {
        background: linear-gradient(135deg, #5f259f, #7b33cc) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 20px 50px !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        box-shadow: 0 15px 40px rgba(95,37,159,0.4) !important;
        border: none !important;
        width: 100% !important;
        height: 80px !important;
    }
    .explore-btn:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 25px 50px rgba(95,37,159,0.6) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- PAGE ROUTING ---
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

page = st.sidebar.selectbox("Navigate", ["🏠 Home", "🏨 Explore Hotels"])

if page == "🏠 Home":
    # HOME PAGE
    st.markdown("<div class='main-header'><h1>👑 H&H Luxury Hotels India</h1><p>20 Premium Properties | 10 Regions</p></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); padding: 3rem; border-radius: 25px; text-align: center; height: 400px; display: flex; flex-direction: column; justify-content: center;">
            <h2 style="color: #5f259f; margin-bottom: 1rem;">20 Luxury Properties</h2>
            <p style="font-size: 1.2rem; color: #666; margin-bottom: 2rem;">Across 10 Beautiful Regions</p>
            <ul style="text-align: left; font-size: 1.1rem; color: #444;">
                <li>📍 10 Regions</li>
                <li>🏨 20 Properties</li>
                <li>⭐ 5-Star Only</li>
                <li>💰 ₹5K - ₹32K/night</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=800&q=80", use_column_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("<h2 style='color: #5f259f; text-align: center;'>Ready to Book?</h2>", unsafe_allow_html=True)
    with col2:
        if st.button("🚀 Explore Luxury Properties", key="explore_btn", help="Find your perfect hotel", use_container_width=True):
            st.session_state.page = "🏨 Explore Hotels"
            st.rerun()
    
    st.markdown("### 📞 Contact Info")
    col1, col2, col3 = st.columns(3)
    with col1: st.info("**support@hhluxury.com**")
    with col2: st.info("**+91 98765 43210**")
    with col3: st.info("**24/7 Support**")

elif page == "🏨 Explore Hotels":
    # HOTELS PAGE - DARK THEME
    st.markdown("""
    <style>
        /* Dark Theme for Hotels Page */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%) !important;
            color: white !important;
        }
        
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%) !important;
        }
        
        /* Golden Headings */
        h1, h2, h3 {
            color: #ffd700 !important;
            text-shadow: 2px 2px 8px rgba(255,215,0,0.5) !important;
            font-weight: 700 !important;
        }
        
        /* Filter Boxes - Dark with Golden Borders */
        .filter-box {
            background: rgba(26,26,46,0.95) !important;
            border: 3px solid #ffd700 !important;
            border-radius: 25px !important;
            padding: 2.5rem !important;
            margin: 1.5rem 0 !important;
            backdrop-filter: blur(15px) !important;
            box-shadow: 0 20px 40px rgba(0,0,0,0.5) !important;
        }
        
        /* White Inner Boxes with Golden Text */
        .inner-box {
            background: rgba(255,255,255,0.98) !important;
            border-radius: 20px !important;
            padding: 2rem !important;
            margin: 1rem 0 !important;
            border-left: 6px solid #ffd700 !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3) !important;
        }
        
        .golden-option, .golden-text {
            color: #ffd700 !important;
            font-weight: 700 !important;
        }
        
        /* Hotel Cards */
        .hotel-card {
            background: rgba(255,255,255,0.95) !important;
            border-radius: 20px !important;
            padding: 1.5rem !important;
            margin: 1rem 0 !important;
            border: 2px solid #ffd700 !important;
            transition: transform 0.3s ease !important;
        }
        
        .hotel-card:hover {
            transform: translateY(-5px) !important;
            box-shadow: 0 20px 40px rgba(255,215,0,0.3) !important;
        }
        
        /* Slider */
        .stSlider > div > div > div {
            background: linear-gradient(90deg, #ffd700, #ffed4e) !important;
        }
        
        /* Multiselect */
        .stMultiSelect > label {
            color: #ffd700 !important;
            font-weight: 800 !important;
            font-size: 1.3rem !important;
        }
        
        /* Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #ffd700, #ffed4e) !important;
            color: #1a1a2e !important;
            border-radius: 25px !important;
            font-weight: 800 !important;
            box-shadow: 0 15px 35px rgba(255,215,0,0.5) !important;
            font-size: 1.1rem !important;
        }
        
        /* Metrics */
        .stMetric {
            background: rgba(255,255,255,0.15) !important;
            border: 2px solid #ffd700 !important;
            border-radius: 20px !important;
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # HOTELS PAGE CONTENT
    st.markdown("<h1>🔍 Find Your Perfect Stay</h1>", unsafe_allow_html=True)
    st.info(f"📊 **{len(df['region'].unique())} Regions | {len(df)} Luxury Hotels**")
    
    # FILTERS IN GOLDEN DARK BOXES
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="filter-box">', unsafe_allow_html=True)
        st.markdown("<h3>🌍 Select Region</h3>", unsafe_allow_html=True)
        selected_regions = st.multiselect(
            "Choose destinations", 
            options=list(df['region'].unique()),
            default=list(df['region'].unique())[:3],
            format_func=lambda x: f"📍 {x}"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="filter-box">', unsafe_allow_html=True)
        st.markdown("<h3>💰 Price Range</h3>", unsafe_allow_html=True)
        min_price, max_price = st.slider(
            "₹ Per Night", 
            3000, 35000, (5000, 20000), 1000
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="filter-box">', unsafe_allow_html=True)
        st.markdown("<h3>✨ Featured Amenities</h3>", unsafe_allow_html=True)
        amenities = st.multiselect(
            "Select features", 
            options=["🏊 Pool", "🧖 Spa", "🏖️ Beach", "⛰️ Mountain", "🏰 Heritage", "🚤 Lake"],
            default=["🏊 Pool", "🧖 Spa"]
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # FILTER & DISPLAY RESULTS
    filtered_df = df[
        (df['region'].isin(selected_regions)) &
        (df['price'].between(min_price, max_price))
    ]
    
    st.markdown(f"<h2>🏨 {len(filtered_df)} Luxury Properties Found</h2>", unsafe_allow_html=True)
    
    if len(filtered_df) > 0:
        # 3-COLUMN HOTEL GRID
        cols = st.columns(3)
        for idx, hotel in enumerate(filtered_df.itertuples()):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="hotel-card">
                    <div style="height:180px; background-image:url('{hotel.amenity_img}'); 
                                background-size:cover; background-position:center; 
                                border-radius:15px; margin-bottom:1rem;"></div>
                    <h4 class="golden-option">{hotel.name}</h4>
                    <p style="color:#666; margin:0.5rem 0;">📍 {hotel.region}</p>
                    <div style="font-size:1.5rem; color:#ffd700; font-weight:800; margin:0.5rem 0;">
                        ₹{hotel.price:,}<span style="font-size:1rem;">/night</span>
                    </div>
                    <div style="color:#ffd700; font-size:0.95rem; font-style:italic;">
                        ✨ {hotel.amenity_name}
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("🔍 No hotels match your filters. Try adjusting your search!")
    
    # BACK TO HOME
    st.markdown("---")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.session_state.page = "🏠 Home"
        st.rerun()

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import time

# --- ENHANCED PAGE CONFIGURATION ---
st.set_page_config(
    page_title="👑 H&H Luxury Hotels India ",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Meta
st.markdown("""
<link rel="icon" type="image/x-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏨</text></svg>">
<meta name="description" content="Book 5⭐ luxury hotels across 10 regions in India. Instant PhonePe payments.">
""", unsafe_allow_html=True)

# --- PREMIUM CUSTOM CSS ---
st.markdown("""
<style>
    /* Full App Theme */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #fafbff 0%, #e8f4fd 50%, #f0f8ff 100%) !important;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #5f259f, #7b33cc) !important;
    }
    
    /* Main Header */
    .main-header {
        background: linear-gradient(135deg, #ffd700, #ffed4e, #ff6b35);
        padding: 2.5rem;
        border-radius: 25px;
        text-align: center;
        color: #1a1a1a;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(255,215,0,0.3);
        font-weight: 700;
    }
    
    .main-header h1 {
        font-size: 3rem !important;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.3) !important;
        background: linear-gradient(45deg, #5f259f, #ffd700) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    
    /* Hotel Hero */
    .hotel-hero {
        height: 450px;
        border-radius: 25px;
        display: flex;
        align-items: flex-end;
        padding: 3rem;
        color: white;
        text-shadow: 2px 2px 12px rgba(0,0,0,0.9);
        margin-bottom: 2rem;
        background-size: cover;
        background-position: center;
        position: relative;
        overflow: hidden;
    }
    
    .hotel-hero::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(45deg, rgba(95,37,159,0.7), rgba(123,51,204,0.6));
        z-index: 1;
    }
    
    .hotel-hero > div { position: relative; z-index: 2; }
    
    /* Amenity Badge */
    .amenity-badge {
        background: rgba(255,215,0,0.95) !important;
        color: #1a1a1a !important;
        padding: 8px 20px !important;
        border-radius: 25px !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2) !important;
    }
    
    /* Buttons */
    .stButton > button {
        width: 100% !important;
        background: linear-gradient(135deg, #5f259f, #7b33cc, #a855f7) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 14px 24px !important;
        font-weight: 600 !important;
        box-shadow: 0 8px 25px rgba(95,37,159,0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 35px rgba(95,37,159,0.6) !important;
    }
    
    /* Form Elements */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        border-radius: 15px !important;
        border: 2px solid #e9ecef !important;
        padding: 14px 16px !important;
    }
    
    /* Metrics */
    .stMetric {
        background: linear-gradient(135deg, #f8f9fa, #e9ecef) !important;
        border-radius: 15px !important;
        padding: 1.5rem !important;
        border: 2px solid #e9ecef !important;
        text-align: center !important;
    }
    
    /* Filters */
    .stMultiSelect > label, .stSlider > label {
        font-weight: 700 !important;
        color: #5f259f !important;
        font-size: 1.1rem !important;
    }
    
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #5f259f, #7b33cc) !important;
    }
    
    /* Status Messages */
    .stInfo, .stSuccess, .stError {
        border-radius: 15px !important;
        border-left: 5px solid #5f259f !important;
        padding: 1.2rem !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #f1f1f1; border-radius: 10px; }
    ::-webkit-scrollbar-thumb { 
        background: linear-gradient(135deg, #5f259f, #7b33cc); 
        border-radius: 10px; 
    }
</style>
""", unsafe_allow_html=True)

# --- 30 HOTELS DATA (10 Regions × 3 Hotels) ---
hotels_data = [
    # GOA
    {"name": "H&H Signature Baga", "region": "Goa", "price": 8500, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Beachfront Infinity Pool"},
    {"name": "Taj Exotica Palolem", "region": "Goa", "price": 12500, "amenity_img": "https://images.unsplash.com/photo-1578631615436-393305d0edef?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Private Golden Beach"},
    {"name": "Alila Diwa Candolim", "region": "Goa", "price": 9800, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Ayurvedic Spa Village"},
    
    # RAJASTHAN
    {"name": "Oberoi Udaivilas", "region": "Rajasthan", "price": 28500, "amenity_img": "https://images.unsplash.com/photo-1583736913811-86d4f318425b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Lake Pichola Palace"},
    {"name": "Taj Lake Palace", "region": "Rajasthan", "price": 32000, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Floating Marble Spa"},
    {"name": "Rambagh Palace", "region": "Rajasthan", "price": 21000, "amenity_img": "https://images.unsplash.com/photo-1564507592333-cdd505798f28?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Royal Polo Gardens"},
    
    # KERALA
    {"name": "Taj Kumarakom", "region": "Kerala", "price": 14200, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Backwater Houseboats"},
    {"name": "Brunton Boatyard", "region": "Kerala", "price": 9100, "amenity_img": "https://images.unsplash.com/photo-1518709268805-4e9042af2176?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Fort Kochi Heritage"},
    {"name": "The Zuri Munnar", "region": "Kerala", "price": 7600, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Tea Estate Infinity Pool"},
    
    # HIMACHAL PRADESH
    {"name": "The Grand Manali", "region": "Himachal Pradesh", "price": 6200, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Snow Mountain Spa"},
    {"name": "Taj Theog Resort", "region": "Himachal Pradesh", "price": 8900, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Pine Forest Villas"},
    {"name": "Wildflower Hall", "region": "Himachal Pradesh", "price": 23800, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Cedar Wood Spa"},
    
    # UTTARAKHAND
    {"name": "Ananda Himalayas", "region": "Uttarakhand", "price": 28500, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Yoga Retreat Palace"},
    {"name": "The Postcard Dewali", "region": "Uttarakhand", "price": 9200, "amenity_img": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Kumaon Hill Terraces"},
    {"name": "Taj Corbett Resort", "region": "Uttarakhand", "price": 15600, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Tiger Safari Decks"},
    
    # MAHARASHTRA
    {"name": "JW Marriott Mumbai", "region": "Maharashtra", "price": 13500, "amenity_img": "https://images.unsplash.com/photo-1564507592333-cdd505798f28?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Arabian Sea Infinity Pool"},
    {"name": "Taj Lands End", "region": "Maharashtra", "price": 11800, "amenity_img": "https://images.unsplash.com/photo-1578631615436-393305d0edef?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Bandra Bandstand Views"},
    {"name": "ITC Grand Maratha", "region": "Maharashtra", "price": 10200, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Mumbai Skyline Lounge"},
    
    # TAMIL NADU
    {"name": "ITC Grand Chola", "region": "Tamil Nadu", "price": 11200, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Chola Dynasty Spa"},
    {"name": "Taj Coromandel", "region": "Tamil Nadu", "price": 9800, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Marina Beach Club"},
    {"name": "Leela Palace Chennai", "region": "Tamil Nadu", "price": 14500, "amenity_img": "https://images.unsplash.com/photo-1518709268805-4e9042af2176?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Temple City Rooftop"},
    
    # KARNATAKA
    {"name": "Taj West End Bengaluru", "region": "Karnataka", "price": 13200, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Banyan Tree Gardens"},
    {"name": "The Oberoi Bengaluru", "region": "Karnataka", "price": 16800, "amenity_img": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Silicon Valley Spa"},
    {"name": "Evolve Back Coorg", "region": "Karnataka", "price": 18900, "amenity_img": "https://images.unsplash.com/photo-1561501900-3701fa6a0864?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Coffee Plantation Resort"},
    
    # ANDHRA PRADESH
    {"name": "Novotel Visakhapatnam", "region": "Andhra Pradesh", "price": 7200, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Bay of Bengal Beach"},
    {"name": "The Park Hyderabad", "region": "Andhra Pradesh", "price": 8900, "amenity_img": "https://images.unsplash.com/photo-1578631615436-393305d0edef?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Charminar Sky Lounge"},
    {"name": "Taj Deccan Hyderabad", "region": "Andhra Pradesh", "price": 12400, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Golconda Fort Views"},
    
    # GUJARAT
    {"name": "Taj Skyline Ahmedabad", "region": "Gujarat", "price": 10800, "amenity_img": "https://images.unsplash.com/photo-1564507592333-cdd505798f28?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Sabarmati Riverfront"},
    {"name": "The Gateway Hotel Vadodara", "region": "Gujarat", "price": 6800, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Laxmi Vilas Palace"},
    {"name": "Fermi Bungalows Diu", "region": "Gujarat", "price": 5200, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Portuguese Beach Resort"}
]

df = pd.DataFrame(hotels_data)

# --- MAIN UI ---
st.markdown("<div class='main-header'><h1>👑 H&H Luxury Hotels India</h1><p>30 Properties | 10 Regions | Instant PhonePe Bookings</p></div>", unsafe_allow_html=True)

st.info(f"📊 {len(df['region'].unique())} Regions | {len(df)} Luxury Hotels Available")

# STEP 1: ADVANCED FILTERS
st.subheader("🔍 Find Your Perfect Stay")
col1, col2, col3 = st.columns(3)

with col1:
    selected_regions = st.multiselect(
        "Select Regions", 
        options=list(df['region'].unique()), 
        default=list(df['region'].unique())[:3],
        max_selections=5
    )

with col2:
    min_price, max_price = st.slider(
        "Price Range (₹/night)", 
        3000, 35000, (5000, 20000), 1000
    )

with col3:
    selected_amenities = st.multiselect(
        "Featured Amenities", 
        options=["Pool", "Spa", "Beach", "Mountain", "Heritage"],
        default=["Pool", "Spa"]
    )

# FILTER HOTELS
filtered_df = df[
    (df['region'].isin(selected_regions)) &
    (df['price'].between(min_price, max_price))
]

# STEP 2: HOTEL GRID
st.subheader(f"🏨 {len(filtered_df)} Luxury Properties Found")

if len(filtered_df) > 0:
    cols = st.columns(3)
    for idx, hotel in enumerate(filtered_df.itertuples()):
        col_idx = idx % 3
        with cols[col_idx]:
            st.markdown(f"""
            <div style="border-radius:20px; overflow:hidden; box-shadow: 0 15px 40px rgba(0,0,0,0.15); 
                        background:white; height:350px; transition: transform 0.3s ease;">
                <div style="height:200px; background-image:url('{hotel.amenity_img}'); 
                            background-size:cover; background-position:center; position:relative;">
                    <div style="position:absolute; bottom:10px; left:15px; right:15px; 
                                background:rgba(95,37,159,0.9); color:white; padding:8px 15px; 
                                border-radius:20px; font-size:0.85rem; text-align:center;">
                        {hotel.amenity_name}
                    </div>
                </div>
                <div style="padding:20px;">
                    <h4 style="margin:0 0 5px 0; color:#5f259f; font-size:1.1rem;">{hotel.name}</h4>
                    <p style="color:#666; margin:0 0 10px 0; font-size:0.9rem;">📍 {hotel.region}</p>
                    <div style="font-size:1.3rem; font-weight:800; color:#ffd700; margin-bottom:15px;">
                        ₹{hotel.price:,}<span style="font-size:0.8rem; font-weight:400;">/night</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # STEP 3: SELECTED HOTEL
    st.subheader("🏆 Featured Property Details")
    selected_hotel_name = st.selectbox(
        "Choose your stay:", 
        options=["None"] + filtered_df['name'].tolist()
    )
    
    if selected_hotel_name != "None":
        hotel_details = df[df['name'] == selected_hotel_name].iloc[0]
        
        st.markdown(f"""
            <div class="hotel-hero" style="background-image: url('{hotel_details['amenity_img']}');">
                <div>
                    <h1>{hotel_details['name']}</h1>
                    <p>📍 {hotel_details['region']} | 💰 ₹{hotel_details['price']:,}/night</p>
                    <span class="amenity-badge">{hotel_details['amenity_name']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Hotel Stats
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.metric("⭐ Rating", "4.8/5")
        with col2: st.metric("🛏️ Rooms", "150+")
        with col3: st.metric("💰 Price/Night", f"₹{hotel_details['price']:,}")
        with col4: st.metric("📍 Region", hotel_details['region'])

# --- BOOKING SECTION ---
if 'hotel_details' in locals():
    st.divider()
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 💳 Secure Instant Booking")
        with st.form("booking_form"):
            st.write(f"**{hotel_details['name']}**")
            name = st.text_input("👤 Full Name *")
            phone = st.text_input("📱 PhonePe Number *")
            nights = st.number_input("🛏️ Number of Nights", min_value=1, value=2)
            
            total_price = hotel_details['price'] * nights
            st.markdown(f"### 💰 **Total: ₹{total_price:,}**")
            
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                if st.form_submit_button("🚀 Book Now", use_container_width=True):
                    if name and phone:
                        st.balloons()
                        st.success(f"✅ Booking Request Sent!\nCheck PhonePe for ₹{total_price:,} payment.")
                        st.markdown("[🔗 Open PhonePe App](https://www.phonepe.com/)", unsafe_allow_html=True)
                    else:
                        st.error("⚠️ Please fill all fields")
    
    with col2:
        st.markdown("""
        <div style="background:linear-gradient(135deg,#f8f9fa,#e9ecef); 
                    padding:25px; border-radius:20px; border:3px solid #5f259f; 
                    height:320px; text-align:center;">
            <h4 style="color:#5f259f; margin-top:0;">🔒 100% Secure</h4>
            <div style="font-size:1.4rem; color:#ffd700; margin:15px 0;">✓ Instant Confirmation</div>
            <ul style="text-align:left; font-size:0.95rem; line-height:1.6;">
                <li>✅ UPI/PhonePe Payments</li>
                <li>✅ No Hidden Fees</li>
                <li>✅ Free Cancellation</li>
                <li>✅ 24/7 Support</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- ENHANCED SIDEBAR CHATBOT ---
with st.sidebar:
    st.title("🤖 H&H Assistant")
    st.markdown("**Ask me anything about hotels!**")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Welcome! I can help you find the perfect luxury hotel. Try asking: 'Show Goa beach hotels' or 'Best spa in Rajasthan'!"}
        ]
    
    # Chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about hotels..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Smart responses
        prompt_lower = prompt.lower()
        if any(word in prompt_lower for word in ["goa", "beach"]):
            response = "🏖️ **Goa Recommendations:** H&H Signature Baga (₹8500) has beachfront infinity pool! Perfect for beach lovers."
        elif any(word in prompt_lower for word in ["rajasthan", "udaipur", "jaipur"]):
            response = "🏰 **Rajasthan Gems:** Oberoi Udaivilas (₹28,500) offers Lake Pichola views. Ultimate luxury!"
        elif "cheap" in prompt_lower or "budget" in prompt_lower:
            response = "💰 **Best Value:** Fermi Bungalows Diu, Gujarat (₹5200) - Portuguese beach resort!"
        elif "spa" in prompt_lower or "wellness" in prompt_lower:
            response = "🧖‍♀️ **Top Spas:** Ananda Himalayas (₹28,500) is world-famous for yoga & wellness retreats."
        else:
            response = "I recommend filtering by region above! Popular choices: Goa beaches, Rajasthan palaces, Kerala backwaters."
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

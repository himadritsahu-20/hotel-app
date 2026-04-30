import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="H&H Luxury Hotels India",
    page_icon="🏨",
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
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
    
    /* Hotel Hero Background */
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
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(95,37,159,0.7), rgba(123,51,204,0.6));
        z-index: 1;
    }
    
    .hotel-hero > div {
        position: relative;
        z-index: 2;
    }
    
    /* Amenity Badge */
    .amenity-badge {
        background: rgba(255,215,0,0.95);
        color: #1a1a1a;
        padding: 8px 20px;
        border-radius: 25px;
        font-size: 0.95rem;
        font-weight: 600;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Buttons */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #5f259f, #7b33cc, #a855f7) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        box-shadow: 0 8px 25px rgba(95,37,159,0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 35px rgba(95,37,159,0.6) !important;
    }
    
    /* Multiselect & Slider Styling */
    .stMultiSelect > label {
        font-weight: 700;
        color: #5f259f !important;
    }
    
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #5f259f, #7b33cc) !important;
    }
    
    /* Metrics Cards */
    .stMetric {
        background: linear-gradient(135deg, #f8f9fa, #e9ecef) !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        border: 2px solid #e9ecef !important;
    }
    
    /* Info & Success Boxes */
    .stInfo, .stSuccess {
        border-radius: 15px !important;
        border-left: 5px solid #5f259f !important;
        padding: 1rem !important;
    }
    
    /* Form Styling */
    .stTextInput > div > div > input {
        border-radius: 15px !important;
        border: 2px solid #e9ecef !important;
        padding: 12px 16px !important;
    }
    
    .stNumberInput > div > div > input {
        border-radius: 15px !important;
        border: 2px solid #e9ecef !important;
    }
    
    /* Sidebar Chat */
    .css-1d391kg {
        background: linear-gradient(135deg, #5f259f, #7b33cc) !important;
        color: white !important;
    }
    
    /* Responsive Grid Fix */
    @media (max-width: 768px) {
        .stColumns > div {
            width: 100% !important;
        }
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #5f259f, #7b33cc);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- DATASET ---
# Including amenity-specific background images for the selection phase
hotels_data = [
    # 1. GOA (3 hotels)
    {"name": "H&H Signature Baga", "region": "Goa", "price": 8500, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Beachfront Infinity Pool"},
    {"name": "Taj Exotica Palolem", "region": "Goa", "price": 12500, "amenity_img": "https://images.unsplash.com/photo-1578631615436-393305d0edef?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Private Golden Beach"},
    {"name": "Alila Diwa Candolim", "region": "Goa", "price": 9800, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Ayurvedic Spa Village"},

    # 2. RAJASTHAN (3 hotels)
    {"name": "Oberoi Udaivilas", "region": "Rajasthan", "price": 28500, "amenity_img": "https://images.unsplash.com/photo-1583736913811-86d4f318425b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Lake Pichola Palace"},
    {"name": "Taj Lake Palace", "region": "Rajasthan", "price": 32000, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Floating Marble Spa"},
    {"name": "Rambagh Palace", "region": "Rajasthan", "price": 21000, "amenity_img": "https://images.unsplash.com/photo-1564507592333-cdd505798f28?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Royal Polo Gardens"},

    # 3. KERALA (3 hotels)
    {"name": "Taj Kumarakom", "region": "Kerala", "price": 14200, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Backwater Houseboats"},
    {"name": "Brunton Boatyard", "region": "Kerala", "price": 9100, "amenity_img": "https://images.unsplash.com/photo-1518709268805-4e9042af2176?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Fort Kochi Heritage"},
    {"name": "The Zuri Munnar", "region": "Kerala", "price": 7600, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Tea Estate Infinity Pool"},

    # 4. HIMACHAL PRADESH (3 hotels)
    {"name": "The Grand Manali", "region": "Himachal Pradesh", "price": 6200, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Snow Mountain Spa"},
    {"name": "Taj Theog Resort", "region": "Himachal Pradesh", "price": 8900, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Pine Forest Villas"},
    {"name": "Wildflower Hall", "region": "Himachal Pradesh", "price": 23800, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Cedar Wood Spa"},

    # 5. UTTARAKHAND (3 hotels)
    {"name": "Ananda Himalayas", "region": "Uttarakhand", "price": 28500, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Yoga Retreat Palace"},
    {"name": "The Postcard Dewali", "region": "Uttarakhand", "price": 9200, "amenity_img": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Kumaon Hill Terraces"},
    {"name": "Taj Corbett Resort", "region": "Uttarakhand", "price": 15600, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Tiger Safari Decks"},

    # 6. MAHARASHTRA (3 hotels)
    {"name": "JW Marriott Mumbai", "region": "Maharashtra", "price": 13500, "amenity_img": "https://images.unsplash.com/photo-1564507592333-cdd505798f28?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Arabian Sea Infinity Pool"},
    {"name": "Taj Lands End", "region": "Maharashtra", "price": 11800, "amenity_img": "https://images.unsplash.com/photo-1578631615436-393305d0edef?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Bandra Bandstand Views"},
    {"name": "ITC Grand Maratha", "region": "Maharashtra", "price": 10200, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Mumbai Skyline Lounge"},

    # 7. TAMIL NADU (3 hotels)
    {"name": "ITC Grand Chola", "region": "Tamil Nadu", "price": 11200, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Chola Dynasty Spa"},
    {"name": "Taj Coromandel", "region": "Tamil Nadu", "price": 9800, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Marina Beach Club"},
    {"name": "Leela Palace Chennai", "region": "Tamil Nadu", "price": 14500, "amenity_img": "https://images.unsplash.com/photo-1518709268805-4e9042af2176?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Temple City Rooftop"},

    # 8. KARNATAKA (3 hotels)
    {"name": "Taj West End Bengaluru", "region": "Karnataka", "price": 13200, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Banyan Tree Gardens"},
    {"name": "The Oberoi Bengaluru", "region": "Karnataka", "price": 16800, "amenity_img": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Silicon Valley Spa"},
    {"name": "Evolve Back Coorg", "region": "Karnataka", "price": 18900, "amenity_img": "https://images.unsplash.com/photo-1561501900-3701fa6a0864?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Coffee Plantation Resort"},

    # 9. ANDHRA PRADESH (3 hotels)
    {"name": "Novotel Visakhapatnam", "region": "Andhra Pradesh", "price": 7200, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Bay of Bengal Beach"},
    {"name": "The Park Hyderabad", "region": "Andhra Pradesh", "price": 8900, "amenity_img": "https://images.unsplash.com/photo-1578631615436-393305d0edef?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Charminar Sky Lounge"},
    {"name": "Taj Deccan Hyderabad", "region": "Andhra Pradesh", "price": 12400, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Golconda Fort Views"},

    # 10. GUJARAT (3 hotels)
    {"name": "Taj Skyline Ahmedabad", "region": "Gujarat", "price": 10800, "amenity_img": "https://images.unsplash.com/photo-1564507592333-cdd505798f28?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Sabarmati Riverfront"},
    {"name": "The Gateway Hotel Vadodara", "region": "Gujarat", "price": 6800, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Laxmi Vilas Palace"},
    {"name": "Fermi Bungalows Diu", "region": "Gujarat", "price": 5200, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Portuguese Beach Resort"}
]

df = pd.DataFrame(hotels_data)

# --- MAIN UI ---
st.markdown("<div class='main-header'><h1>👑 H&H Luxury Hotels India</h1><p>30 Properties | 10 Regions | support@H&HLuxury.com</p></div>", unsafe_allow_html=True)

st.info(f"📊 {len(df['region'].unique())} Regions | {len(df)} Luxury Hotels Available")

# STEP 1: ADVANCED FILTERS (3 Columns)
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
    amenities = ["Pool", "Spa", "Beach", "Mountain", "Heritage", "Lake"]
    selected_amenities = st.multiselect(
        "Featured Amenities", 
        options=amenities,
        default=["Pool", "Spa"]
    )

# FILTER HOTELS
filtered_df = df[
    (df['region'].isin(selected_regions)) &
    (df['price'].between(min_price, max_price))
]

# STEP 2: HOTEL GRID (Responsive)
st.subheader(f"🏨 {len(filtered_df)} Luxury Properties Found")

if len(filtered_df) > 0:
    # Create 3-column grid for hotels
    cols = st.columns(3)
    for idx, hotel in enumerate(filtered_df.itertuples()):
        col_idx = idx % 3
        with cols[col_idx]:
            st.markdown(f"""
            <div style="border-radius:15px; overflow:hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
                <div style="height:200px; background-image:url('{hotel.amenity_img}'); 
                            background-size:cover; background-position:center; position:relative;">
                    <div style="position:absolute; bottom:10px; left:10px; 
                                background:rgba(0,0,0,0.7); color:white; padding:5px 10px; 
                                border-radius:15px; font-size:0.8rem;">
                        {hotel.amenity_name}
                    </div>
                </div>
                <div style="padding:15px;">
                    <h4 style="margin:0; color:#5f259f;">{hotel.name}</h4>
                    <p style="color:#666; margin:5px 0;">📍 {hotel.region}</p>
                    <div style="font-size:1.2rem; font-weight:bold; color:#ffd700;">
                        ₹{hotel.price:,}/night
                    </div>
                    <button onclick="this.parentElement.parentElement.querySelector('.hotel-details').style.display='block'" 
                            style="width:100%; background:linear-gradient(135deg,#5f259f,#7b33cc); 
                                   color:white; border:none; padding:10px; border-radius:20px; 
                                   cursor:pointer; margin-top:10px;">
                        View Details
                    </button>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # STEP 3: SELECTED HOTEL DETAILS (Single View)
    st.subheader("🏆 Featured Property")
    selected_hotel_name = st.selectbox(
        "Choose your favorite:", 
        options=filtered_df['name'].tolist() + ["None"],
        index=len(filtered_df['name'].tolist())
    )
    
    if selected_hotel_name != "None":
        hotel_details = df[df['name'] == selected_hotel_name].iloc[0]
        
        # Hero Section
        st.markdown(f"""
            <div class="hotel-hero" style="background-image: url('{hotel_details['amenity_img']}');">
                <div>
                    <h1>{hotel_details['name']}</h1>
                    <p>📍 {hotel_details['region']} | 💰 ₹{hotel_details['price']:,}/night</p>
                    <span class="amenity-badge">⭐ 4.8/5 | {hotel_details['amenity_name']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Quick Stats
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.metric("Rating", "4.8 ⭐")
        with col2: st.metric("Rooms", "120+")
        with col3: st.metric("Price/Night", f"₹{hotel_details['price']:,}")
        with col4: st.metric("Location", hotel_details['region'][:3])

# --- BOOKING SECTION (Same as before but improved) ---
if 'hotel_details' in locals():
    st.divider()
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 💳 Instant Booking")
        with st.form("booking_form"):
            st.write(f"**{hotel_details['name']}** - {hotel_details['region']}")
            name = st.text_input("👤 Full Name")
            phone = st.text_input("📱 PhonePe Number")
            nights = st.number_input("🛏️ Nights", min_value=1, value=2, max_value=30)
            
            total_price = hotel_details['price'] * nights
            st.markdown(f"**💰 Total: ₹{total_price:,}**")
            
            if st.form_submit_button("🚀 Book with PhonePe", use_container_width=True):
                if name and phone:
                    st.balloons()
                    st.success(f"✅ Booking confirmed for {name}! Check PhonePe for ₹{total_price:,} payment.")
                    st.markdown("[Open PhonePe](https://www.phonepe.com/)", unsafe_allow_html=True)
                else:
                    st.error("⚠️ Please enter your details")
    
    with col2:
        st.markdown("""
        <div style="background:#f8f9fa; padding:20px; border-radius:20px; border:2px solid #5f259f; height:250px;">
            <h4 style="color:#5f259f;">🔒 Why Choose Us?</h4>
            <ul style="font-size:0.9rem; line-height:1.4;">
                <li>✅ Instant Confirmation</li>
                <li>✅ Zero Cancellation Fee</li>
                <li>✅ 24/7 Support</li>
                <li>✅ PhonePe Secure</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- CHATBOT (INTEGRATED) ---
with st.sidebar:
    st.title("🤖 H&H Assistant")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How can I help you find a hotel today?"}]
    
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
        
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        # Simple logic
        reply = "I recommend the properties in Goa for beach lovers or Jaipur for heritage!"
        if "price" in prompt.lower(): reply = "Our luxury rooms start from ₹4,500."
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)

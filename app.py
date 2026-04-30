import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import base64
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="H&H Luxury Hotels India",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for H&H Luxury branding
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #ffd700, #ffed4e);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: #1a1a1a;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .hotel-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-left: 5px solid #ffd700;
        transition: transform 0.3s;
    }
    .hotel-card:hover {
        transform: translateY(-5px);
    }
    .price-tag {
        background: linear-gradient(135deg, #00d4aa, #00b894);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .hhluxury-btn {
        background: linear-gradient(135deg, #ffd700, #ffed4e);
        color: #1a1a1a;
        border: none;
        padding: 12px 24px;
        border-radius: 25px;
        font-weight: bold;
        font-size: 16px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# Load hotels data
@st.cache_data
def load_hotels():
    hotels_data = {
        "hotels": [
            {"id": 1, "name": "Zostel Goa Anjuna", "location": "Anjuna Beach, Goa", "region": "Goa", "price": 3200, "rating": 4.6, "features": ["Beachfront", "Pool"]},
            {"id": 2, "name": "The Hosteller Manali", "location": "Old Manali, HP", "region": "Himachal Pradesh", "price": 3800, "rating": 4.7, "features": ["Mountain View", "Bonfire"]},
            {"id": 3, "name": "Moustache Rishikesh", "location": "Tapovan, Rishikesh", "region": "Uttarakhand", "price": 2900, "rating": 4.5, "features": ["Ganga View", "Yoga"]},
            {"id": 4, "name": "Zostel Mumbai Bandra", "location": "Bandra West, Mumbai", "region": "Maharashtra", "price": 4200, "rating": 4.4, "features": ["Rooftop", "Urban"]},
            {"id": 5, "name": "The Hosteller Jaipur", "location": "Civil Lines, Jaipur", "region": "Rajasthan", "price": 3100, "rating": 4.6, "features": ["Heritage", "Rajasthani"]},
            # Add more from previous JSON...
        ]
    }
    return pd.DataFrame(hotels_data["hotels"])

# Sidebar
st.sidebar.title("🏨 H&H Luxury Hotels")
st.sidebar.markdown("---")
selected_page = st.sidebar.selectbox(
    "Navigate",
    ["🏠 Home", "🛏️ Browse Hotels", "🔍 Search", "💳 Book Now", "📊 Analytics", "👤 Profile", "🤖 Chat"]
)

# Header
st.markdown("""
<div class='main-header'>
    <h1>👑 H&H Luxury Hotels India</h1>
    <p>5-Star Premium Hotels Across Every Tourist Destination</p>
    <p><small>support@H&HLuxury.com | PhonePe Payments | Instant Booking</small></p>
</div>
""", unsafe_allow_html=True)

# Pages
if selected_page == "🏠 Home":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Luxury Hotels", "25+", "↗️")
    with col2:
        st.metric("Avg Rating", "4.6⭐", "↗️")
    with col3:
        st.metric("Starting Price", "₹2,500", "↗️")
    
    st.markdown("### 🌟 Featured Destinations")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        ### 🏖️ Goa
        **12 Luxury Hotels**  
        Starting ₹3,200/night
        """)
    with col2:
        st.markdown("""
        ### 🏔️ Himachal
        **15 Premium Stays**  
        Starting ₹3,800/night
        """)
    with col3:
        st.markdown("""
        ### 🗺️ Rajasthan
        **10 Royal Hotels**  
        Starting ₹3,100/night
        """)
    
    st.markdown("### 💳 Book with PhonePe")
    st.info("🔒 Secure UPI/Cards/Netbanking | Instant Confirmation | No hidden fees")

elif selected_page == "🛏️ Browse Hotels":
    hotels_df = load_hotels()
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        region = st.selectbox("Region", ["All"] + sorted(hotels_df['region'].unique()))
    with col2:
        min_price = st.slider("Min Price", 2000, 8000, 2500)
    with col3:
        min_rating = st.slider("Min Rating", 4.0, 5.0, 4.3)
    
    # Filter hotels
    filtered = hotels_df[
        (hotels_df['price'] >= min_price) &
        (hotels_df['rating'] >= min_rating)
    ]
    if region != "All":
        filtered = filtered[filtered['region'] == region]
    
    st.markdown(f"### Found {len(filtered)} Luxury Hotels")
    
    # Hotel cards
    for idx, hotel in filtered.iterrows():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
            <div class='hotel-card'>
                <h3>{hotel['name']}</h3>
                <p><i class='fas fa-map-marker-alt'></i> {hotel['location']}</p>
                <p><strong>Region:</strong> {hotel['region']}</p>
                <p>{', '.join(hotel['features'])}</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div style='text-align: center;'>
                <div class='price-tag'>₹{hotel['price']}</div>
                <p style='color: gold; font-size: 1.1rem;'>⭐{hotel['rating']}</p>
                <button class='hhluxury-btn'>Book Now</button>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("---")

elif selected_page == "🔍 Search":
    st.markdown("### 🔍 Search Luxury Hostels")
    query = st.text_input("Search by name, location, or region...")
    
    if query:
        hotels_df = load_hotels()
        results = hotels_df[
            hotels_df['name'].str.contains(query, case=False) |
            hotels_df['location'].str.contains(query, case=False) |
            hotels_df['region'].str.contains(query, case=False)
        ]
        st.dataframe(results)

elif selected_page == "💳 Book Now":
    st.markdown("### 💳 H&H Luxury Booking")
    st.info("🔧 PhonePe integration coming soon!")
    
    # Booking form
    with st.form("booking_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        checkin = st.date_input("Check-in")
        checkout = st.date_input("Check-out")
        hotel = st.selectbox("Select Hotel", ["Zostel Goa", "The Hosteller Manali"])
        
        submitted = st.form_submit_button("🚀 Pay with PhonePe")
        if submitted:
            st.success("🎉 Booking Confirmed! Check your email.")
            st.balloons()

elif selected_page == "📊 Analytics":
    hotels_df = load_hotels()
    
    # Charts
    col1, col2 = st.columns(2)
    with col1:
        fig = px.histogram(hotels_df, x='region', y='price', title="Price by Region")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.scatter(hotels_df, x='price', y='rating', 
                        size='price', color='region',
                        title="Price vs Rating")
        st.plotly_chart(fig, use_container_width=True)

elif selected_page == "👤 Profile":
    if 'user' not in st.session_state:
        st.session_state.user = None
    
    if st.session_state.user:
        st.success(f"Welcome {st.session_state.user['name']}!")
        if st.button("Logout"):
            st.session_state.user = None
            st.rerun()
    else:
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                # Demo login
                if email == "user@example.com" and password == "123456":
                    st.session_state.user = {"name": "John Doe", "email": email}
                    st.success("✅ Logged in!")
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials")

elif selected_page == "🤖 Chat":
    st.markdown("### 🤖 H&H Luxury AI Assistant")
    st.info("Chatbot coming soon! Email: support@H&HLuxury.com")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; color: #666;'>
    <h3>👑 H&H Luxury Hotels India</h3>
    <p>Premium 5-Star Hotels | PhonePe Payments | Instant Booking</p>
    <p>📧 <a href='mailto:support@H&HLuxury.com'>support@H&HLuxury.com</a> | 
    📱 +91-9876543210</p>
    <p>© 2024 H&H Luxury Hotels</p>
</div>
""", unsafe_allow_html=True)
import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit_chat
import hashlib
import base64
import json
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="H&H Luxury Hotels India",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- H&H LUXURY STYLING ---
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #ffd700, #ffed4e);
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        color: #1a1a1a;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    .hero-bg {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.4)), 
        url('https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80') center/cover;
        padding: 5rem 2rem;
        border-radius: 25px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .hotel-card {
        background: white;
        border-radius: 15px;
        padding: 1.2rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-left: 5px solid #ffd700;
        margin-bottom: 1rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #5f259f, #7b33cc) !important;
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        font-weight: bold !important;
    }
    .phonepe-text {
        color: #5f259f;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- PHONEPE INTEGRATION LOGIC ---
def initiate_phonepe_payment(amount, user_details):
    """
    Simulates the PhonePe payment gateway flow.
    In production, this would hit your backend to generate the X-VERIFY checksum.
    """
    merchant_id = "PGCHECKOUT" # Replace with your real Merchant ID
    salt_key = "099eb1a5-e509-480a-99df-2bbf32293b34" # Replace with real Salt Key
    
    st.toast("Connecting to PhonePe Secure Servers...", icon="🔒")
    time.sleep(1.5)
    
    # Simulate Redirect to PhonePe Gateway
    st.success(f"Redirecting to PhonePe for ₹{amount:,}...")
    components.html(f"""
        <script>
            setTimeout(function() {{
                window.open("https://merchants.phonepe.com/", "_blank");
            }}, 1000);
        </script>
    """, height=0)
    return True

# --- DATA LOADING ---
@st.cache_data
def get_hotel_data():
    return pd.DataFrame([
        {"id": 1, "name": "H&H Signature Goa", "location": "North Goa", "region": "Goa", "price": 8500, "rating": 5.0, "img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=400"},
        {"id": 2, "name": "The Grand Manali", "location": "Old Manali", "region": "Himachal Pradesh", "price": 6200, "rating": 4.8, "img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=400"},
        {"id": 3, "name": "Royal Palace Jaipur", "location": "Civil Lines", "region": "Rajasthan", "price": 7500, "rating": 4.9, "img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?w=400"},
        {"id": 4, "name": "Varanasi Heritage Hotel", "location": "Assi Ghat", "region": "Uttar Pradesh", "price": 4500, "rating": 4.7, "img": "https://images.unsplash.com/photo-1561501900-3701fa6a0864?w=400"}
    ])

# --- SIDEBAR NAV ---
st.sidebar.title("👑 H&H Luxury Hotels")
page = st.sidebar.radio("Navigation", ["🏠 Home", "🛏️ Hotels", "💳 Booking", "🤖 AI Assistant"])

# --- SHARED HEADER ---
st.markdown("<div class='main-header'><h1>👑 H&H Luxury Hotels India</h1><p>Verified 5-Star Stays • support@H&HLuxury.com</p></div>", unsafe_allow_html=True)

hotels_df = get_hotel_data()

# --- PAGES ---
if page == "🏠 Home":
    st.markdown("""
        <div class='hero-bg'>
            <h1 style='font-size: 3.5rem;'>Experience Pure Luxury</h1>
            <p style='font-size: 1.2rem;'>India's most exclusive hotels, now bookable via PhonePe.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🌟 Featured Properties")
    cols = st.columns(len(hotels_df))
    for i, row in hotels_df.iterrows():
        with cols[i]:
            st.image(row['img'], use_container_width=True)
            st.markdown(f"**{row['name']}**")
            st.caption(f"{row['region']} • ⭐{row['rating']}")

elif page == "🛏️ Hotels":
    st.subheader("Explore our Hotel Collection")
    region_filter = st.multiselect("Filter by Region", hotels_df['region'].unique())
    
    display_df = hotels_df
    if region_filter:
        display_df = hotels_df[hotels_df['region'].isin(region_filter)]
        
    for _, hotel in display_df.iterrows():
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            col1.image(hotel['img'], use_container_width=True)
            with col2:
                st.markdown(f"### {hotel['name']}")
                st.write(f"📍 {hotel['location']}, {hotel['region']}")
                st.write("✅ 5-Star Amenities • Free WiFi • Breakfast Included")
            with col3:
                st.markdown(f"<h2 style='color:#00b894;'>₹{hotel['price']:,}</h2>", unsafe_allow_html=True)
                if st.button(f"Select {hotel['id']}", key=f"btn_{hotel['id']}"):
                    st.session_state.selected_hotel = hotel['name']
                    st.session_state.total_price = hotel['price']
                    st.toast(f"Selected {hotel['name']}")

elif page == "💳 Booking":
    st.subheader("💳 Secure Checkout")
    
    if 'selected_hotel' not in st.session_state:
        st.warning("Please select a hotel from the 'Hotels' tab first.")
    else:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            with st.form("booking_form"):
                st.markdown(f"**Booking for:** {st.session_state.selected_hotel}")
                guest_name = st.text_input("Full Name")
                email = st.text_input("Email Address")
                phone = st.text_input("Mobile Number")
                nights = st.number_input("Number of Nights", min_value=1, value=1)
                
                total = st.session_state.total_price * nights
                
                st.markdown("---")
                st.markdown(f"### Total Payable: ₹{total:,}")
                
                pay_btn = st.form_submit_button("🚀 Pay with PhonePe")
                
                if pay_btn:
                    if not guest_name or not phone:
                        st.error("Please fill in all details.")
                    else:
                        initiate_phonepe_payment(total, {"name": guest_name, "email": email})

        with col2:
            st.markdown("""
                <div style='background:#f1f2f6; padding:1.5rem; border-radius:15px; border: 1px solid #5f259f;'>
                    <h4 class='phonepe-text'>Why PhonePe?</h4>
                    <ul style='font-size:0.9rem;'>
                        <li>Instant Payment Confirmation</li>
                        <li>Zero Transaction Fees for UPI</li>
                        <li>Safe & Encrypted (PCI-DSS)</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

elif page == "🤖 AI Assistant":
    st.subheader("🤖 H&H Support Bot")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I am your H&H Luxury Assistant. How can I help you with your hotel booking today?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Simple Logic
        response = "I can help you find hotels in Goa or Manali. You can pay securely via PhonePe in the Booking tab!"
        if "goa" in prompt.lower(): response = "We have 5 exclusive properties in Goa starting from ₹8,500."
        if "pay" in prompt.lower() or "phonepe" in prompt.lower(): response = "We accept all UPI, Cards, and Netbanking via PhonePe for instant confirmation."
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align:center; color:#666;'>© 2024 H&H Luxury Hotels India | <a href='mailto:support@H&HLuxury.com'>support@H&HLuxury.com</a></div>", unsafe_allow_html=True)

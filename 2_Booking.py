import streamlit as st
from hotels_data import df

# Initialize Session State (CRITICAL for navigation)
if 'current_page' not in st.session_state:
    st.session_state.current_page = "booking"

st.set_page_config(
    page_title="Booking | H&H Luxury Hotels",
    page_icon="💳",
    layout="wide"
)

# --- PREMIUM BOOKING PAGE CSS ---
st.markdown("""
<style>
    /* Elegant Booking Theme */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #fff8e1 0%, #fff3cd 50%, #fff0e6 100%) !important;
    }
    
    .booking-header {
        background: linear-gradient(135deg, #ffd700, #ffed4e, #ff6b35);
        padding: 4rem 3rem;
        border-radius: 30px;
        text-align: center;
        color: #1a1a1a;
        box-shadow: 0 25px 60px rgba(255,215,0,0.4);
        margin-bottom: 3rem;
    }
    
    .form-section {
        background: rgba(255,255,255,0.98);
        border-radius: 25px;
        padding: 3rem;
        box-shadow: 0 20px 50px rgba(0,0,0,0.1);
        border-top: 6px solid #5f259f;
        margin: 2rem 0;
    }
    
    /* Form Styling */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border-radius: 20px !important;
        border: 3px solid #e9ecef !important;
        padding: 18px 20px !important;
        font-size: 1.1rem !important;
        background: #fafbfc !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #5f259f, #7b33cc, #a855f7) !important;
        color: white !important;
        border-radius: 30px !important;
        font-size: 1.3rem !important;
        font-weight: 800 !important;
        padding: 18px 30px !important;
        box-shadow: 0 20px 40px rgba(95,37,159,0.4) !important;
        border: none !important;
        height: 65px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 25px 50px rgba(95,37,159,0.6) !important;
    }
    
    /* Nav Buttons */
    .nav-btn {
        background: linear-gradient(135deg, #ffd700, #ffed4e) !important;
        color: #1a1a1e !important;
        border-radius: 25px !important;
        font-weight: 700 !important;
        box-shadow: 0 15px 35px rgba(255,215,0,0.4) !important;
    }
    
    /* Metrics */
    .stMetric {
        background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(248,249,250,0.8));
        border-radius: 20px !important;
        padding: 2rem !important;
        border: 3px solid #ffd700 !important;
        text-align: center !important;
    }
    
    /* Success Message */
    .stSuccess {
        border-radius: 20px !important;
        border-left: 6px solid #5f259f !important;
        background: linear-gradient(90deg, rgba(95,37,159,0.1), rgba(123,51,204,0.1)) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION FUNCTIONS ---
def go_to_home():
    st.session_state.current_page = "home"
    st.switch_page("app.py")

def go_to_hotels():
    st.session_state.current_page = "hotels"
    st.switch_page("pages/1_Hotels.py")

# --- MAIN HEADER ---
st.markdown("""
<div class='booking-header'>
    <h1>💳 Secure Booking Portal</h1>
    <p>Complete your luxury reservation in 60 seconds</p>
</div>
""", unsafe_allow_html=True)

# --- HOTEL SELECTION ---
st.markdown('<div class="form-section">', unsafe_allow_html=True)
st.markdown("### 🏨 Select Your Dream Hotel")

col1, col2 = st.columns([2, 1])

with col1:
    selected_hotel = st.selectbox(
        "Choose from 20 premium properties:",
        options=df['name'].tolist(),
        format_func=lambda x: f"🏨 {x}"
    )

with col2:
    if selected_hotel:
        hotel_details = df[df['name'] == selected_hotel].iloc[0]
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); 
                    padding: 2rem; border-radius: 20px; text-align: center; 
                    border-left: 5px solid #5f259f;">
            <h4 style="color: #5f259f; margin: 0 0 1rem 0;">{hotel_details['region']}</h4>
            <p style="color: #666; margin: 0.5rem 0;">✨ {hotel_details['amenity_name']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- BOOKING FORM ---
if selected_hotel:
    hotel_details = df[df['name'] == selected_hotel].iloc[0]
    
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown("### 📋 Guest & Stay Details")
    
    with st.form("luxury_booking"):
        col1, col2 = st.columns(2)
        
        with col1:
            full_name = st.text_input("👤 Full Name *", placeholder="Enter your full name")
            email = st.text_input("📧 Email Address *", placeholder="your@email.com")
            phone = st.text_input("📱 PhonePe Number *", placeholder="9876543210")
        
        with col2:
            checkin_date = st.date_input("📅 Check-in Date", value=pd.Timestamp.now())
            nights = st.number_input("🛏️ Number of Nights", min_value=1, max_value=30, value=2)
            rooms = st.selectbox("👨‍👩‍👧‍👦 Rooms", options=[1, 2, 3, 4])
        
        # TOTAL CALCULATION
        total_amount = hotel_details['price'] * nights * rooms
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #5f259f, #7b33cc); 
                    color: white; padding: 2rem; border-radius: 20px; text-align: center; margin: 2rem 0;">
            <h2 style="margin: 0; font-size: 2.5rem;">₹{total_amount:,}</h2>
            <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem;">Total Payable Amount</p>
        </div>
        """, unsafe_allow_html=True)
        
        # SUBMIT BUTTONS
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            submitted = st.form_submit_button("🚀 Pay with PhonePe", use_container_width=True)
        with col2:
            call_booked = st.form_submit_button("📞 Call to Book", use_container_width=True)
        with col3:
            st.empty()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # SUCCESS HANDLING
    if submitted:
        if full_name and phone and email:
            st.balloons()
            st.success(f"""
            ✅ **Booking Confirmed Successfully!**
            
            **🏨 Hotel:** {selected_hotel}
            **👤 Guest:** {full_name}
            **📱 Phone:** {phone}
            **💰 Total:** ₹{total_amount:,}
            **📅 Check-in:** {checkin_date}
            
            💜 **Payment link sent to PhonePe!**
            """)
            st.markdown("[🔗 Open PhonePe App](https://www.phonepe.com/)", unsafe_allow_html=True)
            st.balloons()
        else:
            st.error("⚠️ Please fill all required fields (*)")

    if call_booked:
        st.info("📲 **Connecting you to +91 98765 43210** (Our 24/7 Luxury Concierge)")

# --- HOTEL STATS (If no hotel selected) ---
else:
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("🏨 Total Hotels", len(df))
    with col2: st.metric("📍 Regions", len(df['region'].unique()))
    with col3: st.metric("⭐ Average Rating", "4.8/5")
    with col4: st.metric("💰 Starting", "₹5,200")

# --- PERFECT NAVIGATION BAR ---
st.markdown("---")
st.markdown("<div style='text-align: center; padding: 2rem; background: rgba(255,255,255,0.9); border-radius: 25px; margin: 2rem 0;'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🏠 Home", key="nav_home", help="Back to homepage", use_container_width=True, type="secondary"):
        go_to_home()

with col2:
    if st.button("🏨 Browse Hotels", key="nav_hotels", help="Explore all properties", use_container_width=True):
        go_to_hotels()

with col3:
    if st.button("🔄 New Booking", key="nav_new", help="Start fresh booking", use_container_width=True):
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# --- TRUST BADGES ---
st.markdown("""
<div style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); 
            padding: 2rem; border-radius: 20px; text-align: center; margin-top: 3rem;">
    <h3 style="color: #5f259f;">🔒 Trusted by Thousands</h3>
    <p>✅ PhonePe Secure Payments | ✅ Instant Confirmation | ✅ 24/7 Support</p>
</div>
""", unsafe_allow_html=True)

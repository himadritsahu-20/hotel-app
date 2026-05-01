import streamlit as st
from hotels_data import df

st.set_page_config(page_title="Booking | H&H Luxury", layout="wide")

# BOOKING PAGE CSS (Elegant White/Gold)
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background: linear-gradient(135deg, #fff8e1 0%, #fff3cd 100%) !important; }
    .booking-header { 
        background: linear-gradient(135deg, #ffd700, #ffed4e); 
        padding: 3rem; 
        border-radius: 25px; 
        text-align: center; 
        color: #1a1a1a; 
        box-shadow: 0 20px 50px rgba(255,215,0,0.3);
    }
    .form-section { 
        background: white; 
        border-radius: 20px; 
        padding: 2.5rem; 
        box-shadow: 0 15px 40px rgba(0,0,0,0.1); 
        border-top: 5px solid #5f259f;
    }
    .stTextInput > div > div > input, .stNumberInput > div > div > input {
        border-radius: 15px !important; 
        border: 2px solid #e9ecef !important; 
        padding: 15px !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #5f259f, #7b33cc) !important;
        color: white !important;
        border-radius: 25px !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        padding: 15px !important;
        box-shadow: 0 15px 35px rgba(95,37,159,0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='booking-header'><h1>💳 Secure Booking</h1><p>Complete your luxury stay reservation</p></div>", unsafe_allow_html=True)

# HOTEL SELECTION
st.markdown('<div class="form-section">', unsafe_allow_html=True)
st.markdown("### 🏨 Select Your Hotel")
selected_hotel = st.selectbox("Choose property", df['name'].tolist())

if selected_hotel:
    hotel_details = df[df['name'] == selected_hotel].iloc[0]
    
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("⭐ Rating", "4.8/5")
    with col2: st.metric("💰 Price/Night", f"₹{hotel_details['price']:,}")
    with col3: st.metric("📍 Region", hotel_details['region'])
    
    st.markdown(f"**✨ Featured:** {hotel_details['amenity_name']}")

# BOOKING FORM
st.markdown("### 📋 Guest Details")
with st.form("booking_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Full Name *")
        email = st.text_input("📧 Email *")
    with col2:
        phone = st.text_input("📱 PhonePe Number *")
        nights = st.number_input("🛏️ Nights", min_value=1, max_value=30, value=2)
    
    if selected_hotel:
        total = hotel_details['price'] * nights
        st.markdown(f"### 💰 **Total Amount: ₹{total:,}**")
    
    col1, col2 = st.columns(2)
    with col1:
        submitted = st.form_submit_button("🚀 Confirm & Pay with PhonePe", use_container_width=True)
    with col2:
        if st.form_submit_button("📞 Call to Book", use_container_width=True):
            st.info("📲 Calling +91 98765 43210...")

if submitted:
    if name and phone and selected_hotel:
        st.balloons()
        st.success(f"✅ **Booking Confirmed!**\n\n**Hotel:** {selected_hotel}\n**Total:** ₹{total:,}\n**Check PhonePe for payment**")
        st.markdown("[🔗 Open PhonePe](https://www.phonepe.com/)", unsafe_allow_html=True)
    else:
        st.error("⚠️ Please fill all required fields")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
if st.button("🏨 Browse Hotels", use_container_width=True):
    st.switch_page("pages/1_Hotels.py")
if st.button("🏠 Home", use_container_width=True):
    st.switch_page("app.py")

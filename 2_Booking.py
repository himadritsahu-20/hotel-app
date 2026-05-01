import streamlit as st
from hotels_data import df

# Set session state
st.session_state.current_page = "booking"

st.set_page_config(page_title="Booking | H&H Luxury", layout="wide")

# BOOKING CSS (Same as before)
# ... [booking CSS same as previous] ...

# BOOKING FORM (Same as before)
# ... [booking form same as previous] ...

# FIXED NAVIGATION
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_page = "home"
        st.switch_page("app.py")
with col2:
    if st.button("🏨 Hotels", use_container_width=True):
        st.session_state.current_page = "hotels"
        st.switch_page("pages/1_Hotels.py")
with col3:
    st.empty()

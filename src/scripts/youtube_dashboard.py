import streamlit as st
from youtube_metrics import get_channel_stats
from stripe_integration import get_stripe_revenue

# Fetch channel statistics
stats = get_channel_stats()

# Fetch Stripe revenue metrics
revenue = get_stripe_revenue()

# Streamlit app layout
st.title('YouTube Channel Dashboard')

st.header(f'Metrics for Chuckle Central')
st.metric('Subscribers', stats['subscriberCount'])
st.metric('Views', stats['viewCount'])
st.metric('Videos', stats['videoCount'])

st.header('Revenue Metrics')
st.metric('Available Balance', f"${revenue['available'][0]['amount']/100:.2f}")

import stripe
from config import STRIPE_API_KEY

# Initialize Stripe API
stripe.api_key = STRIPE_API_KEY

# Function to get Stripe revenue metrics
def get_stripe_revenue():
    balance = stripe.Balance.retrieve()
    return balance

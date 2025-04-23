# This is a very basic Flask backend simulation.
# It does NOT include database integration, user authentication, or full messaging.
# Its purpose is to show the structure of a backend that could interact with the front-end.

from flask import Flask, request, jsonify
from flask_cors import CORS # Needed to allow the front-end to make requests

app = Flask(__name__)
CORS(app) # Enable CORS for development

# In a real application, this would be a database
# We'll use a simple list to simulate data storage in memory
listings_data = []

# --- API Endpoints (Simulated) ---

@app.route('/')
def index():
    """Basic route to confirm the backend is running."""
    return "Romantic Listings Backend Simulation is running!"

@app.route('/api/listings', methods=['GET'])
def get_listings():
    """Simulates fetching all listings."""
    # In a real app, this would query the database
    return jsonify(listings_data)

@app.route('/api/listings', methods=['POST'])
def create_listing():
    """Simulates creating a new listing."""
    # In a real app, you would validate data and save to a database
    new_listing = request.json # Get data sent from the front-end
    listings_data.append(new_listing) # Add to our simulated storage
    return jsonify({"message": "Listing created successfully (simulated)", "listing": new_listing}), 201 # Return 201 Created

@app.route('/api/listings/<int:listing_id>', methods=['GET'])
def get_listing(listing_id):
    """Simulates fetching a single listing by ID."""
    # In a real app, this would query the database by ID
    if 0 <= listing_id < len(listings_data):
        return jsonify(listings_data[listing_id])
    else:
        return jsonify({"message": "Listing not found (simulated)"}), 404 # Return 404 Not Found

# --- Simulated Messaging Endpoint (Placeholder) ---
@app.route('/api/message', methods=['POST'])
def send_message():
    """Simulates sending a message."""
    message_data = request.json
    # In a real app, this would save the message to a database
    # and potentially notify the recipient.
    print(f"Simulated Message Received: {message_data}") # Print to console
    return jsonify({"message": "Message sent successfully (simulated)"}), 200


# --- User/Profile Endpoints (Placeholders) ---
@app.route('/api/profile/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    """Simulates fetching a user profile."""
    # In a real app, this would fetch user data from the database
    return jsonify({"message": f"Profile for user {user_id} (simulated)"})

@app.route('/api/profile/<int:user_id>/listings', methods=['GET'])
def get_user_listings(user_id):
     """Simulates fetching listings for a specific user."""
     # In a real app, this would query the database for listings by user ID
     return jsonify({"message": f"Listings for user {user_id} (simulated)", "listings": []}) # Return empty list for simulation


if __name__ == '__main__':
    # In a production environment, a production-ready server like Gunicorn would be used.
    # For local simulation, we can run Flask's built-in server.
    # Debug=True should NOT be used in production.
    app.run(debug=True)

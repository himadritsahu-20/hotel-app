import pandas as pd

hotels_data = [
    # GOA
    {"name": "H&H Signature Baga", "region": "Goa", "price": 8500, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Beachfront Infinity Pool"},
    {"name": "Taj Exotica Palolem", "region": "Goa", "price": 12500, "amenity_img": "https://images.unsplash.com/photo-1578631615436-393305d0edef?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Private Golden Beach"},
    
    # RAJASTHAN
    {"name": "Oberoi Udaivilas", "region": "Rajasthan", "price": 28500, "amenity_img": "https://images.unsplash.com/photo-1583736913811-86d4f318425b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Lake Pichola Palace"},
    {"name": "Taj Lake Palace", "region": "Rajasthan", "price": 32000, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Floating Marble Spa"},
    
    # KERALA
    {"name": "Taj Kumarakom Resort", "region": "Kerala", "price": 14200, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Backwater Houseboats"},
    {"name": "The Zuri Munnar", "region": "Kerala", "price": 7600, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Tea Estate Infinity Pool"},
    
    # HIMACHAL PRADESH
    {"name": "The Grand Manali", "region": "Himachal Pradesh", "price": 6200, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Snow Mountain Spa"},
    {"name": "Taj Theog Resort", "region": "Himachal Pradesh", "price": 8900, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Pine Forest Villas"},
    
    # UTTARAKHAND
    {"name": "Ananda Himalayas", "region": "Uttarakhand", "price": 28500, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Yoga Retreat Palace"},
    {"name": "Taj Corbett Resort", "region": "Uttarakhand", "price": 15600, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Tiger Safari Decks"},
    
    # MAHARASHTRA
    {"name": "JW Marriott Mumbai", "region": "Maharashtra", "price": 13500, "amenity_img": "https://images.unsplash.com/photo-1564507592333-cdd505798f28?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Arabian Sea Infinity Pool"},
    {"name": "Taj Lands End", "region": "Maharashtra", "price": 11800, "amenity_img": "https://images.unsplash.com/photo-1578631615436-393305d0edef?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Bandra Bandstand Views"},
    
    # TAMIL NADU
    {"name": "ITC Grand Chola", "region": "Tamil Nadu", "price": 11200, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Chola Dynasty Spa"},
    {"name": "Taj Coromandel", "region": "Tamil Nadu", "price": 9800, "amenity_img": "https://images.unsplash.com/photo-1551524168-b1ce9215d853?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Marina Beach Club"},
    
    # KARNATAKA
    {"name": "Taj West End Bengaluru", "region": "Karnataka", "price": 13200, "amenity_img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Banyan Tree Gardens"},
    {"name": "The Oberoi Bengaluru", "region": "Karnataka", "price": 16800, "amenity_img": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Silicon Valley Spa"},
    
    # ANDHRA PRADESH
    {"name": "Novotel Visakhapatnam", "region": "Andhra Pradesh", "price": 7200, "amenity_img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Bay of Bengal Beach"},
    {"name": "Taj Deccan Hyderabad", "region": "Andhra Pradesh", "price": 12400, "amenity_img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Golconda Fort Views"},
    
    # GUJARAT
    {"name": "Taj Skyline Ahmedabad", "region": "Gujarat", "price": 10800, "amenity_img": "https://images.unsplash.com/photo-1564507592333-cdd505798f28?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Sabarmati Riverfront"},
    {"name": "The Gateway Vadodara", "region": "Gujarat", "price": 6800, "amenity_img": "https://images.unsplash.com/photo-1571883928745-f86d233dd7e9?auto=format&fit=crop&w=1200&q=80", "amenity_name": "Laxmi Vilas Palace"}
]

df = pd.DataFrame(hotels_data)

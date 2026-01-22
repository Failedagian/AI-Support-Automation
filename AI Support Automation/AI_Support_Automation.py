import pandas as pd

# trial Sample tickets
data = {
    "TicketID": [1,2,3,4,5],
    "CustomerName": ["John", "Sarah", "Mike", "Anna", "Tom"],
    "Query": [
        "I can't reset my password",
        "My booking isn’t showing up",
        "How do I cancel my reservation",
        "I want to change my booking date",
        "App keeps crashing when I log in"
    ]
}

tickets = pd.DataFrame(data)
tickets.to_csv("tickets.csv", index=False)

# Auto-response function
def auto_response(query):
    query = query.lower()
    if "password" in query:
        return "Please reset your password using 'Forgot Password'."
    elif "booking" in query:
        return "Please check your booking details in your account."
    elif "cancel" in query:
        return "You can cancel your reservation via your account settings."
    elif "crash" in query:
        return "Try reinstalling the app and logging in again."
    else:
        return "Our support team will contact you shortly."

# Apply responses
tickets['Response'] = tickets['Query'].apply(auto_response)

# Save updated CSV
tickets.to_csv("tickets_with_responses.csv", index=False)

print(tickets)

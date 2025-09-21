from google import genai

def generate_plan(date_range, theme, location, budget):
    client = genai.Client(vertexai=True, api_key="AQ.Ab8RN6KFLPV-DPjyonsuIOGKrLUy45wugqyfDB_A0uM9_TwH4Q")

    model = "gemini-2.5-flash"
    response = client.models.generate_content(
        model=model,
        contents=f"""
                Generate a travel plan for a trip to {location} from {date_range[0]} to {date_range[1]}. The theme of the trip is {theme} and the maximum budget is INR{budget}.
                Provide a day-by-day itinerary with activities, dining options, and accommodation suggestions.
                Provide the details of accommodation, travel (flight/train/bus) in table. Explain the day by day itinerary later in points.

                Start your reply with a tabular summary of all travel and hotel bookings. If multiple bookings are needed, list them all in the table.
                Preferably start with travel booking and then show hotel booking. In a table format.

                Format the response in markdown for easy readability on frontend.
            """
    )
    
    response_text = response.text

    return response_text
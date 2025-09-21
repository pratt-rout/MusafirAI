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
                Table could include the following columns: [Type, Travel Details, Date, Details, Cost (INR), Booking Link], where --
                - Type: Flight/Train/Bus/Hotel/Cab/Activity
                - Travel Details: For travel bookings, include departure and arrival locations. For hotel bookings, include the hotel name.
                - Date: Date of travel or hotel check-in/check-out.
                Keep the steps in this booking table sequential as per your itinerary. 
                Example - Starting flight will come first, then hotel, then next travel, then next hotel and so on. Ideally it should end with final return travel booking. 
                Above example is just for understanding, you dont need to follow it strictly in your response. 

                In the itinerary, Whenever there is activities involving travel, provide a link named BOOK HERE for booking the travel. Add a dummy link as directed below --
                    - If its a flight booking use --    [BOOK HERE](https://www.easemytrip.com/flights.html)
                    - If its a train booking use --     [BOOK HERE](https://www.easemytrip.com/railways/)
                    - If its a bus booking use --       [BOOK HERE](https://www.easemytrip.com/bus/)
                    - If its a cab booking use --       [BOOK HERE](https://www.easemytrip.com/cabs/)
                    - If its a activity booking use --  [BOOK HERE](https://www.easemytrip.com/activities/)

                Format the response in markdown for easy readability on frontend.
            """
    )
    
    response_text = response.text

    return response_text
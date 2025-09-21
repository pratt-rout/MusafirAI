from google import genai
import os
import streamlit as st 

# load_dotenv()
# os.environ["GOOGLE_API_KEY"] = st.secrets.google.GOOGLE_API_KEY

def generate_plan(date_range, theme, start_location, end_location, budget, special_request):
    client = genai.Client(vertexai=True, api_key=st.secrets.google.GOOGLE_API_KEY)

    model = "gemini-2.5-pro"
    response = client.models.generate_content(
        model=model,
        contents=f"""
            Generate a travel plan for a trip from {start_location} to {end_location} from {date_range[0]} to {date_range[1]}. The theme of the trip is {theme} and the maximum budget is INR{budget}. 
            Also try to accommodate the user's special requests: {special_request}.
            
            If you feel like the max budget and time is too low for the trip, you can increase them as per requirement. Mention them in bold at the start.

            Provide a day-by-day itinerary with activities, dining options, and accommodation suggestions.
            Provide the details of accommodation, travel (flight/train/bus) in table. Explain the day by day itinerary later in points.

            Start your reply with a tabular summary of all travel and hotel bookings. If multiple bookings are needed, list them all in the table.
            Preferably start with travel booking and then show hotel booking. In a table format.
            Table could include the following columns: [Type, Travel Details, Date, Details, Cost (INR), Booking Link], where ---
            - Type: Flight/Train/Bus/Hotel/Cab/Activity. Since Flight and Hotel are major expenses, show them in bold-caps.
            - Travel Details: For travel bookings, include departure and arrival locations. For hotel bookings, include the hotel name.
            - Date: Date of travel or hotel check-in/check-out.
            Keep the steps in this booking table sequential as per your itinerary. 
            Example - Starting flight will come first, then hotel, then next travel, then next hotel and so on. Ideally it should end with final return travel booking. 
            If you are adding additional costs in a separate row, mention it in the 'Type' column as 'Miscellaneous'.
            Expenses for formalities which should be ideally be done before the trip (like visa, insurance etc)can be labeled as 'Miscellaneous' as well. 
            Show these expenses at top of the table , since it should be done before the trip starts. 
            Show final return flight towards the end of the table.
            Show Local Transport on the dates whenever its required. Do not club them towards the end.
            Whenever you are mentioning any travel spot, show google link for that spot. Do not do it in the table, do it in the itinerary section. 
            Use it in markdown format. Eg - [Location_Name](https://www.google.com/maps/search/?api=1&query=Location_Name)

            For visa application, if you have some valid links, you can provide them as well. Eg - [Visa Application](https://visa.vfsglobal.com/ind/en/ita/)

            Above example is just for understanding, you dont need to follow it strictly in your response. 

            In the itinerary, Whenever there is activities involving travel, provide a link named BOOK HERE for booking the travel. Add a dummy link as directed below --
                - If its a flight booking use --    [BOOK HERE](https://www.easemytrip.com/flights.html)
                - If its a train booking use --     [BOOK HERE](https://www.easemytrip.com/railways/)
                - If its a bus booking use --       [BOOK HERE](https://www.easemytrip.com/bus/)
                - If its a cab booking use --       [BOOK HERE](https://www.easemytrip.com/cabs/)
                - If its a activity booking use --  [BOOK HERE](https://www.easemytrip.com/activities/)

            Format the response in markdown for easy readability on frontend. 
            
            """
            # For each day of itinerary, create dropdown sections for better readability. Every day should have its own dropdown section.
    )
    
    response_text = response.text

    return response_text
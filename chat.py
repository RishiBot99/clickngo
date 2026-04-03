from gpiozero import Button
from google import genai

client = genai.Client(api_key="AIzaSyBxViXTTyfdghRZa-kBFaKlt6JplvgPdVo")
blue = Button(17)
yellow = Button(27)
green = Button(23)
red = Button(22)

while True: 
    try: 
        if not blue.is_pressed:
            print("Blue button pressed")
            response = client.models.generate_content(
                model = "gemini-2.5-flash-lite", 
                contents = "What are good vacation spots in 2 weeks in the United States? Keep the response short to 1 or 2 sentances and do not ask follow up questions" ,                
            )
            print(response.text)
        if not yellow.is_pressed:
            print("Yellow button pressed")
            response = client.models.generate_content(
                model = "gemini-2.5-flash-lite", 
                contents = "What is traffic like today in Lawrence KS? Keep the response short to 1 or 2 sentances and do not ask follow up questions" ,                
            )
            print(response.text)
        if not green.is_pressed:
            print("Green button pressed")
            response = client.models.generate_content(
                model = "gemini-2.5-flash-lite", 
                contents = "What are good breakfast places near me in Lawrence KS Keep the response short to 1 or 2 sentances and do not ask follow up questions" ,                
            )
            print(response.text)
        if not red.is_pressed:
            print("Red button pressed")
            response = client.models.generate_content(
                model = "gemini-2.5-flash-lite", 
                contents = "What are some good motivational and inspirational quotes to improve my day?Keep the response short to 1 or 2 sentances and do not ask follow up questions" ,                
            )
            print(response.text)
    except KeyboardInterrupt:
         print("\nExiting......")
         break
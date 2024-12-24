import requests

API_KEY = 'VqcdzP2y0qFebjCJQHstclChaaVR4699e1K97JbQ'

def get_nutritional_info(food_name):
    """
    Fetches the nutritional information for a given food item from the USDA API.
    :param food_name: The name of the food item to get nutritional information for.
    :return: A dictionary with nutrient names as keys and their values and units as values.
    """
    base_url = 'https://api.nal.usda.gov/fdc/v1/foods/search'

    params = {
        'query': food_name,
        'api_key': API_KEY
    }

    response = requests.get(base_url, params=params)

    # Print out the raw response to debug the issue
    if response.status_code == 200:
        data = response.json()

        if 'foods' in data and len(data['foods']) > 0:
            food_item = data['foods'][0]

            nutrients = food_item.get('foodNutrients', [])
            nutrient_data = {}
            
            # Extracting and formatting the nutrient information
            for nutrient in nutrients:
                nutrient_name = nutrient['nutrientName']
                nutrient_value = nutrient['value']
                nutrient_unit = nutrient.get('unitName', 'N/A')  # Default to 'N/A' if no unit found
                
                # Add the nutrient value and unit to the dictionary
                nutrient_data[nutrient_name] = f"{nutrient_value} {nutrient_unit}"

            # Format the data to return it as a clean dictionary
            formatted_data = {}
            for nutrient, value in nutrient_data.items():
                formatted_data[nutrient] = value

            return formatted_data
        else:
            print(f"Error: Unable to retrieve data for {food_name}. No food found.")
            return None
    else:
        print(f"Error: Unable to retrieve data for {food_name}, status code {response.status_code}")
        return None
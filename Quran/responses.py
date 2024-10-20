import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')
def fetch_quran_verse(query):
    api_url = f"http://api.alquran.cloud/v1/ayah/{query}/en.asad"
    try:
        print(f"Fetching from API: {api_url}")
        response = requests.get(api_url)
        print(f"API response status: {response.status_code}")
        print(f"API response content: {response.text}")
        if response.status_code != 200:
            print(f"Error with API request: {response.text}")
            return "Error with the API request."
        data = response.json()
        print(f"API response data: {data}")
        if data['status'] == "OK":
            ayah_text = data['data']['text']
            surah_name = data['data']['surah']['englishName']
            ayah_number = data['data']['numberInSurah']
            response_message = (f"**Surah {surah_name} (Ayah {ayah_number})**\n"f"{ayah_text}\n\n")
            return response_message
        else:
            return "Couldn't find the requested Ayah. Please use the format: <surah>:<ayah>."
    except requests.RequestException as e:
        print(f"Request error occurred: {e}")
        return "An error occurred while fetching the Ayah."
    except Exception as e:
        print(f"General error occurred: {e}")
        return "An error occurred while processing the request."
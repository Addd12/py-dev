import requests

def fetch_api_data(api_url):
    #1a fetch data from the given api
    try:
        request_data = requests.get(api_url)
        #print(request_data.json())
        return request_data.json()
    except Exception as exception:
        print(f"The data could not be fetched as a result of {exception}")
        return None

api_url = 'https://jsonplaceholder.typicode.com/todos'
fetch_api_data(api_url)
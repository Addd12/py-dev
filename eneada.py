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

#2a extract titles from the api data, that contain a specific string
def extract_titles(api_data):
    print("----------------Extracting data using the first method-----------------------")
    specific_str = input("Please type the string you want to find in the title (ex. qui, aut, porro): ")
    titles = []
    print(f"List of titles that contain {specific_str}: ")
    for item in api_data:
        #get only the items that contain a specific string
        if specific_str in item['title']:
            print(item['title'])
            #then store them in a list
            titles.append(item['title'])
    return titles

#2b extract titles from the api data, that contain a specific string using list comprehension
def extract_titles_using_list_comp(api_data):
    print("\n----------------Extracting data using list comprehension method-----------------------")
    specific_str = input("Please type the string you want to find in the title (ex. qui, aut, porro): ")
    print(f"List of titles that contain {specific_str}, extracted using list comprehension: ")

    titles = [item['title'] for item in api_data if specific_str in item['title']]
    for title in titles:
        print(title)

    return titles


api_url = 'https://jsonplaceholder.typicode.com/todos'
fetched_data = fetch_api_data(api_url)
#print(type(fetched_data))
extract_titles(fetched_data)

extract_titles_using_list_comp(fetched_data)
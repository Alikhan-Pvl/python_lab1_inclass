
import requests

post_id = 1
x=requests.get(f'https://jsonplaceholder.typicode.com/todos/{post_id}')
print (x.status_code)

if 400 <= x.status_code <= 499 or 500 <= x.status_code <= 599:
    print(f"Error: {x.status_code}")
    print(x.text)


print(x.json())


class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed


new_todo_object = ToDo(userId=1, id=1, title="Sample Todo", completed=False)


new_todo_payload = {
    "userId": new_todo_object.userId,
    "title": new_todo_object.title,
    "completed": new_todo_object.completed
}

post_response = requests.post('https://jsonplaceholder.typicode.com/todos', json=new_todo_payload)


print("\nPOST Response Content:")
print(post_response.json())


if post_response.status_code >= 400:
    print(f"Error: {post_response.status_code} - {post_response.text}")


new_todo_object.title = "Updated Todo"
new_todo_object.completed = True


updated_todo_payload = {
    "userId": new_todo_object.userId,
    "title": new_todo_object.title,
    "completed": new_todo_object.completed
}

chosen_id = 1  # replace with the actual ID you want to update
put_response = requests.put(f'https://jsonplaceholder.typicode.com/todos/{chosen_id}', json=updated_todo_payload)

# Print response content
print("\nPUT Response Content:")
print(put_response.json())

# Check status code and print error message if applicable
if put_response.status_code >= 400:
    print(f"Error: {put_response.status_code} - {put_response.text}")











#task 2
import requests
import random

character_id = random.randint(1, 826)
character_url = f'https://rickandmortyapi.com/api/character/{character_id}'
character_response = requests.get(character_url).json()


# Print JSON response
print("JSON Response:")
print(character_response)

# Display keys of the JSON structure
print("\nKeys of JSON Structure:")
print(character_response.keys())


import json

# Save JSON response to a file
filename = f'info_character_{character_id}.json'
with open(filename, 'w') as file:
    json.dump(character_response, file)

# Get episode URLs from the "episode" key
episode_urls = character_response['episode']

# Extract episode IDs from URLs
episode_ids = [int(url.split('/')[-1]) for url in episode_urls]

# Create a file and append each episode URL using a loop (APPEND MODE)
with open(f'all_episodes_with_character_{character_id}.txt', 'a') as file:
    for url in episode_urls:
        file.write(url + '\n')

episode_url = 'https://rickandmortyapi.com/api/episode/1'
episode_response = requests.get(episode_url).json()

# Analyze response structure
print("Episode Response Structure:")
print(episode_response.keys())

# In a separate file named episode.py
class Episode:
    def __init__(self, id, name, air_date, episode, characters, url):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        def display_info(self):
            print(f"Episode ID: {self.id}")
            print(f"Name: {self.name}")
            print(f"Air Date: {self.air_date}")
            print(f"Episode Code: {self.episode}")
            print(f"Characters: {len(self.characters)}")




# Iterate each episode from the list and make requests
episode_objects = []
for episode_id in episode_ids:
    episode_url = f'https://rickandmortyapi.com/api/episode/{episode_id}'
    episode_data = requests.get(episode_url).json()
    episode_objects.append(Episode(**episode_data))


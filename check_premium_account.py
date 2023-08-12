import requests

def check_premium_account(request):
    
    # Step 1: Get player information from Tibia API
    def get_account_status(player_name):
        print(f"Fetching data for player: {player_name}")  # Debug print
        url = f"https://api.tibiadata.com/v3/character/{player_name}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error {response.status_code}: Failed to fetch data for {player_name}.")
            print(response.json().get("message", ""))
            return None

        data = response.json()
        account_status = data["characters"]["character"]["account_status"]
        return account_status

    # Step 2: Send message to Discord if account status is "Premium"
    def send_discord_message(message):
        webhook_url = "https://discord.com/api/webhooks/1139703557021511810/RljK_C44NA4ArHfKZZgxOAMZxMuwhqQDZ-bUSFYKsPvx1UnAIqt6TA3Y4hZ56V1n7bJ2"
        payload = {
            "content": message
        }
        response = requests.post(webhook_url, json=payload)
        print(f"Discord Response Status: {response.status_code}")
        print(f"Discord Response Body: {response.text}")
        return response.status_code

    player_name = "Bonezawz"
    account_status = get_account_status(player_name)

    if account_status is None:
        message = "Could not fetch account status."
    elif account_status == "Premium Account":
        send_discord_message(f"@everyone {player_name} has a premium account! ")
        message = f"{player_name} has a premium account!"
    else:
        message = f"{player_name} has a {account_status}."

    return message, 200

# Import libraries
from telebot import TeleBot
import requests
import json
from sseclient import SSEClient

# Replace with your Telegram bot t
CONVERSATION_ID = 'enter conversation id here'
COOKIES = 'Enter cookie here'
YOUR_BOT_TOKEN = "enter bot token here"

# Create a TeleBot object with your token
bot = TeleBot(YOUR_BOT_TOKEN)

def send_message(session, text, CONVERSATION_ID, COOKIES ):
    """Send a message to the AI and handle the response stream."""
    url = 'https://pi.ai/api/chat'
    payload = {
        "text": text,
        "conversation": CONVERSATION_ID
    }
    payload_str = json.dumps(payload)  # Serialize the payload to a JSON string
    content_length = str(len(payload_str.encode('utf-8')))  # Calculate the content length

    headers = {
        'Accept': 'text/event-stream',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'Content-Length': content_length,
        'Cookie': COOKIES,  # Pass cookies as a parameter
        'Origin': 'https://pi.ai',
        'Referer': 'https://pi.ai/talk',
        'Sec-Ch-Ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'X-Api-Version': '3'
    }

    response = session.post(url, headers=headers, data=payload_str, stream=True)
    return response

def handle_response(response, chat_id):
    """Process the SSE stream and extract AI responses."""
    client = SSEClient(response)
    all_data = []
    for event in client.events():
        all_data.append(event.data)  # Collect all data first

    # Now process the collected data
    message_buffer = ""
    for data in all_data:
        parsed_data = json.loads(data)
        if 'text' in parsed_data:
            message_buffer += parsed_data['text']

    if message_buffer:
        bot.send_message(chat_id, message_buffer)

# Function to handle incoming messages
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Get the user's message text
    user_message = message.text
    # Send user message to AI
    session = requests.Session()
    response = send_message(session, user_message, CONVERSATION_ID, COOKIES)

    if response.ok:
        handle_response(response, message.chat.id)
        bot.send_chat_action(message.chat.id, 'typing')
    else:
        bot.send_message(message.chat.id, 'Failed to send message to AI.')

# Start polling for incoming messages
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()

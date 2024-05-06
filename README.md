# Pi_AI_telegram_bot
Chat with PI your friendly AI via telegram
# Pi-AI-python-client
this is a python script that allows you to chat with Pi ai from https://pi.ai/talk viA TELEGRAM.
**Pi**, your personal AI, is an innovative platform designed to be more than just a typical chatbot.

1. **Personal Intelligence**:
   - The name **"Pi"** stands for **"personal intelligence"**. Unlike traditional AI models, **Pi** aims to be more relatable and emotionally aware.
   - It prioritizes **conversations with people**, emphasizing empathy and understanding. Rather than just providing factual answers, **Pi** strives to be a **supportive companion**.

2. **Supportive and Conversational**:
   - **Pi** isn't solely about productivity or search queries. It's more like chatting with a **chatty friend**.
   - When you interact with **Pi**, you'll notice that it takes a moment to think before responding. This deliberate pace creates a more natural and engaging conversation.


3. **Emotional Intelligence (EQ)**:
   - **Pi** isn't just smart; it also possesses **good emotional intelligence**.
   - Whether you need advice, want to discuss something on your mind, or seek creative inspiration, **Pi** is there to listen and engage.

4. **Accessible and Available**:
   - You can find **Pi** at [this link](https://pi.ai/talk) ¹.
   - It's like having a **virtual companion**—ready to chat, offer insights, or simply be there whenever you need it.

This script enables you to interact with Pi AI via the terminal. Additionally, you can modify it to communicate with the AI in various other ways. To use this script effectively, you'll need two key pieces of information:

1. The cookies
2. The chat ID

To obtain these, you must first create an account at [Pi AI's website](https://pi.ai).

### Accessing Browser Developer Tools
Once you have made your account, open your browser's developer tools to capture the required information. Here’s how you can open the developer tools across different browsers:

#### Google Chrome
- **Windows/Linux:** Press `Ctrl + Shift + I` or `F12`. Alternatively, right-click on any page element and select "Inspect" from the context menu.
- **macOS:** Press `Cmd + Option + I`. You can also right-click on any page element and select "Inspect".

#### Mozilla Firefox
- **Windows/Linux:** Press `Ctrl + Shift + I` or `F12` to open the toolbox. For just the console, use `Ctrl + Shift + K`.
- **macOS:** Press `Cmd + Option + I` for the toolbox. For just the console, use `Cmd + Option + K`.

#### Safari
- **macOS:** First, ensure that the developer menu is enabled by going to Safari > Preferences > Advanced, and checking the box at the bottom that says "Show Develop menu in menu bar". Once enabled, you can press `Cmd + Option + I` to open the developer tools.

#### Microsoft Edge
- **Windows/Linux:** Press `F12` or `Ctrl + Shift + I`.
- **macOS:** Press `Cmd + Option + I`.

#### Opera
- **Windows/Linux:** Press `Ctrl + Shift + I` or use `Ctrl + Shift + C` to directly go into the element inspector mode.
- **macOS:** Press `Cmd + Option + I`.

### Capturing Cookies and Chat ID
After accessing the developer tools:
- Navigate to the **Network** tab.
- Send a message to the AI.
- Look for the network request named `chat`.
  
![image](https://github.com/Debronejacobs/Pi-AI-python-client/assets/167520006/ad0615b9-f071-4c39-b6f3-bb9fed57fec3)


now tap on  'chat' 

The cookies can  be found in the request headers 

![image](https://github.com/Debronejacobs/Pi-AI-python-client/assets/167520006/70d0a30c-41ed-4d78-90ee-477dca4305dd)





look for the cookie in the request header



![image](https://github.com/Debronejacobs/Pi-AI-python-client/assets/167520006/5750e5cb-fe68-4382-8303-b600290f592c)





![image](https://github.com/Debronejacobs/Pi-AI-python-client/assets/167520006/a3c4f90d-8496-473f-8458-b4345db8300c)











look for the conversation id in the payload section 






![image](https://github.com/Debronejacobs/Pi-AI-python-client/assets/167520006/a9a87dd9-a406-41be-8175-12063063f713)





now when you run the script provide the session cookie and chat id
please feel free to improve upon the script.


now fill in the cookie and chat id in the telegram bot code and enjoy chatting with PI via the terminal.








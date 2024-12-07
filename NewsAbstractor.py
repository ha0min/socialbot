#!/usr/bin/env python  
# -*- coding:utf-8 _*-


import json
import time
import openai
from pprint import pprint

from newsplease import NewsPlease
import requests


class NewsAbstractor:
    url = 'https://www.reuters.com/markets/us/biden-mccarthy-meet-us-debt-ceiling-talks-come-down-wire-2023-05-16/'
    chatbot_url = 'http://url_to_gpt/conversation'
    response_data = []
    conversation_id = ''
    parent_message_id = ''
    prompt = '''You now serve as a news copywriter. Your job is to provide unbiased news summary for our speaker to make 
    a presentation. You will be given news, which contains news published time, news content. Your job is abstract 
    one statement sentence from the news that aligns with 5W2H rule. You are not allowed to make up things that not 
    reflect from the given news, and use neutral statement to describe the news.
        Agian, You will be given news, which contains news published time, news content. 
        Use neutral statement to summary the news in one sentence.
        
        Your summary should follow the format and less than 30 words:
        At {time (hour:min)}, {your abstract statement}
        
        for every response, reply a json format following the format:
        ```
        {
        "emoji": one emoji prefix to each summary statement that best describe the news country,
        "summary": your summary
        }
        ```
        '''

    user_prompt = '''
        Sure, I can help you with that. Please provide me with the news and I will extract a summary statement 
        following the 5W2H rule and like the format below:
        {
        "emoji": "🌍",
        "summary": "At 09:45, a new international climate agreement was reached by world leaders to reduce greenhouse gas emissions."
        }
        '''

    def __init__(self):
        openai.api_key = 'your_openai_api_key'

    def news(self, url):
        print('-------------------')
        print('news() called')
        article = NewsPlease.from_url(url)
        date_publish = article.date_publish
        news_text = article.maintext
        messages = self.request_body_builder(date_publish, news_text)
        # get_chat_response = self.get_chat_response(message, self.conversation_id, self.parent_message_id)
        # news_response = self.parse_json_response(get_chat_response)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            # temperature=1,
        )
        news_response = response['choices'][0]['message']['content']
        print('news_response: ' + news_response)
        news_response = json.loads(news_response)
        self.store_response(date_publish, news_response)
        print('-------------------')

    def request_body_builder(self, date_publish, news_text):
        # if self.conversation_id == '':
        #     print('-------------------')
        #     print('conversation_id is empty')
        #     self.conversation_id = time.time().__str__()
        #     message = self.prompt
        #     get_chat_response = self.get_chat_response(message, self.conversation_id, self.parent_message_id)
        #     prompt_response = self.parse_json_response(get_chat_response)
        #     # print('prompt_response: ' + prompt_response)
        #     print('prompt send success')
        #     print('-------------------')
        messages = [{"role": "user", "content": self.prompt},
                    {"role": "assistant", "content": self.user_prompt}]
        message = 'News time: ' + str(date_publish) + '\n' + 'News content: ' + news_text
        messages.append({"role": "user", "content": message})
        return messages

    def store_response(self, date_publish, news_response):
        data = {
            'time': int(date_publish.timestamp()),
            'emoji': news_response['emoji'],
            'summary': news_response['summary'],
        }
        self.response_data.append(data)
        print('response stored successfully, so far ' + len(self.response_data).__str__() + ' responses stored')
        pass

    def parse_json_response(self, json_response):
        # if json_response has error, raise exception
        if 'error' in json_response:
            raise Exception(json_response['error'])
        self.parent_message_id = json_response['parentMessageId']
        # if json_response has no error, parse the response and return
        return json_response['response']

    def get_chat_response(self, message, conversation_id, parent_message_id):
        payload = {
            'message': message,
            'conversationId': conversation_id,
            'parentMessageId': parent_message_id,
        }
        # post with json body
        print('sending message')
        response = requests.post(self.chatbot_url, json=payload)
        if response.status_code == 200:
            # print(response.json())
            print('message sent successfully')
            return response.json()
        else:
            print('Chatbot server error')
            print(response.status_code)
            raise Exception('Chatbot server respond error')


if __name__ == '__main__':
    # news()
    news_abstractor = NewsAbstractor()
    url = [
        'https://www.reuters.com/markets/us/biden-mccarthy-meet-us-debt-ceiling-talks-come-down-wire-2023-05-16/',
        'https://www.reuters.com/world/europe/ukrainian-army-revamps-commercial-drones-attack-russian-tanks-trenches-2023-05-16/',
        'https://www.reuters.com/world/europe/what-do-we-know-about-kinzhal-russias-hypersonic-missile-2023-05-16/',
        'https://www.reuters.com/world/kremlin-cia-video-aimed-russians-says-our-special-services-are-monitoring-2023-05-16/'
    ]

    for i in range(len(url)):
        news_abstractor.news(url[i])

    sorted_data = sorted(news_abstractor.response_data, key=lambda x: x['time'])

    for item in sorted_data:
        pprint(item)

#!/usr/bin/env python
# -*- coding:utf-8 _*-


import json

from NewsAbstractor import NewsAbstractor
from TextToSpeech import TextToSpeech


class NewsTextToSpeech:
    def __init__(self):
        self.news_abstractor = NewsAbstractor()
        self.text_to_speech = TextToSpeech()

    def process_news(self, urls):
        data = []
        for url in urls:
            self.news_abstractor.news(url)
        sorted_data = sorted(self.news_abstractor.response_data, key=lambda x: x['time'])

        for item in sorted_data:
            summary = item['summary']
            name = 'summary_' + str(item['time'])
            wav_url, audio_duration = self.text_to_speech.text_to_speech(summary, name)
            data.append({
                'emoji': item['emoji'],
                'summary': summary,
                'wav_url': wav_url,
                'audio_duration': audio_duration,
            })

        filepath = './demo-v/src/video-data.json'
        with open(filepath, 'w') as f:
            json.dump(data, f)

        print('json file generated, locate at ' + filepath)

if __name__ == '__main__':
    urls = [
        'https://www.reuters.com/markets/us/biden-mccarthy-meet-us-debt-ceiling-talks-come-down-wire-2023-05-16/',
        'https://www.reuters.com/world/europe/ukrainian-army-revamps-commercial-drones-attack-russian-tanks-trenches-2023-05-16/',
        'https://www.reuters.com/world/europe/what-do-we-know-about-kinzhal-russias-hypersonic-missile-2023-05-16/',
        'https://www.reuters.com/world/kremlin-cia-video-aimed-russians-says-our-special-services-are-monitoring-2023-05-16/'
    ]

    news_tts = NewsTextToSpeech()
    news_tts.process_news(urls)

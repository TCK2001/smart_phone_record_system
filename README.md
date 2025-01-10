# smart_phone_record_system

### motivation
Sometimes, when making many phone calls, I forget what I talked about and overlook important points. Additionally, when frequently talking with the same person, I often forget what the conversation was about. To address this issue, I developed a system that integrates `LLM` and [Google Speech-to-Text Supported Languages](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages?hl=ko) models to automatically record call logs and summarize the content using LLM to save it as a title.

The idea came from the thought that it would be great to have such a system embedded in our phones, which led me to develop it.

Example :    
<img src="https://github.com/user-attachments/assets/d56fb16a-6459-422e-ae47-3d671aa6b9ed" alt="image" width="300"/>


### Function
+ Since it uses a speech recognition model, it supports most languages worldwide.
+ By utilizing a powerful LLM and GPT-4o-mini, it significantly reduces costs while providing fast summaries of call logs in a single line.
  
### How to work ?
```python
python main.py
```
Simply enter the language you want to use, and that's it!
```python
en-US or ko-KR ...etc
```

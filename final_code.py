import json
from ibm_watson import AssistantV2,SpeechToTextV1,TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from os.path import join, dirname
from playsound import playsound

authenticator = IAMAuthenticator('pYqN3C1pQM3PdLSWPsAzfOuaLh_OBfPJLack9Mnm8_YF')
assistant = AssistantV2(
        version='2020-04-01',
        authenticator = authenticator
        )
assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/4f1e8f08-3416-4773-a53e-c4208ae518ef')

authenticator = IAMAuthenticator('3q46ytQO4ftl2pFmunP1VoNWyK-EyAjGjOhlgmkt-GOv')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator)
speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/fe05bc36-660d-4330-bc0e-bc6c9c7a53a2')

authenticator = IAMAuthenticator('wsDPlrLmNuqTX-zHJbxeUshfblaBOEB9zOGCzh4KX9Mu')
text_to_speech = TextToSpeechV1(
        authenticator=authenticator
        )
text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/6265cfe4-5ac9-4783-8da6-84ca4ea07091')

def stt(file):
    with open(join(dirname(__file__), './.', file),
              'rb') as audio_file:
        a = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/mp3',
            ).get_result()
    b=a['results'][0]['alternatives'][0]['transcript']
    return b
  
def chatbot(text):
    response = assistant.create_session(
        assistant_id='0b8b59bb-23b1-485e-9da0-f6cccbe5e053',
        ).get_result()
    a=response['session_id']
    response1 = assistant.message(
        assistant_id='0b8b59bb-23b1-485e-9da0-f6cccbe5e053',
        session_id=a,
        input={
        'message_type': 'text',
        'text': text
    }).get_result()
    return response1['output']['generic'][0]['text']

def tts(a):
    with open('output.mp3', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                a,
                voice='en-US_AllisonV3Voice',
                accept='audio/mp3'
                ).get_result().content)
    #output audio file
    playsound("output.mp3")

#give input file name here
file="hello_world.mp3"
t=stt(file)
a=chatbot(t)
tts(a)

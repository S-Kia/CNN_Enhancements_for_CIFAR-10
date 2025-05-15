# Python 2.7 compatible
# TTS

import sys
from naoqi import ALProxy

def main():
    if len(sys.argv) < 2:
        print("Usage: python say_to_nao.py <text>")
        return
    text = sys.argv[1]
    nao_ip = "172.18.16.45"
    port = 9559
    tts = ALProxy("ALTextToSpeech", nao_ip, port)
    tts.say(text)

if __name__ == "__main__":
    main()

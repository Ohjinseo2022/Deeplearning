from gtts import gTTS

test = "안녕하세요 테스트 음성입니다"

tts = gTTS(text=test, lang='ko')
tts.save(r"test.mp3")##음성으로 변환후 다운로드



import vlc
import urllib.parse as urlparse
message = urlparse.quote('Это уже даже не смещно')
p = vlc.MediaPlayer('https://tts.voicetech.yandex.net/tts?text='+message)
p.play()
message = urlparse.quote('Кошка похожа на картошку')
p = vlc.MediaPlayer('https://tts.voicetech.yandex.net/tts?text='+message)
p.play()

import pydub
from pydub import AudioSegment
from pydub.playback import play

# 사운드 파일 불러오기
sound = AudioSegment.from_file("warning_sound1.wav", format="wav")

# 좌우 채널 분리
left_channel = sound.split_to_mono()[0]
right_channel = sound.split_to_mono()[1]

# 사용자가 원하는 왼쪽/오른쪽 값 입력받기
user_left_sound=input("user_left_sound : ")
user_right_sound=input("user_right_sound : ")


left_channel=left_channel+user_left_sound
right_channel=right_channel+user_right_sound

# 합치기
adjusted_sound = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

# 출력
play(adjusted_sound)
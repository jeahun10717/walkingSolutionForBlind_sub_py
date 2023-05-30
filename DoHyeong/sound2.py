import wave
import struct
import math
import pyaudio  # PyAudio는 소리를 재생하기 위해 사용됩니다.

def play_stereo_sound(file_path, balance):
    # WAV 파일 열기
    with wave.open(file_path, 'rb') as wav_file:
        # 오디오 파일의 매개변수 얻기
        num_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()

        # 오디오 데이터 읽기
        frames = wav_file.readframes(num_frames)

    # 각 채널 데이터를 추출하여 분리
    left_channel = []
    right_channel = []
    for i in range(0, len(frames), num_channels * sample_width):
        frame = frames[i:i+num_channels * sample_width]
        channels = struct.unpack('<' + 'h'*num_channels, frame)
        left_channel.append(channels[0])
        if num_channels == 2:
            right_channel.append(channels[1])

    # 좌우 소리 조절
    left_channel_adjusted = [int(sample * (1 - balance)) for sample in left_channel]
    if num_channels == 2:
        right_channel_adjusted = [int(sample * balance) for sample in right_channel]
    else:
        right_channel_adjusted = []

    # 새로운 오디오 데이터 생성
    new_frames = []
    for i in range(num_frames):
        new_frames.append(struct.pack('<h', left_channel_adjusted[i]))
        if num_channels == 2:
            new_frames.append(struct.pack('<h', right_channel_adjusted[i]))

    # 재생을 위한 PyAudio 초기화
    p = pyaudio.PyAudio()

    # 오디오 재생 스트림 열기
    stream = p.open(format=p.get_format_from_width(sample_width),
                    channels=num_channels,
                    rate=frame_rate,
                    output=True)

    # 오디오 재생
    stream.write(b''.join(new_frames))

    # 재생 스트림과 PyAudio 종료
    stream.stop_stream()
    stream.close()
    p.terminate()

# 예시 실행
file_path = 'warning_sound1.wav'
balance = 0.8  # 좌우 소리 조절 비율 (0.0 ~ 1.0)
print("시 to the 작")
play_stereo_sound(file_path, balance)

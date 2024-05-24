from pydub import AudioSegment

# 오디오 파일 불러오기
input_file = "example_alarm_sound.mp3"  # 예시 파일 이름을 입력하세요
output_file = "example_alarm_sound_louder.mp3"

# 오디오 파일 읽기
audio = AudioSegment.from_file(input_file)

# 볼륨 높이기 (여기서는 10dB 증가)
louder_audio = audio + 10

# 볼륨 높인 파일 저장
louder_audio.export(output_file, format="mp3")

print(f"볼륨을 높인 파일이 저장되었습니다: {output_file}")


loulouder_audio = audio + 1000
loulouder_audio = audio + 1000
loulouder_audio = audio + 1000
loulouder_audio = audio + 1000
loulouder_audio = audio + 1000
louder_audio.export("example_alarm_sound_loulouder.mp3", format="mp3")
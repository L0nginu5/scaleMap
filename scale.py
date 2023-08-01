ytLink='https://youtu.be/zdUqffwLqDU'


from youtubesearchpython import *
videoInfo = Video.getInfo(ytLink)
videoTitle = videoInfo["title"]
filename = videoTitle + '.mp3'                                  #解析する音声ファイルのパス


from yt_dlp import YoutubeDL
#オプションを指定（最高音質の音声をmp3形式でダウンロードする）
option = {
    'outtmpl' : '%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  
        'preferredcodec': 'mp3',  #変換したい形式を指定
        'preferredquality': '192' #ビットレートを指定
    }]
}

#インスタンスの生成
ydl = YoutubeDL(option)

#動画一覧を取得
ydl = YoutubeDL(option)
result = ydl.download([ytLink])

print(filename)

#ライブラリインポート
import librosa                                                  #音声解析用のライブラリ

#変数定義
sampling_rate = 44100                                           #サンプリングレート


#演算
y, sr = librosa.load(path = "C:/Users/gocho/OneDrive/デスクトップ/vscodeCode/scale判定/" + filename, sr = sampling_rate)         #音声ファイルを1次元のNumPy浮動小数点配列（変数y）に格納
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)        #テンポを算出

#結果表示
print('Estimated tempo: {:.2f} beats per minute'.format(tempo)) #結果を表示



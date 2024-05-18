# AI-for-Subtitle《AI語音辨識生成字幕》
> This is for making AI with generating SRT Subtitle by four NKUST Students

這是一個字幕處理工具，分為speech to text語音轉文字生成逐字稿，以及自動化嵌入逐字稿字幕生成新影片內容，兩種主要功能。


# 前置條件

# Whisper(Speech to Text)
將附有語音的檔案轉錄成文字，執行多語言語音識別、語音翻譯和語言識別。
It can perform multilingual speech recognition, speech translation, and language identification.

1.選擇影音檔案(Choose file you want to transcribe)
《Supported formats》：
Audio:｛mkv、mp3、m4a、wav｝; 
Video:｛mov、mp4、avi、mpeg、mpga｝

2.選擇該檔案的語音語言(Choose Language what the file is)
《Supported language about 100 Countries》

3.選擇欲轉錄的語言模組(Choose Model)
《Supported Language Models》：
「tiny」
「base」
「small」
「medium」
「large-v1」、「large-v2」、「large-v3」

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

※ 注意：選取越大的語言模組，所需要的專屬記憶體也會越多
※ Selecting larger language models requires more VRAM




# SRT Embed
將SRT格式檔案嵌入影片檔案，字幕格式可自行調整。
It can embed the SRT file into a video file, and the font style can be adjusted by yourself.
Finish按鈕將正確關閉程式並退出、Back按鈕將返回Whisper頁面、Embed按鈕將彈出確認視窗，點擊Ok開啟嵌入。
The finish button can close the application 
嵌入必須為影片格式
字型樣式可以自己匯入，嵌入時若字型樣式不支援語言，則會出現嵌入結果沒有字
字型大小為pixel，根據影片比例縮放
若srt檔案格式錯誤，可能導致閃退，建議使用前面的Whisper
Ctrl+qwe






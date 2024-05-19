# AI-for-Subtitle《AI語音辨識生成字幕》
> This is for making AI with generating SRT Subtitle by four NKUST Students

這是一個字幕處理工具，分為speech to text語音轉文字生成逐字稿，以及自動化嵌入逐字稿字幕生成新影片內容，兩種主要功能。


# 前置條件  
本專案會需要安裝以下套件(※ 環境本有內附，也可以不需要特地安裝即可使用)，如果有需要使用自身本機的顧慮，依然可以自行下載  
### CUDA
```
https://pytorch.org/
```
### Torch
```  
1. git clone https://github.com/torch/distro.git ~/torch --recursive
2. cd ~/torch; bash install-deps;
3. ./install.sh
or you can use in CMD

pip install torch
```

# Whisper(Speech to Text)
將附有語音的檔案轉錄成文字，執行多語言語音識別、語音翻譯和語言識別。

It can perform multilingual speech recognition, speech translation, and language identification.
#
1.選擇影音檔案(Choose file you want to transcribe)
```
《Supported formats》：  

Audio:｛mkv、mp3、m4a、wav｝; 
Video:｛mov、mp4、avi、mpeg、mpga｝
```
2.選擇該檔案的語音語言(Choose Language what the file is)  

```《Supported language about 100 Countries》```

3.選擇欲轉錄的語言模組(Choose Model)  
```
《Supported Language Models》：  
「tiny」  
「base」  
「small」  
「medium」  
「large-v1」、「large-v2」、「large-v3」
```
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
1.將SRT格式檔案嵌入影片檔案，字幕格式可自行調整。  
It can embed the SRT file into a video file, and the font style can be adjusted by yourself.

2.Finish按鈕將正確關閉程式並退出、Back按鈕將返回Whisper頁面、Embed按鈕將彈出確認視窗，點擊ok開啟嵌入。  
The Finish button can close this application correctly, the Back button can return to the Whisper page, the Embed button will pop up a message window for a check, and clicking ok will start embed.

3.嵌入必須為影片格式。  
If you want to embed some file, the file must be a video file.

4.字型樣式可以自己匯入到font資料夾，嵌入時選擇之自行樣式需相容於SRT檔案語言。  
The font can be imported into the font folder, if you want to embed it, the font must be compatible with the language of the SRT file.

5.字幕文字大小以pixel為單位，大小將根據影片大小等比例調整。  
The size of the subtitles' characters will be proportionally adjusted according to the size of the video, measured in pixels.

6.SRT檔案可另行準備，但若SRT檔案格式不相容，可能導致錯誤閃退，建議使用上一頁Whisper功能生成之SRT。  
The SRT file can be prepared separately, but if the format of the SRT file is incompatible, might cause a crash error, so we advised using the Whisper function to generate the SRT file on the previous page.

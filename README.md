# OpenCV-Learning-forPython
OpenCVとPythonの両方を学習  
主にOpenCVの使い方を学習するためのリポジトリ  
自分用

# 最終目標
1. 野菜を撮影し、値段を割り当て、家計簿を自動作成。
2. Vtuber用の顔向き推定プログラムをC#で扱えるようにする

# 環境
* Windows10 home
* Visual Studio Code 
* Visual Studio 2019
	Cmakeを利用
* Python 3.8.3
* OpenCV 4.2.0
* dlib 19.19
* Git

dlibのインストールに手間取った  
VS2019のCmakeを使い,pipコマンドでdlibをビルドしインストールした。  
詳細はブックマークで  (後で細かく追記)  

OpenCVの補助ライブラリ?  
imutilsがインストールされていなかったので追加  
pip install --upgrade imutils 

### Anaconda不使用

多分他の人は作らないであろう特殊環境ではあるが  
学生や初心者が片手間で  OpenCVや顔の向き推定するときに  
作りやすい環境ではあると思う。  

いきなりLinux環境を用意したりDockerを覚えたりするよりも  
手元にあるwindowsPCのVSCodeのほうがよっぽど使いやすい

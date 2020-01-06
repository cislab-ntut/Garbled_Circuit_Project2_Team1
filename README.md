# Project1-2_Garbled_circuit

[Reference](https://zhuanlan.zhihu.com/p/41172002)

Truth Table
![image](https://i.imgur.com/9XtFMPJ.jpg)
![image](https://i.imgur.com/PWTLREd.png)
![image](https://i.imgur.com/tNvkuJt.jpg)


[除法](http://www.elecfans.com/baike/computer/taishiji/20100413215660.html)
![](https://i.imgur.com/Y2VWCXe.jpg)

## 步驟 ##
1.設k=2，用K-map化簡出電路</br></br>
2.為最外層（最靠近input）的所有gates randomly產生對應並替換0和1的key，打亂順序後生成Garbled truth tables</br></br>
3.每一層的gates的Garbled truth tables的輸入key值得對應關係要依據上一層gates的Garbled truth tables的輸出來決定。</br></br>
4.將所有gates的topology與Garbled truth tables作為參數傳給Server（Circuit.py)的計算function，並得到計算結果的key</br></br>
5.將得到key值與本地保存的garbled truth tables與truth tables的key值對應關係，解密得到真正結果。

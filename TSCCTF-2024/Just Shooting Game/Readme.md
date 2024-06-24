# Just Shooting Game

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/0137c941-cfd6-41f6-a329-52e6cfdff2de)

基本上這題最大的難點有兩個：
1. 取得 magic 值
2. ~~通靈出~~ Transfer.exec 是某種 bytecode interpreter ，然後把解出來的 code 丟 IDA 之類的解析。

## 解題
這題 code 用 `ILSpy` 逆會比較完整，但是這邊 writeup 還是用 Dnspy 寫。

DnSpy 打開 `ShootingGame_Data\Managed\Assembly-CSharp.dll` 會發現有一些 Class 有一個叫 `code` 的 string variable 裡面塞了一坨奇怪的東西，decode 以後會發現這些都 emoji。

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/be16b075-60a1-42c0-8587-f80b934e9ba8)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/880a248f-13de-40f2-8eeb-cfc99e405ea5)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/3cf4e779-ceb6-428a-8a60-530322d90fd1)

這些 `code` 會在該 Class 裡和一個叫 `magic` 的變數做 `Transfer.etob` 運算以後，跟一些參數一起跑 `Transfer.exec` 

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/e19af70d-a9c9-4e8e-a955-aa58db05ad20)

通過與 `gun`、`enemy` 等等 Class 比對後，發現 `GameManager` 是送入一個字串 Call `Transfer.exec` 以後會依據 Call 完後所得到的 value variable 轉成 Boolean 並判斷如果為 True 就把 `supermode` 設為 True，觀察 `gun` class 會發現 `supermode` 會讓玩家進入無敵狀態並沒有攻擊速度限制，應該是一個打入作弊代碼會開啟作弊模式的東西。其他 Call `Transfer.exec` 的地方都是在做字串比對，可以判斷 `Transfer.exec` 會依據 `code` 跟 `magic` 運算後的 byte array 做相應的事情，但是 `Transfer.exec` 到底做了甚麼還不清楚，同時因為只有 `GameManager` 不是字串比對，所以目標可能在這裡，猜測那個作弊代碼可能就是 flag。

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/b32993fd-a56a-4923-a9a8-96d1783c6da2)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/9625d27f-490a-4e3f-b838-acb916a983a8)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/e84a351d-4f57-4f20-acf1-889c1c962849)

觀察 `Transfer.etob` 以後會發現他會將輸入的字串的做 UTF32 decode 以後依照不同的 range 減掉特定的 offset 以後跟 `magic` 做 XOR，最後減掉 128512 後強轉成 byte 然後拼回 byte array 回傳。

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/40c38580-272d-409c-bdea-67a283cdbd8c)

解析 `Transfer.exec` 可以發現他的參數變數名稱有 `code`、`mem`、`sp`、`bp` 等等疑似 memory、CPU register 的東西，但是因為他太長了要猜一下，直接整個 function 丟給 chatgpt 判斷一下，我是用 GPT4，但是 GPT 3.5 也可以，只是要分段送。

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/c0f4cc85-2eb4-4785-858a-00edb41203a2)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/7009e318-4c3f-4efb-873d-239b74c0c739)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/5b56c4c4-4f0a-4186-8cd8-1ed36fd1d94d)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/45ade104-80c7-4565-90c9-0481b6c32b54)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/e95ccc23-b8a2-4aed-91f2-cdd1efe23657)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/40bc55c2-fb60-4c3b-83d0-7d1dd0b50021)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/cfeeaf1a-1b40-48f5-b188-7eaac2cedd8c)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/4539a256-65d0-4600-b50c-e036f5690b93)

可以確認這確實是某種 bytecode interpreter，這邊就可以知道 `code` 跟 `magic` 經過 `Transfer.etob` 以後會變成 bytecode 然後 `Transfer.exec` 再依據的命令執行 bytecode 的動作，首先我們要發 bytecode 弄出來，但是會發現我們沒有 `magic` 的值。

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/8f36b8af-d752-4cb1-b1ed-ecb764dd30fa)

寫過 unity 的話就會知道 `MonoBehaviour` 可以附加在 GameObject 上面，並且直接在 GameObject 上面指定 public variable 的值，這些在 build 完會存成 asset，所以需要找可以解析 unity asset 的工具。

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/890b3045-7e06-49d8-a145-10ae308e3881)

用 `AssetRipper` 解開並且 export 出來，一個一個找太慢所以直接對 export 完的資料夾下 `grep -A 2 -B 2 -r magic .`，他會把資料夾下所有檔案中含有 `magic` 字串的行跟他的上下兩行印出來，為了濾出正確的，需要觀察 `magic` 的上下兩行有沒有  `GameManager` 的其他 variable ， 會發現 `magic: 228` 上有一個叫 `m_nextLevel` 的 variable，可以判斷 `GameManager` 的 `magic` 就是 228。

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/94c57fcd-184d-4e2d-aee0-36cce9b74d05)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/813779f0-6fc8-4cc5-8329-fa976def9ce6)

用 python 寫 [unicodetoemoji.py](exploit/unicodetoemoji.py) 跟 [emojitobyte.py](exploit/emojitobyte.py) 把他解成 bytecode 並存成檔案。

接著把解出來的 bytecode 丟 Disassembler 的工具，這邊要猜一下是哪種指令集，這個 [Online-Assembler-and-Disassembler](https://shell-storm.org/online/Online-Assembler-and-Disassembler) 網站不錯用，或者直接 IDA 用 x64 解看看，我們會拿到這坨。

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/3f9e5b21-2d7e-416f-8efa-bd5c123e9ce0)

解析他可以得知，輸入的字串的位址在 `rax`，他會先把 `rax` 推到 stack 再來把比對目標也推到 stack，然後將輸入字串的每個字元依照特定順序做 `input[a] = (input[a] ^ input[b]) +- num`，最後將運算結果跟比對目標迴圈比對是否完全一樣，如果一樣就將 `rax` 設為 1，否則為 0。

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/93e326bc-0541-44b9-a70e-ab3b93515583)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/9e709fb8-ae3b-491b-b03c-ee3929e97ecb)

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/98b30c45-a201-4655-a8e0-e636272c9bc4)

因此只需要把運算反過來做，就可以得到 flag。

## exploit
```python
data = [0x545C30D14737AC30, 0x2B818E98088CED63, 0x0BAD50580945D3F0, 0x3823C33FF8E47955, 0x54018BFECBE91C93, 0x0F4B763093C586459, 0x10E088E4C7281]
data = b''.join([a.to_bytes(8, 'little') for a in data])
data = bytearray(data)

order   = [0x2f, 0x20, 0x36, 0x15, 0x24, 0x25, 0x2A, 0x17, 0x11, 0x1e, 0x0c, 0x32, 0x07, 0x04, 0x33, 0x27, 0x09, 0x02, 0x08, 0x22, 0x0f, 0x28, 0x2e, 0x31, 0x1b, 0x1f, 0x1a, 0x1c, 0x13, 0x0d, 0x0e, 0x30, 0x1d, 0x06, 0x10, 0x12, 0x2c, 0x16, 0x23, 0x35, 0x0b, 0x0a, 0x2b, 0x21, 0x34, 0x26, 0x01, 0x29, 0x18, 0x2d, 0x05, 0x14, 0x03, 0x00, 0x19]
xorwith = [0x19, 0x11, 0x12, 0x0d, 0x0e, 0x1a, 0x16, 0x03, 0x20, 0x24, 0x03, 0x09, 0x2c, 0x11, 0x35, 0x15, 0x14, 0x24, 0x2f, 0x1e, 0x05, 0x2d, 0x1d, 0x1d, 0x07, 0x02, 0x08, 0x13, 0x32, 0x0b, 0x14, 0x02, 0x2e, 0x19, 0x32, 0x28, 0x05, 0x12, 0x33, 0x24, 0x36, 0x2e, 0x1a, 0x03, 0x20, 0x03, 0x32, 0x34, 0x13, 0x17, 0x08, 0x34, 0x04, 0x0c, 0x32]
addsub  = [-0x55, 0x7, 0xc9, -0x81, 0x29, -0x4c, -0xa1, -0x6b, -0x2d, 0xe5, 0x25, -0x42, 0x1a, 0xa4, 0x50, -0xac, -0x80, 0x20, -0xff, 0xe5, 0x25, 0x2c, 0x2b, -0x2a, -0x08, -0xf2, -0x29, 0xdb, -0x4d, 0x29, 0x45, 0x75, 0x44, 0x2d, -0x67, -0x35, -0xfc, 0x6a, -0xa4, -0xa, -0x1a, -0xf0, -0xc4, 0xa6, 0x99, 0xf2, 0x7c, 0xf, -0xad, -0xfb, 0xf9, 0xfb, 0x3e, -0x30, 0x4e]

for i in range(len(order)):
    data[order[i]] = (((int(data[order[i]]) + 256*2 - addsub[i]) % 256) ^ (int(data[xorwith[i]])))

data = bytes(data)
print(data)
```

## Flag

![image](https://github.com/Jimmy01240397/My-CTF-Challenges/assets/57281249/80b09844-761e-44a0-8f09-cbf2444f41f9)

`TSC{reV3R53_4md64_45m_w17H_3m0ji_1n_T3H_NeT_5oO0O_c00L}`

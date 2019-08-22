# Cost-Sensitive
*[POLab](http://polab.imis.ncku.edu.tw/)* <br>

<br>

## :black_nib: Cost-Sensitive Binary Classiﬁcation
--------------------------------------------

### :arrow_down_small: Binary Classiﬁcation <br>
若有有一台”指紋辨識系統”
此時有兩個不同的指紋登入，一個是你(正確使用者)的指紋，另一個為他人(侵入者)的指紋
而指紋辨識系統需要判斷 當有一個指紋輸入時 該指紋為正確使用者的指紋或是侵入者的指紋 該種判斷(分類)方式即為Binary Classiﬁcation

<br>
<div align=center>
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%96.png"
width="300" height="150">
</div>
<br>

### :arrow_down_small: Performance Evaluation <br>
一般我們在績效衡量時，只要發生任何error都會给訂一個’相同’的懲罰(cost)， 而在二元分類可能的error如圖1左表的confusion matrix所示:

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%961.png " 
width="360" height="90">
圖1 
</sub>
</div>
<br>                                                                            





<br>

:bulb: __Q1  :  但難道不同的error都給同樣懲罰(cost)是合理的嗎???__ <br>     
---------------------------------------------------------------------------------------------------



                              
                         
### :arrow_down_small: Fingerprint Veriﬁcation for Supermarket  (反例1) <br>
此例子是將指紋辨識系統用於超級市場的客戶身分辨識，會將客戶分成忠誠(+1)或非忠誠(-1)的類別，並且會給予忠誠的客戶折扣 

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/cost-sensitive/blob/master/pic/%E5%9C%962.png" 
width="360" height="90">
圖2 
</sub>
</div>
<br>      

**False reject** :  忠誠客戶輸入指紋，但指紋辨識機說他是不忠誠的客戶
(此時這名忠誠的客戶可能會因沒了折扣而非常不開心，導致未來不再來這間supermarket消費)

**Flase accept** : 不忠誠客戶輸入指紋後，指紋辨識機卻說他是忠誠的客戶
(此時對於不忠誠的客戶來講反而會因為無緣無故得到折扣而更開心，反倒是supermarket會有些微的損失)

由反例1可知
以客戶的感覺來看 當指紋辨識機犯下False reject error會比犯下False accept error來的嚴重，因此可以看到圖2的右表，此時會給予較不想發生的False reject error 一個較高的懲罰(cost)10，而對角線的Cost皆為0因其分類是正確的


### :arrow_down_small: Fingerprint Veriﬁcation for CIA  (反例2) <br>
此例是將指紋辨識系統用於CIA員工登錄確認系統中，會將登入者分成CIA探員(+1)與侵入者(-1)的兩個類別此例子是將指紋辨識系統用於超級市場的客戶身分辨識，會將客戶分成忠誠(+1)或非忠誠(-1)的類別，並且會給予忠誠的客戶折扣 

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/cost-sensitive/blob/master/pic/%E5%9C%963.png" 
width="360" height="90">
圖3 
</sub>
</div>
<br>      

**False reject** : CIA探員輸入指紋想登錄系統，但指紋辨識機卻說他不是CIA探員並拒絕登錄
(此時CIA探員頂多再試一次，並感到厭煩而已)

**Flase accept** : 侵入者輸入指紋想登錄系統，而指紋辨識機竟接受此要求
(此時侵入者可以進入CIA的系統中竊取任何資料，會造成警政系統的危安危機)

由反例2可知
以客戶的感覺來看 當指紋辨識機犯下False accept error會比犯下False reject error來的嚴重，因此可以看到圖3的右表，此時會給予較不想發生的False accept error 一個較高的懲罰(cost)1000

<br>

:bulb: __A1  :  視不同的情況給予不同的error不同的懲罰(cost)較合理__ <br>     
---------------------------------------------------------------------------------------------------


@## :arrow_down_small: “Regular” Binary Classiﬁcation <br>
在機器學習裡面,有一個很重要的概念,叫做training 和 testing

training:  我們利用已有的資料來訓練模型,進而得到目標函數
testing:    把training 後的目標函數, 拿去應用在現實例子中

其中training 會得到 in-sample error  ;   testing 會得到out-sample error

舉例來說,我們想利用病人的檢查結果來預測癌症, 於是我們會先把手上有的資料拿來訓練模型(training); 之後訓練好再把它丟出來給大家拿來預測(testing)

---

然而Regular Binary Classiﬁcation 中 in-sample error與out-of-sample error的計算方式如圖4 :
<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/cost-sensitive/blob/master/pic/%E5%9C%964.png" 
width="360" height="150">
圖4 
  
  []布林向量 : 當符合括號中的條件布林向量值為1，反之則為0
</sub>
</div>
<br>  

由上述公式可知:
\
1.)利用現有的資料作訓練時，當實際值不等於預測值時布林向量為1，所以把所有不相等情況的布林值加總除上樣本數，即為In sample error的計算方式
\
2.)利用未知的資料測試目標函式是否有用時，當實際值不等於預測值時布林向量為1，所以把所有不相等情況的布林值加總，即為out-of sample error的計算方式(此時不用除N因為……?
????????????????)


@## :arrow_down_small: “Class-Weighted Cost-Sensitive” Binary Classiﬁcation <br> 
**(Class-Weighted : 不同的y 下所產生的weight是不同的)**

由Q1 到A1的過程中，可以得知加入懲罰(cost)較為合理，因此當error背後的重要性不同時，較推薦使用Class-Weighted Cost-Sensitive Binary Classiﬁcation，而其中in-sample error、out-of-sample error 的計算方法如 圖6所示:


(以下範例是以supermarket案例的cost martix 圖5做說明)
<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/cost-sensitive/blob/master/pic/%E5%9C%965.png" 
width="150" height="140">
圖5
</sub>
</div>
<br> 

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%966.png" 
width="350" height="200">
圖6 
  
     Positive class : cost=10    ；   negative class : cost=1
</sub>
</div>
<br>  

由上述公式可知:
\
1.)	supermarket案例中，當實際值不等於預測值時，會有不同的cost，因此將所有不相等情況的cost加總並除上樣本數，即為In sample error的計算方式( Eg  y=+1  h(x)=-1  ； cost = 10 )
\
2.)	supermarket案例中，利用未知的資料測試目標函式是否有用時，當實際值不等於預測值時，會有不同的cost，把所有不相等情況的cost加總，即為out-of sample error的計算方式 (此時不用除N因為……?

????????????????)


### :arrow_down_small: Class-Weighted Cost-Sensitive Binary Classiﬁcation 的通用表示如下: <br>

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%967.png" 
width="420" height="120">
圖7
  
     Positive class : cost=10    ；   negative class : cost=1
</sub>
</div>
<br>  
投入N的樣本，每個樣本為一個input Xn 及 label  Yn  
並且給予error 兩種不同的權重 W+、W- 如圖7 右表的cost matrix 所示:

---
<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%968.png" 
width="420" height="120">
圖8      
</sub>
</div>
<br>  
我們希望利用cost matrix這些額外資訊，在未知的資料得到一個很低的out-of-sample error，同時使的分類器g(x)在將所有樣本分類時可以獲得最小的cost，因而做出最佳決策
\
※Regular Binary Classiﬁcation是Class-Weighted Cost-Sensitive Binary Classiﬁcation的特例 (W+ W-為1時)



:bulb: __Q2 : 以supermarket為例，若除了忠誠及不忠誠的客戶外，還有超級忠誠的客戶，這下該如何是好?__ <br> 
---------------------------------------------------------------------------------------------------



圖9左表 同反例1，利用指紋辨識系統於超級市場的客戶身分辨識，但僅將客戶分成忠誠(+1)或非忠誠(-1)的類別，並且給予忠誠的客戶折扣，若此時有一個超級忠誠的客戶加入分類，Regular Binary Classiﬁcation與 Class-Weighted Cost-Sensitive Binary Classiﬁcation等方法較不適合，因此可以改用Example-Weighted Cost-Sensitive Binary Classiﬁcation而其核心概念為給予每個Example 個別的cost

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%969.0.png" 
width="420" height="120">
圖9      
</sub>
</div>
<br>  

***超級忠誠的客戶*** : 因極度不想遺失此類客戶，因此當發生error會給予一個絕對高的cost(100)
\
***忠誠的客戶*** : 遺失此類客戶相較於遺失超級忠誠的客戶來說較不嚴重，因此當發生error會給予一個相對高的cost (10)
\
***不忠誠的客戶*** : 此時對於不忠誠的客戶來講反而會因為無緣無故得到折扣而更開心，反倒是supermarket會有些微的損失cost(1)


:bulb: __A2 : Regular Binary Classiﬁcation與 Class-Weighted Cost-Sensitive Binary Classiﬁcation都是用不同類別來進行分類，若希望可以觀察不同example的特性來進行分類可以使用接下來要介紹的Example-Weighted Cost-Sensitive Binary Classiﬁcation__ <br>
---------------------------------------------------------------------------------------------------

### :arrow_down_small:“Example-Weighted Cost-Sensitive” Binary Classiﬁcation:  <br>

由Q2 到A2的過程中，可知若有許多不同example而不是單純的兩個類別時，觀察每個example下所可能發生的error，也就是利用各別example的特性(cost vector)進行分類較合理，經常使用Example-Weighted Cost-Sensitive Binary Classiﬁcation，而其中in-sample error、out-of-sample error 的計算方法如 圖10所示:

(以下範例是以supermarket擴充版案例的cost matrix 協助說明)
<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%969.1.png" 
width="150" height="140">      
</sub>
</div>
<br>  

---

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/cost-sensitive/blob/master/pic/%E5%9C%9610.png" 
width="360" height="150">
圖10 

</sub>
</div>
<br> 

由上述公式可知:
\
1.)在supermarket的擴充案例中，不同example會有不同的cost vector，將所有實際值不等於預測值情況下的cost(Wn)加總並除上樣本數，即為In sample error的計算方式( Eg  y=big customer  h(x)=-1  ； cost = 100 )
\
2.) 在supermarket的擴充案例中，利用未知的資料測試目標函式是否有用時，當實際值不等於預測值時，不同example會有不同的cost vector，把所有不相等情況的cost(Wn)加總，即為out-of sample error的計算方式 (此時不用除N因為……?????????????????)


### :arrow_down_small:Example-Weighted Cost-Sensitive Binary Classiﬁcation 的通用表示如下:  <br>

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/cost-sensitive/blob/master/pic/%E5%9C%9611.png" 
width="420" height="120">
圖11 

</sub>
</div>
<br> 

投入N的樣本，每個樣本為一個input Xn 及 label  Yn  
並且給予不同example 的error不同的權重 Wn 

---

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/cost-sensitive/blob/master/pic/%E5%9C%9612.png" 
width="420" height="120">
圖12 

</sub>
</div>
<br>

我們希望利用每個example的cost vector這些額外資訊，在未知的資料得到一個很低的out-of-sample error，同時使的分類器g(x)在將所有樣本分類時可以獲得最小的cost，因而做出最佳決策
\
\
※Regular Binary Classiﬁcation是Class-Weighted Cost-Sensitive Binary Classiﬁcation的特例 (W+ W-為1時)
\
\
※Class-Weighted Cost-Sensitive Binary Classiﬁcation是Example-Weighted Cost-Sensitive Binary Classiﬁcation的特例 (當只有兩個example時，且那兩個example一個為 +1類別 另一個為-1類別)


## :black_nib: Bayesian Perspective of Cost-Sensitive Binary Classiﬁcation

### :arrow_down_small:Key Idea: Conditional Probability Estimator  <br>

Bayesian Perspective of Cost-Sensitive Binary Classiﬁcation 的目標與前面介紹的分類法都一樣，希望分類器g(x)將所有未知example分類後可以得到一個最小的cost

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/cost-sensitive/blob/master/pic/%E5%9C%9613.png" 
width="420" height="90">
圖13 

</sub>
</div>
<br>

---

而其中會運用到圖14所介紹的expected error for predicting，其概念與期望值雷同

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/cost-sensitive/blob/master/pic/%E5%9C%9614.0.png" 
width="420" height="90">
圖14 

</sub>
</div>
<br>


Eg : expected error for predicting +1 on x  =  W- × P( -1 | X )

W- :因是二元分類問題，預測h(x)為+1情況下，可能發生的error其真實y類別一定為-1類別(藍色圈)

P( -1 | X ) : 真實y為-1類別，其在某個example下所可能發生的機率為P( -1 | X ) (紅色圈)

因此W- 與 P( -1 | X ) 相乘 即為expected error for predicting +1 on x

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9614.1.png" 
width="130" height="100">
</sub>
</div>
<br>

---

在Bayesian Perspective of Cost-Sensitive Binary Classiﬁcation的核心，是運用到一種Bayes optimal的分類器，如圖15所示

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9615.png" 
width="350" height="100">
圖15 
  
     Sign : 若括號中的值大於1其sign=1；反之則sign=-1 (此例直接將+1、-1當成類別) Eg : sign(156)=1 ；sign(-12)=-1
</sub>
</div>
<br>  

Bayes optimal分類器g*(x)的作法是將expected error for predicting +1 on x 與expected error for predicting -1 on x 拿來比大小，若W- × P( -1 | X )大於W+ × P( +1 | X )則將該樣本分在+1類，反之則分在-1類

---

但一般來講通常P( -1 | X )與P( +1 | X )都是未知的，所以可有用機器學習中常見的logistic regression, Naïve Bayes, ...等方法進行估計，估計後如圖?所示，可以到一個approximately good分類器g(x)

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9616.png" 
width="350" height="100">
圖16
</sub>
</div>
<br>  

若W- × p( X )大於W+ ×  (1-p( X) )則將該樣本分在+1類，反之則分在-1類

### :arrow_down_small:Key Idea: Approximate Bayes-Optimal Decision <br>

經過推倒化簡後可以得到一個用來判斷某example該分類在+1or-1類的式子如圖17所示

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9617.0.png" 
width="490" height="100">
圖17
</sub>
</div>
<br>  

<br>
<div align=center>
<sub> 
(
  <img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9617.1.png" 
width="100" height="70">超市  
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9617.2.png" 
width="100" height="70">CIA
)
</sub>
</div>
<br>  

以supermarket為例子，將w+ w-的真實值帶入公式後可以得到P(x) > 1/11 ，其意思為當某個樣本利用logistic regression, Naïve Bayes, ...等方法估計出來分類為+的機率若大於 1/(11 ) 則將其分類為+1類別

---

Approximate Bayes-Optimal Decision (ABOD) 方法的主要步驟如圖18所示 

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/cost-sensitive/blob/master/pic/%E5%9C%9618.png" 
width="420" height="100">
圖18
</sub>
</div>
<br>

Setep1
\
利用自己習慣的演算法(logistic regression, Naïve Bayes, ...)求出p(x) 、1-p(x)，並用它們估計P( -1 | X )、P( +1 |1 X )
\
Setep2
\
利用approximately good分類器g(x)進行分類，其中根據不同特性題目，分類器g(x)的門檻 (W-)/(W+ + W-) 會有所改變

### :arrow_down_small:Key Idea: ABOD on Artiﬁcial Data <br>
(利用人工資料實作 並以圖形說明 且以supermarket為例)

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9619.20.21.22.png" 
width="680" height="600">
</sub>
</div>
<br>

圖19 中的每個標記都為一個example，而其中圓圈為example分類在+1類別，叉為example分類在-1類別。接著針對每個example利用logistic regression, Naïve Bayes, ...等方法估計其應該被分類在+1 or -1 類別的機率，如圖20所示，越深藍色代表有越高的機率分在+1類別，反之則有越高的機率分在-1類別，接著會用此機率進行分類(g(x) = +1；p(x) > (W-)/(W+ + W-))。

接下來可以看到圖21為使用regular分類方法分出來的結果。圖22為利用ABOD分出來的結果，可以看到使用ABOD可以將+1類別分得更乾淨，也就是將supermarket中，將真的是忠誠客戶的example用更嚴謹的方式分類，以避免False reject error發生

### :arrow_down_small:Pros and Cons of ABOD <br>

***Pros***
\
1.)optimal : 若估計P( -1 | X )與P( +1 | X )的P( X )、1 - P( X )是準的則能夠得到一個optimal的結果
\
2.)simple : 做法簡單，在training中僅須利用logistic regression, Naïve Bayes, ...等方法估計每個樣本分在+1 or-1 類別的機率，在預測階段僅需根據不同特性的題目調整threshold( (W-)/(W+ + W-)  )

***Cons***
\
1.)	difﬁcult : 得到一個好的機率估計往往比得到一個好的二元分類器來的困難
\
2.)	restricted : 我們會需要已知的W+W-來計算threshold，因此會需要一張完整的cost matrix 表












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


### :arrow_down_small: “Regular” Binary Classiﬁcation <br>
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


### :arrow_down_small: “Class-Weighted Cost-Sensitive” Binary Classiﬁcation <br> 
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

<br>
<div align=center>
  (利用人工資料實作 並以圖形說明 且以supermarket為例)
</div>
<br>

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


## :black_nib: Non-Bayesian Perspective of Cost-Sensitive Binary Classiﬁcation
### :arrow_down_small:Key Idea: Example Weight = Copying <br>
Non-Bayesian Perspective of Cost-Sensitive Binary Classiﬁcation的目標也與前面介紹的分類法都一樣，希望分類器g(x)將所有未知example分類後可以得到一個最小的cost

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9623.png" 
width="420" height="110">
  圖23
</sub>
</div>
<br>

---

在前面提到的Class-Weighted Cost-Sensitive Binary Classiﬁcation、Example-Weighted Cost-Sensitive Binary Classiﬁcation、ABOD等方法，都是當example預測錯誤時會給予一個懲罰(cost)或說權重(W)，如圖24左邊，但其實換個角度想當有一個example的權重為W時，其意思等同於copy同個example W 次，並且給予每個example 的cost為1，如圖24右邊，而其中copy方式可以採用oversampling

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9624.png" 
width="390" height="100">
  圖24
</sub>
</div>
<br>

---

用前面提到的Example-Weighted Classiﬁcation的例子來輔助說明，一開始的original problem如圖25邊，同之前說明不再贅述，此時有五個example(x1 ~x5)且分類錯誤的W已經知道了，接著可以利用oversampling(不一定是oversampling，undersampling等方法看題目要求，下方會再做介紹)的方法將題目轉換為equivalent problem，如圖25右邊的形式。以X3 example為例，original problem為(X3、+1、100)，經過轉換後也就是將X3 example複製100次並給予每個example的W為1，可以看到變成圖25右邊的形式，接著再用equivalent problem下被轉換的example(很多個w為1的樣本)去訓練出一個好的二元分類器，而訓練的方式可以用SVM、NNet、Adaboost…等等的方法
\
- __題外話__
\
{{{copy的方式較不推薦，因這樣直接copy可能會導致不符合iid條件及線性回歸假設，換個方式想若將此問題轉制為電腦讀得懂的語言，有可能會發生線性重合的問題(很多個column對應到的值都一樣)}}}

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9625.png" 
width="390" height="200">
  圖25
</sub>
</div>
<br>

※Non-Bayesian Perspective of Cost-Sensitive Binary Classiﬁcation中有個方法叫Cost-Proportionate Example Weighting(接下來要介紹)，而以上介紹的技巧(copy)則是Cost-Proportionate Example Weighting 的某個方法

### :arrow_down_small:Cost-Proportionate Example Weighting(CPEW) <br>

接下來這邊開始詳細介紹Non-Bayesian Perspective of Cost-Sensitive Binary Classiﬁcation中 的其中一個方法Cost-Proportionate Example Weighting，其主要的架構如圖26所示

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9626.png" 
width="550" height="300">
  圖26
</sub>
</div>
<br>

Step1
\
將原始問題(Xn、yn、Wn)利用copy的概念，有效轉換為(Xm、Ym)的形式，而本文將介紹的方法為以下三種方法 (還有其他不同種方法 可參閱相關論文) :
\
\
1.over/under-sampling with normalized wn (Elkan, 2001)  – 概念如前頁提到的例子，不再贅述
\
2.under-sampling by rejection (Zadrozny, 2003) 
\
3.modify existing algorithms equivalently (Zadrozny, 2003)
\
\
Step2
\
用自己喜歡的演算法，對變更後的example進行分類，已得到一個好的分類器g(x)
\
\
Step3
\
利用訓練好的分類器g(x)進行未來資料的分類

### :arrow_down_small:CPEW by “Modiﬁcation”  <br>
(step1中的3.)

此方法與其他方法最大的差異在step1其餘步驟step2 step3皆相同，而其主要概念是透過修改演算法的目標函示做到Cost-Proportionate Example Weighting，如圖27可知 SVM的目標涵是為regulation part  1/2(w、w) + hinge loss part ∑_(n=1)^N▒〖C ξn〗 ，前面介紹的方法可知，我們在解original problem時是給予每個example一個若發生分類錯誤的weight，但CPEW by Modiﬁcation的方法是直接更改目標函式變成1/2(w、w) + ∑_(n=1)^N▒〖C Wn ξn〗，換句話說也就是直接修改每個example的權重w

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9627.png" 
width="390" height="120">
  圖27
</sub>
</div>
<br>

---
<br>
<div align=center>
  (利用人工資料實作 並以圖形說明 且以supermarket為例)
</div>
<br>

圖28可以看到原始問題經過CPEW by Modiﬁcation的方法後，+1類別原本為小圓圈，修改了example的權重(W)後，由小圓圈變成了大圓圈，接著再利用二元分類器進行分類(圖28右下)會發現分的比用regular方法分類來的好

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9628.png" 
width="550" height="350">
  圖28
</sub>
</div>
<br>

### :arrow_down_small:CPEW by “Rejection Sampling”  <br>
(step1中的2.)

此方法做Step1時的主要概念是會賦予每個樣本一個隨機數值，且會設定一個threshold(這例子中為一個nomalized weight)，若樣本賦予的隨機值低於設定的threshold，則我們會將該example取出放入訓練集中，反之若隨機值大於threshold則拒絕，因此我們會得到一個比原資料集少的新資料集，接著Step2我們會用新的資料集進行分類，過程中會得到一個弱分類器，重複做Step1、Step2的步驟，最終Step將所有弱分類器組合起來會得到一個集合分類器，流程如圖29所示

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/%E5%9C%9629.png" 
width="550" height="300">
  圖29
</sub>
</div>
<br>

---

Non-Bayesian Perspective of Cost-Sensitive Binary Classiﬁcation中介紹的方法，其使用時建議 :
\
white box :
若使用者非常清楚演算法的細節，且該演算法中具有可以調整權重的項目則建議使用CPEW by “Modiﬁcation”的方法
\
black box : 
若使用者不了解演算法的細節，或該演算法中不具有調整參數的項目則建議使用CPEW by “Rejection Sampling”的方法



## :black_nib: 實作 <br>
資料來源 : kaggla -- Credit Card Fraud Detection
- (https://www.kaggle.com/mlg-ulb/creditcardfraud)


### :arrow_down_small: RandomForestClassifier <br>

```python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random
import warnings
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold,train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, roc_auc_score
from costcla.metrics import savings_score, cost_loss
import itertools
import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random
import seaborn as sns
import warnings
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, roc_auc_score
import itertools
import sys
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from costcla.metrics import cost_loss, savings_score
from costcla.models import CostSensitiveLogisticRegression, CostSensitiveDecisionTreeClassifier,CostSensitiveRandomForestClassifier


warnings.filterwarnings('ignore')

def display_summary(true,pred):
    tn, fp, fn, tp = confusion_matrix(true,pred).ravel()
    print('confusion matrix')
    print(np.array([[fn,tn],[tp,fp]]))
    print('sensitivity is %f',1.*tp/(tp+fn))
    print('specificity is %f',1.*tn/(tn+fp))
    print('accuracy is %f',1.*(tp+tn)/(tp+tn+fp+fn))
    print('balanced accuracy is %',1./2*(1.*tp/(tp+fn)+1.*tn/(tn+fp)))

#print('Gaussian NB')
#display_summary(y_test,y_pred_nb)

##########################################################################

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
#    else:
#        print('Confusion matrix, without normalization')

#    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    
######################################################################
def show_data(cm, print_res = 0):
    tp = cm[0,0]
    fn = cm[1,0]
    fp = cm[0,1]
    tn = cm[1,1]
    if print_res == 1:
        print('Precision =     {:.8f}'.format(tp/(tp+fp)))
        print('Recall (TPR)(sensitivity) =  {:.8f}'.format(tp/(tp+fn)))
        print('Fallout (FPR) = {:.8e}'.format(fp/(fp+tn)))
        print('Specificity = {:.8e}'.format(tn/(fp+tn)))
    return tp/(tp+fp), tp/(tp+fn), fp/(fp+tn)


df = open('C:/Users/tsungyu/Downloads/creditcarddata/creditcard.csv')

df = pd.read_csv(df)

df.head()
df.shape
df.columns[df.isnull().any()].tolist() # there is no missing values in columns

df = df.drop(['Time'],axis=1) # drop the Time column.since it doesn't make sense in modeling.


np.random.seed(37)
x = df.iloc[:, df.columns != 'Class']
y = df.iloc[:, df.columns == 'Class']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

cost_mat_train = np.zeros((len(y_train),4))

#false positives cost 5
cost_mat_train[:,0]=2
#false negatives cost the transaction amount
cost_mat_train[:,1]=x_train['Amount']
#true positives also cost 5
cost_mat_train[:,2]=0
cost_mat_train[:,3]=0

cost_mat_test = np.zeros((len(y_test),4))

cost_mat_test[:,0]=2
cost_mat_test[:,1]=x_test['Amount']
cost_mat_test[:,2]=0
cost_mat_test[:,3]=0



clf_random = RandomForestClassifier(random_state=0)
clf_random = clf_random.fit(x_train, y_train)
y_pred_rf = clf_random.predict(x_test)


print('-------RandomForestClassifier------')
display_summary(y_test,y_pred_rf)


cm = confusion_matrix(y_test, y_pred_rf)
tn, fp, fn, tp = confusion_matrix(y_test,y_pred_rf).ravel()

plot_confusion_matrix(cm, ['0', '1'], )
pr, tpr, fpr = show_data(cm, print_res = 1);

# Savings using only RandomForest
print("savings_score=" , savings_score(y_test, y_pred_rf, cost_mat_test))
print("cost_loss=" , cost_loss(y_test, y_pred_rf, cost_mat_test))
print('F1_score  =     {:.8f}'.format(2*(((tp/(tp+fp))*(tp/(tp+fn)))/((tp/(tp+fp))+(tp/(tp+fn))))))
```

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/randomforest.jpg" 
width="300" height="500">
</sub>
</div>
<br>


### :arrow_down_small: CostSensitiveRandomForestClassifier <br>

```python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random
import seaborn as sns
import warnings
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, roc_auc_score
import itertools
import sys
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from costcla.metrics import cost_loss, savings_score
from costcla.models import CostSensitiveLogisticRegression, CostSensitiveDecisionTreeClassifier,CostSensitiveRandomForestClassifier


##########################################################################
def display_summary(true,pred):
    tn, fp, fn, tp = confusion_matrix(true,pred).ravel()  #網路資料版
    print('confusion matrix')
    print(np.array([[fn,tn],[tp,fp]]))
    print('sensitivity is %f',1.*tp/(tp+fn))
    print('specificity is %f',1.*tn/(tn+fp))
    print('accuracy is %f',1.*(tp+tn)/(tp+tn+fp+fn))
    print('balanced accuracy is %',1./2*(1.*tp/(tp+fn)+1.*tn/(tn+fp)))

#print('Gaussian NB')
#display_summary(y_test,y_pred_nb)

##########################################################################

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
#    else:
#        print('Confusion matrix, without normalization')

#    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    
######################################################################
def show_data(cm, print_res = 0):
    tp = cm[0,0]
    fn = cm[1,0]
    fp = cm[0,1]
    tn = cm[1,1]
    if print_res == 1:
        print('Precision =     {:.8f}'.format(tp/(tp+fp)))
        print('Recall (TPR)(sensitivity) =  {:.8f}'.format(tp/(tp+fn)))
        print('Fallout (FPR) = {:.8e}'.format(fp/(fp+tn)))
        print('Specificity = {:.8e}'.format(tn/(fp+tn)))
    return tp/(tp+fp), tp/(tp+fn), fp/(fp+tn)


df_credit = pd.read_csv('C:/Users/tsungyu/Downloads/creditcarddata/creditcard.csv')
 
col_names = df_credit.columns
feature_cols = col_names[:-1]
df_negative = df_credit[df_credit[col_names[-1]]==0]
df_positive = df_credit[df_credit[col_names[-1]]==1]
X = df_credit[feature_cols]
y = df_credit[col_names[-1]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)




cost_mat_train = np.zeros((len(y_train),4))
#X_train['Amount']=abs(X_train['Amount']-5) ###############!!!!!!

#false positives cost 5
cost_mat_train[:,0]=2
#false negatives cost the transaction amount
cost_mat_train[:,1]=250
#true positives also cost 5
cost_mat_train[:,2]=0
cost_mat_train[:,3]=0



cost_mat_test = np.zeros((len(y_test),4))

cost_mat_test[:,0]=2
cost_mat_test[:,1]=250
cost_mat_test[:,2]=0
cost_mat_test[:,3]=0


g = CostSensitiveRandomForestClassifier()
g.fit(np.array(X_train), np.array(y_train), cost_mat_train)
y_pred_rf_cslr=g.predict(np.array(X_test))

print('--------CostSensitiveRandomForestClassifier------')
display_summary(y_test,y_pred_rf_cslr)




cm = confusion_matrix(y_test, y_pred_rf_cslr)
tn, fp, fn, tp = confusion_matrix(y_test,y_pred_rf_cslr).ravel()

plot_confusion_matrix(cm, ['0', '1'], )
pr, tpr, fpr = show_data(cm, print_res = 1);


# Savings using only RandomForest
print("savings_score=" , savings_score(y_test, y_pred_rf_cslr, cost_mat_test))
print("cost_loss=" , cost_loss(y_test, y_pred_rf_cslr, cost_mat_test))
print('F1_score  =     {:.8f}'.format(2*(((tp/(tp+fp))*(tp/(tp+fn)))/((tp/(tp+fp))+(tp/(tp+fn))))))
```

<br>
<div align=center>
<sub> 
<img src="https://github.com/wutsungyu/Cost-Sensitive/blob/master/pic/costsensitive%20randomforest.jpg" 
width="300" height="500">
</sub>
</div>
<br>



## :black_nib: Reference <br>
- [Wu, Min-You, Cost-Sensitive Classification:
Algorithms and Advances](https://www.csie.ntu.edu.tw/~htlin/talk/doc/cs.acml13.handout.pdf)


## :black_nib: Package 使用參考 <br>
- [costcla](http://albahnsen.github.io/CostSensitiveClassification/index.html)


# KNN-algorithm
------------------

<p align="center">
  <img src="https://user-images.githubusercontent.com/65572032/159425143-e07117ca-e3de-4633-a21a-2fddff4400a9.png" />
</p>

K-NN ( K-Nearest Neighbor) algoritması en basit ve en çok kullanılan sınıflandırma algoritmasından biridir. 
-	Avantajları: basit ve gürültülü eğitim verilerine karşı dirençli olması sebebiyle en popüler Gözetimli makine öğrenme algoritmalarından biridir.
-	Dezavantajları: uzaklık hesabı yaparken bütün durumları sakladığından, büyük veriler için kullanıldığında çok sayıda bellek alanına gereksinim duymaktadır

      •	Gözetimli öğrenme: etiketli verileri kullanır. Eğitimde kullanılacak veriler önceden bilinir. Bu bilgi ile sistem öğrenir ve yeni gelen veriyi yorumlar, Gözetimsiz ise Önceden eğitilmemiş ve bilinmeyen veriler arasında bağlantı kurarak birbirine yakın olan verileri sınıflandırması ve kümelendirmesi mantığıyla çalışır.


Çalışma mantığı:
Eğitim verilerini öğrenmez, bunun yerine eğitim veri kümesini “ezberler”. Bir tahmin yapmak istediğimizde, tüm veri setinde en yakın komşuları arar.


İşleyişi:
1-	Algoritmanın çalışmasında bir K değeri belirlenir. K değerinin anlamı bakılacak eleman sayısıdır. Örneğin: k=2 olsun. Bu durumda en yakın 2 komşuya göre sınıflandırma yapılacaktır.
2-	Bir değer geldiğinde en yakın K kadar eleman alınarak gelen değer arasındaki uzaklık hesaplanır. Ve uzaklığı hesaplamak için 3 farklı tip uzaklık fonksiyonu kullanılmaktadır: 
1- Manhattan Uzaklık Fonksiyonu	 2- Minkowski Uzaklık Fonksiyonu 3- Öklid Uzaklık Fonksiyonu
3-	İlgili uzaklıklardan en yakın k komşu ele alınır. Öznitelik değerlerine göre k komşu veya komşuların sınıfına atanır.
4-	Seçilen sınıf, tahmin edilmesi beklenen gözlem değerinin sınıfı olarak kabul edilir. Yani yeni veri etiketlenmiş (label) olur.





örnek:


(şekil2)'de 10 tane verimiz olsun. X1=8 ve X2=4 değerleri için en yakın komşu bulma algoritmasını kullanarak hangi sınıfa ait olduğunu bulalım. K=4 verilmiş olsun. Öklid uzaklık fonksiyonunu kullanarak;

   ![şekil2](https://user-images.githubusercontent.com/65572032/159424762-52b9b4de-3d2e-4a02-a2d4-429afc62c29d.png)


   ![2 1](https://user-images.githubusercontent.com/65572032/159425231-ab2efa3d-5878-4b12-a97c-5d42b6e6ff5a.png)






Hesaplamaları yaptık şimdi en yakın 4 noktayı alıp bakacağız. 2.24, 2.83, 3.16, 4.24 sonuçlarının tabloda karşılık geldiği değerler GOOD, BAD, BAD, BAD olarak gözüküyor. 3tane BAD 1 tane GOOD olduğundan en çok olan sınıfa dâhil ederiz. Yani BAD sınıfına dâhil oldu.



*** Uygulamanın kodu ektiki knn.py dosyasındadır.





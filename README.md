# webden_cek
Web sayfalarının arama listelerinden veri çekme örneği

Örnek olarak 
https://www.internethaber.com/arama?key=kale&page=2<br>
Şu sitede bir arama yapalım linkten kontrol ederek en fazla 30 sayfa sonuç olduğunu gördüm<br>
https://www.internethaber.com/arama?key=kale&page=30<br>
Yani sorgulayacağımız sayfalar 1 ile 30 arasındaki linklerde bulunan ve classında news-list bulunan divlerdeki ilk a tagının href bilgisi olmalı.<br>

![image](https://user-images.githubusercontent.com/619879/171192864-981acb55-7d69-4ace-ab8f-cbbe2435ce45.png)<br>

1'den 30'a kadar döndüreceğimiz bir döngü ile her sayfayı yukardaki class ve a tagına göre aratmamız lazım. Elde ettiğimiz her yeni linki de yeni bir request yaparak tekrar sorgulamalı ve classı news-detail__title ile başlığı, classı news-detail-content ile de içeriği olacak şekilde sorgularımızı düzenlemeliyiz.

![image](https://user-images.githubusercontent.com/619879/171193767-7da44450-c121-496c-a780-b220b96a9fb7.png)

Koddaki örnek [akrofili.org](https://arkeofili.com/) sitesi için hazırlanmıştır. Siz de kendi veri çekme kodunu bu mantıkta düzenleyebilirsiniz.

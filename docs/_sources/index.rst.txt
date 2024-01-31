.. _index:

===========================
Haber Görseli Üretim Projesi: Mozaik
===========================

.. toctree::
   :maxdepth: 2
   :caption: İçindekiler

   genel-bakis
   kullanici-kilavuzu
   sınıflandırma-sistemi

Sınıflandırma Sistemi
=====================

Haber Görseli Üretim Projesindeki sınıflandırma sistemi, girdi olarak verilen haber metinleri ve görsellerini analiz ederek, bunları çeşitli kategorilere ayırmak için tasarlanmıştır. Bu bölüm, sistemin genel yapısını ve işlevselliğini detaylandırmaktadır.

İşlevsel Bileşenler
--------------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Bileşen
     - Açıklama
   * - **Metin Analizi**
     - Haber metninin içeriğini, dilini ve tonunu analiz ederek temel konuyu ve duygusal yönü belirler.
   * - **Görsel Analizi**
     - Görselleri içerik, renk ve kompozisyon açısından inceler, metinle uyumunu ve kalitesini değerlendirir.
   * - **Kategorizasyon**
     - Analiz sonuçlarına göre haber içeriğini belirli kategorilere ayırır.
   * - **Görsel Öneriler**
     - Sınıflandırma sonuçlarına uygun görsel tasarımlar önerir.


.. toctree::
   :maxdepth: 1

   siniflandirma/kategorizasyon
   siniflandirma/kullanim-senaryolari

Arama ve Filtreleme
=============================

Projemizdeki arama ve filtreleme özellikleri, kullanıcıların haber görsellerine ve haberlerle ilişkili görsellere daha hızlı ve etkin bir şekilde erişmesini sağlar. Kullanıcılar, başlıklar, anahtar kelimeler, alt kategoriler, nesne detayları, karakterler ve yükleme türüne göre içerikleri filtreleyebilirler. Bu özellik, aradığınız içeriği bulmanızı kolaylaştırır ve keşfetme sürecini kişiselleştirir.

.. toctree::
   :maxdepth: 1

   filtering/filter



Üretilen Görseller
==================

Bu bölüm, sistemimiz tarafından şu ana kadar üretilen görselleri içermektedir. GörüntüÜretimi modelimiz, haber içeriklerine uygun görseller üretmek için tasarlanmıştır. Bu görseller, haberlerin anlatımını güçlendirmekte ve içeriklerin görsel olarak zenginleştirilmesine katkıda bulunmaktadır.

.. toctree::
   :maxdepth: 1

   generated_images


Indices and Tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
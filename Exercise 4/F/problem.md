<div class="problem-statement">
   <div class="header">
      <h1 class="title">F. Продажи</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись вида Покупатель
            товар количество, где Покупатель&nbsp;— имя покупателя (строка без пробелов), товар&nbsp;— название товара (строка без пробелов), количество&nbsp;—
            количество приобретенных единиц товара. Создайте список всех покупателей, а для каждого покупателя подсчитайте количество
            приобретенных им единиц каждого вида товаров. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Вводятся сведения о покупках в указанном формате. 
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите список всех покупателей в лексикографическом порядке, после имени каждого покупателя выведите двоеточие, затем выведите
            список названий всех приобретенных данным покупателем товаров в лексикографическом порядке, после названия каждого товара
            выведите количество единиц товара, приобретенных данным покупателем. Информация о каждом товаре выводится в отдельной строке.</p></span></div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>Ivanov paper 10
Petrov pens 5
Ivanov marker 3
Ivanov paper 7
Petrov envelope 20
Ivanov envelope 5
</pre></td>
            <td><pre>Ivanov:
envelope 5
marker 3
paper 17
Petrov:
envelope 20
pens 5
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>Ivanov aaa 1
Petrov aaa 2
Sidorov aaa 3
Ivanov aaa 6
Petrov aaa 7
Sidorov aaa 8
Ivanov bbb 3
Petrov bbb 7
Sidorov aaa 345
Ivanov ccc 45
Petrov ddd 34
Ziborov eee 234
Ivanov aaa 45
</pre></td>
            <td><pre>Ivanov:
aaa 52
bbb 3
ccc 45
Petrov:
aaa 9
bbb 7
ddd 34
Sidorov:
aaa 356
Ziborov:
eee 234
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 3</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>TKSNUU FKXYPUGQ 855146
TKSNUU FKXYPUGQ 930060
TKSNUU FKXYPUGQ 886973
TKSNUU FKXYPUGQ 59344
TKSNUU FKXYPUGQ 296343
TKSNUU FKXYPUGQ 193166
TKSNUU FKXYPUGQ 211696
TKSNUU FKXYPUGQ 821064
TKSNUU FKXYPUGQ 672846
TKSNUU FKXYPUGQ 820341
TKSNUU FKXYPUGQ 350693
TKSNUU FKXYPUGQ 469538
TKSNUU FKXYPUGQ 849069
TKSNUU FKXYPUGQ 502007
TKSNUU FKXYPUGQ 961595
TKSNUU FKXYPUGQ 747271
TKSNUU FKXYPUGQ 863648
TKSNUU FKXYPUGQ 952069
TKSNUU FKXYPUGQ 286019
TKSNUU FKXYPUGQ 364841
TKSNUU FKXYPUGQ 455930
TKSNUU FKXYPUGQ 100486
TKSNUU FKXYPUGQ 335026
TKSNUU FKXYPUGQ 197672
TKSNUU FKXYPUGQ 217640
TKSNUU FKXYPUGQ 612549
TKSNUU FKXYPUGQ 622501
TKSNUU FKXYPUGQ 96554
TKSNUU FKXYPUGQ 327166
TKSNUU FKXYPUGQ 425399
TKSNUU FKXYPUGQ 362309
TKSNUU FKXYPUGQ 78477
TKSNUU FKXYPUGQ 258916
TKSNUU FKXYPUGQ 297923
TKSNUU FKXYPUGQ 8891
TKSNUU FKXYPUGQ 13639
TKSNUU FKXYPUGQ 77308
TKSNUU FKXYPUGQ 707620
TKSNUU FKXYPUGQ 68205
TKSNUU FKXYPUGQ 256702
TKSNUU FKXYPUGQ 668334
TKSNUU FKXYPUGQ 968673
TKSNUU FKXYPUGQ 138125
TKSNUU FKXYPUGQ 222904
TKSNUU FKXYPUGQ 214091
TKSNUU FKXYPUGQ 500231
TKSNUU FKXYPUGQ 19611
TKSNUU FKXYPUGQ 491343
TKSNUU FKXYPUGQ 404307
TKSNUU FKXYPUGQ 68367
TKSNUU FKXYPUGQ 287107
TKSNUU FKXYPUGQ 794935
TKSNUU FKXYPUGQ 254217
TKSNUU FKXYPUGQ 206370
TKSNUU FKXYPUGQ 202761
TKSNUU FKXYPUGQ 929017
TKSNUU FKXYPUGQ 843359
TKSNUU FKXYPUGQ 955269
TKSNUU FKXYPUGQ 134139
TKSNUU FKXYPUGQ 946168
TKSNUU FKXYPUGQ 967781
TKSNUU FKXYPUGQ 856474
TKSNUU FKXYPUGQ 465070
TKSNUU FKXYPUGQ 580526
TKSNUU FKXYPUGQ 172109
TKSNUU FKXYPUGQ 191703
TKSNUU FKXYPUGQ 207916
TKSNUU FKXYPUGQ 512264
TKSNUU FKXYPUGQ 533081
TKSNUU FKXYPUGQ 577208
TKSNUU FKXYPUGQ 831389
TKSNUU FKXYPUGQ 439158
TKSNUU FKXYPUGQ 565633
TKSNUU FKXYPUGQ 452643
TKSNUU FKXYPUGQ 164426
TKSNUU FKXYPUGQ 540743
TKSNUU FKXYPUGQ 880704
TKSNUU FKXYPUGQ 868529
TKSNUU FKXYPUGQ 240742
TKSNUU FKXYPUGQ 868865
TKSNUU FKXYPUGQ 910442
TKSNUU FKXYPUGQ 146737
TKSNUU FKXYPUGQ 820984
TKSNUU FKXYPUGQ 660948
TKSNUU FKXYPUGQ 957975
TKSNUU FKXYPUGQ 135847
TKSNUU FKXYPUGQ 401865
TKSNUU FKXYPUGQ 982859
TKSNUU FKXYPUGQ 748454
TKSNUU FKXYPUGQ 354734
TKSNUU FKXYPUGQ 525638
TKSNUU FKXYPUGQ 119140
TKSNUU FKXYPUGQ 484816
TKSNUU FKXYPUGQ 616539
TKSNUU FKXYPUGQ 682553
TKSNUU FKXYPUGQ 841541
TKSNUU FKXYPUGQ 713063
TKSNUU FKXYPUGQ 433453
TKSNUU FKXYPUGQ 465340
TKSNUU FKXYPUGQ 985635
</pre></td>
            <td><pre>TKSNUU:
FKXYPUGQ 49769497
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

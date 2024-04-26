<div class="problem-statement">
   <div class="header">
      <h1 class="title">H. Охрана</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>4&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
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
         <p>На секретной военной базе работает N охранников. Сутки поделены на 10000 равных промежутков времени, и известно когда каждый
            из охранников приходит на дежурство и уходит с него. Например, если охранник приходит в 5, а уходит в 8, то значит, что он
            был в 6, 7 и 8-ой промежуток (а в 5-й нет!!!).
         </p></span><p>Укажите, верно ли что для данного набора охранников, объект охраняется в любой момент времени хотя бы одним охранником и удаление
         любого из них приводит к появлению промежутка времени, когда объект не охраняется.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входного файла записано натуральное число K (1 ≤ K ≤ 100) — количество тестов в файле. Каждый тест начинается
            с числа N (1 ≤ N ≤ 10000), за которым следует N пар неотрицательных целых чисел A и B — время прихода на дежурство и ухода
            (0 ≤ A ≤ B ≤ 10000) соответствующего охранника.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите K строк, где в M-ой строке находится слово Accepted, если M-ый набор охранников удовлетворяет описанным выше условиям.
            В противном случае выведите Wrong Answer.
         </p></span><p></p>
   </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>2
3 0 3000 2500 7000 2700 10000
2 0 3000 2700 10000
</pre></td>
            <td><pre>Wrong Answer
Accepted
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

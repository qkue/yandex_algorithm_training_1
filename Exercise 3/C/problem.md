<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Кубики</h1>
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
         <p>Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны по
            цвету. Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах.
            Для этого они занумеровали все цвета случайными числами. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в
            оставшейся части. Номер любого цвета&nbsp;— это целое число в пределах от 0 до <span class="tex-math-text">10<sup>9</sup></span>. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входного файла записаны числа N и M&nbsp;— количество кубиков у Ани и Бори соответственно. В следующих N строках
            заданы номера цветов кубиков Ани. В последних M строках номера цветов кубиков Бори. 
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите сначала количество, а затем отсортированные по возрастанию номера цветов таких, что кубики каждого цвета есть в обоих
            наборах, затем количество и отсортированные по возрастанию номера остальных цветов у Ани, потом количество и отсортированные
            по возрастанию номера остальных цветов у Бори. 
         </p></span></div>
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
            <td><pre>4 3
0
1
10
9
1
3
0
</pre></td>
            <td><pre>2
0 1
2
9 10
1
3
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
            <td><pre>2 2
1
2
2
3
</pre></td>
            <td><pre>1
2
1
1
1
3
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
            <td><pre>0 0
</pre></td>
            <td><pre>0

0

0

</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

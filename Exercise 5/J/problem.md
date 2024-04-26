<div class="problem-statement">
   <div class="header">
      <h1 class="title">J. Треугольники</h1>
      <table>
         <thead>
            <th></th>
            <th>Все языки</th>
            <th>Python 3.9.1</th>
         </thead>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
            <td>4&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
            <td>256Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="2">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="2">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Петя достаточно давно занимается в математическом кружке, поэтому он уже успел не только правила выполнения простейших операций,
            но и такое достаточно сложное понятие как симметрия. Для того, чтобы получше изучить симметрию Петя решил начать с наиболее
            простых геометрических фигур – треугольников. Он скоро понял, что осевой симметрией обладают так называемые равнобедренные
            треугольники. Поэтому теперь Петя ищет везде такие треугольники.
         </p></span><p>Напомним, что треугольник называется равнобедренным, если его площадь положительна, и у него есть хотя бы две равные стороны.</p>
      <p>Недавно Петя, зайдя в класс, увидел, что на доске нарисовано n точек. Разумеется, он сразу задумался, сколько существует троек
         из этих точек, которые являются вершинами равнобедренных треугольников.
      </p>
      <p>Требуется написать программу, решающую указанную задачу.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Входной файл содержит целое число n (3 ≤ n ≤ 1500). Каждая из последующих строк содержит по два целых числа – <span class="tex-math-text">x<sub>i</sub></span> и <span class="tex-math-text">y<sub>i</sub></span> – координаты i-ой точки. Координаты точек не превосходят <span class="tex-math-text">10<sup>9</sup></span> по абсолютной величине. Среди заданных точек нет совпадающих.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В выходной файл выведите ответ на задачу.</p></span><p></p>
   </div>
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
            <td><pre>3
0 0
2 2
-2 2
</pre></td>
            <td><pre>1
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
            <td><pre>4
0 0
1 1
1 0
0 1
</pre></td>
            <td><pre>4
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

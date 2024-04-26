<div class="problem-statement">
   <div class="header">
      <h1 class="title">K. Медиана объединения-2</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>5&nbsp;секунд</td>
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
         <p>Дано N упорядоченных по неубыванию последовательностей целых чисел (т.е. каждый следующий элемент больше либо равен предыдущему),
            в каждой из последовательностей ровно L элементов. Для каждых двух последовательностей выполняют следующую операцию: объединяют
            их элементы (в объединенной последовательности каждое число будет идти столько раз, сколько раз оно встречалось суммарно в
            объединяемых последовательностях), упорядочивают их по неубыванию и смотрят, какой элемент в этой последовательности из 2L
            элементов окажется на месте номер L (этот элемент называют левой медианой). 
         </p></span><p>Напишите программу, которая для каждой пары последовательностей выведет левую медиану их объединения.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала вводятся числа N и L (2 ≤ N ≤ 200, 1 ≤ L ≤ 50000). В следующих N строках задаются параметры, определяющие последовательности.</p></span><p>Каждая последовательность определяется пятью целочисленными параметрами: <span class="tex-math-text">x<sub>1</sub></span>, <span class="tex-math-text">d<sub>1</sub></span>, a, c, m. Элементы последовательности вычисляются по следующим формулам: <span class="tex-math-text">x<sub>1</sub></span> нам задано, а для всех i от 2 до L: <span class="tex-math-text">x<sub>i</sub></span> = <span class="tex-math-text">x<sub>i–1</sub></span>+<span class="tex-math-text">d<sub>i–1</sub></span>. Последовательность <span class="tex-math-text">d<sub>i</sub></span> определяется следующим образом: <span class="tex-math-text">d<sub>1</sub></span> нам задано, а для i ≥ 2 <span class="tex-math-text">d<sub>i</sub></span> = ((a*<span class="tex-math-text">d<sub>i–1</sub></span>+c) mod m), где mod – операция получения остатка от деления (a*<span class="tex-math-text">d<sub>i–1</sub></span>+c) на m.
      </p>
      <p>Для всех последовательностей выполнены следующие ограничения: 1 ≤ m ≤ 40000, 0 ≤ a &lt; m, 0≤c&lt;m, 0≤<span class="tex-math-text">d<sub>1</sub></span>&lt;m. Гарантируется, что все члены всех последовательностей по модулю не превышают <span class="tex-math-text">10<sup>9</sup></span>.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В первой строке выведите медиану объединения 1-й и 2-й последовательностей, во второй строке — объединения 1-й и 3-й, и так
            далее, в (N‑1)-ой строке — объединения 1-й и N-ой последовательностей, далее медиану объединения 2-й и 3-й, 2-й и 4-й, и т.д.
            до 2-й и N-ой, затем 3-й и 4-й и так далее. В последней строке должна быть выведена медиана объединения (N–1)-й и N-ой последовательностей.
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
            <td><pre>3 6
1 3 1 0 5
0 2 1 1 100
1 6 8 5 11
</pre></td>
            <td><pre>7
10
9
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Последовательности, объединения которых мы считаем, таковы:</p></span><p>1 4 7 10 13 16</p>
      <p>0 2 5 9 14 20</p>
      <p>1 7 16 16 21 22</p>
   </div>
</div></div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Приближенный двоичный поиск</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
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
         <p>Для каждого из чисел второй последовательности найдите ближайшее к нему в первой.</p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входных данных содержатся числа <span class="tex-math-text">N</span> и <span class="tex-math-text">K</span> (<span class="tex-math-inline"><img class="tex-math" src="picx.png"></span>). Во второй строке задаются <span class="tex-math-text">N</span> чисел первого массива, отсортированного по неубыванию, а в третьей строке – <span class="tex-math-text">K</span> чисел второго массива. Каждое число в обоих массивах по модулю не превосходит <span class="tex-math-text">2&#x22C5;10<sup>9</sup></span>. 
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого из <span class="tex-math-text">K</span> чисел выведите в отдельную строку число из первого массива, наиболее близкое к данному. Если таких несколько, выведите меньшее
            из них.
         </p>
         <p></p></span></div>
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
            <td><pre>5 5
1 3 5 7 9 
2 4 8 1 6 
</pre></td>
            <td><pre>1
3
7
1
5
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
            <td><pre>6 11
1 1 4 4 8 120 
1 2 3 4 5 6 7 8 63 64 65 
</pre></td>
            <td><pre>1
1
4
4
4
4
8
8
8
8
120
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
            <td><pre>10 10
-5 1 1 3 5 5 8 12 13 16 
0 3 7 -17 23 11 0 11 15 7 
</pre></td>
            <td><pre>1
3
8
-5
16
12
1
12
16
8
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

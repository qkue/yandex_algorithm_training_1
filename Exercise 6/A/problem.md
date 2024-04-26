<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Двоичный поиск</h1>
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
         <p>Реализуйте двоичный поиск в массиве </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входных данных содержатся натуральные числа <span class="tex-math-text">N</span> и <span class="tex-math-text">K</span> (<span class="tex-math-inline"><img class="tex-math" src="/testsys/tex/render/MCBcbHQgTiwgSyBcbGUgMTAwXCwwMDA=.png"></span>). Во второй строке&nbsp;задаются <span class="tex-math-text">N</span> элементов первого массива, а в третьей строке – <span class="tex-math-text">K</span> элементов второго массива. Элементы обоих массивов - целые числа, каждое из которых по модулю не превосходит <span class="tex-math-text">10<sup>9</sup></span> 
         </p>
         <p></p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Требуется для каждого из K чисел вывести в отдельную строку "YES", если это число встречается в первом массиве, и "NO" в противном
            случае. 
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
            <td><pre>10 10
1 61 126 217 2876 6127 39162 98126 712687 1000000000 
100 6127 1 61 200 -10000 1 217 10000 1000000000 
</pre></td>
            <td><pre>NO
YES
YES
YES
NO
NO
YES
YES
NO
YES
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
            <td><pre>10 10
-8 -6 -4 -4 -2 -1 0 2 3 3 
8 3 -3 -2 2 -1 2 9 -8 0 
</pre></td>
            <td><pre>NO
YES
NO
YES
YES
YES
YES
NO
YES
YES
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
            <td><pre>10 5
1 2 3 4 5 6 7 8 9 10 
-2 0 4 9 12 
</pre></td>
            <td><pre>NO
NO
YES
YES
NO
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

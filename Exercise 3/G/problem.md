<div class="problem-statement">
   <div class="header">
      <h1 class="title">G. Черепахи</h1>
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
         <p>Широко известна следующая задача для младших школьников. Три черепахи ползут по дороге. Одна черепаха говорит: “Впереди меня
            две черепахи”. Другая черепаха говорит: “Позади меня две черепахи”. Третья черепаха говорит: “Впереди меня две черепахи и
            позади меня две черепахи”. Как такое может быть? Ответ: третья черепаха врет! По дороге одна за другой движутся N черепах.
            Каждая черепаха говорит фразу вида: “Впереди меня <span class="tex-math-text">a<sub>i</sub></span> черепах, а позади меня <span class="tex-math-text">b<sub>i</sub></span> черепах”. Ваша задача определить, сколько самое большее количество черепах могут говорить правду. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке вводится целое число N (1 ≤ N ≤ 10000) строк, содержащих целые числа <span class="tex-math-text">a<sub>i</sub></span> и <span class="tex-math-text">b<sub>i</sub></span>, по модулю не превосходящие 10000, описывающие высказывание i-ой черепахи. 
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите целое число M – максимальное количество черепах, которые могут говорить правду. </p></span></div>
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
2 0
0 2
2 2
</pre></td>
            <td><pre>2
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
            <td><pre>5
0 4
1 3
2 2
3 1
4 0
</pre></td>
            <td><pre>5
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
            <td><pre>10
9 1
8 1
7 2
6 2
5 3
4 4
3 6
2 7
1 9
0 8

</pre></td>
            <td><pre>4
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

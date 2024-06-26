<div class="problem-statement">
   <div class="header">
      <h1 class="title">G. Детали</h1>
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
         <p>Имеется N кг металлического сплава. Из него изготавливают заготовки массой K&nbsp;кг каждая. После этого из каждой заготовки вытачиваются
            детали массой M&nbsp;кг каждая (из каждой заготовки вытачивают максимально возможное количество деталей). Если от заготовок после
            этого что-то остается, то этот материал возвращают к началу производственного цикла и сплавляют с тем, что осталось при изготовлении
            заготовок. Если того сплава, который получился, достаточно для изготовления хотя бы одной заготовки, то из него снова изготавливают
            заготовки, из них – детали и т.д. Напишите программу, которая вычислит, какое количество деталей может быть получено по этой
            технологии из имеющихся исходно N кг сплава. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Вводятся N, K, M. Все числа натуральные и не превосходят 200. </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите одно число — количество деталей, которое может получиться по такой технологии. </p></span></div>
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
            <td><pre>10 5 2
</pre></td>
            <td><pre>4
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
            <td><pre>13 5 3
</pre></td>
            <td><pre>3
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
            <td><pre>14 5 3
</pre></td>
            <td><pre>4
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

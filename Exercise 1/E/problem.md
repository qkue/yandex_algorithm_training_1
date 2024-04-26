<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Скорая помощь</h1>
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
         <p>Бригада скорой помощи выехала по вызову в один из отделенных районов. К сожалению, когда диспетчер получил вызов, он успел
            записать только адрес дома и номер квартиры <span class="tex-math-text">K<sub>1</sub></span>, а затем связь прервалась. Однако он вспомнил, что по этому же адресу дома некоторое время назад скорая помощь выезжала в
            квартиру <span class="tex-math-text">K<sub>2</sub></span>, которая расположена в подъезда <span class="tex-math-text">P<sub>2</sub></span> на этаже <span class="tex-math-text">N<sub>2</sub></span>. Известно, что в доме <span class="tex-math-text">M</span> этажей и количество квартир на каждой лестничной площадке одинаково. Напишите программу, которая вычилсяет номер подъезда
            <span class="tex-math-text">P<sub>1</sub></span> и номер этажа <span class="tex-math-text">N<sub>1</sub></span> квартиры <span class="tex-math-text">K<sub>1</sub></span>.
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Во входном файле записаны пять положительных целых чисел <span class="tex-math-text">K<sub>1</sub></span>, <span class="tex-math-text">M</span>, <span class="tex-math-text">K<sub>2</sub></span>, <span class="tex-math-text">P<sub>2</sub></span>, <span class="tex-math-text">N<sub>2</sub></span>. Все числа не превосходят <span class="tex-math-text">10<sup>6</sup></span>.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите два числа <span class="tex-math-text">P<sub>1</sub></span> и <span class="tex-math-text">N<sub>1</sub></span>. Если входные данные не позволяют однозначно определить <span class="tex-math-text">P<sub>1</sub></span> или <span class="tex-math-text">N<sub>1</sub></span>, вместо соответствующего числа напечатайте <span class="tex-math-text">0</span>. Если входные данные противоречивы, напечатайте два числа <span class="tex-math-text">–1</span> (минус один).
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
            <td><pre>89 20 41 1 11
</pre></td>
            <td><pre>2 3
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
            <td><pre>11 1 1 1 1
</pre></td>
            <td><pre>0 1
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
            <td><pre>3 2 2 2 1
</pre></td>
            <td><pre>-1 -1
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

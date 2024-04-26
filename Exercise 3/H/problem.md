<div class="problem-statement">
   <div class="header">
      <h1 class="title">H. Злые свинки</h1>
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
         <p>Вы никогда не задумывались, почему в Angry Birds у птиц нет крыльев? Тем же вопросом задались разработчики новой игры. В их
            версии смысл игры прямо противоположен Angry Birds: зеленая свинка стреляет по злым птицам из лазерного ружья (завязка явно
            не хуже исходной игры).
         </p></span><p>Птицы в игре представляются точками на плоскости. Выстрел сбивает только ближайшую птицу находящуюся на линии огня. При этом
         сбитая птица падая сбивает всех птиц, находящихся ровно под ней. Две птицы не могут находиться в одной точке. По заданному
         расположению птиц необходимо определить, какое минимальное количество выстрелов необходимо, чтобы все птицы были сбиты.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка входного файла содержит единственное целое число N (1 ≤ N ≤ 1000) — количество птиц.</p></span><p>Следующие N строк содержат по два натуральных числа каждая <span class="tex-math-text">x<sub>i</sub></span>, <span class="tex-math-text">y<sub>i</sub></span> — координаты i-ой птицы (0 &lt; x, y ≤ <span class="tex-math-text">10<sup>9</sup></span>). Свинка находится в точке с координатами (0, 0).
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Единственная строка выходного файла должна содержать одно целое число — минимальное количество выстрелов, необходимое для
            того, чтобы сбить всех птиц.
         </p></span><p></p>
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
            <td><pre>6
1 1
2 2
3 3
2 1
3 2
3 1
</pre></td>
            <td><pre>3
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
            <td><pre>6
1 1
2 2
3 3
2 1
3 2
3 4
</pre></td>
            <td><pre>3
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

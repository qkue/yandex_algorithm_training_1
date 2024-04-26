<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Кондиционер</h1>
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
         <p>В офисе, где работает программист Петр, установили кондиционер нового типа. Этот кондиционер отличается особой простотой в
            управлении. У кондиционера есть всего лишь два управляемых параметра: желаемая температура и режим работы.
         </p></span><p>Кондиционер может работать в следующих четырех режимах:</p>
      <p>«freeze» — охлаждение. В этом режиме кондиционер может только уменьшать температуру. Если температура в комнате и так не больше
         желаемой, то он выключается.
      </p>
      <p>«heat» — нагрев. В этом режиме кондиционер может только увеличивать температуру. Если температура в комнате и так не меньше
         желаемой, то он выключается.
      </p>
      <p>«auto» — автоматический режим. В этом режиме кондиционер может как увеличивать, так и уменьшать температуру в комнате до желаемой.</p>
      <p>«fan» — вентиляция. В этом режиме кондиционер осуществляет только вентиляцию воздуха и не изменяет температуру в комнате.</p>
      <p>Кондиционер достаточно мощный, поэтому при настройке на правильный режим работы он за час доводит температуру в комнате до
         желаемой.
      </p>
      <p>Требуется написать программу, которая по заданной температуре в комнате <span class="tex-math-text">t<sub>room</sub></span>, установленным на кондиционере желаемой температуре <span class="tex-math-text">t<sub>cond</sub></span> и режиму работы определяет температуру, которая установится в комнате через час.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка входного файла содержит два целых числа troom, и tcond, разделенных ровно одним пробелом (<span class="tex-math-text">–50 &le; t<sub>room</sub> &le; 50</span>, <span class="tex-math-text">–50 &le; t<sub>cond</sub> &le; 50</span>).
         </p></span><p>Вторая строка содержит одно слово, записанное строчными буквами латинского алфавита — режим работы кондиционера.</p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выходной файл должен содержать одно целое число — температуру, которая установится в комнате через час.</p></span><p></p>
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
            <td><pre>10 20
heat
</pre></td>
            <td><pre>20
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
            <td><pre>10 20
freeze
</pre></td>
            <td><pre>10
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>В первом примере кондиционер находится в режиме нагрева. Через час он нагреет комнату до желаемой температуры в 20 градусов.</p></span><p>Во втором примере кондиционер находится в режиме охлаждения. Поскольку температура в комнате ниже, чем желаемая, кондиционер
         самостоятельно выключается и температура в комнате не поменяется.
      </p>
   </div>
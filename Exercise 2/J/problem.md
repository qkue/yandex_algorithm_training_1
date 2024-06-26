<div class="problem-statement">
   <div class="header">
      <h1 class="title">J. Треугольник Максима</h1>
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
         <p>С детства Максим был неплохим музыкантом и мастером на все руки. Недавно он самостоятельно сделал несложный перкуссионный
            музыкальный инструмент — треугольник. Ему нужно узнать, какова частота звука, издаваемого его инструментом.
         </p></span><p>У Максима есть профессиональный музыкальный тюнер, с помощью которого можно проигрывать ноту с заданной частотой. Максим действует
         следующим образом: он включает на тюнере ноты с разными частотами и для каждой ноты на слух определяет, ближе или дальше она
         к издаваемому треугольником звуку, чем предыдущая нота. Поскольку слух у Максима абсолютный, он определяет это всегда абсолютно
         верно.
      </p>
      <p>Вам Максим показал запись, в которой приведена последовательность частот, выставляемых им на тюнере, и про каждую ноту, начиная
         со второй, записано — ближе или дальше она к звуку треугольника, чем предыдущая нота. Заранее известно, что частота звучания
         треугольника Максима составляет не менее 30 герц и не более 4000 герц.
      </p>
      <p>Требуется написать программу, которая определяет, в каком интервале может находиться частота звучания треугольника.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка входного файла содержит целое число n — количество нот, которые воспроизводил Максим с помощью тюнера (<span class="tex-math-text">2 &le; n &le; 1000</span>). Последующие n строк содержат записи Максима, причём каждая строка содержит две компоненты: вещественное число <span class="tex-math-text">f<sub>i</sub></span> — частоту, выставленную на тюнере, в герцах (<span class="tex-math-text">30 &le; f<sub>i</sub> &le; 4000</span>), и слово «closer» или слово «further» для каждой частоты, кроме первой.
         </p></span><p>Слово «closer» означает, что частота данной ноты ближе к частоте звучания треугольника, чем частота предыдущей ноты, что формально
         описывается соотношением: <span class="tex-math-text">|f<sub>i</sub> − f<sub>triangle</sub>| &lt; |f<sub>i − 1</sub> − f<sub>triangle</sub>|</span> .
      </p>
      <p>Слово «further» означает, что частота данной ноты дальше, чем предыдущая.</p>
      <p>Если оказалось, что очередная нота так же близка к звуку треугольника, как и предыдущая нота, то Максим мог записать любое
         из двух указанных выше слов.
      </p>
      <p>Гарантируется, что результаты, полученные Максимом, непротиворечивы.</p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В выходной файл необходимо вывести через пробел два вещественных числа — наименьшее и наибольшее возможное значение частоты
            звучания треугольника, изготовленного Максимом. Числа должны быть выведены с точностью не хуже <span class="tex-math-text">10<sup>−6</sup></span>.
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
            <td><pre>3
440
220 closer
300 further
</pre></td>
            <td><pre>30.0 260.0
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
554
880 further
440 closer
622 closer
</pre></td>
            <td><pre>531.0 660.0
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

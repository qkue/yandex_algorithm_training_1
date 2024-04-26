<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Определить вид последовательности</h1>
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
         <p>По последовательности чисел во входных данных определите ее вид:</p></span><p>
         <ul>
            <li><span style="font-weight:bold;">CONSTANT</span> &ndash; последовательность состоит из <span style="font-weight:bold;">одинаковых</span> значений 
            </li>
            <li><span style="font-weight:bold;">ASCENDING</span> &ndash; последовательность является <span style="font-weight:bold;">строго</span> возрастающей 
            </li>
            <li><span style="font-weight:bold;">WEAKLY ASCENDING</span> &ndash; последовательность является <span style="font-weight:bold;">нестрого</span> возрастающей 
            </li>
            <li><span style="font-weight:bold;">DESCENDING</span> &ndash; последовательность является <span style="font-weight:bold;">строго</span> убывающей 
            </li>
            <li><span style="font-weight:bold;">WEAKLY DESCENDING</span> &ndash; последовательность является <span style="font-weight:bold;">нестрого</span> убывающей 
            </li>
            <li><span style="font-weight:bold;">RANDOM</span> &ndash; последовательность не принадлежит ни к одному из вышеупомянутых типов 
            </li>
         </ul>
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>По одному на строке поступают числа последовательности <span class="tex-math-text">a<sub>i</sub>, |a<sub>i</sub>| &le; 10<sup>9</sup></span>.<br></p></span><p>Признаком окончания последовательности является число <span class="tex-math-text">-2&times; 10<sup>9</sup></span>. <span style="font-weight:bold;">Оно в последовательность не входит</span>.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В единственной строке выведите тип последовательности.</p></span></div>
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
            <td><pre>-530
-530
-530
-530
-530
-530
-2000000000
</pre></td>
            <td><pre>CONSTANT
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

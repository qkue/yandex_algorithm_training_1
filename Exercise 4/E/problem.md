<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Пирамида</h1>
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
   <div class="legend"> Для строительства двумерной пирамиды используются прямоугольные блоки, каждый из которых характеризуется шириной и высотой.
      <!--l. 49-->
      <p style="text-indent: 0em;">Можно поставить один блок на другой, только если ширина верхнего блока строго меньше ширины нижнего
      (блоки нельзя поворачивать). Самым нижним в пирамиде может быть блок любой ширины. <!--l. 51-->
      </p><p style="text-indent: 0em;">По заданному набору блоков определите, пирамиду какой наибольшей высоты можно построить из
      них. </p>
      <p></p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке входных данных задается число <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math>&nbsp;—
      количество блоков (<!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn>
      <mo>≤</mo> <mi>N</mi> <mo>≤</mo> <mn>1</mn><mn>0</mn><mn>0</mn><mspace width="0.3em"><mn>0</mn><mn>0</mn><mn>0</mn></mspace></math>).
      <!--l. 56-->
      <p style="text-indent: 0em;">В следующих <!--l. 56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math>
      строках задаются пары натуральных чисел <!--l. 56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>w</mi></mrow><mrow><mi>i</mi></mrow></msub></math>
      и <!--l. 56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>h</mi></mrow><mrow><mi>i</mi></mrow></msub></math>
      (<!--l. 56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <msub><mrow><mi>w</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>,</mo><msub><mrow><mi>h</mi></mrow><mrow><mi>i</mi></mrow></msub>
      <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn><sup>9</sup></mn></mrow></msup></math>)&nbsp;— ширина и высота блока соответственно.
      </p>
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите одно целое число&nbsp;— максимальную высоту пирамиды. </div>
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
            <td><pre>3
3 1
2 2
3 3
</pre></td>
            <td><pre>5
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"> В примере пирамида будет состоять из двух блоков: нижним блоком будет блок номер 3, а верхним&nbsp;— блок номер 2. Блок номер
      1 нельзя использовать вместе с блоком номер 3. 
   </div>
</div>

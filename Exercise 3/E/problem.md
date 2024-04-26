<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. OpenCalculator</h1>
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
         <p>В новой программе OpenCalculator появилась новая возможность – можно настроить, какие кнопки отображаются, а какие – нет.
            Если кнопка не отображается на экране, то ввести соответствующую цифру с клавиатуры или копированием из другой программы нельзя.
            Петя настроил калькулятор так, что он отображает только кнопки с цифрами x, y, z. Напишите программу, определяющую, сможет
            ли Петя ввести число N, а если нет, то какое минимальное количество кнопок надо дополнительно отобразить на экране для его
            ввода.
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала вводятся три различных числа из диапазона от 0 до 9: x, y и z (числа разделяются пробелами). Далее вводится целое
            неотрицательное число N, которое Петя хочет ввести в калькулятор. Число N не превышает 10000.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите, какое минимальное количество кнопок должно быть добавлено для того, чтобы можно было ввести число N (если число
            может быть введено с помощью уже имеющихся кнопок, выведите 0)
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
            <td><pre>1 2 3
1123
</pre></td>
            <td><pre>0
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
            <td><pre>1 2 3
1001
</pre></td>
            <td><pre>1
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
            <td><pre>5 7 3
123
</pre></td>
            <td><pre>2
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Комментарии к примерам тестов.</p></span><p>1. Число может быть введено имеющимися кнопками.</p>
      <p>2. Нужно добавить кнопку 0.</p>
      <p>3. Нужно добавить кнопки 1 и 2.</p>
   </div>
</div></div>

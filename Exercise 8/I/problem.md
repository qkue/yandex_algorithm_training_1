<div class="problem-statement">
   <div class="header">
      <h1 class="title">I. Родословная: число потомков</h1>
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
         <p>В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель. </p></span><p>Для каждого элемента дерева определите число всех его потомков (не считая его самого).</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя для каждого
            элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите список всех элементов в лексикографическом порядке, для каждого элемента выводите количество всех его потомков.</p></span></div>
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
            <td><pre>9
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I
</pre></td>
            <td><pre>Alexander_I 0
Alexei 1
Anna 4
Elizabeth 0
Nicholaus_I 0
Paul_I 2
Peter_I 8
Peter_II 0
Peter_III 3
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Если вы используете рекурсию, то вам может быть полезно добавление в начало программы следующих строк: </p></span><p>import sys </p>
      <p>sys.setrecursionlimit(100000)</p>
   </div>
</div></div>

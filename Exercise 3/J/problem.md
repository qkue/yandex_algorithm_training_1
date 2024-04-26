<div class="problem-statement">
   <div class="header">
      <h1 class="title">J. Пробежки по Манхэттену</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
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
         <p>Дороги Нью-Манхэттена устроены следующим образом. С юга на север через каждые сто метров проходит авеню, с запада на восток
            через каждые сто метров проходит улица. Авеню и улицы нумеруются целыми числами. Меньшие номера соответствуют западным авеню
            и южным улицам. Таким образом, можно построить прямоугольную систему координат так, чтобы точка (x, y) лежала на пересечении
            x-ой авеню и y-ой улицы. Легко заметить, что для того, чтобы в Нью-Манхэттене дойти от точки (<span class="tex-math-text">x<sub>1</sub>, y<sub>1</sub></span>) до точки (<span class="tex-math-text">x<sub>2</sub>, y<sub>2</sub></span>) нужно пройти <span class="tex-math-text">|x<sub>2</sub> − x<sub>1</sub>| + |y<sub>2</sub> − y<sub>1</sub>|</span> кварталов. Эта величина называется манхэттенским расстоянием между точками (<span class="tex-math-text">x<sub>1</sub>, y<sub>1</sub></span>) и (<span class="tex-math-text">x<sub>2</sub>, y<sub>2</sub></span>).
         </p></span><p>Миша живет в Нью-Манхэттене и каждое утро делает пробежку по городу. Он выбегает из своего дома, который находится в точке
         (0, 0) и бежит по случайному маршруту. Каждую минуту Миша либо остается на том же перекрестке, что и минуту назад, или перемещается
         на один квартал в любом направлении. Чтобы не заблудиться Миша берет с собой навигатор, который каждые t минут говорит Мише,
         в какой точке он находится. К сожалению, навигатор показывает не точное положение Миши, он может показать любую из точек,
         манхэттенское расстояние от которых до Миши не превышает d.
      </p>
      <p>Через <span class="tex-math-text">t &times; n</span> минут от начала пробежки, получив n-е сообщение от навигатора, Миша решил, что пора бежать домой. Для этого он хочет понять,
         в каких точках он может находиться. Помогите Мише сделать это.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка входного файла содержит числа t, d и n (<span class="tex-math-text">1 &le; t &le; 100</span>, <span class="tex-math-text">1 &le; d &le; 100</span>, <span class="tex-math-text">1 &le; n &le; 100</span>).
         </p></span><p>Далее n строк описывают данные, полученные от навигатора. Строка номер i содержит числа <span class="tex-math-text">x<sub>i</sub></span> и <span class="tex-math-text">y<sub>i</sub></span> — данные, полученные от навигатора через <span class="tex-math-text">t<sub>i</sub></span> минут от начала пробежки.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В первой строке выходного файла выведите число m — число точек, в которых может находиться Миша. Далее выведите m пар чисел
            — координаты точек. Точки можно вывести в произвольном порядке.
         </p></span><p>Гарантируется, что навигатор исправен и что существует по крайней мере одна точка, в которой может находиться Миша.</p>
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
            <td><pre>2 1 5
0 1
-2 1
-2 3
0 3
2 5
</pre></td>
            <td><pre>2
1 5
2 4
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
            <td><pre>1 1 1
0 0
</pre></td>
            <td><pre>5
-1 0
0 -1
0 0
0 1
1 0
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
            <td><pre>1 10 1
0 0
</pre></td>
            <td><pre>5
-1 0
0 -1
0 0
0 1
1 0
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

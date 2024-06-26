<div class="problem-statement">
   <div class="header">
      <h1 class="title">J. НГУ-стройка</h1>
      <table>
         <thead>
            <th></th>
            <th>Все языки</th>
            <th>Python 3.6</th>
         </thead>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
            <td>4&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
            <td>256Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="2">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="2">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Над ареной огромного спортивного комплекса Независимого Главного Университета (НГУ) решили построить перекрытие. Перекрытие
            будет построено по клеевой технологии и состоять из склеенных друг с другом блоков. Блок представляет собой легкий прямоугольный
            параллелепипед. Два блока можно склеить, если они соприкасаются перекрывающимися частями боковых граней ненулевой площади.
         </p></span><p>НГУ представил план комплекса, имеющий вид прямоугольника размером W на L. При этом один из углов прямоугольника находится
         в начале системы координат, а другой имеет координаты (W, L). Стены комплекса параллельны осям координат. 
      </p>
      <p>Подрядчики известили НГУ, что они готовы к определенному сроку изготовить блоки и установить их. Для каждого блока фиксировано
         место его возможного монтажа, совпадающее по размерам с этим блоком. Места выбраны так, что ребра блоков параллельны осям
         координат. Места монтажа блоков не пересекаются. 
      </p>
      <p><img class="user-image" src="pic_j.gif"> 
      </p>
      <p>По техническим условиям перекрытие должно состоять из такого набора склеенных блоков, который содержит сплошной горизонтальный
         слой ненулевой толщины. Торопясь ввести комплекс в эксплуатацию, НГУ решил построить перекрытие из минимально возможного числа
         блоков. 
      </p>
      <p>Требуется написать программу, которая позволяет выбрать минимальное число блоков, которые, будучи установленными на указанных
         подрядчиками местах, образуют перекрытие, либо определить, что этого сделать невозможно. Высота, на которой образуется перекрытие,
         не имеет значения.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входного файла указаны три целых числа: N — количество возможных блоков (<span class="tex-math-text">1 &le; N &le; 10<sup>5</sup></span>) и размеры комплекса W и L (<span class="tex-math-text">1 &le; W, L &le; 10<sup>4</sup></span>). Каждая из последующих N строк описывает место монтажа одного блока, определяемое координатами противоположных углов: <span class="tex-math-text">(x<sub>1</sub>, y<sub>1</sub>, z<sub>1</sub>)</span> и <span class="tex-math-text">(x<sub>2</sub>, y<sub>2</sub>, z<sub>2</sub>)</span>, при этом <span class="tex-math-text">0 &le; x<sub>1</sub> &lt; x<sub>2</sub> &le; W</span>, <span class="tex-math-text">0 &le; y<sub>1</sub> &lt; y<sub>2</sub> &le; L</span>, <span class="tex-math-text">0 &le; z<sub>1</sub> &lt; z<sub>2</sub> &le; 10<sub>9</sub></span>. Все числа во входном файле целые и разделяются пробелами или переводами строк. 
         </p></span><p>Гарантируется, что места установки блоков не пересекаются друг с другом.</p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Первая строка выходного файла должна содержать либо слово «YES», если перекрытие возможно построить, иначе — слово «NO». В
            первом случае вторая строка выходного файла должна содержать минимальное число блоков, образующих перекрытие, а последующие
            строки — номера этих блоков, в соответствии с порядком, в котором они перечислены во входном файле. 
         </p></span><p>Если возможно несколько минимальных наборов блоков, выведите любой из них.</p>
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
            <td><pre>1 10 10
0 0 0 10 10 10
</pre></td>
            <td><pre>YES
1
1 
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
            <td><pre>2 10 10
0 0 0 10 5 5
0 5 5 10 10 10
</pre></td>
            <td><pre>NO
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

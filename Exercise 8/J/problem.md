<div class="problem-statement">
   <div class="header">
      <h1 class="title">J. Родословная: подсчет уровней</h1>
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
         <p>В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель. Каждом элементу дерева сопоставляется
            целое неотрицательное число, называемое высотой. У родоначальника высота равна 0, у любого другого элемента высота на 1 больше,
            чем у его родителя. Вам дано генеалогическое древо, определите высоту всех его элементов. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Программа получает на вход число элементов в генеалогическом древе <span class="tex-math-text">N</span>. Далее следует <span class="tex-math-text">N-1</span> строка, задающие родителя для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого элемента необходимо
            вывести его высоту. 
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
            <td><pre>Alexander_I 4
Alexei 1
Anna 1
Elizabeth 1
Nicholaus_I 4
Paul_I 3
Peter_I 0
Peter_II 2
Peter_III 2
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
            <td><pre>10
AQHFYP MKFXCLZBT
AYKOTYQ QIUKGHWCDC
IWCGKHMFM WPLHJL
MJVAURUDN QIUKGHWCDC
MKFXCLZBT IWCGKHMFM
PUTRIPYHNQ UQNGAXNP
QIUKGHWCDC WPLHJL
UQNGAXNP WPLHJL
YURTPJNR QIUKGHWCDC
</pre></td>
            <td><pre>AQHFYP 3
AYKOTYQ 2
IWCGKHMFM 1
MJVAURUDN 2
MKFXCLZBT 2
PUTRIPYHNQ 2
QIUKGHWCDC 1
UQNGAXNP 1
WPLHJL 0
YURTPJNR 2
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
            <td><pre>10
BFNRMLH CSZMPFXBZ
CSZMPFXBZ IHWBQDJ
FMVQTU FUXATQUGIG
FUXATQUGIG IRVAVMQKN
GNVIZ IQGIGUJZ
IHWBQDJ LACXYFQHSQ
IQGIGUJZ JMUPNYRQD
IRVAVMQKN GNVIZ
JMUPNYRQD BFNRMLH
</pre></td>
            <td><pre>BFNRMLH 3
CSZMPFXBZ 2
FMVQTU 9
FUXATQUGIG 8
GNVIZ 6
IHWBQDJ 1
IQGIGUJZ 5
IRVAVMQKN 7
JMUPNYRQD 4
LACXYFQHSQ 0
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Эта задача имеет решение сложности <span class="tex-math-text">O(n)</span>, но вам достаточно написать решение сложности <span class="tex-math-text">O(n<sup>2</sup>)</span> (не считая сложности обращения к элементам словаря). Пример ниже соответствует приведенному древу рода Романовых.
         </p></span></div>
</div></div>

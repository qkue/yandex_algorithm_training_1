<div class="problem-statement">
   <div class="header">
      <h1 class="title">G. Банковские счета</h1>
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
         <p>Некоторый банк хочет внедрить систему управления счетами клиентов, поддерживающую следующие операции:</p></span><p>Пополнение счета клиента.</p>
      <p>Снятие денег со счета.</p>
      <p>Запрос остатка средств на счете.</p>
      <p>Перевод денег между счетами клиентов.</p>
      <p>Начисление процентов всем клиентам.</p>
      <p>Вам необходимо реализовать такую систему. Клиенты банка идентифицируются именами (уникальная строка, не содержащая пробелов).
         Первоначально у банка нет ни одного клиента. Как только для клиента проводится операция пололнения, снятия или перевода денег,
         ему заводится счет с нулевым балансом. Все дальнейшие операции проводятся только с этим счетом. Сумма на счету может быть
         как положительной, так и отрицательной, при этом всегда является целым числом. 
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Входной файл содержит последовательность операций. Возможны следующие операции: DEPOSIT name sum - зачислить сумму sum на
            счет клиента name. Если у клиента нет счета, то счет создается. WITHDRAW name sum - снять сумму sum со счета клиента name.
            Если у клиента нет счета, то счет создается. BALANCE name - узнать остаток средств на счету клиента name. TRANSFER name1 name2
            sum - перевести сумму sum со счета клиента name1 на счет клиента name2. Если у какого-либо клиента нет счета, то ему создается
            счет. INCOME p - начислить всем клиентам, у которых открыты счета, p% от суммы счета. Проценты начисляются только клиентам
            с положительным остатком на счету, если у клиента остаток отрицательный, то его счет не меняется. После начисления процентов
            сумма на счету остается целой, то есть начисляется только целое число денежных единиц. Дробная часть начисленных процентов
            отбрасывается. 
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого запроса BALANCE программа должна вывести остаток на счету данного клиента. Если же у клиента с запрашиваемым именем
            не открыт счет в банке, выведите ERROR. 
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
            <td><pre>DEPOSIT Ivanov 100
INCOME 5
BALANCE Ivanov
TRANSFER Ivanov Petrov 50
WITHDRAW Petrov 100
BALANCE Petrov
BALANCE Sidorov
</pre></td>
            <td><pre>105
-50
ERROR
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
            <td><pre>BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 100
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 150
BALANCE Petrov
DEPOSIT Ivanov 10
DEPOSIT Petrov 15
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 46
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 14
BALANCE Ivanov
BALANCE Petrov
</pre></td>
            <td><pre>ERROR
ERROR
100
ERROR
150
110
165
156
165
156
179
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
            <td><pre>BALANCE a
BALANCE b
DEPOSIT a 100
BALANCE a
BALANCE b
WITHDRAW a 20
BALANCE a
BALANCE b
WITHDRAW b 78
BALANCE a
BALANCE b
WITHDRAW a 784
BALANCE a
BALANCE b
DEPOSIT b 849
BALANCE a
BALANCE b
</pre></td>
            <td><pre>ERROR
ERROR
100
ERROR
80
ERROR
80
-78
-704
-78
-704
771
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>

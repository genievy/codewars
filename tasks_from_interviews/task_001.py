"""
Дано: список строк состоящий из символа подчеркивания и латинских букв
['___atcggctacgt__tactgcatgtca_________',
'tc________agtacgtactactgacgtca____',
'gcgtatagcgttga_____cgtgacgtacgg']

требуется - написать функцию, которая заменит в каждой строке списка символы подчеркивания
Следующим образом
- непрерывные последовательности из символа полчеркивания меняем на последовательность из символа .
- если последовательность из символов подчеркивания заключена в буквы - оставляем как есть

на выходе в примере

['...atcggctacgt__tactgcatgtca......',
'tc________agtacgtactactgacgtca...',
'gcgtatagcgttga_____cgtgacgtacgg']
"""

init_list = ['___atcggctacgt__tactgcatgtca_________',
             'tc________agtacgtactactgacgtca____',
             'gcgtatagcgttga_____cgtgacgtacgg'
             ]


def my_func(list_of_letters):
    list_result = []
    for s in list_of_letters:
        """
        s.lstrip('_') >>> This returns a str without a '_' on the left
        s.replace(s.lstrip('_'), '') >>> This "subtracts" from str the part that was obtained by the previous action
        s.replace(s.lstrip('_'), '').replace('_', '.') >>> This replaces '_' with '.'
        """
        left_part = s.replace(s.lstrip('_'), '').replace('_', '.')
        right_part = s.replace(s.rstrip('_'), '').replace('_', '.')
        center_part = s.strip('_')
        list_result.append(left_part + center_part + right_part)
    return list_result


print(my_func(init_list))

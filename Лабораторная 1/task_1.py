numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_none_element = 4  # TODO заменить значение пропущенного элемента средним арифметическим
avg_correct_numbers = sum(numbers[:index_none_element] + numbers[index_none_element+1:]) / len(numbers)

numbers[index_none_element] = avg_correct_numbers

print("Измененный список:", numbers)

def arithmetic_arranger(list_a, sum_1=False):
    if len(list_a) > 4:
        return "Error: Too many problems."
    else:
        list_1 = []
        list_2 = []
        underline = []
        sum_list = []

        for item in list_a:
            top_str = ""
            bottom_str = ""
            list_item = item.split(" ")
            if list_item[1] not in "+-":
                return "Error: Operator must be ", "+", " or ", "-", "."
            if not list_item[0].isdigit() and list_item[2].isdigit():
                return "Error: Numbers must only contain digits."
            if len(list_item[0]) > 4 or len(list_item[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
            if len(list_item[0]) > len(list_item[2]):
                top_str += ("  " * (len(list_item[0]) - len(list_item[2]))) + list_item[
                    0
                ]
                bottom_str += (
                    list_item[1]
                    + (" " * (len(list_item[0]) - len(list_item[2]) + 1))
                    + list_item[2]
                )
                list_1.append(top_str)
                list_2.append(bottom_str)
                bottom_line = "-" * len(top_str)
                underline.append(bottom_line)

                if list_item[1] == "+":
                    total = int(list_item[0]) + int(list_item[2])
                    sums = (" " * (len(bottom_line) - len(str(total)))) + str(total)
                    sum_list.append(sums)
                else:
                    total = int(list_item[0]) - int(list_item[2])
                    sums = (" " * (len(bottom_line) - len(str(total)))) + str(total)
                    sum_list.append(sums)

            elif len(list_item[0]) < len(list_item[2]):
                top_str += (
                    " " * ((len(list_item[2]) - len(list_item[0])) + 2)
                ) + list_item[0]
                bottom_str += list_item[1] + " " + list_item[2]
                list_1.append(top_str)
                list_2.append(bottom_str)
                bottom_line = "-" * len(bottom_str)
                underline.append(bottom_line)

                if list_item[1] == "+":
                    total = int(list_item[0]) + int(list_item[2])
                    sums = (" " * (len(bottom_line) - len(str(total)))) + str(total)
                    sum_list.append(sums)
                else:
                    total = int(list_item[0]) - int(list_item[2])
                    sums = (" " * (len(bottom_line) - len(str(total)))) + str(total)
                    sum_list.append(sums)

            elif len(list_item[0]) == len(list_item[2]):
                top_str += "  " + list_item[0]
                bottom_str += list_item[1] + " " + list_item[2]
                list_1.append(top_str)
                list_2.append(bottom_str)
                bottom_line = "-" * len(top_str)
                underline.append(bottom_line)

                if list_item[1] == "+":
                    total = int(list_item[0]) + int(list_item[2])
                    sums = (" " * (len(bottom_line) - len(str(total)))) + str(total)
                    sum_list.append(sums)
                else:
                    total = int(list_item[0]) - int(list_item[2])
                    sums = (" " * (len(bottom_line) - len(str(total)))) + str(total)
                    sum_list.append(sums)

        space = " " * 4

        first_line = space.join(list_1)
        second_line = space.join(list_2)
        bottom_line = space.join(underline)
        sum_line = space.join(sum_list)

    if sum_1 == True:
        return "{}\n{}\n{}\n{}".format(first_line, second_line, bottom_line, sum_line)

    else:
        return "{}\n{}\n{}".format(first_line, second_line, bottom_line)


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

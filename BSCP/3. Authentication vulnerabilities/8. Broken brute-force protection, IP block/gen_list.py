with open('pass_list.txt', 'r', encoding='UTF-8') as file_input_pass:
    with open('output_pass.txt', 'a', encoding='UTF-8') as file_output_pass:
        with open('output_logins.txt', 'a', encoding='UTF-8') as file_output_logins:
            while line := file_input_pass.readline():
                file_output_pass.write(line)
                file_output_logins.write('carlos\n')
                file_output_pass.write('peter\n')
                file_output_logins.write('wiener\n')
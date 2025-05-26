import hashlib

with open('pass_list.txt', 'r', encoding='UTF-8') as file_input_pass:
    with open('output_pass_md5.txt', 'a', encoding='UTF-8') as file_output_pass:
        while line := file_input_pass.readline():
            file_output_pass.write(hashlib.md5(str(line).encode).hexdigest())
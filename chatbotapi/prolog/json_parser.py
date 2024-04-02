import json


def convert_to_pl(json_data, output_file):
    questions = []
    with open(output_file, 'w') as f:
        for item in json_data:
            question = item['question']
            questions.append(question)
            answer = item['answer']
            f.write(f"conocimiento('{question}', '{answer}').\n")

    with open('questions.py', 'w') as f:
        f.write('questions = [\n')
        for pregunta in questions:
            f.write(f'    "{pregunta}",\n')
        f.write(']\n')


def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


json_file_path = 'datos.json'  
output_pl_file = 'conocimientos.pl'  

json_data = read_json_from_file(json_file_path)


convert_to_pl(json_data, output_pl_file)

print(f"Archivo {output_pl_file} generado con éxito.")

import random


def GenerateCard(names, links, column_in_row):
    '''

    :param names: name of each card
    :param links: link of each card
    :param column_in_row: number of columns in each row
    :return:
    '''
    colors = ['info', 'success', 'warning', 'primary', 'danger', 'secondary', 'dark']
    while len(links) < len(names):
        links.append('#')

    icons = []
    while len(icons) < len(names):
        icons.append(random.choice(['fa-user-md', 'fa-user-nurse', 'fa-user', 'fa-user-cog']))

    template_path = 'card_template.txt'
    with open(template_path, 'r', encoding='utf8') as f:
        template = f.read().strip()
    row = ''
    k = 0
    while k < len(names):
        cnt = 0
        row += '<div class="row">\n'
        while cnt < column_in_row and k < len(names):
            temp = template
            temp = temp.replace('%name', names[k])
            temp = temp.replace('%link', links[k])
            temp = temp.replace('%color', colors[k])
            temp = temp.replace('%icon', icons[k])
            row += temp
            cnt += 1
            k += 1
        row += '\n</div>\n'
    print(row)


def GenerateTable(table_name, columns):
    '''
    :param table_name: name of the table
    :param columns:  list of column names
    :return:
    '''
    if table_name is None or table_name == '':
        print('Table name cannot be empty')
        return None

    template_path = 'table_template.txt'
    with open(template_path, 'r', encoding='utf8') as f:
        template = f.read().strip()
    k = 0
    row = ''
    while k < len(columns):
        row += '<th class="sorting sorting_asc" tabindex="0" aria-controls="dataTable" rowspan="1" colspan="1" aria-sort="ascending" aria-label="Name: activate to sort column descending">\n'
        row += columns[k]
        row += '\n</th>\n'
        k += 1
    template = template.replace('%table_name', table_name)
    template = template.replace('%columns', row)
    print(template)

def FormatText(text:str):
    text = text.split('\t')
    text = "', '".join(text)
    text = "['" + text + "']"
    print(text)

if __name__ == '__main__':
    # GenerateCard(['Doctor Record', 'Register Doctor', 'Approve Doctor', 'Doctor Specialisation'],
    #              ['/admin-view-doctor', '/admin-add-doctor', '/admin-approve-doctor',
    #               '/admin-view-doctor-specialisation'],
    #              2)

    # Doctor
    # Name
    # Description
    # Date
    # Status

    FormatText("Doctor name	Description Date	Status")
    GenerateTable('Discharge Patient', ['Name', 'Symptoms', 'Mobile', 'Discharge'])

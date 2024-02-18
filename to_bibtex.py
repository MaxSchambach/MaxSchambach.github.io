"""Convert the publications into a bibliography.bib file"""

import os
import glob
from dateutil.parser import parse


def bold_to_latex(s):
    """Replace HTML warpped bold text with Latex bold"""
    s = s.replace('<b>', '\\textbf{')
    s = s.replace('</b>', '}')
    return s

def generate_unique_key(first_author, year, description, curr_bib_keys):
    """Create BibTeX key in the format FirstAuthor:Year:Description"""
    # Here curr_bib_keys is a list containing all the bibtex keys in the existing bibliography
    unique_key_count = curr_bib_keys.count(f"{first_author}:{year}:{description}")
    if unique_key_count > 0:
        bibtex_key = f"{first_author}:{year}:{description}-{unique_key_count}"
    else:
        bibtex_key = f"{first_author}:{year}:{description}"
    curr_bib_keys_list.append(bibtex_key)
    return bibtex_key, curr_bib_keys_list

def md_to_bibtex(md_file, topic, curr_bib_keys_list):
    """Convert md publication file into bibtex entry"""

    with open(md_file, 'r') as file:
        content = file.read()
        if content.count('---') >= 2:
            start = content.index('---') + 3
            end = content.index('---', start)
            content = content[start:end].strip().split('\n')
        else:
            content = content.split('\n')

    fields_dict = {field.split(':')[0]: ':'.join(field.split(':')[1:]).strip() for field in content if ':' in field}
    fields_dict["ref-authors"] = bold_to_latex(fields_dict["ref-authors"])
    file_date_str = os.path.basename(md_file).split('-')[0:3] # get YYYY MM DD from filename
    file_date_str = '-'.join(file_date_str)
    date_obj = parse(file_date_str)

    fields_dict.update({
        'year': date_obj.year,
        'month': date_obj.month,
    })

    if 'ref-pages' in fields_dict:
        def _parse_pages(s):
            s = s.replace('-', '--')  # Replace dash
            s = s.replace('–', '--')  # Replace en-dash
            s = s.replace('—', '--')  # Replace em-dash
            return s
        fields_dict['pages'] = _parse_pages(fields_dict.pop('ref-pages'))

    fields_dict['title'] = fields_dict['title'].replace('"', '')
    fields_dict['author'] = fields_dict.pop('ref-authors')

    _ = fields_dict.pop("layout")
    _ = fields_dict.pop("ref-year")

    if 'ref-reference' in fields_dict:
        fields_dict['howpublished'] = fields_dict.pop('ref-reference')

    if 'ref-data' in fields_dict:
        fields_dict['note'] = fields_dict.pop('ref-data')

    if 'ref-link' in fields_dict:
        fields_dict['note'] = fields_dict.pop('ref-link')

    if 'ref-volume' in fields_dict:
        fields_dict['volume'] = fields_dict.pop('ref-volume')

    if 'ref-issue' in fields_dict:
        fields_dict['number'] = fields_dict.pop('ref-issue')

    if 'ref-conference' in fields_dict:
        fields_dict['journal'] = fields_dict.pop('ref-conference')

    # Write to bibtex
    type = {
        "conference": "article",
        "journal": "article",
        "dataset": "misc",
        "thesis": "misc",
        "software": "misc",
    }.get(topic)

    # Extract the first author's surname
    #first_author = fields_dict['author'].split(',')[0].split()[-1]
    first_author = fields_dict['author'].replace('\\textbf{', '').replace('}', '').split(',')[0].split()[-1]

    # Extract a short description from the title (first three words)
    description = ''.join(fields_dict['title'].split()[:3]).replace(' ', '').replace(":", "")

    # Use it like this
    bibtex_key, curr_bib_keys_list = generate_unique_key(first_author, fields_dict['year'], description, curr_bib_keys_list)
    bibtex_entry = f"@{type}{{{bibtex_key},\n"

    for field, value in fields_dict.items():
        bibtex_entry += f"  {field.lower()} = {{{value}}},\n"

    bibtex_entry += "}"

    return bibtex_entry, curr_bib_keys_list

if __name__ == "__main__":
    # replace the dir_path with your own directory path where the .md files are located
    dir_path = "./"
    os.chdir(dir_path)
    curr_bib_keys_list = []
    with open('bibliography.bib', 'w') as bibliography:
        for topic in ['conference', 'journal', 'thesis', 'dataset']:
            for file in glob.glob(os.path.join(dir_path, f"publications/{topic}/_posts/*.md")):
                content, curr_bib_keys_list = md_to_bibtex(file, topic, curr_bib_keys_list)
                bibliography.write(content)
                bibliography.write('\n\n')
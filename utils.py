import sys
import re
import os
import time 

"""
Read text from file, input: file path
"""
def readfile(filepath) :
    text = str('')
    if not os.path.exists(filepath):
        raise ValueError("text file does not exist!")
    with open(filepath, "r+", encoding='UTF-8') as file:
        line = file.readline()
        while line:
            text = text + str(line.strip())
            line = file.readline()
    return text

"""
clean the text, inclue some special icons.
"""
def clean(text):
    # 文本清理
    text = text.strip('[(),- :\'\"\n]\s*')
    text = text.replace('—', ' - ')
    text = re.sub('([A-Za-z0-9\)]{2,}\.)([A-Z]+[a-z]*)', r"\g<1> \g<2>", text, flags=re.UNICODE)
    text = re.sub('([A-Za-z0-9]{2,}\.)(\"\w+)', r"\g<1> \g<2>", text, flags=re.UNICODE)
    text = re.sub('([A-Za-z0-9]{2,}\.\/)(\w+)', r"\g<1> \g<2>", text, flags=re.UNICODE)
    text = re.sub('([[A-Z]{1}[[.]{1}[[A-Z]{1}[[.]{1}) ([[A-Z]{1}[a-z]{1,2} )', r"\g<1> . \g<2>", text, flags=re.UNICODE)
    text = re.sub('([A-Za-z]{3,}\.)([A-Z]+[a-z]+)', r"\g<1> \g<2>", text, flags=re.UNICODE)
    text = re.sub('([[A-Z]{1}[[.]{1}[[A-Z]{1}[[.]{1}) ([[A-Z]{1}[a-z]{1,2} )', r"\g<1> . \g<2>", text, flags=re.UNICODE)
    text = re.sub('([A-Za-z0-9]{2,}\.)([A-Za-z]+)', r"\g<1> \g<2>", text, flags=re.UNICODE)
    
    text = re.sub('’', "'", text, flags=re.UNICODE)           # curly apostrophe
    text = re.sub('‘', "'", text, flags=re.UNICODE)           # curly apostrophe
    text = re.sub('“', ' "', text, flags=re.UNICODE)
    text = re.sub('”', ' "', text, flags=re.UNICODE)
    text = re.sub("\|", ", ", text, flags=re.UNICODE)
    text = text.replace('\t', ' ')
    text = re.sub('…', '.', text, flags=re.UNICODE)           # elipsis
    text = re.sub('â€¦', '.', text, flags=re.UNICODE)          
    text = re.sub('â€“', '-', text)           # long hyphen
    text = re.sub('\s+', ' ', text, flags=re.UNICODE).strip()
    text = re.sub(' – ', ' . ', text, flags=re.UNICODE).strip()

    return text

"""
write the list into file. Create one file firstly, and write list.
"""
def write_list_into_file(work_path, list):
    local_time  = time.localtime()
    year = local_time.tm_year
    month = local_time.tm_mon
    day = local_time.tm_mday
    hour = local_time.tm_hour
    minute = local_time.tm_min

    file_name = "triples_" + str(year) + "_" + str(month) + "_" + str(day) + "_" + str(hour) + "_" + str(minute) + ".csv"
    if os.path.exists(work_path + file_name):
        raise ValueError("old extract triples already exist, please make sure you want to overwrite it!")
    with open(file_name, "w+", encoding='utf-8') as file:
        for triple in list:
            file.write(str(triple) + "\n")

def filter_key_words_from_triples(work_path, list, filters):
    local_time  = time.localtime()
    year = local_time.tm_year
    month = local_time.tm_mon
    day = local_time.tm_mday
    hour = local_time.tm_hour
    minute = local_time.tm_min

    filter_triples = []

    file_name = "fileter_triples_" + str(year) + "_" + str(month) + "_" + str(day) + "_" + str(hour) + "_" + str(minute) + ".csv"
    if os.path.exists(work_path + file_name):
        raise ValueError("old extract triples already exist, please make sure you want to overwrite it!")
    with open(file_name, "w+", encoding='utf-8') as file:
        for triple in list:
            for filter in filters:
                if str(triple).find(str(filter)) is not -1:
                    filter_triples.append(triple)
                    file.write(str(triple) + "\n")
                    break
        
        return filter_triples
                    
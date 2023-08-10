def item_split_by(item, string, splitby):
  item2 = item - 1
  return string.split(splitby)[item2]

def get_characters_in_range(string, start_index, end_index):
    return string[start_index:end_index]

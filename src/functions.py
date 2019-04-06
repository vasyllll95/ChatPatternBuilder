

def search_with_delete(source_list, target_list):
    for target_item in target_list:
        if target_item not in source_list:
            return False
        source_list.remove(target_item)
    return True

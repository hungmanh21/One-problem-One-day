class Solution(object):
    def check_is_sub_folder(self, current_folder, next_folder):
        current_folder_list = current_folder.split("/")
        next_folder_list = next_folder.split("/")
        if len(next_folder_list) == len(current_folder_list):
            return False
        else:
            for i in range(min(len(next_folder_list), len(current_folder_list))):
                if next_folder_list[i] != current_folder_list[i]:
                    return False
            return True

    def removeSubfolders(self, folder):
        folder.sort()
        result = []
        i = 0
        while i < len(folder):
            result.append(folder[i])
            current_folder = folder[i]
            while i+1 < len(folder) and self.check_is_sub_folder(current_folder, folder[i+1]):
                i += 1
            i += 1
        return result

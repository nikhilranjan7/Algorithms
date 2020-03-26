class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        content_dict = {}

        for i in range(len(paths)):
            text = paths[i].strip().split()
            root_path = text[0] + '/'
            for j in range(1, len(text)):
                content = text[j].split('(')
                if content[1][:-1] not in content_dict:
                    content_dict[content[1][:-1]] = [root_path + content[0]]
                else:
                    content_dict[content[1][:-1]].append(root_path + content[0])

        ans = []
        #print(content_dict)

        for i in content_dict.values():
            if len(i) > 1:
                ans.append(i)

        return ans

'''
Time complexity: O(N*M) - N is number of directories and M is max. number of files a directory
Space complexity: O(N*M) - Worst case content dict size
'''

'''
Improve points:
-
'''

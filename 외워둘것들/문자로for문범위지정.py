base_list = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
base_list.extend([chr(x) for x in range(ord('a'), ord('z') + 1)])
base_list.extend([chr(x) for x in range(ord('0'), ord('9') + 1)])
base_list.append('+')
base_list.append('/')
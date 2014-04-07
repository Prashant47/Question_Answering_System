import linecache
ans = []
def print_ans(filename, str_ln, end_ln):
	for k in range(str_ln, end_ln + 1):
		ans.append(linecache.getline(filename, k))
		k = k + 1
	return ans

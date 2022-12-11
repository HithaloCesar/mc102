import os
import sys

if len(sys.argv) < 2:
	print(f"Uso: python {os.path.basename(__file__)} path/to/labXX.py")
	sys.exit()

labfile = sys.argv[1]
if not os.path.exists(labfile):
	print("Arquivo", labfile, "não encontrado.")
	sys.exit()

i = 1
test_name = str(i).zfill(2)
in_file = "../../tests/" + test_name + "-in.txt"

while (os.path.exists(in_file)):
	out_file = "../../tests/" + test_name + "-out.txt"
	if not os.path.exists(out_file):
		print("Arquivo", out_file, "não encontrado.")
		sys.exit()

	ans_file = "../../tests/" + test_name + "-ans.txt"
	diff_file = "../../tests/" + test_name + "-diff.txt"

	os.system("python " + labfile + " < " + in_file + " > " + ans_file)
	if os.system("diff " + ans_file + " " + out_file + " > " + diff_file) == 0:
		print(f"Teste {test_name}: resultado correto.")
		os.remove(diff_file)
	else:
		print(f"Teste {test_name}: resultado incorreto.")
		os.system("cat " + diff_file)
		os.remove(diff_file)
		sys.exit()
	os.remove(ans_file)
	i += 1
	test_name = str(i).zfill(2)
	in_file = "../../tests/" + test_name + "-in.txt"

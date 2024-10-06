import subprocess
from pathlib import Path

solve_path = input('solve_path: ')
tests_path = input('tests_path: ')
tests = list(Path(tests_path).iterdir())
ok = True
for i in range(0, len(tests), 2):
    test_number = i // 2 + 1
    test_file = open(tests[i])
    answer = open(tests[i+1]).read().strip()
    result = subprocess.run(['python', solve_path], capture_output=True, stdin=test_file)
    test_file.close()
    user_answer = result.stdout.decode().strip()
    if user_answer == answer:
        print(f'test#{test_number:<{9}} {"OK"}')
    else:
        print(f'test#{test_number:<{9}} {"WRONG":>}')
        ok = False                        
print('-'*17)
if ok:
    print('OK')
else:
    print('FAILED')
    

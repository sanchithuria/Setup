import subprocess

def test_dynamic_input():
    result = subprocess.run(
        ['python', 'python.py'],
        input='4\n',
        capture_output=True,
        text=True
    )

    assert result.returncode == 0

    expected_output = "1\n2\n3\n4"
    assert result.stdout.strip().endswith(expected_output)

from io import StringIO


def count_lines(stream):
    return sum(1 for line in stream)


string_stream = StringIO("first\nsecond\nthird")
lines_in_string = count_lines(string_stream)
print(f"Количество строк в StringIO: {lines_in_string}")

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("line 1\nline 2\nline 3\nline 4")

with open("data.txt", "r", encoding="utf-8") as file_stream:
    lines_in_file = count_lines(file_stream)
    print(f"Количество строк в реальном файле: {lines_in_file}")

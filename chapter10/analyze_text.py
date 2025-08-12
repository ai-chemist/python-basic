from pathlib import Path

f_path = Path('frankenstein.txt')
m_path = Path('moby_dick.txt')

def count_words(path):
    """Count the number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print("File not found")
        # pass 를 사용하면 예외 발생 시 조용히 넘어감
        pass
    else:
        words = contents.split()
        print(f"{str(path).replace('.txt', '').title()} has {len(words)} words")

count_words(f_path)
count_words(m_path)
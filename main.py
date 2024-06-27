def main():
    # Đường dẫn đến tệp frankenstein.txt
    path_to_file = 'books/frankenstein.txt'
    
    # Mở và đọc nội dung tệp
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    
    # Đếm số từ trong văn bản
    word_count = count_words(file_contents)
    print(f"Number of words: {word_count}")
    
    # Đếm số lần xuất hiện của mỗi ký tự
    character_count = count_characters(file_contents)
    print("Character counts:")
    for char, count in character_count.items():
        print(f"Number of {char} is : {count} times")

    # Ghi kết quả vào tệp
    with open('output.txt', 'w') as f:
        f.write(f"Number of words: {word_count}\n")
        f.write("Character counts:\n")
        for char, count in character_count.items():
            f.write(f"Number of {char} is : {count} times\n")
    
    print("Results have been written to output.txt")    

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    # Chuyển đổi văn bản thành chữ thường
    text = text.lower()
    
    # Khởi tạo từ điển để đếm ký tự
    char_count = {}
    
    # Đếm số lần xuất hiện của mỗi ký tự
    for char in text:
        if char.isalpha():  # Chỉ đếm các ký tự chữ cái
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()

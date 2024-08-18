import os

def linecount(m_dir, m_filetype):
    m_lines = 0

    for subdir, _, files in os.walk(m_dir):
        for file in files:
            if file.endswith("." + m_filetype):
                file_path = os.path.join(subdir, file)

                try: #UTF-8
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        m_lines += len(lines)
                except UnicodeDecodeError: #non UTF-8
                    try:
                        with open(file_path, 'r', encoding='latin-1') as f:
                            lines = f.readlines()
                            m_lines += len(lines)
                    except UnicodeDecodeError: #error
                        print(f"Skipping file due to encoding issues: {file_path}")

    return m_lines

if __name__ == "__main__":
    path = input("Enter the directory path= ")
    filetype = input("Enter the extension of the files you want to count (without the dot .)= ")
    line_count = linecount(path, filetype)
    
    print(f"Total number of lines in .{filetype} files={line_count}")

import os

initial_path="./test"

def create_svg_from_txt(path):    
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                if not entry.name.startswith('.') and entry.name.endswith('.txt'):
                    filepath = path + '/' +entry.name    
                    svg_code = open(filepath, "r").read()
                    svg_file = open(filepath.replace('.txt', '.svg'), "w")
                    svg_file.write(str(svg_code))
                    svg_file.close()
            else:                
                create_svg_from_txt(entry.path)

create_svg_from_txt(initial_path)
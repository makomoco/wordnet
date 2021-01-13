def format_text(file,new_file): 
    f = open(file)
    ff = open(new_file,’w’) 
    line = f.readline() 
    while line:
        line = line.upper()
        line = re.sub(r’[^A-Z\u3000-\u303F\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF\s]’,’、’,line) 
        ff.write(line)
        line = f.readline() 
    f.close()
    ff.close()